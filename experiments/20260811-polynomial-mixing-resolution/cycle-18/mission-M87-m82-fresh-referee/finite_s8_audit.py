#!/usr/bin/env python3
"""Independent full rank-eight eliminated-row scan for the M82 referee."""

from __future__ import annotations

import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import independent_audit as core


def record(value: Fraction, context: tuple[int, int, int, int]) -> dict:
    return {
        "context": list(context),
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    maxima: dict[str, tuple[Fraction, tuple[int, int, int, int] | None]] = {
        "unweighted": (Fraction(-1), None),
        "right_heavy_unweighted": (Fraction(-1), None),
        "row_over_multitype_bound": (Fraction(-1), None),
        "weighted_eliminated_over_parent": (Fraction(-1), None),
    }
    failures = {key: 0 for key in maxima}
    first_unweighted_failure = None
    contexts = 0
    for s in range(2, 9):
        for K in range(1, 9):
            for R in range(K):
                if R == 0 and K > 1:
                    continue
                for B in range(1, s + 1):
                    x = (s, K, R, B)
                    contexts += 1
                    kernel = core.eliminated_reset(*x)
                    row = sum(kernel.values(), Fraction())
                    q = core.split_mass(s, B)
                    multitype = (K - R) * (1 - q)
                    W_parent = core.phase_potential(x, 0)
                    W_image = sum(
                        (
                            coefficient * core.phase_potential(child, 0)
                            for child, coefficient in kernel.items()
                        ),
                        Fraction(),
                    )
                    values = {
                        "unweighted": row,
                        "row_over_multitype_bound": row / multitype,
                        "weighted_eliminated_over_parent": W_image / W_parent,
                    }
                    if K - R == 1:
                        values["right_heavy_unweighted"] = row
                    for key, value in values.items():
                        if value > maxima[key][0]:
                            maxima[key] = (value, x)
                        if value > 1:
                            failures[key] += 1
                    if row > 1 and first_unweighted_failure is None:
                        first_unweighted_failure = record(row, x)

    assert contexts == 1015
    assert first_unweighted_failure is not None
    assert first_unweighted_failure["context"] == [6, 8, 1, 2]
    result = {
        "claim_tested": "Independent full rank-eight eliminated M82 scan",
        "imports_predecessor_code": False,
        "imports_only_owned_core": True,
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "scope": "2<=s<=8, 1<=K<=8, exact reachable closure, every B",
        "contexts": contexts,
        "maxima": {
            key: record(value, context)  # type: ignore[arg-type]
            for key, (value, context) in maxima.items()
        },
        "failure_counts": failures,
        "first_unweighted_failure": first_unweighted_failure,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = Path("finite_s8_audit.json")
    output.write_text(encoded)
    print(json.dumps({
        "output": str(output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "contexts": contexts,
        "failure_counts": failures,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
