#!/usr/bin/env python3
"""Exact falsification harness for component-layer log concavity.

Universal claim tested (finite arithmetic can only falsify it): for every
N,m, the exact layer counts W_c(N,m) are log-concave in c after zeros outside
their feasible interval are removed.  The script computes counts from the
Frobenius character trace and the labeled exponential/component recurrence;
it does not enumerate words or sample randomly.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from functools import lru_cache
from pathlib import Path


def partitions(n: int, max_part: int | None = None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dimension(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            below = sum(1 for lower in shape[i + 1 :] if lower > j)
            hooks *= row - j + below
    return math.factorial(n) // hooks


def content_sum(shape: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


@lru_cache(maxsize=None)
def total_identity(v: int, k: int) -> int:
    if v <= 1:
        return int(k == 0)
    numerator = 0
    for shape in partitions(v):
        dim = hook_dimension(shape)
        numerator += dim * dim * pow(content_sum(shape), k)
    value, remainder = divmod(numerator, math.factorial(v))
    assert remainder == 0
    return value


def connected_table(n_max: int, m_max: int):
    # C[v][k]: connected exact-support identity words on a fixed v-set.
    C = [[0] * (m_max + 1) for _ in range(n_max + 1)]
    C[1][0] = 1
    for v in range(2, n_max + 1):
        for k in range(m_max + 1):
            value = total_identity(v, k)
            # Remove decompositions whose component containing label 1 has
            # size s<v.  The remaining term is exactly C[v][k].
            for s in range(1, v):
                choose_labels = math.comb(v - 1, s - 1)
                for ell in range(k + 1):
                    if C[s][ell] == 0:
                        continue
                    rest = total_identity(v - s, k - ell)
                    if rest:
                        value -= (
                            choose_labels
                            * math.comb(k, ell)
                            * C[s][ell]
                            * rest
                        )
            assert value >= 0, (v, k, value)
            C[v][k] = value
    return C


def layer_table(n_max: int, m_max: int, C):
    # W[n][m][c]: exact words on n labels with c support components,
    # including isolated singleton components.
    W = [
        [[0] * (n_max + 1) for _ in range(m_max + 1)]
        for _ in range(n_max + 1)
    ]
    W[0][0][0] = 1
    for n in range(1, n_max + 1):
        for m in range(m_max + 1):
            for c in range(1, n + 1):
                value = 0
                for s in range(1, n + 1):
                    choose_labels = math.comb(n - 1, s - 1)
                    for ell in range(m + 1):
                        if C[s][ell] == 0:
                            continue
                        rest = W[n - s][m - ell][c - 1]
                        if rest:
                            value += (
                                choose_labels
                                * math.comb(m, ell)
                                * C[s][ell]
                                * rest
                            )
                W[n][m][c] = value
    return W


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=10)
    parser.add_argument("--m-max", type=int, default=60)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    C = connected_table(args.n_max, args.m_max)
    W = layer_table(args.n_max, args.m_max, C)

    failures = []
    records = []
    for n in range(2, args.n_max + 1):
        for m in range(0, args.m_max + 1, 2):
            counts = [W[n][m][c] for c in range(1, n + 1)]
            positive = [i for i, x in enumerate(counts) if x > 0]
            if not positive:
                continue
            lo, hi = min(positive), max(positive)
            internal_zero = any(counts[i] == 0 for i in range(lo, hi + 1))
            violations = []
            for i in range(lo + 1, hi):
                if counts[i] * counts[i] < counts[i - 1] * counts[i + 1]:
                    violations.append(i + 1)  # component count, not index
            if internal_zero or violations:
                failures.append(
                    {
                        "N": n,
                        "m": m,
                        "counts_c1_to_N": [str(x) for x in counts],
                        "internal_zero": internal_zero,
                        "violating_component_counts": violations,
                    }
                )
            if (n, m) in {(3, 4), (4, 4), (4, 6)}:
                records.append(
                    {
                        "N": n,
                        "m": m,
                        "counts_c1_to_N": [str(x) for x in counts],
                        "total": str(sum(counts)),
                    }
                )

    payload = {
        "repository_commit": "502a6f031c6d5a4bc0064ee5b370a4fa3914f993",
        "claim_tested": (
            "Exact component-layer counts W_c(N,m) are log-concave in c "
            "on their feasible interval. Finite results can falsify but not "
            "prove this universal claim."
        ),
        "deterministic": True,
        "random_seed": None,
        "parameters": {"n_max": args.n_max, "m_max": args.m_max},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "nonstandard_dependencies": [],
        },
        "calibration_records": records,
        "failure_count": len(failures),
        "first_failures": failures[:20],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
