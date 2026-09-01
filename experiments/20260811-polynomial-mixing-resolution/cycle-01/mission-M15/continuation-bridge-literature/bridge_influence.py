#!/usr/bin/env python3
"""Exact local conditional influence for the Q=P*P prefix-path Gibbs law.

This is a falsification harness for a Dobrushin/path-coupling hypothesis, not a
mixing experiment.  Permutations are tuples and compose as p after q.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p*q, so (p*q)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for i, image in enumerate(p):
        ans[image] = i
    return tuple(ans)


def transposition(n: int, i: int, j: int) -> tuple[int, ...]:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def left_increment(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    """Return a^{-1}*b for a path edge a -> b."""
    return compose(inverse(a), b)


def pair_counts(n: int) -> Counter[tuple[int, ...]]:
    ts = [transposition(n, i, j) for i in range(n) for j in range(i + 1, n)]
    return Counter(compose(s, t) for s in ts for t in ts)


def conditional_integer_weights(
    counts: Counter[tuple[int, ...]],
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> dict[tuple[int, ...], int]:
    """Weights proportional to Q(left^-1*b) Q(b^-1*right).

    The common M^-4 denominator cancels.  Because the second factor must lie
    in supp(Q), candidate b can be generated as right*s^{-1}, s in supp(Q).
    """
    weights: dict[tuple[int, ...], int] = {}
    for s, a_s in counts.items():
        b = compose(right, inverse(s))
        a_first = counts.get(left_increment(left, b), 0)
        if a_first:
            weights[b] = a_first * a_s
    return weights


def tv_distance(
    w: dict[tuple[int, ...], int], z: dict[tuple[int, ...], int]
) -> Fraction:
    sw = sum(w.values())
    sz = sum(z.values())
    assert sw > 0 and sz > 0
    total = sum(
        abs(Fraction(w.get(x, 0), sw) - Fraction(z.get(x, 0), sz))
        for x in set(w) | set(z)
    )
    return total / 2


def run_case(n: int) -> dict[str, object]:
    if n < 3:
        raise ValueError("N must be at least 3")
    identity = tuple(range(n))
    t01 = transposition(n, 0, 1)
    t12 = transposition(n, 1, 2)
    g = compose(t01, t12)
    counts = pair_counts(n)

    # Two feasible degree-two star configurations have center identity and
    # leaf pairs (identity,identity) and (g,identity), respectively.
    w00 = conditional_integer_weights(counts, identity, identity)
    wg0 = conditional_integer_weights(counts, g, identity)
    tv = tv_distance(w00, wg0)
    pair_type_histogram: Counter[tuple[int, int]] = Counter()
    for b, a_b in counts.items():
        pair_type_histogram[(a_b, counts.get(left_increment(g, b), 0))] += 1

    m = comb(n, 2)
    number_3cycles = 2 * comb(n, 3)
    number_double_transpositions = 3 * comb(n, 4) if n >= 4 else 0
    expected_support = 1 + number_3cycles + number_double_transpositions
    assert len(counts) == expected_support
    assert counts[identity] == m
    assert counts[g] == 3
    assert sum(counts.values()) == m * m

    # The path-coupling expression in the closest primary theorem has d=2.
    corrected_contraction_margin = 1 - 4 * tv
    # The 9-site path adjacency matrix has spectral radius
    # 2*cos(pi/10)>19/10.  If all nearest-neighbor influences are at least
    # tv, every dependency matrix therefore has spectral radius >19*tv/10.
    path9_dependency_spectral_radius_rational_lower_bound = Fraction(19, 10) * tv
    return {
        "N": n,
        "M": m,
        "Q_support_size": len(counts),
        "conditional_support_identity_identity": len(w00),
        "conditional_support_3cycle_identity": len(wg0),
        "normalizer_identity_identity_pair_count_units": sum(w00.values()),
        "normalizer_3cycle_identity_pair_count_units": sum(wg0.values()),
        "tv_numerator": tv.numerator,
        "tv_denominator": tv.denominator,
        "tv_decimal": float(tv),
        "one_minus_4tv_numerator": corrected_contraction_margin.numerator,
        "one_minus_4tv_denominator": corrected_contraction_margin.denominator,
        "one_minus_4tv_decimal": float(corrected_contraction_margin),
        "positive_dobrushin_margin_for_this_pair": corrected_contraction_margin > 0,
        "path9_dependency_spectral_radius_lower_bound_numerator": (
            path9_dependency_spectral_radius_rational_lower_bound.numerator
        ),
        "path9_dependency_spectral_radius_lower_bound_denominator": (
            path9_dependency_spectral_radius_rational_lower_bound.denominator
        ),
        "path9_dependency_spectral_radius_lower_bound_decimal": float(
            path9_dependency_spectral_radius_rational_lower_bound
        ),
        "path9_all_matrix_norm_conditions_falsified_by_this_bound": (
            path9_dependency_spectral_radius_rational_lower_bound > 1
        ),
        "histogram_pair_count_b_then_g_inverse_b": [
            {"a_b": key[0], "a_g_inverse_b": key[1], "multiplicity": value}
            for key, value in sorted(pair_type_histogram.items())
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, action="append", dest="ns", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "convention": "(p*q)(x)=p(q(x)); edge weight Q(a^{-1}b)",
        "claim_tested": (
            "Whether the positive d=2 worst-case conditional-influence margin "
            "required by the intended path-coupling hypothesis can hold for Q_N"
        ),
        "deterministic": True,
        "cases": [run_case(n) for n in args.ns],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
