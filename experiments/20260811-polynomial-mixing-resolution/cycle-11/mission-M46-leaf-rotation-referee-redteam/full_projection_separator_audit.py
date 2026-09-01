#!/usr/bin/env python3
"""Exact finite falsifier for lifting the M48 cut to the full parking projection.

The M48 set A is defined using maximum plane-tree outdegree and the capped
reversible-pebble component of the root-branch prefix set.  This script
enumerates every exact adjacent-rank-two projected heat-bath edge in the
smallest long-cycle sectors and reports low-degree edges that cross A.  One
such edge rigorously refutes support containment for the *full* projection;
finite absence would not prove an asymptotic bottleneck.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
M35 = HERE.parents[1] / "cycle-08" / "mission-M35-general-parking-flow"
sys.path.insert(0, str(M35))

import adjacent_bypass_probe as exact  # noqa: E402
import leaf_rotation_probe as leaf  # noqa: E402


def pebble_component(n: int, p: int) -> set[frozenset[int]]:
    start: frozenset[int] = frozenset()
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for i in range(1, n + 1):
            if i != 1 and i - 1 not in state:
                continue
            target = state ^ {i}
            if len(target) <= p and target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def root_prefixes(degrees: tuple[int, ...]) -> tuple[int, ...]:
    children = leaf.preorder_children(degrees)

    def vertices(v: int) -> int:
        return 1 + sum(vertices(u) for u in children[v])

    branches = [vertices(u) for u in children[0]]
    running = 0
    prefixes = []
    for size in branches[:-1]:
        running += size
        prefixes.append(running)
    assert sum(branches) == len(degrees)
    return tuple(prefixes)


def audit(size_n: int) -> dict:
    # exact.run uses n for the long cycle size and r=n-1 for tree edges.
    result = exact.run(size_n, dump_edges=True)
    r = size_n - 1
    chain_n = r - 1
    degree_cut = 2 + math.ceil(math.log2(chain_n))
    pebble_cap = degree_cut - 2
    c0 = pebble_component(chain_n, pebble_cap)

    def data(macro_list: list[int]) -> tuple[bool, tuple[int, ...], tuple[int, ...]]:
        macro = tuple(macro_list)
        degrees = leaf.counts_from_macro(macro)
        prefixes = root_prefixes(degrees)
        low = max(degrees) < degree_cut
        inside = low and frozenset(prefixes) in c0
        return inside, degrees, prefixes

    crossings = []
    macros = {tuple(row["source"]) for row in result["projected_rates"]}
    macros.update(tuple(row["target"]) for row in result["projected_rates"])
    adjacency = {macro: set() for macro in macros}
    for row in result["projected_rates"]:
        source_macro = tuple(row["source"])
        target_macro = tuple(row["target"])
        adjacency[source_macro].add(target_macro)
        adjacency[target_macro].add(source_macro)
        source_inside, source_d, source_s = data(row["source"])
        target_inside, target_d, target_s = data(row["target"])
        both_low = max(source_d) < degree_cut and max(target_d) < degree_cut
        if both_low and source_inside != target_inside:
            crossings.append(
                {
                    "source_macro": row["source"],
                    "target_macro": row["target"],
                    "source_degrees": source_d,
                    "target_degrees": target_d,
                    "source_prefix_set": source_s,
                    "target_prefix_set": target_s,
                    "source_in_A": source_inside,
                    "target_in_A": target_inside,
                    "rate": row["rate"],
                    "capacity_count": row["capacity_count"],
                }
            )

    low = {
        macro
        for macro in macros
        if max(leaf.counts_from_macro(macro)) < degree_cut
    }
    unseen = set(low)
    components = []
    total_weight = sum(exact.orbit_weight(macro) for macro in macros)
    while unseen:
        seed = unseen.pop()
        queue = deque([seed])
        component = [seed]
        while queue:
            macro = queue.popleft()
            for neighbor in adjacency[macro]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.append(neighbor)
                    queue.append(neighbor)
        weight = sum(exact.orbit_weight(macro) for macro in component)
        components.append((weight, len(component), seed))
    components.sort(reverse=True)
    return {
        "cycle_size_n": size_n,
        "tree_edges_r": r,
        "pebble_path_n": chain_n,
        "degree_cut_D": degree_cut,
        "pebble_cap_p": pebble_cap,
        "macros": result["macros"],
        "directed_full_projection_edges": result["projected_off_diagonal_edges"],
        "low_degree_cut_crossings": len(crossings),
        "first_crossings": crossings[:20],
        "full_projection_low_degree_components": len(components),
        "largest_low_degree_components": [
            {
                "stationary_mass": weight / total_weight,
                "macro_count": count,
                "representative_macro": seed,
                "representative_degrees": leaf.counts_from_macro(seed),
            }
            for weight, count, seed in components[:10]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle-size-min", type=int, default=4)
    parser.add_argument("--cycle-size-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [audit(n) for n in range(args.cycle_size_min, args.cycle_size_max + 1)]
    output = {
        "claim_tested": "M48 low-degree boundary containment survives every full projected adjacent-rank-two heat-bath edge",
        "scope": "finite exact falsifier; one crossing refutes literal support containment, absence proves no asymptotic cut",
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "rows": rows,
    }
    args.output.write_text(json.dumps(output, indent=2, default=list) + "\n")


if __name__ == "__main__":
    main()
