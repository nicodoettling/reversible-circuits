#!/usr/bin/env python3
"""Deterministic finite probe of scores inside M94's central-double event.

This is a formula/falsification diagnostic only.  It reconstructs the frozen
M83 quotient kernel and reports every event-orbit score; no finite row is used
as asymptotic evidence.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
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


def color_and_residual(gaps: list[int], residual: list[int]) -> str:
    x, y, z, w = gaps
    separated = sorted((x, z, y + w), reverse=True)
    nested = sorted((x + z, y, w), reverse=True)
    matches = []
    if separated == residual:
        matches.append("S")
    if nested == residual:
        matches.append("N")
    return "".join(matches) or "?"


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h, orbits, _, squared, pi, _ = M.build(n, False)
    oid = {state: index for index, orbit in enumerate(orbits) for state in orbit}
    source_a = oriented_cycle(n, (0, k, 2 * k))
    source_b = M.mul(M.edge_perm(n, 0, 1), M.edge_perm(n, k, 2 * k))
    delta = squared[oid[source_b]] - squared[oid[source_a]]
    threshold = (k + 1) // 2
    rows = []
    for index, orbit in enumerate(orbits):
        representative = orbit[0]
        descriptor = M.descriptor(representative, h)
        if descriptor["kind"] != "D":
            continue
        gaps = list(descriptor["support_gaps"])
        if min(gaps) < threshold:
            continue
        residual = list(descriptor["residual_sizes"])
        score = float(delta[index] / pi[index])
        rows.append({
            "orbit": index,
            "gaps": gaps,
            "gaps_over_n": [value / n for value in gaps],
            "color": color_and_residual(gaps, residual),
            "residual_sizes": residual,
            "stationary_mass": float(pi[index]),
            "delta": float(delta[index]),
            "score": score,
            "k_times_score": k * score,
        })
    mass = sum(row["stationary_mass"] for row in rows)
    signed = sum(row["delta"] for row in rows)
    by_color = {}
    for color in sorted({str(row["color"]) for row in rows}):
        subset = [row for row in rows if row["color"] == color]
        subset_mass = sum(row["stationary_mass"] for row in subset)
        subset_signed = sum(row["delta"] for row in subset)
        by_color[color] = {
            "orbits": len(subset),
            "mass": subset_mass,
            "signed": subset_signed,
            "k_times_mean_score": k * subset_signed / subset_mass,
        }
    return {
        "k": k,
        "n": n,
        "threshold": threshold,
        "quotient_states": len(orbits),
        "event_orbits": len(rows),
        "event_mass": mass,
        "event_signed": signed,
        "k_times_mass": k * mass,
        "k_squared_signed": k * k * signed,
        "k_times_mean_score": k * signed / mass,
        "by_color": by_color,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_formula_probe_only",
        "target": "M94 central-double event pointwise posterior scores",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {key: value for key, value in result.items() if key != "rows"}
        for result in payload["results"]
    ], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
