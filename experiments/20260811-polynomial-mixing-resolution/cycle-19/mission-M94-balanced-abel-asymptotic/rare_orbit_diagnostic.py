#!/usr/bin/env python3
"""Finite floating shell diagnostic for the balanced BA2 contrast.

This imports the accepted M83 kernel builder solely to falsify asymptotic
ansatzes.  It does not prove any rate.  The localized signed target row is
grouped by invariant target residual data before either its L1 or L2
contribution is accumulated.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


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


def shell_rows(groups, k: int):
    rows = []
    for key, values in sorted(groups.items(), key=lambda item: item[0]):
        signed, l1, l2, mass, count = values
        rows.append({
            "shell": key if isinstance(key, (str, int)) else list(key),
            "orbit_count": count,
            "stationary_mass": mass,
            "signed_delta": signed,
            "TV_contribution": l1 / 2,
            "BA2_contribution": l2,
            "k_squared_TV_contribution": k * k * l1 / 2,
            "k_fourth_BA2_contribution": k ** 4 * l2,
        })
    return rows


def score_envelope_rows(groups, k: int):
    rows = []
    for key, targets in sorted(groups.items(), key=lambda item: item[0]):
        mass = sum(row["stationary_mass"] for row in targets)
        signed = sum(row["delta"] for row in targets)
        absolute = sum(abs(row["delta"]) for row in targets)
        max_score = max(abs(row["posterior_score"]) for row in targets)
        rms_score = np.sqrt(
            sum(row["BA2_contribution"] for row in targets) / mass
        )
        rows.append({
            "shell": key if isinstance(key, (str, int)) else list(key),
            "orbit_count": len(targets),
            "stationary_mass": mass,
            "signed_delta": signed,
            "absolute_delta": absolute,
            "maximum_absolute_score": max_score,
            "conditional_RMS_score": float(rms_score),
            "k_times_maximum_absolute_score": k * max_score,
            "k_times_conditional_RMS_score": k * float(rms_score),
            "k_squared_absolute_delta": k * k * absolute,
        })
    return rows


def double_color(cycles, support):
    if len(cycles) != 2:
        return None
    p0, p1, p2, p3 = support
    edges = {tuple(sorted(cycle)) for cycle in cycles}
    if edges == {(p0, p1), (p2, p3)}:
        return "S"
    if edges == {(p0, p3), (p1, p2)}:
        return "N"
    raise AssertionError((cycles, support))


def analyze(k: int, top: int, include_all: bool) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h, orbits, kernel, squared, pi, _ = M.build(n, False)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}
    a = oriented_cycle(n, (0, k, 2 * k))
    b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    delta = squared[oid[b]] - squared[oid[a]]

    by_min = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0, 0])
    by_sizes = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0, 0])
    by_kind_min = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0, 0])
    score_by_min = defaultdict(list)
    score_by_kind_min = defaultdict(list)
    targets = []
    for index, (orbit, value, mass) in enumerate(zip(orbits, delta, pi)):
        representative = orbit[0]
        target_descriptor = M.descriptor(representative, h)
        sizes = tuple(sorted(M.cycle_sizes(M.mul(M.inv(representative), h))))
        minimum = sizes[0]
        target_kind = M.kind(representative)
        l1 = abs(float(value))
        l2 = float(value) ** 2 / float(mass)
        for group, key in (
            (by_min, minimum),
            (by_sizes, sizes),
            (by_kind_min, (target_kind, minimum)),
        ):
            row = group[key]
            row[0] += float(value)
            row[1] += l1
            row[2] += l2
            row[3] += float(mass)
            row[4] += 1
        moved = sorted(vertex for cycle in target_descriptor["cycles"] for vertex in cycle)
        target_row = {
            "orbit": index,
            "kind": target_kind,
            "cycles": target_descriptor["cycles"],
            "support_gaps": target_descriptor["support_gaps"],
            "double_color": double_color(target_descriptor["cycles"], moved),
            "residual_sizes": list(sizes),
            "orbit_size": len(orbit),
            "stationary_mass": float(mass),
            "delta": float(value),
            "posterior_score": float(value) / float(mass),
            "TV_contribution": l1 / 2,
            "BA2_contribution": l2,
            "k_squared_TV_contribution": k * k * l1 / 2,
            "k_fourth_BA2_contribution": k ** 4 * l2,
        }
        targets.append(target_row)
        score_by_min[minimum].append(target_row)
        score_by_kind_min[(target_kind, minimum)].append(target_row)

    actual_tv = 0.5 * float(np.sum(np.abs(delta)))
    actual_l2 = float(np.sum(delta * delta / pi))
    top_l2 = sorted(targets, key=lambda row: row["BA2_contribution"], reverse=True)[:top]
    top_tv = sorted(targets, key=lambda row: row["TV_contribution"], reverse=True)[:top]
    central_targets = []
    eta = kernel[oid[b]] - kernel[oid[a]]
    for color in ("S", "N"):
        candidates = [row for row in targets if row["double_color"] == color]
        central = min(
            candidates,
            key=lambda row: sum((gap - n / 4.0) ** 2 for gap in row["support_gaps"]),
        )
        target_index = central["orbit"]
        grouped = defaultdict(lambda: [0.0, 0.0])
        for source_index, contribution in enumerate(eta * kernel[:, target_index]):
            source = orbits[source_index][0]
            source_sizes = M.cycle_sizes(M.mul(M.inv(source), h))
            key = (M.kind(source), min(source_sizes))
            grouped[key][0] += float(contribution)
            grouped[key][1] += abs(float(contribution))
        central_targets.append({
            **central,
            "k_times_score": k * central["posterior_score"],
            "intermediate_shells": [
                {
                    "kind": key[0],
                    "minimum_residual_size": key[1],
                    "k_times_signed_score_contribution": k * values[0] / float(pi[target_index]),
                    "k_times_triangle_score_seminorm": k * values[1] / float(pi[target_index]),
                }
                for key, values in sorted(grouped.items())
            ],
        })
    result = {
        "k": k,
        "n": n,
        "quotient_states": len(orbits),
        "actual_two_step_TV": actual_tv,
        "k_squared_actual_two_step_TV": k * k * actual_tv,
        "actual_BA2_L2": actual_l2,
        "k_fourth_actual_BA2_L2": k ** 4 * actual_l2,
        "by_minimum_residual_size": shell_rows(by_min, k),
        "by_kind_and_minimum_residual_size": shell_rows(by_kind_min, k),
        "by_residual_size_triple": shell_rows(by_sizes, k),
        "score_envelope_by_minimum_residual_size": score_envelope_rows(score_by_min, k),
        "score_envelope_by_kind_and_minimum_residual_size": score_envelope_rows(score_by_kind_min, k),
        "top_BA2_orbits": top_l2,
        "top_TV_orbits": top_tv,
        "central_bulk_targets": central_targets,
    }
    if include_all:
        result["all_targets"] = targets
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", required=True, type=int)
    parser.add_argument("--top", default=30, type=int)
    parser.add_argument("--include-all", action="store_true")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_falsification_diagnostic_only",
        "target": "balanced localized BA2 and direct signed L1",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k, args.top, args.include_all) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {
            "k": row["k"],
            "states": row["quotient_states"],
            "k2_TV": row["k_squared_actual_two_step_TV"],
            "k4_BA2": row["k_fourth_actual_BA2_L2"],
        }
        for row in payload["results"]
    ], indent=2))


if __name__ == "__main__":
    main()
