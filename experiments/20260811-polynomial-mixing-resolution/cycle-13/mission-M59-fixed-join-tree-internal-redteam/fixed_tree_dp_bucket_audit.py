#!/usr/bin/env python3
"""Exact fixed-tree fiber and block-bucket audit for N=5.

This is a bounded falsifier, not an asymptotic proof.  It enumerates a single
fixed labeled join-tree fiber using the exact prefix automaton, then represents
the literal rejected-exit H3/H4/H5 restriction as a union of conditional
cliques.  It also computes exact full-K and rejected-exit flow for named thin
chronology cuts.
"""

from __future__ import annotations

import argparse
import functools
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Edge = tuple[int, int]
Word = tuple[int, ...]


def edges(n: int) -> list[Edge]:
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


def append_edge(p: Permutation, e: Edge) -> Permutation:
    """Return p after right multiplication by transposition e."""
    q = list(p)
    q[e[0]], q[e[1]] = q[e[1]], q[e[0]]
    return tuple(q)


def evaluate(n: int, all_edges: list[Edge], word) -> Permutation:
    p = tuple(range(n))
    for idx in word:
        p = append_edge(p, all_edges[idx])
    return p


def compose(p: Permutation, q: Permutation) -> Permutation:
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


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


def strand_nulls(word: Word, all_edges: list[Edge], n: int, v: int) -> tuple[int, int]:
    p = tuple(range(n))
    old = erase_label(p, v)
    nulls = []
    for j, idx in enumerate(word):
        p = append_edge(p, all_edges[idx])
        new = erase_label(p, v)
        delta = compose(inverse(old), new)
        if all(delta[x] == x for x in range(n - 1)):
            nulls.append(j)
        old = new
    if len(nulls) != 2:
        raise AssertionError((word, v, nulls))
    return nulls[0], nulls[1]


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def tree_shapes() -> dict[str, tuple[Edge, ...]]:
    return {
        "star": ((0, 1), (0, 2), (0, 3), (0, 4)),
        "path": ((0, 1), (0, 3), (1, 2), (2, 4)),
        "tshape": ((0, 1), (0, 2), (0, 3), (3, 4)),
    }


def components_from_mask(n: int, tree: tuple[Edge, ...], mask: int) -> tuple[int, ...]:
    dsu = DSU(n)
    for bit, (a, b) in enumerate(tree):
        if mask & (1 << bit):
            dsu.union(a, b)
    return tuple(dsu.find(v) for v in range(n))


def transition_table(n: int, tree: tuple[Edge, ...], all_edges: list[Edge]):
    tree_bit = {e: bit for bit, e in enumerate(tree)}
    table = {}
    for mask in range(1 << (n - 1)):
        component = components_from_mask(n, tree, mask)
        for idx, e in enumerate(all_edges):
            a, b = e
            if component[a] == component[b]:
                next_mask = mask
            elif e in tree_bit and not (mask & (1 << tree_bit[e])):
                next_mask = mask | (1 << tree_bit[e])
            else:
                next_mask = None
            table[(mask, idx)] = next_mask
    return table


def enumerate_fixed_tree(n: int, tree: tuple[Edge, ...], all_edges: list[Edge]):
    """Enumerate exactly via positive-completion DP states."""
    m = 2 * n - 2
    identity = tuple(range(n))
    full_mask = (1 << (n - 1)) - 1
    transitions = transition_table(n, tree, all_edges)

    @functools.lru_cache(maxsize=None)
    def count(step: int, p: Permutation, mask: int) -> int:
        if step == m:
            return int(p == identity and mask == full_mask)
        total = 0
        for idx, e in enumerate(all_edges):
            next_mask = transitions[(mask, idx)]
            if next_mask is None:
                continue
            total += count(step + 1, append_edge(p, e), next_mask)
        return total

    expected = count(0, identity, 0)
    words: list[Word] = []

    def visit(step: int, p: Permutation, mask: int, prefix: list[int]) -> None:
        if step == m:
            if p != identity or mask != full_mask:
                raise AssertionError("positive-completion walk ended incorrectly")
            words.append(tuple(prefix))
            return
        for idx, e in enumerate(all_edges):
            next_mask = transitions[(mask, idx)]
            if next_mask is None:
                continue
            next_p = append_edge(p, e)
            if count(step + 1, next_p, next_mask) == 0:
                continue
            prefix.append(idx)
            visit(step + 1, next_p, next_mask, prefix)
            prefix.pop()

    visit(0, identity, 0, [])
    if len(words) != expected or len(set(words)) != expected:
        raise AssertionError((len(words), expected, len(set(words))))
    return words, count.cache_info()


def verify_join_tree(n: int, tree: tuple[Edge, ...], all_edges: list[Edge], word: Word):
    dsu = DSU(n)
    joins = []
    for position, idx in enumerate(word):
        a, b = all_edges[idx]
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            joins.append(((a, b), position))
    if tuple(sorted(e for e, _ in joins)) != tuple(sorted(tree)):
        raise AssertionError((tree, word, joins))
    return tuple(joins)


def product_counts(n: int, all_edges: list[Edge], r: int) -> dict[Permutation, int]:
    counts = Counter()
    for block in itertools.product(range(len(all_edges)), repeat=r):
        counts[evaluate(n, all_edges, block)] += 1
    if sum(counts.values()) != len(all_edges) ** r:
        raise AssertionError("product count mismatch")
    return dict(counts)


def identity_word_count(n: int, all_edges: list[Edge], m: int) -> int:
    identity = tuple(range(n))
    counts = {identity: 1}
    for _ in range(m):
        nxt = Counter()
        for p, value in counts.items():
            for e in all_edges:
                nxt[append_edge(p, e)] += value
        counts = dict(nxt)
    return counts.get(identity, 0)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def tree_leaves(n: int, tree: tuple[Edge, ...]) -> list[int]:
    degree = [0] * n
    for a, b in tree:
        degree[a] += 1
        degree[b] += 1
    return [v for v, d in enumerate(degree) if d == 1]


def word_statistics(
    n: int,
    tree: tuple[Edge, ...],
    all_edges: list[Edge],
    word: Word,
) -> dict[str, int]:
    joins = verify_join_tree(n, tree, all_edges, word)
    canonical_edge = min(tree)
    canonical_leaf = min(tree_leaves(n, tree))
    join_rank = next(k + 1 for k, (e, _j) in enumerate(joins) if e == canonical_edge)
    join_position = next(j + 1 for e, j in joins if e == canonical_edge)
    first_null, second_null = strand_nulls(word, all_edges, n, canonical_leaf)

    midpoint = len(word) // 2
    midpoint_edges = [e for e, position in joins if position < midpoint]
    dsu = DSU(n)
    for a, b in midpoint_edges:
        dsu.union(a, b)
    component_sizes = Counter(dsu.find(v) for v in range(n))
    return {
        "canonical_edge_join_rank": join_rank,
        "canonical_edge_join_position": join_position,
        "leaf_null_separation": second_null - first_null,
        "midpoint_join_count": len(midpoint_edges),
        "midpoint_largest_join_component": max(component_sizes.values()),
    }


def audit_tree(
    n: int,
    name: str,
    tree: tuple[Edge, ...],
    all_edges: list[Edge],
    global_fiber_sizes: dict[int, dict[Permutation, int]],
    global_identity_words: int,
):
    m = 2 * n - 2
    words, cache_info = enumerate_fixed_tree(n, tree, all_edges)
    word_index = {word: idx for idx, word in enumerate(words)}
    if len(word_index) != len(words):
        raise AssertionError("duplicate words")

    statistics = {
        word: word_statistics(n, tree, all_edges, word)
        for word in words
    }

    # Each bucket is one fixed (r,i,outside,block-product) conditional clique.
    # Every word has exactly one entry in every (r,i) bucket partition.
    buckets = {}
    bucket_counts_by_r = Counter()
    max_bucket_by_r = Counter()
    for r in (3, 4, 5):
        for i in range(m - r + 1):
            grouped = defaultdict(list)
            for idx, word in enumerate(words):
                product = evaluate(n, all_edges, word[i : i + r])
                key = (word[:i], word[i + r :], product)
                grouped[key].append(idx)
            for key, members in grouped.items():
                bucket_key = (r, i, key)
                buckets[bucket_key] = tuple(members)
                bucket_counts_by_r[r] += 1
                max_bucket_by_r[r] = max(max_bucket_by_r[r], len(members))

    expected_memberships = len(words) * sum(m - r + 1 for r in (3, 4, 5))
    if sum(len(x) for x in buckets.values()) != expected_memberships:
        raise AssertionError("bucket membership mismatch")

    dsu = DSU(len(words))
    nontrivial_buckets = Counter()
    directed_internal_mechanisms = Counter()
    for (r, _i, key), members in buckets.items():
        if len(members) > 1:
            nontrivial_buckets[r] += 1
            root = members[0]
            for other in members[1:]:
                dsu.union(root, other)
        product = key[2]
        fiber_size = global_fiber_sizes[r][product]
        directed_internal_mechanisms[r] += len(members) * (len(members) - 1)
        if len(members) > fiber_size:
            raise AssertionError((r, len(members), fiber_size))

    components = Counter(dsu.find(idx) for idx in range(len(words)))
    component_sizes = sorted(components.values(), reverse=True)

    distributions = {
        stat: dict(sorted(Counter(row[stat] for row in statistics.values()).items()))
        for stat in next(iter(statistics.values()))
    }

    cuts = []
    word_set = set(words)
    for stat, distribution in distributions.items():
        for threshold in sorted(distribution)[:-1]:
            subset = {word_index[w] for w in words if statistics[w][stat] <= threshold}
            if len(subset) > len(words) // 2:
                subset = set(range(len(words))) - subset
                orientation = "gt"
            else:
                orientation = "le"
            if not subset:
                continue
            full_by_r = {r: Fraction(0) for r in (3, 4, 5)}
            restricted_by_r = {r: Fraction(0) for r in (3, 4, 5)}
            for (r, _i, key), members in buckets.items():
                a = sum(idx in subset for idx in members)
                if not a:
                    continue
                b = len(members)
                product = key[2]
                f = global_fiber_sizes[r][product]
                outer = Fraction(1, 6 * (m - r + 1))
                full_by_r[r] += outer * a * Fraction(f - a, f)
                restricted_by_r[r] += outer * a * Fraction(b - a, f)
            full_escape = sum(full_by_r.values(), Fraction(0)) / len(subset)
            restricted_escape = sum(restricted_by_r.values(), Fraction(0)) / len(subset)
            cuts.append({
                "statistic": stat,
                "threshold": threshold,
                "conditional_smaller_side_orientation": orientation,
                "side_size": len(subset),
                "global_mass_numerator": len(subset),
                "global_mass_denominator": global_identity_words,
                "global_mass_at_most_half": 2 * len(subset) <= global_identity_words,
                "full_K_escape": fraction_text(full_escape),
                "restricted_escape": fraction_text(restricted_escape),
                "full_by_r": {str(r): fraction_text(full_by_r[r] / len(subset)) for r in (3, 4, 5)},
                "restricted_by_r": {
                    str(r): fraction_text(restricted_by_r[r] / len(subset)) for r in (3, 4, 5)
                },
            })

    expected_sizes = {"star": 8856, "path": 7808, "tshape": 8254}
    if len(words) != expected_sizes[name]:
        raise AssertionError((name, len(words), expected_sizes[name]))
    return {
        "name": name,
        "tree_edges": [list(e) for e in tree],
        "fiber_size": len(words),
        "automaton_completion_cache": {
            "hits": cache_info.hits,
            "misses": cache_info.misses,
            "maxsize": cache_info.maxsize,
            "currsize": cache_info.currsize,
        },
        "components": len(component_sizes),
        "component_sizes": component_sizes,
        "buckets_by_r": {str(r): bucket_counts_by_r[r] for r in (3, 4, 5)},
        "nontrivial_buckets_by_r": {str(r): nontrivial_buckets[r] for r in (3, 4, 5)},
        "max_bucket_size_by_r": {str(r): max_bucket_by_r[r] for r in (3, 4, 5)},
        "directed_internal_mechanisms_by_r": {
            str(r): directed_internal_mechanisms[r] for r in (3, 4, 5)
        },
        "statistic_distributions": distributions,
        "named_cut_flows": cuts,
        "minimum_named_full_escape": min(
            (row["full_K_escape"] for row in cuts),
            key=lambda text: Fraction(text),
        ),
        "minimum_named_restricted_escape": min(
            (row["restricted_escape"] for row in cuts),
            key=lambda text: Fraction(text),
        ),
    }


def main() -> None:
    started = time.perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("--shape", choices=("star", "path", "tshape", "all"), default="all")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = 5
    m = 2 * n - 2
    all_edges = edges(n)
    shapes = tree_shapes()
    requested = list(shapes) if args.shape == "all" else [args.shape]
    global_fiber_sizes = {
        r: product_counts(n, all_edges, r)
        for r in (3, 4, 5)
    }
    global_identity_words = identity_word_count(n, all_edges, m)
    rows = [
        audit_tree(
            n,
            name,
            shapes[name],
            all_edges,
            global_fiber_sizes,
            global_identity_words,
        )
        for name in requested
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
        "convention": "(pq)(x)=p(q(x)); append a factor by swapping domain entries of p",
        "kernel": "literal lazy K; each ordered replacement outcome has weight 1/[6(m-r+1)|F_r(product)|]",
        "claims_tested": [
            "The fixed-tree rejected-exit restriction is connected for representative N=5 star/path/T fibers.",
            "Named join chronology and leaf-strand threshold cuts can have superpolynomially small full-K flow.",
        ],
        "scope_warning": "These exact N=5 calculations can falsify but cannot prove a universal connectivity, gap, or conductance theorem.",
        "summary": {
            "N": n,
            "m": m,
            "global_identity_words": global_identity_words,
            "shapes": requested,
            "all_tested_restrictions_connected": all(row["components"] == 1 for row in rows),
            "smallest_named_full_escape": min(
                (row["minimum_named_full_escape"] for row in rows),
                key=lambda text: Fraction(text),
            ),
            "smallest_named_restricted_escape": min(
                (row["minimum_named_restricted_escape"] for row in rows),
                key=lambda text: Fraction(text),
            ),
            "elapsed_seconds_before_json_write": time.perf_counter() - started,
        },
        "trees": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
