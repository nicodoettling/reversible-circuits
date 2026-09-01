#!/usr/bin/env python3
"""Audit finite H2 curvature and the exact higher-core correction budget."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[4]
M125_RESULTS = (
    REPOSITORY
    / "experiments/20260811-polynomial-mixing-resolution/cycle-26"
    / "mission-M125-defect-mass-no-valley/exact_results.json"
)
M133_RESULTS = (
    REPOSITORY
    / "experiments/20260811-polynomial-mixing-resolution/cycle-28"
    / "mission-M133-defect-coefficient-no-valley/core_profile_results.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return "unavailable"


def frac_record(value: Fraction) -> dict:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h2-results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.h2_results = args.h2_results.resolve()
    args.output = args.output.resolve()
    h2_payload = json.loads(args.h2_results.read_text())
    m125_payload = json.loads(M125_RESULTS.read_text())
    m133_payload = json.loads(M133_RESULTS.read_text())
    h2 = {
        record["d"]: {
            int(cycles): int(value)
            for cycles, value in record["masses_by_cycles"].items()
        }
        for record in h2_payload["records"]
    }
    full = {
        record["d"]: {
            record["d"] - defect: int(value)
            for defect, value in enumerate(record["raw_integer_masses"])
        }
        for record in m125_payload["cases"]
    }
    m133_h2 = {
        record["d"]: {
            int(cycles): int(value)
            for cycles, value in record["masses_by_core_and_cycles"]["2"].items()
        }
        for record in m133_payload["records"]
    }
    reference_checks = [
        {"d": d, "match": h2[d] == values}
        for d, values in sorted(m133_h2.items())
    ]
    failures = []
    first_shifted_ulc_failure = None
    first_inverse_linear_failure = None
    first_inverse_square_failure = None
    weakest_h2_ratio = None
    weakest_full_budget = None
    largest_correction_ratio = None
    records = []
    for d, row in sorted(h2.items()):
        checks = []
        if d not in full:
            failures.append({"d": d, "reason": "missing full accepted row"})
            continue
        for cycles in range(3, d):
            centre = row[cycles]
            side_product = row[cycles - 1] * row[cycles + 1]
            ratio = Fraction(centre * centre, side_product)
            margin = centre * centre - side_product
            shifted_index = cycles - 2
            shifted_degree = d - 2
            ulc_margin = (
                shifted_index
                * (shifted_degree - shifted_index)
                * centre
                * centre
                - (shifted_index + 1)
                * (shifted_degree - shifted_index + 1)
                * side_product
            )
            inverse_linear_margin = d * centre * centre - (d + 1) * side_product
            inverse_square_margin = d * d * centre * centre - (d * d + 1) * side_product
            correction = {
                value: Fraction(full[d][value], row[value])
                for value in (cycles - 1, cycles, cycles + 1)
            }
            correction_ratio = (
                correction[cycles - 1]
                * correction[cycles + 1]
                / correction[cycles] ** 2
            )
            budget_ratio = ratio / correction_ratio
            item = {
                "cycles": cycles,
                "h2_margin": str(margin),
                "h2_ratio": frac_record(ratio),
                "shifted_ulc_margin": str(ulc_margin),
                "inverse_linear_margin": str(inverse_linear_margin),
                "inverse_square_margin": str(inverse_square_margin),
                "higher_core_correction_ratio": frac_record(correction_ratio),
                "full_budget_ratio": frac_record(budget_ratio),
            }
            checks.append(item)
            indexed = {"d": d, **item}
            if margin < 0:
                failures.append({"d": d, "cycles": cycles, "reason": "H2 LC"})
            if ulc_margin < 0 and first_shifted_ulc_failure is None:
                first_shifted_ulc_failure = indexed
            if inverse_linear_margin < 0 and first_inverse_linear_failure is None:
                first_inverse_linear_failure = indexed
            if inverse_square_margin < 0 and first_inverse_square_failure is None:
                first_inverse_square_failure = indexed
            if weakest_h2_ratio is None or ratio < Fraction(
                int(weakest_h2_ratio["h2_ratio"]["numerator"]),
                int(weakest_h2_ratio["h2_ratio"]["denominator"]),
            ):
                weakest_h2_ratio = indexed
            if weakest_full_budget is None or budget_ratio < Fraction(
                int(weakest_full_budget["full_budget_ratio"]["numerator"]),
                int(weakest_full_budget["full_budget_ratio"]["denominator"]),
            ):
                weakest_full_budget = indexed
            if largest_correction_ratio is None or correction_ratio > Fraction(
                int(largest_correction_ratio["higher_core_correction_ratio"]["numerator"]),
                int(largest_correction_ratio["higher_core_correction_ratio"]["denominator"]),
            ):
                largest_correction_ratio = indexed
        records.append({"d": d, "checks": checks})
    payload = {
        "claim_scope": (
            "exact finite curvature diagnostics only; no finite sign proves "
            "universal H2 or full coefficient log-concavity"
        ),
        "target": (
            "H2[d,c]^2/(H2[d,c-1]H2[d,c+1]) versus the exact "
            "higher-core correction E[d,c-1]E[d,c+1]/E[d,c]^2"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "inputs": {
            "h2_results": str(args.h2_results.relative_to(REPOSITORY)),
            "h2_results_sha256": sha256(args.h2_results),
            "m125_results": str(M125_RESULTS.relative_to(REPOSITORY)),
            "m125_results_sha256": sha256(M125_RESULTS),
            "m133_results": str(M133_RESULTS.relative_to(REPOSITORY)),
            "m133_results_sha256": sha256(M133_RESULTS),
        },
        "reference_checks": reference_checks,
        "reference_failure_count": sum(not item["match"] for item in reference_checks),
        "h2_log_concavity_failure_count": len(failures),
        "h2_log_concavity_failures": failures,
        "first_shifted_ulc_failure": first_shifted_ulc_failure,
        "first_inverse_linear_surplus_failure": first_inverse_linear_failure,
        "first_inverse_square_surplus_failure": first_inverse_square_failure,
        "weakest_h2_ratio": weakest_h2_ratio,
        "largest_higher_core_correction_ratio": largest_correction_ratio,
        "weakest_full_budget_ratio": weakest_full_budget,
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"reference_failures={payload['reference_failure_count']} "
        f"h2_failures={payload['h2_log_concavity_failure_count']}"
    )
    print(f"first_shifted_ulc_failure={first_shifted_ulc_failure and (first_shifted_ulc_failure['d'], first_shifted_ulc_failure['cycles'])}")
    print(f"first_inverse_linear_failure={first_inverse_linear_failure and (first_inverse_linear_failure['d'], first_inverse_linear_failure['cycles'])}")
    print(f"first_inverse_square_failure={first_inverse_square_failure and (first_inverse_square_failure['d'], first_inverse_square_failure['cycles'])}")
    print(f"weakest_h2_ratio={weakest_h2_ratio and weakest_h2_ratio['h2_ratio']['decimal']}")
    print(f"weakest_full_budget={weakest_full_budget and weakest_full_budget['full_budget_ratio']['decimal']}")
    print(f"wrote {args.output} sha256={sha256(args.output)}")


if __name__ == "__main__":
    main()
