#!/usr/bin/env python3
"""Exact finite audit of Caraceni right-peak translations versus M35 shifts.

For each plane tree on r edges, generate each local right peak translation

    [..., (), B, ...]  ->  [..., ((), *children(B)), ...],

i.e. detach a leaf and reinsert it as the first child of its next sibling.
Test whether the endpoints are connected in the M35 undirected leaf-rotation
graph while all intermediate stationary weights stay at least the smaller
endpoint weight.  If not, compute the exact widest-path stationary-weight
floor.  Enumeration is a finite falsifier only.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from collections import deque
from pathlib import Path

import leaf_chain_bridge_probe as base


Tree = tuple["Tree", ...]


def nested_from_degree(d: tuple[int, ...]) -> Tree:
    children = base.children_from_degrees(d)

    def rec(v: int) -> Tree:
        return tuple(rec(u) for u in children[v])

    return rec(0)


def degree_from_nested(t: Tree) -> tuple[int, ...]:
    degrees: list[int] = []

    def rec(x: Tree) -> None:
        degrees.append(len(x))
        for child in x:
            rec(child)

    rec(t)
    assert degrees[-1] == 0
    return tuple(degrees[:-1])


def right_peak_targets(t: Tree) -> set[Tree]:
    """All one-step UDU -> UUD translations, including nested locations."""
    out: set[Tree] = set()
    kids = list(t)
    for p in range(len(kids) - 1):
        if kids[p] == ():
            b = kids[p + 1]
            replacement = ((),) + b
            out.add(tuple(kids[:p] + [replacement] + kids[p + 2 :]))
    for q, child in enumerate(kids):
        for child_target in right_peak_targets(child):
            new_kids = kids.copy()
            new_kids[q] = child_target
            out.add(tuple(new_kids))
    out.discard(t)
    return out


def integer_weight(d: tuple[int, ...]) -> int:
    r = len(d)
    ans = math.factorial(r)
    for x in d:
        ans //= math.factorial(x)
    return ans


def widest_floor(
    source: int, target: int, adj: list[list[int]], weights: list[int]
) -> tuple[int, list[int]]:
    best = [-1] * len(adj)
    pred = [-1] * len(adj)
    best[source] = weights[source]
    heap: list[tuple[int, int]] = [(-weights[source], source)]
    while heap:
        neg, v = heapq.heappop(heap)
        score = -neg
        if score != best[v]:
            continue
        if v == target:
            break
        for u in adj[v]:
            cand = min(score, weights[u])
            if cand > best[u]:
                best[u] = cand
                pred[u] = v
                heapq.heappush(heap, (-cand, u))
    assert best[target] >= 0
    path = []
    v = target
    while v != -1:
        path.append(v)
        if v == source:
            break
        v = pred[v]
    path.reverse()
    return best[target], path


def monotone_distance(
    source: int, target: int, adj: list[list[int]], weights: list[int]
) -> int | None:
    threshold = min(weights[source], weights[target])
    dist = [-1] * len(adj)
    dist[source] = 0
    queue = deque([source])
    while queue:
        v = queue.popleft()
        if v == target:
            return dist[v]
        for u in adj[v]:
            if dist[u] < 0 and weights[u] >= threshold:
                dist[u] = dist[v] + 1
                queue.append(u)
    return None


def audit(r: int) -> dict:
    states = list(base.degree_vectors(r))
    index = {d: i for i, d in enumerate(states)}
    adj = [[] for _ in states]
    for i, d in enumerate(states):
        children = base.children_from_degrees(d)
        for parent, row in enumerate(children):
            for leaf in row[:-1]:
                if d[leaf] != 0:
                    continue
                e = list(d)
                e[parent] -= 1
                e[leaf] += 1
                j = index[tuple(e)]
                adj[i].append(j)
                adj[j].append(i)
    weights = [integer_weight(d) for d in states]

    pairs: set[tuple[int, int]] = set()
    for i, d in enumerate(states):
        tree = nested_from_degree(d)
        for target_tree in right_peak_targets(tree):
            target_d = degree_from_nested(target_tree)
            assert target_d in index
            pairs.add((i, index[target_d]))

    failures = []
    max_monotone_distance = 0
    for i, j in sorted(pairs):
        distance = monotone_distance(i, j, adj, weights)
        if distance is not None:
            max_monotone_distance = max(max_monotone_distance, distance)
            continue
        floor, path = widest_floor(i, j, adj, weights)
        threshold = min(weights[i], weights[j])
        failures.append(
            {
                "source": states[i],
                "target": states[j],
                "source_weight": weights[i],
                "target_weight": weights[j],
                "endpoint_floor": threshold,
                "widest_path_floor": floor,
                "barrier_ratio": [threshold, floor],
                "widest_path": [states[v] for v in path],
            }
        )
    return {
        "r": r,
        "state_count": len(states),
        "right_peak_pair_count": len(pairs),
        "monotone_pair_count": len(pairs) - len(failures),
        "failure_count": len(failures),
        "max_monotone_shortest_distance": max_monotone_distance,
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=9)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "interpretation": "finite falsifier only; weights proportional to stationary density",
        "definition": "right peak translation UDU->UUD; monotone means every vertex weight >= min(endpoint weights)",
        "rows": [audit(r) for r in range(2, args.max_r + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
