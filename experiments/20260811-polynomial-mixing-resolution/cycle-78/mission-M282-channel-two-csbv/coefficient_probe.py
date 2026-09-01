#!/usr/bin/env python3
"""One exact formula-only falsifier for M282's fixed CSBV reduction.

The script evaluates the abstract support-pair coefficients and the literal
two-seam embedding.  It does not enumerate factorizations and makes no
asymptotic inference.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


def tau(r: int) -> Fraction:
    return Fraction(r ** (r - 1), math.factorial(r))


def conv_ratio(r: int, x: int) -> Fraction:
    if not 1 <= x < r:
        return Fraction()
    return tau(x) * tau(r - x) / tau(r)


def h(r: int, R: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), r * R)


def u_kernel(r: int, x: int, R: int) -> Fraction:
    if not 1 <= x < r:
        return Fraction()
    kernel = conv_ratio(r, x) / R
    second = (r - x - 1) * kernel if x <= r - 2 else Fraction()
    cross = Fraction(4 * (r - 1), r * R) - 2 * kernel
    return second + cross


def tv(values) -> Fraction:
    return sum((abs(y - x) for x, y in zip(values, values[1:])), Fraction())


def l1(values) -> Fraction:
    return sum((abs(x) for x in values), Fraction())


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least 3")
    D, R, n = 2 * k - 1, 2 * k - 3, 3 * k
    p = {}
    q = {}
    a_l = {}
    a_f = {}
    A = {}
    W = {}
    for s in range(1, k):
        p[s] = Fraction(D, D - 1) * conv_ratio(D, s)
        q[s] = (
            Fraction(k, k - 1) * conv_ratio(k, s)
            if s < Fraction(k, 2)
            else Fraction()
        )
        a_l[s] = h(s, R) + h(D - s, R)
        a_f[s] = h(s, R) + h(k - s, R) + Fraction(k - 1, R)
        A[s] = p[s] * a_l[s] - q[s] * a_f[s]
        W[s] = A[s] / a_l[s]

    endpoint = -Fraction(6 * (k - 1), k * D * R)
    assert sum(A.values(), Fraction()) == endpoint
    assert sum(p.values(), Fraction()) == 1
    assert sum(q.values(), Fraction()) == 1

    c = [Fraction() for _ in range(D)]
    first = [Fraction() for _ in range(D)]
    mixture = [Fraction() for _ in range(D)]
    for d in range(1, D):
        first[d] = A[min(d, D - d)]
        for r in range(1, D):
            mixture[d] += W[min(r, D - r)] * (
                u_kernel(r, d, R) + u_kernel(r, D - d, R)
            )
        c[d] = first[d] + mixture[d]
    assert all(c[d] == c[D - d] for d in range(1, D))

    J = [Fraction() for _ in range(n)]
    half = [Fraction()] + [c[s] for s in range(1, k)] + [Fraction()]
    for ell in range(1, k + 1):
        J[ell] = (
            (D - 2 * ell) * half[ell]
            + (ell - 1) * half[ell - 1]
        ) / D
    for ell in range(k + 1, 2 * k):
        J[ell] = (
            (ell - k) * c[ell - k]
            + (2 * k - ell) * c[2 * k - ell]
        ) / D
    for ell in range(1, n):
        reflected = n - ell
        if J[ell] and J[reflected]:
            assert J[ell] == J[reflected]
        elif J[ell]:
            J[reflected] = J[ell]
    assert all(J[ell] == J[n - ell] for ell in range(1, n))
    derivative = [J[ell + 1] - J[ell] for ell in range(2, n - 2)]

    paired_kernel_tvs = []
    for s in range(1, k):
        row = [Fraction()]
        for d in range(1, k):
            row.append(
                u_kernel(s, d, R)
                + u_kernel(s, D - d, R)
                + u_kernel(D - s, d, R)
                + u_kernel(D - s, D - d, R)
            )
        row.append(Fraction())
        paired_kernel_tvs.append(tv(row))

    a_half = [Fraction()] + [A[s] for s in range(1, k)] + [Fraction()]
    m_half = [Fraction()] + [mixture[s] for s in range(1, k)] + [Fraction()]
    return {
        "k": k,
        "endpoint_exact": qstr(endpoint),
        "sum_abs_A_float": float(l1(A.values())),
        "sum_abs_W_float": float(l1(W.values())),
        "sum_W_exact": qstr(sum(W.values(), Fraction())),
        "A_half_tv_float": float(tv(a_half)),
        "k_A_half_tv_float": float(k * tv(a_half)),
        "mixture_half_tv_float": float(tv(m_half)),
        "k_mixture_half_tv_float": float(k * tv(m_half)),
        "abstract_half_tv_float": float(tv(half)),
        "k_abstract_half_tv_float": float(k * tv(half)),
        "abstract_half_l1_float": float(l1(half[1:-1])),
        "ambient_csbv_l1_exact": qstr(l1(derivative)),
        "ambient_csbv_l1_float": float(l1(derivative)),
        "k_ambient_csbv_l1_float": float(k * l1(derivative)),
        "max_paired_kernel_tv_float": float(max(paired_kernel_tvs)),
        "R_times_max_paired_kernel_tv_float": float(R * max(paired_kernel_tvs)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, default=[3, 5, 7, 9, 15, 31])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [analyze(k) for k in args.k]
    payload = {
        "status": "exact finite formula falsification only; no ACBV/CSBV inference",
        "target": "M282 abstract coefficient BV and literal embedded CSBV",
        "convention": "(pq)(x)=p(q(x)); displayed factors left-to-right",
        "formulas_fixed_before_computation": True,
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(__import__("sys").argv),
        "results": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

