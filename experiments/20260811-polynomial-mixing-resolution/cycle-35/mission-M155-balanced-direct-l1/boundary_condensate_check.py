#!/usr/bin/env python3
"""Deterministic checks for the M155 boundary-condensate reduction.

Exact rational arithmetic checks the colored-cell stationary weight.  The
Borel harmonic sums and inherited k=7,9 shell profiles are finite floating
calibration only; they do not prove score asymptotics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]


def tau(r: int) -> Fraction:
    return Fraction(r ** (r - 1), math.factorial(r))


def cell_weight_exact(n: int, a: int, b: int) -> Fraction:
    c = n - a - b
    if min(a, b) < 1 or c < 2:
        raise ValueError((n, a, b))
    return (
        Fraction(c - 1, 2)
        * Fraction(n * math.factorial(n - 3), n ** (n - 2))
        * tau(a)
        * tau(b)
        * tau(c)
    )


def log_borel(j: int) -> float:
    return -j + (j - 1) * math.log(j) - math.lgamma(j + 1)


def borel(j: int) -> float:
    return math.exp(log_borel(j))


def harmonic_sum(D: int) -> float:
    masses = [0.0] + [borel(j) for j in range(1, D + 1)]
    suffix = 0.0
    total = 0.0
    for r in range(D, 0, -1):
        suffix += masses[r]
        total += suffix * suffix
    return total


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inherited_shell_rows(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text())
    result = payload["results"][0]
    k = int(result["k"])
    rows = []
    for row in result["by_minimum_residual_size"]:
        d = int(row["shell"])
        scaled_absolute = 2.0 * float(row["k_squared_TV_contribution"])
        rows.append({
            "d": d,
            "k_squared_absolute_shell_mass": scaled_absolute,
            "d_times_k_squared_absolute_shell_mass": d * scaled_absolute,
        })
    return {
        "source": str(path.relative_to(ROOT)),
        "source_sha256": sha256(path),
        "k": k,
        "status": "inherited_finite_floating_evidence_only",
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    exact_rows = []
    total_mass_rows = []
    for n in (9, 15, 21, 27):
        for a, b in ((1, 1), (1, 3), (3, 3)):
            if n - a - b < 2:
                continue
            weight = cell_weight_exact(n, a, b)
            limit = 0.5 * borel(a) * borel(b)
            exact_rows.append({
                "n": n,
                "a": a,
                "b": b,
                "exact_weight": str(weight),
                "float_weight": float(weight),
                "limit_half_ba_bb": limit,
                "ratio_to_limit": float(weight) / limit,
            })
        total = sum(
            (
                cell_weight_exact(n, a, b)
                for a in range(1, n - 2)
                for b in range(1, n - a - 1)
            ),
            Fraction(0),
        )
        expected = Fraction(n - 3, 2 * n)
        if total != expected:
            raise AssertionError((n, total, expected))
        total_mass_rows.append({
            "n": n,
            "sum_exact_cell_weights": str(total),
            "expected_half_double_mass": str(expected),
            "identity_verified": True,
        })

    harmonic_rows = []
    for D in (10, 100, 1000, 10000, 100000):
        value = harmonic_sum(D)
        harmonic_rows.append({
            "D": D,
            "H_D": value,
            "H_D_over_log_D": value / math.log(D),
            "limit_2_over_pi": 2.0 / math.pi,
        })

    shell_paths = [
        ROOT / "experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/score_envelopes_k7.json",
        ROOT / "experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/score_envelopes_k9.json",
    ]
    shell_rows = [inherited_shell_rows(path) for path in shell_paths]

    payload = {
        "status": "exact_weight_identity_and_finite_floating_calibration_only",
        "target": "balanced minimal-long-cycle quotient boundary-condensate reduction",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "exact_colored_cell_weights": exact_rows,
        "exact_total_cell_mass": total_mass_rows,
        "borel_harmonic_partial_sums": harmonic_rows,
        "inherited_shell_calibration": shell_rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "exact_rows": len(exact_rows),
        "harmonic": harmonic_rows,
        "shell_sources": [row["source"] for row in shell_rows],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
