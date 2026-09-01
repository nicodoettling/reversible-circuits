#!/usr/bin/env python3
"""Exact falsifier for branch-additivity of aggregate root-split rates."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def load_m50():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-12/mission-M50-full-parking-flow"
        / "root_composition_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m50_branch_add", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def split_rates(n: int, m50):
    macros, adjacency, capacities, _ = m50.exact_instance(n)
    orbit_weight = m50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    answer = {}
    for source in macros:
        comp = m50.root_composition(source)
        answer[source] = sum(
            (
                rates[source, target]
                for target in adjacency[source]
                if len(m50.root_composition(target)) == len(comp) + 1
            ),
            Fraction(),
        )
    return macros, answer


def merge_at(comp, p):
    return comp[:p] + (comp[p] + comp[p + 1],) + comp[p + 2 :]


def split_rates_by_branch(n: int, m50):
    macros, adjacency, capacities, _ = m50.exact_instance(n)
    orbit_weight = m50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    answer = {}
    assignment_failures = []
    for source in macros:
        coarse = m50.root_composition(source)
        values = [Fraction() for _ in coarse]
        for target in adjacency[source]:
            refined = m50.root_composition(target)
            if len(refined) != len(coarse) + 1:
                continue
            indices = [
                p
                for p in range(len(refined) - 1)
                if merge_at(refined, p) == coarse
            ]
            if len(indices) != 1:
                assignment_failures.append(
                    {
                        "source": list(source),
                        "target": list(target),
                        "coarse": list(coarse),
                        "refined": list(refined),
                        "candidate_indices": indices,
                    }
                )
                continue
            values[indices[0]] += rates[source, target]
        answer[source] = tuple(values)
    return macros, answer, assignment_failures


def phi_tables(r_max: int, m50):
    """phi_s(u)=p_unary(u)/alpha_(s+1), with phi_0=0."""
    tables = {0: {(): Fraction()}}
    failures = []
    for s in range(1, r_max):
        total_r = s + 1
        macros, p_split = split_rates(total_r + 1, m50)
        alpha = Fraction(2, 3 * total_r * (total_r - 1))
        table = {}
        for macro in macros:
            if m50.root_composition(macro) != (total_r,):
                continue
            intervals = m50.root_intervals(macro)
            if len(intervals) != 1:
                raise AssertionError("unary root has non-unary intervals")
            local = m50.local_macro(macro, intervals[0])
            value = p_split[macro] / alpha
            if local in table and table[local] != value:
                failures.append(
                    {
                        "s": s,
                        "local_macro": list(local),
                        "first": str(table[local]),
                        "second": str(value),
                    }
                )
            table[local] = value
        tables[s] = table
    return tables, failures


def run(r: int, m50, phi) -> dict:
    macros, p_split = split_rates(r + 1, m50)
    _, p_by_branch, assignment_failures = split_rates_by_branch(r + 1, m50)
    alpha = Fraction(2, 3 * r * (r - 1))
    failures = []
    max_phi = Fraction()
    max_row = None
    locality_values = defaultdict(set)
    scaling_values = defaultdict(set)
    for macro in sorted(macros):
        local_rows = []
        predicted_scaled = Fraction()
        comp = m50.root_composition(macro)
        for branch_index, interval in enumerate(m50.root_intervals(macro)):
            local = m50.local_macro(macro, interval)
            s = len(local)
            value = phi[s][local] if s else Fraction()
            observed_branch = p_by_branch[macro][branch_index] / alpha
            locality_values[(comp, branch_index, local)].add(observed_branch)
            if value:
                scaling_values[(comp, branch_index)].add(
                    observed_branch / value
                )
            local_rows.append(
                {
                    "branch_index": branch_index,
                    "s": s,
                    "local_macro": list(local),
                    "phi": str(value),
                    "observed_branch_p_over_alpha": str(observed_branch),
                }
            )
            predicted_scaled += value
        observed_scaled = p_split[macro] / alpha
        if observed_scaled != predicted_scaled:
            failures.append(
                {
                    "macro": list(macro),
                    "composition": list(m50.root_composition(macro)),
                    "observed_p_over_alpha": str(observed_scaled),
                    "predicted_sum_phi": str(predicted_scaled),
                    "branches": local_rows,
                }
            )
        if observed_scaled > max_phi:
            max_phi = observed_scaled
            max_row = {
                "macro": list(macro),
                "composition": list(m50.root_composition(macro)),
                "p_over_alpha": str(observed_scaled),
                "branches": local_rows,
            }
    return {
        "r": r,
        "macro_count": len(macros),
        "branch_additivity_failures": failures,
        "split_branch_assignment_failures": assignment_failures,
        "contextual_locality_failures": [
            {
                "composition": list(key[0]),
                "branch_index": key[1],
                "local_macro": list(key[2]),
                "values": sorted(str(x) for x in values),
            }
            for key, values in locality_values.items()
            if len(values) > 1
        ],
        "unary_scaling_failures_within_context": [
            {
                "composition": list(key[0]),
                "branch_index": key[1],
                "ratios": sorted(str(x) for x in values),
            }
            for key, values in scaling_values.items()
            if len(values) > 1
        ],
        "context_scalings": [
            {
                "composition": list(key[0]),
                "branch_index": key[1],
                "ratio_to_unary_phi": str(next(iter(values))),
            }
            for key, values in sorted(scaling_values.items())
            if len(values) == 1
        ],
        "maximum_p_over_alpha": str(max_phi),
        "maximum_row": max_row,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    m50 = load_m50()
    phi, unary_failures = phi_tables(args.r_max, m50)
    result = {
        "claim_tested": (
            "Aggregate root-split propensity is alpha_r times a sum of "
            "unary-root branch functionals phi_s(local subtree)."
        ),
        "universal_scope": (
            "A failure refutes the branch-additive formula.  Finite passes "
            "do not prove its proposed universal interleaving argument."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-12/mission-M54-root-mean-lift-referee/"
            "branch_split_additivity.py "
            f"--r-max {args.r_max} --output {args.output}"
        ),
        "unary_table_failures": unary_failures,
        "phi_tables": {
            str(s): {str(list(m)): str(value) for m, value in table.items()}
            for s, table in phi.items()
        },
        "records": [run(r, m50, phi) for r in range(2, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
