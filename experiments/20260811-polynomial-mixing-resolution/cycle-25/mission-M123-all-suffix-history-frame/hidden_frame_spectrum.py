#!/usr/bin/env python3
"""Exact principal-minor certificate for the M123 basin frame.

At local rank ``s`` let ``rho`` be the accepted root-composition law.  For
each active canonical endpoint ``e`` let ``B_e`` be its basin and

    c_e = len(e) rho(e),
    O_(e,f) = rho(B_e intersect B_f).

The basin analysis vectors in ``L2(rho)`` are

    v_e(C) = 1[C in B_e] / sqrt(c_e),

so their Gram matrix is ``G=C^(-1/2) O C^(-1/2)``.  The frame operator is
bounded by the identity exactly when ``C-O`` is positive semidefinite.

The earlier interrupted version expanded a full characteristic polynomial
by minors and was factorial-time at ``s=5``.  This replacement emits a
small exact rational principal-minor and Rayleigh certificate.  Floating
power iteration is retained only as a calibration and supports no sign.

Marked-space scope is deliberately explicit.  If a marked probability
space has a forgetful map whose pushforward is ``rho``, then pulling the
vectors back along that map is an isometry and preserves this Gram matrix.
This algebraic fact does not by itself construct the full success/failure
history space.  A success-only submeasure has a different Gram matrix.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import subprocess
from fractions import Fraction as F
from pathlib import Path


Composition = tuple[int, ...]
Matrix = tuple[tuple[F, ...], ...]


def record(value: F) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


@functools.cache
def weight(n: int) -> F:
    return F(n ** (n - 1), math.factorial(n))


@functools.cache
def compositions(n: int) -> tuple[Composition, ...]:
    if n == 0:
        return ((),)
    return tuple(
        (first,) + tail
        for first in range(1, n + 1)
        for tail in compositions(n - first)
    )


def rho(parts: Composition) -> F:
    return math.prod(weight(a) for a in parts) / (
        math.factorial(len(parts)) * weight(sum(parts) + 1)
    )


def active(endpoint: Composition) -> bool:
    return len(endpoint) >= 2 and endpoint[0] + endpoint[1] - 1 >= 2


def in_basin(source: Composition, endpoint: Composition) -> bool:
    merged, tail = endpoint[0], endpoint[1:]
    return any(
        sum(source[:cut]) == merged and source[cut:] == tail
        for cut in range(1, len(source) + 1)
    )


def determinant(matrix: Matrix) -> F:
    """Fraction-preserving Gaussian-elimination determinant."""
    n = len(matrix)
    if n == 0:
        return F(1)
    work = [list(row) for row in matrix]
    answer = F(1)
    sign = 1
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if work[row][column]), None
        )
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        answer *= pivot_value
        for row in range(column + 1, n):
            if not work[row][column]:
                continue
            factor = work[row][column] / pivot_value
            for j in range(column + 1, n):
                work[row][j] -= factor * work[column][j]
            work[row][column] = F(0)
    return sign * answer


def principal(matrix: Matrix, indices: tuple[int, ...]) -> Matrix:
    return tuple(tuple(matrix[i][j] for j in indices) for i in indices)


def principal_minor_audit(matrix: Matrix, maximum_size: int) -> dict:
    checked = 0
    negative = []
    zero = 0
    for size in range(1, min(maximum_size, len(matrix)) + 1):
        for indices in itertools.combinations(range(len(matrix)), size):
            value = determinant(principal(matrix, indices))
            checked += 1
            if value < 0:
                negative.append(
                    {"indices": list(indices), "determinant": record(value)}
                )
            elif value == 0:
                zero += 1
    return {
        "maximum_size": min(maximum_size, len(matrix)),
        "checked": checked,
        "negative_count": len(negative),
        "zero_count": zero,
        "first_negative": negative[0] if negative else None,
    }


def frame_data(s: int):
    atoms = compositions(s)
    endpoints = tuple(row for row in atoms if active(row))
    masses = {row: rho(row) for row in atoms}
    assert sum(masses.values(), F(0)) == 1
    capacities = tuple(len(endpoint) * masses[endpoint] for endpoint in endpoints)
    overlap = tuple(
        tuple(
            sum(
                (
                    masses[source]
                    for source in atoms
                    if in_basin(source, left) and in_basin(source, right)
                ),
                F(0),
            )
            for right in endpoints
        )
        for left in endpoints
    )
    defect = tuple(
        tuple(
            (capacities[i] if i == j else F(0)) - overlap[i][j]
            for j in range(len(endpoints))
        )
        for i in range(len(endpoints))
    )
    return atoms, endpoints, capacities, overlap, defect


def approximate_largest_gram(
    capacities: tuple[F, ...], overlap: Matrix, iterations: int = 250
) -> float:
    """Symmetric power iteration; calibration only, never an exact sign."""
    n = len(capacities)
    if not n:
        return 0.0
    matrix = [
        [
            float(overlap[i][j])
            / math.sqrt(float(capacities[i] * capacities[j]))
            for j in range(n)
        ]
        for i in range(n)
    ]
    vector = [1 / math.sqrt(n)] * n
    for _ in range(iterations):
        image = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
        norm = math.sqrt(sum(value * value for value in image))
        vector = [value / norm for value in image]
    image = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
    return sum(vector[i] * image[i] for i in range(n))


def dot_quadratic(vector: tuple[F, ...], matrix: Matrix) -> F:
    return sum(
        (
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        F(0),
    )


def exact_s5_certificate() -> dict:
    _, endpoints, capacities, overlap, defect = frame_data(5)
    selected = ((1, 3, 1), (2, 2, 1), (3, 1, 1), (4, 1))
    indices = tuple(endpoints.index(endpoint) for endpoint in selected)
    local_capacity = tuple(capacities[index] for index in indices)
    local_overlap = principal(overlap, indices)
    local_defect = principal(defect, indices)
    vector = (F(1, 2), F(5, 7), F(41, 49), F(1))
    defect_energy = dot_quadratic(vector, local_defect)
    capacity_norm = sum(
        (vector[i] * vector[i] * local_capacity[i] for i in range(4)), F(0)
    )
    overlap_energy = dot_quadratic(vector, local_overlap)

    assert local_defect == (
        (F(5, 108), F(0), F(0), F(-5, 216)),
        (F(0), F(35, 1296), F(0), F(-25, 1296)),
        (F(0), F(0), F(49, 1296), F(-41, 1296)),
        (F(-5, 216), F(-25, 1296), F(-41, 1296), F(4, 81)),
    )
    assert determinant(local_defect) == F(-27125, 235092492288)
    assert defect_energy == F(-155, 63504)
    assert capacity_norm == F(2094265, 6223392)
    assert overlap_energy == F(2109455, 6223392)
    assert overlap_energy / capacity_norm == F(421891, 418853) > 1

    return {
        "s": 5,
        "selected_endpoints": [list(endpoint) for endpoint in selected],
        "indices_in_full_active_order": list(indices),
        "capacities": [record(value) for value in local_capacity],
        "C_minus_O": [[record(value) for value in row] for row in local_defect],
        "determinant_C_minus_O": record(determinant(local_defect)),
        "rational_test_vector": [record(value) for value in vector],
        "xT_C_minus_O_x": record(defect_energy),
        "xT_C_x": record(capacity_norm),
        "xT_O_x": record(overlap_energy),
        "exact_gram_rayleigh_quotient": record(overlap_energy / capacity_norm),
        "conclusion": (
            "C-O is not positive semidefinite, hence the basin Gram matrix "
            "has an eigenvalue strictly greater than one"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = []
    for s in range(2, 6):
        atoms, endpoints, capacities, overlap, defect = frame_data(s)
        # All principal minors certify PSD through s=4.  At s=5, retain the
        # exact search fact that no principal obstruction occurs below size 4.
        audit = principal_minor_audit(defect, len(endpoints) if s <= 4 else 3)
        assert audit["negative_count"] == 0
        rows.append(
            {
                "s": s,
                "atom_count": len(atoms),
                "active_coordinate_count": len(endpoints),
                "active_endpoints": [list(endpoint) for endpoint in endpoints],
                "principal_minor_audit": audit,
                "largest_gram_eigenvalue_float_calibration": approximate_largest_gram(
                    capacities, overlap
                ),
            }
        )

    certificate = exact_s5_certificate()
    payload = {
        "claim_tested": (
            "the canonical-basin analysis frame has operator at most the identity"
        ),
        "status": "refuted",
        "first_exact_failure_rank": 5,
        "arithmetic": "fractions.Fraction; exact Gaussian determinants and Rayleigh quotient",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "repository_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "rows": rows,
        "exact_certificate": certificate,
        "marked_pullback_audit": {
            "proved_abstract_lemma": (
                "If kappa_*mu=rho and marked vectors are v_e composed with kappa "
                "with unchanged capacities c_e, pullback is an isometry and the "
                "Gram matrix is exactly unchanged."
            ),
            "natural_full_space_consequence": (
                "Any complete marked frame satisfying that full-space normalization "
                "and containing the root reset coordinates inherits the s=5 failure."
            ),
            "qualification": (
                "The existing success_history_stats recursion aggregates only the "
                "success submeasure of mass q.  It does not construct a full "
                "success/failure probability space or compute cross-prefix Gram entries."
            ),
            "different_operator_not_decided": (
                "A success-weighted pullback has overlaps sum_C rho(C) h(C) "
                "1_Be(C)1_Bf(C), not O_(e,f); that operator is not computed here "
                "and does not reproduce the same Bessel identity without extra work."
            ),
        },
        "scope_warning": (
            "This refutes the natural universal Bessel/frame shortcut only.  It does "
            "not refute H<=q(1-q), any all-L contraction, a Pbar gap, ROOT-MEAN LIFT, "
            "the original heat-bath gap, or either terminal outcome."
        ),
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "status": payload["status"],
                "first_exact_failure_rank": payload["first_exact_failure_rank"],
                "exact_rayleigh_quotient": certificate[
                    "exact_gram_rayleigh_quotient"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
