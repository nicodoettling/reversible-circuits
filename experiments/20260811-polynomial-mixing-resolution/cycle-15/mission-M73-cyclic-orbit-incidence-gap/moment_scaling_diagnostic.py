#!/usr/bin/env python3
"""Fit only descriptive finite-size models to M73 trace moments.

This does not promote an asymptotic claim.  It compares constant, inverse-n,
and log-n corrections to expose whether trace two should remain the primary
proof target or be treated as potentially logarithmically divergent.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
from pathlib import Path

import numpy as np


def fit(design: np.ndarray, values: np.ndarray) -> dict[str, object]:
    coefficients, _, _, _ = np.linalg.lstsq(design, values, rcond=None)
    residual = values - design @ coefficients
    return {
        "coefficients_numeric": [float(x) for x in coefficients],
        "max_absolute_residual_numeric": float(np.max(np.abs(residual))),
        "root_mean_square_residual_numeric": float(np.sqrt(np.mean(residual**2))),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    rows = payload["results"]
    n = np.array([row["n"] for row in rows], dtype=float)
    trace_two = np.array([
        row["l_squared_times_centered_H0_K_Hilbert_Schmidt_squared_numeric"]
        for row in rows
    ])
    trace_four = np.array([
        row["l_fourth_times_centered_H0_K_Schatten_fourth_trace_numeric"]
        for row in rows
    ])
    models = {
        "constant_plus_1_over_n_plus_1_over_n_squared": np.column_stack(
            [np.ones_like(n), 1 / n, 1 / n**2]
        ),
        "constant_plus_log_n": np.column_stack([np.ones_like(n), np.log(n)]),
        "constant_plus_log_n_over_n_plus_1_over_n": np.column_stack(
            [np.ones_like(n), np.log(n) / n, 1 / n]
        ),
    }
    output = {
        "status": "finite_numeric_diagnostic_only",
        "scope_warning": (
            "Model fits do not prove boundedness, convergence, or divergence; "
            "they only prioritize analytic proof routes."
        ),
        "input": str(args.input),
        "n": [int(x) for x in n],
        "l_squared_trace_two": [float(x) for x in trace_two],
        "l_fourth_trace_four": [float(x) for x in trace_four],
        "trace_two_fits": {name: fit(design, trace_two) for name, design in models.items()},
        "trace_four_fits": {name: fit(design, trace_four) for name, design in models.items()},
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "deterministic": True,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": (
            "python3 -B moment_scaling_diagnostic.py --input "
            f"{args.input} --output {args.output}"
        ),
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
