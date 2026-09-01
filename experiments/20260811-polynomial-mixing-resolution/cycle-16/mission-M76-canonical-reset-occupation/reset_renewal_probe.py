#!/usr/bin/env python3
"""Finite reset-to-reset renewal diagnostics for M71's canonical flow.

This script eliminates pure-deep transitions exactly on the rank DAG:

    b = (I-D)^(-1) a,       Kreset = (I-D)^(-1) Jcan.

Every target of Kreset is right-heavy.  The output tests polynomial
potentials but is only a finite falsifier, never an asymptotic proof.
"""

from __future__ import annotations

import argparse
import functools
import json
import platform
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
M71 = HERE.parents[1] / "cycle-15" / "mission-M71-marked-weighted-green-contraction"
sys.path.insert(0, str(M71))

import weighted_green_probe as base  # noqa: E402
from canonical_marked_probe import CanonicalResolvent  # noqa: E402
from marked_resolvent_probe import (  # noqa: E402
    context_grid,
    negative_hypergeometric,
)


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


class Renewal:
    def __init__(self, s_max: int):
        self.solver = CanonicalResolvent(s_max)

    @functools.lru_cache(maxsize=None)
    def split(self, s: int, K: int, R: int, B: int):
        data = self.solver.rank_data[s]
        rho = data["rho"]
        keys = data["keys"]
        masses = data["masses"]
        values = base.contextual_values(keys, K, R, B)
        mean = float(np.dot(masses, values))
        value_by_state = np.empty(len(rho))
        for key_index, key in enumerate(keys):
            value_by_state[data["groups"][key]] = values[key_index]
        charge = rho * (value_by_state - mean)

        quotient = defaultdict(float)
        quotient_rows = []
        a = 0.0
        for edge, basin in data["canonical_edges"]:
            (
                _,
                _,
                capacity,
                child_rank,
                left,
                right,
                child_K,
                child_R,
            ) = edge
            current = float(sum(charge[index] for index in basin))
            energy = current * current / capacity / mean
            a += energy
            quotient_rows.append(
                {
                    "weight": energy,
                    "child_rank": child_rank,
                    "child_K": child_K,
                    "child_R": child_R,
                    "child_B": right,
                    "child_budget": child_rank + child_K,
                    "child_excess_plus_one": left,
                }
            )
            if child_rank >= 2:
                quotient[(child_rank, child_K, child_R, right)] += energy

        deep = defaultdict(float)
        for index, (k, last) in enumerate(keys):
            if last <= B:
                continue
            child_rank = last - 1
            child_mean = base.w_ratio(last - B, B)
            for mark_j in range(1, k + 1):
                weight = (
                    masses[index]
                    * child_mean
                    * negative_hypergeometric(K, R, k, mark_j)
                    / mean
                )
                if child_rank >= 2:
                    deep[(child_rank, K + k, R + mark_j, B)] += weight
        return a, dict(deep), dict(quotient), quotient_rows

    @functools.lru_cache(maxsize=None)
    def eliminated(self, s: int, K: int, R: int, B: int):
        if s <= 1:
            return 0.0, {}
        a, deep, quotient, _ = self.split(s, K, R, B)
        base_cost = a
        resets = defaultdict(float)
        for child, weight in quotient.items():
            resets[child] += weight
        for child, weight in deep.items():
            child_base, child_resets = self.eliminated(*child)
            base_cost += weight * child_base
            for reset_child, reset_weight in child_resets.items():
                resets[reset_child] += weight * reset_weight
        return base_cost, dict(resets)


def potential(context, exponent: int, excess_power: int) -> float:
    s, K, _, B = context
    return float((s + K) ** exponent * (s - B + 1) ** excess_power)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=12)
    parser.add_argument("--K-max", type=int, default=8)
    parser.add_argument("--exponents", type=int, nargs="+", default=[1, 2, 3, 4])
    parser.add_argument("--excess-powers", type=int, nargs="+", default=[0, 1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.s_max <= 14:
        raise SystemExit("bounded range is 2 <= s-max <= 14")

    started = time.time()
    renewal = Renewal(args.s_max)
    records = []
    for s in range(2, args.s_max + 1):
        worst = {
            f"N^{p}L^{q}": None
            for p in args.exponents
            for q in args.excess_powers
        }
        worst_row_sum = None
        worst_base = None
        count = 0
        for K, R, B in context_grid(s, args.K_max):
            if R != K - 1:
                continue
            context = (s, K, R, B)
            base_cost, resets = renewal.eliminated(*context)
            row_sum = sum(resets.values())
            row = {
                "s": s,
                "K": K,
                "R": R,
                "B": B,
                "pure_deep_base": base_cost,
                "renewal_row_sum": row_sum,
                "reset_target_count": len(resets),
            }
            if worst_row_sum is None or row_sum > worst_row_sum["renewal_row_sum"]:
                worst_row_sum = row
            if worst_base is None or base_cost > worst_base["pure_deep_base"]:
                worst_base = row
            for p in args.exponents:
                for q in args.excess_powers:
                    label = f"N^{p}L^{q}"
                    parent = potential(context, p, q)
                    demand = base_cost + sum(
                        weight * potential(child, p, q)
                        for child, weight in resets.items()
                    )
                    ratio = demand / parent
                    candidate = dict(row)
                    candidate["potential_ratio"] = ratio
                    if worst[label] is None or ratio > worst[label]["potential_ratio"]:
                        worst[label] = candidate
            count += 1
        record = {
            "s": s,
            "scanned_right_heavy_context_count": count,
            "worst_renewal_row_sum": worst_row_sum,
            "worst_pure_deep_base": worst_base,
            "worst_potential_ratios": worst,
        }
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)

    payload = {
        "claim_tested": (
            "After exact pure-deep elimination, a polynomial ambient-budget "
            "potential controls the right-heavy canonical reset renewal."
        ),
        "finite_scope_warning": (
            "A ratio above one refutes that tested potential. Ratios below "
            "one at finite ranks prove no universal occupation bound."
        ),
        "normalization": (
            "G_s=R_s/alpha_s; Jcan edge weight is theta_e^2/[Q_G(e)q]; "
            "D is M65's exact marked deep kernel."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "command": (
            "python3 -B "
            f"{Path(__file__)} --s-max {args.s_max} --K-max {args.K_max} "
            f"--exponents {' '.join(map(str, args.exponents))} "
            f"--excess-powers {' '.join(map(str, args.excess_powers))} "
            f"--output {args.output}"
        ),
        "parameters": vars(args) | {"output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "deep_mass_identity_max_abs_error": renewal.solver.max_deep_mass_error,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
