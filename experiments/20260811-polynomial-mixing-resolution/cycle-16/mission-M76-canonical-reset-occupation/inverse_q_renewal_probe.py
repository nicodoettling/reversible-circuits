#!/usr/bin/env python3
"""Bounded falsifier for inverse-split-mass renewal superharmonicity.

For a context x=(s,K,R,B), put

    q_x = w_(s+1-B) w_B / w_(s+1),   h_x = 1/q_x.

This script compares the raw Bellman rows D+J_can with the pure-deep
eliminated rows (I-D)^(-1)J_can.  Finite passes are diagnostics only.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import time
from pathlib import Path

import numpy as np
import scipy

from reset_renewal_probe import Renewal, base


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def inverse_q(context) -> float:
    s, _, _, B = context
    return 1.0 / base.w_ratio(s + 1 - B, B)


def update_worst(current, ratio, row):
    if current is None or ratio > current["ratio"]:
        answer = dict(row)
        answer["ratio"] = ratio
        return answer
    return current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=14)
    parser.add_argument("--K-max", type=int, default=16)
    parser.add_argument("--K-slices", type=int, nargs="*", default=[64, 256, 4096])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 14:
        raise SystemExit("bounded range is 2 <= s-max <= 14")

    started = time.time()
    renewal = Renewal(args.s_max)
    K_values = sorted(set(range(1, args.K_max + 1)) | set(args.K_slices))
    records = []
    for s in range(2, args.s_max + 1):
        worst = {
            "raw_child": None,
            "raw_with_base": None,
            "eliminated_child": None,
            "eliminated_with_base": None,
            "eliminated_row_sum": None,
        }
        for K in K_values:
            context_prefix = (s, K, K - 1)
            for B in range(1, s + 1):
                context = context_prefix + (B,)
                parent_h = inverse_q(context)
                a, deep, reset, _ = renewal.split(*context)
                raw_child = sum(
                    weight * inverse_q(child)
                    for child, weight in deep.items()
                ) + sum(
                    weight * inverse_q(child)
                    for child, weight in reset.items()
                )
                base_cost, eliminated = renewal.eliminated(*context)
                eliminated_child = sum(
                    weight * inverse_q(child)
                    for child, weight in eliminated.items()
                )
                row_sum = sum(eliminated.values())
                row = {
                    "s": s,
                    "K": K,
                    "R": K - 1,
                    "B": B,
                    "q_parent": 1.0 / parent_h,
                    "h_parent": parent_h,
                    "raw_base": a,
                    "eliminated_base": base_cost,
                    "raw_deep_mass": sum(deep.values()),
                    "raw_reset_mass": sum(reset.values()),
                    "eliminated_reset_mass": row_sum,
                }
                worst["raw_child"] = update_worst(
                    worst["raw_child"], raw_child / parent_h, row
                )
                worst["raw_with_base"] = update_worst(
                    worst["raw_with_base"], (a + raw_child) / parent_h, row
                )
                worst["eliminated_child"] = update_worst(
                    worst["eliminated_child"], eliminated_child / parent_h, row
                )
                worst["eliminated_with_base"] = update_worst(
                    worst["eliminated_with_base"],
                    (base_cost + eliminated_child) / parent_h,
                    row,
                )
                worst["eliminated_row_sum"] = update_worst(
                    worst["eliminated_row_sum"], row_sum, row
                )
        record = {"s": s, "worst": worst}
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)

    payload = {
        "claim_tested": (
            "For right-heavy seeds, inverse stationary split mass is a "
            "superharmonic potential for the pure-deep-eliminated canonical "
            "reset kernel; the raw one-step version is tested separately."
        ),
        "finite_scope_warning": (
            "A ratio above one refutes the named inequality. Ratios below "
            "one at bounded ranks prove no universal inequality."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; q_x=w_(s+1-B)w_B/w_(s+1); "
            "J_can=theta_e^2/[Q_G(e)q_x]; D is M65's exact marked kernel."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            f"python3 -B {Path(__file__)} --s-max {args.s_max} "
            f"--K-max {args.K_max} --K-slices "
            f"{' '.join(map(str, args.K_slices))} --output {args.output}"
        ),
        "parameters": vars(args) | {"output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "deep_mass_identity_max_abs_error": renewal.solver.max_deep_mass_error,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
