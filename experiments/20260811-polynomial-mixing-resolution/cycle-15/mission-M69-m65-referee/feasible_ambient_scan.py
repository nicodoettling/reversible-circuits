#!/usr/bin/env python3
"""Numerically exhaust contextual absorption parameters below ambient 16.

The exact rank-two failure at ambient 16 is proved algebraically elsewhere.
This finite sparse solve checks that no earlier feasible parameter tuple was
missed.  It imports the frozen quotient builder after its source was audited;
therefore this is an independent rerun, not code-independent verification.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SOURCE = (
    REPO
    / "experiments/20260811-polynomial-mixing-resolution"
    / "cycle-14/mission-M65-contextual-quotient-absorption"
    / "absorption_scan.py"
)


def load_source():
    spec = importlib.util.spec_from_file_location("m69_absorption_source", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--rtol", type=float, default=1e-12)
    parser.add_argument("--maxiter", type=int, default=50000)
    args = parser.parse_args()
    source = load_source()
    best = None
    failures = []
    rank_rows = []
    context_count = 0
    for s in range(2, 15):
        comps, rho, laplacian, keys, groups, asymmetry = source.build_rank(s)
        masses, green, residual, iterations = source.compressed_green(
            rho, laplacian, keys, groups, args.rtol, args.maxiter
        )
        rank_best = None
        for K in range(1, 16 - s):
            for R in range(K):
                for B in range(1, s + 1):
                    values = source.contextual_values(keys, K, R, B)
                    terminal = float(sum(
                        masses[j] * values[j]
                        for j, (_, t) in enumerate(keys)
                        if t == B
                    ))
                    energy = float(values @ green @ values)
                    ratio = energy / terminal if terminal > 0 else 0.0
                    row = {
                        "ambient_r": s + K,
                        "s": s,
                        "K": K,
                        "R": R,
                        "B": B,
                        "ratio": ratio,
                    }
                    if best is None or ratio > best["ratio"]:
                        best = row
                    if rank_best is None or ratio > rank_best["ratio"]:
                        rank_best = row
                    if ratio > 1.0 + 1e-8:
                        failures.append(row)
                    context_count += 1
        rank_rows.append({
            "s": s,
            "state_count": len(comps),
            "laplacian_max_asymmetry": asymmetry,
            "cg_max_relative_residual": residual,
            "cg_max_iterations": iterations,
            "best": rank_best,
        })
    result = {
        "claim_tested": "No feasible contextual absorption failure has ambient r<16",
        "finite_numerical_warning": (
            "This exhaustive finite solve is numerical. The exact exhibited "
            "rank-two failure at r=16 is certified separately."
        ),
        "source": str(SOURCE.relative_to(REPO)),
        "context_count": context_count,
        "failure_count": len(failures),
        "failures": failures,
        "best_below_16": best,
        "rank_rows": rank_rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "context_count": context_count,
        "failure_count": len(failures),
        "best_below_16": best,
        "max_cg_residual": max(row["cg_max_relative_residual"] for row in rank_rows),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
