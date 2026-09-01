#!/usr/bin/env python3
"""Compact post-identity diagnostic for the exact B-side Y profile.

Finite floating-point output is used only to attack candidate analytic bounds.
It is not proof of DV.  No permutation or factorization enumeration occurs.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path


def log_b(j: int) -> float:
    return -j + (j - 1) * math.log(j) - math.lgamma(j + 1)


def kernel(R: int, r: int, d: int) -> float:
    return math.exp(log_b(d) + log_b(r - d) - log_b(r)) / R


def h(R: int, r: int) -> float:
    return (r - 1) * (r - 2) / (r * R)


def exterior_word(k: int) -> list[int]:
    return list(range(1, k)) + list(range(2 * k, 3 * k))


def f_profile(k: int, ell: int) -> list[float]:
    n, D = 3 * k, 2 * k - 1
    v = exterior_word(k)
    out = [0.0] * D
    for x in range(1, D):
        out[x] = sum(
            2 <= (v[(i + x) % D] - v[i]) % n <= ell for i in range(D)
        ) / D
    return out


def y_values(k: int, ell: int) -> list[float]:
    D, R = 2 * k - 1, 2 * k - 3
    f = f_profile(k, ell)
    w = [0.0] * D
    for r in range(1, D):
        w[r] = sum(
            (r - d - 1) * kernel(R, r, d) * f[d]
            for d in range(1, r - 1)
        )
    ans = [0.0] * k
    for s in range(1, k):
        q = D - s
        numerator = h(R, s) * f[q] + h(R, q) * f[s] + w[s] + w[q]
        ans[s] = numerator / (h(R, s) + h(R, q))
    return ans


def case(k: int, ell: int) -> dict:
    values = y_values(k, ell)
    diffs = [values[s + 1] - values[s] for s in range(1, k - 1)]
    signs = [0 if abs(x) < 1e-13 else (1 if x > 0 else -1) for x in diffs]
    changes = sum(a != b for a, b in zip(signs, signs[1:]) if a and b)
    return {
        "k": k,
        "ell": ell,
        "dv_ratio_Y": sum(math.sqrt(s) * abs(diffs[s - 1]) for s in range(1, k - 1)) / math.sqrt(ell),
        "unweighted_total_variation_Y": sum(map(abs, diffs)),
        "sign_changes_ignoring_zeros": changes,
        "min": min(values[1:]),
        "max": max(values[1:]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    rows = []
    for k in (5, 9, 21, 51, 101, 201):
        candidates = sorted({2, min(5, (3 * k - 1) // 2), k // 4, k // 2, k - 1, k, k + 1, (3 * k - 1) // 2})
        for ell in candidates:
            if 2 <= ell <= (3 * k - 1) // 2:
                rows.append(case(k, ell))
    payload = {
        "mission": "M251",
        "method": "exact closed Y formula evaluated in floating point after paired identity was fixed",
        "python": platform.python_version(),
        "seed": None,
        "finite_only": True,
        "universal_inference": False,
        "rows": rows,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
