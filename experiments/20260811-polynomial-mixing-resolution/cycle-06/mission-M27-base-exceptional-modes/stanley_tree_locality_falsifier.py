#!/usr/bin/env python3
"""Exact falsifier for one-step locality of Stanley's labelled-tree bijection.

For every reduced factorization of the long cycle, form its maximal chain in
NC_n and Stanley's labelled tree T_m (EJC 4(2), 1997, Theorem 3.1 and the
paragraph following Proposition 3.2).  Group chains which differ at one rank.
The tested claim is that such a local rank/Hurwitz move always becomes one
spanning-tree basis exchange, or one Pruefer-coordinate change.

Convention: (p q)(x)=p(q(x)); tuple products are left-to-right.  Exhaustive,
deterministic, seed null.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, a: int, b: int) -> Perm:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def stanley_tree(n: int, raw_edges: tuple[Edge, ...]) -> tuple[Edge, ...]:
    """Return edge set of Stanley's tree, with vertex labels 0,...,n-1."""
    blocks = [{i} for i in range(n)]
    gamma_edges: list[tuple[int, int, int]] = []
    for rank, (a, b) in enumerate(raw_edges, start=1):
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        if ia == ib:
            raise AssertionError("Reduced prefix failed to merge two blocks")
        B, Bp = blocks[ia], blocks[ib]
        if min(B) > min(Bp):
            B, Bp = Bp, B
            ia, ib = ib, ia
        min_bp = min(Bp)
        label = max(x for x in B if x < min_bp)
        gamma_edges.append((label, min_bp, rank))
        merged = B | Bp
        blocks = [block for j, block in enumerate(blocks) if j not in (ia, ib)]
        blocks.append(merged)

    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, rank in gamma_edges:
        adjacency[u].append((v, rank))
        adjacency[v].append((u, rank))
    parent = [-2] * n
    parent[0] = -1
    stack = [0]
    vertex_label = [-1] * n
    vertex_label[0] = 0
    while stack:
        u = stack.pop()
        for v, rank in adjacency[u]:
            if v == parent[u]:
                continue
            if parent[v] != -2:
                raise AssertionError("Gamma_m is not a tree")
            parent[v] = u
            vertex_label[v] = rank
            stack.append(v)
    if any(a < 0 for a in vertex_label):
        raise AssertionError("Gamma_m disconnected")
    out = []
    for u, v, _ in gamma_edges:
        out.append(tuple(sorted((vertex_label[u], vertex_label[v]))))
    return tuple(sorted(out))


def prufer_code(n: int, tree: tuple[Edge, ...]) -> tuple[int, ...]:
    adjacency = [set() for _ in range(n)]
    for u, v in tree:
        adjacency[u].add(v)
        adjacency[v].add(u)
    code = []
    for _ in range(n - 2):
        leaf = min(i for i in range(n) if len(adjacency[i]) == 1)
        neighbor = next(iter(adjacency[leaf]))
        code.append(neighbor)
        adjacency[leaf].remove(neighbor)
        adjacency[neighbor].remove(leaf)
    return tuple(code)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = args.n
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    perms = [transposition(n, *e) for e in edges]
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])

    words: list[tuple[int, ...]] = []
    for indices in itertools.product(range(len(edges)), repeat=n - 1):
        product = identity
        for i in indices:
            product = compose(product, perms[i])
        if product == cycle:
            words.append(indices)
    trees = {w: stanley_tree(n, tuple(edges[i] for i in w)) for w in words}
    if len(set(trees.values())) != len(words):
        raise AssertionError("Implemented Stanley tree map is not bijective")

    max_tree_diff = -1
    max_prufer_diff = -1
    tree_witness = None
    prufer_witness = None
    fiber_sizes = set()
    for rank in range(n - 2):
        groups: dict[tuple[object, ...], list[tuple[int, ...]]] = {}
        for w in words:
            pair_product = compose(perms[w[rank]], perms[w[rank + 1]])
            key = (w[:rank], pair_product, w[rank + 2 :])
            groups.setdefault(key, []).append(w)
        for group in groups.values():
            fiber_sizes.add(len(group))
            for w, z in itertools.combinations(group, 2):
                t_w, t_z = trees[w], trees[z]
                tree_diff = len(set(t_w) ^ set(t_z))
                code_w, code_z = prufer_code(n, t_w), prufer_code(n, t_z)
                code_diff = sum(a != b for a, b in zip(code_w, code_z))
                witness = {
                    "rank_zero_based": rank,
                    "word_1_edges": [edges[i] for i in w],
                    "word_2_edges": [edges[i] for i in z],
                    "stanley_tree_1": t_w,
                    "stanley_tree_2": t_z,
                    "tree_symmetric_difference": tree_diff,
                    "prufer_1": code_w,
                    "prufer_2": code_z,
                    "prufer_hamming_distance": code_diff,
                }
                if tree_diff > max_tree_diff:
                    max_tree_diff = tree_diff
                    tree_witness = witness
                if code_diff > max_prufer_diff:
                    max_prufer_diff = code_diff
                    prufer_witness = witness

    result = {
        "claim_tested": (
            "Every one-rank heat-bath/Hurwitz move becomes a single basis "
            "exchange, respectively a single-coordinate Pruefer update, "
            "under Stanley's labelled-tree bijection."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "n": n,
        "total_factorizations": len(words),
        "denes_expected": n ** (n - 2),
        "rank_two_fiber_sizes": sorted(fiber_sizes),
        "distinct_stanley_trees": len(set(trees.values())),
        "maximum_tree_symmetric_difference": max_tree_diff,
        "maximum_prufer_hamming_distance": max_prufer_diff,
        "tree_witness": tree_witness,
        "prufer_witness": prufer_witness,
        "universal_implication": (
            "A tree symmetric difference greater than two refutes direct "
            "one-edge basis-exchange domination; Pruefer Hamming distance "
            "greater than one refutes direct coordinate-refresh domination."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
