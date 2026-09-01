#!/usr/bin/env python3
"""Extract exact minimax-density paths for leaf--chain root-child swaps."""

from __future__ import annotations

import argparse
import heapq
import json
import math

from rotation_replant_probe import Tree, dyck, rotations, trees, weight_denominator


def degrees(t: Tree) -> list[int]:
    ans = [len(t)]
    for child in t:
        ans.extend(degrees(child))
    return ans


def leaf_then_chain(r: int) -> Tree:
    chain: Tree = ()
    for _ in range(r - 2):
        chain = (chain,)
    return ((), chain)


def chain_then_leaf(r: int) -> Tree:
    chain: Tree = ()
    for _ in range(r - 2):
        chain = (chain,)
    return (chain, ())


def minimax_path(start: Tree, target: Tree, adjacency):
    best = {start: weight_denominator(start)}
    length = {start: 0}
    prev = {}
    heap = [(best[start], 0, dyck(start), start)]
    while heap:
        value, steps, _, x = heapq.heappop(heap)
        if (value, steps) != (best[x], length[x]):
            continue
        if x == target:
            break
        for y in adjacency[x]:
            candidate = max(value, weight_denominator(y))
            pair = (candidate, steps + 1)
            if pair < (best.get(y, math.inf), length.get(y, math.inf)):
                best[y], length[y], prev[y] = candidate, steps + 1, x
                heapq.heappush(heap, (candidate, steps + 1, dyck(y), y))
    path = [target]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    return best[target], path


def run(r_max: int):
    records = []
    for r in range(2, r_max + 1):
        states = trees(r)
        adjacency = {t: rotations(t) for t in states}
        source, target = leaf_then_chain(r), chain_then_leaf(r)
        bound, path = minimax_path(source, target, adjacency)
        records.append(
            {
                "r": r,
                "minimax_denominator": bound,
                "endpoint_denominator": 2,
                "path_length_at_minimax": len(path) - 1,
                "path": [
                    {
                        "dyck": dyck(t),
                        "degrees": degrees(t),
                        "denominator": weight_denominator(t),
                    }
                    for t in path
                ],
            }
        )
    return {
        "claim_tested": (
            "For the leaf--chain root-child swap, compute a path minimizing "
            "the maximum factorial weight denominator through r_max."
        ),
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
    for rec in result["records"]:
        print(rec["r"], rec["minimax_denominator"], rec["path_length_at_minimax"])


if __name__ == "__main__":
    main()
