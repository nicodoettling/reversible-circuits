#!/usr/bin/env python3
"""Exact profile-level falsification harness for threshold square flow.

Universal claim tested (finite arithmetic can only falsify it): the explicit
H3 square down-up contribution across every support-component threshold is
inverse-polynomial in N,m after division by the smaller stationary side.
Counts use the exact connected Hurwitz table and labeled component-profile
exponential formula; no word sampling is used.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

from real_root_test import connected_table


def integer_partitions(n: int, least: int = 1):
    if n == 0:
        yield ()
        return
    for first in range(least, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def profile_count(n: int, m: int, sizes: tuple[int, ...], C) -> int:
    """Number of exact words whose unordered component sizes are `sizes`."""
    label_factor = math.factorial(n)
    multiplicities: dict[int, int] = {}
    for v in sizes:
        label_factor //= math.factorial(v)
        multiplicities[v] = multiplicities.get(v, 0) + 1
    for multiplicity in multiplicities.values():
        label_factor //= math.factorial(multiplicity)

    # Coefficient of x^m in product_v sum_k C[v][k] x^k/k!, multiplied by m!.
    coeff = [Fraction(0) for _ in range(m + 1)]
    coeff[0] = Fraction(1)
    for v in sizes:
        new = [Fraction(0) for _ in range(m + 1)]
        if v == 1:
            series = [(0, 1)]
        else:
            series = [(k, C[v][k]) for k in range(m + 1) if C[v][k]]
        for used, value in enumerate(coeff):
            if not value:
                continue
            for k, count in series:
                if used + k <= m:
                    new[used + k] += value * Fraction(count, math.factorial(k))
        coeff = new
    answer = coeff[m] * math.factorial(m) * label_factor
    assert answer.denominator == 1
    return answer.numerator


def layer_and_weighted_square_tables(n_max: int, m_max: int, C):
    # W[n,m,c] and U[n,m,c]=sum_exact_partitions E_P(m)e(P)(M-e(P)).
    W = [[[0] * (n_max + 1) for _ in range(m_max + 1)] for _ in range(n_max + 1)]
    U = [[[0] * (n_max + 1) for _ in range(m_max + 1)] for _ in range(n_max + 1)]
    for n in range(2, n_max + 1):
        M = math.comb(n, 2)
        for sizes in integer_partitions(n):
            c = len(sizes)
            e = sum(math.comb(v, 2) for v in sizes)
            if e == 0:
                continue
            minimum = 2 * sum(v - 1 for v in sizes)
            for m in range(minimum, m_max + 1, 2):
                count = profile_count(n, m, sizes, C)
                W[n][m][c] += count
                U[n][m][c] += count * e * (M - e)
    return W, U


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=10)
    parser.add_argument("--m-max", type=int, default=60)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    C = connected_table(args.n_max, args.m_max)
    W, U = layer_and_weighted_square_tables(args.n_max, args.m_max, C)
    worst = None
    records = []
    for n in range(3, args.n_max + 1):
        M = math.comb(n, 2)
        D = (3 * n * n + n - 12) // 2
        for m in range(max(4, 2 * n), args.m_max + 1, 2):
            total = sum(W[n][m])
            if not total:
                continue
            prefix = 0
            for c0 in range(1, n - 1):
                prefix += W[n][m][c0]
                suffix = total - prefix
                if not prefix or not suffix:
                    continue
                c_boundary = c0 + 1
                # Exact retained K flow: for each shorter partition P with
                # c_boundary components, choose internal t and crossing s.
                numerator = U[n][m - 2][c_boundary]
                Rsize = len([r for r in (3, 4, 5) if r <= m])
                phi_lb = Fraction(numerator, 2 * Rsize * (m - 2) * D * min(prefix, suffix))
                scaled = phi_lb * (n * m) ** 6
                row = {
                    "N": n,
                    "m": m,
                    "c0": c0,
                    "smaller_side": "lower" if prefix <= suffix else "upper",
                    "phi_H3_square_lower_bound": f"{phi_lb.numerator}/{phi_lb.denominator}",
                    "phi_float": float(phi_lb),
                    "scaled_by_(Nm)^6": float(scaled),
                }
                if worst is None or phi_lb < worst[0]:
                    worst = (phi_lb, row)
                if (n, m) in {(3, 6), (4, 6), (4, 8)}:
                    records.append(row)

    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "The exact retained H3 square flow across every component-count "
            "threshold has inverse-polynomial two-sided conductance. Finite "
            "arithmetic can falsify proposed bounds but cannot prove universality."
        ),
        "deterministic": True,
        "random_seed": None,
        "parameters": {"n_max": args.n_max, "m_max": args.m_max},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
        },
        "worst_unscaled": None if worst is None else worst[1],
        "selected_records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
