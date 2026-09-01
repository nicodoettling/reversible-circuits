#!/usr/bin/env python3
"""Exact bounded falsifier for the M05 shuttle recovery map.

For every identity word in the requested small cases, this script constructs
both oriented shuttle paths for every pair of consecutive occurrences of a
support-component color.  It verifies path correctness and tests whether two
different sources can have the same directed used edge and the same metadata
(a,u,v,epsilon,s).  Such a collision would refute the claimed injective
recovery.  Absence in finite cases is calibration only; the proof is the
bijection argument in the referee report.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import defaultdict
from pathlib import Path


Word = tuple[int, ...]


def edges_of(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def eval_word(n: int, edges: list[tuple[int, int]], word: Word) -> tuple[int, ...]:
    p = list(range(n))
    for index in word:
        a, b = edges[index]
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate_edge(edges: list[tuple[int, int]], lookup: dict[tuple[int, int], int], target: int, by: int) -> int:
    a, b = edges[target]
    x, y = edges[by]
    image = tuple(sorted((y if a == x else x if a == y else a, y if b == x else x if b == y else b)))
    return lookup[image]


def hurwitz(word: Word, position: int, orientation: int, edges: list[tuple[int, int]], lookup: dict[tuple[int, int], int]) -> Word:
    p, q = word[position], word[position + 1]
    if orientation == 1:
        pair = (q, conjugate_edge(edges, lookup, p, q))
    else:
        pair = (conjugate_edge(edges, lookup, q, p), p)
    return word[:position] + pair + word[position + 2 :]


def components(n: int, edges: list[tuple[int, int]], word: Word) -> tuple[tuple[int, ...], ...]:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index in word:
        x, y = edges[index]
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
    blocks: dict[int, list[int]] = defaultdict(list)
    for x in range(n):
        blocks[find(x)].append(x)
    return tuple(sorted(tuple(block) for block in blocks.values()))


def color_map(n: int, edges: list[tuple[int, int]], word: Word) -> dict[int, tuple[int, ...]]:
    blocks = components(n, edges, word)
    result = {}
    for index in set(word):
        x, y = edges[index]
        result[index] = next(block for block in blocks if x in block and y in block)
    return result


def audit_case(n: int, m: int) -> dict:
    edges = edges_of(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    identity = tuple(range(n))
    words = [w for w in itertools.product(range(len(edges)), repeat=m) if eval_word(n, edges, w) == identity]
    recovery: dict[tuple[object, ...], Word] = {}
    physical_edge_metadata_counts: dict[tuple[Word, Word], int] = defaultdict(int)
    collisions = []
    path_failures = []
    path_count = 0
    edge_occurrences = 0
    ignored_central_self_loops = 0
    duplicate_orientation_outputs = 0
    repeated_intervening_color_paths = 0
    direct_color_duplicate_targets = 0

    for source in words:
        edge_color = color_map(n, edges, source)
        colors = tuple(edge_color[index] for index in source)
        positions: dict[tuple[int, ...], list[int]] = defaultdict(list)
        for pos, color in enumerate(colors):
            positions[color].append(pos)

        # Direct unequal-color swaps must have a unique changed position.
        seen_color_targets = set()
        for pos in range(m - 1):
            if colors[pos] == colors[pos + 1]:
                continue
            target = source[:pos] + (source[pos + 1], source[pos]) + source[pos + 2 :]
            if target in seen_color_targets:
                direct_color_duplicate_targets += 1
            seen_color_targets.add(target)

        for color, occurrences in positions.items():
            if len(occurrences) < 2 or len(color) < 2:
                continue
            for ell, (u, v) in enumerate(zip(occurrences, occurrences[1:])):
                middle_colors = colors[u + 1 : v]
                if len(set(middle_colors)) < len(middle_colors):
                    repeated_intervening_color_paths += 2
                plus_target = hurwitz(source, u, 1, edges, lookup) if v == u + 1 else None
                minus_target = hurwitz(source, u, -1, edges, lookup) if v == u + 1 else None
                if plus_target is not None and plus_target == minus_target and plus_target != source:
                    duplicate_orientation_outputs += 1
                for orientation in (1, -1):
                    schedule = list(range(u, v - 1)) + [(v - 1, orientation)] + list(range(v - 2, u - 1, -1))
                    # Normalize the outer entries to right-Hurwitz orientation.
                    normalized = [(item, 1) if isinstance(item, int) else item for item in schedule]
                    current = source
                    # If the requested internal generator is a self-loop, its
                    # Dirichlet commodity is omitted by the proof.
                    internal = tuple(source[pos] for pos in occurrences)
                    internal_target = hurwitz(internal, ell, orientation, edges, lookup)
                    if internal_target == internal:
                        ignored_central_self_loops += 1
                        continue
                    path_count += 1
                    for stage, (pos, orient) in enumerate(normalized):
                        nxt = hurwitz(current, pos, orient, edges, lookup)
                        key = (current, nxt, color, u, v, orientation, stage)
                        previous = recovery.get(key)
                        if previous is not None and previous != source:
                            collisions.append({"source_one": previous, "source_two": source, "metadata": [color, u, v, orientation, stage]})
                        recovery[key] = source
                        physical_edge_metadata_counts[(current, nxt)] += 1
                        edge_occurrences += 1
                        current = nxt
                    final_colors = tuple(color_map(n, edges, current)[index] for index in current)
                    final_positions: dict[tuple[int, ...], list[int]] = defaultdict(list)
                    for pos, final_color in enumerate(final_colors):
                        final_positions[final_color].append(pos)
                    final_internal = tuple(current[pos] for pos in final_positions[color])
                    if final_colors != colors or final_internal != internal_target:
                        path_failures.append({"source": source, "u": u, "v": v, "orientation": orientation, "target": current})

    return {
        "n": n,
        "m": m,
        "identity_word_count": len(words),
        "shuttle_path_count": path_count,
        "used_edge_occurrences": edge_occurrences,
        "recovery_collision_count": len(collisions),
        "first_recovery_collisions": collisions[:3],
        "path_failure_count": len(path_failures),
        "first_path_failures": path_failures[:3],
        "ignored_central_self_loop_commodities": ignored_central_self_loops,
        "duplicate_orientation_outputs_adjacent": duplicate_orientation_outputs,
        "paths_with_repeated_intervening_colors": repeated_intervening_color_paths,
        "direct_color_duplicate_target_count": direct_color_duplicate_targets,
        "maximum_metadata_occurrences_on_one_directed_physical_edge": max(physical_edge_metadata_counts.values(), default=0),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # (5,6) is the smallest listed run that contains a nontrivial connected
    # S_3 component interleaved with a positive disjoint S_2 component, so it
    # exercises genuine shuttle paths of length greater than one.
    cases = [audit_case(3, 4), audit_case(4, 4), audit_case(4, 6), audit_case(5, 6)]
    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": "fixed-(a,u,v,epsilon,s) source recovery is injective and both shuttle orientations implement the requested internal Hurwitz move",
        "logical_scope": "a finite collision refutes the universal recovery claim; no collision is calibration only",
        "composition": "(pq)(x)=p(q(x))",
        "deterministic": True,
        "random_seed": None,
        "environment": {"python": platform.python_version(), "nonstandard_dependencies": []},
        "cases": cases,
        "total_recovery_collisions": sum(case["recovery_collision_count"] for case in cases),
        "total_path_failures": sum(case["path_failure_count"] for case in cases),
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
