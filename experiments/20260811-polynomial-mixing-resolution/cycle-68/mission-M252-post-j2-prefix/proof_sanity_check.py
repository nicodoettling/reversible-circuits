#!/usr/bin/env python3
"""Narrow exact sanity checks for M252.

Finite checks below are falsification aids only. The all-rank proof is the
algebra in post_j2_wpcr_theorem.md.
"""

from fractions import Fraction
import json


hardy_rows = 0
for m in range(4, 257):
    tail = Fraction(0)
    weights = {}
    for d in range(m - 1, 1, -1):
        tail += Fraction(1, d * d)
        weights[d] = Fraction(1, m) + tail
    weights[m] = Fraction(1, m)
    for d in range(2, m + 1):
        assert weights[d] <= Fraction(3, d)
        hardy_rows += 1

endpoint_rows = 0
for k in range(3, 256, 2):
    shared = 3 * (
        Fraction(3, 2 * k - 1)
        + Fraction(3 * (k - 2), k * (2 * k - 3))
    )
    endpoint = Fraction(18 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert shared <= Fraction(15, k)
    assert endpoint <= Fraction(18, k * k)
    # endpoint <= 6 sqrt(D)/k for every D>=2, checked after squaring at D=2.
    assert (endpoint * k / 6) ** 2 <= 2
    endpoint_rows += 1

print(
    json.dumps(
        {
            "status": "pass",
            "hardy_exact_rows": hardy_rows,
            "odd_k_endpoint_rows": endpoint_rows,
            "scope": "finite exact falsification only; theorem proof is all-rank",
        },
        indent=2,
        sort_keys=True,
    )
)

