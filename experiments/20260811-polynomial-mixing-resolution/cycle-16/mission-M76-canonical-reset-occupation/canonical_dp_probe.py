#!/usr/bin/env python3
"""Polynomial-time exact-sum probe for one canonical marked context.

This evaluates the same one-step recurrence as ``CanonicalResolvent`` but
groups all compositions by prefix length and boundary suffix.  It therefore
reaches ranks far beyond direct enumeration.  Floating arithmetic makes it a
falsifier/calibration only; the formulas recorded in the report are exact
finite sums.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import time
from pathlib import Path

import numpy as np


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def v_weight(a: int) -> float:
    """The exponentially scaled tree weight v_a=e^{-a}a^{a-1}/a!."""
    return math.exp((a - 1) * math.log(a) - math.lgamma(a + 1) - a)


def comb_ratio(n1: int, k1: int, n2: int, k2: int) -> float:
    if not (0 <= k1 <= n1 and 0 <= k2 <= n2):
        return 0.0
    return math.exp(
        math.lgamma(n1 + 1)
        - math.lgamma(k1 + 1)
        - math.lgamma(n1 - k1 + 1)
        - math.lgamma(n2 + 1)
        + math.lgamma(k2 + 1)
        + math.lgamma(n2 - k2 + 1)
    )


def negative_hypergeometric(K: int, R: int, k: int, j: int) -> float:
    return math.exp(
        math.lgamma(R + j + 1)
        - math.lgamma(j + 1)
        - math.lgamma(R + 1)
        + math.lgamma(K - R + k - j)
        - math.lgamma(k - j + 1)
        - math.lgamma(K - R)
        - math.lgamma(K + k + 1)
        + math.lgamma(k + 1)
        + math.lgamma(K + 1)
    )


def contextual_value(
    k: int, t: int, K: int, R: int, B: int, v: list[float]
) -> float:
    if t < B:
        return 0.0
    if t == B:
        return K * comb_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    local = v[t - B] * v[B] / v[t]
    bad = comb_ratio(K, R + 1, K + k, R + 1)
    return local * (1.0 - bad)


def composition_products(s: int, v: list[float]) -> np.ndarray:
    """F[n,p]=sum over p-part compositions of n of product(v_part)."""
    F = np.zeros((s + 1, s + 1), dtype=float)
    F[0, 0] = 1.0
    for p in range(1, s + 1):
        for n in range(p, s + 1):
            F[n, p] = sum(v[a] * F[n - a, p - 1] for a in range(1, n + 1))
    return F


def analyze(
    s: int, K: int, R: int, B: int, exponent: int, log_power: int = 1,
    u_power: int = 0, positional_power: int = 0, positional_shift: int = 1,
) -> dict:
    if not (s >= 2 and K >= 1 and 0 <= R < K and 1 <= B <= s):
        raise ValueError((s, K, R, B))
    v = [0.0] + [v_weight(a) for a in range(1, s + 2)]
    F = composition_products(s, v)
    q = v[s + 1 - B] * v[B] / v[s + 1]
    u = K - R
    P = s + u
    ell = s - B + 1
    positional = (R + 1) * u / (K + 1)
    parent_phase = u**u_power * (positional + positional_shift) ** positional_power
    parent_V = (
        P**exponent * (1.0 + math.log(ell)) ** log_power * parent_phase
    )

    base = 0.0
    reset = 0.0
    reset_final = 0.0
    reset_final_by_t: dict[int, float] = {}
    reset_by_m: dict[int, float] = {}
    reset_m2_by_ct: dict[tuple[int, int], float] = {}
    # Refined edge is (A,d_1,...,d_m), where m>=1.  Its basin
    # replaces A by every ordered refinement into p>=1 parts.
    for A in range(1, s):
        for m in range(1, s - A + 1):
            suffix_total = s - A
            if suffix_total < m:
                continue
            for t in range(1, suffix_total - (m - 1) + 1):
                rest = suffix_total - t
                if m == 1 and rest != 0:
                    continue
                if m >= 2 and rest < m - 1:
                    continue
                current_core = 0.0
                for p in range(1, A + 1):
                    if F[A, p] == 0.0:
                        continue
                    k_source = p + m
                    H = contextual_value(k_source, t, K, R, B, v)
                    current_core += F[A, p] * (H - q) / math.factorial(k_source)
                if current_core == 0.0:
                    continue
                common = (
                    math.exp(-1.0)
                    * math.factorial(m)
                    * current_core**2
                    / (v[A] * v[s + 1] * q)
                )
                suffix_mass = v[t] * F[rest, m - 1]
                base += common * suffix_mass

                child_positional = (m - 1) / m
                child_phase = (child_positional + positional_shift) ** positional_power
                h_A = (1.0 + math.log(A)) ** log_power * child_phase
                weighted_suffix = 0.0
                if m == 1:
                    c = t
                    if A + c >= 3:
                        weighted_suffix = v[c] * (A + c) ** exponent * h_A
                else:
                    # d_1=c, d_m=t, with m-2 middle parts.
                    for c in range(1, rest + 1):
                        middle_total = rest - c
                        middle_mass = F[middle_total, m - 2]
                        if middle_mass and A + c >= 3:
                            weighted_suffix += (
                                v[c]
                                * middle_mass
                                * v[t]
                                * (A + c) ** exponent
                                * h_A
                            )
                contribution = common * weighted_suffix
                reset += contribution
                reset_by_m[m] = reset_by_m.get(m, 0.0) + contribution
                if m == 1:
                    reset_final += contribution
                    reset_final_by_t[t] = contribution
                elif m == 2:
                    c = rest
                    reset_m2_by_ct[(c, t)] = contribution

    deep = 0.0
    deep_mass = 0.0
    for k in range(1, s + 1):
        for t in range(1, s + 1):
            prefix = s - t
            prefix_parts = k - 1
            if F[prefix, prefix_parts] == 0.0 or t <= B:
                continue
            group_mass = (
                math.exp(-1.0)
                * F[prefix, prefix_parts]
                * v[t]
                / (math.factorial(k) * v[s + 1])
            )
            child_mean = v[t - B] * v[B] / v[t]
            for j in range(1, k + 1):
                nu = negative_hypergeometric(K, R, k, j)
                weight = group_mass * child_mean * nu / q
                deep_mass += weight
                if t - 1 >= 2:
                    child_P = t - 1 + u + k - j
                    child_ell = t - B
                    child_u = u + k - j
                    child_K = K + k
                    child_R = R + j
                    child_positional = (child_R + 1) * child_u / (child_K + 1)
                    child_phase = (
                        child_u**u_power
                        * (child_positional + positional_shift) ** positional_power
                    )
                    deep += (
                        weight
                        * child_P**exponent
                        * (1.0 + math.log(child_ell)) ** log_power
                        * child_phase
                    )

    return {
        "s": s,
        "K": K,
        "R": R,
        "u": u,
        "B": B,
        "P": P,
        "ell": ell,
        "exponent": exponent,
        "log_power": log_power,
        "u_power": u_power,
        "positional_power": positional_power,
        "positional_shift": positional_shift,
        "mean": q,
        "base": base,
        "deep_mass": deep_mass,
        "base_over_V": base / parent_V,
        "deep_over_V": deep / parent_V,
        "reset_over_V": reset / parent_V,
        "reset_final_over_V": reset_final / parent_V,
        "reset_final_by_t_over_V": {
            str(t): value / parent_V for t, value in reset_final_by_t.items()
        },
        "reset_by_m_over_V": {
            str(m): value / parent_V for m, value in reset_by_m.items()
        },
        "reset_m2_by_ct_over_V": {
            f"{c},{t}": value / parent_V
            for (c, t), value in reset_m2_by_ct.items()
        },
        "child_ratio": (deep + reset) / parent_V,
        "full_ratio": (base + deep + reset) / parent_V,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--R", type=int, required=True)
    parser.add_argument("--B", type=int, required=True)
    parser.add_argument("--exponent", type=int, default=2)
    parser.add_argument("--log-power", type=int, default=1)
    parser.add_argument("--u-power", type=int, default=0)
    parser.add_argument("--positional-power", type=int, default=0)
    parser.add_argument("--positional-shift", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    rows = []
    for s in args.s_values:
        row = analyze(
            s, args.K, args.R, args.B, args.exponent, args.log_power,
            args.u_power, args.positional_power, args.positional_shift,
        )
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    payload = {
        "claim_tested": (
            "Large-rank grouped exact sums falsify or calibrate the proposed "
            "canonical marked one-step potential."
        ),
        "finite_scope_warning": (
            "Floating evaluation of exact finite sums can refute after an "
            "error audit but cannot prove the asymptotic inequality."
        ),
        "normalization": (
            "v_a=e^{-a}w_a; G_s=R_s/alpha_s; canonical basin currents and "
            "M65 deep weights are summed without enumerating compositions."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "command": (
            f"python3 -B {Path(__file__)} --s-values "
            f"{' '.join(map(str, args.s_values))} --K {args.K} --R {args.R} "
            f"--B {args.B} --exponent {args.exponent} "
            f"--log-power {args.log_power} --u-power {args.u_power} "
            f"--positional-power {args.positional_power} "
            f"--positional-shift {args.positional_shift} --output {args.output}"
        ),
        "parameters": vars(args) | {"output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
