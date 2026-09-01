#!/usr/bin/env python3
"""Bounded falsifiers for the root-composition quotient and split bias.

The sparse spectrum uses all 2^(r-1) ordered compositions and the exact
quotient rates, divided by alpha_r.  The reverse-split audit imports the
already checked exact long-cycle constructor and enumerates only n <= 8.
Neither finite calculation proves an asymptotic claim.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


Composition = tuple[int, ...]


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def compositions(r: int) -> list[Composition]:
    answer = []
    for mask in range(1 << (r - 1)):
        comp = []
        part = 1
        for gap in range(r - 1):
            if mask & (1 << gap):
                comp.append(part)
                part = 1
            else:
                part += 1
        comp.append(part)
        answer.append(tuple(comp))
    return answer


def w(a: int) -> Fraction:
    return Fraction(a ** (a - 1), math.factorial(a))


def quotient_spectrum(r: int) -> dict:
    """Numerical spectrum of -G_r/alpha_r, assembled edge by edge."""
    states = compositions(r)
    index = {state: i for i, state in enumerate(states)}
    diagonal = np.zeros(len(states))
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    edge_count = 0

    for refined in states:
        k = len(refined)
        if k < 2:
            continue
        i = index[refined]
        for p in range(k - 1):
            a, b = refined[p], refined[p + 1]
            coarse = refined[:p] + (a + b,) + refined[p + 2 :]
            j = index[coarse]
            beta_down = Fraction(k)
            beta_up = w(a) * w(b) / w(a + b)
            diagonal[i] += float(beta_down)
            diagonal[j] += float(beta_up)
            off = -math.sqrt(float(beta_down * beta_up))
            rows.extend((i, j))
            cols.extend((j, i))
            data.extend((off, off))
            edge_count += 1

    rows.extend(range(len(states)))
    cols.extend(range(len(states)))
    data.extend(diagonal.tolist())
    laplacian = coo_matrix(
        (data, (rows, cols)), shape=(len(states), len(states))
    ).tocsr()

    if len(states) <= 16:
        eigenvalues = np.linalg.eigvalsh(laplacian.toarray())[:5]
    else:
        eigenvalues = eigsh(
            laplacian,
            k=min(5, len(states) - 1),
            which="SM",
            return_eigenvectors=False,
            tol=1e-11,
            maxiter=max(10000, 20 * len(states)),
        )
        eigenvalues.sort()
    zero = float(eigenvalues[0])
    gamma = float(eigenvalues[1])
    return {
        "r": r,
        "state_count": len(states),
        "undirected_edge_count": edge_count,
        "smallest_eigenvalues_of_minus_G_over_alpha": [
            float(x) for x in eigenvalues
        ],
        "zero_residual": abs(zero),
        "gamma_equals_gap_over_alpha": gamma,
        "gamma_times_r": gamma * r,
        "proved_lower_constant_one_over_3e": 1.0 / (3.0 * math.e),
    }


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


def reverse_split_audit(n: int, m50) -> dict:
    """Exact aggregate split-target RN data for all root compositions."""
    r = n - 1
    macros, adjacency, capacities, _ = m50.exact_instance(n)
    orbit_weight = m50.M41.BASE.orbit_weight
    rates = {
        edge: Fraction(capacity, orbit_weight(edge[0]))
        for edge, capacity in capacities.items()
    }
    by_comp = defaultdict(list)
    for macro in macros:
        by_comp[m50.root_composition(macro)].append(macro)

    records = []
    formula_failures = []
    for comp, states in sorted(by_comp.items()):
        split_rates = {}
        for source in states:
            split_rates[source] = sum(
                (
                    rates[source, target]
                    for target in adjacency[source]
                    if len(m50.root_composition(target)) == len(comp) + 1
                ),
                Fraction(),
            )
        mass = sum((Fraction(orbit_weight(x)) for x in states), Fraction())
        qbar = sum(
            (
                Fraction(orbit_weight(x), 1) * split_rates[x]
                for x in states
            ),
            Fraction(),
        ) / mass
        alpha = Fraction(2, 3 * r * (r - 1))
        h_comp = sum((Fraction(c - 1, c) for c in comp), Fraction())
        expected = 2 * alpha * h_comp
        if qbar != expected:
            formula_failures.append(
                {
                    "composition": list(comp),
                    "observed": str(qbar),
                    "expected": str(expected),
                }
            )
        if qbar == 0:
            continue
        rn_values = {x: split_rates[x] / qbar for x in states}
        chi_square = sum(
            (
                Fraction(orbit_weight(x), 1)
                * (rn_values[x] - 1) ** 2
                for x in states
            ),
            Fraction(),
        ) / mass
        p_max = max(split_rates.values())
        p_max_states = [x for x in states if split_rates[x] == p_max]
        k = len(comp)
        alpha = Fraction(2, 3 * r * (r - 1))
        theoretical_p_max = alpha * (r - k)
        theoretical_rn = Fraction(r - k + 1, 2)
        records.append(
            {
                "composition": list(comp),
                "fiber_macro_count": len(states),
                "mean_split_rate": str(qbar),
                "maximum_pointwise_split_rate": str(p_max),
                "maximum_pointwise_macros": [
                    list(x) for x in p_max_states
                ],
                "maximum_pointwise_degrees": [
                    m50.degrees(x) for x in p_max_states
                ],
                "maximum_RN": str(max(rn_values.values())),
                "chi_square_RN": str(chi_square),
                "q_times_chi_square": str(qbar * chi_square),
                "pmax_upper_bound": str(theoretical_p_max),
                "RN_upper_bound": str(theoretical_rn),
                "pointwise_bounds_hold": (
                    p_max <= theoretical_p_max
                    and max(rn_values.values()) <= theoretical_rn
                ),
            }
        )

    def frac_key(record: dict, field: str) -> Fraction:
        return Fraction(record[field])

    return {
        "n": n,
        "r": r,
        "split_mean_formula_failures": formula_failures,
        "all_pointwise_bounds_hold": all(
            record["pointwise_bounds_hold"] for record in records
        ),
        "worst_maximum_RN": max(
            records, key=lambda x: frac_key(x, "maximum_RN")
        ),
        "worst_chi_square_RN": max(
            records, key=lambda x: frac_key(x, "chi_square_RN")
        ),
        "worst_q_times_chi_square": max(
            records, key=lambda x: frac_key(x, "q_times_chi_square")
        ),
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=14)
    parser.add_argument("--exact-r-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.r_max <= 18:
        raise SystemExit("require 2 <= r-max <= 18")
    if not 2 <= args.exact_r_max <= 7:
        raise SystemExit("require 2 <= exact-r-max <= 7 (n <= 8)")

    m50 = load_m50()
    result = {
        "claim_tested": (
            "The normalized root quotient gap gap(G_r)/alpha_r does not "
            "decay over the tested range, and the exact aggregate reverse-"
            "split target density obeys the derived O(r) bound."
        ),
        "universal_scope": (
            "A failure refutes the named formula/bound.  A finite pass or "
            "stable numerical spectrum proves no asymptotic gap theorem."
        ),
        "convention": "(pq)(x)=p(q(x)); factor tuples left-to-right",
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "git_commit": git_commit(),
        "command": (
            "python3 -B experiments/20260811-polynomial-mixing-resolution/"
            "cycle-12/mission-M54-root-mean-lift-referee/"
            "root_quotient_spectrum.py "
            f"--r-max {args.r_max} --exact-r-max {args.exact_r_max} "
            f"--output {args.output}"
        ),
        "spectrum": [
            quotient_spectrum(r) for r in range(2, args.r_max + 1)
        ],
        "reverse_split": [
            reverse_split_audit(n, m50)
            for n in range(3, args.exact_r_max + 2)
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
