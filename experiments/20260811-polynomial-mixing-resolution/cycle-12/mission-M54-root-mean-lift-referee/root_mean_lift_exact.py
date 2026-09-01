#!/usr/bin/env python3
"""Exact-state numerical falsifier for ROOT-MEAN LIFT.

For each r <= 7 this builds the exact full Pbar stationary capacities on
parking degree macros, its root-composition stationary-flow quotient, and
the lifted quotient quadratic form f -> E_G(E[f|root],E[f|root]).  The
largest generalized eigenvalue against E_P is the sharp finite mean-lift
constant.  Floating eigensolves are diagnostics, not asymptotic proofs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.linalg import eigvalsh


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
    spec = importlib.util.spec_from_file_location("m50_exact_lift", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add_edge(laplacian: np.ndarray, i: int, j: int, q: float) -> None:
    laplacian[i, i] += q
    laplacian[j, j] += q
    laplacian[i, j] -= q
    laplacian[j, i] -= q


def first_positive(values: np.ndarray, tolerance: float = 1e-9) -> float:
    for value in values:
        if value > tolerance:
            return float(value)
    raise RuntimeError("no positive generalized eigenvalue")


def run(n: int, m50) -> dict:
    r = n - 1
    macros, _, capacities, raw_count = m50.exact_instance(n)
    states = sorted(macros)
    state_index = {state: i for i, state in enumerate(states)}
    orbit_weight = m50.M41.BASE.orbit_weight
    pi = np.array(
        [float(orbit_weight(state) / raw_count) for state in states]
    )

    comps = sorted({m50.root_composition(state) for state in states})
    comp_index = {comp: i for i, comp in enumerate(comps)}
    rho = np.zeros(len(comps))
    conditional = np.zeros((len(comps), len(states)))
    for state in states:
        i = state_index[state]
        a = comp_index[m50.root_composition(state)]
        rho[a] += pi[i]
    for state in states:
        i = state_index[state]
        a = comp_index[m50.root_composition(state)]
        conditional[a, i] = pi[i] / rho[a]

    lp = np.zeros((len(states), len(states)))
    lg = np.zeros((len(comps), len(comps)))
    for (source, target), capacity_count in capacities.items():
        i, j = state_index[source], state_index[target]
        if i >= j:
            continue
        q = float(capacity_count / raw_count)
        add_edge(lp, i, j, q)
        a = comp_index[m50.root_composition(source)]
        b = comp_index[m50.root_composition(target)]
        if a != b:
            add_edge(lg, a, b, q)

    lifted = conditional.T @ lg @ conditional
    # lp is singular only on constants.  pi*pi^T makes the denominator
    # positive definite there, while lifted annihilates constants.
    denominator = lp + np.outer(pi, pi)
    mean_lift_values = eigvalsh(lifted, denominator)
    p_gap_values = eigvalsh(lp, np.diag(pi))
    g_gap_values = eigvalsh(lg, np.diag(rho))
    sharp = float(mean_lift_values[-1])
    return {
        "n": n,
        "r": r,
        "macro_count": len(states),
        "root_composition_count": len(comps),
        "sharp_mean_lift_constant": sharp,
        "sharp_mean_lift_constant_over_r": sharp / r,
        "sharp_mean_lift_constant_over_r_squared": sharp / (r * r),
        "full_Pbar_gap": first_positive(p_gap_values),
        "root_quotient_gap": first_positive(g_gap_values),
        "root_gap_times_r_rminus1": (
            first_positive(g_gap_values) * r * (r - 1)
        ),
        "generalized_zero_residual": float(
            np.max(np.abs(mean_lift_values[mean_lift_values < 1e-9]))
            if np.any(mean_lift_values < 1e-9)
            else 0.0
        ),
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
            "The sharp finite constant in E_G(E[f|root]) <= A_r E_P(f) "
            "does not exhibit superpolynomial growth over r <= 7."
        ),
        "universal_scope": (
            "A singularity or anomalously large A_r can refute a proposed "
            "bounded-range claim.  Finite numerical values prove no "
            "universal polynomial mean-lift inequality."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "git_commit": git_commit(),
        "command": (
            "python3 -B experiments/"
            "20260811-polynomial-mixing-resolution/cycle-12/"
            "mission-M54-root-mean-lift-referee/root_mean_lift_exact.py "
            f"--r-max {args.r_max} --output {args.output}"
        ),
        "records": [run(n, m50) for n in range(3, args.r_max + 2)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
