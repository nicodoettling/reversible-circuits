#!/usr/bin/env python3
"""Finite falsifier for the descending potential P=s+(K-R).

For the canonical marked recurrence this records separately the deep and
first-boundary reset contributions to

    V_p(x) = (s + K - R)^p [1 + log(s-B+1)].

The ambient-feasible coordinate is s+(K-R), not s+K.  We therefore scan
large K at fixed u=K-R.  A finite pass is not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
M71 = HERE.parents[1] / "cycle-15" / "mission-M71-marked-weighted-green-contraction"
sys.path.insert(0, str(M71))

from reset_renewal_probe import Renewal  # noqa: E402


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def potential(
    context: tuple[int, int, int, int], exponent: int, u_power: int,
    positional_power: int, positional_shift: int,
) -> float:
    s, K, R, B = context
    u = K - R
    P = s + K - R
    ell = s - B + 1
    positional = (R + 1) * u / (K + 1)
    phase = (positional + positional_shift) ** positional_power
    return float(P**exponent * u**u_power * phase * (1.0 + math.log(ell)))


def k_slices(u: int, k_scan: int) -> list[int]:
    values = set(range(u, max(u, k_scan) + 1))
    values.update(max(u, x) for x in (64, 128, 256, 1024, 4096))
    return sorted(values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-max", type=int, default=15)
    parser.add_argument("--k-scan", type=int, default=16)
    parser.add_argument("--exponents", type=int, nargs="+", default=[1, 2, 3, 4])
    parser.add_argument("--u-powers", type=int, nargs="+", default=[0])
    parser.add_argument("--positional-powers", type=int, nargs="+", default=[0])
    parser.add_argument("--positional-shifts", type=int, nargs="+", default=[0])
    parser.add_argument("--reachable-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.p_max <= 15:
        raise SystemExit("bounded implementation requires 3 <= p-max <= 15")

    started = time.time()
    renewal = Renewal(args.p_max - 1)
    records = []
    labels = [
        (p, q, a, b, f"P^{p}u^{q}(w+{b})^{a}")
        for p in args.exponents for q in args.u_powers
        for a in args.positional_powers for b in args.positional_shifts
    ]
    global_worst = {label: None for _, _, _, _, label in labels}
    for P in range(3, args.p_max + 1):
        worst = {label: None for _, _, _, _, label in labels}
        scanned = 0
        for s in range(2, P):
            u = P - s
            for K in k_slices(u, args.k_scan):
                R = K - u
                if R < 0:
                    continue
                if args.reachable_only and R == 0 and u > 1:
                    continue
                for B in range(1, s + 1):
                    context = (s, K, R, B)
                    base_cost, deep, reset, rows = renewal.split(*context)
                    assert all(
                        row["child_budget"] == row["child_rank"] + row["child_K"]
                        for row in rows
                    )
                    for exponent, u_power, pos_power, pos_shift, label in labels:
                        parent = potential(
                            context, exponent, u_power, pos_power, pos_shift
                        )
                        deep_demand = sum(
                            weight * potential(
                                child, exponent, u_power, pos_power, pos_shift
                            )
                            for child, weight in deep.items()
                        )
                        reset_demand = sum(
                            weight * potential(
                                child, exponent, u_power, pos_power, pos_shift
                            )
                            for child, weight in reset.items()
                        )
                        row = {
                            "P": P,
                            "s": s,
                            "K": K,
                            "R": R,
                            "u": u,
                            "B": B,
                            "ell": s - B + 1,
                            "exponent": exponent,
                            "u_power": u_power,
                            "positional_power": pos_power,
                            "positional_shift": pos_shift,
                            "base_over_V": base_cost / parent,
                            "deep_over_V": deep_demand / parent,
                            "reset_over_V": reset_demand / parent,
                            "child_ratio": (deep_demand + reset_demand) / parent,
                            "full_ratio": (base_cost + deep_demand + reset_demand) / parent,
                            "deep_mass": sum(deep.values()),
                            "reset_mass": sum(reset.values()),
                        }
                        key = label
                        if worst[key] is None or row["full_ratio"] > worst[key]["full_ratio"]:
                            worst[key] = row
                        if (
                            global_worst[key] is None
                            or row["full_ratio"] > global_worst[key]["full_ratio"]
                        ):
                            global_worst[key] = row
                    scanned += 1
        record = {"P": P, "scanned_contexts": scanned, "worst": worst}
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)

    payload = {
        "claim_tested": (
            "The full one-step canonical marked recurrence, including base "
            "energy, is controlled by V_p=(s+K-R)^p[1+log(s-B+1)]."
        ),
        "finite_scope_warning": (
            "A ratio above one refutes the displayed potential. A finite pass "
            "cannot prove the universal inequality."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; reset weight=theta_e^2/[Q_G(e)q_x]; "
            "deep weight is the exact M65 marked stationary coefficient."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            f"python3 -B {Path(__file__)} --p-max {args.p_max} "
            f"--k-scan {args.k_scan} --exponents "
            f"{' '.join(map(str, args.exponents))} --output {args.output}"
        ),
        "parameters": vars(args) | {"output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "deep_mass_identity_max_abs_error": renewal.solver.max_deep_mass_error,
        "global_worst": global_worst,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
