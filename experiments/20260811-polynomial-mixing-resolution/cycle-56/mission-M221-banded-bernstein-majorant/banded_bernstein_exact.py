#!/usr/bin/env python3
"""Standalone exact M221 bandwidth-one Bernstein certificate.

Standard library only.  The checker reconstructs the single actual kernel
from the grouped Cayley-root recursion and reads no predecessor artifact.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


Poly = tuple[Q, ...]
Kernel = dict[tuple[int, int], Q]
Matrix = list[list[Q]]


def trim(poly: list[Q] | tuple[Q, ...]) -> Poly:
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def padd(left: Poly, right: Poly) -> Poly:
    out = [Q(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def pscale(poly: Poly, scalar: Q) -> Poly:
    return trim([scalar * value for value in poly])


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def monomial(degree: int, coefficient: Q = Q(1)) -> Poly:
    return (Q(0),) * degree + (coefficient,)


def kclean(kernel: Kernel) -> Kernel:
    return {key: value for key, value in kernel.items() if value}


def kadd(left: Kernel, right: Kernel) -> Kernel:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Q(0)) + value
    return kclean(out)


def kscale(kernel: Kernel, scalar: Q) -> Kernel:
    return kclean({key: scalar * value for key, value in kernel.items()})


def outer(left: Poly, right: Poly) -> Kernel:
    return kclean({
        (i, j): x * y
        for i, x in enumerate(left)
        for j, y in enumerate(right)
    })


def lift(kernel: Kernel, likelihood: Poly) -> Kernel:
    out: Kernel = {}
    for (i, j), value in kernel.items():
        for a, x in enumerate(likelihood):
            for b, y in enumerate(likelihood):
                key = (i + a, j + b)
                out[key] = out.get(key, Q(0)) + value * x * y
    return kclean(out)


def rising(start: int, length: int) -> int:
    return math.prod(range(start, start + length))


def beta_moment(kappa: int, deficit: int, degree: int) -> Q:
    return Q(rising(deficit, degree), rising(kappa, degree))


def beta_expect(poly: Poly, kappa: int, deficit: int) -> Q:
    return sum(
        (coefficient * beta_moment(kappa, deficit, degree)
         for degree, coefficient in enumerate(poly)),
        Q(0),
    )


@functools.lru_cache(None)
def tree_weight(size: int) -> Q:
    return Q(size ** (size - 1), math.factorial(size))


def split_probability(total: int, bottom: int) -> Q:
    return (
        tree_weight(total + 1 - bottom)
        * tree_weight(bottom)
        / tree_weight(total + 1)
    )


@functools.lru_cache(None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    return tuple(
        (first,) + tail
        for first in range(1, total + 1)
        for tail in compositions(total - first)
    )


def root_mass(source: tuple[int, ...]) -> Q:
    return math.prod(tree_weight(part) for part in source) / (
        math.factorial(len(source)) * tree_weight(sum(source) + 1)
    )


def reaches(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.lru_cache(None)
def basin_structure(total: int) -> tuple[
    tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...
]:
    sources = compositions(total)
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    }, key=lambda row: (len(row), row))
    return tuple(
        (endpoint, tuple(source for source in sources if reaches(source, endpoint)))
        for endpoint in endpoints
    )


def point_current(source: tuple[int, ...], bottom: int) -> Poly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return monomial(degree - 1, Q(degree))
    q_child = split_probability(last - 1, bottom)
    out = [Q(0)] * (degree + 1)
    out[0], out[degree] = q_child, -q_child
    return trim(out)


@functools.lru_cache(None)
def reset_kernel(total: int, bottom: int) -> Kernel:
    q_parent = split_probability(total, bottom)
    result: Kernel = {}
    for endpoint, basin in basin_structure(total):
        current: Poly = (Q(0),)
        for source in basin:
            centered = padd(point_current(source, bottom), (Q(-q_parent),))
            current = padd(current, pscale(centered, root_mass(source)))
        capacity = Q(len(endpoint)) * root_mass(endpoint)
        result = kadd(
            result,
            kscale(outer(current, current), Q(1) / (q_parent * capacity)),
        )
    return result


@functools.lru_cache(None)
def cayley_composition_mass(total: int, parts: int) -> Q:
    if (total, parts) == (0, 0):
        return Q(1)
    if not 1 <= parts <= total:
        return Q(0)
    return Q(parts * total ** (total - parts), total * math.factorial(total - parts))


@functools.lru_cache(None)
def grouped_roots(total: int) -> tuple[tuple[int, int, Q], ...]:
    rows = []
    for degree in range(1, total + 1):
        for last in range(1, total + 1):
            mass = (
                tree_weight(last)
                * cayley_composition_mass(total - last, degree - 1)
                / (math.factorial(degree) * tree_weight(total + 1))
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return tuple(rows)


def bernstein(degree: int, index: int) -> Poly:
    out = [Q(0)] * (degree + 1)
    for extra in range(degree - index + 1):
        out[index + extra] = Q(
            math.comb(degree, index)
            * math.comb(degree - index, extra)
            * ((-1) ** extra)
        )
    return trim(out)


def attachment_mass(kappa: int, deficit: int, degree: int, observed: int) -> Q:
    return Q(
        math.comb(degree, observed)
        * rising(deficit, observed)
        * rising(kappa - deficit, degree - observed),
        rising(kappa, degree),
    )


@functools.lru_cache(None)
def history_kernel(total: int, kappa: int, deficit: int, bottom: int) -> Kernel:
    q_parent = split_probability(total, bottom)
    result = dict(reset_kernel(total, bottom))
    for degree, last, mass in grouped_roots(total):
        if last <= bottom or last - 1 < 2:
            continue
        eta = mass * split_probability(last - 1, bottom) / q_parent
        attachment = [
            attachment_mass(kappa, deficit, degree, observed)
            for observed in range(degree + 1)
        ]
        assert sum(attachment, Q(0)) == 1
        for observed in range(degree):  # observed=degree is killed exactly
            child = history_kernel(
                last - 1, kappa + degree, deficit + observed, bottom
            )
            contribution = lift(child, bernstein(degree, observed))
            result = kadd(
                result,
                kscale(contribution, eta / attachment[observed]),
            )
    return kclean(result)


def zero_matrix(size: int) -> Matrix:
    return [[Q(0) for _ in range(size)] for _ in range(size)]


def monomial_to_bernstein(kernel: Kernel, degree: int) -> Matrix:
    result = zero_matrix(degree + 1)
    for (i, j), value in kernel.items():
        assert i <= degree and j <= degree
        for a in range(i, degree + 1):
            left = Q(math.comb(a, i), math.comb(degree, i))
            for b in range(j, degree + 1):
                right = Q(math.comb(b, j), math.comb(degree, j))
                result[a][b] += value * left * right
    return result


def uniform_expect(poly: Poly) -> Q:
    return sum(
        (coefficient / Q(degree + 1)
         for degree, coefficient in enumerate(poly)),
        Q(0),
    )


def charge_matrix(degree: int) -> Matrix:
    features = [bernstein(degree, index) for index in range(degree + 1)]
    first = [
        uniform_expect(pmul((Q(-1, 2), Q(1)), feature))
        for feature in features
    ]
    return [
        [
            uniform_expect(pmul(features[i], features[j]))
            - 12 * first[i] * first[j]
            for j in range(degree + 1)
        ]
        for i in range(degree + 1)
    ]


def matrix_inner(left: Matrix, right: Matrix) -> Q:
    return sum(
        (left[i][j] * right[i][j]
         for i in range(len(left)) for j in range(len(left))),
        Q(0),
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def matrix_outer(vector: list[Q]) -> Matrix:
    return [[x * y for y in vector] for x in vector]


def matrix_bandwidth(matrix: Matrix) -> int:
    return max(
        (abs(i - j) for i in range(len(matrix)) for j in range(len(matrix))
         if matrix[i][j]),
        default=0,
    )


def strict_diagonal_dominance_margins(matrix: Matrix) -> list[Q]:
    return [
        matrix[i][i]
        - sum((abs(matrix[i][j]) for j in range(len(matrix)) if j != i), Q(0))
        for i in range(len(matrix))
    ]


def elevation_coefficients(source_degree: int, index: int, cap: int) -> list[Q]:
    out = [Q(0)] * (cap + 1)
    for target in range(index, index + cap - source_degree + 1):
        out[target] = Q(
            math.comb(source_degree, index)
            * math.comb(cap - source_degree, target - index),
            math.comb(cap, target),
        )
    return out


def elevate_vector(vector: list[Q], source_degree: int, cap: int) -> list[Q]:
    out = [Q(0)] * (cap + 1)
    for index, coefficient in enumerate(vector):
        elevation = elevation_coefficients(source_degree, index, cap)
        for target, value in enumerate(elevation):
            out[target] += coefficient * value
    return out


def qtext(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix_hash(matrix: Matrix) -> str:
    encoded = ";".join(
        f"{i},{j}:{value.numerator}/{value.denominator}"
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
    )
    return hashlib.sha256(encoded.encode()).hexdigest()


def kernel_hash(kernel: Kernel) -> str:
    encoded = ";".join(
        f"{i},{j}:{value.numerator}/{value.denominator}"
        for (i, j), value in sorted(kernel.items())
    )
    return hashlib.sha256(encoded.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    bottom, cap, kappa, deficit = 1, 6, 2, 1
    total = bottom + cap
    kernel = history_kernel(total, kappa, deficit, bottom)
    assert len(kernel) == 49
    actual = monomial_to_bernstein(kernel, cap)
    charge = charge_matrix(cap)
    assert all(actual[i][j] == actual[j][i] for i in range(7) for j in range(7))
    assert all(charge[i][j] == charge[j][i] for i in range(7) for j in range(7))

    q = split_probability(total, bottom)
    budget = 1 - q
    actual_t1 = matrix_inner(charge, actual)
    actual_slack = budget - actual_t1
    assert q == Q(117649, 262144)
    assert actual_t1 == Q(
        100831060869578347854833692341308821,
        459142800034351572282356269056000000,
    )
    assert actual_slack > 0

    # Exact width-zero dual obstruction.  X is PSD by the displayed
    # rank-one-plus-positive-diagonal decomposition and matches G on the band.
    signs = [-1, -1, -1, 1, 1, 1, 1]
    radii = [
        Q(1, 5), Q(4, 25), Q(17, 100), Q(9, 50),
        Q(17, 100), Q(4, 25), Q(1, 5),
    ]
    vector = [Q(sign) * radius for sign, radius in zip(signs, radii)]
    diagonal_weights = [charge[i][i] for i in range(7)]
    remainders = [
        diagonal_weights[i] - radii[i] ** 2 for i in range(7)
    ]
    assert all(value > 0 for value in remainders)
    dual_zero = matrix_outer(vector)
    for i, remainder in enumerate(remainders):
        dual_zero[i][i] += remainder
    assert [dual_zero[i][i] for i in range(7)] == diagonal_weights
    dual_zero_objective = matrix_inner(actual, dual_zero)
    dual_zero_excess = dual_zero_objective - budget
    assert dual_zero_excess == Q(
        1000948704365931347999936328408157889213,
        48209994003606915089647408250880000000000,
    )
    assert dual_zero_excess > 0

    # Compact exact width-one primal certificate.
    primal_one = zero_matrix(7)
    diagonal = [
        Q(101, 50), Q(111, 100), Q(43, 100), Q(19, 25),
        Q(39, 25), Q(99, 50), Q(21, 5),
    ]
    adjacent = [Q(1, 3), Q(2, 15), Q(1, 12), Q(1, 5), Q(3, 5), Q(11, 8)]
    for i, value in enumerate(diagonal):
        primal_one[i][i] = value
    for i, value in enumerate(adjacent):
        primal_one[i][i + 1] = primal_one[i + 1][i] = value
    assert matrix_bandwidth(primal_one) == 1

    domination_residual = matrix_subtract(primal_one, actual)
    primal_margins = strict_diagonal_dominance_margins(primal_one)
    residual_margins = strict_diagonal_dominance_margins(domination_residual)
    assert all(value > 0 for value in primal_margins)
    assert all(value > 0 for value in residual_margins)
    # Symmetric strict diagonal dominance with positive diagonal proves PD.
    assert all(primal_one[i][i] > 0 for i in range(7))
    assert all(domination_residual[i][i] > 0 for i in range(7))

    primal_one_charge = matrix_inner(charge, primal_one)
    primal_one_slack = budget - primal_one_charge
    assert primal_one_charge == Q(4937603, 9172800)
    assert primal_one_slack == Q(485323987, 37571788800)
    assert primal_one_slack > 0

    # Raw retained-lift stability.  Saturation shifts indices and preserves
    # bandwidth.  Unsaturated elevation can increase w to w+(L-n).
    saturated_checks = 0
    unsaturated_bound_checks = 0
    for likelihood_degree in range(1, cap + 1):
        for child_degree in range(cap - likelihood_degree + 1):
            combined = likelihood_degree + child_degree
            for i in range(child_degree + 1):
                for j in range(child_degree + 1):
                    if abs(i - j) > 1:
                        continue
                    for observed in range(likelihood_degree + 1):
                        left_index = observed + i
                        right_index = observed + j
                        if combined == cap:
                            assert abs(left_index - right_index) <= 1
                            saturated_checks += 1
                        else:
                            left_support = [
                                r for r, value in enumerate(
                                    elevation_coefficients(combined, left_index, cap)
                                ) if value
                            ]
                            right_support = [
                                r for r, value in enumerate(
                                    elevation_coefficients(combined, right_index, cap)
                                ) if value
                            ]
                            assert max(
                                abs(r - s) for r in left_support for s in right_support
                            ) <= 1 + (cap - combined)
                            unsaturated_bound_checks += 1

    # Concrete retained d=1,a=0 lift of the width-one child rank-one vector
    # (1,1): after multiplication its degree-two vector is (1,1/2,0).
    lifted_degree_two = [Q(1), Q(1, 2), Q(0)]
    elevated = elevate_vector(lifted_degree_two, 2, 6)
    expected_elevated = [
        Q(1), Q(5, 6), Q(2, 3), Q(1, 2), Q(1, 3), Q(1, 6), Q(0)
    ]
    assert elevated == expected_elevated
    elevated_outer = matrix_outer(elevated)
    assert matrix_bandwidth(elevated_outer) == 5

    # A coarse positive-linear stabilization always exists for PSD M:
    # Env(M)=Tr(M)I >= M.  It lands in bandwidth zero, but no budget claim is
    # made for this envelope.
    stability = {
        "saturated_bandwidth_one_checks": saturated_checks,
        "unsaturated_bandwidth_upper_bound_checks": unsaturated_bound_checks,
        "raw_fixed_width_one_closed": False,
        "counterexample_child_degree": 1,
        "counterexample_likelihood_d_a": [1, 0],
        "counterexample_combined_degree": 2,
        "counterexample_elevated_vector": [qtext(value) for value in elevated],
        "counterexample_output_bandwidth": matrix_bandwidth(elevated_outer),
        "general_raw_upper_bound": "w+(L-n), capped at L",
        "coarse_positive_linear_envelope": "Env(M)=Tr(M) I >=_PSD M",
        "cost_controlled_width_one_recursive_envelope": "unresolved",
    }

    payload = {
        "schema": "M221-banded-Bernstein-majorant-v1",
        "python": platform.python_version(),
        "seed": None,
        "method": "one exact Fraction row; grouped Cayley roots; no predecessor import/data",
        "state_B_L_kappa_D": [bottom, cap, kappa, deficit],
        "conic_program": {
            "primal": "min <G,C>: C-A PSD, C_ij=0 for |i-j|>w",
            "dual": "max <A,X>: X PSD, X_ij=G_ij for |i-j|<=w",
            "strong_duality_reason": "strict primal point C=tI for sufficiently large rational t",
        },
        "reconstruction": {
            "kernel_terms": len(kernel),
            "kernel_sha256": kernel_hash(kernel),
            "actual_coefficient_sha256": matrix_hash(actual),
            "charge_matrix_sha256": matrix_hash(charge),
            "eta_over_pi": True,
            "killed_a_equals_d_absent": True,
        },
        "width_zero_dual_obstruction": {
            "dual_matrix_sha256": matrix_hash(dual_zero),
            "diagonal_matches_G": True,
            "psd_reason": "X=vv^T+diag(strictly positive remainders)",
            "diagonal_remainders": [qtext(value) for value in remainders],
            "objective": qtext(dual_zero_objective),
            "positive_excess_over_budget": qtext(dual_zero_excess),
        },
        "width_one_primal_certificate": {
            "matrix_sha256": matrix_hash(primal_one),
            "diagonal": [qtext(value) for value in diagonal],
            "adjacent_offdiagonal": [qtext(value) for value in adjacent],
            "bandwidth": matrix_bandwidth(primal_one),
            "C_strict_diagonal_dominance_margins": [
                qtext(value) for value in primal_margins
            ],
            "minimum_C_strict_diagonal_dominance_margin": qtext(min(primal_margins)),
            "C_minus_A_sha256": matrix_hash(domination_residual),
            "C_minus_A_strict_diagonal_dominance_margins": [
                qtext(value) for value in residual_margins
            ],
            "minimum_C_minus_A_strict_diagonal_dominance_margin": qtext(
                min(residual_margins)
            ),
            "psd_reason": "C and C-A are symmetric strictly diagonally dominant with positive diagonal",
            "charge": qtext(primal_one_charge),
            "positive_budget_slack": qtext(primal_one_slack),
        },
        "least_feasible_bandwidth": 1,
        "actual_kernel": {
            "q": qtext(q),
            "budget": qtext(budget),
            "T1": qtext(actual_t1),
            "positive_actual_slack": qtext(actual_slack),
        },
        "lift_stability": stability,
        "all_checks_pass": True,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "all_checks_pass": True,
        "output": str(args.output),
        "output_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "least_feasible_bandwidth": 1,
        "width_zero_dual_excess": qtext(dual_zero_excess),
        "width_one_budget_slack": qtext(primal_one_slack),
        "raw_width_one_closed_under_unsaturated_lifts": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

