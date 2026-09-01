#!/usr/bin/env python3
"""Exact bounded falsifier for replanting-to-leaf-rotation templates.

Trees are immutable tuples of child trees.  The M35 rotation replaces two
consecutive children `(leaf, Q)` of a parent by the unary child `(Q)`, and
the reverse replaces a unary child `(Q)` by `(leaf, Q)`.

This script tests graph connectivity and shortest rotation distances of all
distinct shape-level root-preserving leaf replants.  Finite success is not a
proof of polynomial comparison.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
from functools import lru_cache

Tree = tuple["Tree", ...]


@lru_cache(None)
def trees(edges: int) -> tuple[Tree, ...]:
    if edges == 0:
        return ((),)
    ans: list[Tree] = []

    def compositions(total: int, prefix: tuple[int, ...] = ()):
        if total == 0:
            yield prefix
            return
        for part in range(1, total + 1):
            yield from compositions(total - part, prefix + (part,))

    for parts in compositions(edges):
        pools = [trees(part - 1) for part in parts]
        stack: list[Tree] = []

        def product(i: int):
            if i == len(pools):
                ans.append(tuple(stack))
                return
            for child in pools[i]:
                stack.append(child)
                product(i + 1)
                stack.pop()

        product(0)
    return tuple(ans)


def size(t: Tree) -> int:
    return sum(1 + size(c) for c in t)


def weight_denominator(t: Tree) -> int:
    value = math.factorial(len(t))
    for child in t:
        value *= weight_denominator(child)
    return value


def paths(t: Tree, prefix: tuple[int, ...] = ()):
    yield prefix, t
    for i, child in enumerate(t):
        yield from paths(child, prefix + (i,))


def get(t: Tree, path: tuple[int, ...]) -> Tree:
    for i in path:
        t = t[i]
    return t


def replace(t: Tree, path: tuple[int, ...], new: Tree) -> Tree:
    if not path:
        return new
    i = path[0]
    return t[:i] + (replace(t[i], path[1:], new),) + t[i + 1 :]


def rotations(t: Tree) -> set[Tree]:
    out: set[Tree] = set()
    for path, node in paths(t):
        # Forward: leaf followed by one sibling subtree -> unary subtree.
        for i in range(len(node) - 1):
            if node[i] == ():
                new_node = node[:i] + ((node[i + 1],),) + node[i + 2 :]
                out.add(replace(t, path, new_node))
        # Reverse: unary child -> leaf followed by its unique child.
        for i, child in enumerate(node):
            if len(child) == 1:
                new_node = node[:i] + ((), child[0]) + node[i + 1 :]
                out.add(replace(t, path, new_node))
    out.discard(t)
    return out


def remove_at(t: Tree, parent: tuple[int, ...], index: int) -> Tree:
    node = get(t, parent)
    assert node[index] == ()
    return replace(t, parent, node[:index] + node[index + 1 :])


def insert_at(t: Tree, parent: tuple[int, ...], index: int) -> Tree:
    node = get(t, parent)
    return replace(t, parent, node[:index] + ((),) + node[index:])


def replant_neighbors(t: Tree) -> set[Tree]:
    out: set[Tree] = set()
    leaf_sites = []
    for parent, node in paths(t):
        for i, child in enumerate(node):
            if child == ():
                leaf_sites.append((parent, i))
    for parent, i in leaf_sites:
        residual = remove_at(t, parent, i)
        for destination, node in paths(residual):
            for slot in range(len(node) + 1):
                out.add(insert_at(residual, destination, slot))
    out.discard(t)
    return out


def distances(start: Tree, adjacency: dict[Tree, set[Tree]]) -> dict[Tree, int]:
    dist = {start: 0}
    queue = collections.deque([start])
    while queue:
        x = queue.popleft()
        for y in adjacency[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                queue.append(y)
    return dist


def dyck(t: Tree) -> str:
    return "".join("U" + dyck(c) + "D" for c in t)


def run(r_max: int):
    records = []
    witnesses = []
    for r in range(1, r_max + 1):
        states = trees(r)
        adj = {t: rotations(t) for t in states}
        directed_edges = sum(map(len, adj.values()))
        all_dist = {t: distances(t, adj) for t in states}
        connected = all(len(d) == len(states) for d in all_dist.values())
        max_replant_distance = -1
        max_pair = None
        replant_pairs = 0
        for x in states:
            for y in replant_neighbors(x):
                replant_pairs += 1
                d = all_dist[x].get(y)
                if d is None:
                    max_replant_distance = None
                    max_pair = (x, y)
                    break
                if d > max_replant_distance:
                    max_replant_distance = d
                    max_pair = (x, y)
            if max_replant_distance is None:
                break
        records.append(
            {
                "r": r,
                "states": len(states),
                "undirected_rotation_edges": directed_edges // 2,
                "connected": connected,
                "directed_distinct_replant_pairs": replant_pairs,
                "max_replant_rotation_distance": max_replant_distance,
                "min_weight_denominator": min(weight_denominator(t) for t in states),
                "max_weight_denominator": max(weight_denominator(t) for t in states),
            }
        )
        if max_pair is not None:
            witnesses.append(
                {
                    "r": r,
                    "distance": max_replant_distance,
                    "source": dyck(max_pair[0]),
                    "target": dyck(max_pair[1]),
                }
            )
    return {
        "claim_tested": (
            "Every shape-level root-preserving leaf replant through r_max is "
            "connected by exact UD P <-> U P D rotations, and record its "
            "maximum shortest distance. Finite success cannot prove a universal bound."
        ),
        "python": platform.python_version(),
        "deterministic": True,
        "seed": None,
        "records": records,
        "max_distance_witnesses": witnesses,
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
