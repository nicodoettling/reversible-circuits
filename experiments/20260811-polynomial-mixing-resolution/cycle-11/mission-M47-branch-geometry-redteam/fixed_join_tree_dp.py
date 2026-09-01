#!/usr/bin/env python3
"""Exact DP for the prefix-join-tree marginal in the minimal identity macro.

For a fixed labeled tree T, a word has prefix join tree T iff every factor
joining two components of the already accepted T-forest is the unique unused
T-edge between those components; factors internal to a component are cuts.
The DP below tracks (prefix permutation, accepted-T-edge mask), and therefore
counts the fiber exactly without enumerating all words in F_N.

The finite output can refute named layer-unimodality/log-concavity claims.  It
does not prove an asymptotic theorem.  Convention: (pq)(x)=p(q(x)); appending
e on the right sends p to p after e, i.e. swaps the two domain entries of p.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


def all_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def prufer_tree(seq: tuple[int, ...], n: int) -> tuple[tuple[int, int], ...]:
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((min(leaf, x), max(leaf, x)))
        degree[leaf] -= 1
        degree[x] -= 1
    last = [i for i, d in enumerate(degree) if d == 1]
    edges.append((min(last), max(last)))
    return tuple(sorted(edges))


def adjacency(tree: tuple[tuple[int, int], ...], n: int) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    return adj


def rooted_code(adj: list[list[int]], u: int, parent: int) -> str:
    return "(" + "".join(sorted(rooted_code(adj, v, u) for v in adj[u] if v != parent)) + ")"


def canonical_shape(tree: tuple[tuple[int, int], ...], n: int) -> str:
    adj = adjacency(tree, n)
    degree = [len(x) for x in adj]
    remaining = n
    leaves = deque(i for i, d in enumerate(degree) if d <= 1)
    while remaining > 2:
        layer = len(leaves)
        remaining -= layer
        for _ in range(layer):
            u = leaves.popleft()
            degree[u] = 0
            for v in adj[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                    if degree[v] == 1:
                        leaves.append(v)
    # The surviving one or two vertices are exactly the pending leaf queue.
    # Their decremented degrees can be zero (a star center after its whole
    # outer layer is removed), so testing degree>0 is off by one.
    centers = list(leaves)
    if not centers:  # singleton only, not used in this mission
        centers = [0]
    if len(centers) == 1:
        return rooted_code(adj, centers[0], -1)
    a, b = centers
    x, y = rooted_code(adj, a, b), rooted_code(adj, b, a)
    return "[" + min(x, y) + max(x, y) + "]"


def tree_stats(tree: tuple[tuple[int, int], ...], n: int) -> dict[str, int]:
    adj = adjacency(tree, n)
    deg = [len(x) for x in adj]
    diameter = 0
    centroid_balance = n
    edge_balance = 0
    rooted_max_branch = 0
    for root in range(n):
        parent = [-2] * n
        parent[root] = -1
        order = [root]
        for u in order:
            for v in adj[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
        dist = [0] * n
        sub = [1] * n
        for u in order[1:]:
            dist[u] = dist[parent[u]] + 1
        for u in reversed(order[1:]):
            sub[parent[u]] += sub[u]
        diameter = max(diameter, max(dist))
        branches = [sub[v] for v in adj[root]]
        centroid_balance = min(centroid_balance, max(branches, default=0))
        if root == 0:
            rooted_max_branch = max(branches, default=0)
        for u in order[1:]:
            edge_balance = max(edge_balance, min(sub[u], n - sub[u]))
    return {
        "diameter": diameter,
        "centroid_balance": centroid_balance,
        "edge_balance": edge_balance,
        "leaf_count": sum(d == 1 for d in deg),
        "max_degree": max(deg),
        "root0_max_branch": rooted_max_branch,
    }


def root0_max_branch(tree: tuple[tuple[int, int], ...], n: int) -> int:
    adj = adjacency(tree, n)
    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for u in order:
        for v in adj[u]:
            if parent[v] == -2:
                parent[v] = u
                order.append(v)
    sub = [1] * n
    for u in reversed(order[1:]):
        sub[parent[u]] += sub[u]
    return max((sub[v] for v in adj[0]), default=0)


def shape_representatives(n: int) -> dict[str, dict]:
    grouped: dict[str, dict] = {}
    for seq in itertools.product(range(n), repeat=n - 2):
        tree = prufer_tree(seq, n)
        code = canonical_shape(tree, n)
        if code not in grouped:
            grouped[code] = {
                "tree": tree,
                "multiplicity": 0,
                "root0_max_branch_multiplicity": Counter(),
            }
        grouped[code]["multiplicity"] += 1
        grouped[code]["root0_max_branch_multiplicity"][root0_max_branch(tree, n)] += 1
    if sum(x["multiplicity"] for x in grouped.values()) != n ** (n - 2):
        raise AssertionError("Cayley multiplicities do not sum correctly")
    return grouped


def fixed_tree_weight(tree: tuple[tuple[int, int], ...], n: int) -> tuple[int, dict]:
    es = all_edges(n)
    edge_to_global = {e: i for i, e in enumerate(es)}
    tree_bit = {edge_to_global[e]: j for j, e in enumerate(tree)}
    full = (1 << (n - 1)) - 1
    masks = 1 << (n - 1)

    # Component ids and allowed mask transition for every forest mask/edge.
    next_mask = [[-1] * len(es) for _ in range(masks)]
    for mask in range(masks):
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x

        for j, (a, b) in enumerate(tree):
            if (mask >> j) & 1:
                union(a, b)
        for ei, (a, b) in enumerate(es):
            if find(a) == find(b):
                next_mask[mask][ei] = mask
            elif ei in tree_bit and not ((mask >> tree_bit[ei]) & 1):
                next_mask[mask][ei] = mask | (1 << tree_bit[ei])

    perms = list(itertools.permutations(range(n)))
    perm_index = {p: i for i, p in enumerate(perms)}
    identity = perm_index[tuple(range(n))]
    perm_next = [[0] * len(es) for _ in perms]
    for pi, p in enumerate(perms):
        for ei, (a, b) in enumerate(es):
            q = list(p)
            q[a], q[b] = q[b], q[a]
            perm_next[pi][ei] = perm_index[tuple(q)]

    dp = {(identity, 0): 1}
    peak_states = 1
    m = 2 * n - 2
    for _step in range(m):
        ndp = defaultdict(int)
        for (pi, mask), count in dp.items():
            for ei in range(len(es)):
                nm = next_mask[mask][ei]
                if nm >= 0:
                    ndp[(perm_next[pi][ei], nm)] += count
        dp = ndp
        peak_states = max(peak_states, len(dp))
    return dp.get((identity, full), 0), {"peak_dp_states": peak_states}


def layer_record(counter: Counter[int]) -> dict:
    support = sorted(counter)
    counts = [counter[x] for x in support]
    i = 1
    while i < len(counts) and counts[i] >= counts[i - 1]:
        i += 1
    while i < len(counts) and counts[i] <= counts[i - 1]:
        i += 1
    return {
        "support": support,
        "counts": counts,
        "unimodal": i == len(counts),
        "log_concave": all(
            counts[j] * counts[j] >= counts[j - 1] * counts[j + 1]
            for j in range(1, len(counts) - 1)
        ),
    }


def run(n: int) -> dict:
    t0 = time.time()
    shapes = shape_representatives(n)
    records = []
    layers = {name: Counter() for name in (
        "diameter", "centroid_balance", "edge_balance", "leaf_count", "max_degree",
        "root0_max_branch",
    )}
    total = 0
    for code, data in sorted(shapes.items()):
        st0 = time.time()
        weight, diagnostics = fixed_tree_weight(data["tree"], n)
        stats = tree_stats(data["tree"], n)
        contribution = data["multiplicity"] * weight
        total += contribution
        for name in layers:
            if name == "root0_max_branch":
                continue
            layers[name][stats[name]] += contribution
        for value, labeled_count in data["root0_max_branch_multiplicity"].items():
            layers["root0_max_branch"][value] += labeled_count * weight
        records.append({
            "shape_code": code,
            "representative_edges": [list(e) for e in data["tree"]],
            "labeled_tree_multiplicity": data["multiplicity"],
            "root0_max_branch_multiplicity": dict(sorted(
                data["root0_max_branch_multiplicity"].items()
            )),
            "fixed_labeled_tree_fiber_weight": weight,
            "weighted_contribution": contribution,
            "stats": stats,
            "elapsed_seconds": time.time() - st0,
            **diagnostics,
        })
    expected = math.factorial(2 * n - 2) * n ** (n - 3)
    if total != expected:
        raise AssertionError(f"weighted tree total {total} != Hurwitz count {expected}")
    return {
        "N": n,
        "m": 2 * n - 2,
        "number_unlabeled_shapes": len(records),
        "weighted_total": total,
        "expected_F_N": expected,
        "elapsed_seconds": time.time() - t0,
        "layers": {name: layer_record(c) for name, c in layers.items()},
        "shape_records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "purpose": "Exact fixed-N falsifier; finite passes imply no asymptotic theorem.",
        "claims_tested": [
            "Actual join-tree diameter/centroid/edge-balance layers are universally unimodal.",
            "Those actual branch layers are universally log-concave.",
        ],
        "convention": "(pq)(x)=p(q(x)); appending e swaps the two domain entries of p",
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "argv": sys.argv,
        "result": run(args.N),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
