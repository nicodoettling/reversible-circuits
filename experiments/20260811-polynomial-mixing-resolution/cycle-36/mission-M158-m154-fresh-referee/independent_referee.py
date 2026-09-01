#!/usr/bin/env python3
"""Clean-room referee checks for frozen M154.

The script never imports or executes an M154/predecessor module.  It verifies
the assigned frozen bytes, checks the universal Hurwitz word on literal group
tuples, reconstructs the complete d=3 framing split, identifies the d=4
S4/V4 block system and accepted DPS witness, and caps d=5 at quotient-orbit
enumeration and primitivity.  It deliberately does not compute the d=5 group
order or enumerate its elements.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path

from sympy.combinatorics import Permutation as SymPermutation
from sympy.combinatorics import PermutationGroup


Perm = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]


M154_EXPECTED = {
    "report.md": "6421f55bccf2c6750f21a7cf9a236f8811c06f5759170d4ca3acae79c9b5d806",
    "inner_nielsen_voltage_reduction.md": "e689fec00762b773d56030640aff7af21053cb63901c47571e3c9b33ce48d958",
    "hurwitz_framing_audit.py": "0292268cbad8c0c322c440f4ca6596ebfcc3fd3e5b94c500f616859c208dccfc",
    "results.json": "13ee821c42f01cc040f4c9a335b6e2acbf38522834e83195dca17a895246f1be",
    "d4_exceptional_block_audit.py": "e5cf3ff0d660b5a5e62325c87c8a7c40f4b3a1639d95dd787435f97353947a68",
    "d4_results.json": "9d55fb82af30ccfcfc0a39e63c41a77c05518cc79888249678ffbed8183e3cfa",
    "freeze_manifest.md": "7adf2270a89ab870335417305ba5db6fb577ded29721a30dc38234eea07b07fa",
    "SHA256SUMS": "b5c7273819a6d247836dc596723efb438cb91ae310ced670ad57738a3bb0ba04",
}


def compose(p: Perm, q: Perm) -> Perm:
    """p*q, with (p*q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def invert(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def perm_sign(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) & 1


def transposition(d: int, edge: Edge) -> Perm:
    p = list(range(d))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def eval_word(d: int, word: Word) -> Perm:
    ans = tuple(range(d))
    for edge in word:
        ans = compose(ans, transposition(d, edge))
    return ans


def support_connected(d: int, word: Word) -> bool:
    graph = [set() for _ in range(d)]
    for a, b in word:
        graph[a].add(b)
        graph[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        a = todo.pop()
        for b in graph[a] - seen:
            seen.add(b)
            todo.append(b)
    return len(seen) == d


def edge_relabel(edge: Edge, rho: Perm) -> Edge:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def word_relabel(word: Word, rho: Perm) -> Word:
    return tuple(edge_relabel(edge, rho) for edge in word)


def canonical(word: Word, relabelings: tuple[Perm, ...]) -> Word:
    return min(word_relabel(word, rho) for rho in relabelings)


def edge_conjugate(edge: Edge, by_edge: Edge) -> Edge:
    return edge_relabel(edge, transposition(max(max(edge), max(by_edge)) + 1, by_edge))


def hurwitz_edge(word: Word, slot: int, direction: int = 1) -> Word:
    a, b = word[slot], word[slot + 1]
    d = 1 + max(max(edge) for edge in word)
    out = list(word)
    if direction == 1:
        out[slot : slot + 2] = (b, edge_relabel(a, transposition(d, b)))
    elif direction == -1:
        out[slot : slot + 2] = (edge_relabel(b, transposition(d, a)), a)
    else:
        raise ValueError(direction)
    return tuple(out)


def hurwitz_perm(word: tuple[Perm, ...], slot: int, direction: int) -> tuple[Perm, ...]:
    a, b = word[slot], word[slot + 1]
    out = list(word)
    if direction == 1:
        out[slot : slot + 2] = (b, compose(compose(invert(b), a), b))
    elif direction == -1:
        out[slot : slot + 2] = (compose(compose(a, b), invert(a)), a)
    else:
        raise ValueError(direction)
    return tuple(out)


def apply_braid(word: tuple[Perm, ...], braid: tuple[tuple[int, int], ...]) -> tuple[Perm, ...]:
    for slot, direction in braid:
        word = hurwitz_perm(word, slot, direction)
    return word


def inner_conjugation_braid(m: int, factor_slot: int) -> tuple[tuple[int, int], ...]:
    transport = tuple((j, -1) for j in range(factor_slot, m - 1))
    last_loop = tuple((j, 1) for j in range(m - 2, -1, -1)) + tuple(
        (j, 1) for j in range(m - 1)
    )
    undo = tuple((j, 1) for j in range(m - 2, factor_slot - 1, -1))
    return transport + last_loop + undo


def conjugate_right(word: tuple[Perm, ...], p: Perm) -> tuple[Perm, ...]:
    pinv = invert(p)
    return tuple(compose(compose(pinv, x), p) for x in word)


def inverse_braid(braid: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    return tuple((slot, -direction) for slot, direction in reversed(braid))


def brute_target(d: int, m: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    return tuple(
        word
        for word in itertools.product(edges, repeat=m)
        if eval_word(d, word) == identity and support_connected(d, word)
    )


def action_cycle_histogram(action: tuple[int, ...]) -> dict[str, int]:
    unseen = set(range(len(action)))
    counts = Counter()
    while unseen:
        x = min(unseen)
        length = 0
        while x in unseen:
            unseen.remove(x)
            x = action[x]
            length += 1
        counts[length] += 1
    return {str(k): counts[k] for k in sorted(counts)}


def action_sign(action: tuple[int, ...]) -> int:
    return (len(action) - sum(action_cycle_histogram(action).values())) & 1


def orbit(seed, actions):
    seen = {seed}
    todo = deque([seed])
    while todo:
        point = todo.popleft()
        for action in actions:
            if isinstance(point, tuple):
                nxt = tuple(action[x] for x in point)
            else:
                nxt = action[point]
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def verify_frozen_bytes(root: Path) -> dict[str, str]:
    m154 = root / "experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M154-common-parity-hurwitz-transitivity"
    observed = {name: hashlib.sha256((m154 / name).read_bytes()).hexdigest() for name in M154_EXPECTED}
    assert observed == M154_EXPECTED
    return observed


def universal_braid_audit() -> dict:
    failures = []
    length_rows = []
    physical = brute_target(3, 4)
    for edges in physical:
        word = tuple(transposition(3, edge) for edge in edges)
        for i, factor in enumerate(word):
            braid = inner_conjugation_braid(len(word), i)
            if apply_braid(word, braid) != conjugate_right(word, factor):
                failures.append(["d3", edges, i])
            expected_inverse = tuple(
                compose(compose(factor, x), invert(factor)) for x in word
            )
            if apply_braid(word, inverse_braid(braid)) != expected_inverse:
                failures.append(["d3_inverse", edges, i])
        
    s4 = tuple(itertools.permutations(range(4)))
    x1 = transposition(4, (0, 1))
    x2 = compose(transposition(4, (0, 1)), transposition(4, (1, 2)))
    x3 = transposition(4, (0, 3))
    prefix = compose(compose(x1, x2), x3)
    general = (x1, x2, x3, invert(prefix))
    assert math.prod([1]) == 1
    product = tuple(range(4))
    for x in general:
        product = compose(product, x)
    assert product == tuple(range(4)) and x2 in s4
    for i, factor in enumerate(general):
        braid = inner_conjugation_braid(len(general), i)
        if apply_braid(general, braid) != conjugate_right(general, factor):
            failures.append(["noninvolutive_S4", i])
        length_rows.append(
            {
                "factor_slot": i + 1,
                "observed_length": len(braid),
                "formula": 2 * (len(general) - i - 1) + 2 * (len(general) - 1),
                "at_most_4m_minus_4": len(braid) <= 4 * len(general) - 4,
            }
        )
    return {
        "chronological_sequence": "R_(m-1),...,R_1,R_1,...,R_(m-1), after inverse-Hurwitz transport",
        "d3_factor_checks": len(physical) * 4,
        "noninvolutive_group_check": "S4 product-one tuple containing a 3-cycle",
        "failures": failures,
        "last_factor_loop_length": 2 * (len(general) - 1),
        "per_factor_length_rows": length_rows,
        "claimed_per_generator_bound": "4m-4",
    }


def d3_framing_audit() -> dict:
    d, m = 3, 4
    relabelings = tuple(itertools.permutations(range(d)))
    words = tuple(sorted(brute_target(d, m)))
    index = {word: i for i, word in enumerate(words)}
    classes = tuple(sorted({canonical(word, relabelings) for word in words}))
    class_index = {word: i for i, word in enumerate(classes)}
    word_class = tuple(class_index[canonical(word, relabelings)] for word in words)
    actions = tuple(
        tuple(index[hurwitz_edge(word, slot, 1)] for word in words)
        for slot in range(m - 1)
    )
    physical_group = PermutationGroup([SymPermutation(list(a)) for a in actions])
    quotient_actions = tuple(
        tuple(class_index[canonical(hurwitz_edge(word, slot, 1), relabelings)] for word in classes)
        for slot in range(m - 1)
    )
    quotient_group = PermutationGroup([SymPermutation(list(a)) for a in quotient_actions])
    pair_states = tuple(
        (i, j)
        for i in range(len(words))
        for j in range(len(words))
        if word_class[i] != word_class[j]
    )
    remaining = set(pair_states)
    pair_orbits = []
    while remaining:
        component = orbit(min(remaining), actions)
        assert component <= remaining
        pair_orbits.append(component)
        remaining -= component
    pair_orbits.sort(key=lambda component: min(component))

    source = min(pair_states)
    source_orbit = next(component for component in pair_orbits if source in component)
    parity_counts = defaultdict(lambda: {"total": 0, "reachable": 0})
    conjugate_targets = set()
    for rho, sigma in itertools.product(relabelings, repeat=2):
        target = (
            index[word_relabel(words[source[0]], rho)],
            index[word_relabel(words[source[1]], sigma)],
        )
        conjugate_targets.add(target)
        label = f"{perm_sign(rho)}{perm_sign(sigma)}"
        parity_counts[label]["total"] += 1
        parity_counts[label]["reachable"] += target in source_orbit
    quotient_pair_orbit = orbit((0, 1), quotient_actions)
    assert len(conjugate_targets) == 36
    assert sorted(map(len, pair_orbits)) == [216, 216]
    assert len(quotient_pair_orbit) == 12
    assert {key: row["reachable"] for key, row in parity_counts.items()} == {
        "00": 9,
        "01": 0,
        "10": 0,
        "11": 9,
    }
    assert all(perm_sign(a) == 0 for a in quotient_actions)
    return {
        "physical_words": len(words),
        "free_global_classes": len(classes),
        "global_class_sizes": dict(Counter(map(str, Counter(word_class).values()))),
        "literal_action_image_order": physical_group.order(),
        "quotient_action_image_order": quotient_group.order(),
        "quotient_image_identification": "A4: order 12 and all degree-4 generators even",
        "quotient_ordered_distinct_pair_orbit": len(quotient_pair_orbit),
        "generating_ordered_pair_states": len(pair_states),
        "literal_pair_orbit_sizes": sorted(map(len, pair_orbits)),
        "fixed_absolute_pair_conjugates": len(conjugate_targets),
        "relative_parity_reachability": dict(sorted(parity_counts.items())),
        "conclusion": "exactly two literal framed orbits, indexed by F2^2/Delta",
    }


MATCHINGS_4 = (
    frozenset(((0, 1), (2, 3))),
    frozenset(((0, 2), (1, 3))),
    frozenset(((0, 3), (1, 2))),
)


def exceptional_action(rho: Perm) -> Perm:
    images = []
    for matching in MATCHINGS_4:
        moved = frozenset(edge_relabel(edge, rho) for edge in matching)
        images.append(MATCHINGS_4.index(moved))
    return tuple(images)


def projected_edge(edge: Edge) -> Edge:
    p = exceptional_action(transposition(4, edge))
    moved = tuple(i for i in range(3) if p[i] != i)
    assert len(moved) == 2
    return moved


def projected_word(word: Word) -> Word:
    return tuple(projected_edge(edge) for edge in word)


def prufer_trees(d: int):
    for code in itertools.product(range(d), repeat=d - 2):
        degree = [1] * d
        for v in code:
            degree[v] += 1
        edges = []
        for v in code:
            leaf = next(x for x in range(d) if degree[x] == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        edges.append(tuple(i for i in range(d) if degree[i] == 1))
        yield frozenset(edges)


def rooted_parents(tree: frozenset[Edge], root: int) -> dict[int, int]:
    graph = [set() for _ in range(root + 1)]
    for a, b in tree:
        graph[a].add(b)
        graph[b].add(a)
    parent = {root: -1}
    todo = [root]
    while todo:
        a = todo.pop()
        for b in graph[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    return parent


def dps_word(tree: frozenset[Edge], order: tuple[int, ...], d: int) -> Word:
    """Independent implementation of the accepted plus-mirror DPS closure."""
    m, root = 2 * d - 2, d - 1
    parent = rooted_parents(tree, root)
    incidence = defaultdict(dict)
    first_black = {}
    for black in range(root):
        for label, white in zip(order[2 * black : 2 * black + 2], (black, parent[black])):
            bn, wn = ("b", black), ("w", white)
            incidence[bn][label] = wn
            incidence[wn][label] = bn
            first_black[label] = black

    start = (("w", 0), 0)
    state = start
    visited = set()
    boundary = []
    while state not in visited:
        visited.add(state)
        node, incoming = state
        nxt_label = (incoming + (1 if node[0] == "w" else -1)) % m
        if nxt_label in incidence[node]:
            boundary.append(("arc",))
            state = (incidence[node][nxt_label], nxt_label)
        else:
            boundary.append(("stub", node[0], node[1], nxt_label))
            state = (node, nxt_label)
    assert state == start and len(boundary) == (2 * d - 1) * m

    second_black = {}
    while True:
        stub_positions = [i for i, token in enumerate(boundary) if token[0] == "stub"]
        chosen = None
        for k, white_pos in enumerate(stub_positions):
            black_pos = stub_positions[(k + 1) % len(stub_positions)]
            if boundary[white_pos][1] == "w" and boundary[black_pos][1] == "b":
                chosen = white_pos, black_pos
                break
        if chosen is None:
            break
        white_pos, black_pos = chosen
        boundary = boundary[white_pos:] + boundary[:white_pos]
        black_pos = (black_pos - white_pos) % len(boundary)
        white, black = boundary[0], boundary[black_pos]
        assert white[3] == black[3]
        arc_distance = sum(token[0] == "arc" for token in boundary[1:black_pos])
        assert arc_distance in (1, 3)
        if arc_distance == 3:
            second_black[white[3]] = black[2]
        boundary = [("arc",)] + boundary[black_pos + 1 :]
    survivors = [token for token in boundary if token[0] == "stub"]
    assert len(survivors) == m and all(token[1] == "w" for token in survivors)
    return tuple(
        tuple(sorted((first_black[label], second_black.get(label, root))))
        for label in range(m)
    )


def swap_values(order: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    return tuple(b if x == a else a if x == b else x for x in order)


def dps_witness_check(sources: tuple[Word, Word], targets: tuple[Word, Word]) -> dict:
    preimages = {source: [] for source in sources}
    for tree in prufer_trees(4):
        for order in itertools.permutations(range(6)):
            word = dps_word(tree, order, 4)
            if word in preimages:
                preimages[word].append((tree, order))
    rows = []
    for source, target in zip(sources, targets):
        images = {
            dps_word(tree, swap_values(order, 0, 1), 4)
            for tree, order in preimages[source]
        }
        rows.append(
            {
                "source_preimages": len(preimages[source]),
                "root_independent_tau1_images": len(images),
                "tau1_equals_declared_target": images == {target},
            }
        )
    assert all(row == {
        "source_preimages": 4,
        "root_independent_tau1_images": 1,
        "tau1_equals_declared_target": True,
    } for row in rows)
    return {"rows": rows, "all_declared_endpoints_verified": True}


def paired_group_order(left: Word, right: Word) -> int:
    generators = tuple(
        (transposition(4, a), transposition(4, b)) for a, b in zip(left, right)
    )
    identity = (tuple(range(4)), tuple(range(4)))
    seen = {identity}
    todo = deque([identity])
    while todo:
        x, y = todo.popleft()
        for a, b in generators:
            nxt = (compose(x, a), compose(y, b))
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return len(seen)


def factor_integer(n: int) -> dict[str, int]:
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[str(p)] = factors.get(str(p), 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[str(n)] = factors.get(str(n), 0) + 1
    return factors


def d4_exceptional_audit() -> dict:
    s4 = tuple(itertools.permutations(range(4)))
    s3 = tuple(itertools.permutations(range(3)))
    hom_failures = 0
    for p, q in itertools.product(s4, repeat=2):
        hom_failures += exceptional_action(compose(p, q)) != compose(
            exceptional_action(p), exceptional_action(q)
        )
    image = {exceptional_action(p) for p in s4}
    kernel = {p for p in s4 if exceptional_action(p) == tuple(range(3))}
    edge_images = Counter(projected_edge(edge) for edge in itertools.combinations(range(4), 2))
    assert hom_failures == 0 and len(image) == 6 and len(kernel) == 4
    assert set(edge_images.values()) == {2}

    z4 = brute_target(4, 6)
    z36 = brute_target(3, 6)
    q4 = tuple(sorted({canonical(word, s4) for word in z4}))
    q36 = tuple(sorted({canonical(word, s3) for word in z36}))
    q4_index = {word: i for i, word in enumerate(q4)}
    phi = tuple(canonical(projected_word(word), s3) for word in q4)
    product_failures = sum(eval_word(3, projected_word(word)) != tuple(range(3)) for word in q4)
    connected_failures = sum(not support_connected(3, projected_word(word)) for word in q4)
    phi_fibers = defaultdict(set)
    for i, key in enumerate(phi):
        phi_fibers[key].add(i)
    assert len(z4) == 2880 and len(q4) == 120 and len(q36) == 40
    assert set(phi_fibers) == set(q36) and set(map(len, phi_fibers.values())) == {3}
    assert product_failures == connected_failures == 0

    actions = tuple(
        tuple(q4_index[canonical(hurwitz_edge(word, slot, 1), s4)] for word in q4)
        for slot in range(5)
    )
    group = PermutationGroup([SymPermutation(list(action)) for action in actions])
    algebraic_partition = {frozenset(block) for block in phi_fibers.values()}
    labels = group.minimal_blocks(randomized=False)[0]
    computed = defaultdict(set)
    for point, label in enumerate(labels):
        computed[label].add(point)
    computed_partition = {frozenset(block) for block in computed.values()}
    block_mapping_failures = 0
    for action in actions:
        for block in algebraic_partition:
            image_block = frozenset(action[x] for x in block)
            block_mapping_failures += image_block not in algebraic_partition
    order = int(group.order())
    subdegrees = sorted(len(o) for o in group.stabilizer(0).orbits())
    assert group.is_transitive() and not group.is_primitive()
    assert computed_partition == algebraic_partition and block_mapping_failures == 0

    A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
    sources = ((A, B, B, A, C, C), (A, B, B, C, A, C))
    targets = ((A, D, B, E, D, C), (A, D, B, C, E, C))
    witness_valid = [
        eval_word(4, word) == tuple(range(4)) and support_connected(4, word)
        for word in sources + targets
    ]
    source_keys = [canonical(projected_word(word), s3) for word in sources]
    target_keys = [canonical(projected_word(word), s3) for word in targets]
    conjugacy = {
        "source_pair_globally_conjugate": any(word_relabel(sources[0], p) == sources[1] for p in s4),
        "target_pair_globally_conjugate": any(word_relabel(targets[0], p) == targets[1] for p in s4),
    }
    paired_orders = {
        "source": paired_group_order(*sources),
        "target": paired_group_order(*targets),
    }
    dps = dps_witness_check(sources, targets)
    assert all(witness_valid)
    assert source_keys[0] == source_keys[1] and target_keys[0] != target_keys[1]
    assert conjugacy == {
        "source_pair_globally_conjugate": False,
        "target_pair_globally_conjugate": False,
    }
    assert paired_orders == {"source": 96, "target": 288}
    return {
        "exceptional_homomorphism": {
            "homomorphism_failures_over_S4_squared": hom_failures,
            "image_order": len(image),
            "kernel_order": len(kernel),
            "kernel_cycle_types": sorted(
                [action_cycle_histogram(p) for p in kernel], key=lambda row: tuple(row.items())
            ),
            "transposition_preimage_multiplicities": {
                str(key): edge_images[key] for key in sorted(edge_images)
            },
        },
        "physical_words": len(z4),
        "absolute_quotient_degree": len(q4),
        "projected_absolute_classes": len(q36),
        "phi_fiber_size_histogram": dict(Counter(map(str, map(len, phi_fibers.values())))),
        "projected_product_failures": product_failures,
        "projected_connectedness_failures": connected_failures,
        "connectedness_reason": "a single projected edge-label would lift to one disjoint S4 edge-pair, contradicting connected support",
        "quotient_action": {
            "order": order,
            "order_factorization": factor_integer(order),
            "transitive": group.is_transitive(),
            "primitive": group.is_primitive(),
            "subdegrees": subdegrees,
            "minimal_block_histogram": dict(Counter(map(str, map(len, computed_partition)))),
            "sympy_minimal_blocks_equal_phi_fibers": computed_partition == algebraic_partition,
            "generator_block_mapping_failures": block_mapping_failures,
        },
        "accepted_rank4_witness": {
            "all_four_words_valid": all(witness_valid),
            "dps_tau1_endpoint_check": dps,
            "source_same_phi_fiber": source_keys[0] == source_keys[1],
            "target_same_phi_fiber": target_keys[0] == target_keys[1],
            "therefore_common_literal_braid_obstructed": source_keys[0] == source_keys[1] and target_keys[0] != target_keys[1],
            "global_conjugacy": conjugacy,
            "paired_subgroup_orders": paired_orders,
        },
    }


def quotient_component(d: int) -> tuple[tuple[Word, ...], tuple[tuple[int, ...], ...]]:
    relabelings = tuple(itertools.permutations(range(d)))
    m = 2 * d - 2
    star = tuple(edge for v in range(1, d) for edge in ((0, v), (0, v)))
    assert eval_word(d, star) == tuple(range(d)) and support_connected(d, star)
    start = canonical(star, relabelings)
    states = {start}
    todo = deque([start])
    canonical_cache = {}

    def canon(word):
        if word not in canonical_cache:
            canonical_cache[word] = canonical(word, relabelings)
        return canonical_cache[word]

    while todo:
        word = todo.popleft()
        for slot in range(m - 1):
            for direction in (1, -1):
                nxt = canon(hurwitz_edge(word, slot, direction))
                if nxt not in states:
                    states.add(nxt)
                    todo.append(nxt)
    ordered = tuple(sorted(states))
    index = {word: i for i, word in enumerate(ordered)}
    actions = tuple(
        tuple(index[canon(hurwitz_edge(word, slot, 1))] for word in ordered)
        for slot in range(m - 1)
    )
    return ordered, actions


def d5_capped_audit() -> dict:
    states, actions = quotient_component(5)
    expected = 5 ** 2 * math.factorial(8) // math.factorial(5)
    assert len(states) == expected == 8400
    group = PermutationGroup([SymPermutation(list(action)) for action in actions])
    rows = [
        {
            "slot": i + 1,
            "cycle_histogram": action_cycle_histogram(action),
            "parity": action_sign(action),
        }
        for i, action in enumerate(actions)
    ]
    transitive = group.is_transitive()
    primitive = group.is_primitive()
    assert transitive and primitive
    assert all(row["parity"] == 0 for row in rows)
    assert {tuple(sorted(row["cycle_histogram"].items())) for row in rows} == {
        (("1", 660), ("2", 1440), ("3", 1620))
    }
    return {
        "component_size": len(states),
        "accepted_DPS_quotient_count": expected,
        "transitive": transitive,
        "primitive": primitive,
        "positive_generators": len(actions),
        "positive_generator_rows": rows,
        "group_order_computed": False,
        "scope": "exact finite orbit/primitivity check only; no alternating-image or asymptotic inference",
    }


def main() -> None:
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    payload = {
        "experiment": "M158 clean-room referee of frozen M154",
        "target": "literal/inner/absolute Hurwitz orbit reductions; not a sampler or gap claim",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "hurwitz_convention": "R_j(a,b)=(b,b^-1*a*b), chronological order",
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "python": platform.python_version(),
        "dependencies": {"sympy": __import__("sympy").__version__},
        "seed": None,
        "command": "python3 -B independent_referee.py",
        "frozen_hashes_verified": verify_frozen_bytes(root),
        "universal_inner_conjugation": universal_braid_audit(),
        "d3_framing": d3_framing_audit(),
        "d4_exceptional_block": d4_exceptional_audit(),
        "d5_capped_quotient": d5_capped_audit(),
        "universal_claim_note": "Universal claims are decided by proof audit; finite rows calibrate conventions and exceptions only.",
    }
    assert payload["universal_inner_conjugation"]["failures"] == []
    (here / "independent_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "d3_orbits": payload["d3_framing"]["literal_pair_orbit_sizes"],
        "d4_blocks_equal": payload["d4_exceptional_block"]["quotient_action"]["sympy_minimal_blocks_equal_phi_fibers"],
        "d5": {
            "size": payload["d5_capped_quotient"]["component_size"],
            "primitive": payload["d5_capped_quotient"]["primitive"],
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
