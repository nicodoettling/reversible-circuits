#!/usr/bin/env python3
"""Bounded exact audit of marked root-coalescence normalization.

This script can refute exact stationarity of the proposed history kernel.
Finite density ratios do not prove a universal polynomial bound.
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
    spec = importlib.util.spec_from_file_location("m50_exact", path)
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


def frac(x: Fraction) -> str:
    return str(x)


def boundary_spines(macro):
    children = M50.children(macro)
    answer = []
    for first_child in children[0][:-1]:
        spine = []
        vertex = first_child
        while True:
            spine.append(vertex)
            if not children[vertex]:
                break
            vertex = children[vertex][-1]
        answer.append(spine)
    return answer


def target_law(macros, raw_count, orbit_weight, root_degree):
    states = [
        macro
        for macro in macros
        if len(M50.root_composition(macro)) == root_degree
    ]
    mass = sum((orbit_weight(macro) for macro in states), 0)
    return {
        macro: Fraction(orbit_weight(macro), mass) for macro in states
    }


def one_composition_merge(
    composition, states, rates, orbit_weight, alpha
):
    source_mass = sum((orbit_weight(macro) for macro in states), 0)
    output = defaultdict(Fraction)
    k = len(composition)
    for macro in states:
        first_spine = boundary_spines(macro)[0]
        for vertex in first_spine:
            target = M50.target_after_exchange(macro, 0, vertex)
            output[target] += (
                Fraction(orbit_weight(macro), source_mass)
                * rates.get((macro, target), Fraction())
                / (alpha * k)
            )
    return dict(output)


def endpoint_coalescence(
    macros, raw_count, rates, orbit_weight, alpha, random_boundary
):
    distribution = {
        macro: Fraction(orbit_weight(macro), raw_count) for macro in macros
    }
    r = len(next(iter(macros)))
    for _ in range(r - 1):
        output = defaultdict(Fraction)
        for macro, mass in distribution.items():
            spines = boundary_spines(macro)
            k = len(spines) + 1
            if not spines:
                output[macro] += mass
                continue
            selected = spines if random_boundary else spines[:1]
            denominator = alpha * k * len(selected)
            observed = Fraction()
            for spine in selected:
                for vertex in spine:
                    target = M50.target_after_exchange(macro, 0, vertex)
                    rate = rates.get((macro, target), Fraction())
                    observed += rate
                    output[target] += mass * rate / denominator
            if observed != denominator:
                raise AssertionError(
                    (macro, observed, denominator, random_boundary)
                )
        distribution = dict(output)
    return distribution


def density_summary(distribution, target):
    ratios = sorted(
        (distribution.get(macro, Fraction()) / mass, macro)
        for macro, mass in target.items()
    )
    tv = sum(
        (
            abs(distribution.get(macro, Fraction()) - mass)
            for macro, mass in target.items()
        ),
        Fraction(),
    ) / 2
    second_moment = sum(
        (
            mass
            * (distribution.get(macro, Fraction()) / mass) ** 2
            for macro, mass in target.items()
        ),
        Fraction(),
    )
    return {
        "equal": all(ratio == 1 for ratio, _ in ratios),
        "minimum_density": frac(ratios[0][0]),
        "minimum_macro": list(ratios[0][1]),
        "maximum_density": frac(ratios[-1][0]),
        "maximum_macro": list(ratios[-1][1]),
        "total_variation": frac(tv),
        "density_second_moment": frac(second_moment),
        "chi_square": frac(second_moment - 1),
    }


def run(n):
    r = n - 1
    macros, adjacency, capacities, raw_count = M50.exact_instance(n)
    orbit_weight = M50.M41.BASE.orbit_weight
    rates = {
        edge: capacity / orbit_weight(edge[0])
        for edge, capacity in capacities.items()
    }
    alpha = Fraction(2, 3 * r * (r - 1))
    by_composition = defaultdict(list)
    for macro in macros:
        by_composition[M50.root_composition(macro)].append(macro)

    first_one_step_failure = None
    for composition in sorted(by_composition):
        if len(composition) < 2:
            continue
        merged = (composition[0] + composition[1],) + composition[2:]
        output = one_composition_merge(
            composition,
            by_composition[composition],
            rates,
            orbit_weight,
            alpha,
        )
        target_states = by_composition[merged]
        target_mass = sum(
            (orbit_weight(macro) for macro in target_states), 0
        )
        target = {
            macro: Fraction(orbit_weight(macro), target_mass)
            for macro in target_states
        }
        if output != target:
            first_one_step_failure = {
                "source_composition": list(composition),
                "target_composition": list(merged),
                "output": [
                    {"macro": list(macro), "mass": frac(output.get(macro, 0))}
                    for macro in sorted(target)
                ],
                "stationary_conditional": [
                    {"macro": list(macro), "mass": frac(target[macro])}
                    for macro in sorted(target)
                ],
                "density": [
                    {
                        "macro": list(macro),
                        "ratio": frac(output.get(macro, 0) / target[macro]),
                    }
                    for macro in sorted(target)
                ],
            }
            break

    unary_target = target_law(macros, raw_count, orbit_weight, 1)
    canonical = endpoint_coalescence(
        macros, raw_count, rates, orbit_weight, alpha, False
    )
    randomized = endpoint_coalescence(
        macros, raw_count, rates, orbit_weight, alpha, True
    )

    layer_summaries = []
    for k in range(2, r + 1):
        source = target_law(macros, raw_count, orbit_weight, k)
        output = defaultdict(Fraction)
        for macro, mass in source.items():
            spines = boundary_spines(macro)
            denominator = alpha * k * (k - 1)
            for spine in spines:
                for vertex in spine:
                    target_macro = M50.target_after_exchange(
                        macro, 0, vertex
                    )
                    output[target_macro] += (
                        mass
                        * rates.get((macro, target_macro), Fraction())
                        / denominator
                    )
        layer_target = target_law(
            macros, raw_count, orbit_weight, k - 1
        )
        layer_summaries.append(
            {"source_root_degree": k, **density_summary(output, layer_target)}
        )

    return {
        "n": n,
        "r": r,
        "macro_count": len(macros),
        "raw_factorization_count": raw_count,
        "first_one_step_normalization_failure": first_one_step_failure,
        "canonical_first_boundary_endpoint": density_summary(
            canonical, unary_target
        ),
        "uniform_boundary_endpoint": density_summary(
            randomized, unary_target
        ),
        "uniform_boundary_layer_transfers": layer_summaries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 8:
        raise SystemExit("bounded exact range is 3 <= n-max <= 8")
    result = {
        "claim_tested": (
            "Canonical or uniform-boundary marked root coalescence sends "
            "the stationary plane-tree law exactly to the stationary "
            "conditional law in the unary-root fiber."
        ),
        "universal_scope": (
            "One exact failure refutes exact normalization. Finite density "
            "ratios do not prove a universal polynomial bound."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "python": platform.python_version(),
        "git_commit": git_commit(),
        "seed": None,
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-13/mission-M56-marked-root-history-flow/"
            "marked_history_audit.py "
            f"--n-max {args.n_max} --output {args.output}"
        ),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
