#!/usr/bin/env python3
"""Finite dynamic-LP discovery for positive potentials on the marked DAG.

For fixed c,C and lambda_s=1-c/s^C, the pointwise-minimal solution of

    W_x >= 1,
    a_x + sum_y w_xy W_y <= lambda_s W_x

is computed exactly on the rank-acyclic finite context closure.  This is the
dynamic-programming solution of the corresponding LP.  It is a finite
certificate-discovery aid, not a universal proof.
"""

from __future__ import annotations

import argparse
import functools
import json
import platform
import subprocess
import time
from pathlib import Path

import numpy as np
import scipy

from marked_resolvent_probe import Resolvent, context_grid


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


class Certificate:
    def __init__(self, solver: Resolvent, constant: float, exponent: float):
        self.solver = solver
        self.constant = constant
        self.exponent = exponent

    @functools.lru_cache(maxsize=None)
    def value(self, s: int, K: int, R: int, B: int) -> float:
        if s <= 1:
            return 1.0
        contraction = 1.0 - self.constant / (s**self.exponent)
        if contraction <= 0:
            return float("inf")
        a, _, _, children = self.solver.transitions(s, K, R, B)
        demand = a + sum(
            weight * self.value(*child)
            for child, weight in children.items()
        )
        return max(1.0, demand / contraction)

    def slack(self, context) -> float:
        s, K, R, B = context
        contraction = 1.0 - self.constant / (s**self.exponent)
        a, _, _, children = self.solver.transitions(*context)
        return (
            contraction * self.value(*context)
            - a
            - sum(
                weight * self.value(*child)
                for child, weight in children.items()
            )
        )


def parse_pair(text: str) -> tuple[float, float]:
    left, right = text.split(",", 1)
    return float(left), float(right)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=10)
    parser.add_argument("--K-max", type=int, default=16)
    parser.add_argument(
        "--certificate",
        action="append",
        type=parse_pair,
        default=[],
        help="c,C for lambda_s=1-c/s^C; may be repeated",
    )
    parser.add_argument("--rtol", type=float, default=1e-11)
    parser.add_argument("--maxiter", type=int, default=20000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.certificate:
        args.certificate = [
            (0.25, 1.0),
            (0.5, 1.0),
            (0.75, 1.0),
            (1.0, 1.0),
            (0.5, 2.0),
        ]
    if not 2 <= args.s_max <= 14:
        raise SystemExit("bounded range is 2 <= s-max <= 14")

    started = time.time()
    solver = Resolvent(args.s_max, args.rtol, args.maxiter)
    records = []
    for constant, exponent in args.certificate:
        certificate = Certificate(solver, constant, exponent)
        by_rank = []
        global_worst = None
        min_slack = float("inf")
        for s in range(2, args.s_max + 1):
            worst = None
            count = 0
            for K, R, B in context_grid(s, args.K_max):
                context = (s, K, R, B)
                value = certificate.value(*context)
                slack = certificate.slack(context)
                min_slack = min(min_slack, slack)
                row = {
                    "s": s,
                    "K": K,
                    "R": R,
                    "B": B,
                    "W": value,
                    "constraint_slack": slack,
                    "suffix_fraction": B / s,
                    "suffix_excess": s - B,
                    "unpassed_attachment_fraction": (K - R) / (K + s),
                }
                if worst is None or value > worst["W"]:
                    worst = row
                if global_worst is None or value > global_worst["W"]:
                    global_worst = row
                count += 1
            by_rank.append(
                {
                    "s": s,
                    "scanned_context_count": count,
                    "worst": worst,
                }
            )
        record = {
            "constant_c": constant,
            "exponent_C": exponent,
            "global_worst": global_worst,
            "minimum_constraint_slack": min_slack,
            "memoized_contexts": certificate.value.cache_info().currsize,
            "by_rank": by_rank,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)

    result = {
        "claim_tested": (
            "There is a bounded positive marked-context potential W with "
            "a_x+sum_y w_xy W_y <=(1-c/s^C)W_x."
        ),
        "finite_scope_warning": (
            "The dynamic program solves only the finite scanned context "
            "closure. A bounded finite W neither proves a universal formula "
            "nor solves actual-edge history collisions."
        ),
        "normalization": (
            "The child weights and base costs are the exact normalized "
            "marked separated-capacity recurrence from marked_resolvent_probe."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-15/mission-M71-marked-weighted-green-contraction/"
            f"lyapunov_certificate_probe.py --s-max {args.s_max} "
            f"--K-max {args.K_max} "
            + " ".join(
                f"--certificate {constant},{exponent}"
                for constant, exponent in args.certificate
            )
            + f" --rtol {args.rtol} --maxiter {args.maxiter} "
            f"--output {args.output}"
        ),
        "parameters": {
            "s_max": args.s_max,
            "K_max": args.K_max,
            "certificates": args.certificate,
            "rtol": args.rtol,
            "maxiter": args.maxiter,
            "output": str(args.output),
        },
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
