#!/usr/bin/env python3
"""Exact falsification harness for the DYZ adjacent-genus ratio bound.

Universal claim tested (finite arithmetic can only falsify it): if C_g(v)
counts connected identity transposition words of length 2(v-1)+2g on a
fixed labeled v-set, then

  [C_g(v)/k!] / [C_{g-1}(v)/(k-2)!] <= v^3/12.

The proof in checkpoint.md is universal and uses DYZ Proposition 1; this
script independently checks normalization and boundary cases from the exact
Frobenius/component recurrence.
"""

from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction
from pathlib import Path

from real_root_test import connected_table


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=20)
    parser.add_argument("--m-max", type=int, default=160)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    C = connected_table(args.n_max, args.m_max)
    failures = []
    maximum_scaled = (Fraction(0), None)
    records = []
    for v in range(2, args.n_max + 1):
        for k in range(2 * v, args.m_max + 1, 2):
            if not C[v][k - 2]:
                continue
            normalized_ratio = Fraction(C[v][k], C[v][k - 2] * k * (k - 1))
            bound = Fraction(v**3, 12)
            scaled = normalized_ratio / bound
            if scaled > maximum_scaled[0]:
                maximum_scaled = (scaled, (v, k, normalized_ratio, bound))
            if normalized_ratio > bound:
                failures.append(
                    {
                        "v": v,
                        "k": k,
                        "ratio": f"{normalized_ratio.numerator}/{normalized_ratio.denominator}",
                        "bound": f"{bound.numerator}/{bound.denominator}",
                    }
                )
            if (v, k) in {(2, 4), (3, 6), (4, 8), (4, 10)}:
                records.append(
                    {
                        "v": v,
                        "k": k,
                        "C_previous": str(C[v][k - 2]),
                        "C_current": str(C[v][k]),
                        "normalized_ratio": f"{normalized_ratio.numerator}/{normalized_ratio.denominator}",
                    }
                )

    item = maximum_scaled[1]
    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "For all v>=2,g>=1, normalized connected Hurwitz ratio "
            "h_g(v)/h_{g-1}(v) is at most v^3/12. Finite arithmetic "
            "checks normalization but is not the universal proof."
        ),
        "deterministic": True,
        "random_seed": None,
        "parameters": {"n_max": args.n_max, "m_max": args.m_max},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
        },
        "failure_count": len(failures),
        "first_failures": failures[:20],
        "maximum_ratio_divided_by_bound": None
        if item is None
        else {
            "v": item[0],
            "k": item[1],
            "ratio": f"{item[2].numerator}/{item[2].denominator}",
            "bound": f"{item[3].numerator}/{item[3].denominator}",
            "fraction_of_bound": float(maximum_scaled[0]),
        },
        "calibration_records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
