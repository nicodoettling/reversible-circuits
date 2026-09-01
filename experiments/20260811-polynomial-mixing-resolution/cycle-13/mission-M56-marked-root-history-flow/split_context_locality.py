#!/usr/bin/env python3
"""Exact falsifier for branch-locality of each root-split bias function.

For fixed coarse/refined root compositions, this tests whether the exit
rate depends on a source tree only through the local macro of the branch
being split.  It also compares that contextual local function with the
corresponding unary-root split function.  Finite passes prove neither claim.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def load_m50():
    repo = Path(__file__).resolve().parents[4]
    path = (
        repo
        / "experiments/20260811-polynomial-mixing-resolution"
        / "cycle-12/mission-M50-full-parking-flow"
        / "root_composition_audit.py"
    )
    spec = importlib.util.spec_from_file_location("m50_context", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M50 = load_m50()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def merge_at(comp, index):
    return (
        comp[:index]
        + (comp[index] + comp[index + 1],)
        + comp[index + 2 :]
    )


def instance_rates(r):
    macros, adjacency, capacities, raw_count = M50.exact_instance(r + 1)
    orbit_weight = M50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    return macros, adjacency, rates, raw_count


def unary_tables(r_max):
    tables = {}
    for c in range(2, r_max + 1):
        macros, adjacency, rates, _ = instance_rates(c)
        alpha = Fraction(2, 3 * c * (c - 1))
        table = {}
        for source in macros:
            if M50.root_composition(source) != (c,):
                continue
            interval = M50.root_intervals(source)[0]
            local = M50.local_macro(source, interval)
            for target in adjacency[source]:
                refined = M50.root_composition(target)
                if len(refined) != 2:
                    continue
                key = (local, refined)
                table[key] = table.get(key, Fraction()) + (
                    rates[source, target] / alpha
                )
        tables[c] = table
    return tables


def run(r, unary):
    macros, adjacency, rates, raw_count = instance_rates(r)
    alpha = Fraction(2, 3 * r * (r - 1))
    grouped = defaultdict(set)
    rows = []

    for source in macros:
        coarse = M50.root_composition(source)
        intervals = M50.root_intervals(source)
        exits = defaultdict(Fraction)
        for target in adjacency[source]:
            refined = M50.root_composition(target)
            if len(refined) == len(coarse) + 1:
                exits[refined] += rates[source, target]
        for refined, rate in exits.items():
            indices = [
                index
                for index in range(len(refined) - 1)
                if merge_at(refined, index) == coarse
            ]
            if len(indices) != 1:
                rows.append(
                    {
                        "assignment_failure": True,
                        "source": list(source),
                        "coarse": list(coarse),
                        "refined": list(refined),
                        "indices": indices,
                    }
                )
                continue
            index = indices[0]
            local = M50.local_macro(source, intervals[index])
            normalized = rate / alpha
            grouped[(coarse, refined, index, local)].add(normalized)

    locality_failures = []
    unary_support_failures = []
    ratios = []
    ratio_groups = defaultdict(set)
    for (coarse, refined, index, local), values in sorted(grouped.items()):
        if len(values) != 1:
            locality_failures.append(
                {
                    "coarse": list(coarse),
                    "refined": list(refined),
                    "branch_index": index,
                    "local_macro": list(local),
                    "contextual_values_over_alpha_r": sorted(
                        str(value) for value in values
                    ),
                }
            )
            continue
        contextual = next(iter(values))
        c = coarse[index]
        local_refined = (refined[index], refined[index + 1])
        unary_value = unary[c].get((local, local_refined), Fraction())
        if (contextual == 0) != (unary_value == 0):
            unary_support_failures.append(
                {
                    "coarse": list(coarse),
                    "refined": list(refined),
                    "branch_index": index,
                    "local_macro": list(local),
                    "contextual": str(contextual),
                    "unary": str(unary_value),
                }
            )
        if contextual and unary_value:
            ratio_groups[(coarse, refined, index)].add(
                contextual / unary_value
            )
            ratios.append(
                (
                    contextual / unary_value,
                    coarse,
                    refined,
                    index,
                    local,
                    contextual,
                    unary_value,
                )
            )

    def ratio_row(row):
        if row is None:
            return None
        ratio, coarse, refined, index, local, contextual, unary_value = row
        return {
            "ratio": str(ratio),
            "coarse": list(coarse),
            "refined": list(refined),
            "branch_index": index,
            "local_macro": list(local),
            "contextual_over_alpha_r": str(contextual),
            "unary_over_alpha_c": str(unary_value),
        }

    return {
        "r": r,
        "macro_count": len(macros),
        "raw_factorization_count": raw_count,
        "contextual_group_count": len(grouped),
        "contextual_locality_failures": locality_failures,
        "contextual_vs_unary_support_failures": unary_support_failures,
        "fixed_refinement_scaling_failures": [
            {
                "coarse": list(key[0]),
                "refined": list(key[1]),
                "branch_index": key[2],
                "ratios": sorted(str(value) for value in values),
            }
            for key, values in sorted(ratio_groups.items())
            if len(values) > 1
        ],
        "minimum_positive_context_to_unary_ratio": ratio_row(
            min(ratios) if ratios else None
        ),
        "maximum_context_to_unary_ratio": ratio_row(
            max(ratios) if ratios else None
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    unary = unary_tables(args.r_max)
    result = {
        "claim_tested": (
            "For fixed coarse/refined root compositions, each split exit "
            "rate is a function only of the local macro of the split branch."
        ),
        "finite_scope_warning": (
            "One contextual collision refutes branch locality. Finite passes "
            "cannot prove locality or polynomial ratio bounds."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            f"split_context_locality.py --r-max {args.r_max} --output {args.output}"
        ),
        "records": [run(r, unary) for r in range(2, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
