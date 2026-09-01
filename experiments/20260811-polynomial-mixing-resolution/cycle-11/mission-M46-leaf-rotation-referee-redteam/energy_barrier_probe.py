#!/usr/bin/env python3
"""Finite widest-vertex-path audit for leaf-rotation energy barriers.

For every parking degree vector d, compute the maximum possible minimum
stationary numerator w along a path from d to the all-unary path vector.
The ratio w(d)/width(d) is the least unavoidable stationary-density loss for
that endpoint.  A finite failure can refute a proposed uniform barrier bound;
finite success is not an asymptotic proof or congestion bound.
"""

from __future__ import annotations

import argparse
import heapq
import json
from fractions import Fraction
from pathlib import Path

import leaf_chain_bridge_probe as base


def run(r):
    states = list(base.degree_vectors(r))
    index = {state: i for i, state in enumerate(states)}
    weights = [base.orbit_weight(state) for state in states]
    adjacency = [[] for _ in states]
    forward_counts = [0] * len(states)
    for left, state in enumerate(states):
        children = base.children_from_degrees(state)
        for parent, row in enumerate(children):
            for leaf in row[:-1]:
                if state[leaf] != 0:
                    continue
                target = list(state)
                target[parent] -= 1
                target[leaf] += 1
                right = index[tuple(target)]
                adjacency[left].append(right)
                adjacency[right].append(left)
                forward_counts[left] += 1

    target = index[tuple([1] * r)]
    width = [0] * len(states)
    predecessor = [-1] * len(states)
    width[target] = weights[target]
    heap = [(-width[target], target)]
    while heap:
        negative, vertex = heapq.heappop(heap)
        current = -negative
        if current != width[vertex]:
            continue
        for neighbor in adjacency[vertex]:
            candidate = min(current, weights[neighbor])
            if candidate > width[neighbor]:
                width[neighbor] = candidate
                predecessor[neighbor] = vertex
                heapq.heappush(heap, (-candidate, neighbor))
    if any(value == 0 for value in width):
        raise AssertionError("disconnected")

    ratios = [Fraction(weights[i], width[i]) for i in range(len(states))]
    worst = max(range(len(states)), key=lambda i: ratios[i])
    local_sinks = [i for i, count in enumerate(forward_counts) if count == 0]
    worst_sink = max(local_sinks, key=lambda i: ratios[i])
    comb_state = (2,) + (1,) * (r - 2) + (0,)
    comb = index[comb_state]
    route = []
    vertex = worst
    while vertex != -1:
        route.append(list(states[vertex]))
        if vertex == target:
            break
        vertex = predecessor[vertex]
    if not route or route[-1] != list(states[target]):
        raise AssertionError(("missing reconstructed route", states[worst]))
    return {
        "r": r,
        "states": len(states),
        "local_forward_sinks": len(local_sinks),
        "worst_state": list(states[worst]),
        "worst_weight": weights[worst],
        "widest_path_floor": width[worst],
        "worst_barrier_ratio": str(ratios[worst]),
        "worst_barrier_float": float(ratios[worst]),
        "worst_sink_state": list(states[worst_sink]),
        "worst_sink_ratio": str(ratios[worst_sink]),
        "comb_state": list(comb_state),
        "comb_weight": weights[comb],
        "comb_widest_path_floor": width[comb],
        "comb_barrier_ratio": str(ratios[comb]),
        "widest_route_length": len(route) - 1,
        "widest_route": route,
        "scope": "finite vertex-barrier falsifier; no congestion/asymptotic inference",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [run(r) for r in range(args.r_min, args.r_max + 1)]
    args.output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
