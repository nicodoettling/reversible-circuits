#!/usr/bin/env python3
"""Exact falsifier for the deep contextual parameter map.

The proposed universal recursion says that a deep suffix statistic in an
outer (K,R) context is D_{K,R}(k) times the contextual statistic on the
last inner branch with new context (K',R')=(k,0).  This bounded audit can
refute, but cannot prove, that marked-shuffle identity.
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


def scalar(K, R, k):
    return Fraction(1) - Fraction(
        math.comb(K, R + 1), math.comb(K + k, R + 1)
    )


def singleton(values):
    if len(values) != 1:
        raise AssertionError(f"contextual collision: {values}")
    return next(iter(values))


def context_key(context):
    return (
        tuple(context["coarse"]),
        context["branch_index"],
        context["suffix_size"],
    )


def run(r, tables):
    contexts = tables[r]
    failures = []
    checks = 0
    for parent in contexts:
        K = len(parent["coarse"])
        R = K - parent["branch_index"] - 1
        B = parent["suffix_size"]
        s = parent["branch_size"] - 1
        if s < 2:
            continue
        child_lookup = {context_key(row): row for row in tables[s]}
        for local, values in parent["values_by_local"].items():
            comp = M50.root_composition(local)
            k = len(comp)
            t = comp[-1]
            if t <= B:
                continue
            child_key = (comp, k - 1, B)
            child = child_lookup.get(child_key)
            if child is None:
                failures.append(
                    {
                        "kind": "missing_child_context",
                        "parent_coarse": list(parent["coarse"]),
                        "parent_refined": list(parent["refined"]),
                        "inner_composition": list(comp),
                        "child_key": [list(comp), k - 1, B],
                    }
                )
                continue
            interval = M50.root_intervals(local)[-1]
            last_local = M50.local_macro(local, interval)
            if last_local not in child["values_by_local"]:
                failures.append(
                    {
                        "kind": "missing_child_local_macro",
                        "inner_composition": list(comp),
                        "last_local": list(last_local),
                    }
                )
                continue
            actual = singleton(values)
            child_value = singleton(child["values_by_local"][last_local])
            expected = scalar(K, R, k) * child_value
            checks += 1
            if actual != expected:
                failures.append(
                    {
                        "kind": "value_mismatch",
                        "parent_coarse": list(parent["coarse"]),
                        "parent_refined": list(parent["refined"]),
                        "inner_composition": list(comp),
                        "last_local": list(last_local),
                        "K": K,
                        "R": R,
                        "k": k,
                        "actual": str(actual),
                        "child_value": str(child_value),
                        "scalar": str(scalar(K, R, k)),
                        "expected": str(expected),
                    }
                )
    return {"ambient_r": r, "check_count": checks, "failures": failures}


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
    records = [run(r, tables) for r in range(2, args.r_max + 1)]
    result = {
        "claim_tested": (
            "Every deep (K,R) contextual statistic equals D_{K,R}(k) "
            "times its last-branch child statistic, whose new external "
            "parameters are (k,0)."
        ),
        "finite_scope_warning": (
            "One mismatch refutes the exact context map. Empty finite "
            "failure lists do not prove it."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-14/mission-M65-contextual-quotient-absorption/"
            f"context_map_audit.py --r-max {args.r_max} --output "
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
                    "check_count": row["check_count"],
                    "failure_count": len(row["failures"]),
                }
                for row in records
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
