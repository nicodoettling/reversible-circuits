#!/usr/bin/env python3
"""Exact characteristic-polynomial certificates for compressed H0 kernels.

The input is produced by h0_coordinate_correlation.py.  Its sparse rational
matrix is reconstructed over QQ, so the characteristic polynomial and root
isolating intervals below are exact.  Decimal approximations are labels only.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path

import sympy as sp


def parse_rational(text: str) -> sp.Rational:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return sp.Rational(int(numerator), int(denominator))
    return sp.Rational(int(text))


def interval_record(interval: tuple[sp.Rational, sp.Rational], multiplicity: int) -> dict:
    left, right = interval
    return {
        "left_exact": str(left),
        "right_exact": str(right),
        "midpoint_numeric": float((left + right) / 2),
        "multiplicity": int(multiplicity),
    }


def certify(row: dict, tolerance_power: int) -> dict:
    dimension = int(row["theta_orbits"])
    matrix = sp.zeros(dimension)
    for source, target, value in row["H0_K_sparse_exact"]:
        matrix[int(source), int(target)] = parse_rational(value)

    stationary = sp.Matrix(1, dimension, [
        parse_rational(value) for value in row["orbit_masses_exact"]
    ])
    centered = matrix - sp.ones(dimension, 1) * stationary
    centered_square = centered * centered
    centered_trace_two = sp.factor(sp.trace(centered_square))
    centered_trace_four = sp.factor(sp.trace(centered_square * centered_square))
    centered_square_row_l1 = [
        sp.factor(sum(abs(centered_square[source, target]) for target in range(dimension)))
        for source in range(dimension)
    ]
    max_centered_square_row_l1 = max(centered_square_row_l1)
    max_centered_square_row_l1_source = centered_square_row_l1.index(
        max_centered_square_row_l1
    )

    variable = sp.Symbol("x")
    characteristic = sp.Poly(matrix.charpoly(variable).as_expr(), variable, domain=sp.QQ)
    denominator, integer_poly = characteristic.clear_denoms(convert=True)
    _, primitive = integer_poly.primitive()
    intervals = characteristic.intervals(eps=sp.Rational(1, 10**tolerance_power))
    roots = []
    for interval, multiplicity in intervals:
        roots.extend([interval_record(interval, multiplicity)] * multiplicity)
    roots.sort(key=lambda item: item["midpoint_numeric"])
    if len(roots) != dimension:
        raise AssertionError("root isolation did not recover the matrix dimension")
    # Remove exactly one copy of the constant root, as required by the
    # one-coordinate mean-zero space.  At n=5 other exact roots at one remain.
    constant_candidates = [
        index
        for index, root in enumerate(roots)
        if parse_rational(root["left_exact"]) <= 1 <= parse_rational(root["right_exact"])
    ]
    if not constant_candidates:
        raise AssertionError("constant eigenvalue one was not isolated")
    del roots[constant_candidates[-1]]

    factor_data = []
    for factor, exponent in sp.factor_list(primitive.as_expr())[1]:
        polynomial = sp.Poly(factor, variable, domain=sp.ZZ)
        factor_data.append({
            "degree": polynomial.degree(),
            "exponent": int(exponent),
            "coefficients_descending": [str(value) for value in polynomial.all_coeffs()],
        })
    factor_data.sort(key=lambda item: (item["degree"], item["coefficients_descending"]))
    return {
        "n": row["n"],
        "l": row["l"],
        "dimension": dimension,
        "characteristic_polynomial_denominator_cleared": str(denominator),
        "primitive_integer_characteristic_factors": factor_data,
        "centered_trace_second_exact": str(centered_trace_two),
        "l_squared_centered_trace_second_numeric": float(
            row["l"] ** 2 * centered_trace_two
        ),
        "centered_trace_fourth_exact": str(centered_trace_four),
        "l_fourth_centered_trace_fourth_numeric": float(
            row["l"] ** 4 * centered_trace_four
        ),
        "max_centered_K_squared_row_L1_exact": str(max_centered_square_row_l1),
        "max_centered_K_squared_row_L1_source_orbit": (
            max_centered_square_row_l1_source
        ),
        "l_squared_max_centered_K_squared_row_L1_numeric": float(
            row["l"] ** 2 * max_centered_square_row_l1
        ),
        "bottom_mean_zero_root_interval": roots[0],
        "top_mean_zero_root_interval": roots[-1],
        "all_roots_isolated_exactly": True,
        "constant_root_removed_copies": 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--n", type=int, action="append")
    parser.add_argument("--tolerance-power", type=int, default=12)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    selected = set(args.n or [row["n"] for row in source["results"]])
    rows = [row for row in source["results"] if row["n"] in selected]
    if {row["n"] for row in rows} != selected:
        raise ValueError("requested n is absent from input")
    payload = {
        "status": "complete",
        "claim": (
            "The displayed rational intervals rigorously isolate the extremal "
            "mean-zero roots of the exact H0 kernel at the listed finite n."
        ),
        "scope_warning": "Finite exact spectra do not prove an asymptotic bound.",
        "input": str(args.input),
        "tolerance_power": args.tolerance_power,
        "records": [certify(row, args.tolerance_power) for row in rows],
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([
        {
            "n": record["n"],
            "dimension": record["dimension"],
            "kappa_min_interval": record["bottom_mean_zero_root_interval"],
            "kappa_max_interval": record["top_mean_zero_root_interval"],
            "factor_degrees": [
                (factor["degree"], factor["exponent"])
                for factor in record["primitive_integer_characteristic_factors"]
            ],
        }
        for record in payload["records"]
    ], indent=2))


if __name__ == "__main__":
    main()
