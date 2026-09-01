#!/usr/bin/env python3
"""Exact bounded falsifier for join-tree branch-cut shortcuts.

This enumerates the known minimal connected Hurwitz orbit F_N and tests only
the following named universal auxiliary claims:

* diameter and centroid/edge-balance layers are unimodal or log-concave;
* every path-tree state has an adjacent Hurwitz exit from the path-tree cut;
* every state with a perfectly balanced join-tree edge has an adjacent
  Hurwitz exit from that balanced-edge cut.

A finite pass is not evidence for an asymptotic conductance theorem.  A zero
exit witness is an exact refutation of the corresponding pointwise claim.
Convention: (pq)(x)=p(q(x)); R(a,b)=(b,bab).
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


def edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def apply_edge(e: tuple[int, int], x: int) -> int:
    if x == e[0]:
        return e[1]
    if x == e[1]:
        return e[0]
    return x


def conjugate(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    x, y = apply_edge(b, a[0]), apply_edge(b, a[1])
    return (x, y) if x < y else (y, x)


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.s = [1] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.s[x] < self.s[y]:
            x, y = y, x
        self.p[y] = x
        self.s[x] += self.s[y]
        return True


def join_tree(word: list[int], es: list[tuple[int, int]], n: int) -> tuple[tuple[int, int], ...]:
    dsu = DSU(n)
    ans = []
    for idx in word:
        a, b = es[idx]
        if dsu.union(a, b):
            ans.append((a, b))
    if len(ans) != n - 1:
        raise AssertionError("word is not in the minimal connected orbit")
    return tuple(sorted(ans))


def tree_stats(tree: tuple[tuple[int, int], ...], n: int) -> dict[str, int | bool]:
    adj = [[] for _ in range(n)]
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    deg = [len(x) for x in adj]

    diameter = 0
    centroid_balance = n
    edge_balance = 0
    rooted_max_branch = 0
    for root in range(n):
        parent = [-1] * n
        order = [root]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        dist = [0] * n
        for u in order[1:]:
            dist[u] = dist[parent[u]] + 1
        diameter = max(diameter, max(dist))
        sub = [1] * n
        for u in reversed(order[1:]):
            sub[parent[u]] += sub[u]
        branches = [sub[v] for v in adj[root] if parent[v] == root]
        if parent[root] != -1:
            raise AssertionError("root parent corrupted")
        # For this rooted traversal every neighbor of root is a child.
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
        "is_path": max(deg) <= 2,
        "has_balanced_edge": n % 2 == 0 and edge_balance == n // 2,
    }


def decode(code: int, base: int, m: int) -> list[int]:
    word = [0] * m
    for i in range(m):
        word[i], code = code % base, code // base
    return word


def layers(counter: Counter[int]) -> dict:
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


def enumerate_orbit(n: int) -> dict:
    es = edges(n)
    edge_index = {e: i for i, e in enumerate(es)}
    base = len(es)
    m = 2 * n - 2
    powers = [base**i for i in range(m)]
    conj = [[edge_index[conjugate(es[a], es[b])] for b in range(base)] for a in range(base)]

    start_word = []
    for v in range(1, n):
        idx = edge_index[(0, v)]
        start_word.extend((idx, idx))
    start = sum(x * powers[i] for i, x in enumerate(start_word))

    queue = deque([start])
    seen = {start}
    tree_of: dict[int, tuple[tuple[int, int], ...]] = {}
    t0 = time.time()
    while queue:
        code = queue.popleft()
        word = decode(code, base, m)
        tree_of[code] = join_tree(word, es, n)
        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            for u, v in ((b, conj[a][b]), (conj[b][a], a)):
                nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)

    expected = math.factorial(m) * n ** (n - 3)
    if len(seen) != expected:
        raise AssertionError(f"orbit size {len(seen)} != {expected}")

    tree_weight = Counter(tree_of.values())
    tree_stat_cache = {t: tree_stats(t, n) for t in tree_weight}
    layer_counters = {name: Counter() for name in (
        "diameter", "centroid_balance", "edge_balance", "leaf_count",
        "max_degree", "root0_max_branch",
    )}
    path_states = balanced_states = 0
    path_zero = balanced_zero = None
    path_no_degree2_leaf = None
    path_min_leaf_occurrence = Counter()
    path_min_exits = 2 * (m - 1) + 1
    balanced_min_exits = 2 * (m - 1) + 1

    for code, tree in tree_of.items():
        st = tree_stat_cache[tree]
        for name in layer_counters:
            layer_counters[name][int(st[name])] += 1
        in_path = bool(st["is_path"])
        in_balanced = bool(st["has_balanced_edge"])
        if not (in_path or in_balanced):
            continue
        word = decode(code, base, m)
        path_exits = balanced_exits = 0
        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            for u, v in ((b, conj[a][b]), (conj[b][a], a)):
                nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
                nst = tree_stat_cache[tree_of[nxt]]
                if in_path and not bool(nst["is_path"]):
                    path_exits += 1
                if in_balanced and not bool(nst["has_balanced_edge"]):
                    balanced_exits += 1
        if in_path:
            path_states += 1
            path_min_exits = min(path_min_exits, path_exits)
            if path_exits == 0 and path_zero is None:
                path_zero = [list(es[x]) for x in word]
            degree = [0] * n
            occurrences = [0] * n
            for a, b in tree:
                degree[a] += 1
                degree[b] += 1
            for idx in word:
                a, b = es[idx]
                occurrences[a] += 1
                occurrences[b] += 1
            leaf_min = min(occurrences[v] for v in range(n) if degree[v] == 1)
            path_min_leaf_occurrence[leaf_min] += 1
            if leaf_min > 2 and path_no_degree2_leaf is None:
                path_no_degree2_leaf = [list(es[x]) for x in word]
        if in_balanced:
            balanced_states += 1
            balanced_min_exits = min(balanced_min_exits, balanced_exits)
            if balanced_exits == 0 and balanced_zero is None:
                balanced_zero = [list(es[x]) for x in word]

    by_unlabeled_weight = defaultdict(list)
    for tree, weight in tree_weight.items():
        st = tree_stat_cache[tree]
        key = (int(st["diameter"]), int(st["leaf_count"]), int(st["max_degree"]))
        by_unlabeled_weight[str(key)].append(weight)

    return {
        "N": n,
        "m": m,
        "orbit_size": len(seen),
        "expected_orbit_size": expected,
        "elapsed_seconds": time.time() - t0,
        "number_labeled_join_trees": len(tree_weight),
        "tree_fiber_weight_min": min(tree_weight.values()),
        "tree_fiber_weight_max": max(tree_weight.values()),
        "tree_fiber_weight_ratio": max(tree_weight.values()) / min(tree_weight.values()),
        "layers": {name: layers(c) for name, c in layer_counters.items()},
        "path_cut": {
            "states": path_states,
            "conditional_mass_in_F": path_states / len(seen),
            "minimum_oriented_Hurwitz_exits": path_min_exits,
            "first_zero_exit_witness": path_zero,
            "minimum_leaf_occurrence_distribution": dict(sorted(path_min_leaf_occurrence.items())),
            "first_witness_with_no_degree2_tree_leaf": path_no_degree2_leaf,
        },
        "balanced_edge_cut": {
            "states": balanced_states,
            "conditional_mass_in_F": balanced_states / len(seen),
            "minimum_oriented_Hurwitz_exits": balanced_min_exits if n % 2 == 0 else None,
            "first_zero_exit_witness": balanced_zero,
        },
        "weights_grouped_by_coarse_shape": {
            key: {"min": min(ws), "max": max(ws), "distinct": sorted(set(ws))}
            for key, ws in sorted(by_unlabeled_weight.items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "purpose": "Exact finite falsifier only; finite passes imply no asymptotic theorem.",
        "claims_tested": [
            "Branch-statistic layers are universally unimodal/log-concave.",
            "Every path join-tree state has an adjacent Hurwitz exit from the path cut.",
            "Every path join-tree state has a tree leaf occurring in exactly two factors.",
            "Every perfect-balanced-edge state has an adjacent Hurwitz exit from that cut.",
        ],
        "convention": "(pq)(x)=p(q(x)); word product left-to-right; R(a,b)=(b,bab)",
        "seed": None,
        "python": platform.python_version(),
        "argv": sys.argv,
        "result": enumerate_orbit(args.N),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
