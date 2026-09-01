#!/usr/bin/env python3
"""Exact calibration audit for M01 and the adjacent-pair reduction.

Composition convention: compose(p, q) is p after q, and words are multiplied
as t_1 ... t_m. All transition probabilities are exact Fractions.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
import platform


def identity(n):
    return tuple(range(n))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def transpositions(n):
    out = []
    for a in range(n):
        for b in range(a + 1, n):
            t = list(range(n))
            t[a], t[b] = t[b], t[a]
            out.append(tuple(t))
    return tuple(out)


def word_product(word, n):
    g = identity(n)
    for t in word:
        g = compose(g, t)
    return g


def fiber_table(ts, n, r):
    ans = defaultdict(list)
    for word in product(ts, repeat=r):
        ans[word_product(word, n)].append(word)
    return ans


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.p[y] = x
        self.size[x] += self.size[y]

    def component_sizes(self):
        counts = defaultdict(int)
        for x in range(len(self.p)):
            counts[self.find(x)] += 1
        return sorted(counts.values(), reverse=True)


def hurwitz_right(a, b):
    # b^{-1}=b for a transposition.
    return b, compose(compose(b, a), b)


def audit_case(n, m):
    ts = transpositions(n)
    M = len(ts)
    e = identity(n)
    states = [w for w in product(ts, repeat=m) if word_product(w, n) == e]
    index = {w: i for i, w in enumerate(states)}
    fibers = {r: fiber_table(ts, n, r) for r in range(2, min(5, m) + 1)}
    R = tuple(r for r in (3, 4, 5) if r <= m)

    uf_k = UnionFind(len(states))
    uf_h = UnionFind(len(states))
    all_rows_normalized_k = True
    all_rows_normalized_j = True
    max_offdiag_j_scan_multiplicity = 0
    min_point_ratio = None
    min_ratio_witness = None
    whole_word_h4_min_contribution_ok = True

    for xi, x in enumerate(states):
        krow = defaultdict(Fraction)
        jrow = defaultdict(Fraction)
        jindices = defaultdict(set)
        krow[xi] += Fraction(1, 2)
        jrow[xi] += Fraction(1, 2)

        for r in R:
            scan_coeff = Fraction(1, 2 * len(R) * (m - r + 1))
            for start in range(m - r + 1):
                old = x[start : start + r]
                h = word_product(old, n)
                fib = fibers[r][h]
                each = scan_coeff / len(fib)
                for new in fib:
                    y = x[:start] + new + x[start + r :]
                    yi = index[y]
                    krow[yi] += each
                    if yi != xi:
                        uf_k.union(xi, yi)
                    if r == 4 and m == 4 and each != Fraction(1, 4 * len(states)):
                        whole_word_h4_min_contribution_ok = False

        for start in range(m - 1):
            old = x[start : start + 2]
            p = word_product(old, n)
            fib = fibers[2][p]
            each = Fraction(1, 2 * (m - 1) * len(fib))
            for new in fib:
                y = x[:start] + new + x[start + 2 :]
                yi = index[y]
                jrow[yi] += each
                if yi != xi:
                    jindices[yi].add(start)

        all_rows_normalized_k &= sum(krow.values(), Fraction()) == 1
        all_rows_normalized_j &= sum(jrow.values(), Fraction()) == 1
        for yi, inds in jindices.items():
            max_offdiag_j_scan_multiplicity = max(
                max_offdiag_j_scan_multiplicity, len(inds)
            )
            ratio = krow[yi] / jrow[yi]
            if min_point_ratio is None or ratio < min_point_ratio:
                min_point_ratio = ratio
                min_ratio_witness = [xi, yi, sorted(inds)]

        for start in range(m - 1):
            a, b = x[start], x[start + 1]
            c, d = hurwitz_right(a, b)
            y = x[:start] + (c, d) + x[start + 2 :]
            uf_h.union(xi, index[y])

    square_counts = []
    label_uniform = []
    for start in range(m - 1):
        by_label = {t: 0 for t in ts}
        for x in states:
            if x[start] == x[start + 1]:
                by_label[x[start]] += 1
        square_counts.append(sum(by_label.values()))
        label_uniform.append(len(set(by_label.values())) == 1)

    shorter_count = 1 if m == 2 else sum(
        1
        for w in product(ts, repeat=m - 2)
        if word_product(w, n) == e
    )
    expected_square_count = M * shorter_count
    lower_bound_holds = all(c * M >= len(states) for c in square_counts)

    return {
        "N": n,
        "m": m,
        "M": M,
        "omega_size": len(states),
        "K_component_sizes": uf_k.component_sizes(),
        "Hurwitz_component_sizes": uf_h.component_sizes(),
        "K_rows_normalized": all_rows_normalized_k,
        "J_rows_normalized": all_rows_normalized_j,
        "max_offdiag_J_scan_multiplicity": max_offdiag_j_scan_multiplicity,
        "min_offdiag_K_over_J": (
            [min_point_ratio.numerator, min_point_ratio.denominator]
            if min_point_ratio is not None
            else None
        ),
        "claimed_ratio_floor": [1, 3 * M * M],
        "pointwise_floor_holds": (
            min_point_ratio is None or min_point_ratio >= Fraction(1, 3 * M * M)
        ),
        "min_ratio_witness_indices": min_ratio_witness,
        "m4_H4_each_whole_word_contribution_exact": whole_word_h4_min_contribution_ok,
        "square_counts_by_position": square_counts,
        "expected_square_count_each_position": expected_square_count,
        "square_bijection_holds": all(c == expected_square_count for c in square_counts),
        "square_labels_uniform_each_position": all(label_uniform),
        "square_probability_ge_1_over_M": lower_bound_holds,
    }


def main():
    result = {
        "python": platform.python_version(),
        "random_seed": None,
        "composition": "pq means p after q; word product t1...tm",
        "cases": [audit_case(3, 4), audit_case(4, 4), audit_case(4, 6)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
