#!/usr/bin/env python3
"""Exact finite certificate for the central double-target bulk event.

The calculation tests the scalar obstruction

    Delta_k(E_k) = Kbar^2(B_k,E_k)-Kbar^2(A_k,E_k),

where every cyclic support gap of a double target in E_k is at least
``(k+1)/2``.  Exact finite values can falsify formulas but do not establish
an asymptotic lower bound.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
M83 = (
    ROOT
    / "experiments/20260811-polynomial-mixing-resolution/cycle-17/"
      "mission-M83-endpoint-sharing-influence/influence_diagnostic.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load_module("m83_influence", M83)


def oriented_cycle(n: int, entries: tuple[int, ...]):
    out = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        out[a] = b
    return tuple(out)


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def exact_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def event_mass_composition_formula(n: int, threshold: int) -> Fraction:
    weighted = Fraction(0)
    for x in range(threshold, n + 1):
        for y in range(threshold, n - x + 1):
            for z in range(threshold, n - x - y + 1):
                w = n - x - y - z
                if w < threshold:
                    continue
                weighted += tau(x) * tau(z) * tau(y + w)
    return Fraction(n * math.factorial(n - 3), n ** (n - 2)) * weighted


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    threshold = (k + 1) // 2
    h, orbits, kernel, squared, pi, _ = M.build(n, True)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}
    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    ai, bi = oid[source_a], oid[source_b]

    event = []
    for index, orbit in enumerate(orbits):
        representative = orbit[0]
        if M.kind(representative) != "D":
            continue
        gaps = M.descriptor(representative, h)["support_gaps"]
        if min(gaps) >= threshold:
            event.append(index)

    delta = [squared[bi][index] - squared[ai][index] for index in range(len(orbits))]
    event_mass = sum((pi[index] for index in event), Fraction(0))
    event_delta = sum((delta[index] for index in event), Fraction(0))
    event_l2 = sum((delta[index] ** 2 / pi[index] for index in event), Fraction(0))
    event_partition_lower = event_delta ** 2 / event_mass
    actual_l2 = sum((delta[index] ** 2 / pi[index] for index in range(len(orbits))), Fraction(0))
    actual_tv = sum((abs(value) for value in delta), Fraction(0)) / 2
    formula_mass = event_mass_composition_formula(n, threshold)
    if formula_mass != event_mass:
        raise AssertionError("colored-composition event mass formula failed")
    if event_l2 < event_partition_lower or actual_l2 < event_l2:
        raise AssertionError("stationary Cauchy lower bound failed")

    return {
        "k": k,
        "n": n,
        "threshold": threshold,
        "quotient_states": len(orbits),
        "event_orbits": len(event),
        "event_stationary_mass": exact_string(event_mass),
        "k_times_event_stationary_mass": exact_string(k * event_mass),
        "event_signed_two_step_difference": exact_string(event_delta),
        "k_squared_event_signed_difference": exact_string(k * k * event_delta),
        "event_BA2_contribution": exact_string(event_l2),
        "k_fourth_event_BA2_contribution": exact_string(k ** 4 * event_l2),
        "event_partition_BA2_lower_bound": exact_string(event_partition_lower),
        "k_fourth_event_partition_lower_bound": exact_string(k ** 4 * event_partition_lower),
        "actual_two_step_TV": exact_string(actual_tv),
        "k_squared_actual_two_step_TV": exact_string(k * k * actual_tv),
        "actual_BA2_L2": exact_string(actual_l2),
        "k_fourth_actual_BA2_L2": exact_string(k ** 4 * actual_l2),
        "composition_mass_formula_matches": True,
        "stationary_Cauchy_lower_bound_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "exact_finite_formula_certificate_only",
        "target": "central double bulk event scalar obstruction to balanced BA2",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
