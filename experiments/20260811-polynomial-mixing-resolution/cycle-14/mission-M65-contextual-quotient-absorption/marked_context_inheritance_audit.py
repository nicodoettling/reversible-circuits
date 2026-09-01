#!/usr/bin/env python3
"""Exact falsifier for accumulated-attachment marked inheritance.

For a deep (K,R) context with k current inner attachments, let J be the
number of inner attachments before the active outer attachment in their
uniform two-chain shuffle.  The claimed exact recursion is a mixture over
J=j>=1 of synthetic child contexts (K+k,R+j).  This script checks every
instance whose parent and synthetic child ambient ranks are at most seven.
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
M50 = G.M50


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def singleton(values):
    if len(values) != 1:
        raise AssertionError(f"contextual collision: {values}")
    return next(iter(values))


def j_probability(K, R, k, j):
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


def context_key(context):
    return (
        tuple(context["coarse"]),
        context["branch_index"],
        context["suffix_size"],
    )


def synthetic_key(t, B, K_new, R_new):
    left = K_new - R_new - 1
    coarse = (1,) * left + (t,) + (1,) * R_new
    return coarse, left, B


def run(parent_r, tables, lookups, r_max):
    failures = []
    checks = 0
    skipped_too_large = 0
    for parent in tables[parent_r]:
        K = len(parent["coarse"])
        R = K - parent["branch_index"] - 1
        B = parent["suffix_size"]
        for local, values in parent["values_by_local"].items():
            comp = M50.root_composition(local)
            k = len(comp)
            t = comp[-1]
            if t <= B:
                continue
            last_local = M50.local_macro(local, M50.root_intervals(local)[-1])
            K_new = K + k
            synthetic_r = t + K_new - 1
            if synthetic_r > r_max:
                skipped_too_large += 1
                continue
            expected = Fraction()
            missing = []
            terms = []
            for j in range(1, k + 1):
                R_new = R + j
                key = synthetic_key(t, B, K_new, R_new)
                child = lookups[synthetic_r].get(key)
                if child is None or last_local not in child["values_by_local"]:
                    missing.append(
                        {
                            "j": j,
                            "synthetic_r": synthetic_r,
                            "key": [list(key[0]), key[1], key[2]],
                        }
                    )
                    continue
                probability = j_probability(K, R, k, j)
                child_value = singleton(child["values_by_local"][last_local])
                expected += probability * child_value
                terms.append(
                    {
                        "j": j,
                        "probability": str(probability),
                        "K_new": K_new,
                        "R_new": R_new,
                        "child_value": str(child_value),
                    }
                )
            actual = singleton(values)
            checks += 1
            if missing or actual != expected:
                failures.append(
                    {
                        "parent_coarse": list(parent["coarse"]),
                        "parent_refined": list(parent["refined"]),
                        "inner_composition": list(comp),
                        "last_local": list(last_local),
                        "K": K,
                        "R": R,
                        "k": k,
                        "actual": str(actual),
                        "expected": str(expected),
                        "terms": terms,
                        "missing": missing,
                    }
                )
    return {
        "ambient_r": parent_r,
        "check_count": checks,
        "skipped_synthetic_rank_too_large": skipped_too_large,
        "failure_count": len(failures),
        "failures": failures,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    tables = {
        r: G.REC.contextual_tables(r)[0] for r in range(2, args.r_max + 1)
    }
    lookups = {
        r: {context_key(row): row for row in rows}
        for r, rows in tables.items()
    }
    records = [
        run(r, tables, lookups, args.r_max) for r in range(2, args.r_max + 1)
    ]
    result = {
        "claim_tested": (
            "A deep (K,R) contextual statistic is the exact "
            "negative-hypergeometric mixture over synthetic child contexts "
            "(K+k,R+j), 1<=j<=k."
        ),
        "finite_scope_warning": (
            "One mismatch refutes the marked inheritance formula. Empty "
            "finite failure lists do not prove it."
        ),
        "j_probability": (
            "binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k)"
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"marked_context_inheritance_audit.py --r-max {args.r_max} "
            f"--output {args.output}"
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "ambient_r": row["ambient_r"],
                    "check_count": row["check_count"],
                    "skipped": row["skipped_synthetic_rank_too_large"],
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
