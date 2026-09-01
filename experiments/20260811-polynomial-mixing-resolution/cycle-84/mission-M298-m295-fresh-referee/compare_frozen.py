#!/usr/bin/env python3
"""Post-hoc comparison of independently generated M298 data to frozen M295."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def cell_map(payload: dict) -> dict[tuple[int, tuple[int, int]], Fraction]:
    return {
        (int(row["ell"]), tuple(row["middle_edge"])): Fraction(row["fmcp_value"])
        for row in payload["cells"]
    }


def fraction_map(values: dict[str, str]) -> dict[int, Fraction]:
    return {int(key): Fraction(value) for key, value in values.items()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--independent", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    independent = json.loads(args.independent.read_text())
    frozen = json.loads(args.frozen.read_text())
    checks = {
        "all_120_cells_equal": cell_map(independent) == cell_map(frozen),
        "all_12_eta1_lags_equal": fraction_map(independent["eta1_direct"])
        == fraction_map(frozen["channel_one_lag_totals"]),
        "all_12_weighted_alpha1_cp1_equal": fraction_map(
            independent["weighted_alpha1_CP1"]
        )
        == fraction_map(frozen["weighted_channel_one_cp"]),
        "minimum_value_equal": Fraction(independent["minimum_value"])
        == Fraction(frozen["minimum_cell"]["fmcp_value"]),
        "minimum_weighted_value_equal": Fraction(
            independent["minimum_weighted_alpha1_CP1"]
        )
        == Fraction(frozen["minimum_weighted_channel_one_cp"]),
        "negative_count_equal": independent["negative_cells"]
        == frozen["negative_cells"],
        "alpha1_equal": Fraction(independent["alpha_1"])
        == Fraction(frozen["alpha_1"]),
        "lambda_equal": Fraction(independent["Lambda_n"])
        == Fraction(frozen["Lambda_n"]),
        "response_denominator_equal": independent["R_n"] == frozen["R_n"],
    }
    assert all(checks.values())
    payload = {
        "status": "post-hoc exact comparison after clean-room generation",
        "independent_input": str(args.independent),
        "frozen_input": str(args.frozen),
        "checks": checks,
        "all_checks_pass": True,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
