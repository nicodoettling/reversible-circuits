#!/usr/bin/env python3
"""Exact N=4 falsifier for fixed-join-tree restriction and chronology cuts.

Finite connectivity cannot prove a universal restriction theorem.  A
disconnect would refute it.  The script also computes literal full-K escape
for named join-rank and leaf-null-separation cuts, including r=3,4,5.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Word = tuple[int, ...]
Edge = tuple[int, int]


def edges(n: int) -> list[Edge]:
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


def append_edge(p: Permutation, e: Edge) -> Permutation:
    q = list(p)
    q[e[0]], q[e[1]] = q[e[1]], q[e[0]]
    return tuple(q)


def evaluate(n: int, es: list[Edge], word) -> Permutation:
    p = tuple(range(n))
    for idx in word:
        p = append_edge(p, es[idx])
    return p


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[b] = a
        return True


def join_tree_and_order(word: Word, es: list[Edge], n: int):
    dsu = DSU(n)
    order = []
    for j, idx in enumerate(word):
        a, b = es[idx]
        if dsu.union(a, b):
            order.append(((a, b), j))
    if len(order) != n - 1:
        return None, None
    return tuple(sorted(edge for edge, _ in order)), tuple(order)


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def compose(p: Permutation, q: Permutation) -> Permutation:
    return tuple(p[q[i]] for i in range(len(p)))


def erase_label(p: Permutation, v: int) -> Permutation:
    labels = [x for x in range(len(p)) if x != v]
    rank = {x: i for i, x in enumerate(labels)}
    out = []
    for x in labels:
        y = p[x]
        if y == v:
            y = p[v]
        out.append(rank[y])
    return tuple(out)


def strand_nulls(word: Word, es: list[Edge], n: int, v: int) -> tuple[int, int]:
    p = tuple(range(n))
    old = erase_label(p, v)
    nulls = []
    for j, idx in enumerate(word):
        p = append_edge(p, es[idx])
        new = erase_label(p, v)
        delta = compose(inverse(old), new)
        if all(delta[x] == x for x in range(n - 1)):
            nulls.append(j)
        old = new
    if len(nulls) != 2:
        raise AssertionError((word, v, nulls))
    return nulls[0], nulls[1]


def tree_leaves(tree: tuple[Edge, ...], n: int) -> list[int]:
    degree = [0] * n
    for a, b in tree:
        degree[a] += 1
        degree[b] += 1
    return [v for v, d in enumerate(degree) if d == 1]


def enumerate_fibers(n: int, m: int, es: list[Edge]):
    identity = tuple(range(n))
    grouped = defaultdict(list)
    identity_count = 0
    for word in itertools.product(range(len(es)), repeat=m):
        if evaluate(n, es, word) != identity:
            continue
        identity_count += 1
        tree, order = join_tree_and_order(word, es, n)
        if tree is not None:
            grouped[tree].append((word, order))
    return identity_count, grouped


def block_fibers(n: int, es: list[Edge], lengths=(3, 4, 5)):
    answer = {}
    for r in lengths:
        grouped = defaultdict(list)
        for block in itertools.product(range(len(es)), repeat=r):
            grouped[evaluate(n, es, block)].append(block)
        answer[r] = {p: tuple(blocks) for p, blocks in grouped.items()}
    return answer


class IndexDSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.p[b] = a
        self.size[a] += self.size[b]


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def audit_tree(
    n: int,
    m: int,
    es: list[Edge],
    tree: tuple[Edge, ...],
    records,
    fibers,
):
    words = [word for word, _order in records]
    word_set = set(words)
    index = {word: j for j, word in enumerate(words)}
    dsu = IndexDSU(len(words))
    adjacency = [set() for _ in words]
    internal_mechanisms = Counter()
    all_mechanisms = {}
    for word in words:
        mechanisms = []
        for r in (3, 4, 5):
            window_weight = Fraction(1, 6 * (m - r + 1))
            for i in range(m - r + 1):
                product = evaluate(n, es, word[i : i + r])
                options = fibers[r][product]
                option_weight = window_weight / len(options)
                for block in options:
                    target = word[:i] + block + word[i + r :]
                    mechanisms.append((r, target, option_weight))
                    if target in word_set and target != word:
                        a, b = index[word], index[target]
                        dsu.union(a, b)
                        adjacency[a].add(b)
                        adjacency[b].add(a)
                        internal_mechanisms[r] += 1
        all_mechanisms[word] = mechanisms

    components = defaultdict(list)
    for j, word in enumerate(words):
        components[dsu.find(j)].append(word)
    component_sizes = sorted((len(x) for x in components.values()), reverse=True)

    # Exact unweighted support-graph diameter, only when connected.
    diameter = None
    if len(component_sizes) == 1:
        diameter = 0
        for start in range(len(words)):
            distance = [-1] * len(words)
            distance[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in adjacency[u]:
                    if distance[v] < 0:
                        distance[v] = distance[u] + 1
                        queue.append(v)
            if min(distance) < 0:
                raise AssertionError("DSU/adjacency mismatch")
            diameter = max(diameter, max(distance))

    canonical_edge = min(tree)
    canonical_leaf = min(tree_leaves(tree, n))
    stats = {}
    for word, order in records:
        rank = next(k + 1 for k, (edge, _position) in enumerate(order) if edge == canonical_edge)
        first_null, second_null = strand_nulls(word, es, n, canonical_leaf)
        stats[word] = {
            "join_rank": rank,
            "leaf_null_separation": second_null - first_null,
        }

    distributions = {
        name: dict(sorted(Counter(data[name] for data in stats.values()).items()))
        for name in ("join_rank", "leaf_null_separation")
    }
    cuts = []
    for name, distribution in distributions.items():
        values = sorted(distribution)
        for threshold in values[:-1]:
            subset = {word for word in words if stats[word][name] <= threshold}
            if len(subset) > len(words) // 2:
                subset = word_set - subset
                orientation = "gt"
            else:
                orientation = "le"
            if not subset:
                continue
            by_r_full = {r: Fraction(0) for r in (3, 4, 5)}
            by_r_restricted = {r: Fraction(0) for r in (3, 4, 5)}
            for word in subset:
                for r, target, weight in all_mechanisms[word]:
                    if target not in subset:
                        by_r_full[r] += weight
                        if target in word_set:
                            by_r_restricted[r] += weight
            full_escape = sum(by_r_full.values(), Fraction(0)) / len(subset)
            restricted_escape = sum(by_r_restricted.values(), Fraction(0)) / len(subset)
            cuts.append({
                "statistic": name,
                "threshold": threshold,
                "smaller_side_orientation": orientation,
                "smaller_side_size": len(subset),
                "full_K_escape": fraction_text(full_escape),
                "restricted_escape": fraction_text(restricted_escape),
                "full_by_r": {str(r): fraction_text(by_r_full[r] / len(subset)) for r in (3, 4, 5)},
                "restricted_by_r": {
                    str(r): fraction_text(by_r_restricted[r] / len(subset)) for r in (3, 4, 5)
                },
            })

    representative_components = []
    for comp in sorted(components.values(), key=len, reverse=True)[:5]:
        representative_components.append({
            "size": len(comp),
            "representative_word_edges": [[list(es[idx]) for idx in comp[0]]],
            "join_rank_values": sorted({stats[word]["join_rank"] for word in comp}),
            "leaf_null_separation_values": sorted({
                stats[word]["leaf_null_separation"] for word in comp
            }),
        })

    return {
        "tree_edges": [list(e) for e in tree],
        "fiber_size": len(words),
        "components": len(component_sizes),
        "component_sizes": component_sizes,
        "support_graph_diameter": diameter,
        "undirected_internal_support_edges": sum(len(x) for x in adjacency) // 2,
        "directed_internal_mechanisms_by_r": {
            str(r): internal_mechanisms[r] for r in (3, 4, 5)
        },
        "canonical_edge": list(canonical_edge),
        "canonical_leaf": canonical_leaf,
        "statistic_distributions": distributions,
        "named_cut_flows": cuts,
        "representative_components": representative_components,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.N != 4:
        raise SystemExit("This bounded exact harness is intentionally scoped to N=4")
    n = args.N
    m = 2 * n - 2
    es = edges(n)
    identity_count, grouped = enumerate_fibers(n, m, es)
    if identity_count != 3936 or sum(len(x) for x in grouped.values()) != 2880:
        raise AssertionError((identity_count, sum(len(x) for x in grouped.values())))
    fibers = block_fibers(n, es)
    tree_rows = [
        audit_tree(n, m, es, tree, records, fibers)
        for tree, records in sorted(grouped.items())
    ]
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
        "convention": "(pq)(x)=p(q(x)); right-appending swaps domain entries",
        "kernel": "lazy K; nontrivial mechanisms use 1/[6(m-r+1)|F_r(product)|]",
        "claims_tested": [
            "Every fixed labeled join-tree fiber at N=4 is connected under rejected-exit r=3,4,5 heat-bath support.",
            "Join-rank and leaf-null-separation threshold cuts can be trapped after full K exits are included.",
        ],
        "scope_warning": "N=4 connectivity and positive flow can falsify but cannot prove any universal asymptotic theorem.",
        "summary": {
            "N": n,
            "m": m,
            "identity_words": identity_count,
            "minimal_full_support_words": sum(len(x) for x in grouped.values()),
            "labeled_tree_fibers": len(grouped),
            "all_restrictions_connected": all(row["components"] == 1 for row in tree_rows),
            "maximum_support_diameter": max(row["support_graph_diameter"] for row in tree_rows),
        },
        "trees": tree_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
