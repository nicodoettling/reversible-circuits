#!/usr/bin/env python3
"""High-rank numerical falsifier for the exact right-heavy two-layer limit.

All formulas are the ``K -> infinity`` limits of the frozen rational M98
formulas.  Exponential Cayley factors are scaled out before binary64
evaluation.  This script is a discovery/falsification aid; positive output is
not a proof.  Low-rank rows are checked against independent exact fractions in
``two_layer_exact.py`` before retention.
"""

from __future__ import annotations

import argparse
import functools
import json
import math
import platform
import time
from pathlib import Path


@functools.lru_cache(maxsize=None)
def v(a: int) -> float:
    """``exp(-a) a^(a-1)/a!`` computed in log space."""
    if a < 1:
        raise ValueError(a)
    return math.exp((a - 1) * math.log(a) - math.lgamma(a + 1) - a)


@functools.lru_cache(maxsize=None)
def dcayley(total: int, parts: int) -> float:
    """``exp(-total) [z^total]T(z)^parts``."""
    if parts == 0:
        return float(total == 0)
    if not 1 <= parts <= total:
        return 0.0
    return math.exp(
        math.log(parts)
        + (total - parts - 1) * math.log(total)
        - math.lgamma(total - parts + 1)
        - total
    )


@functools.lru_cache(maxsize=None)
def dL(A: int, ell: int) -> float:
    """``exp(-A) sum_p [z^A]T^p/(p+ell)!``."""
    return math.fsum(
        dcayley(A, p) * math.exp(-math.lgamma(p + ell + 1))
        for p in range(1, A + 1)
    )


@functools.lru_cache(maxsize=None)
def suffix_kernel(A: int, u: int) -> float:
    """Collapse ``sum_p dC(u,p)(p+2)! dL(A,p+2)^2``."""
    terms = []
    if u == 0:
        terms.append(2.0 * dL(A, 2) ** 2)
    for p in range(1, u + 1):
        ell = p + 2
        terms.append(
            dcayley(u, p) * math.factorial(ell) * dL(A, ell) ** 2
        )
    return math.fsum(terms)


def q_split(s: int, B: int) -> float:
    return v(s + 1 - B) * v(B) / v(s + 1)


@functools.lru_cache(maxsize=None)
def last_masses(s: int) -> tuple[float, ...]:
    rows = [0.0] * (s + 1)
    scale = math.exp(-1.0) / v(s + 1)
    for t in range(1, s + 1):
        n = s - t
        prefix = 1.0 if n == 0 else n * v(n) / (n + 1)
        rows[t] = scale * v(t) * prefix
    if abs(math.fsum(rows) - 1.0) > 2e-11:
        raise AssertionError(("last mass", s, math.fsum(rows)))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def limiting_energy_coefficients(s: int) -> tuple[float, ...]:
    """Return M98's coefficient ``e_(s,t)`` using scaled Cayley sums."""
    answer = [0.0] * (s + 1)
    common = math.exp(-1.0) / v(s + 1)

    # ell=1: A+t=s.
    for t in range(1, s):
        A = s - t
        answer[t] += (
            common
            * v(t)
            * dL(A, 1) ** 2
            / v(A)
            * (1.0 - v(A) * v(t) / v(s))
        )

    # ell=p+2>=2, with A+b+u+t=s.  The full p/ell sum is
    # collapsed into ``suffix_kernel`` before the A,b,t convolution.
    for A in range(1, s):
        inv_vA = 1.0 / v(A)
        for b in range(1, s - A):
            reward = 1.0 - v(A) * v(b) / v(A + b)
            remaining = s - A - b
            for t in range(1, remaining + 1):
                u = remaining - t
                factor_bt = common * v(b) * v(t) * inv_vA * reward
                answer[t] += factor_bt * suffix_kernel(A, u)
    return tuple(answer)


def limiting_defect(s: int, B: int) -> float:
    q = q_split(s, B)
    masses = last_masses(s)
    energy = limiting_energy_coefficients(s)
    terms = []
    for t in range(1, s + 1):
        if t <= B:
            h = float(t == s == B)
        else:
            h = q_split(t - 1, B)
        terms.append((masses[t] - energy[t]) * (h - q) ** 2)
    return math.fsum(terms)


def scan(s_max: int, emit_every: int) -> dict[str, object]:
    started = time.time()
    defects: dict[tuple[int, int], float] = {}
    rank_rows = []
    final_rank_rows = []
    global_worst = None
    negatives = []
    for s in range(2, s_max + 1):
        rank_worst = None
        masses = last_masses(s)
        for B in range(1, s + 1):
            r = limiting_defect(s, B)
            defects[s, B] = r
            qr = math.fsum(
                masses[t] * defects[t - 1, B]
                for t in range(B + 1, s + 1)
                if t - 1 >= 2
            )
            block = r + qr
            U = q_split(s, B) * (1.0 - q_split(s, B))
            row = {
                "s": s,
                "B": B,
                "r_infinity": r,
                "Q_r_infinity": qr,
                "two_layer": block,
                "normalized_r": r / U,
                "normalized_Q_r": qr / U,
                "normalized_two_layer": block / U,
            }
            if rank_worst is None or row["normalized_two_layer"] < rank_worst["normalized_two_layer"]:
                rank_worst = row
            if global_worst is None or row["normalized_two_layer"] < global_worst["normalized_two_layer"]:
                global_worst = row
            if block < 0:
                negatives.append(row)
            if s == s_max:
                final_rank_rows.append(row)
        rank_rows.append(rank_worst)
        if s % emit_every == 0 or s == s_max or negatives:
            print(json.dumps({"rank_worst": rank_worst, "elapsed_seconds": time.time() - started}), flush=True)
        if negatives:
            break
    return {
        "rank_rows": rank_rows,
        "final_rank_rows": final_rank_rows,
        "global_worst": global_worst,
        "negative_count": len(negatives),
        "first_negatives": negatives[:3],
        "elapsed_seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, required=True)
    parser.add_argument("--emit-every", type=int, default=4)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = scan(args.s_max, args.emit_every)
    payload = {
        "claim_tested": "right-heavy K-infinity global two-layer defect",
        "scope": "auxiliary nonlazy minimal-long-cycle Pbar reset operator only",
        "formula": "b_inf(s,B)=r_inf(s,B)+sum_(t>B,t-1>=2)m_(s,t)r_inf(t-1,B)",
        "finite_scope_warning": "Binary64 positive output is discovery evidence only.",
        "arithmetic": "binary64 after exact exponential scaling",
        "normalization": "right-heavy K-infinity j=k limit only; no finite attachment ranks discarded",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"s_max": args.s_max, "emit_every": args.emit_every},
        "result": result,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
