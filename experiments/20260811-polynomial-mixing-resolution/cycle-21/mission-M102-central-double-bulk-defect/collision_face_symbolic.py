#!/usr/bin/env python3
"""Symbolic certificate for M102's nonintegrable naive bulk collision face.

The exact rational cell is

    s=(1/10,1/9,24/25,24/25+delta),
    t=(1/7,9/20,5/7,15/16),

with separated intermediate s.  The script records the positive rational
products whose square-root ratio is the coefficient of delta^(-3/2).
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


F = Fraction


def prod(values: list[Fraction]) -> Fraction:
    out = F(1)
    for value in values:
        out *= value
    return out


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    # Limit delta -> 0.  These residual-length lists come from the exact
    # cycle topology of source A, the separated intermediate, and the two
    # central target colors.  Every number is strictly positive.
    a_lengths = [F(1, 90), F(29, 90), F(1, 3), F(1, 3)]
    b_lengths = [F(1, 90), F(1, 3), F(59, 90)]
    s_regular = [F(1, 90), F(89, 90)]
    joint_ss_regular = [F(1, 90), F(25, 112), F(43, 140), F(2311, 5040)]
    joint_sn_regular = [F(1, 90), F(979, 5040), F(37, 140), F(297, 560)]
    source_a_denominator = F(1, 27)  # product of A's three 1/3 residuals
    source_b_denominator = F(2, 9)   # product of B's positive 1/3,2/3 residuals

    # For a positive list L, `power(L)=prod(L)^(-3/2)`.  The exact coefficient
    # is a product of positive radicals and the signed source radical
    # `source_base_B^(3/2)-source_base_A^(3/2)`.  The latter is negative
    # because its bases satisfy the exact rational inequality below.
    source_base_a = source_a_denominator / prod(a_lengths)
    source_base_b = source_b_denominator / prod(b_lengths)
    intermediate_base = prod(s_regular)
    joint_base_ss = F(1, 1) / prod(joint_ss_regular)
    joint_base_sn = F(1, 1) / prod(joint_sn_regular)
    assert source_base_b < source_base_a
    assert intermediate_base > 0 and joint_base_ss > 0 and joint_base_sn > 0
    floating_coefficient = (
        float(source_base_b) ** 1.5 - float(source_base_a) ** 1.5
    ) * float(intermediate_base) ** 1.5 * (
        float(joint_base_ss) ** 1.5 + float(joint_base_sn) ** 1.5
    )

    payload = {
        "status": "exact_symbolic_collision_face_certificate",
        "claim": "naive channel-combined double/double bulk integrand is nonintegrable",
        "cell": {
            "s": ["1/10", "1/9", "24/25", "24/25+delta"],
            "t": ["1/7", "9/20", "5/7", "15/16"],
            "intermediate_color": "S",
        },
        "source_A_residual_lengths_after_removing_delta": [text(x) for x in a_lengths],
        "source_B_positive_residual_lengths_after_removing_delta_and_singleton": [text(x) for x in b_lengths],
        "intermediate_residual_lengths_after_removing_delta": [text(x) for x in s_regular],
        "joint_SS_residual_lengths_after_removing_delta": [text(x) for x in joint_ss_regular],
        "joint_SN_residual_lengths_after_removing_delta": [text(x) for x in joint_sn_regular],
        "coefficient": {
            "form": "(source_base_B^(3/2)-source_base_A^(3/2))*intermediate_base^(3/2)*(joint_base_SS^(3/2)+joint_base_SN^(3/2))",
            "source_base_A": text(source_base_a),
            "source_base_B": text(source_base_b),
            "source_base_B_less_than_A": source_base_b < source_base_a,
            "intermediate_base": text(intermediate_base),
            "joint_base_SS": text(joint_base_ss),
            "joint_base_SN": text(joint_base_sn),
            "strictly_negative": True,
            "floating_value": floating_coefficient,
        },
        "asymptotic": "F(delta)=-C delta^(-3/2)+O(delta^(-1/2)), C>0",
        "integrability": "integral_0^epsilon F(delta) ddelta diverges to -infinity",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
