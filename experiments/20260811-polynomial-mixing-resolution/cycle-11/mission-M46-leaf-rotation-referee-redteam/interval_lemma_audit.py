#!/usr/bin/env python3
"""Exhaustive bounded falsifier for M35 Lemma 2.1.

This enumerates every noncrossing spanning tree on cyclic labels 0,...,n-1.
It checks that its forward-degree sequence encodes a plane tree whose child
subtree intervals agree with the components obtained by deleting each vertex
from the corresponding induced interval.  It also checks the two edge
consequences used in the leaf-rotation proof.  Passing finitely many n cannot
prove the universal lemma; one failure would refute it.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def crosses(e, f):
    a, b = sorted(e)
    c, d = sorted(f)
    if len({a, b, c, d}) < 4:
        return False
    return (a < c < b < d) or (c < a < d < b)


def connected(n, edges):
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adjacency[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return len(seen) == n, adjacency


def plane_children(degrees):
    n = len(degrees)
    children = [[] for _ in range(n)]
    remaining = list(degrees)
    stack = [0]
    for vertex in range(1, n):
        while stack and remaining[stack[-1]] == 0:
            stack.pop()
        if not stack:
            return None
        parent = stack[-1]
        children[parent].append(vertex)
        remaining[parent] -= 1
        stack.append(vertex)
    while stack and remaining[stack[-1]] == 0:
        stack.pop()
    if stack:
        return None
    return children


def subtree_sets(children):
    n = len(children)
    result = [None] * n

    def visit(v):
        vertices = {v}
        for child in children[v]:
            vertices.update(visit(child))
        result[v] = vertices
        return vertices

    visit(0)
    return result


def components_after_delete(vertices, deleted, adjacency):
    remaining = set(vertices) - {deleted}
    answer = []
    while remaining:
        seed = min(remaining)
        component = {seed}
        stack = [seed]
        remaining.remove(seed)
        while stack:
            v = stack.pop()
            for u in adjacency[v]:
                if u in remaining and u in vertices:
                    remaining.remove(u)
                    component.add(u)
                    stack.append(u)
        answer.append(component)
    return answer


def audit(n):
    possible = list(itertools.combinations(range(n), 2))
    examined = 0
    noncrossing_trees = 0
    leaf_checks = 0
    for edges in itertools.combinations(possible, n - 1):
        examined += 1
        if any(crosses(e, f) for e, f in itertools.combinations(edges, 2)):
            continue
        is_connected, adjacency = connected(n, edges)
        if not is_connected:
            continue
        noncrossing_trees += 1
        edge_set = {tuple(sorted(edge)) for edge in edges}
        degrees = tuple(sum(u > v for u in adjacency[v]) for v in range(n))
        children = plane_children(degrees)
        if children is None:
            return {"ok": False, "failure": "invalid degree sequence", "edges": edges, "degrees": degrees}
        subtrees = subtree_sets(children)
        for v in range(n):
            actual = {frozenset(x) for x in components_after_delete(subtrees[v], v, adjacency)}
            expected = {frozenset(subtrees[child]) for child in children[v]}
            if actual != expected:
                return {
                    "ok": False,
                    "failure": "component mismatch",
                    "n": n,
                    "edges": edges,
                    "degrees": degrees,
                    "vertex": v,
                    "actual": [sorted(x) for x in actual],
                    "expected": [sorted(x) for x in expected],
                }
            for position, child in enumerate(children[v][:-1]):
                if degrees[child] != 0:
                    continue
                leaf_checks += 1
                next_child = children[v][position + 1]
                if tuple(sorted((v, child))) not in edge_set:
                    return {"ok": False, "failure": "missing leaf edge", "edges": edges, "degrees": degrees, "vertex": v, "leaf": child}
                attachments = [u for u in subtrees[next_child] if tuple(sorted((v, u))) in edge_set]
                if len(attachments) != 1:
                    return {"ok": False, "failure": "next-child attachment", "edges": edges, "degrees": degrees, "vertex": v, "leaf": child, "attachments": attachments}
    return {
        "ok": True,
        "n": n,
        "edge_subsets_examined": examined,
        "noncrossing_trees": noncrossing_trees,
        "canonical_nonlast_leaf_checks": leaf_checks,
        "scope": "bounded falsifier only",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for n in range(2, args.n_max + 1):
        row = audit(n)
        rows.append(row)
        if not row["ok"]:
            break
    args.output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
