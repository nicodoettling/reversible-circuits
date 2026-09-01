#!/usr/bin/env python3
"""Exact finite H^{-1} norms of root-split target-bias functionals."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh


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
    spec = importlib.util.spec_from_file_location("m50_hminus", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add_edge(laplacian, i, j, capacity):
    laplacian[i, i] += capacity
    laplacian[j, j] += capacity
    laplacian[i, j] -= capacity
    laplacian[j, i] -= capacity


def hminus_norm_squared(laplacian, linear, tolerance=1e-11):
    values, vectors = eigh(laplacian)
    answer = 0.0
    zero_projection = 0.0
    for value, vector in zip(values, vectors.T):
        projection = float(vector @ linear)
        if value <= tolerance:
            zero_projection = max(zero_projection, abs(projection))
        else:
            answer += projection * projection / float(value)
    return answer, zero_projection


def run(r: int, m50) -> dict:
    macros, adjacency, capacities, raw_count = m50.exact_instance(r + 1)
    orbit_weight = m50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    by_comp = defaultdict(list)
    for macro in macros:
        by_comp[m50.root_composition(macro)].append(macro)

    rows = []
    maximum_individual = None
    maximum_sum = None
    zero_projection_max = 0.0
    for comp, states_unsorted in sorted(by_comp.items()):
        states = sorted(states_unsorted)
        index = {state: i for i, state in enumerate(states)}
        masses = np.array([float(orbit_weight(x)) for x in states])
        masses /= masses.sum()
        laplacian = np.zeros((len(states), len(states)))
        comp_mass_count = sum(Fraction(orbit_weight(x)) for x in states)
        for (source, target), capacity_count in capacities.items():
            if source not in index or target not in index:
                continue
            i, j = index[source], index[target]
            if i >= j:
                continue
            q_conditional = float(
                Fraction(capacity_count, 1) / comp_mass_count
            )
            add_edge(laplacian, i, j, q_conditional)

        refined_comps = sorted(
            {
                m50.root_composition(target)
                for source in states
                for target in adjacency[source]
                if len(m50.root_composition(target)) == len(comp) + 1
            }
        )
        edge_rows = []
        sum_coefficient = 0.0
        for refined in refined_comps:
            p = np.array(
                [
                    float(
                        sum(
                            (
                                rates[source, target]
                                for target in adjacency[source]
                                if m50.root_composition(target) == refined
                            ),
                            Fraction(),
                        )
                    )
                    for source in states
                ]
            )
            mean_rate = float(masses @ p)
            centered = p - mean_rate
            linear = masses * centered
            if len(states) == 1:
                norm_squared = 0.0
                zero_projection = abs(float(linear[0]))
            else:
                norm_squared, zero_projection = hminus_norm_squared(
                    laplacian, linear
                )
            zero_projection_max = max(zero_projection_max, zero_projection)
            coefficient = (
                norm_squared / mean_rate if mean_rate > 0 else 0.0
            )
            sum_coefficient += coefficient
            row = {
                "refined_composition": list(refined),
                "mean_split_rate": mean_rate,
                "hminus_norm_squared": norm_squared,
                "coefficient_hminus_over_mean_rate": coefficient,
                "density_max": float(np.max(p) / mean_rate),
                "density_chi_square": float(
                    masses @ ((p / mean_rate - 1.0) ** 2)
                ),
            }
            edge_rows.append(row)
            if (
                maximum_individual is None
                or coefficient
                > maximum_individual[
                    "coefficient_hminus_over_mean_rate"
                ]
            ):
                maximum_individual = {
                    "coarse_composition": list(comp),
                    **row,
                }
        comp_row = {
            "coarse_composition": list(comp),
            "fiber_size": len(states),
            "sum_bias_coefficients": sum_coefficient,
            "edge_rows": edge_rows,
        }
        rows.append(comp_row)
        if (
            maximum_sum is None
            or sum_coefficient > maximum_sum["sum_bias_coefficients"]
        ):
            maximum_sum = comp_row

    return {
        "r": r,
        "macro_count": len(macros),
        "maximum_individual": maximum_individual,
        "maximum_sum": maximum_sum,
        "maximum_nullspace_projection_residual": zero_projection_max,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 7:
        raise SystemExit("bounded exact range is 2 <= r-max <= 7")
    m50 = load_m50()
    result = {
        "claim_tested": (
            "All individual reverse-split target-bias densities have "
            "polynomial-looking H-minus-one norm in the exact rejected-exit "
            "root-fiber restriction through r <= 7."
        ),
        "universal_scope": (
            "A disconnected support with nonzero null projection refutes "
            "finite mean-lift control.  Small finite norms prove no "
            "universal polynomial Hardy/Poincare inequality."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "git_commit": git_commit(),
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-12/mission-M54-root-mean-lift-referee/"
            "spine_bias_hminus.py "
            f"--r-max {args.r_max} --output {args.output}"
        ),
        "records": [run(r, m50) for r in range(2, args.r_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
