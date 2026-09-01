#!/usr/bin/env python3
"""Independent formula-only q=1 calibration for the M211 witness.

This checker imports no M211 code or data and performs no topology
reconstruction. The universal conclusion is analytic, not finite.
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


def split_weight(k: int, parent: int, child: int) -> Fraction:
    rank = 2 * k - 3
    return tau(child) * tau(parent - child) / (rank * tau(parent))


def nonincident_mass(k: int, r: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * (2 * k - 3))


def untouched_mass(k: int) -> Fraction:
    return Fraction(k - 1, 2 * k - 3)


def shared_mass(k: int, side: str, s: int) -> Fraction:
    other = 2 * k - 1 - s if side == "B" else k - s
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def seam_average(k: int, ell: int, source_length: int) -> Fraction:
    D, n = 2 * k - 1, 3 * k
    if source_length < k:
        atoms = (
            (source_length, D - 2 * source_length),
            (source_length + 1, source_length),
            (source_length + k, source_length),
        )
    else:
        c = D - source_length
        atoms = (
            (n - c, D - 2 * c),
            (n - c - 1, c),
            (n - c - k, c),
        )
    accepted = sum(count for size, count in atoms if 2 <= size <= ell)
    return Fraction(accepted, D)


def contiguous_average(k: int, ell: int, source_length: int) -> Fraction:
    if 2 <= source_length <= ell:
        return Fraction(k - source_length, k)
    return Fraction()


def fragment_sum(k: int, parent: int, value) -> Fraction:
    return sum(
        (parent - d - 1) * split_weight(k, parent, d) * value(d)
        for d in range(1, parent)
    )


def q1_calibration() -> dict:
    q = 1
    k, s, ell = 12 * q - 1, 3 * q, 4 * q
    D = 2 * k - 1
    hs = nonincident_mass(k, s)
    hlong = nonincident_mass(k, D - s)
    hmarked = nonincident_mass(k, k - s)
    u = untouched_mass(k)

    Fs = seam_average(k, ell, s)
    Flong = seam_average(k, ell, D - s)
    Js = contiguous_average(k, ell, s)
    Jlong = contiguous_average(k, ell, k - s)
    assert Fs == Fraction(6, 7)
    assert Flong == 0
    assert Js == Fraction(8, 11)
    assert Jlong == 0

    b_fragment = fragment_sum(
        k, s, lambda d: seam_average(k, ell, d)
    ) + fragment_sum(
        k, D - s, lambda d: seam_average(k, ell, d)
    )
    a_fragment = fragment_sum(
        k, s, lambda d: contiguous_average(k, ell, d)
    ) + fragment_sum(
        k, k - s, lambda d: contiguous_average(k, ell, d)
    )
    a_fresh = sum(
        (k - d) * split_weight(k, k, d)
        for d in range(2, ell + 1)
    )

    b_surviving = hs * Flong + hlong * Fs
    a_surviving = (
        hs * Jlong + hmarked * Js + u * (Js + Jlong)
    )
    b_denominator = hs + hlong
    a_denominator = hs + hmarked + u
    assert b_denominator == 1 - shared_mass(k, "B", s)
    assert a_denominator == 1 - shared_mass(k, "A", s)

    phi = (b_surviving + b_fragment) / b_denominator
    psi = (a_surviving + a_fragment + a_fresh) / a_denominator
    defect = phi - psi
    assert defect > 0

    b_limit_kernel_coefficient = Fraction(1, 8) + Fraction(7, 8)
    a_limit_kernel_coefficient = (
        Fraction(1, 8) + Fraction(3, 8) + Fraction(1, 2)
    )
    b_limit_surviving = Fraction(7, 8) ** 2
    a_limit_surviving = Fraction(7, 8) * Fraction(3, 4)
    assert b_limit_kernel_coefficient == a_limit_kernel_coefficient == 1
    assert b_limit_surviving - a_limit_surviving == Fraction(7, 64)

    return {
        "parameters": {"q": q, "k": k, "s": s, "l": ell},
        "exact_cutoffs": {
            "F_s": str(Fs),
            "F_D_minus_s": str(Flong),
            "J_s": str(Js),
            "J_k_minus_s": str(Jlong),
        },
        "normalizers": {
            "B": str(b_denominator),
            "A": str(a_denominator),
        },
        "finite_components": {
            "B_surviving": str(b_surviving),
            "B_fragment": str(b_fragment),
            "A_surviving": str(a_surviving),
            "A_fragment": str(a_fragment),
            "A_fresh": str(a_fresh),
        },
        "finite_profiles": {
            "Phi": str(phi),
            "Psi": str(psi),
            "Phi_minus_Psi": str(defect),
            "decimal_defect": float(defect),
        },
        "symbolic_limit": {
            "B_kernel_coefficient": str(b_limit_kernel_coefficient),
            "A_kernel_coefficient": str(a_limit_kernel_coefficient),
            "B_surviving": str(b_limit_surviving),
            "A_surviving": str(a_limit_surviving),
            "difference": str(Fraction(7, 64)),
        },
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: cleanroom_witness.py OUTPUT.json")
    payload = {
        "mission": "M215",
        "method": "independent exact closed-form q=1 calibration",
        "imports_m211_code_or_data": False,
        "topology_reconstruction": False,
        "finite_only": True,
        "universal_inference": False,
        "seed": None,
        "python": platform.python_version(),
        "result": q1_calibration(),
        "status": "all independent exact calibration assertions passed",
    }
    Path(sys.argv[1]).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
