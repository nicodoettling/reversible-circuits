#!/usr/bin/env python3
"""Compact exact checks for the M256 implication algebra.

This checks finite identities and boundary normalizations only. It neither
tests nor attempts DV/TAV, FD, or any asymptotic theorem.
"""

from fractions import Fraction as Q
import json
import platform


def prefix(values, d):
    return sum((values[x] for x in range(2, d + 1)), Q(0))


def check_sbp(m):
    # Arbitrary deterministic rational coefficients and response sequences.
    p = {d: Q((-1) ** d * (d + 1), 2 * d + 1) for d in range(2, m + 1)}
    nn = {d: Q((-1) ** (d + 1) * (d + 2), 3 * d + 1)
          for d in range(2, m + 1)}
    u2 = {d: Q(2 * d - 1, d * d + 1) for d in range(2, m + 1)}
    rr = {d: Q(d + 3, d * d + 2) for d in range(2, m + 1)}
    aa = {d: prefix(nn, d) for d in range(2, m + 1)}
    cc = {d: prefix(p, d) for d in range(2, m + 1)}
    direct = sum((nn[d] * u2[d] + p[d] * rr[d]
                  for d in range(2, m + 1)), Q(0))
    abel = aa[m] * u2[m] + cc[m] * rr[m]
    abel += sum((aa[d] * (u2[d] - u2[d + 1])
                 + cc[d] * (rr[d] - rr[d + 1])
                 for d in range(2, m)), Q(0))
    assert direct == abel


def check_tv_close(values):
    variation = sum(abs(values[i + 1] - values[i])
                    for i in range(len(values) - 1))
    assert sum(map(abs, values)) <= abs(sum(values)) + len(values) * variation


hardy_rows = 0
sbp_rows = 0
normalization_rows = 0
for m in range(4, 65):
    for d in range(2, m + 1):
        coefficient = Q(1, m) + sum((Q(1, D * D)
                                     for D in range(d, m)), Q(0))
        assert coefficient <= Q(3, d)
        hardy_rows += 1
    check_sbp(m)
    sbp_rows += 1

for length in range(1, 33):
    check_tv_close([Q((i % 5) - 2, (i % 3) + 1) for i in range(length)])

for k in range(3, 102, 2):
    n = 3 * k
    m = (n - 1) // 2
    sequence_length = n - 3
    assert 2 * m == n - 1
    assert m == n // 2
    assert Q(1, 3) <= Q(k, sequence_length) <= Q(1, 2)
    assert Q(sequence_length * k, k * k) <= 3

    den = (3 * k - 3) * (3 * k - 4)
    alpha0 = Q((k - 1) * (k - 2), den)
    alpha1 = Q(2 * (k - 1) * (2 * k - 2), den)
    alpha2 = Q((2 * k - 2) * (2 * k - 3), den)
    assert alpha0 + alpha1 + alpha2 == 1
    assert min(alpha0, alpha1, alpha2) >= 0

    rn = (n - 3) * (n - 4)
    assert Q(rn, n * n) >= Q(10, 27)
    t_kind = Q(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    assert 2 * n * t_kind <= 2

    pi_raw = Q(2 * n * (n - 2) ** (n - 4), n ** (n - 2))
    pi_closed = Q(2, n - 2) * Q(n - 2, n) ** (n - 3)
    assert pi_raw == pi_closed
    normalization_rows += 1

# M252's scaled full-WPCR constant, coefficient by coefficient.
# Order: K1, K2, K_E*K_V, numerical DE/shared/endpoint constant.
unscaled = (6, 3, 6, 6 * 7185)
scaled_by_n_over_k = tuple(3 * x for x in unscaled)
assert scaled_by_n_over_k == (18, 9, 18, 18 * 7185)

result = {
    "claim_scope": "finite exact algebra and normalization only",
    "dv_tav_attempted": False,
    "fd_attempted": False,
    "hardy_coefficient_rows": hardy_rows,
    "sbp_identity_rows": sbp_rows,
    "tv_close_rows": 32,
    "normalization_rows": normalization_rows,
    "odd_k_range": [3, 101],
    "wpcr_scaled_coefficients": {
        "K1": 18,
        "K2": 9,
        "K_E_times_K_V": 18,
        "constant": 18 * 7185,
    },
    "python": platform.python_version(),
    "seed": None,
    "status": "pass",
}
print(json.dumps(result, indent=2, sort_keys=True))
