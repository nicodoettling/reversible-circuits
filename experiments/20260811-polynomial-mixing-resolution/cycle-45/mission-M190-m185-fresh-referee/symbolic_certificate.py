#!/usr/bin/env python3
"""Clean-room symbolic derivation of the M185 3/4 Loewner certificate."""

from argparse import ArgumentParser
from json import dumps
from pathlib import Path

import sympy as sp


def moment(alpha, total, degree):
    if degree == 0:
        return sp.Integer(1)
    return sp.prod(alpha + j for j in range(degree)) / sp.prod(total + j for j in range(degree))


def even_polynomial_to_x(expression, variable, x):
    terms = sp.Poly(sp.expand(expression), variable).as_dict()
    if any(power[0] % 2 for power in terms):
        raise AssertionError("unexpected odd power")
    return sp.expand(sum(coefficient * x ** (power[0] // 2) for power, coefficient in terms.items()))


def shifted_coefficients(expression, variable, shifted_variable):
    return [str(value) for value in sp.Poly(sp.expand(expression.subs(variable, shifted_variable + 1)), shifted_variable).all_coeffs()]


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    d, t, u, x, e = sp.symbols("d t u x e")
    a = (d + t) / 2
    alpha, total = a + 1, d + 2
    alpha_hat, total_hat = 2 * a + 1, 2 * d + 2

    p = sp.factor(alpha / total)
    variance = sp.factor(moment(alpha, total, 2) - p**2)
    central3 = sp.factor(moment(alpha, total, 3) - 3 * p * moment(alpha, total, 2) + 2 * p**3)
    central4 = sp.factor(
        moment(alpha, total, 4)
        - 4 * p * moment(alpha, total, 3)
        + 6 * p**2 * moment(alpha, total, 2)
        - 3 * p**4
    )
    gamma = sp.factor(central3 / variance)
    norm2 = sp.factor(central4 - central3**2 / variance - variance**2)
    basis = [sp.Integer(1), u - p, (u - p) ** 2 - gamma * (u - p) - variance]

    def posterior_expectation(expression):
        polynomial = sp.Poly(sp.expand(expression), u)
        return sp.factor(
            sum(coefficient * moment(alpha_hat, total_hat, power[0]) for power, coefficient in polynomial.terms())
        )

    posterior_gram = sp.Matrix(3, 3, lambda i, j: posterior_expectation(basis[i] * basis[j]))
    covariance = sp.Matrix([p - sp.Rational(1, 2), variance, 0])
    gram = sp.diag(1, variance, norm2)
    lambda_star = (d + 1) / (2 * d + 1)
    slack = sp.simplify(
        sp.Rational(3, 4) * gram
        - lambda_star * posterior_gram
        + 12 / (d + 1) * covariance * covariance.T
    )

    first = sp.factor(slack[0, 0])
    second = sp.factor(sp.cancel(slack[:2, :2].det()))
    third = sp.factor(sp.cancel(slack.det()))
    second_num, second_den = sp.fraction(second)
    third_num, third_den = sp.fraction(third)
    p2 = even_polynomial_to_x(second_num, t, x)
    positive_factor = (d - t + 2) * (d + t + 2)
    p3_in_t = sp.cancel(third_num / positive_factor)
    p3 = even_polynomial_to_x(p3_in_t, t, x)

    expected_first = (
        2 * d**4 + 9 * d**3 + 11 * d**2 - 4 + (24 * d + 12) * t**2
    ) / (4 * (d + 1) * (d + 2) ** 2 * (2 * d + 1))
    expected_second_den = (
        64 * (d + 1) * (d + 2) ** 3 * (d + 3) ** 2
        * (2 * d + 1) ** 2 * (2 * d + 3)
    )
    expected_third_den = (
        2048 * (d + 1) * (d + 2) ** 4 * (d + 3) ** 4 * (d + 4) ** 2
        * (d + 5) * (2 * d + 1) ** 3 * (2 * d + 3) ** 3 * (2 * d + 5)
    )
    p2_zero_expected = (d + 2) ** 3 * (2 * d - 1) * (
        8 * d**4 + 40 * d**3 + 101 * d**2 + 108 * d + 27
    )
    p2_end_expected = 4 * (d + 1) * (2 * d + 1) * (
        4 * d**5 + 108 * d**4 + 351 * d**3 + 410 * d**2 - 27 * d - 54
    )

    coefficients = [sp.Poly(p3, x).coeff_monomial(x**j) for j in range(4)]
    bernstein = [
        coefficients[0],
        coefficients[0] + coefficients[1] * d**2 / 3,
        coefficients[0] + 2 * coefficients[1] * d**2 / 3 + coefficients[2] * d**4 / 3,
        coefficients[0] + coefficients[1] * d**2 + coefficients[2] * d**4 + coefficients[3] * d**6,
    ]
    shifted = [sp.Poly(sp.expand(value.subs(d, e + 1)), e) for value in bernstein]
    assertions = {
        "variance_positive_form": sp.factor(variance - (((d + 2) ** 2 - t**2) / (4 * (d + 2) ** 2 * (d + 3)))) == 0,
        "quadratic_norm_positive_form": sp.factor(
            norm2
            - (((d + 2) ** 2 - t**2) * ((d + 4) ** 2 - t**2)
               / (8 * (d + 2) * (d + 3) ** 2 * (d + 4) ** 2 * (d + 5)))
        ) == 0,
        "first_minor_identity": sp.factor(first - expected_first) == 0,
        "second_denominator_identity": sp.factor(second_den - expected_second_den) == 0,
        "second_zero_endpoint_identity": sp.factor(p2.subs(x, 0) - p2_zero_expected) == 0,
        "second_d_squared_endpoint_identity": sp.factor(p2.subs(x, d**2) - p2_end_expected) == 0,
        "second_concave": sp.Poly(p2, x).coeff_monomial(x**2).subs(d, 1) < 0,
        "third_denominator_identity": sp.factor(third_den - expected_third_den) == 0,
        "third_degree_three": sp.degree(p3, x) == 3,
        "bernstein_degrees": [poly.degree() for poly in shifted] == [14, 14, 13, 12],
        "all_shifted_bernstein_coefficients_positive": all(
            coefficient > 0 for poly in shifted for coefficient in poly.all_coeffs()
        ),
    }
    assertions = {key: bool(value) for key, value in assertions.items()}
    if not all(assertions.values()):
        raise AssertionError(assertions)

    payload = {
        "schema": "M190-symbolic-certificate-v1",
        "sympy_version": sp.__version__,
        "seed": None,
        "assertions": assertions,
        "first_minor": str(first),
        "second_numerator_in_x": str(sp.factor(p2)),
        "third_coefficients_in_x": [str(sp.factor(value)) for value in coefficients],
        "shifted_bernstein_coefficients_descending": [
            [str(value) for value in poly.all_coeffs()] for poly in shifted
        ],
    }
    args.output.write_text(dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
