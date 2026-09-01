#!/usr/bin/env python3
"""Independent exact calibration for the orbit-incidence conflict coloring.

This script reimplements the accepted plus-mirror DPS closure.  It does not
import predecessor experiment code or results.  The all-rank statements are
proved in ``orbit_incidence_reduction.md``; the finite calculations here only
fix conventions and falsify accidental extensions through the exceptional
rank four.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


Edge = tuple[int, int]
Word = tuple[Edge, ...]
Tree = frozenset[tuple[int, int]]
Perm = tuple[int, ...]


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str
    label: int | None = None
    tail: tuple[str, int] | None = None
    head: tuple[str, int] | None = None


def compose(p: Perm, q: Perm) -> Perm:
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(d: int, edge: Edge) -> Perm:
    a, b = edge
    out = list(range(d))
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(d: int, word: Word) -> Perm:
    out = tuple(range(d))
    for edge in word:
        out = compose(out, edge_perm(d, edge))
    return out


def conjugate_edge_by_map(edge: Edge, rho: Perm) -> Edge:
    return tuple(sorted((rho[edge[0]], rho[edge[1]])))


def conjugate_word(word: Word, rho: Perm) -> Word:
    return tuple(conjugate_edge_by_map(edge, rho) for edge in word)


def conjugate_edge_by_transposition(edge: Edge, by: Edge) -> Edge:
    a, b = edge
    x, y = by

    def image(z: int) -> int:
        return y if z == x else x if z == y else z

    return tuple(sorted((image(a), image(b))))


def hurwitz(word: Word, position: int, sign: int) -> Word:
    a, b = word[position], word[position + 1]
    out = list(word)
    if sign == 1:
        out[position : position + 2] = [b, conjugate_edge_by_transposition(a, b)]
    elif sign == -1:
        out[position : position + 2] = [conjugate_edge_by_transposition(b, a), a]
    else:
        raise ValueError(sign)
    return tuple(out)


def connected(d: int, word: Word) -> bool:
    adj = [[] for _ in range(d)]
    for a, b in word:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        v = todo.pop()
        for u in adj[v]:
            if u not in seen:
                seen.add(u)
                todo.append(u)
    return len(seen) == d


def cayley_trees(d: int):
    if d == 2:
        yield frozenset({(1, 2)})
        return
    for code in itertools.product(range(1, d + 1), repeat=d - 2):
        degree = [0] + [1] * d
        for v in code:
            degree[v] += 1
        edges = []
        for v in code:
            leaf = next(u for u in range(1, d + 1) if degree[u] == 1)
            edges.append(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        edges.append(tuple(sorted(u for u in range(1, d + 1) if degree[u] == 1)))
        yield frozenset(edges)


def rooted_parent(tree: Tree, d: int) -> dict[int, int]:
    adj = {v: [] for v in range(1, d + 1)}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    parent = {d: 0}
    todo = [d]
    while todo:
        v = todo.pop()
        for u in adj[v]:
            if u not in parent:
                parent[u] = v
                todo.append(u)
    return parent


def hairy_incidence(tree: Tree, pi: tuple[int, ...], d: int):
    parent = rooted_parent(tree, d)
    incidence: dict[tuple[str, int], dict[int, tuple[str, int]]] = defaultdict(dict)
    first_black: dict[int, int] = {}
    for black in range(1, d):
        pair = pi[2 * black - 2 : 2 * black]
        for label, white in ((pair[0], black), (pair[1], parent[black])):
            bv = ("b", black)
            wv = ("w", white)
            incidence[bv][label] = wv
            incidence[wv][label] = bv
            first_black[label] = black
    return incidence, first_black


def hairy_boundary(incidence, d: int) -> list[Half | Side]:
    m = 2 * d - 2
    start = (("w", 1), 1)
    state = start
    seen = set()
    tokens: list[Half | Side] = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "w" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            head = incidence[vertex][label]
            tokens.append(Side("tree", label, vertex, head))
            state = (head, label)
        else:
            tokens.append(Half(vertex[0], vertex[1], label))
            state = (vertex, label)
    if state != start or len(tokens) != (2 * d - 1) * m:
        raise AssertionError("invalid hairy boundary")
    return tokens


def close_hairy(tokens: list[Half | Side], d: int) -> dict[int, int]:
    tokens = list(tokens)
    second_black: dict[int, int] = {}
    while True:
        positions = [j for j, token in enumerate(tokens) if isinstance(token, Half)]
        pair = None
        for offset, white_position in enumerate(positions):
            black_position = positions[(offset + 1) % len(positions)]
            white = tokens[white_position]
            black = tokens[black_position]
            if white.color == "w" and black.color == "b":
                pair = white_position, black_position
                break
        if pair is None:
            break
        white_position, black_position = pair
        tokens = tokens[white_position:] + tokens[:white_position]
        black_position = (black_position - white_position) % len(tokens)
        white = tokens[0]
        black = tokens[black_position]
        if white.label != black.label:
            raise AssertionError("closure label mismatch")
        distance = sum(isinstance(token, Side) for token in tokens[1:black_position])
        if distance not in (1, 3):
            raise AssertionError(("bad closure distance", distance))
        if distance == 3:
            second_black[white.label] = black.vertex
        tokens = [Side("closure")] + tokens[black_position + 1 :]
    remaining = [token for token in tokens if isinstance(token, Half)]
    if len(remaining) != 2 * d - 2 or any(token.color != "w" for token in remaining):
        raise AssertionError("bad final closure")
    return second_black


def dps_word(tree: Tree, pi: tuple[int, ...], d: int) -> Word:
    incidence, first_black = hairy_incidence(tree, pi, d)
    second_black = close_hairy(hairy_boundary(incidence, d), d)
    word = []
    for label in range(1, 2 * d - 1):
        a = first_black[label]
        b = second_black.get(label, d)
        if a == b:
            raise AssertionError("degenerate output transposition")
        word.append(tuple(sorted((a - 1, b - 1))))
    return tuple(word)


def swap_values(pi: tuple[int, ...], i: int) -> tuple[int, ...]:
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def build_rank(d: int):
    m = 2 * d - 2
    preimages: dict[Word, list[tuple[Tree, tuple[int, ...]]]] = defaultdict(list)
    for tree in cayley_trees(d):
        for pi in itertools.permutations(range(1, m + 1)):
            word = dps_word(tree, pi, d)
            if evaluate(d, word) != tuple(range(d)) or not connected(d, word):
                raise AssertionError("DPS target failure")
            preimages[word].append((tree, pi))
    if set(map(len, preimages.values())) != {d}:
        raise AssertionError("root quotient failure")
    words = tuple(sorted(preimages))
    index = {word: j for j, word in enumerate(words)}
    target_maps: dict[int, tuple[int, ...]] = {}
    for i in range(1, m):
        image = []
        for word in words:
            targets = {
                dps_word(tree, swap_values(pi, i), d)
                for tree, pi in preimages[word]
            }
            if len(targets) != 1:
                raise AssertionError("tau does not descend")
            image.append(index[next(iter(targets))])
        if len(set(image)) != len(words) or any(image[image[j]] != j for j in range(len(words))):
            raise AssertionError("tau not involutive")
        target_maps[i] = tuple(image)
    return words, index, preimages, target_maps


def canonical(word: Word, permutations: tuple[Perm, ...]) -> Word:
    return min(conjugate_word(word, rho) for rho in permutations)


def subgroup_of_product(d: int, words: tuple[Word, ...]) -> frozenset[tuple[Perm, ...]]:
    identity = tuple(range(d))
    generators = tuple(
        tuple(edge_perm(d, word[position]) for word in words)
        for position in range(len(words[0]))
    )
    one = tuple(identity for _ in words)
    seen = {one}
    todo = deque([one])
    while todo:
        value = todo.popleft()
        for generator in generators:
            new = tuple(compose(a, b) for a, b in zip(value, generator))
            if new not in seen:
                seen.add(new)
                todo.append(new)
    return frozenset(seen)


def perfect_matching(edge_rows, left_vertices, right_vertices, active):
    adjacency = {left: [] for left in left_vertices}
    for edge_id in active:
        left, right = edge_rows[edge_id]
        adjacency[left].append((right, edge_id))
    match_right: dict[object, tuple[object, int]] = {}

    def augment(left, seen_right) -> bool:
        for right, edge_id in adjacency[left]:
            if right in seen_right:
                continue
            seen_right.add(right)
            if right not in match_right or augment(match_right[right][0], seen_right):
                match_right[right] = (left, edge_id)
                return True
        return False

    for left in left_vertices:
        if not augment(left, set()):
            raise AssertionError("regular bipartite multigraph lacked perfect matching")
    if len(match_right) != len(right_vertices):
        raise AssertionError("matching did not cover right side")
    return {edge_id for _left, edge_id in match_right.values()}


def edge_coloring(edge_rows, left_vertices, right_vertices, degree):
    active = set(range(len(edge_rows)))
    colors = {}
    for color in range(degree):
        matching = perfect_matching(edge_rows, left_vertices, right_vertices, active)
        for edge_id in matching:
            colors[edge_id] = color
        active -= matching
    if active or len(colors) != len(edge_rows):
        raise AssertionError("incomplete edge coloring")
    return colors


def compose_action(left: tuple[int, ...], right: tuple[int, ...]):
    return tuple(left[right[j]] for j in range(len(right)))


def d3_action_cover(words, index, target_maps):
    generators = []
    descriptors = []
    for position in range(len(words[0]) - 1):
        for sign in (1, -1):
            generators.append(tuple(index[hurwitz(word, position, sign)] for word in words))
            descriptors.append((position + 1, sign))
    identity = tuple(range(len(words)))
    actions = {identity}
    todo = deque([identity])
    while todo:
        action = todo.popleft()
        for generator in generators:
            new = compose_action(generator, action)
            if new not in actions:
                actions.add(new)
                todo.append(new)
    rows = []
    full = (1 << len(words)) - 1
    for i, target in sorted(target_maps.items()):
        masks = {
            sum((action[source] == target[source]) << source for source in range(len(words)))
            for action in actions
        }
        masks.discard(0)
        frontier = {0}
        minimum = None
        sizes = [1]
        for depth in range(1, len(words) + 1):
            frontier = {old | mask for old in frontier for mask in masks}
            sizes.append(len(frontier))
            if full in frontier:
                minimum = depth
                break
        rows.append(
            {
                "adjacent_index": i,
                "action_image_order": len(actions),
                "agreement_masks": len(masks),
                "maximum_agreement": max(mask.bit_count() for mask in masks),
                "minimum_schedule_cover": minimum,
                "union_frontier_sizes": sizes,
            }
        )
    return rows


def serialize_word(word: Word):
    return [[a + 1, b + 1] for a, b in word]


def audit_rank(d: int):
    words, index, preimages, target_maps = build_rank(d)
    all_perms = tuple(itertools.permutations(range(d)))
    root_stabilizer = tuple(rho for rho in all_perms if rho[d - 1] == d - 1)
    global_keys = tuple(canonical(word, all_perms) for word in words)
    root_keys = tuple(canonical(word, root_stabilizer) for word in words)
    global_blocks: dict[Word, list[int]] = defaultdict(list)
    root_blocks: dict[Word, list[int]] = defaultdict(list)
    for j, (gkey, hkey) in enumerate(zip(global_keys, root_keys)):
        global_blocks[gkey].append(j)
        root_blocks[hkey].append(j)
    row = {
        "d": d,
        "m": 2 * d - 2,
        "z_size": len(words),
        "rooted_coordinate_count": sum(map(len, preimages.values())),
        "dps_root_fiber_histogram": dict(sorted(Counter(map(len, preimages.values())).items())),
        "global_conjugacy_orbits": len(global_blocks),
        "global_orbit_size_histogram": dict(sorted(Counter(map(len, global_blocks.values())).items())),
        "root_stabilizer_orbits": len(root_blocks),
        "root_stabilizer_orbit_size_histogram": dict(sorted(Counter(map(len, root_blocks.values())).items())),
        "adjacent_rows": [],
    }
    for i, target in sorted(target_maps.items()):
        equivariance_failures = 0
        for source, word in enumerate(words):
            for rho in root_stabilizer:
                conjugate_source = index[conjugate_word(word, rho)]
                lhs = words[target[conjugate_source]]
                rhs = conjugate_word(words[target[source]], rho)
                if lhs != rhs:
                    equivariance_failures += 1
        hkeys = tuple(root_blocks)
        edge_rows = []
        edge_hkeys = []
        for hkey in hkeys:
            representative = root_blocks[hkey][0]
            target_hkeys = {root_keys[target[source]] for source in root_blocks[hkey]}
            if len(target_hkeys) != 1:
                raise AssertionError("tau did not descend to H orbit")
            edge_rows.append((global_keys[representative], global_keys[target[representative]]))
            edge_hkeys.append(hkey)
        left_vertices = tuple(sorted(set(left for left, _right in edge_rows)))
        right_vertices = tuple(sorted(set(right for _left, right in edge_rows)))
        left_degrees = Counter(left for left, _right in edge_rows)
        right_degrees = Counter(right for _left, right in edge_rows)
        colors = edge_coloring(edge_rows, left_vertices, right_vertices, d)
        color_sources: dict[int, list[int]] = defaultdict(list)
        for edge_id, color in colors.items():
            color_sources[color].extend(root_blocks[edge_hkeys[edge_id]])
        split_counts = [
            len({global_keys[target[source]] for source in block})
            for block in global_blocks.values()
        ]
        adjacent_row = {
            "adjacent_index": i,
            "root_stabilizer_equivariance_failures": equivariance_failures,
            "incidence_edges": len(edge_rows),
            "left_vertices": len(left_vertices),
            "right_vertices": len(right_vertices),
            "left_degree_histogram": dict(sorted(Counter(left_degrees.values()).items())),
            "right_degree_histogram": dict(sorted(Counter(right_degrees.values()).items())),
            "edge_colors": len(set(colors.values())),
            "color_physical_size_histogram": dict(sorted(Counter(map(len, color_sources.values())).items())),
            "target_global_orbit_split_histogram_per_source_global_orbit": dict(sorted(Counter(split_counts).items())),
            "maximum_target_orbit_split": max(split_counts),
        }
        if d == 3:
            conflict_failures = 0
            for sources in color_sources.values():
                for offset, left in enumerate(sources):
                    for right in sources[offset + 1 :]:
                        before = subgroup_of_product(d, (words[left], words[right]))
                        after = subgroup_of_product(d, (words[target[left]], words[target[right]]))
                        if before != after:
                            conflict_failures += 1
            adjacent_row["exact_color_pair_conflicts"] = conflict_failures
        row["adjacent_rows"].append(adjacent_row)
    if d == 3:
        row["complete_action_cover"] = d3_action_cover(words, index, target_maps)
    if d == 4:
        A, B, C, D, E = (0, 1), (0, 2), (2, 3), (1, 2), (1, 3)
        x = (A, B, B, A, C, C)
        y = (A, B, B, C, A, C)
        xp = (A, D, B, E, D, C)
        yp = (A, D, B, C, E, C)
        witness = {
            "sources": [serialize_word(x), serialize_word(y)],
            "targets": [serialize_word(xp), serialize_word(yp)],
            "all_in_Z4": all(word in index for word in (x, y, xp, yp)),
            "tau1_endpoints_match": words[target_maps[1][index[x]]] == xp and words[target_maps[1][index[y]]] == yp,
            "source_pair_subgroup_order": len(subgroup_of_product(4, (x, y))),
            "target_pair_subgroup_order": len(subgroup_of_product(4, (xp, yp))),
            "sources_globally_conjugate": canonical(x, all_perms) == canonical(y, all_perms),
            "targets_globally_conjugate": canonical(xp, all_perms) == canonical(yp, all_perms),
            "interpretation": "Rank four has the extra V4 Goursat quotient: nonconjugate pairs can change 96 to 288, so the d-color proof deliberately excludes d=4.",
        }
        row["rank_four_exception_witness"] = witness
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[3, 4])
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    rows = [audit_rank(d) for d in args.d]
    payload = {
        "experiment": "M135 conflict coloring and simultaneous realization",
        "target": "uniform physical Z_d; no Markov-gap claim",
        "composition_convention": "(pq)(x)=p(q(x)); displayed factors multiply left-to-right",
        "kernel_context": "signed adjacent Hurwitz generators; this script does not estimate a kernel",
        "seed": None,
        "python": platform.python_version(),
        "dependencies": {},
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": "python3 -B conflict_coloring_audit.py --d 3 4 --output results.json",
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - start,
        "claims": {
            "all_rank_conflict_coloring": "proved in orbit_incidence_reduction.md, not inferred from these finite rows",
            "d3_calibration": "exact finite",
            "d4_exception": "exact finite symbolic witness",
            "simultaneous_realization": "unresolved",
        },
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "elapsed_seconds": payload["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
