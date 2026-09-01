#!/usr/bin/env python3
"""Clean-room bounded referee checks for frozen M141.

The script imports no predecessor code or result payload.  It verifies the
frozen bytes, reconstructs the rooted DPS involutions only at d=3,4, checks
the actual rank-three matching statistics and rank-four witness, constructs
the abstract A3 counterexample, and exactly checks simplicity of A5 and A6.
The universal multisource theorem is audited by proof, not extrapolated from
these finite computations.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[Edge, ...]
Node = tuple[str, int]
Token = tuple[str, str | None, int | None, int | None]

FROZEN_HASHES = {
    "report.md": "ebda7181e031603f598648d2409f8a484645022f24acd34e92ef5813459afb87",
    "multisource_subgroup_theorem.md": "7c9588dc64e3731a90e3e59bbe60a4d15dc8a42c4f98ce7ed60c386c7e8b8678",
    "multisource_subgroup_audit.py": "44f8fd167808bb41d2823bb10943951d6404d88aa4530697760a914b1e321d93",
    "results.json": "548ddf460a9184ebdc36c449ba35e8e2b8c3719b4994200808afa8868590c241",
    "freeze_manifest.md": "b45f4a80ca8745a9f7e6291b5118b27a64e22040a7799f872773624aff671e62",
    "SHA256SUMS": "9aa52349d288f04b7f46895cf7fe01373dcea807abf69892ef3ccea705acc057",
}


def compose(left: Perm, right: Perm) -> Perm:
    """Return left*right under (pq)(x)=p(q(x))."""
    return tuple(left[right[x]] for x in range(len(left)))


def invert(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def transposition(d: int, edge: Edge) -> Perm:
    p = list(range(d))
    a, b = edge
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def parity(p: Perm) -> int:
    inversions = sum(
        p[a] > p[b] for a in range(len(p)) for b in range(a + 1, len(p))
    )
    return inversions & 1


def word_product(d: int, word: Word) -> Perm:
    value = tuple(range(d))
    for edge in word:
        value = compose(value, transposition(d, edge))
    return value


def connected(d: int, word: Word) -> bool:
    neighbors = [set() for _ in range(d)]
    for a, b in word:
        neighbors[a].add(b)
        neighbors[b].add(a)
    reached = {0}
    active = [0]
    while active:
        x = active.pop()
        for y in neighbors[x] - reached:
            reached.add(y)
            active.append(y)
    return len(reached) == d


def relabel(word: Word, rho: Perm) -> Word:
    return tuple(tuple(sorted((rho[a], rho[b]))) for a, b in word)


def target_words(d: int) -> tuple[Word, ...]:
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    return tuple(
        word
        for word in itertools.product(edges, repeat=2 * d - 2)
        if word_product(d, word) == identity and connected(d, word)
    )


def prufer_trees(d: int):
    for code in itertools.product(range(d), repeat=max(0, d - 2)):
        degrees = [1] * d
        for x in code:
            degrees[x] += 1
        tree: list[Edge] = []
        for x in code:
            leaf = next(y for y, degree in enumerate(degrees) if degree == 1)
            tree.append(tuple(sorted((leaf, x))))
            degrees[leaf] -= 1
            degrees[x] -= 1
        leaves = tuple(y for y, degree in enumerate(degrees) if degree == 1)
        assert len(leaves) == 2
        tree.append(tuple(sorted(leaves)))
        yield frozenset(tree)


def rooted_parents(tree: frozenset[Edge], root: int) -> dict[int, int]:
    neighbors = [[] for _ in range(root + 1)]
    for a, b in tree:
        neighbors[a].append(b)
        neighbors[b].append(a)
    parent = {root: -1}
    active = [root]
    while active:
        x = active.pop()
        for y in neighbors[x]:
            if y not in parent:
                parent[y] = x
                active.append(y)
    return parent


def hairy_incidence(tree: frozenset[Edge], order: tuple[int, ...], d: int):
    root = d - 1
    parent = rooted_parents(tree, root)
    incidence: dict[Node, dict[int, Node]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for black in range(root):
        left_label, right_label = order[2 * black : 2 * black + 2]
        for label, white in ((left_label, black), (right_label, parent[black])):
            bn = ("b", black)
            wn = ("w", white)
            incidence[bn][label] = wn
            incidence[wn][label] = bn
            first_black[label] = black
    return incidence, first_black


def boundary_tokens(incidence: dict[Node, dict[int, Node]], d: int) -> list[Token]:
    modulus = 2 * d - 2
    start = (("w", 0), 0)
    state = start
    seen = set()
    tokens: list[Token] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        label = (incoming + (1 if vertex[0] == "w" else -1)) % modulus
        if label in incidence[vertex]:
            tokens.append(("arc", None, None, label))
            state = (incidence[vertex][label], label)
        else:
            tokens.append(("stub", vertex[0], vertex[1], label))
            state = (vertex, label)
    assert state == start and len(tokens) == (2 * d - 1) * modulus
    return tokens


def close_boundary(tokens: list[Token], d: int) -> dict[int, int]:
    work = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        stubs = [j for j, token in enumerate(work) if token[0] == "stub"]
        chosen = None
        for position, white_index in enumerate(stubs):
            black_index = stubs[(position + 1) % len(stubs)]
            if work[white_index][1] == "w" and work[black_index][1] == "b":
                chosen = (white_index, black_index)
                break
        if chosen is None:
            break
        white_index, black_index = chosen
        work = work[white_index:] + work[:white_index]
        black_index = (black_index - white_index) % len(work)
        white, black = work[0], work[black_index]
        assert white[0] == black[0] == "stub" and white[3] == black[3]
        distance = sum(token[0] == "arc" for token in work[1:black_index])
        assert distance in (1, 3)
        if distance == 3:
            assert white[3] not in second_black
            assert black[2] is not None and white[3] is not None
            second_black[white[3]] = black[2]
        work = [("arc", None, None, None)] + work[black_index + 1 :]
    survivors = [token for token in work if token[0] == "stub"]
    assert len(survivors) == 2 * d - 2
    assert all(token[1] == "w" for token in survivors)
    return second_black


def dps_word(tree: frozenset[Edge], order: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_incidence(tree, order, d)
    second_black = close_boundary(boundary_tokens(incidence, d), d)
    root = d - 1
    result = tuple(
        tuple(sorted((first_black[label], second_black.get(label, root))))
        for label in range(2 * d - 2)
    )
    assert all(a != b for a, b in result)
    return result


def swap_values(order: tuple[int, ...], adjacent: int) -> tuple[int, ...]:
    return tuple(
        adjacent + 1 if x == adjacent else adjacent if x == adjacent + 1 else x
        for x in order
    )


def reconstruct_dps(d: int):
    fibers: dict[Word, list[tuple[frozenset[Edge], tuple[int, ...]]]] = defaultdict(list)
    m = 2 * d - 2
    for tree in prufer_trees(d):
        for order in itertools.permutations(range(m)):
            word = dps_word(tree, order, d)
            assert word_product(d, word) == tuple(range(d)) and connected(d, word)
            fibers[word].append((tree, order))
    brute = tuple(sorted(target_words(d)))
    assert set(brute) == set(fibers) and set(map(len, fibers.values())) == {d}
    tau: list[dict[Word, Word]] = []
    for adjacent in range(m - 1):
        action: dict[Word, Word] = {}
        for word in brute:
            images = {
                dps_word(tree, swap_values(order, adjacent), d)
                for tree, order in fibers[word]
            }
            assert len(images) == 1
            action[word] = next(iter(images))
        assert set(action.values()) == set(brute)
        assert all(action[action[word]] == word for word in brute)
        tau.append(action)
    return brute, fibers, tau


def canonical(word: Word, group: tuple[Perm, ...]) -> Word:
    return min(relabel(word, rho) for rho in group)


def orbit_blocks(words: tuple[Word, ...], group: tuple[Perm, ...]):
    blocks: dict[Word, list[Word]] = defaultdict(list)
    for word in words:
        blocks[canonical(word, group)].append(word)
    return blocks


def perfect_matching_decomposition(edges, degree: int) -> list[tuple[int, ...]]:
    left_vertices = tuple(sorted({left for left, _right in edges}))
    right_vertices = tuple(sorted({right for _left, right in edges}))
    unused = set(range(len(edges)))
    answer = []
    for _color in range(degree):
        adjacency = {left: [] for left in left_vertices}
        for edge_id in sorted(unused):
            left, right = edges[edge_id]
            adjacency[left].append((right, edge_id))
        occupied = {}

        def augment(left, visited):
            for right, edge_id in adjacency[left]:
                if right in visited:
                    continue
                visited.add(right)
                if right not in occupied or augment(occupied[right][0], visited):
                    occupied[right] = (left, edge_id)
                    return True
            return False

        assert all(augment(left, set()) for left in left_vertices)
        chosen = tuple(sorted(edge_id for _left, edge_id in occupied.values()))
        assert len(chosen) == len(left_vertices) == len(right_vertices)
        answer.append(chosen)
        unused.difference_update(chosen)
    assert not unused
    return answer


def product_tuple(left: tuple[Perm, ...], right: tuple[Perm, ...]):
    return tuple(compose(a, b) for a, b in zip(left, right))


def aligned_group(d: int, words: tuple[Word, ...]):
    width = len(words)
    identity = tuple(range(d))
    one = tuple(identity for _ in range(width))
    generators = tuple(
        tuple(transposition(d, word[position]) for word in words)
        for position in range(len(words[0]))
    )
    reached = {one}
    active = deque([one])
    while active:
        current = active.popleft()
        for generator in generators:
            nxt = product_tuple(current, generator)
            if nxt not in reached:
                reached.add(nxt)
                active.append(nxt)
    return frozenset(reached)


def expected_common_parity_order(d: int, width: int) -> int:
    return math.factorial(d) if width == 1 else 2 * (math.factorial(d) // 2) ** width


def rank_three_actual_audit(words: tuple[Word, ...], tau):
    d = 3
    full = tuple(itertools.permutations(range(d)))
    root = tuple(rho for rho in full if rho[d - 1] == d - 1)
    global_key = {word: canonical(word, full) for word in words}
    root_blocks = orbit_blocks(words, root)
    root_key = {word: canonical(word, root) for word in words}
    rows = []
    aggregate = {
        "colors": 0,
        "orders_source": defaultdict(Counter),
        "orders_target": defaultdict(Counter),
        "equal_literal": Counter(),
        "subsets": Counter(),
    }
    for adjacent, action in enumerate(tau):
        edges = []
        representatives = []
        for _key, block in sorted(root_blocks.items()):
            target_root_keys = {root_key[action[word]] for word in block}
            assert len(target_root_keys) == 1
            representative = min(block)
            edges.append((global_key[representative], global_key[action[representative]]))
            representatives.append(representative)
        matchings = perfect_matching_decomposition(edges, d)
        adjacent_row = {"adjacent_index": adjacent + 1, "colors": []}
        for color, edge_ids in enumerate(matchings):
            source_words = tuple(representatives[j] for j in edge_ids)
            target_words_here = tuple(action[word] for word in source_words)
            source_endpoints = tuple(global_key[word] for word in source_words)
            target_endpoints = tuple(global_key[word] for word in target_words_here)
            assert len(set(source_endpoints)) == len(source_words) == 4
            assert len(set(target_endpoints)) == len(target_words_here) == 4
            color_row = {
                "color": color,
                "edges": len(edge_ids),
                "source_orders": {},
                "target_orders": {},
                "equal_literal_by_width": {},
            }
            for width in range(1, 5):
                source_hist = Counter()
                target_hist = Counter()
                equal = 0
                count = 0
                for positions in itertools.combinations(range(4), width):
                    sg = aligned_group(d, tuple(source_words[j] for j in positions))
                    tg = aligned_group(d, tuple(target_words_here[j] for j in positions))
                    source_hist[len(sg)] += 1
                    target_hist[len(tg)] += 1
                    equal += sg == tg
                    count += 1
                    assert all(len({parity(p) for p in element}) == 1 for element in sg)
                    assert all(len({parity(p) for p in element}) == 1 for element in tg)
                    if width <= 2:
                        assert len(sg) == len(tg) == expected_common_parity_order(d, width)
                color_row["source_orders"][str(width)] = dict(sorted(source_hist.items()))
                color_row["target_orders"][str(width)] = dict(sorted(target_hist.items()))
                color_row["equal_literal_by_width"][str(width)] = equal
                aggregate["orders_source"][width].update(source_hist)
                aggregate["orders_target"][width].update(target_hist)
                aggregate["equal_literal"][width] += equal
                aggregate["subsets"][width] += count
            adjacent_row["colors"].append(color_row)
            aggregate["colors"] += 1
        rows.append(adjacent_row)

    compact = {
        "colors": aggregate["colors"],
        "orders_source": {
            str(width): {str(order): count for order, count in sorted(hist.items())}
            for width, hist in sorted(aggregate["orders_source"].items())
        },
        "orders_target": {
            str(width): {str(order): count for order, count in sorted(hist.items())}
            for width, hist in sorted(aggregate["orders_target"].items())
        },
        "equal_literal": {str(k): v for k, v in sorted(aggregate["equal_literal"].items())},
        "subsets": {str(k): v for k, v in sorted(aggregate["subsets"].items())},
    }
    assert compact["colors"] == 9
    assert compact["orders_source"] == {
        "1": {"6": 36}, "2": {"18": 54}, "3": {"18": 36}, "4": {"18": 9}
    }
    assert compact["orders_target"] == compact["orders_source"]
    assert compact["equal_literal"] == {"1": 36, "2": 54, "3": 3, "4": 0}
    return {"rows": rows, "aggregate": compact}


def abstract_rank_three() -> dict:
    d = 3
    group = tuple(itertools.permutations(range(d)))
    even = tuple(p for p in group if parity(p) == 0)
    identity = tuple(range(d))
    t = transposition(d, (0, 1))
    kernel = {
        x
        for x in itertools.product(even, repeat=3)
        if compose(compose(x[0], x[1]), x[2]) == identity
    }
    odd = {tuple(compose(a, t) for a in x) for x in kernel}
    subgroup = frozenset(kernel | odd)
    assert all(product_tuple(x, y) in subgroup for x in subgroup for y in subgroup)
    projections = {
        f"{a + 1},{b + 1}": len({(x[a], x[b]) for x in subgroup})
        for a, b in itertools.combinations(range(3), 2)
    }
    assert len(subgroup) == 18 and set(projections.values()) == {18}
    return {
        "subgroup_order": len(subgroup),
        "common_parity_order": expected_common_parity_order(d, 3),
        "pair_projection_orders": projections,
        "proper": len(subgroup) < expected_common_parity_order(d, 3),
    }


def pair_group(d: int, first: Word, second: Word):
    return aligned_group(d, (first, second))


def rank_four_witness(words: tuple[Word, ...], tau) -> dict:
    d = 4
    A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
    x = (A, B, B, A, C, C)
    y = (A, B, B, C, A, C)
    xp = (A, D, B, E, D, C)
    yp = (A, D, B, C, E, C)
    assert all(word in words for word in (x, y, xp, yp))
    assert tau[0][x] == xp and tau[0][y] == yp
    full = tuple(itertools.permutations(range(d)))
    assert canonical(x, full) != canonical(y, full)
    assert canonical(xp, full) != canonical(yp, full)
    before = pair_group(d, x, y)
    after = pair_group(d, xp, yp)
    identity = tuple(range(d))
    v4 = (
        identity,
        compose(transposition(d, (0, 1)), transposition(d, (2, 3))),
        compose(transposition(d, (0, 2)), transposition(d, (1, 3))),
        compose(transposition(d, (0, 3)), transposition(d, (1, 2))),
    )
    expected_before = frozenset(
        (compose(n1, g), compose(n2, g)) for n1 in v4 for n2 in v4 for g in full
    )
    expected_after = frozenset(
        (p, q) for p in full for q in full if parity(p) == parity(q)
    )
    assert before == expected_before and after == expected_after
    return {
        "all_words_in_Z4": True,
        "tau1_endpoints_match": True,
        "source_globally_conjugate": False,
        "target_globally_conjugate": False,
        "source_group_order": len(before),
        "target_group_order": len(after),
        "source_description_verified": "(V4 x V4)Diag(S4)",
        "target_description_verified": "P4",
        "singleton_bound": len(words),
        "d_to_six": d**6,
    }


def generated_permutation_group(d: int, generators) -> frozenset[Perm]:
    identity = tuple(range(d))
    reached = {identity}
    active = deque([identity])
    generators = tuple(generators)
    while active:
        current = active.popleft()
        for generator in generators:
            nxt = compose(current, generator)
            if nxt not in reached:
                reached.add(nxt)
                active.append(nxt)
    return frozenset(reached)


def exact_alternating_simplicity(d: int) -> dict:
    full = tuple(itertools.permutations(range(d)))
    alternating = tuple(p for p in full if parity(p) == 0)
    identity = tuple(range(d))
    unseen = set(alternating)
    rows = []
    while unseen:
        representative = min(unseen)
        conjugacy_class = {
            compose(compose(g, representative), invert(g)) for g in alternating
        }
        unseen.difference_update(conjugacy_class)
        if representative == identity:
            closure_order = 1
        else:
            closure_order = len(generated_permutation_group(d, conjugacy_class))
            assert closure_order == len(alternating)
        rows.append(
            {
                "class_size": len(conjugacy_class),
                "normal_closure_order": closure_order,
                "identity_class": representative == identity,
            }
        )
    return {
        "d": d,
        "alternating_order": len(alternating),
        "conjugacy_classes": sorted(rows, key=lambda row: (not row["identity_class"], row["class_size"])),
        "every_nonidentity_class_normally_generates": True,
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    started = time.perf_counter()
    mission = Path(__file__).resolve().parent
    root = Path(__file__).resolve().parents[4]
    frozen = (
        root
        / "experiments/20260811-polynomial-mixing-resolution/cycle-32"
        / "mission-M141-multisource-matching-subgroup"
    )
    observed = {name: sha256(frozen / name) for name in FROZEN_HASHES}
    assert observed == FROZEN_HASHES

    words3, fibers3, tau3 = reconstruct_dps(3)
    words4, fibers4, tau4 = reconstruct_dps(4)
    d3_actual = rank_three_actual_audit(words3, tau3)
    d3_abstract = abstract_rank_three()
    d4 = rank_four_witness(words4, tau4)
    simplicity = [exact_alternating_simplicity(d) for d in (5, 6)]

    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    payload = {
        "experiment": "M143 clean-room referee checks for frozen M141",
        "repository_commit": commit,
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "command": "python3 -B independent_referee.py",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "frozen_hashes_verified": observed,
        "finite_rank_cap": [3, 4, 5, 6],
        "dps_reconstruction": {
            "d3": {
                "target_words": len(words3),
                "rooted_coordinates": sum(map(len, fibers3.values())),
                "root_fiber_sizes": dict(Counter(map(len, fibers3.values()))),
            },
            "d4": {
                "target_words": len(words4),
                "rooted_coordinates": sum(map(len, fibers4.values())),
                "root_fiber_sizes": dict(Counter(map(len, fibers4.values()))),
            },
        },
        "actual_d3_matching_audit": d3_actual,
        "abstract_d3_counterexample": d3_abstract,
        "d4_pair_dichotomy_exception": d4,
        "boundary_rank_simplicity_checks": simplicity,
        "universal_claim_note": "The d>=5 theorem is accepted or rejected by proof audit, not finite extrapolation.",
    }
    (mission / "independent_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    print(
        json.dumps(
            {
                "elapsed_seconds": time.perf_counter() - started,
                "output": str(mission / "independent_results.json"),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

