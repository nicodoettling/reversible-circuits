#!/usr/bin/env python3
"""Finite mass audit for separators based on maximum outdegree.

Delete states with max(d)>=threshold from the leaf-rotation graph and compute
the exact stationary numerator of every remaining component.  This tests the
candidate that rare high-degree states separate two macroscopic regions.
Finite output can refute a proposed bounded instance but cannot prove an
asymptotic separator theorem.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

import leaf_chain_bridge_probe as base


def run(r, threshold):
    states = list(base.degree_vectors(r))
    index = {state: i for i, state in enumerate(states)}
    weights = [base.orbit_weight(state) for state in states]
    total = sum(weights)
    removed = {i for i, state in enumerate(states) if max(state) >= threshold}
    adjacency = [[] for _ in states]
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

    unseen = set(range(len(states))) - removed
    components = []
    while unseen:
        seed = next(iter(unseen))
        unseen.remove(seed)
        queue = deque([seed])
        vertices = []
        while queue:
            vertex = queue.popleft()
            vertices.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        components.append((sum(weights[v] for v in vertices), len(vertices), seed))
    components.sort(reverse=True)
    return {
        "r": r,
        "threshold_removed_max_degree_ge": threshold,
        "states": len(states),
        "removed_states": len(removed),
        "removed_weight": sum(weights[i] for i in removed),
        "removed_mass": sum(weights[i] for i in removed) / total,
        "remaining_components": len(components),
        "largest_components": [
            {
                "weight": weight,
                "mass": weight / total,
                "states": size,
                "representative": list(states[seed]),
            }
            for weight, size, seed in components[:10]
        ],
        "scope": "finite exact mass/separator falsifier only",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, required=True)
    parser.add_argument("--threshold-min", type=int, default=3)
    parser.add_argument("--threshold-max", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [run(args.r, k) for k in range(args.threshold_min, args.threshold_max + 1)]
    args.output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
