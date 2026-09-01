#!/usr/bin/env python3
"""Exact falsifier for the contextual closed conditional-mean formula.

This script compares every exact contextual conditional mean available
through ambient rank seven with the universal two-chain shuffle formula.
A single mismatch refutes that formula.  Empty finite failure lists do not
prove it; the separate counting argument in closed_mean_formula.md does.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_generator():
    path = HERE / "generator_defect.py"
    spec = importlib.util.spec_from_file_location("m65_generator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


G = load_generator()


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def terminal_coefficient(K, R, k):
    return Fraction(
        K * math.comb(k + K - R - 2, K - R - 1),
        math.comb(k + K - 1, K - 1),
    )


def deep_coefficient(K, R, k):
    return Fraction(1) - Fraction(
        math.comb(K, R + 1), math.comb(K + k, R + 1)
    )


def predicted(K, R, B, comp):
    k = len(comp)
    t = comp[-1]
    if t < B:
        return Fraction()
    if t == B:
        return terminal_coefficient(K, R, k)
    return (
        G.w(t - B)
        * G.w(B)
        / G.w(t)
        * deep_coefficient(K, R, k)
    )


def context_record(ambient_r, context):
    means = G.conditional_means(context)
    K = len(context["coarse"])
    R = K - context["branch_index"] - 1
    B = context["suffix_size"]
    failures = []
    for comp, actual in sorted(means.items()):
        expected = predicted(K, R, B, comp)
        if actual != expected:
            failures.append(
                {
                    "composition": list(comp),
                    "actual": str(actual),
                    "predicted": str(expected),
                }
            )
    return {
        "ambient_r": ambient_r,
        "coarse": list(context["coarse"]),
        "refined": list(context["refined"]),
        "branch_index": context["branch_index"],
        "K": K,
        "R": R,
        "B": B,
        "composition_count": len(means),
        "failure_count": len(failures),
        "failures": failures,
    }


def run(ambient_r):
    contexts, macro_count, raw_count = G.REC.contextual_tables(ambient_r)
    rows = [context_record(ambient_r, context) for context in contexts]
    return {
        "ambient_r": ambient_r,
        "macro_count": macro_count,
        "raw_factorization_count": raw_count,
        "context_count": len(rows),
        "composition_count": sum(row["composition_count"] for row in rows),
        "failure_count": sum(row["failure_count"] for row in rows),
        "failure_rows": [row for row in rows if row["failures"]],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    records = [run(r) for r in range(2, args.r_max + 1)]
    result = {
        "claim_tested": (
            "For every contextual suffix observable, E[phi|C] is exactly "
            "the stated K,R,k,t,B two-chain-shuffle formula."
        ),
        "finite_scope_warning": (
            "One mismatch refutes the universal formula. Empty finite "
            "failure lists prove no universal statement."
        ),
        "formula": {
            "last_less_B": "0",
            "last_equal_B": (
                "K*binom(k+K-R-2,K-R-1)/binom(k+K-1,K-1)"
            ),
            "last_greater_B": (
                "w(t-B)w(B)/w(t) * "
                "[1-binom(K,R+1)/binom(K+k,R+1)]"
            ),
            "w(t)": "t^(t-1)/t!",
        },
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"closed_mean_formula.py --r-max {args.r_max} --output "
            f"{args.output}"
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "ambient_r": row["ambient_r"],
                    "context_count": row["context_count"],
                    "composition_count": row["composition_count"],
                    "failure_count": row["failure_count"],
                }
                for row in records
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
