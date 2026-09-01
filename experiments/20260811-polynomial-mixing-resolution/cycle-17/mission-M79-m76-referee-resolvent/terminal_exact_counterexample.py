#!/usr/bin/env python3
"""Exact-rational certificate against M76 inequality (8.1).

Take the reachable right-heavy seed x=(s,1,0,s).  Its contextual root
observable is one on the unary composition (s) and zero elsewhere.  There
are no deep children because no last part exceeds B=s, so

    q_x [(I-D)^(-1) J h](x) = sum_e theta_e^2/[Q_G(e) q_e].

For a canonical first-boundary edge with refined endpoint
(A,b,c_3,...,c_{l+1}), its basin never contains the unary composition.
Thus theta=-q_x*rho(basin).  Cayley composition coefficients sum basin and
suffix weights exactly, reducing the certificate to a finite rational sum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from fractions import Fraction
from pathlib import Path


def w(a: int) -> Fraction:
    return Fraction(a ** (a - 1), math.factorial(a))


def cayley_coefficient(a: int, p: int) -> Fraction:
    """[z^a]T(z)^p for T=sum_{n>=1} w_n z^n."""
    if a == 0 and p == 0:
        return Fraction(1)
    if not (1 <= p <= a):
        return Fraction(0)
    return Fraction(p * a ** (a - p), a * math.factorial(a - p))


def exact_values(s: int) -> tuple[Fraction, Fraction, Fraction]:
    q_parent = w(s) / w(s + 1)
    total = Fraction(0)
    row_sum = Fraction(0)
    # l is suffix length; refined root degree is l+1.
    for l in range(1, s):
        for A in range(1, s + 1):
            basin_prefix = sum(
                (
                    cayley_coefficient(A, p) / math.factorial(p + l)
                    for p in range(1, A + 1)
                ),
                Fraction(0),
            )
            if not basin_prefix:
                continue
            for b in range(1, s - A + 1):
                tail_total = s - A - b
                tail_parts = l - 1
                suffix_product_sum = w(b) * cayley_coefficient(
                    tail_total, tail_parts
                )
                if not suffix_product_sum:
                    continue
                child_rank = A + b - 1
                if child_rank < 2:
                    continue
                q_child = w(A) * w(b) / w(A + b)
                theta_scalar = -q_parent * basin_prefix
                edge_energy_sum = (
                    suffix_product_sum
                    / w(s + 1)
                    * math.factorial(l)
                    / w(A)
                    * theta_scalar
                    * theta_scalar
                )
                total += edge_energy_sum / q_child
                row_sum += edge_energy_sum / q_parent
    degree_two = q_parent ** 3 * sum(
        (Fraction(A, A + 1) ** 2 for A in range(1, s)),
        Fraction(0),
    )
    return total, row_sum, degree_two


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", default=[18, 19, 20, 21])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = []
    for s in args.s_values:
        ratio, row_sum, degree_two = exact_values(s)
        records.append(
            {
                "s": s,
                "context": [s, 1, 0, s],
                "ratio_numerator": str(ratio.numerator),
                "ratio_denominator": str(ratio.denominator),
                "ratio_decimal": float(ratio),
                "difference_from_one_numerator": str(
                    ratio.numerator - ratio.denominator
                ),
                "strict_counterexample": ratio > 1,
                "plain_reset_row_sum_numerator": str(row_sum.numerator),
                "plain_reset_row_sum_denominator": str(row_sum.denominator),
                "plain_reset_row_sum_decimal": float(row_sum),
                "degree_two_subrow_numerator": str(degree_two.numerator),
                "degree_two_subrow_denominator": str(degree_two.denominator),
                "degree_two_subrow_decimal": float(degree_two),
                "degree_two_identity": (
                    "q_s^3 sum_(A=1)^(s-1) (A/(A+1))^2"
                ),
            }
        )
    payload = {
        "claim_tested": (
            "sum_y[(I-D)^-1 J_can](x,y)/q_y <= 1/q_x on every right-heavy x"
        ),
        "arithmetic": "fractions.Fraction exact rational Cayley-coefficient sum",
        "normalization": (
            "G_s=R_s/alpha_s; q_x=w_s/w_(s+1); D=0 at B=s; "
            "edge capacity Q_G=rho(refined)*(root degree)"
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "records": records,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "records": records,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
