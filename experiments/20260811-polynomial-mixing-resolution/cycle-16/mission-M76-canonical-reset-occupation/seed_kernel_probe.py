#!/usr/bin/env python3
"""One-dimensional rank-lowering seed-kernel diagnostics.

The reset edges with the smallest possible drop in P=s+(K-R) have parent
and child (K,R)=(1,0), refined root degree two, and P_child=P_parent-1.
This script evaluates their exact Cayley-coefficient kernel J_s(B,t),
avoiding composition enumeration.
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


def tree_weight(a: int, scaled: bool = True) -> float:
    exponent = (a - 1) * math.log(a) - math.lgamma(a + 1)
    if scaled:
        exponent -= a
    return math.exp(exponent)


def coefficient_tables(s: int, scaled: bool = True):
    v = [0.0] + [tree_weight(a, scaled) for a in range(1, s + 2)]
    # F[a,p] is the coefficient of T^p at degree a.
    F = np.zeros((s + 1, s + 1), dtype=float)
    F[0, 0] = 1.0
    for p in range(1, s + 1):
        for a in range(p, s + 1):
            F[a, p] = sum(v[x] * F[a - x, p - 1] for x in range(1, a + 1))
    A = np.zeros(s + 1)
    C = np.zeros(s + 1)
    for a in range(s + 1):
        A[a] = sum(F[a, p] / math.factorial(p + 1) for p in range(a + 1))
        C[a] = sum(
            (p + 1) * F[a, p] / math.factorial(p + 2)
            for p in range(a + 1)
        )
    return v, A, C


def kernel_row(s: int, B: int, v, A, C, scaled: bool = True):
    q = v[s + 1 - B] * v[B] / v[s + 1]
    # With v_a=e^{-a}w_a, every displayed size sum is s while the
    # denominator has size s+1. Thus p_t, M_B(t), and Q_G each acquire
    # exactly one common factor e^{-1}; q_B is scale invariant.
    scale = math.exp(-1.0) if scaled else 1.0
    row = []
    for t in range(1, s):
        probability = scale * v[t] * A[s - t] / v[s + 1]
        if t < B:
            marked = 0.0
        elif t == B:
            marked = scale * v[B] * A[s - B] / v[s + 1]
        else:
            marked = scale * v[t - B] * v[B] * C[s - t] / v[s + 1]
        capacity = scale * v[s - t] * v[t] / v[s + 1]
        value = (marked - q * probability) ** 2 / (capacity * q)
        row.append((t, value))
    return row


def normalization_audit(s: int) -> dict:
    """Compare the scaled and literal unscaled formulas before scanning."""
    v, A_v, C_v = coefficient_tables(s, scaled=True)
    w, A_w, C_w = coefficient_tables(s, scaled=False)
    coefficient_error = 0.0
    for a in range(s + 1):
        factor = math.exp(a)
        coefficient_error = max(
            coefficient_error,
            abs(A_w[a] - factor * A_v[a]) / max(abs(A_w[a]), 1e-300),
            abs(C_w[a] - factor * C_v[a]) / max(abs(C_w[a]), 1e-300),
        )
    kernel_error = 0.0
    for B in range(1, s + 1):
        scaled_row = kernel_row(s, B, v, A_v, C_v, scaled=True)
        unscaled_row = kernel_row(s, B, w, A_w, C_w, scaled=False)
        for (_, left), (_, right) in zip(scaled_row, unscaled_row):
            kernel_error = max(
                kernel_error,
                abs(left - right) / max(abs(right), 1e-300),
            )
    if coefficient_error > 5e-12 or kernel_error > 5e-11:
        raise AssertionError((s, coefficient_error, kernel_error))
    return {
        "audit_rank": s,
        "max_relative_coefficient_scaling_error": coefficient_error,
        "max_relative_kernel_error": kernel_error,
        "expected_component_scale": math.exp(-1.0),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-values", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    normalization = normalization_audit(min(max(args.s_values), 12))
    records = []
    for s in args.s_values:
        v, A, C = coefficient_tables(s, scaled=True)
        worst_log = None
        worst_plain = None
        for B in range(1, s + 1):
            row = kernel_row(s, B, v, A, C, scaled=True)
            plain = sum(value for _, value in row)
            log_parent = 1.0 + math.log(s - B + 1)
            weighted = sum(
                value * (1.0 + math.log(s - t)) / log_parent
                for t, value in row
            )
            # A degree-d P potential gains the additional factor below.
            weighted_d2 = weighted * (s / (s + 1)) ** 2
            candidate = {"s": s, "B": B, "row_sum": plain, "log_ratio": weighted}
            candidate["P2_log_ratio"] = weighted_d2
            if worst_plain is None or plain > worst_plain["row_sum"]:
                worst_plain = candidate
            if worst_log is None or weighted > worst_log["log_ratio"]:
                worst_log = candidate
        record = {
            "s": s,
            "worst_row_sum": worst_plain,
            "worst_log_weight_ratio": worst_log,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
    payload = {
        "claim_tested": (
            "The minimal-drop reset operator on seed contexts is controlled "
            "by a rank-power times suffix-logarithm weight."
        ),
        "finite_scope_warning": (
            "Finite coefficient values are falsifiers only; they do not prove "
            "a universal Cayley-coefficient inequality."
        ),
        "normalization": (
            "J_s(B,t)=[M_B(t)-q_B p_t]^2/[Q_G((s-t,t),s)q_B], "
            "with scaled Cayley weights v_a=e^{-a}w_a."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "command": (
            f"python3 -B {Path(__file__)} --s-values "
            f"{' '.join(map(str, args.s_values))} --output {args.output}"
        ),
        "parameters": vars(args) | {"output": str(args.output)},
        "normalization_audit": normalization,
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
