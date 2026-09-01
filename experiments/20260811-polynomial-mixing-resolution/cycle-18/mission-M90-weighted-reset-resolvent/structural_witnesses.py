#!/usr/bin/env python3
"""Freeze exact witnesses rejecting tempting variance/Bessel shortcuts."""

from __future__ import annotations

import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import contextual_second_moment as MOMENT
import exact_unweighted_resolvent as UNWEIGHTED
import exact_weighted_resolvent as EXACT


def record(value: Fraction) -> dict[str, object]:
    return {
        "decimal": float(value),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def variance_of_root_mean(x: tuple[int, int, int, int]) -> Fraction:
    s, K, R, B = x
    q = EXACT.q_split(s, B)
    return sum(
        (
            mass * (EXACT.contextual_value(k, t, K, R, B) - q) ** 2
            for k, t, mass in EXACT.groups(s)
        ),
        Fraction(),
    )


def contextual_max(x: tuple[int, int, int, int]):
    s, K, R, B = x
    value, k, t = max(
        (
            (EXACT.contextual_value(k, t, K, R, B), k, t)
            for k, t, _ in EXACT.groups(s)
        ),
        key=lambda row: row[0],
    )
    return value, k, t


def main() -> None:
    moments = MOMENT.SecondMoment()
    solver = UNWEIGHTED.ExactUnweighted()

    h_over_variance_x = (8, 1, 0, 3)
    q = EXACT.q_split(h_over_variance_x[0], h_over_variance_x[3])
    h = solver.h(*h_over_variance_x)
    variance = moments.variance(*h_over_variance_x)

    raw_bessel_x = (11, 1, 0, 4)
    A0 = UNWEIGHTED.reset_unweighted_budget(*raw_bessel_x)
    root_variance = variance_of_root_mean(raw_bessel_x)

    nonprobability_x = (12, 32, 5, 4)
    max_H, max_k, max_t = contextual_max(nonprobability_x)

    payload = {
        "claim_tested": "exact witnesses rejecting direct variance/Bernoulli shortcuts",
        "arithmetic": "fractions.Fraction exact grouped formulas",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "witnesses": {
            "unweighted_resolvent_exceeds_contextual_variance": {
                "context": list(h_over_variance_x),
                "q": record(q),
                "transformed_unweighted_resolvent": record(h),
                "contextual_variance": record(variance),
                "difference": record(h - variance),
                "ratio": record(h / variance),
            },
            "raw_unweighted_reset_energy_exceeds_root_mean_variance": {
                "context": list(raw_bessel_x),
                "A0": record(A0),
                "variance_of_root_mean": record(root_variance),
                "difference": record(A0 - root_variance),
                "ratio": record(A0 / root_variance),
            },
            "nonright_contextual_statistic_not_probability_valued": {
                "context": list(nonprobability_x),
                "root_group": {"k": max_k, "t": max_t},
                "contextual_value": record(max_H),
                "excess_over_one": record(max_H - 1),
            },
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = Path("structural_witnesses.json")
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "witnesses": payload["witnesses"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
