#!/usr/bin/env python3
"""Compact exact falsification checks for the M256 implication algebra."""

from fractions import Fraction as F
import json


def pref(values, d):
    return sum((values[j] for j in range(2, d + 1)), F(0))


def check_sbp(m):
    p = {d: F((-1) ** d * (d + 1), 2 * d + 1) for d in range(2, m + 1)}
    nn = {d: F((-1) ** (d + 1) * (d + 2), 3 * d + 1)
          for d in range(2, m + 1)}
    u = {d: F(2 * d - 1, d * d + 1) for d in range(2, m + 1)}
    r = {d: F(d + 3, d * d + 2) for d in range(2, m + 1)}
    a = {d: pref(nn, d) for d in range(2, m + 1)}
    c = {d: pref(p, d) for d in range(2, m + 1)}
    direct = sum((nn[d] * u[d] + p[d] * r[d]
                  for d in range(2, m + 1)), F(0))
    abel = a[m] * u[m] + c[m] * r[m]
    abel += sum((a[d] * (u[d] - u[d + 1])
                 + c[d] * (r[d] - r[d + 1])
                 for d in range(2, m)), F(0))
    assert direct == abel


hardy_rows = 0
sbp_rows = 0
for m in range(4, 65):
    for d in range(2, m + 1):
        coefficient = F(1, m) + sum(
            (F(1, D * D) for D in range(d, m)), F(0)
        )
        assert coefficient <= F(3, d)
        hardy_rows += 1
    check_sbp(m)
    sbp_rows += 1

rank_rows = 0
for k in range(3, 502, 2):
    n = 3 * k
    m = (n - 1) // 2
    den = (3 * k - 3) * (3 * k - 4)
    alpha = (
        F((k - 1) * (k - 2), den),
        F(2 * (k - 1) * (2 * k - 2), den),
        F((2 * k - 2) * (2 * k - 3), den),
    )
    assert sum(alpha, F(0)) == 1 and min(alpha) >= 0
    assert m == n // 2 and 2 * m == n - 1
    assert F((n - 3) * k, k * k) <= 3
    assert F(1, 3) <= F(k, n - 3) <= F(1, 2)
    assert F((n - 3) * (n - 4), n * n) >= F(10, 27)

    shared = 3 * (
        F(3, 2 * k - 1) + F(3 * (k - 2), k * (2 * k - 3))
    )
    endpoint = F(18 * (k - 1), k * (2 * k - 1) * (2 * k - 3))
    assert shared <= F(15, k)
    assert endpoint <= F(18, k * k)

    t_kind = F(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    assert 2 * n * t_kind <= 2

    pi_raw = F(2 * n * (n - 2) ** (n - 4), n ** (n - 2))
    pi_closed = F(2, n - 2) * F(n - 2, n) ** (n - 3)
    assert pi_raw == pi_closed
    rank_rows += 1

assert tuple(3 * x for x in (6, 3, 6, 6 * 7185)) == (
    18, 9, 18, 18 * 7185
)

print(json.dumps({
    "scope": "finite exact algebra and normalization only",
    "dv_attempted": False,
    "fd_attempted": False,
    "hardy_rows": hardy_rows,
    "sbp_rows": sbp_rows,
    "odd_rank_rows": rank_rows,
    "odd_k_range": [3, 501],
    "status": "pass",
}, indent=2, sort_keys=True))

