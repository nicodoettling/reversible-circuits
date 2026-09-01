#!/usr/bin/env python3
"""Exact Sturm falsification test for real-rooted component polynomials."""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import sympy

from real_root_test import connected_table, layer_table


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=12)
    parser.add_argument("--m-max", type=int, default=80)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    C = connected_table(args.n_max, args.m_max)
    W = layer_table(args.n_max, args.m_max, C)
    u = sympy.Symbol("u")
    failures = []
    tested = 0
    for n in range(2, args.n_max + 1):
        for m in range(0, args.m_max + 1, 2):
            counts = [W[n][m][c] for c in range(1, n + 1)]
            if not any(counts):
                continue
            poly = sympy.Poly(sum(counts[c - 1] * u**c for c in range(1, n + 1)), u)
            # Remove the forced zero root; all remaining coefficients are
            # positive, so any real roots must be negative.
            multiplicity_zero = min(c for c, value in enumerate([0] + counts) if c > 0 and value)
            reduced = sympy.Poly(poly.as_expr() / u**multiplicity_zero, u)
            real_count = reduced.count_roots(-sympy.oo, sympy.oo)
            tested += 1
            if real_count != reduced.degree():
                failures.append(
                    {
                        "N": n,
                        "m": m,
                        "degree_after_forced_zero": reduced.degree(),
                        "real_roots_counted_with_multiplicity": int(real_count),
                        "counts_c1_to_N": [str(x) for x in counts],
                    }
                )
                if len(failures) >= 20:
                    break
        if len(failures) >= 20:
            break

    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "The component-count polynomial sum_c W_c(N,m)u^c has only "
            "real nonpositive zeros after forced zero roots are removed. "
            "Finite results can falsify but not prove this universal claim."
        ),
        "deterministic": True,
        "random_seed": None,
        "parameters": {"n_max": args.n_max, "m_max": args.m_max},
        "environment": {
            "python": platform.python_version(),
            "sympy": sympy.__version__,
        },
        "polynomials_tested": tested,
        "failure_count": len(failures),
        "first_failures": failures,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
