#!/usr/bin/env python3
"""Exact formula-only diagnostics for the signed averaged DE term.

The script evaluates immutable closed profile formulas and exact q_hat split
weights. It reconstructs no topology. Finite k<=15 values prove no universal
statement.
"""

from __future__ import annotations

import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path


def tau(d):
    return Fraction(d ** (d - 1), math.factorial(d))


def b(d):
    return tau(d)  # common e^{-d} factors cancel in every ratio below


def K(k, r, d):
    return b(d) * b(r - d) / ((2 * k - 3) * b(r))


def h(k, r):
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def u(k):
    return Fraction(k - 1, 2 * k - 3)


def gamma(k, side, s):
    other = 2 * k - 1 - s if side == "B" else k - s
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def q_split(k, s):
    # The e^{-d} factors cancel in b_s b_(k-s)/b_k.
    return Fraction(k, k - 1) * b(s) * b(k - s) / b(k)


def qhat(k, s):
    return q_split(k, s) * (1 - gamma(k, "A", s))


def F(k, ell, x):
    D, n = 2 * k - 1, 3 * k
    if x < k:
        atoms = ((x, D - 2 * x), (x + 1, x), (x + k, x))
    else:
        c = D - x
        atoms = ((n - c, D - 2 * c), (n - c - 1, c), (n - c - k, c))
    return Fraction(sum(m for size, m in atoms if 2 <= size <= ell), D)


def J(k, ell, x):
    return Fraction(k - x, k) if 2 <= x <= ell else Fraction()


def W(k, r, value):
    return sum(
        (r - d - 1) * K(k, r, d) * value(d)
        for d in range(1, r)
    )


def phi_y(k, s, ell):
    D = 2 * k - 1
    numerator = (
        h(k, s) * F(k, ell, D - s)
        + h(k, D - s) * F(k, ell, s)
        + W(k, s, lambda d: F(k, ell, d))
        + W(k, D - s, lambda d: F(k, ell, d))
    )
    denominator = h(k, s) + h(k, D - s)
    return numerator / denominator


def psi_y(k, s, ell):
    numerator = (
        h(k, s) * J(k, ell, k - s)
        + h(k, k - s) * J(k, ell, s)
        + W(k, s, lambda d: J(k, ell, d))
        + W(k, k - s, lambda d: J(k, ell, d))
        + u(k) * (J(k, ell, s) + J(k, ell, k - s))
        + sum((k - d) * K(k, k, d) for d in range(2, min(ell, k - 1) + 1))
    )
    denominator = h(k, s) + h(k, k - s) + u(k)
    return numerator / denominator


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: signed_de_formula.py OUTPUT.json")
    rows = []
    for k in (3, 5, 7, 9, 11, 13, 15):
        max_y = None
        total_qhat = sum(qhat(k, s) for s in range(1, (k - 1) // 2 + 1))
        for ell in range(2, (3 * k - 1) // 2 + 1):
            pieces = [
                (s, qhat(k, s), phi_y(k, s, ell) - psi_y(k, s, ell))
                for s in range(1, (k - 1) // 2 + 1)
            ]
            signed = sum(weight * defect for _, weight, defect in pieces)
            scaled = k * abs(float(signed)) / math.sqrt(ell)
            candidate = (scaled, ell, signed, pieces)
            max_y = candidate if max_y is None or candidate > max_y else max_y
        scaled, ell, signed, pieces = max_y
        rows.append(
            {
                "k": k,
                "sum_qhat": str(total_qhat),
                "max_Y_scaled": scaled,
                "max_Y_l": ell,
                "max_Y_signed_exact": str(signed),
                "terms_at_max": [
                    {
                        "s": s,
                        "qhat": str(weight),
                        "profile_defect": str(defect),
                        "weighted_defect": str(weight * defect),
                    }
                    for s, weight, defect in pieces
                ],
            }
        )
    payload = {
        "mission": "M217",
        "method": "exact q_hat-weighted closed Y-profile formula",
        "parameters": {"k": [3, 5, 7, 9, 11, 13, 15], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "topology_reconstruction": False,
        "finite_only": True,
        "universal_inference": False,
        "results": rows,
    }
    Path(sys.argv[1]).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
