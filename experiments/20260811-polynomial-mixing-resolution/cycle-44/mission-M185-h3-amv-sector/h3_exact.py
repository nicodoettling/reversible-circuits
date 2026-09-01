#!/usr/bin/env python3
"""Clean exact audit for the M185 fresh h=3 reduction.

Standard library only.  This checks named decisive rows; the universal
matrix statement is proved symbolically in h3_reduction.md.
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from json import dump
from math import comb, factorial
from pathlib import Path


def rising(x: int, n: int) -> Q:
    out = Q(1)
    for i in range(n):
        out *= x + i
    return out


def moment(alpha: int, beta: int, n: int) -> Q:
    return rising(alpha, n) / rising(alpha + beta, n)


def beta_moment(alpha: int, beta: int, i: int, j: int = 0) -> Q:
    return rising(alpha, i) * rising(beta, j) / rising(alpha + beta, i + j)


def poly_mul(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def poly_expect(coeffs: list[Q], alpha: int, beta: int) -> Q:
    return sum((c * moment(alpha, beta, i) for i, c in enumerate(coeffs)), Q(0))


def det3(matrix: list[list[Q]]) -> Q:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def branch(d: int, a: int) -> tuple[list[list[Q]], Q, Q]:
    alpha, beta, k = a + 1, d - a + 1, d + 2
    p = Q(alpha, k)
    v = moment(alpha, beta, 2) - p * p
    m3 = moment(alpha, beta, 3) - 3 * p * moment(alpha, beta, 2) + 2 * p**3
    m4 = (
        moment(alpha, beta, 4)
        - 4 * p * moment(alpha, beta, 3)
        + 6 * p * p * moment(alpha, beta, 2)
        - 3 * p**4
    )
    gamma = m3 / v
    h2 = m4 - m3 * m3 / v - v * v
    basis = [
        [Q(1)],
        [-p, Q(1)],
        [p * p + gamma * p - v, -2 * p - gamma, Q(1)],
    ]
    alpha_hat, beta_hat = 2 * a + 1, 2 * d - 2 * a + 1
    lambda0 = Q(d + 1, 2 * d + 1) * Q(comb(d, a) ** 2, comb(2 * d, 2 * a))
    matrix = [
        [
            lambda0 * poly_expect(poly_mul(basis[i], basis[j]), alpha_hat, beta_hat)
            for j in range(3)
        ]
        for i in range(3)
    ]
    z = [p - Q(1, 2), v, Q(0)]
    pi = Q(1, d + 1)
    for i in range(3):
        for j in range(3):
            matrix[i][j] -= 12 * pi * z[i] * z[j]
    return matrix, v, h2


def normalized_slack_det(d: int, a: int, constant: Q) -> Q:
    matrix, v, h2 = branch(d, a)
    gram = [Q(1), v, h2]
    slack = [
        [(constant * gram[i] if i == j else Q(0)) - matrix[i][j] for j in range(3)]
        for i in range(3)
    ]
    return det3(slack) / (v * h2)


def cayley(n: int) -> Q:
    return Q(n ** (n - 1), factorial(n))


def likelihood_ratio(alpha: int, beta: int, j: int) -> Q:
    choose = comb(2, j)
    pi = choose * beta_moment(alpha, beta, j, 2 - j)
    second = choose * choose * beta_moment(alpha, beta, 2 * j, 2 * (2 - j))
    return second / pi


def square_expect(coeffs: list[Q], alpha: int, beta: int) -> Q:
    return sum(
        (
            left * right * beta_moment(alpha, beta, i + j)
            for i, left in enumerate(coeffs)
            for j, right in enumerate(coeffs)
        ),
        Q(0),
    )


def trace_envelope(B: int, d: int, a: int) -> dict[str, Q]:
    k, alpha, beta = d + 2, a + 1, d - a + 1
    y = cayley(B) / cayley(B + 1)
    b = cayley(B) / cayley(B + 2)
    q = Q(3, 2) * cayley(B) / cayley(B + 3)
    h0, h1 = Q(B + 1, B + 3), Q(B, B + 2)
    reset = (
        q * (h0 - Q(5, 9) * q - q / (3 * y))
        + square_expect([-q, Q(0), Q(3)], alpha, beta) / 27
        + square_expect([-4 * q, Q(6), Q(3)], alpha, beta) / 54
        + square_expect([y - q, Q(0), -y], alpha, beta) / (6 * y)
    )
    height_one = (
        likelihood_ratio(alpha, beta, 0) + likelihood_ratio(alpha, beta, 1)
    ) * (1 - y) / 3
    beta1 = beta + 1
    p1 = Q(alpha, k + 1)
    exceptional = (
        beta_moment(alpha, beta1, 2)
        - b * beta_moment(alpha, beta1, 1)
        + b * b / 4
        - beta_moment(alpha, beta1, 3)
        + b * beta_moment(alpha, beta1, 2)
        - b * b * beta_moment(alpha, beta1, 1) / 4
    )
    unary_weighted = (
        (1 - p1) * b * (h1 - b / 2)
        + exceptional
        + beta_moment(alpha, beta1, 0, 3) * (1 - y) / (1 - p1)
    )
    total = reset + height_one + Q(2, 3) * unary_weighted
    return {
        "reset": reset,
        "height_one": height_one,
        "unary_weighted": unary_weighted,
        "total": total,
    }


def qstr(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    two_thirds_20 = normalized_slack_det(20, 0, Q(2, 3))
    two_thirds_50 = normalized_slack_det(50, 0, Q(2, 3))
    three_fourths_1 = normalized_slack_det(1, 0, Q(3, 4))
    trace_rows = {}
    for B, d, a in ((3, 20, 19), (2, 1, 0), (1, 1, 0)):
        trace_rows[f"B{B}_d{d}_a{a}"] = {
            key: qstr(value) for key, value in trace_envelope(B, d, a).items()
        }
    payload = {
        "schema": "M185-h3-exact-v1",
        "python": "standard-library Fraction",
        "seed": None,
        "matrix_rows": {
            "d20_a0_det_2over3": qstr(two_thirds_20),
            "d50_a0_det_2over3": qstr(two_thirds_50),
            "d1_a0_det_3over4": qstr(three_fourths_1),
        },
        "trace_rows": trace_rows,
        "assertions": {
            "d20_refutes_2over3": two_thirds_20 < 0,
            "d50_confirms_obstruction": two_thirds_50 < 0,
            "d1_3over4_positive": three_fourths_1 > 0,
            "named_trace_exceeds_one": trace_envelope(3, 20, 19)["total"] > 1,
            "killed_a_equals_d_not_called": True,
        },
    }
    if not all(payload["assertions"].values()):
        raise AssertionError(payload)
    args.output.write_text(__import__("json").dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
