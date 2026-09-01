#!/usr/bin/env python3
"""Bounded minimax-density test for replant-to-rotation routes."""

from __future__ import annotations

import argparse
import heapq
import json
import math
import platform

from rotation_replant_probe import (
    Tree,
    dyck,
    replant_neighbors,
    rotations,
    trees,
    weight_denominator,
)


def minimax_denominators(
    start: Tree, adjacency: dict[Tree, set[Tree]]
) -> dict[Tree, int]:
    """Minimum possible maximum factorial denominator along a path."""
    initial = weight_denominator(start)
    best = {start: initial}
    heap = [(initial, dyck(start), start)]
    while heap:
        value, _, x = heapq.heappop(heap)
        if value != best[x]:
            continue
        for y in adjacency[x]:
            candidate = max(value, weight_denominator(y))
            if candidate < best.get(y, math.inf):
                best[y] = candidate
                heapq.heappush(heap, (candidate, dyck(y), y))
    return best


def run(r_max: int):
    records = []
    for r in range(2, r_max + 1):
        states = trees(r)
        adjacency = {t: rotations(t) for t in states}
        maximum = 0.0
        witness = None
        for x in states:
            best = minimax_denominators(x, adjacency)
            den_x = weight_denominator(x)
            for y in replant_neighbors(x):
                endpoint_den = max(den_x, weight_denominator(y))
                factor = best[y] / endpoint_den
                if factor > maximum:
                    maximum = factor
                    witness = {
                        "source": dyck(x),
                        "target": dyck(y),
                        "path_max_denominator": best[y],
                        "endpoint_max_denominator": endpoint_den,
                    }
        records.append(
            {
                "r": r,
                "states": len(states),
                "max_minimax_denominator_factor": maximum,
                "witness": witness,
            }
        )
    return {
        "claim_tested": (
            "Every shape-level leaf replant through r_max has a rotation path "
            "whose minimum stationary density is at least the lower endpoint "
            "density; this is a bounded falsifier, not a universal proof."
        ),
        "python": platform.python_version(),
        "deterministic": True,
        "seed": None,
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=8)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = run(args.r_max)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result["records"], indent=2))


if __name__ == "__main__":
    main()
