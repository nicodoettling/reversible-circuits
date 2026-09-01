#!/usr/bin/env python3
"""Finite exact-mark resolvent for M56/M65's separated-capacity recurrence.

For a contextual type x=(s,K,R,B), compute T(x)=a(x)+sum_y W(x,y)T(y).
Every child has smaller local rank. Deep weights retain the exact
negative-hypergeometric mark, and quotient residuals retain the external
mark determined by the split edge.

This is a numerical falsifier/calibration of the marked separated-capacity
recurrence. It is not an actual-edge source-recovery proof.
"""

from __future__ import annotations

import argparse
import functools
import json
import math
import platform
import subprocess
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import scipy

import weighted_green_probe as base


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def negative_hypergeometric(K: int, R: int, k: int, j: int) -> float:
    return float(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j)
        / math.comb(K + k, k)
    )


class Resolvent:
    def __init__(self, s_max: int, rtol: float, maxiter: int):
        self.rank_data = {}
        self.max_deep_mass_error = 0.0
        self.contexts_evaluated = 0
        for s in range(2, s_max + 1):
            (
                comps,
                rho,
                laplacian,
                keys,
                groups,
                merge_edges,
            ) = base.build_rank(s)
            masses, basis, residual, iterations = base.solve_group_basis(
                rho, laplacian, keys, groups, rtol, maxiter
            )
            self.rank_data[s] = {
                "comps": comps,
                "rho": rho,
                "keys": keys,
                "masses": masses,
                "basis": basis,
                "merge_edges": merge_edges,
                "cg_residual": residual,
                "cg_iterations": iterations,
            }

    def transitions(self, s: int, K: int, R: int, B: int):
        data = self.rank_data[s]
        rho = data["rho"]
        keys = data["keys"]
        masses = data["masses"]
        values = base.contextual_values(keys, K, R, B)
        mean = float(np.dot(masses, values))
        potential = (data["basis"] @ values) / np.sqrt(rho)
        children = defaultdict(float)
        quotient_energy = 0.0

        for (
            i,
            j,
            capacity,
            child_rank,
            left,
            right,
            child_K,
            child_R,
        ) in data["merge_edges"]:
            energy = capacity * (potential[i] - potential[j]) ** 2
            quotient_energy += energy
            if child_rank >= 2:
                children[
                    (child_rank, child_K, child_R, right)
                ] += energy / mean

        deep_weight = 0.0
        terminal = 0.0
        for index, (k, last) in enumerate(keys):
            group_mass = masses[index]
            if last == B:
                terminal += group_mass * values[index]
            if last <= B:
                continue
            child_rank = last - 1
            child_mean = base.w_ratio(last - B, B)
            for mark_j in range(1, k + 1):
                nu = negative_hypergeometric(K, R, k, mark_j)
                weight = group_mass * child_mean * nu / mean
                deep_weight += weight
                if child_rank >= 2:
                    children[
                        (child_rank, K + k, R + mark_j, B)
                    ] += weight

        delta = (mean - terminal) / mean
        a = quotient_energy / mean
        self.max_deep_mass_error = max(
            self.max_deep_mass_error, abs(deep_weight - delta)
        )
        return a, delta, deep_weight, dict(children)

    @functools.lru_cache(maxsize=None)
    def value(self, s: int, K: int, R: int, B: int) -> float:
        if s <= 1:
            return 0.0
        if not (1 <= B <= s and 1 <= K and 0 <= R < K):
            raise ValueError((s, K, R, B))
        self.contexts_evaluated += 1
        a, _, _, children = self.transitions(s, K, R, B)
        result = a
        for child, weight in children.items():
            result += weight * self.value(*child)
        return result


def context_grid(s: int, K_max: int):
    k_values = list(range(1, K_max + 1))
    for extra in (64, 128, 256, 1024, 4096):
        if extra > K_max:
            k_values.append(extra)
    for K in k_values:
        if K <= 32:
            r_values = range(K)
        else:
            r_values = sorted(
                {
                    0,
                    1 if K > 1 else 0,
                    K // 4,
                    K // 2,
                    (3 * K) // 4,
                    K - 2 if K > 1 else 0,
                    K - 1,
                }
            )
        for R in r_values:
            for B in range(1, s + 1):
                yield K, R, B


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=9)
    parser.add_argument("--K-max", type=int, default=32)
    parser.add_argument("--rtol", type=float, default=1e-11)
    parser.add_argument("--maxiter", type=int, default=20000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 14:
        raise SystemExit("bounded range is 2 <= s-max <= 14")
    if args.K_max < 1:
        raise SystemExit("K-max must be positive")

    started = time.time()
    solver = Resolvent(args.s_max, args.rtol, args.maxiter)
    records = []
    for s in range(2, args.s_max + 1):
        worst = None
        count = 0
        for K, R, B in context_grid(s, args.K_max):
            value = solver.value(s, K, R, B)
            a, delta, deep_weight, children = solver.transitions(
                s, K, R, B
            )
            row = {
                "s": s,
                "K": K,
                "R": R,
                "B": B,
                "resolvent_value": value,
                "base_green_cost": a,
                "deep_fraction": delta,
                "deep_transfer_weight": deep_weight,
                "total_child_weight": sum(children.values()),
                "child_context_count": len(children),
            }
            if worst is None or value > worst["resolvent_value"]:
                worst = row
            count += 1
        record = {
            "s": s,
            "scanned_context_count": count,
            "memoized_context_count": solver.contexts_evaluated,
            "worst": worst,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)

    result = {
        "claim_tested": (
            "The exact marked, child-rank-resolved separated-capacity "
            "recurrence has polynomial Green resolvent."
        ),
        "finite_scope_warning": (
            "Finite growth can falsify a proposed envelope but cannot prove "
            "a universal polynomial bound. This recurrence still duplicates "
            "capacity across histories and is not an actual unmarked flow."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; a=edge-resolved quotient Green energy/mean; "
            "deep weights use stationary group mass times exact "
            "negative-hypergeometric nu_j times child mean / parent mean."
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
            f"marked_resolvent_probe.py --s-max {args.s_max} "
            f"--K-max {args.K_max} --rtol {args.rtol} "
            f"--maxiter {args.maxiter} --output {args.output}"
        ),
        "parameters": {
            "s_max": args.s_max,
            "K_max": args.K_max,
            "rtol": args.rtol,
            "maxiter": args.maxiter,
            "output": str(args.output),
        },
        "rank_linear_solve_diagnostics": {
            str(s): {
                "cg_max_relative_residual": data["cg_residual"],
                "cg_max_iterations": data["cg_iterations"],
            }
            for s, data in solver.rank_data.items()
        },
        "transition_audit_max_abs_error": solver.max_deep_mass_error,
        "total_memoized_contexts": solver.contexts_evaluated,
        "elapsed_seconds": time.time() - started,
        "records": records,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
