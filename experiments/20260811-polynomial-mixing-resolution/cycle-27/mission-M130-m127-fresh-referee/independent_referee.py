#!/usr/bin/env python3
"""Independent exact referee for M127's DPS fixed-braid obstruction.

This file imports no predecessor experiment code or data.  It reconstructs
the accepted plus-mirror hairy-tree closure, separately brute-forces Z_d for
d <= 4, and closes the signed Hurwitz action image on Z_3.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Perm = tuple[int, ...]
Tree = frozenset[tuple[int, int]]


EXPECTED_HASHES = {
    "report.md": "d7983caa8cc20bc0e882d11afed3b1953a940b98c56299d2e956d625deb6acc0",
    "fixed_braid_obstruction.md": "0f8c1ce6d5ddc8f54bd3a1fe366f49b512fe8ee5e03a5a68cf547adbaaeb534a",
    "fixed_braid_audit.py": "4fe5a897d3dc38e6c92216a2c576e20ac82e83bbf2038af571b255833bf3718d",
    "fixed_braid_results.json": "51c2e14f868bf433852b606ec71faf9dacc6537b6e2a788373cdbdc10cfbdb9c",
    "freeze_manifest.md": "04b37e3e6a3127137c46a655009ccd18960118138f1c1f1b004528e45e76d7b3",
}


def compose(p: Perm, q: Perm) -> Perm:
    """Return pq, meaning x -> p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(d: int, e: Edge) -> Perm:
    p = list(range(d))
    p[e[0]], p[e[1]] = p[e[1]], p[e[0]]
    return tuple(p)


def eval_word(d: int, word: Word) -> Perm:
    value = tuple(range(d))
    for e in word:
        value = compose(value, transposition(d, e))
    return value


def conjugate_edge(e: Edge, by: Edge) -> Edge:
    u, v = by

    def move(x: int) -> int:
        if x == u:
            return v
        if x == v:
            return u
        return x

    return tuple(sorted((move(e[0]), move(e[1]))))


def signed_hurwitz(word: Word, j: int, sign: int) -> Word:
    a, b = word[j], word[j + 1]
    out = list(word)
    if sign == 1:
        out[j : j + 2] = (b, conjugate_edge(a, b))
    elif sign == -1:
        out[j : j + 2] = (conjugate_edge(b, a), a)
    else:
        raise ValueError(sign)
    return tuple(out)


def connected(d: int, word: Word) -> bool:
    adjacency = [set() for _ in range(d)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    reached = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adjacency[u] - reached:
            reached.add(v)
            todo.append(v)
    return len(reached) == d


def brute_z(d: int) -> tuple[Word, ...]:
    """Enumerate the physical target independently of the DPS map."""
    edges = tuple(itertools.combinations(range(d), 2))
    identity = tuple(range(d))
    m = 2 * d - 2
    return tuple(
        word
        for word in itertools.product(edges, repeat=m)
        if eval_word(d, word) == identity and connected(d, word)
    )


def prufer_trees(d: int) -> tuple[Tree, ...]:
    """Cayley trees on one-based labels, decoded from Prüfer words."""
    if d == 2:
        return (frozenset({(1, 2)}),)
    answer = []
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = {v: 1 for v in range(1, d + 1)}
        for v in code:
            degree[v] += 1
        tree = []
        for v in code:
            leaf = min(x for x in degree if degree[x] == 1)
            tree.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        leaves = sorted(x for x in degree if degree[x] == 1)
        tree.append((leaves[0], leaves[1]))
        answer.append(frozenset(tree))
    return tuple(answer)


def parents_toward_d(tree: Tree, d: int) -> dict[int, int | None]:
    adjacency = {v: [] for v in range(1, d + 1)}
    for u, v in tree:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent: dict[int, int | None] = {d: None}
    queue = deque([d])
    while queue:
        v = queue.popleft()
        for u in adjacency[v]:
            if u not in parent:
                parent[u] = v
                queue.append(u)
    return parent


def dps_plus_word(tree: Tree, pi: tuple[int, ...], d: int) -> Word:
    """Reconstruct the DPS plus mirror by contour tracing and stack closure.

    Vertices are tagged ('w',j) and ('b',j), using one-based white/black
    indices and edge labels.  A token is ('s',) for a traversed/closure side
    or ('h', color, vertex, label) for a dangling half-edge.
    """
    m = 2 * d - 2
    parent = parents_toward_d(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for black in range(1, d):
        p = parent[black]
        assert p is not None
        left_label, right_label = pi[2 * black - 2 : 2 * black]
        bv = ("b", black)
        for label, white in ((left_label, black), (right_label, p)):
            wv = ("w", white)
            incidence[bv][label] = wv
            incidence[wv][label] = bv
            first_black[label] = black

    start = (("w", 1), 1)
    state = start
    visited = set()
    boundary: list[tuple] = []
    while state not in visited:
        visited.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        neighbor = incidence[vertex].get(label)
        if neighbor is None:
            boundary.append(("h", vertex[0], vertex[1], label))
            state = (vertex, label)
        else:
            boundary.append(("s",))
            state = (neighbor, label)
    assert state == start
    assert len(boundary) == (2 * d - 1) * m

    tokens = boundary
    second_black: dict[int, int] = {}
    while True:
        half_positions = [k for k, tok in enumerate(tokens) if tok[0] == "h"]
        chosen: tuple[int, int] | None = None
        for k, left_pos in enumerate(half_positions):
            right_pos = half_positions[(k + 1) % len(half_positions)]
            left, right = tokens[left_pos], tokens[right_pos]
            if left[1] == "w" and right[1] == "b":
                chosen = left_pos, right_pos
                break
        if chosen is None:
            break
        offset, right_pos = chosen
        tokens = tokens[offset:] + tokens[:offset]
        right_pos = (right_pos - offset) % len(tokens)
        left, right = tokens[0], tokens[right_pos]
        assert left[3] == right[3]
        sides = sum(tok[0] == "s" for tok in tokens[1:right_pos])
        assert sides in (1, 3)
        if sides == 3:
            assert left[3] not in second_black
            second_black[left[3]] = right[2]
        tokens = [("s",)] + tokens[right_pos + 1 :]

    halves = [tok for tok in tokens if tok[0] == "h"]
    assert len(halves) == m
    assert all(tok[1] == "w" for tok in halves)
    assert sorted(tok[3] for tok in halves) == list(range(1, m + 1))
    word = []
    for label in range(1, m + 1):
        u = first_black[label]
        v = second_black.get(label, d)
        assert u != v
        word.append(tuple(sorted((u - 1, v - 1))))
    return tuple(word)


def swap_values(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def pair_subgroup(d: int, x: Word, y: Word) -> frozenset[tuple[Perm, Perm]]:
    identity = tuple(range(d))
    generators = tuple((transposition(d, a), transposition(d, b)) for a, b in zip(x, y))

    def mul(left: tuple[Perm, Perm], right: tuple[Perm, Perm]) -> tuple[Perm, Perm]:
        return compose(left[0], right[0]), compose(left[1], right[1])

    seen = {(identity, identity)}
    todo = [(identity, identity)]
    while todo:
        element = todo.pop()
        for generator in generators:
            nxt = mul(element, generator)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return frozenset(seen)


def physical_orbit(words: tuple[Word, ...]) -> int:
    allowed = set(words)
    reached = {words[0]}
    todo = [words[0]]
    m = len(words[0])
    while todo:
        word = todo.pop()
        for j in range(m - 1):
            for sign in (-1, 1):
                nxt = signed_hurwitz(word, j, sign)
                assert nxt in allowed
                if nxt not in reached:
                    reached.add(nxt)
                    todo.append(nxt)
    return len(reached)


def first_subgroup_witness(
    d: int, words: tuple[Word, ...], target: dict[Word, Word]
) -> dict | None:
    tested = 0
    for x in words:
        for y in words:
            tested += 1
            before = pair_subgroup(d, x, y)
            after = pair_subgroup(d, target[x], target[y])
            if before != after:
                return {
                    "pairs_tested": tested,
                    "source_a": serialize_word(x),
                    "source_b": serialize_word(y),
                    "target_a": serialize_word(target[x]),
                    "target_b": serialize_word(target[y]),
                    "source_subgroup_order": len(before),
                    "target_subgroup_order": len(after),
                    "intersection_order": len(before & after),
                }
    return None


def serialize_word(word: Word) -> list[list[int]]:
    return [[a + 1, b + 1] for a, b in word]


def compose_action(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[x]] for x in range(len(right)))


def d3_action_audit(words: tuple[Word, ...], targets: dict[int, dict[Word, Word]]) -> dict:
    index = {word: k for k, word in enumerate(words)}
    m = len(words[0])
    generators = []
    for j in range(m - 1):
        for sign in (-1, 1):
            generators.append(tuple(index[signed_hurwitz(w, j, sign)] for w in words))
    identity = tuple(range(len(words)))
    group = {identity}
    queue = deque([identity])
    while queue:
        action = queue.popleft()
        for generator in generators:
            nxt = compose_action(generator, action)
            if nxt not in group:
                group.add(nxt)
                queue.append(nxt)

    rows = []
    full = (1 << len(words)) - 1
    for i in sorted(targets):
        tau = tuple(index[targets[i][w]] for w in words)
        masks = {
            sum((action[source] == tau[source]) << source for source in range(len(words)))
            for action in group
        }
        masks.discard(0)
        frontier = {0}
        sizes = [1]
        minimum = None
        for depth in range(1, len(words) + 1):
            frontier = {covered | mask for covered in frontier for mask in masks}
            sizes.append(len(frontier))
            if full in frontier:
                minimum = depth
                break
        assert minimum is not None
        rows.append(
            {
                "adjacent_index": i,
                "tau_is_bijection": len(set(tau)) == len(words),
                "tau_is_involution": compose_action(tau, tau) == identity,
                "tau_in_action_image": tau in group,
                "nonempty_agreement_masks": len(masks),
                "maximum_agreement": max(mask.bit_count() for mask in masks),
                "minimum_schedule_cover": minimum,
                "cover_frontier_sizes": sizes,
            }
        )
    return {"action_image_order": len(group), "generator_count": len(generators), "rows": rows}


def rank_audit(d: int) -> tuple[dict, dict[int, dict[Word, Word]]]:
    m = 2 * d - 2
    brute = tuple(sorted(brute_z(d)))
    preimages: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    rooted_rows = []
    for tree in prufer_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            word = dps_plus_word(tree, pi, d)
            preimages[word].append((tree, pi))
            rooted_rows.append((tree, pi, word))
    dps_words = tuple(sorted(preimages))
    output_set_equal = dps_words == brute
    fiber_histogram = Counter(len(rows) for rows in preimages.values())
    identity_failures = sum(eval_word(d, word) != tuple(range(d)) for _, _, word in rooted_rows)
    support_failures = sum(not connected(d, word) for _, _, word in rooted_rows)

    target_maps: dict[int, dict[Word, Word]] = {}
    index_rows = []
    for i in range(1, m):
        choices: dict[Word, set[Word]] = defaultdict(set)
        for tree, pi, word in rooted_rows:
            choices[word].add(dps_plus_word(tree, swap_values(pi, i), d))
        target = {word: next(iter(target_set)) for word, target_set in choices.items() if len(target_set) == 1}
        collision_count = sum(len(target_set) != 1 for target_set in choices.values())
        if collision_count == 0:
            target_maps[i] = target
            target_values = tuple(target[w] for w in brute)
            target_involution = all(target[target[w]] == w for w in brute)
            target_bijection = len(set(target_values)) == len(brute)
            obstruction = first_subgroup_witness(d, brute, target)
        else:
            target_involution = False
            target_bijection = False
            obstruction = None
        index_rows.append(
            {
                "adjacent_index": i,
                "root_fiber_collision_sources": collision_count,
                "descends": collision_count == 0,
                "target_is_bijection": target_bijection,
                "target_is_involution": target_involution,
                "first_pair_subgroup_witness": obstruction,
            }
        )
    return (
        {
            "d": d,
            "m": m,
            "cayley_tree_count": len(prufer_trees(d)),
            "rooted_coordinate_count": len(rooted_rows),
            "brute_z_size": len(brute),
            "dps_image_size": len(dps_words),
            "dps_image_equals_brute_z": output_set_equal,
            "root_fiber_histogram": {str(k): v for k, v in sorted(fiber_histogram.items())},
            "identity_failures": identity_failures,
            "support_failures": support_failures,
            "signed_hurwitz_orbit_size": physical_orbit(brute),
            "adjacent_rows": index_rows,
        },
        target_maps,
    )


def displayed_witness() -> dict:
    tree = frozenset({(1, 2), (1, 3)})
    pi_a = (3, 4, 1, 2)
    pi_b = (1, 2, 4, 3)
    x = dps_plus_word(tree, pi_a, 3)
    y = dps_plus_word(tree, pi_b, 3)
    xp = dps_plus_word(tree, swap_values(pi_a, 3), 3)
    yp = dps_plus_word(tree, swap_values(pi_b, 3), 3)
    source_group = pair_subgroup(3, x, y)
    target_group = pair_subgroup(3, xp, yp)
    expected_words = (
        ((0, 1), (0, 1), (0, 2), (0, 2)),
        ((0, 1), (0, 2), (0, 1), (1, 2)),
        ((1, 2), (1, 2), (0, 2), (0, 2)),
        ((0, 2), (0, 2), (0, 1), (0, 1)),
    )
    return {
        "tree": [[1, 2], [1, 3]],
        "pi_a": list(pi_a),
        "pi_b": list(pi_b),
        "x": serialize_word(x),
        "y": serialize_word(y),
        "x_prime": serialize_word(xp),
        "y_prime": serialize_word(yp),
        "all_endpoints_match_report": (x, y, xp, yp) == expected_words,
        "source_subgroup_order": len(source_group),
        "target_subgroup_order": len(target_group),
        "subgroups_differ": source_group != target_group,
    }


def file_hashes(source: Path) -> dict:
    rows = {}
    for name, expected in EXPECTED_HASHES.items():
        observed = hashlib.sha256((source / name).read_bytes()).hexdigest()
        rows[name] = {"expected": expected, "observed": observed, "matches": observed == expected}
    return rows


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()


def main() -> None:
    started = time.perf_counter()
    here = Path(__file__).resolve().parent
    source = here.parents[1] / "cycle-26" / "mission-M127-dps-fixed-braid-intertwining"
    hashes = file_hashes(source)
    rows = []
    targets_by_d = {}
    for d in (2, 3, 4):
        row, targets = rank_audit(d)
        rows.append(row)
        targets_by_d[d] = targets
    d3_words = tuple(sorted(brute_z(3)))
    action = d3_action_audit(d3_words, targets_by_d[3])
    witness = displayed_witness()

    finite_ok = (
        [(r["d"], r["rooted_coordinate_count"], r["brute_z_size"], r["root_fiber_histogram"]) for r in rows]
        == [(2, 2, 1, {"2": 1}), (3, 72, 24, {"3": 24}), (4, 11520, 2880, {"4": 2880})]
        and all(r["dps_image_equals_brute_z"] and r["identity_failures"] == r["support_failures"] == 0 for r in rows)
        and all(a["descends"] and a["target_is_bijection"] and a["target_is_involution"] for r in rows for a in r["adjacent_rows"])
        and all(a["first_pair_subgroup_witness"] is not None for r in rows if r["d"] in (3, 4) for a in r["adjacent_rows"])
        and action["action_image_order"] == 216
        and all(
            not a["tau_in_action_image"]
            and a["maximum_agreement"] == 6
            and a["minimum_schedule_cover"] == 5
            for a in action["rows"]
        )
        and witness["all_endpoints_match_report"]
        and witness["source_subgroup_order"] == 18
        and witness["target_subgroup_order"] == 6
    )
    payload = {
        "experiment": "M130 independent fresh referee of frozen M127",
        "verdict": "ACCEPT" if finite_ok and all(v["matches"] for v in hashes.values()) else "REJECT",
        "material_numbered_objections": [],
        "target": "uniform physical Z_d, with the constant-d rooted DPS lift used only for coordinates",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "dps_convention": "accepted plus mirror, Cayley tree rooted at y_d",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "commit": git_commit(),
        "argv": sys.argv,
        "source_hashes": hashes,
        "displayed_d3_i3_witness": witness,
        "rank_rows": rows,
        "d3_complete_action_image": action,
        "scope": {
            "proved_by_general_argument": [
                "DPS adjacent-value relabeling descends independently of the forgotten white root",
                "diagonal signed Hurwitz action preserves the literal coordinate-pair generated subgroup",
            ],
            "refuted": "one source-independent signed Hurwitz word realizes a whole adjacent-value action (already d=3)",
            "finite_only": [
                "all-index d=3,4 paired-subgroup witnesses",
                "d=3 action image order 216 and five-class schedule cover",
            ],
            "unresolved": [
                "polynomial schedule cover",
                "rooted product local comparison",
                "all-edge congestion",
                "physical P_(0,d) gap",
                "original heat-bath gap",
                "Terminal A or B",
            ],
        },
        "elapsed_seconds": time.perf_counter() - started,
    }
    output = here / "independent_results.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
