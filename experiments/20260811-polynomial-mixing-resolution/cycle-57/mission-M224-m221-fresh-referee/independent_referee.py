#!/usr/bin/env python3
"""Clean-room exact referee reconstruction for the single M224 audit row.

This script reads no predecessor artifact and imports no project code.  It uses
literal ordered compositions for root masses and exact Gaussian elimination
for the Bernstein coefficient matrix, deliberately differing from the frozen
source implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path


Poly = tuple[F, ...]
Kernel = dict[tuple[int, int], F]
Matrix = list[list[F]]


def trim(poly: list[F] | tuple[F, ...]) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_add(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * max(len(left), len(right))
    for degree, value in enumerate(left):
        out[degree] += value
    for degree, value in enumerate(right):
        out[degree] += value
    return trim(out)


def poly_scale(poly: Poly, scalar: F) -> Poly:
    return trim([scalar * value for value in poly])


def poly_mul(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def monomial(degree: int, coefficient: F = F(1)) -> Poly:
    return (F(0),) * degree + (coefficient,)


def bernstein(degree: int, index: int) -> Poly:
    """Return C(degree,index) u^index (1-u)^(degree-index)."""
    assert 0 <= index <= degree
    out = [F(0)] * (degree + 1)
    for extra in range(degree - index + 1):
        out[index + extra] = F(
            math.comb(degree, index)
            * math.comb(degree - index, extra)
            * ((-1) ** extra)
        )
    return trim(out)


def clean_kernel(kernel: Kernel) -> Kernel:
    return {key: value for key, value in kernel.items() if value}


def kernel_add(left: Kernel, right: Kernel) -> Kernel:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, F(0)) + value
    return clean_kernel(out)


def kernel_scale(kernel: Kernel, scalar: F) -> Kernel:
    return clean_kernel({key: scalar * value for key, value in kernel.items()})


def outer(left: Poly, right: Poly) -> Kernel:
    return clean_kernel({
        (i, j): x * y
        for i, x in enumerate(left)
        for j, y in enumerate(right)
    })


def likelihood_lift(kernel: Kernel, likelihood: Poly) -> Kernel:
    """Multiply a kernel by L(u)L(v), without any branch scalar."""
    out: Kernel = {}
    for (i, j), value in kernel.items():
        for a, x in enumerate(likelihood):
            for b, y in enumerate(likelihood):
                key = (i + a, j + b)
                out[key] = out.get(key, F(0)) + value * x * y
    return clean_kernel(out)


def rising(start: int, length: int) -> int:
    return math.prod(range(start, start + length))


@lru_cache(None)
def tree_weight(size: int) -> F:
    return F(size ** (size - 1), math.factorial(size))


def split_probability(total: int, bottom: int) -> F:
    return (
        tree_weight(total + 1 - bottom)
        * tree_weight(bottom)
        / tree_weight(total + 1)
    )


@lru_cache(None)
def ordered_compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for first in range(1, total + 1):
        for tail in ordered_compositions(total - first):
            rows.append((first,) + tail)
    return tuple(rows)


def root_mass(composition: tuple[int, ...]) -> F:
    numerator = math.prod(tree_weight(part) for part in composition)
    return numerator / (
        math.factorial(len(composition))
        * tree_weight(sum(composition) + 1)
    )


def endpoint_basins(total: int) -> tuple[
    tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...
]:
    sources = ordered_compositions(total)
    endpoints: set[tuple[int, ...]] = set()
    for source in sources:
        for cut in range(1, len(source)):
            if sum(source[:cut]) + source[cut] - 1 >= 2:
                endpoints.add((sum(source[:cut]),) + source[cut:])

    def flows_to(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
        for cut in range(1, len(source) + 1):
            if sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]:
                return True
        return False

    return tuple(
        (endpoint, tuple(source for source in sources if flows_to(source, endpoint)))
        for endpoint in sorted(endpoints, key=lambda row: (len(row), row))
    )


def point_current(composition: tuple[int, ...], bottom: int) -> Poly:
    degree = len(composition)
    last = composition[-1]
    if last < bottom:
        return (F(0),)
    if last == bottom:
        return monomial(degree - 1, F(degree))
    q_child = split_probability(last - 1, bottom)
    out = [F(0)] * (degree + 1)
    out[0] = q_child
    out[degree] = -q_child
    return trim(out)


@lru_cache(None)
def exact_reset_kernel(total: int, bottom: int) -> Kernel:
    q_parent = split_probability(total, bottom)
    result: Kernel = {}
    for endpoint, basin in endpoint_basins(total):
        current: Poly = (F(0),)
        for source in basin:
            centered = poly_add(point_current(source, bottom), (F(-q_parent),))
            current = poly_add(current, poly_scale(centered, root_mass(source)))
        capacity = F(len(endpoint)) * root_mass(endpoint)
        result = kernel_add(
            result,
            kernel_scale(outer(current, current), F(1) / (q_parent * capacity)),
        )
    return result


def attachment_mass(kappa: int, deficit: int, degree: int, observed: int) -> F:
    return F(
        math.comb(degree, observed)
        * rising(deficit, observed)
        * rising(kappa - deficit, degree - observed),
        rising(kappa, degree),
    )


@lru_cache(None)
def exact_history_kernel(
    total: int, kappa: int, deficit: int, bottom: int
) -> Kernel:
    """Reconstruct R + sum_live sum_(a<d) (eta/pi_a) L_a K_child L_a."""
    q_parent = split_probability(total, bottom)
    result = dict(exact_reset_kernel(total, bottom))
    assert sum((root_mass(row) for row in ordered_compositions(total)), F(0)) == 1

    for root in ordered_compositions(total):
        degree = len(root)
        last = root[-1]
        if last <= bottom or last - 1 < 2:
            continue
        eta = root_mass(root) * split_probability(last - 1, bottom) / q_parent
        masses = [
            attachment_mass(kappa, deficit, degree, observed)
            for observed in range(degree + 1)
        ]
        assert sum(masses, F(0)) == 1
        for observed in range(degree):  # observed=degree is killed, exactly once
            pi_a = masses[observed]
            assert pi_a > 0 and eta > 0
            child = exact_history_kernel(
                last - 1, kappa + degree, deficit + observed, bottom
            )
            lifted = likelihood_lift(child, bernstein(degree, observed))
            result = kernel_add(result, kernel_scale(lifted, eta / pi_a))
    return clean_kernel(result)


def zeros(size: int) -> Matrix:
    return [[F(0) for _ in range(size)] for _ in range(size)]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    assert len(left[0]) == len(right)
    out = [[F(0) for _ in range(len(right[0]))] for _ in range(len(left))]
    for i in range(len(left)):
        for k in range(len(right)):
            if left[i][k]:
                for j in range(len(right[0])):
                    out[i][j] += left[i][k] * right[k][j]
    return out


def identity(size: int) -> Matrix:
    out = zeros(size)
    for i in range(size):
        out[i][i] = 1
    return out


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    aug = [list(row) + identity(size)[i] for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if aug[row][column])
        aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [value / scale for value in aug[column]]
        for row in range(size):
            if row == column:
                continue
            factor = aug[row][column]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[column][j]
                    for j in range(2 * size)
                ]
    return [row[size:] for row in aug]


def determinant(matrix: Matrix) -> F:
    work = [list(row) for row in matrix]
    value = F(1)
    size = len(work)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value *= -1
        diagonal = work[column][column]
        value *= diagonal
        for row in range(column + 1, size):
            factor = work[row][column] / diagonal
            for j in range(column + 1, size):
                work[row][j] -= factor * work[column][j]
    return value


def monomial_matrix(kernel: Kernel, degree: int) -> Matrix:
    out = zeros(degree + 1)
    for (i, j), value in kernel.items():
        assert i <= degree and j <= degree
        out[i][j] += value
    return out


def bernstein_basis_matrix(degree: int) -> Matrix:
    """Rows are monomial powers and columns are Bernstein features."""
    out = zeros(degree + 1)
    for column in range(degree + 1):
        feature = bernstein(degree, column)
        for row, value in enumerate(feature):
            out[row][column] = value
    return out


def exact_bernstein_coefficient_matrix(kernel: Kernel, degree: int) -> Matrix:
    basis = bernstein_basis_matrix(degree)
    basis_inverse = inverse(basis)
    monomials = monomial_matrix(kernel, degree)
    coefficients = matmul(matmul(basis_inverse, monomials), transpose(basis_inverse))
    assert matmul(matmul(basis, coefficients), transpose(basis)) == monomials
    return coefficients


def uniform_expectation(poly: Poly) -> F:
    return sum((value / F(degree + 1) for degree, value in enumerate(poly)), F(0))


def first_jacobi_feature_charge(feature: Poly) -> F:
    square = poly_mul(feature, feature)
    centered = poly_mul((F(-1, 2), F(1)), feature)
    return uniform_expectation(square) - 12 * uniform_expectation(centered) ** 2


def first_jacobi_kernel_charge(kernel: Kernel) -> F:
    diagonal = sum(
        (value / F(i + j + 1) for (i, j), value in kernel.items()), F(0)
    )
    centered_moments = {
        degree: F(1, degree + 2) - F(1, 2 * (degree + 1))
        for degree in range(7)
    }
    first_mode = 12 * sum(
        (
            value * centered_moments[i] * centered_moments[j]
            for (i, j), value in kernel.items()
        ),
        F(0),
    )
    return diagonal - first_mode


def elevation_coefficients(source_degree: int, index: int, cap: int) -> list[F]:
    assert source_degree <= cap
    out = [F(0)] * (cap + 1)
    for target in range(index, index + cap - source_degree + 1):
        out[target] = F(
            math.comb(source_degree, index)
            * math.comb(cap - source_degree, target - index),
            math.comb(cap, target),
        )
    return out


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def matrix_outer(vector: list[F]) -> Matrix:
    return [[x * y for y in vector] for x in vector]


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def matrix_inner(left: Matrix, right: Matrix) -> F:
    return sum(
        (left[i][j] * right[i][j]
         for i in range(len(left)) for j in range(len(left))),
        F(0),
    )


def matrix_bandwidth(matrix: Matrix) -> int:
    return max(
        (abs(i - j)
         for i in range(len(matrix)) for j in range(len(matrix))
         if matrix[i][j]),
        default=0,
    )


def signed_diagonal_dominance_margins(matrix: Matrix) -> list[F]:
    return [
        matrix[i][i]
        - sum((abs(matrix[i][j])
               for j in range(len(matrix)) if j != i), F(0))
        for i in range(len(matrix))
    ]


def charge_matrix(degree: int) -> Matrix:
    features = [bernstein(degree, index) for index in range(degree + 1)]
    first = [
        uniform_expectation(poly_mul((F(-1, 2), F(1)), feature))
        for feature in features
    ]
    return [
        [
            uniform_expectation(poly_mul(features[i], features[j]))
            - 12 * first[i] * first[j]
            for j in range(degree + 1)
        ]
        for i in range(degree + 1)
    ]


def elevate_vector(vector: list[F], source_degree: int, cap: int) -> list[F]:
    result = [F(0)] * (cap + 1)
    for index, coefficient in enumerate(vector):
        for target, elevation in enumerate(
            elevation_coefficients(source_degree, index, cap)
        ):
            result[target] += coefficient * elevation
    return result


def envelope_matrix(vector: list[F]) -> Matrix:
    total = sum(vector, F(0))
    out = zeros(len(vector))
    for i, value in enumerate(vector):
        out[i][i] = total * value
    rank_one = matrix_outer(vector)
    return [
        [out[i][j] - rank_one[i][j] for j in range(len(vector))]
        for i in range(len(vector))
    ]


def pairwise_psd_decomposition(vector: list[F]) -> Matrix:
    """sum_(i<j) e_i e_j (unit_i-unit_j)(unit_i-unit_j)^T."""
    out = zeros(len(vector))
    for i in range(len(vector)):
        for j in range(i + 1, len(vector)):
            weight = vector[i] * vector[j]
            out[i][i] += weight
            out[j][j] += weight
            out[i][j] -= weight
            out[j][i] -= weight
    return out


def evaluate_bernstein(degree: int, index: int, point: F) -> F:
    return F(math.comb(degree, index)) * point ** index * (1 - point) ** (degree - index)


def fraction_text(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix_digest(matrix: Matrix) -> str:
    text = ";".join(
        f"{i},{j}:{value.numerator}/{value.denominator}"
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
    )
    return hashlib.sha256(text.encode()).hexdigest()


def kernel_digest(kernel: Kernel) -> str:
    text = ";".join(
        f"{i},{j}:{value.numerator}/{value.denominator}"
        for (i, j), value in sorted(kernel.items())
    )
    return hashlib.sha256(text.encode()).hexdigest()


def recursion_audit(top_state: tuple[int, int, int, int]) -> dict[str, object]:
    pending = [top_state]
    seen: set[tuple[int, int, int, int]] = set()
    live_root_rows = 0
    retained_observations = 0
    killed_observations = 0
    eta_over_pi_terms: list[str] = []
    while pending:
        total, kappa, deficit, bottom = pending.pop()
        state = (total, kappa, deficit, bottom)
        if state in seen:
            continue
        seen.add(state)
        q_parent = split_probability(total, bottom)
        roots = ordered_compositions(total)
        assert sum((root_mass(root) for root in roots), F(0)) == 1
        for root in roots:
            degree, last = len(root), root[-1]
            masses = [attachment_mass(kappa, deficit, degree, a) for a in range(degree + 1)]
            assert sum(masses, F(0)) == 1
            if last <= bottom or last - 1 < 2:
                continue
            live_root_rows += 1
            eta = root_mass(root) * split_probability(last - 1, bottom) / q_parent
            killed_observations += 1
            for observed in range(degree):
                pi_a = masses[observed]
                retained_observations += 1
                eta_over_pi_terms.append(fraction_text(eta / pi_a))
                pending.append((last - 1, kappa + degree, deficit + observed, bottom))
    encoded = ";".join(eta_over_pi_terms)
    return {
        "unique_recursive_states": len(seen),
        "live_root_rows": live_root_rows,
        "retained_observations": retained_observations,
        "killed_a_equals_d_omissions": killed_observations,
        "all_attachment_laws_sum_to_one": True,
        "branch_scalar": "eta/pi_a",
        "eta_over_pi_sequence_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    bottom, cap, kappa, deficit = 1, 6, 2, 1
    total = bottom + cap

    # Audit exact Bernstein multiplication, saturation, and every elevation
    # occurring inside this declared cap.  This is algebra, not a parameter scan.
    product_checks = 0
    saturated_checks = 0
    unsaturated_checks = 0
    nondiagonal_unsaturated_cases = 0
    elevation_checks = 0
    for source_degree in range(cap + 1):
        for index in range(source_degree + 1):
            e = elevation_coefficients(source_degree, index, cap)
            elevated: Poly = (F(0),)
            for target, coefficient in enumerate(e):
                elevated = poly_add(elevated, poly_scale(bernstein(cap, target), coefficient))
            assert elevated == bernstein(source_degree, index)
            assert all(value >= 0 for value in e)
            assert envelope_matrix(e) == pairwise_psd_decomposition(e)
            elevation_checks += 1
            if source_degree == cap:
                assert sum(value != 0 for value in e) == 1

    for likelihood_degree in range(1, cap + 1):
        for child_degree in range(cap - likelihood_degree + 1):
            combined_degree = likelihood_degree + child_degree
            for observed in range(likelihood_degree + 1):
                for child_index in range(child_degree + 1):
                    ratio = F(
                        math.comb(likelihood_degree, observed)
                        * math.comb(child_degree, child_index),
                        math.comb(combined_degree, observed + child_index),
                    )
                    assert poly_mul(
                        bernstein(likelihood_degree, observed),
                        bernstein(child_degree, child_index),
                    ) == poly_scale(
                        bernstein(combined_degree, observed + child_index), ratio
                    )
                    product_checks += 1
                    if combined_degree == cap:
                        saturated_checks += 1
                    else:
                        unsaturated_checks += 1
                        e = elevation_coefficients(combined_degree, observed + child_index, cap)
                        if sum(value > 0 for value in e) > 1:
                            nondiagonal_unsaturated_cases += 1

    example_elevation = elevation_coefficients(5, 2, 6)
    assert example_elevation[2] == F(2, 3)
    assert example_elevation[3] == F(1, 2)
    assert matrix_outer(example_elevation)[2][3] == F(1, 3)

    kernel = exact_history_kernel(total, kappa, deficit, bottom)
    assert len(kernel) == 49
    assert all(kernel.get((i, j), F(0)) == kernel.get((j, i), F(0)) for i in range(7) for j in range(7))

    coefficient = exact_bernstein_coefficient_matrix(kernel, cap)
    assert all(coefficient[i][j] == coefficient[j][i] for i in range(7) for j in range(7))

    basis = bernstein_basis_matrix(cap)
    basis_det = determinant(basis)
    assert basis_det != 0
    evaluation = [
        [evaluate_bernstein(cap, index, F(row, cap)) for index in range(cap + 1)]
        for row in range(cap + 1)
    ]
    evaluation_det = determinant(evaluation)
    assert evaluation_det != 0

    cost = charge_matrix(cap)
    assert all(cost[i][j] == cost[j][i] for i in range(7) for j in range(7))
    weights = [cost[index][index] for index in range(cap + 1)]
    assert weights == [
        first_jacobi_feature_charge(bernstein(cap, index))
        for index in range(cap + 1)
    ]
    signs = [-1, -1, -1, 1, 1, 1, 1]
    radii = [F(1, 5), F(4, 25), F(17, 100), F(9, 50), F(17, 100), F(4, 25), F(1, 5)]
    vector = [F(sign) * radius for sign, radius in zip(signs, radii)]
    remainders = [weight - radius * radius for weight, radius in zip(weights, radii)]
    assert all(value > 0 for value in remainders)
    dual = matrix_outer(vector)
    for index, remainder in enumerate(remainders):
        dual[index][index] += remainder
    assert [dual[index][index] for index in range(7)] == weights

    objective = sum(
        (coefficient[i][j] * dual[j][i] for i in range(7) for j in range(7)),
        F(0),
    )
    q = split_probability(total, bottom)
    budget = 1 - q
    dual_excess = objective - budget
    actual_t1 = first_jacobi_kernel_charge(kernel)
    actual_slack = budget - actual_t1
    assert q == F(7, 8) ** 6
    assert objective == F(
        27574523089250503170656957870808157889213,
        48209994003606915089647408250880000000000,
    )
    assert dual_excess == F(
        1000948704365931347999936328408157889213,
        48209994003606915089647408250880000000000,
    )
    assert dual_excess > 0
    assert actual_slack > 0

    # Exact tridiagonal width-one primal, typed independently from the frozen
    # theorem statement.  Strict signed diagonal dominance certifies both PSD
    # matrices without an eigenvalue approximation.
    primal = zeros(7)
    diagonal = [
        F(101, 50), F(111, 100), F(43, 100), F(19, 25),
        F(39, 25), F(99, 50), F(21, 5),
    ]
    adjacent = [F(1, 3), F(2, 15), F(1, 12), F(1, 5), F(3, 5), F(11, 8)]
    for i, value in enumerate(diagonal):
        primal[i][i] = value
    for i, value in enumerate(adjacent):
        primal[i][i + 1] = primal[i + 1][i] = value
    assert matrix_bandwidth(primal) == 1
    residual = matrix_subtract(primal, coefficient)
    primal_margins = signed_diagonal_dominance_margins(primal)
    residual_margins = signed_diagonal_dominance_margins(residual)
    assert all(value > 0 for value in primal_margins)
    assert all(value > 0 for value in residual_margins)
    assert all(primal[i][i] > 0 and residual[i][i] > 0 for i in range(7))
    assert primal_margins == [
        F(253, 150), F(193, 300), F(16, 75), F(143, 300),
        F(19, 25), F(1, 200), F(113, 40),
    ]
    expected_residual_margins = [
        F(260320697099383109737650392531, 42810517485720426320033218560000),
        F(732473570171065182244302170489, 77058931474296767376059793408000),
        F(22066085580152050340437577895121, 9632366434287095922007474176000000),
        F(1509226832311692335786724342497, 214052587428602131600166092800000),
        F(7067441003517689910864640423799, 1070262937143010658000830464000000),
        F(855769982930667113675511847409, 42810517485720426320033218560000),
        F(21088769888592000787, 5613145673139486720000),
    ]
    assert residual_margins == expected_residual_margins
    primal_charge = matrix_inner(cost, primal)
    primal_slack = budget - primal_charge
    assert primal_charge == F(4937603, 9172800)
    assert primal_slack == F(485323987, 37571788800) > 0

    # Re-derive the bandwidth law directly from elevation supports. Saturated
    # multiplication shifts both indices equally. Unsaturated elevation gives
    # each index an interval of length h=cap-combined, hence w+h.
    saturated_band_checks = 0
    unsaturated_bound_checks = 0
    for likelihood_degree in range(1, cap + 1):
        for child_degree in range(cap - likelihood_degree + 1):
            combined = likelihood_degree + child_degree
            for child_left in range(child_degree + 1):
                for child_right in range(child_degree + 1):
                    width = abs(child_left - child_right)
                    for observed in range(likelihood_degree + 1):
                        left_index = observed + child_left
                        right_index = observed + child_right
                        if combined == cap:
                            assert abs(left_index - right_index) == width
                            saturated_band_checks += 1
                        else:
                            left_support = [
                                target for target, value in enumerate(
                                    elevation_coefficients(combined, left_index, cap)
                                ) if value
                            ]
                            right_support = [
                                target for target, value in enumerate(
                                    elevation_coefficients(combined, right_index, cap)
                                ) if value
                            ]
                            maximum = max(
                                abs(left - right)
                                for left in left_support for right in right_support
                            )
                            assert maximum <= min(cap, width + cap - combined)
                            unsaturated_bound_checks += 1

    lifted_degree_two = [F(1), F(1, 2), F(0)]
    elevated_width_example = elevate_vector(lifted_degree_two, 2, cap)
    assert elevated_width_example == [
        F(1), F(5, 6), F(2, 3), F(1, 2), F(1, 3), F(1, 6), F(0)
    ]
    assert matrix_bandwidth(matrix_outer(elevated_width_example)) == 5

    payload = {
        "schema": "M224-independent-M221-referee-v1",
        "python": platform.python_version(),
        "seed": None,
        "method": "single exact row; literal ordered compositions; exact matrix inversion; no M221 import or data read",
        "state_B_L_kappa_D": [bottom, cap, kappa, deficit],
        "source_independence": {
            "project_imports": False,
            "predecessor_files_read_by_checker": False,
            "parameter_scan": False,
        },
        "bernstein_algebra": {
            "product_checks": product_checks,
            "saturated_exact_closure_checks": saturated_checks,
            "unsaturated_product_checks": unsaturated_checks,
            "unsaturated_cases_with_nondiagonal_outer_product": nondiagonal_unsaturated_cases,
            "degree_elevation_checks": elevation_checks,
            "example_b_5_2_to_degree_6": [fraction_text(value) for value in example_elevation],
            "example_raw_offdiagonal_2_3": "1/3",
            "envelope_psd_reason": "s*diag(e)-ee^T=sum_(i<j)e_i e_j(unit_i-unit_j)(unit_i-unit_j)^T",
        },
        "basis_and_necessary_condition": {
            "bernstein_basis_determinant": fraction_text(basis_det),
            "seven_point_evaluation_determinant": fraction_text(evaluation_det),
            "coefficient_matrix_symmetric": True,
            "kernel_psd_iff_coefficient_matrix_psd": True,
        },
        "charge_matrix": {
            "sha256": matrix_digest(cost),
            "symmetric": True,
            "construction": "uniform Bernstein Gram minus first-Jacobi rank one",
        },
        "recursion": {
            **recursion_audit((total, kappa, deficit, bottom)),
            "top_kernel_terms": len(kernel),
            "kernel_sha256": kernel_digest(kernel),
            "bernstein_coefficient_sha256": matrix_digest(coefficient),
        },
        "width_zero_dual_certificate": {
            "weights": [fraction_text(value) for value in weights],
            "signs": signs,
            "radii": [fraction_text(value) for value in radii],
            "diagonal_remainders": [fraction_text(value) for value in remainders],
            "dual_psd_reason": "X=vv^T+diag(strictly positive remainders)",
            "q": fraction_text(q),
            "budget": fraction_text(budget),
            "objective": fraction_text(objective),
            "positive_excess": fraction_text(dual_excess),
        },
        "width_one_primal_certificate": {
            "matrix_sha256": matrix_digest(primal),
            "diagonal": [fraction_text(value) for value in diagonal],
            "adjacent_offdiagonal": [fraction_text(value) for value in adjacent],
            "bandwidth": matrix_bandwidth(primal),
            "C_margins": [fraction_text(value) for value in primal_margins],
            "C_minus_A_sha256": matrix_digest(residual),
            "C_minus_A_margins": [
                fraction_text(value) for value in residual_margins
            ],
            "minimum_C_margin": fraction_text(min(primal_margins)),
            "minimum_C_minus_A_margin": fraction_text(min(residual_margins)),
            "psd_reason": "symmetric strict signed diagonal dominance with positive diagonal",
            "charge": fraction_text(primal_charge),
            "positive_budget_slack": fraction_text(primal_slack),
        },
        "least_feasible_bandwidth": 1,
        "lift_audit": {
            "saturated_preserves_bandwidth_checks": saturated_band_checks,
            "unsaturated_upper_bound_checks": unsaturated_bound_checks,
            "general_bound": "min(L,w+(L-n))",
            "counterexample_likelihood_d_a": [1, 0],
            "counterexample_child_vector": ["1", "1"],
            "counterexample_combined_degree_vector": ["1", "1/2", "0"],
            "counterexample_elevated_vector": [
                fraction_text(value) for value in elevated_width_example
            ],
            "counterexample_output_bandwidth": 5,
            "raw_width_one_closed": False,
            "cost_controlled_recursive_envelope": "unresolved",
        },
        "actual_kernel": {
            "T1": fraction_text(actual_t1),
            "positive_contraction_slack": fraction_text(actual_slack),
            "contraction_counterexample": False,
        },
        "all_checks_pass": True,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "all_checks_pass": True,
        "output": str(args.output),
        "output_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "verdict": "ACCEPT",
        "least_feasible_bandwidth": 1,
        "width_zero_dual_positive_excess": fraction_text(dual_excess),
        "width_one_positive_budget_slack": fraction_text(primal_slack),
        "raw_width_one_closed_under_unsaturated_lifts": False,
        "actual_positive_slack": fraction_text(actual_slack),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
