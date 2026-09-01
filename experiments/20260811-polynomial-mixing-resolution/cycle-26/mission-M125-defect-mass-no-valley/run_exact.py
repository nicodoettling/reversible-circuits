#!/usr/bin/env python3
"""Reproducible CLI for the exact M125 defect-species coefficient engine."""

from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction
from pathlib import Path

import defect_species as core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=list(range(2, 12)))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-types", action="store_true")
    parser.add_argument("--numeric-roots", action="store_true")
    args = parser.parse_args()
    if any(d < 2 for d in args.d):
        raise SystemExit("all d must be at least 2")

    started = time.time()
    cases = []
    for d in args.d:
        case_started = time.time()
        row, type_records = core.defect_row(d)
        primitive_row, divisor = core.primitive(row)
        record = {
            "d": d,
            "raw_integer_masses": row,
            "primitive_integer_masses": primitive_row,
            "common_gcd": divisor,
            "total_mass": sum(row),
            "checks": core.sequence_checks(row),
            "elapsed_seconds": time.time() - case_started,
        }
        if args.numeric_roots:
            record["defect_polynomial_roots_numeric"] = core.polynomial_roots(row)
        if args.include_types:
            record["cycle_type_contributions"] = type_records
        cases.append(record)
        print(
            f"d={d} mode={record['checks']['mode_interval']} "
            f"unimodal={record['checks']['unimodal']} "
            f"LC={record['checks']['log_concave']} "
            f"ULC={record['checks']['ultra_log_concave']}",
            flush=True,
        )

    lc_candidates: list[tuple[Fraction, int, int]] = []
    first_ulc_failure = None
    for case in cases:
        row = case["raw_integer_masses"]
        for r in range(1, len(row) - 1):
            lc_candidates.append(
                (Fraction(row[r] ** 2, row[r - 1] * row[r + 1]), case["d"], r)
            )
        if first_ulc_failure is None and not case["checks"]["ultra_log_concave"]:
            margins = case["checks"]["ulc_cleared_margins"]
            first_bad = next(index for index, value in enumerate(margins, 1) if value < 0)
            first_ulc_failure = {"d": case["d"], "r": first_bad}
    weakest = min(lc_candidates, default=None)
    finite_summary = {
        "all_rows_unimodal": all(case["checks"]["unimodal"] for case in cases),
        "all_rows_log_concave": all(
            case["checks"]["log_concave"] for case in cases
        ),
        "first_ulc_failure": first_ulc_failure,
        "weakest_ordinary_lc_ratio": None,
    }
    if weakest is not None:
        ratio, d_weak, r_weak = weakest
        finite_summary["weakest_ordinary_lc_ratio"] = {
            "d": d_weak,
            "r": r_weak,
            "numerator": str(ratio.numerator),
            "denominator": str(ratio.denominator),
            "float": float(ratio),
        }

    payload = {
        "claim_scope": (
            "exact coefficient evaluation from the M113 cell formula; finite "
            "sequence checks do not prove a universal no-valley statement"
        ),
        "target": "M[d,r]=sum_{R(kappa)=r}|C_kappa| for rho(kappa)=|C_kappa|/Z_inc",
        "coefficient_method": (
            "integer cycle types + weighted partition polynomial + exact rooted "
            "multiset-aggregated connected recurrence; retain only L+R=c"
        ),
        "git_commit": core.git_commit(),
        "python": core.platform.python_version(),
        "numpy": None,
        "seed": None,
        "arguments": {
            "d": args.d,
            "output": str(args.output),
            "include_types": args.include_types,
            "numeric_roots": args.numeric_roots,
        },
        "finite_summary": finite_summary,
        "cases": cases,
        "elapsed_seconds": time.time() - started,
    }
    try:
        import numpy as np

        payload["numpy"] = np.__version__
    except ImportError:
        pass
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output} sha256={core.sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
