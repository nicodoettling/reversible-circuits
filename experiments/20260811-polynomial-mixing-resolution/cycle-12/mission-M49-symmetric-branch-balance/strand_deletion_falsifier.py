#!/usr/bin/env python3
"""Exact bounded falsifier for the M49 strand-deletion lemmas.

This enumerates the minimal connected Hurwitz orbit F_N and can falsify:

1. erasing a join-tree leaf produces exactly two null increments and a word
   of F_(N-1) whose join tree is the old join tree minus that leaf;
2. for fixed deleted word, leaf, and two null positions, the deletion fiber
   has size at most (N-1)^2;
3. every non-endpoint balance threshold has a threshold-preserving leaf, and
   the even perfectly-balanced endpoint deletes to the maximum lower layer;
4. centroid branch radius equals maximum smaller edge side.

A finite pass is not a universal proof.  Convention: (pq)(x)=p(q(x)); a
right-appended transposition swaps the corresponding domain entries.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
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


def decode(code: int, base: int, m: int) -> list[int]:
    ans = [0] * m
    for i in range(m):
        ans[i], code = code % base, code // base
    return ans


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


def join_tree(word: tuple[int, ...] | list[int], es: list[tuple[int, int]], n: int) -> tuple[tuple[int, int], ...]:
    dsu = DSU(n)
    out = []
    for idx in word:
        a, b = es[idx]
        if dsu.union(a, b):
            out.append((a, b))
    if len(out) != n - 1:
        raise AssertionError("not a minimal connected join tree")
    return tuple(sorted(out))


def tree_data(tree: tuple[tuple[int, int], ...], n: int) -> tuple[int, int, tuple[int, ...]]:
    adj = [[] for _ in range(n)]
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    leaves = tuple(i for i in range(n) if len(adj[i]) == 1)
    edge_balance = 0
    centroid = n
    for root in range(n):
        parent = [-1] * n
        order = [root]
        for u in order:
            for z in adj[u]:
                if z != parent[u]:
                    parent[z] = u
                    order.append(z)
        sub = [1] * n
        for z in reversed(order[1:]):
            sub[parent[z]] += sub[z]
        branches = [sub[z] for z in adj[root]]
        centroid = min(centroid, max(branches, default=0))
        for z in order[1:]:
            edge_balance = max(edge_balance, min(sub[z], n - sub[z]))
    return edge_balance, centroid, leaves


def orbit(n: int) -> tuple[list[tuple[int, int]], set[int]]:
    es = edges(n)
    edge_index = {e: i for i, e in enumerate(es)}
    b = len(es)
    m = 2 * n - 2
    powers = [b**i for i in range(m)]
    conj = [[edge_index[conjugate(es[a], es[c])] for c in range(b)] for a in range(b)]
    start_word = []
    for v in range(1, n):
        z = edge_index[(0, v)]
        start_word.extend((z, z))
    start = sum(z * powers[i] for i, z in enumerate(start_word))
    seen = {start}
    queue = deque([start])
    while queue:
        code = queue.popleft()
        word = decode(code, b, m)
        for i in range(m - 1):
            a, c = word[i], word[i + 1]
            for x, y in ((c, conj[a][c]), (conj[c][a], a)):
                nxt = code + (x - a) * powers[i] + (y - c) * powers[i + 1]
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    expected = math.factorial(m) * n ** (n - 3)
    if len(seen) != expected:
        raise AssertionError((n, len(seen), expected))
    return es, seen


def append_transposition(p: tuple[int, ...], e: tuple[int, int]) -> tuple[int, ...]:
    q = list(p)
    q[e[0]], q[e[1]] = q[e[1]], q[e[0]]
    return tuple(q)


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def erase_label(p: tuple[int, ...], v: int) -> tuple[int, ...]:
    labels = [x for x in range(len(p)) if x != v]
    rank = {x: i for i, x in enumerate(labels)}
    out = []
    for x in labels:
        y = p[x]
        if y == v:
            y = p[v]
        out.append(rank[y])
    return tuple(out)


def delete_strand(word: list[int], es: list[tuple[int, int]], n: int, v: int):
    base_labels = [x for x in range(n) if x != v]
    rank = {x: i for i, x in enumerate(base_labels)}
    base_es = edges(n - 1)
    base_index = {e: i for i, e in enumerate(base_es)}
    p = tuple(range(n))
    old = erase_label(p, v)
    out = []
    nulls = []
    for j, idx in enumerate(word):
        p = append_transposition(p, es[idx])
        new = erase_label(p, v)
        delta = compose(inverse(old), new)
        moved = [x for x in range(n - 1) if delta[x] != x]
        if not moved:
            nulls.append(j)
        elif len(moved) == 2 and delta[moved[0]] == moved[1] and delta[moved[1]] == moved[0]:
            e = tuple(sorted(moved))
            out.append(base_index[e])
        else:
            raise AssertionError(("non-transposition projection", n, v, j, delta))
        old = new
    if p != tuple(range(n)):
        raise AssertionError("input did not close")
    return tuple(out), tuple(nulls), base_es


def audit(n: int) -> dict:
    t0 = time.time()
    es, seen = orbit(n)
    b = len(es)
    m = 2 * n - 2
    tree_cache = {}
    stats_cache = {}
    threshold_counts = Counter()
    fiber = Counter()
    deletion_pairs = 0
    preserving_leaf_failures = 0
    endpoint_leaf_failures = 0
    for code in seen:
        word = decode(code, b, m)
        tree = join_tree(word, es, n)
        if tree not in stats_cache:
            stats_cache[tree] = tree_data(tree, n)
        bal, cent, leaves = stats_cache[tree]
        if bal != cent:
            raise AssertionError(("centroid mismatch", tree, bal, cent))
        threshold_counts[bal] += 1
        good_by_q = {q: False for q in range(1, (n - 1) // 2 + 1)}
        for v in leaves:
            out, nulls, base_es = delete_strand(word, es, n, v)
            if len(nulls) != 2 or len(out) != m - 2:
                raise AssertionError(("wrong null count", n, code, v, nulls))
            out_tree = join_tree(out, base_es, n - 1)
            relabel = {x: i for i, x in enumerate(x for x in range(n) if x != v)}
            expected_tree = tuple(sorted(tuple(sorted((relabel[a], relabel[c]))) for a, c in tree if v not in (a, c)))
            if out_tree != expected_tree:
                raise AssertionError(("tree deletion mismatch", n, code, v, out_tree, expected_tree))
            out_bal, out_cent, _ = tree_data(out_tree, n - 1)
            if out_bal != out_cent:
                raise AssertionError("base centroid mismatch")
            for q in good_by_q:
                if bal >= q and out_bal >= q:
                    good_by_q[q] = True
            if n % 2 == 0 and bal == n // 2 and out_bal != n // 2 - 1:
                endpoint_leaf_failures += 1
            fiber[(v, out, nulls)] += 1
            deletion_pairs += 1
        for q, good in good_by_q.items():
            if bal >= q and not good:
                preserving_leaf_failures += 1
    max_fiber = max(fiber.values(), default=0)
    bound = (n - 1) ** 2
    if max_fiber > bound:
        raise AssertionError(("fiber bound", n, max_fiber, bound))
    if preserving_leaf_failures or endpoint_leaf_failures:
        raise AssertionError((preserving_leaf_failures, endpoint_leaf_failures))

    # Exact tail inequalities against an independently enumerated F_(N-1).
    base_es, base_seen = orbit(n - 1)
    base_b = len(base_es)
    base_m = 2 * (n - 1) - 2
    base_layers = Counter()
    for code in base_seen:
        word = decode(code, base_b, base_m)
        bal, cent, _ = tree_data(join_tree(word, base_es, n - 1), n - 1)
        if bal != cent:
            raise AssertionError("base centroid mismatch")
        base_layers[bal] += 1
    tails = {}
    L = math.comb(m, 2) * (n - 1) ** 2
    for q in range(1, n // 2 + 1):
        hn = sum(c for z, c in threshold_counts.items() if z >= q)
        bq = q if q < n / 2 else q - 1
        hb = sum(c for z, c in base_layers.items() if z >= bq)
        tails[str(q)] = {
            "H_N": hn,
            "base_threshold": bq,
            "H_N_minus_1": hb,
            "upper_bound": n * L * hb,
            "inequality_holds": hn <= n * L * hb,
        }
        if hn > n * L * hb:
            raise AssertionError(("tail count bound", n, q))
    return {
        "N": n,
        "m": m,
        "orbit_size": len(seen),
        "deletion_pairs": deletion_pairs,
        "distinct_fixed_position_fibers": len(fiber),
        "max_fixed_position_fiber": max_fiber,
        "proved_upper_bound_tested": bound,
        "edge_balance_layers": {str(k): threshold_counts[k] for k in sorted(threshold_counts)},
        "base_edge_balance_layers": {str(k): base_layers[k] for k in sorted(base_layers)},
        "tail_count_checks": tails,
        "preserving_leaf_failures": preserving_leaf_failures,
        "endpoint_leaf_failures": endpoint_leaf_failures,
        "elapsed_seconds": time.time() - t0,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.N < 3:
        raise SystemExit("N must be at least 3")
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": "(pq)(x)=p(q(x)); right-appending a transposition swaps domain entries",
        "claims_tested": [
            "Canonical deletion at every prefix-join-tree leaf has exactly two null increments and output join tree T-v.",
            "For fixed v, output word, and null positions, the leaf-deletion fiber is at most (N-1)^2.",
            "Every q<N/2 balanced-edge threshold tree has a threshold-preserving leaf; the even endpoint deletes to q-1.",
            "Maximum smaller edge side equals minimum largest centroid branch.",
        ],
        "scope_warning": "Finite passes can falsify these universal lemmas but cannot prove them.",
        "result": audit(args.N),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
