#!/usr/bin/env python3
"""Formula-only finite diagnostics for the M211 IKBE-b obstruction.

No topology or permutation reconstruction occurs. The code evaluates the
audited M199 closed Y-profile formulas using exact rational arithmetic.
Finite values do not prove the asymptotic counterexample.
"""

from __future__ import annotations

import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def kernel(k: int, r: int, d: int) -> Fraction:
    R = 2 * k - 3
    return tau(d) * tau(r - d) / (R * tau(r))


def h(k: int, r: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def u(k: int) -> Fraction:
    return Fraction(k - 1, 2 * k - 3)


def gamma(k: int, side: str, s: int) -> Fraction:
    other = 2 * k - 1 - s if side == "B" else k - s
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def F(k: int, ell: int, x: int) -> Fraction:
    D, n = 2 * k - 1, 3 * k
    if x < k:
        atoms = ((x, D - 2 * x), (x + 1, x), (x + k, x))
    else:
        c = D - x
        atoms = ((n - c, D - 2 * c), (n - c - 1, c), (n - c - k, c))
    return Fraction(sum(count for gap, count in atoms if 2 <= gap <= ell), D)


def J(k: int, ell: int, x: int) -> Fraction:
    return Fraction(k - x, k) if 2 <= x <= ell else Fraction()


def W(k: int, r: int, value) -> Fraction:
    return sum(
        (r - d - 1) * kernel(k, r, d) * value(d)
        for d in range(1, r)
    )


def phi_y(k: int, s: int, ell: int) -> Fraction:
    D = 2 * k - 1
    numerator = (
        h(k, s) * F(k, ell, D - s)
        + h(k, D - s) * F(k, ell, s)
        + W(k, s, lambda d: F(k, ell, d))
        + W(k, D - s, lambda d: F(k, ell, d))
    )
    denominator = h(k, s) + h(k, D - s)
    assert denominator == 1 - gamma(k, "B", s)
    return numerator / denominator


def psi_y(k: int, s: int, ell: int) -> Fraction:
    numerator = (
        h(k, s) * J(k, ell, k - s)
        + h(k, k - s) * J(k, ell, s)
        + W(k, s, lambda d: J(k, ell, d))
        + W(k, k - s, lambda d: J(k, ell, d))
        + u(k) * (J(k, ell, s) + J(k, ell, k - s))
        + sum(
            (k - d) * kernel(k, k, d)
            for d in range(1, k)
            if 2 <= d <= ell
        )
    )
    denominator = h(k, s) + h(k, k - s) + u(k)
    assert denominator == 1 - gamma(k, "A", s)
    return numerator / denominator


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: ikbe_formula_check.py OUTPUT.json")
    rows = []
    for k in (3, 5, 7, 9, 11):
        maximum = None
        for s in range(1, (k - 1) // 2 + 1):
            for ell in range(2, (3 * k - 1) // 2 + 1):
                defect = phi_y(k, s, ell) - psi_y(k, s, ell)
                scaled = k * abs(float(defect)) / math.sqrt(ell)
                candidate = (scaled, s, ell, defect)
                maximum = candidate if maximum is None or candidate > maximum else maximum
        assert maximum is not None
        scaled, s, ell, defect = maximum
        row = {
            "k": k,
            "max_k_abs_defect_over_sqrt_l": scaled,
            "maximizer": {"s": s, "l": ell, "defect": str(defect)},
        }
        if k == 11:
            witness = phi_y(11, 3, 4) - psi_y(11, 3, 4)
            row["q1_witness"] = {
                "s": 3,
                "l": 4,
                "defect": str(witness),
                "decimal": float(witness),
                "target_limit": str(Fraction(7, 64)),
            }
        rows.append(row)
    payload = {
        "mission": "M211",
        "method": "exact closed Y-profile formulas only",
        "parameters": {"k": [3, 5, 7, 9, 11], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "finite_only": True,
        "universal_inference": False,
        "results": rows,
        "status": "formula checks passed; asymptotic refutation is analytic",
    }
    Path(sys.argv[1]).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
