#!/usr/bin/env python3
"""Exact arithmetic for an M113 split-family edge and its aggregate flow.

The source key has p=(0,1), Q_L={{0,1,2},{3},...,{d-1}}, and
Q_R={{0,...,d-1}}.  A target has p'=id, the same Q_L, and
Q_R'={A,A^c}, where 0 is in A and 1 is not.  The moved seam factor is
(0,1).  The formula below is the exact A_d transition probability when
|A|=a.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


def int_power_fraction(base: int, exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(base ** exponent, 1)
    return Fraction(1, base ** (-exponent))


def transition_probability(d: int, a: int) -> Fraction:
    """A_d(kappa_d, lambda_{d,a}) for the balanced-split family."""
    b = d - a
    return (
        int_power_fraction(a, a - 3)
        * int_power_fraction(b, b - 3)
        / (8 * (2 * d - 3) * int_power_fraction(d, d - 4))
    )


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def record(d: int) -> dict:
    if d % 2:
        raise ValueError("the displayed exact simplification uses even d")
    a = d // 2
    one = transition_probability(d, a)
    simplified = Fraction(1, (2 ** (d - 3)) * (2 * d - 3) * d * d)
    assert one == simplified
    multiplicity = math.comb(d - 2, a - 1)
    aggregate = multiplicity * one
    elementary_lower = Fraction(2, (d - 1) * (2 * d - 3) * d * d)
    assert aggregate >= elementary_lower
    return {
        "d": d,
        "balanced_block_size": a,
        "compatible_balanced_splits": multiplicity,
        "individual_probability": {
            "numerator": one.numerator,
            "denominator": one.denominator,
            "float": float(one),
        },
        "identity_individual_times_2powd_d3": float(one * (2 ** d) * d ** 3),
        "aggregate_probability": {
            "numerator": aggregate.numerator,
            "denominator": aggregate.denominator,
            "float": float(aggregate),
        },
        "proved_aggregate_lower_bound": {
            "numerator": elementary_lower.numerator,
            "denominator": elementary_lower.denominator,
            "float": float(elementary_lower),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int,
                        default=[6, 8, 10, 12, 16, 20, 30, 40])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if any(d < 6 or d % 2 for d in args.d):
        raise SystemExit("all d must be even and at least 6")
    payload = {
        "claim_scope": (
            "exact formula audit for an infinite family; no spectral inference"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "formula": (
            "A(sigma_d,lambda_A), |A|=d/2, 0 in A, 1 not in A = "
            "2^(-d+3)/((2d-3)d^2)"
        ),
        "cases": [record(d) for d in args.d],
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
