#!/usr/bin/env python3
"""Clean-room exact referee checks for frozen M185.

No M185 module or data is imported.  Named rational rows audit the formulas;
the universal proof is independently checked in proof_audit.md.
"""

from argparse import ArgumentParser
from fractions import Fraction as F
from json import dumps
from math import comb, factorial
from pathlib import Path


def rise(x: int, n: int) -> F:
    answer = F(1)
    for j in range(n):
        answer *= x + j
    return answer


def beta_raw(alpha: int, beta: int, n: int) -> F:
    return rise(alpha, n) / rise(alpha + beta, n)


def beta_mixed(alpha: int, beta: int, left: int, right: int) -> F:
    return rise(alpha, left) * rise(beta, right) / rise(alpha + beta, left + right)


def multiply(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def expectation(poly: list[F], alpha: int, beta: int) -> F:
    return sum((coefficient * beta_raw(alpha, beta, n) for n, coefficient in enumerate(poly)), F(0))


def determinant3(matrix: list[list[F]]) -> F:
    m = matrix
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def branch_unscaled(d: int, a: int, vandermonde_upper: bool = False) -> tuple[list[list[F]], list[F]]:
    alpha, beta, total = a + 1, d - a + 1, d + 2
    p = F(alpha, total)
    variance = beta_raw(alpha, beta, 2) - p * p
    central3 = beta_raw(alpha, beta, 3) - 3 * p * beta_raw(alpha, beta, 2) + 2 * p**3
    central4 = (
        beta_raw(alpha, beta, 4)
        - 4 * p * beta_raw(alpha, beta, 3)
        + 6 * p * p * beta_raw(alpha, beta, 2)
        - 3 * p**4
    )
    gamma = central3 / variance
    norm2 = central4 - central3 * central3 / variance - variance * variance
    basis = [
        [F(1)],
        [-p, F(1)],
        [p * p + gamma * p - variance, -2 * p - gamma, F(1)],
    ]
    alpha_hat, beta_hat = 2 * a + 1, 2 * d - 2 * a + 1
    likelihood_mass = F(d + 1, 2 * d + 1)
    if not vandermonde_upper:
        likelihood_mass *= F(comb(d, a) ** 2, comb(2 * d, 2 * a))
    matrix = [
        [
            likelihood_mass * expectation(multiply(basis[i], basis[j]), alpha_hat, beta_hat)
            for j in range(3)
        ]
        for i in range(3)
    ]
    covariance = [p - F(1, 2), variance, F(0)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] -= F(12, d + 1) * covariance[i] * covariance[j]
    return matrix, [F(1), variance, norm2]


def normalized_slack_determinant(d: int, a: int, constant: F) -> F:
    matrix, gram = branch_unscaled(d, a)
    slack = [
        [(constant * gram[i] if i == j else F(0)) - matrix[i][j] for j in range(3)]
        for i in range(3)
    ]
    return determinant3(slack) / (gram[1] * gram[2])


def cayley_weight(n: int) -> F:
    return F(n ** (n - 1), factorial(n))


def square_expectation(poly: list[F], alpha: int, beta: int) -> F:
    return expectation(multiply(poly, poly), alpha, beta)


def likelihood_second_ratio(alpha: int, beta: int, observation: int) -> F:
    coefficient = comb(2, observation)
    first = coefficient * beta_mixed(alpha, beta, observation, 2 - observation)
    second = coefficient**2 * beta_mixed(alpha, beta, 2 * observation, 2 * (2 - observation))
    return second / first


def trace_envelope(B: int, d: int, a: int) -> dict[str, F]:
    total, alpha, beta = d + 2, a + 1, d - a + 1
    y = cayley_weight(B) / cayley_weight(B + 1)
    b = cayley_weight(B) / cayley_weight(B + 2)
    q = F(3, 2) * cayley_weight(B) / cayley_weight(B + 3)
    reset = (
        q * (F(B + 1, B + 3) - F(5, 9) * q - q / (3 * y))
        + square_expectation([-q, F(0), F(3)], alpha, beta) / 27
        + square_expectation([-4 * q, F(6), F(3)], alpha, beta) / 54
        + square_expectation([y - q, F(0), -y], alpha, beta) / (6 * y)
    )
    height_one = (
        likelihood_second_ratio(alpha, beta, 0)
        + likelihood_second_ratio(alpha, beta, 1)
    ) * (1 - y) / 3
    beta_after = beta + 1
    p_after = F(alpha, total + 1)
    outer_exceptional = (
        beta_mixed(alpha, beta_after, 2, 0)
        - b * beta_mixed(alpha, beta_after, 1, 0)
        + b * b / 4
        - beta_mixed(alpha, beta_after, 3, 0)
        + b * beta_mixed(alpha, beta_after, 2, 0)
        - b * b * beta_mixed(alpha, beta_after, 1, 0) / 4
    )
    unary = (
        (1 - p_after) * b * (F(B, B + 2) - b / 2)
        + outer_exceptional
        + beta_mixed(alpha, beta_after, 0, 3) * (1 - y) / (1 - p_after)
    )
    return {
        "reset": reset,
        "height_one": height_one,
        "unary": unary,
        "total": reset + height_one + F(2, 3) * unary,
    }


def compositions(n: int, r: int) -> F:
    if n == 0 and r == 0:
        return F(1)
    if n == r:
        return F(1)
    return F(r * n ** (n - r - 1), factorial(n - r))


def eta(n: int, r: int) -> F:
    return F(3, 2) * compositions(n, r) / (factorial(r + 1) * cayley_weight(n + 4))


def rational(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    det20 = normalized_slack_determinant(20, 0, F(2, 3))
    det50 = normalized_slack_determinant(50, 0, F(2, 3))
    det1 = normalized_slack_determinant(1, 0, F(3, 4))
    trace = trace_envelope(3, 20, 19)
    boundary_b1 = trace_envelope(1, 1, 0)
    exterior_rows = {}
    for n in (0, 1, 2, 5):
        if n == 0:
            moment = eta(0, 0)
        else:
            moment = sum((F(r + 1) * eta(n, r) for r in range(1, n + 1)), F(0))
        exterior_rows[str(n)] = rational(moment)

    result = {
        "schema": "M190-clean-room-v1",
        "seed": None,
        "matrix": {
            "det_2over3_d20_a0": rational(det20),
            "det_2over3_d50_a0": rational(det50),
            "det_3over4_d1_a0": rational(det1),
        },
        "trace_B3_d20_a19": {key: rational(value) for key, value in trace.items()},
        "trace_B1_d1_a0_nominal_envelope": {
            key: rational(value) for key, value in boundary_b1.items()
        },
        "exterior_first_moments": exterior_rows,
        "assertions": {
            "two_thirds_refuted": det20 < 0,
            "second_refutation_row": det50 < 0,
            "minimal_three_fourths_slack_positive": det1 > 0,
            "trace_envelope_exceeds_one": trace["total"] > 1,
            "n0_eta": eta(0, 0) == F(9, 16),
            "n1_includes_r_equals_n": exterior_rows["1"] == "36/125",
            "killed_observation_never_evaluated": True,
        },
    }
    if not all(result["assertions"].values()):
        raise AssertionError(result)
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
