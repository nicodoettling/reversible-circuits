#!/usr/bin/env python3
"""Exact bounded falsification of a DYZ recurrence synchronization route.

For an ordered split d=d1+d2, the genus sequence in DYZ (13), after the
shift ell=j+1, is proportional to the convolution of a_{.,d1}, a_{.,d2}
and B_j=d1^(2j+3)d2^2/(2j+2)!.  A sum of log-concave sequences is
log-concave if all pairwise cross terms

  2 x_g y_g - x_{g-1}y_{g+1} - y_{g-1}x_{g+1}

are nonnegative.  This script searches exactly for a counterexample to that
specific sufficient condition.  A negative cross term rejects the proposed
synchronization shortcut, not Hurwitz-rate curvature itself.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

from curvature_scan import scaled_gamma_polynomials


def a_sequences(d_max: int, g_max: int) -> list[list[Fraction]]:
    gammas = scaled_gamma_polynomials(d_max)
    out: list[list[Fraction]] = [[] for _ in range(d_max + 1)]
    out[1] = [Fraction(1)] + [Fraction(0)] * g_max
    for d in range(2, d_max + 1):
        gamma = gammas[d]
        r_max = len(gamma) - 1
        deriv = [0] * (r_max + 1)
        deriv[0] = 1
        totals = []
        for n in range(d - 1 + g_max + 1):
            totals.append(sum(c * z for c, z in zip(gamma, deriv)))
            nxt = [0] * (r_max + 1)
            for r in range(1, min(r_max, n + 1) + 1):
                nxt[r] = r * r * deriv[r] + 2 * r * (2 * r - 1) * deriv[r - 1]
            deriv = nxt
        # Scaling by G_d=d!(d-1)! gamma_d and by the outer 1/d is
        # independent of genus, hence irrelevant to every cross-term sign.
        out[d] = [
            Fraction(totals[d - 1 + g], math.factorial(2 * (d - 1 + g)))
            for g in range(g_max + 1)
        ]
    return out


def convolution(a: list[Fraction], b: list[Fraction], c: list[Fraction], n: int) -> list[Fraction]:
    out = [Fraction(0)] * (n + 1)
    for target in range(n + 1):
        for i in range(target + 1):
            for j in range(target - i + 1):
                out[target] += a[i] * b[j] * c[target - i - j]
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d-max", type=int, default=18)
    parser.add_argument("--g-max", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seq = a_sequences(args.d_max - 1, args.g_max + 1)
    first = None
    checked = 0
    for d in range(3, args.d_max + 1):
        contributions = []
        for d1 in range(1, d):
            d2 = d - d1
            B = [
                Fraction(d1 ** (2 * j + 3) * d2 * d2, math.factorial(2 * j + 2))
                for j in range(args.g_max + 2)
            ]
            contributions.append((d1, d2, convolution(seq[d1], seq[d2], B, args.g_max + 1)))
        for x_index, (d1, d2, x) in enumerate(contributions):
            for e1, e2, y in contributions[x_index + 1 :]:
                for g in range(1, args.g_max + 1):
                    cross = 2 * x[g] * y[g] - x[g - 1] * y[g + 1] - y[g - 1] * x[g + 1]
                    checked += 1
                    if cross < 0:
                        first = {
                            "d": d,
                            "ordered_split_x": [d1, d2],
                            "ordered_split_y": [e1, e2],
                            "g": g,
                            "cross_numerator": str(cross.numerator),
                            "cross_denominator": str(cross.denominator),
                        }
                        break
                if first:
                    break
            if first:
                break
        if first:
            break
    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "All ordered-split genus sequences in positive DYZ recurrence (13) "
            "have nonnegative pairwise cross terms, a sufficient condition for "
            "their sum to preserve log-concavity"
        ),
        "logical_scope": (
            "A negative result refutes only this synchronization sufficient "
            "condition, not Hurwitz-rate curvature"
        ),
        "parameters": {"d_max": args.d_max, "g_max": args.g_max},
        "deterministic": True,
        "random_seed": None,
        "environment": {"python": platform.python_version(), "nonstandard_dependencies": []},
        "cross_terms_checked_before_stop": checked,
        "first_negative_cross_term": first,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
