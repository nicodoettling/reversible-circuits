#!/usr/bin/env python3
"""Extract the invariant central-double certificate from all-target runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summarize(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text())
    if len(payload["results"]) != 1:
        raise ValueError(f"expected one result in {path}")
    result = payload["results"][0]
    targets = result.get("all_targets")
    if targets is None:
        raise ValueError(f"{path} was not produced with --include-all")

    k = int(result["k"])
    n = int(result["n"])
    r = (k + 1) // 2
    event = [
        row
        for row in targets
        if row["kind"] == "D" and min(row["support_gaps"]) >= r
    ]

    mass = sum(row["stationary_mass"] for row in event)
    delta = sum(row["delta"] for row in event)
    event_l2 = sum(row["BA2_contribution"] for row in event)
    total_mass = sum(row["stationary_mass"] for row in targets)
    total_delta = sum(row["delta"] for row in targets)
    total_l2 = sum(row["BA2_contribution"] for row in targets)
    total_tv = sum(row["TV_contribution"] for row in targets)

    return {
        "k": k,
        "n": n,
        "source_file": path.name,
        "source_sha256": sha256(path),
        "source_command": payload["command"],
        "source_status": payload["status"],
        "central_event": {
            "definition": "double target with every support gap >= (k+1)/2",
            "threshold": r,
            "orbit_count": len(event),
            "stationary_mass": mass,
            "k_times_stationary_mass": k * mass,
            "signed_delta": delta,
            "k_squared_signed_delta": k * k * delta,
            "l2_contribution": event_l2,
            "k_fourth_l2_contribution": k**4 * event_l2,
            "cauchy_partition_lower_bound": delta * delta / mass,
            "k_fourth_cauchy_partition_lower_bound": k**4 * delta * delta / mass,
        },
        "complete_kernel": {
            "orbit_count": len(targets),
            "stationary_mass_sum": total_mass,
            "signed_delta_sum": total_delta,
            "actual_BA2_L2": result["actual_BA2_L2"],
            "summed_BA2_L2": total_l2,
            "k_fourth_actual_BA2_L2": result["k_fourth_actual_BA2_L2"],
            "actual_two_step_TV": result["actual_two_step_TV"],
            "summed_two_step_TV": total_tv,
            "k_squared_actual_two_step_TV": result[
                "k_squared_actual_two_step_TV"
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    first = json.loads(args.inputs[0].read_text())

    output = {
        "status": "finite_floating_falsification_diagnostic_only",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": first["numpy"],
        "nonstandard_dependencies": {"numpy": first["numpy"]},
        "repository_commit": first["repository_commit"],
        "command": " ".join(__import__("sys").argv),
        "results": [summarize(path) for path in args.inputs],
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
