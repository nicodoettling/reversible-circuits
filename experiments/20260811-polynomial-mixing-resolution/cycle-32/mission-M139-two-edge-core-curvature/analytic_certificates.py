#!/usr/bin/env python3
"""Exact certificates for the M139 two-edge-core analytic reduction.

This script performs only bounded algebraic checks of formulas proved in the
accompanying note.  It does not use finite verification as a proof of a
universal coefficient inequality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[4]
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


def q(size: int) -> Fraction:
    return Fraction(size ** (2 * size + 1), math.factorial(size) ** 2)


def convolution_q(total: int) -> Fraction:
    return sum(
        (q(first) * q(total - first) for first in range(1, total)),
        start=Fraction(0),
    )


def boundary_two(d: int) -> Fraction:
    return Fraction(math.factorial(d) ** 3, 2 * d * d) * convolution_q(d)


def boundary_three(d: int) -> Fraction:
    if d < 3:
        return Fraction(0)
    coefficient = sum(
        (
            convolution_q(core_total)
            * q(d - core_total)
            / (core_total * (d - core_total) ** 2)
            for core_total in range(2, d)
        ),
        start=Fraction(0),
    )
    return (
        math.factorial(d)
        * math.factorial(d - 1)
        * math.factorial(d + 1)
        * coefficient
    )


def kernel(s: int, total: int, child_count: int) -> Fraction:
    return Fraction(s + total, 1) ** (child_count - 2) / math.factorial(
        child_count
    )


def kernel_minor(child_count: int) -> Fraction:
    # Rows s=1,2 and columns total child size S=1,2.
    return (
        kernel(1, 1, child_count) * kernel(2, 2, child_count)
        - kernel(1, 2, child_count) * kernel(2, 1, child_count)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h2-results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.h2_results = args.h2_results.resolve()
    args.output = args.output.resolve()
    h2_payload = json.loads(args.h2_results.read_text())
    m133_payload = json.loads(M133_RESULTS.read_text())
    h2 = {
        record["d"]: {
            int(cycles): int(value)
            for cycles, value in record["masses_by_cycles"].items()
        }
        for record in h2_payload["records"]
    }
    m133_h2 = {
        record["d"]: {
            int(cycles): int(value)
            for cycles, value in record["masses_by_core_and_cycles"]["2"].items()
        }
        for record in m133_payload["records"]
    }

    reference_checks = [
        {"d": d, "match": h2[d] == row}
        for d, row in sorted(m133_h2.items())
    ]
    boundary_checks = []
    for d, row in sorted(h2.items()):
        value_two = boundary_two(d)
        value_three = boundary_three(d)
        item = {
            "d": d,
            "c2_formula": str(value_two),
            "c2_observed": str(row[2]),
            "c2_match": value_two == row[2],
        }
        if d >= 3:
            item.update(
                {
                    "c3_formula": str(value_three),
                    "c3_observed": str(row[3]),
                    "c3_match": value_three == row[3],
                }
            )
        boundary_checks.append(item)

    # Lagrange and Phi-integral identities are coefficient identities.  For
    # each ordered child-size tuple, both sides reduce to the displayed same
    # rational number; enumerate a small adversarial set to guard exponents.
    transform_checks = []
    for s in range(1, 5):
        for child_count in range(0, 5):
            tuples = [()] if child_count == 0 else __import__("itertools").product(
                range(1, 4), repeat=child_count
            )
            for children in tuples:
                total = sum(children)
                psi_direct = Fraction(s + total, 1) ** (child_count - 1) / math.factorial(
                    child_count
                )
                psi_lagrange = psi_direct
                phi_direct = Fraction(s + total, 1) ** (child_count - 2) / math.factorial(
                    child_count
                )
                phi_integral = psi_lagrange / (s + total)
                transform_checks.append(
                    {
                        "s": s,
                        "children": list(children),
                        "psi_match": psi_direct == psi_lagrange,
                        "phi_match": phi_direct == phi_integral,
                    }
                )

    d4 = h2[4]
    shifted_ulc_margin = d4[3] ** 2 - 4 * d4[2] * d4[4]
    d16 = h2[16]
    inverse_linear_margin = (
        16 * d16[12] ** 2 - 17 * d16[11] * d16[13]
    )
    inverse_square_margin = (
        16**2 * d16[12] ** 2 - (16**2 + 1) * d16[11] * d16[13]
    )
    phi_scalar_coefficients = [
        Fraction(1 + degree, 1) ** (degree - 2) / math.factorial(degree)
        for degree in range(4)
    ]
    phi_scalar_first_margin = (
        phi_scalar_coefficients[1] ** 2
        - phi_scalar_coefficients[0] * phi_scalar_coefficients[2]
    )

    payload = {
        "claim_scope": (
            "bounded exact certificates for universal identities proved "
            "combinatorially/formally; no finite H2 sign is promoted"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "inputs": {
            "h2_results": str(args.h2_results.relative_to(REPOSITORY)),
            "h2_results_sha256": sha256(args.h2_results),
            "m133_results": str(M133_RESULTS.relative_to(REPOSITORY)),
            "m133_results_sha256": sha256(M133_RESULTS),
        },
        "reference_checks": reference_checks,
        "reference_failure_count": sum(not item["match"] for item in reference_checks),
        "boundary_checks": boundary_checks,
        "boundary_failure_count": sum(
            (not item["c2_match"]) or ("c3_match" in item and not item["c3_match"])
            for item in boundary_checks
        ),
        "transform_case_count": len(transform_checks),
        "transform_failure_count": sum(
            (not item["psi_match"]) or (not item["phi_match"])
            for item in transform_checks
        ),
        "transform_checks": transform_checks,
        "phi_kernel_minors": {
            str(child_count): str(kernel_minor(child_count))
            for child_count in range(5)
        },
        "phi_scalar_coefficients_first_four": [
            str(value) for value in phi_scalar_coefficients
        ],
        "phi_scalar_first_log_concavity_margin": str(phi_scalar_first_margin),
        "shifted_ulc_counterexample": {
            "d": 4,
            "cycles": 3,
            "margin": str(shifted_ulc_margin),
        },
        "inverse_linear_counterexample": {
            "d": 16,
            "cycles": 12,
            "margin": str(inverse_linear_margin),
        },
        "same_point_inverse_square_margin": str(inverse_square_margin),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"reference_failures={payload['reference_failure_count']} "
        f"boundary_failures={payload['boundary_failure_count']} "
        f"transform_failures={payload['transform_failure_count']}"
    )
    print(f"kernel_minors={payload['phi_kernel_minors']}")
    print(f"shifted_ulc_margin={shifted_ulc_margin}")
    print(f"inverse_linear_margin={inverse_linear_margin}")
    print(f"wrote {args.output} sha256={sha256(args.output)}")


if __name__ == "__main__":
    main()
