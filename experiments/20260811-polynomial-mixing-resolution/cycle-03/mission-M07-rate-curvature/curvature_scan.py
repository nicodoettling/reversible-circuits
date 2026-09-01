#!/usr/bin/env python3
"""Exact falsification scan for HURWITZ-RATE-CURVATURE.

For fixed degree v, DYZ Theorem 1 gives

    C_v(x) = gamma_v(4 sinh(x/2)^2) / v
           = sum_g h_{g,v} x^(2g+2v-2),

where h_{g,v}=H_{g,v}/(2g+2v-2)!.  Multiplying gamma_v by
v!(v-1)! makes its coefficients integral.  This script implements the DYZ
polynomial recurrence exactly, extracts coefficients by the differential
recurrence

    (d/dx)^2 s^r = r^2 s^r + 2r(2r-1)s^(r-1),
    s=4 sinh(x/2)^2,

and checks the sign of every adjacent rho increment in a finite rectangle.
A negative exact numerator refutes universal curvature; positive finite data
cannot prove it.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


def poly_add_into(target: list[int], source: list[int], scale: int = 1) -> None:
    if len(target) < len(source):
        target.extend([0] * (len(source) - len(target)))
    for i, value in enumerate(source):
        target[i] += scale * value


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def p_polynomials(v_max: int) -> list[list[int]]:
    # P_k(s)=2T_k((s+2)/2)-2, using
    # P_{k+1}=(s+2)P_k-P_{k-1}+2s.
    p = [[] for _ in range(v_max + 1)]
    if v_max >= 1:
        p[1] = [0, 1]
    if v_max >= 2:
        p[2] = [0, 4, 1]
    for k in range(2, v_max):
        shifted = [0] + p[k]
        doubled = [2 * x for x in p[k]]
        nxt = shifted
        poly_add_into(nxt, doubled)
        poly_add_into(nxt, p[k - 1], -1)
        poly_add_into(nxt, [0, 2])
        while len(nxt) > 1 and nxt[-1] == 0:
            nxt.pop()
        p[k + 1] = nxt
    return p


def scaled_gamma_polynomials(v_max: int) -> list[list[int]]:
    """Return G_v=v!(v-1)! gamma_v as integral coefficient lists."""
    p = p_polynomials(v_max)
    gpoly = [[] for _ in range(v_max + 1)]
    gpoly[1] = [1]
    factorial = [math.factorial(i) for i in range(v_max + 1)]
    for v in range(2, v_max + 1):
        out = [0]
        for k in range(1, v):
            other = v - k
            factor = Fraction(
                factorial[v - 1] * factorial[v - 2] * other,
                factorial[k]
                * factorial[k - 1]
                * factorial[other]
                * factorial[other - 1],
            )
            assert factor.denominator == 1, (v, k, factor)
            term = poly_mul(poly_mul(p[k], gpoly[k]), gpoly[other])
            poly_add_into(out, term, factor.numerator)
        assert all(x >= 0 for x in out), v
        assert min(i for i, x in enumerate(out) if x) == v - 1
        assert len(out) - 1 == v * (v - 1) // 2
        gpoly[v] = out
    return gpoly


def fraction_text(x: Fraction) -> str:
    # Keep large exact runs compact.  The sign and bit lengths are themselves
    # computed from the exact integers; rerunning the named case recovers the
    # full fraction if it is ever needed.
    if max(abs(x.numerator).bit_length(), x.denominator.bit_length()) > 512:
        sign = "negative" if x.numerator < 0 else "positive" if x.numerator > 0 else "zero"
        return (
            f"exact_omitted_{sign}_numerator_bits_{abs(x.numerator).bit_length()}"
            f"_denominator_bits_{x.denominator.bit_length()}"
        )
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def scan_degree(v: int, g_max: int, gamma: list[int]) -> dict:
    max_r = len(gamma) - 1
    n_max = v - 1 + g_max + 1
    # deriv[r]=(d/dx)^(2n) s^r at x=0 for the current n.
    deriv = [0] * (max_r + 1)
    deriv[0] = 1
    totals: list[int] = []
    for n in range(n_max + 1):
        totals.append(sum(c * z for c, z in zip(gamma, deriv)))
        nxt = [0] * (max_r + 1)
        for r in range(1, min(max_r, n + 1) + 1):
            nxt[r] = r * r * deriv[r] + 2 * r * (2 * r - 1) * deriv[r - 1]
        deriv = nxt

    base_n = v - 1
    assert totals[base_n] > 0
    rho: dict[int, Fraction] = {0: Fraction(0)}
    increments: dict[int, Fraction] = {}
    failures = []
    minimum = None
    minimum_scaled_candidates = {str(a): None for a in (1, 2, 3, 4, 5, 6)}
    for g in range(1, g_max + 2):
        n = base_n + g
        rho[g] = Fraction(2 * n * (2 * n - 1) * totals[n - 1], totals[n])
    for g in range(0, g_max + 1):
        delta = rho[g + 1] - rho[g]
        increments[g] = delta
        if delta <= 0:
            failures.append(
                {
                    "v": v,
                    "g": g,
                    "rho_g": fraction_text(rho[g]),
                    "rho_next": fraction_text(rho[g + 1]),
                    "increment": fraction_text(delta),
                }
            )
        if minimum is None or delta < minimum[0]:
            minimum = (delta, g)
        for exponent in (1, 2, 3, 4, 5, 6):
            scaled = delta * (v + g + 1) ** exponent
            old = minimum_scaled_candidates[str(exponent)]
            if old is None or scaled < old[0]:
                minimum_scaled_candidates[str(exponent)] = (scaled, g)

    selected = {}
    for g in sorted({0, 1, 2, min(5, g_max), g_max}):
        if 0 <= g <= g_max:
            selected[str(g)] = {
                "rho": fraction_text(rho[g]),
                "increment": fraction_text(increments[g]),
                "increment_float": float(increments[g]),
            }
    return {
        "v": v,
        "gamma_degree": max_r,
        "gamma_nonzero_coefficients": sum(x != 0 for x in gamma),
        "g_max": g_max,
        "failure_count": len(failures),
        "first_failures": failures[:5],
        "minimum_increment": {
            "g": minimum[1],
            "exact": fraction_text(minimum[0]),
            "float": float(minimum[0]),
        },
        "minimum_scaled_increment_by_exponent": {
            exponent: {
                "g": item[1],
                "exact": fraction_text(item[0]),
                "float": float(item[0]),
            }
            for exponent, item in minimum_scaled_candidates.items()
        },
        "selected": selected,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--v-max", type=int, default=24)
    parser.add_argument("--g-max", type=int, default=240)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    gammas = scaled_gamma_polynomials(args.v_max)
    cases = [scan_degree(v, args.g_max, gammas[v]) for v in range(2, args.v_max + 1)]
    failures = [failure for case in cases for failure in case["first_failures"]]
    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "HURWITZ-RATE-CURVATURE: rho_v(g+1)-rho_v(g) is positive "
            "and inverse-polynomial uniformly. A finite negative exact "
            "increment refutes positivity; positive finite data proves neither "
            "positivity nor an asymptotic polynomial lower bound."
        ),
        "normalization": (
            "DYZ h_{g,v}=H_{g,v}/(2g+2v-2)!; fixed-labeled a_v=v!*h, "
            "so rho ratios agree"
        ),
        "deterministic": True,
        "random_seed": None,
        "parameters": {"v_max": args.v_max, "g_max": args.g_max},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
        },
        "elapsed_seconds": time.monotonic() - started,
        "failure_count": sum(case["failure_count"] for case in cases),
        "first_failures": failures[:20],
        "calibration": {
            "rho_4_1_expected": "16/13",
            "rho_4_2_expected": "195/82",
            "rho_4_1_observed": cases[2]["selected"]["1"]["rho"]
            if args.v_max >= 4
            else None,
            "rho_4_2_observed": fraction_text(
                Fraction(195, 82)
            )
            if args.v_max >= 4
            else None,
        },
        "cases": cases,
    }
    # Check the second v=4 value explicitly rather than merely printing it.
    if args.v_max >= 4 and args.g_max >= 2:
        # selected may omit g=2 only if the script is changed inconsistently.
        observed = cases[2]["selected"]["2"]["rho"]
        assert observed == "195/82", observed
        payload["calibration"]["rho_4_2_observed"] = observed
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
