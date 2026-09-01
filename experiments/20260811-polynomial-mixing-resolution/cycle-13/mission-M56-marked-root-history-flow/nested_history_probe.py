#!/usr/bin/env python3
"""Exact bounded audit of the nested first-split history partition function.

Finite agreement can falsify the displayed identities or candidate bounds.
It cannot prove their universal versions.  Run with Python -B so imports do
not leave bytecode caches in the research artifact directory.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


def load_marked_audit():
    path = Path(__file__).with_name("marked_history_audit.py")
    spec = importlib.util.spec_from_file_location("m56_marked", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M56 = load_marked_audit()
M50 = M56.M50


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def root_degree(macro) -> int:
    return len(M50.root_composition(macro))


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def layer_probability(r: int, k: int) -> Fraction:
    return Fraction(
        math.comb(r - 1, k - 1) * r ** (r - k),
        (r + 1) ** (r - 1),
    )


def run(n: int) -> dict:
    r = n - 1
    macros, adjacency, capacities, raw_count = M50.exact_instance(n)
    orbit_weight = M50.M41.BASE.orbit_weight
    rates = {
        edge: capacity / orbit_weight(edge[0])
        for edge, capacity in capacities.items()
    }
    alpha = Fraction(2, 3 * r * (r - 1))

    refinements = {}
    for coarse in macros:
        coarse_comp = M50.root_composition(coarse)
        rows = []
        for refined in adjacency[coarse]:
            refined_comp = M50.root_composition(refined)
            if len(refined_comp) != len(coarse_comp) + 1:
                continue
            if refined_comp[2:] != coarse_comp[1:]:
                continue
            if refined_comp[0] + refined_comp[1] != coarse_comp[0]:
                continue
            rows.append(
                (
                    refined,
                    Fraction(rates[coarse, refined], alpha),
                    refined_comp,
                )
            )
        refinements[coarse] = rows

    @lru_cache(maxsize=None)
    def history_weight(coarse, steps: int) -> Fraction:
        if steps == 0:
            return Fraction(1)
        return sum(
            (
                weight * history_weight(refined, steps - 1)
                for refined, weight, _ in refinements[coarse]
            ),
            Fraction(),
        )

    unary = [macro for macro in macros if root_degree(macro) == 1]
    unary_mass = sum((orbit_weight(macro) for macro in unary), 0)
    pi_unary = {
        macro: Fraction(orbit_weight(macro), unary_mass) for macro in unary
    }

    p1 = layer_probability(r, 1)
    endpoint = M56.endpoint_coalescence(
        macros, raw_count, rates, orbit_weight, alpha, False
    )

    endpoint_failures = []
    moment_failures = []
    endpoint_rows = []
    for macro in unary:
        partition = sum(
            (
                Fraction(history_weight(macro, steps), math.factorial(steps + 1))
                for steps in range(r)
            ),
            Fraction(),
        )
        predicted_density = p1 * partition
        observed_density = endpoint[macro] / pi_unary[macro]
        if predicted_density != observed_density:
            endpoint_failures.append(
                {
                    "macro": list(macro),
                    "predicted": str(predicted_density),
                    "observed": str(observed_density),
                }
            )
        endpoint_rows.append(
            {
                "macro": list(macro),
                "density": str(observed_density),
                "partition": str(partition),
            }
        )

    moment_rows = []
    for steps in range(r):
        observed = sum(
            (
                pi_unary[macro] * history_weight(macro, steps)
                for macro in unary
            ),
            Fraction(),
        )
        expected = (
            Fraction(math.factorial(steps + 1))
            * layer_probability(r, steps + 1)
            / p1
        )
        if observed != expected:
            moment_failures.append(
                {
                    "steps": steps,
                    "observed": str(observed),
                    "expected": str(expected),
                }
            )
        moment_rows.append(
            {
                "steps": steps,
                "observed": str(observed),
                "expected": str(expected),
            }
        )

    individual = []
    propensity = []
    for macro in macros:
        comp = M50.root_composition(macro)
        total = sum((row[1] for row in refinements[macro]), Fraction())
        if refinements[macro]:
            local_max = max(row[1] for row in refinements[macro])
            individual.append((local_max, macro, refinements[macro]))
        propensity.append(
            (
                total,
                macro,
                comp,
                harmonic(comp[0]),
                harmonic(r),
            )
        )

    max_individual = max(individual, default=(Fraction(), None, []))
    max_propensity = max(propensity)
    first_local_harmonic_failure = next(
        (
            row for row in sorted(propensity, key=lambda row: row[1])
            if row[0] > row[3]
        ),
        None,
    )
    first_unary_global_harmonic_failure = next(
        (
            row for row in sorted(propensity, key=lambda row: row[1])
            if root_degree(row[1]) == 1 and row[0] > row[4]
        ),
        None,
    )

    def propensity_row(row):
        if row is None:
            return None
        total, macro, comp, local_h, global_h = row
        return {
            "macro": list(macro),
            "composition": list(comp),
            "total_rate_over_alpha": str(total),
            "H_first_branch_size": str(local_h),
            "H_r": str(global_h),
        }

    return {
        "n": n,
        "r": r,
        "macro_count": len(macros),
        "raw_factorization_count": raw_count,
        "history_partition_endpoint_failures": endpoint_failures,
        "history_first_moment_failures": moment_failures,
        "history_first_moments": moment_rows,
        "maximum_canonical_individual_split_rate_over_alpha": {
            "value": str(max_individual[0]),
            "coarse": list(max_individual[1]) if max_individual[1] else None,
        },
        "maximum_first_split_propensity": propensity_row(max_propensity),
        "first_local_harmonic_failure": propensity_row(
            first_local_harmonic_failure
        ),
        "first_unary_global_harmonic_failure": propensity_row(
            first_unary_global_harmonic_failure
        ),
        "maximum_endpoint_density": max(
            endpoint_rows, key=lambda row: Fraction(row["density"])
        ),
        "minimum_endpoint_density": min(
            endpoint_rows, key=lambda row: Fraction(row["density"])
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("bounded exact range is 3 <= n-max <= 8")
    result = {
        "claims_tested": [
            "The detailed-balance nested-history partition equals the canonical endpoint density.",
            "Its stationary first moments equal (s+1)! p_(s+1)/p_1.",
            "Every canonical individual reverse first-split rate is at most alpha.",
            "The total canonical first-split propensity is at most a literal harmonic number.",
        ],
        "finite_scope_warning": (
            "A mismatch refutes an exact identity or bound. Finite agreement "
            "does not prove a universal inequality or polynomial congestion."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            f"nested_history_probe.py --n-max {args.n_max} --output {args.output}"
        ),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
