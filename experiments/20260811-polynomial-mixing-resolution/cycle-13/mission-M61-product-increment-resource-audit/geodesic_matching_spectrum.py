#!/usr/bin/env python3
"""Bounded exact calibration of the geodesic matching endpoint formula.

The universal proof is combinatorial and appears in checkpoint.md/report.md.
This program only checks the stated Kneser eigenvalue and Gram formulas for
small l; it cannot prove their asymptotic validity.
"""

from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction
from pathlib import Path


def record(length: int) -> dict:
    n = 2 * length
    kappa_standard = Fraction(-2, n - 2)
    kappa_two_row = Fraction(2, (n - 2) * (n - 3))
    candidates = {
        "negative_once": Fraction(1 + (length - 1) * kappa_standard, length),
        "negative_orthogonal": Fraction(1 - kappa_standard, length),
        "two_row_once": Fraction(1 + (length - 1) * kappa_two_row, length),
        "two_row_orthogonal": Fraction(1 - kappa_two_row, length),
        "antisymmetric": Fraction(1, length),
    }
    mu = max(candidates.values())
    return {
        "length": length,
        "atom_count": n,
        "kappa_standard": str(kappa_standard),
        "kappa_two_row": str(kappa_two_row),
        "gram_candidates": {k: str(v) for k, v in candidates.items()},
        "mu": str(mu),
        "claimed_mu": str(Fraction(1, length - 1)),
        "matches": mu == Fraction(1, length - 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--l-max", type=int, default=20)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "claim_falsified_if_mismatch": (
            "for the endpoint made of 2l disjoint transpositions, mu_l=1/(l-1)"
        ),
        "scope_warning": (
            "Finite rational substitution checks formulas only; the universal "
            "geodesic and Kneser-spectrum proof is separate."
        ),
        "records": [record(length) for length in range(3, args.l_max + 1)],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
