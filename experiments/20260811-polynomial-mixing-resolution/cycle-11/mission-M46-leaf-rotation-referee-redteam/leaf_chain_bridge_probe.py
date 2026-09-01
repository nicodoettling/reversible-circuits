#!/usr/bin/env python3
"""Exact finite falsification probe for the weighted leaf-rotation chain.

Universal claims this script can refute, but cannot prove:

1. the undirected canonical leaf-rotation graph is connected;
2. a proposed bridge/articulation bottleneck exists already in every size;
3. cuts by first-root-subtree size or leaf count have a stated finite flow.

Weights are stored as parking-orbit integers r!/prod(d_i!).  Edge capacities
are stored without the common factor 2/[3r(r-1)(r+1)^(r-1)].
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path


def degree_vectors(r: int):
    """Yield J_r in lexicographic recursive order."""

    row = [0] * r

    def rec(pos: int, remaining: int, slots: int):
        if pos == r:
            if remaining == 0 and slots == 1:
                yield tuple(row)
            return
        for value in range(remaining + 1):
            next_slots = slots - 1 + value
            if next_slots < 1:
                continue
            row[pos] = value
            yield from rec(pos + 1, remaining - value, next_slots)

    yield from rec(0, r, 1)


def children_from_degrees(degrees: tuple[int, ...]):
    r = len(degrees)
    all_degrees = degrees + (0,)
    children = [[] for _ in range(r + 1)]
    stack = [[0, all_degrees[0]]]
    for vertex in range(1, r + 1):
        while stack and stack[-1][1] == 0:
            stack.pop()
        if not stack:
            raise AssertionError(("invalid", degrees, vertex))
        parent = stack[-1][0]
        children[parent].append(vertex)
        stack[-1][1] -= 1
        stack.append([vertex, all_degrees[vertex]])
    while stack and stack[-1][1] == 0:
        stack.pop()
    if stack:
        raise AssertionError(("unfilled", degrees, stack))
    return tuple(tuple(row) for row in children)


def orbit_weight(degrees: tuple[int, ...]) -> int:
    answer = math.factorial(len(degrees))
    for value in degrees:
        answer //= math.factorial(value)
    return answer


def first_root_subtree_size(children: tuple[tuple[int, ...], ...], r: int) -> int:
    root_children = children[0]
    if not root_children:
        return 0
    end = root_children[1] if len(root_children) >= 2 else r + 1
    return end - root_children[0]


def conductance_record(
    name: str,
    inside: set[int],
    weights: list[int],
    edges: list[tuple[int, int, int]],
    r: int,
):
    total = sum(weights)
    mass = sum(weights[index] for index in inside)
    boundary_numerator = sum(
        capacity for left, right, capacity in edges if (left in inside) != (right in inside)
    )
    smaller = min(mass, total - mass)
    phi = Fraction(0) if smaller == 0 else Fraction(2 * boundary_numerator, 3 * r * (r - 1) * smaller)
    return {
        "name": name,
        "inside_weight": mass,
        "outside_weight": total - mass,
        "boundary_capacity_numerator": boundary_numerator,
        "phi_numerator": phi.numerator,
        "phi_denominator": phi.denominator,
        "phi_float": float(phi),
    }


def run(r: int):
    states = list(degree_vectors(r))
    sys.setrecursionlimit(max(10_000, 4 * len(states)))
    index = {state: i for i, state in enumerate(states)}
    weights = [orbit_weight(state) for state in states]
    total = (r + 1) ** (r - 1)
    if sum(weights) != total:
        raise AssertionError((sum(weights), total))

    edges = []
    edge_seen = {}
    child_rows = []
    first_sizes = []
    leaf_counts = []
    for left, state in enumerate(states):
        children = children_from_degrees(state)
        child_rows.append(children)
        first_sizes.append(first_root_subtree_size(children, r))
        leaf_counts.append(sum(value == 0 for value in state) + 1)
        for parent, row in enumerate(children):
            for leaf in row[:-1]:
                if state[leaf] != 0:
                    continue
                target = list(state)
                target[parent] -= 1
                target[leaf] += 1
                right = index[tuple(target)]
                key = (min(left, right), max(left, right))
                capacity = weights[left] * state[parent]
                if key in edge_seen:
                    raise AssertionError(("duplicate edge", key, state, target))
                if capacity != weights[right]:
                    raise AssertionError(
                        ("detailed balance", state, tuple(target), capacity, weights[right])
                    )
                edge_seen[key] = (parent, leaf)
                edges.append((key[0], key[1], capacity))

    adjacency = [[] for _ in states]
    for edge_id, (left, right, _) in enumerate(edges):
        adjacency[left].append((right, edge_id))
        adjacency[right].append((left, edge_id))

    seen = {0}
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for neighbor, _ in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    timer = 0
    tin = [-1] * len(states)
    low = [-1] * len(states)
    subtree_weight = [0] * len(states)
    bridges = []

    def dfs(vertex: int, parent_edge: int):
        nonlocal timer
        tin[vertex] = low[vertex] = timer
        timer += 1
        subtree_weight[vertex] = weights[vertex]
        for neighbor, edge_id in adjacency[vertex]:
            if edge_id == parent_edge:
                continue
            if tin[neighbor] >= 0:
                low[vertex] = min(low[vertex], tin[neighbor])
                continue
            dfs(neighbor, edge_id)
            subtree_weight[vertex] += subtree_weight[neighbor]
            low[vertex] = min(low[vertex], low[neighbor])
            if low[neighbor] > tin[vertex]:
                left, right, capacity = edges[edge_id]
                smaller = min(subtree_weight[neighbor], total - subtree_weight[neighbor])
                phi = Fraction(2 * capacity, 3 * r * (r - 1) * smaller)
                bridges.append(
                    {
                        "edge": [left, right],
                        "states": [list(states[left]), list(states[right])],
                        "component_weight": subtree_weight[neighbor],
                        "smaller_weight": smaller,
                        "capacity_numerator": capacity,
                        "phi_numerator": phi.numerator,
                        "phi_denominator": phi.denominator,
                        "phi_float": float(phi),
                    }
                )

    if states:
        dfs(0, -1)
    bridges.sort(key=lambda row: Fraction(row["phi_numerator"], row["phi_denominator"]))

    cuts = []
    for size in sorted(set(first_sizes)):
        cuts.append(
            conductance_record(
                f"first_root_subtree_size_le_{size}",
                {i for i, value in enumerate(first_sizes) if value <= size},
                weights,
                edges,
                r,
            )
        )
    for leaves in sorted(set(leaf_counts)):
        cuts.append(
            conductance_record(
                f"leaf_count_le_{leaves}",
                {i for i, value in enumerate(leaf_counts) if value <= leaves},
                weights,
                edges,
                r,
            )
        )
    nontrivial_cuts = [row for row in cuts if row["inside_weight"] and row["outside_weight"]]
    nontrivial_cuts.sort(key=lambda row: row["phi_float"])

    return {
        "r": r,
        "claim_scope": "finite falsification only; no asymptotic inference",
        "stationary_weight": "orbit(d)=r!/prod_i d_i!, total=(r+1)^(r-1)",
        "rate_normalization": "edge Q numerator times 2/[3r(r-1)(r+1)^(r-1)]",
        "states": len(states),
        "edges": len(edges),
        "connected_states": len(seen),
        "connected": len(seen) == len(states),
        "bridges": len(bridges),
        "minimum_bridge": bridges[0] if bridges else None,
        "smallest_candidate_cuts": nontrivial_cuts[:10],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=9)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = [run(r) for r in range(args.r_min, args.r_max + 1)]
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
