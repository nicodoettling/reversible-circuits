#!/usr/bin/env python3
"""Clean-room exact/symbolic audit of frozen M193.

No M193 module, data, or expression is imported.  Starting from the accepted
M185/M190 actual-history envelope, this script derives its observation
average, all monotonicity certificates, the exterior rows, and the n=0
matrix boundary.
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from json import dumps
from math import factorial
from pathlib import Path

import sympy as sp


d, D = sp.symbols("d D", integer=True, positive=True)
y, b, q = sp.symbols("y b q", positive=True)
H0, H1 = sp.symbols("H0 H1", positive=True)


def rising(x, degree):
    return sp.prod(x + j for j in range(degree)) if degree else sp.Integer(1)


def beta_moment(alpha, beta, i, j=0):
    return sp.cancel(
        rising(alpha, i) * rising(beta, j) / rising(alpha + beta, i + j)
    )


def expect_polynomial(poly, alpha, beta, u):
    polynomial = sp.Poly(sp.expand(poly), u)
    return sp.factor(sum(
        coefficient * beta_moment(alpha, beta, exponent)
        for (exponent,), coefficient in polynomial.terms()
    ))


def sum_power(power):
    return {
        0: d,
        1: d * (d + 1) / 2,
        2: d * (d + 1) * (2 * d + 1) / 6,
        3: d**2 * (d + 1)**2 / 4,
        4: d * (d + 1) * (2 * d + 1) * (3 * d**2 + 3 * d - 1) / 30,
    }[power]


def average_polynomial(expr):
    expression = sp.cancel(expr)
    numerator, denominator = sp.fraction(expression)
    assert D not in denominator.free_symbols
    polynomial = sp.Poly(sp.expand(numerator), D)
    summed = sum(
        coefficient * sum_power(exponent)
        for (exponent,), coefficient in polynomial.terms()
    )
    return sp.factor(summed / (d * denominator))


def shift_one(coefficients):
    e = sp.symbols("e", nonnegative=True)
    polynomial = sum(coefficient * d**j for j, coefficient in enumerate(coefficients))
    return [int(value) for value in reversed(sp.Poly(sp.expand(polynomial.subs(d, e + 1)), e).all_coeffs())]


def w(n):
    return Q(n ** (n - 1), factorial(n))


def c(n, r):
    if r == n:
        return Q(1)
    return Q(r * n ** (n - r - 1), factorial(n - r))


def eta3(n, r):
    return Q(3, 2) * c(n, r) / (factorial(r + 1) * w(n + 4))


def qstr(value):
    if isinstance(value, Q):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    return str(sp.factor(value))


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    u = sp.symbols("u")
    k = d + 2
    alpha, beta = D, k - D

    reset = (
        q * (H0 - sp.Rational(5, 9) * q - q / (3 * y))
        + expect_polynomial((3 * u**2 - q)**2, alpha, beta, u) / 27
        + expect_polynomial((3 * u**2 + 6 * u - 4 * q)**2, alpha, beta, u) / 54
        + expect_polynomial((y * (1 - u**2) - q)**2, alpha, beta, u) / (6 * y)
    )

    def likelihood_ratio(j):
        choose = sp.binomial(2, j)
        pi = choose * beta_moment(alpha, beta, j, 2 - j)
        second = choose**2 * beta_moment(alpha, beta, 2 * j, 4 - 2 * j)
        return sp.cancel(second / pi)

    height_one = (likelihood_ratio(0) + likelihood_ratio(1)) * (1 - y) / 3

    beta1 = beta + 1
    p1 = D / (k + 1)
    unary = (
        (1 - p1) * b * (H1 - b / 2)
        + expect_polynomial((1 - u) * (u - b / 2)**2, alpha, beta1, u)
        + beta_moment(alpha, beta1, 0, 3) * (1 - y) / (1 - p1)
    )
    sbar = sp.factor(reset + height_one + sp.Rational(2, 3) * unary)
    average = average_polynomial(sbar)

    pbar = (d + 1) / (2 * (d + 2))
    m2 = (d + 1) / (3 * (d + 3))
    m3 = (d + 1) / (4 * (d + 4))
    m4 = (d + 1) / (5 * (d + 5))
    reset_target = (
        m2 * (sp.Rational(2, 3) - (q + y) / 3)
        + sp.Rational(2, 3) * m3
        + (sp.Rational(1, 2) + y / 6) * m4
        + q**2 * (-sp.Rational(2, 9) - 1 / (6 * y))
        + q * (H0 - sp.Rational(1, 3) - sp.Rational(8, 9) * pbar)
        + y / 6
    )
    height_target = 2 * (d + 7) * (1 - y) / (9 * (d + 4))
    nw = (
        ((12 * H1 - 4) * d**3 + (168 * H1 - 56) * d**2
         + (780 * H1 - 212) * d + 1200 * H1 - 160) * b
        - (3 * d**3 + 42 * d**2 + 195 * d + 300) * b**2
        + 10 * d**3 + 148 * d**2 + 734 * d + 1172
        - y * (8 * d**3 + 120 * d**2 + 664 * d + 1128)
    )
    unary_target = nw / (24 * (d + 3) * (d + 4) * (d + 5))
    target = sp.factor(reset_target + height_target + sp.Rational(2, 3) * unary_target)
    assert sp.simplify(average - target) == 0

    relaxed = sp.factor(target.subs({H0: 1, H1: 1}))
    db = sp.factor(sp.diff(relaxed, b))
    db_target = (
        4 * d**2 + 36 * d + 104 - b * (3 * d**2 + 27 * d + 60)
    ) / (18 * (d + 3) * (d + 4))
    assert sp.simplify(db - db_target) == 0
    assert sp.factor(8 * sp.together(db_target).as_numer_denom()[0].subs(b, sp.Rational(3, 8))) == 23 * d**2 + 207 * d + 652

    q_second = sp.factor(sp.diff(relaxed, q, 2))
    assert sp.simplify(q_second + (4 * y + 3) / (9 * y)) == 0
    qstar = sp.factor(sp.solve(sp.diff(relaxed, q), q)[0])
    qstar_target = y * (d**2 + 11 * d + 22) / ((d + 2) * (d + 3) * (4 * y + 3))
    assert sp.simplify(qstar - qstar_target) == 0

    optimized = sp.factor(relaxed.subs({b: sp.Rational(3, 8), q: qstar}))
    dy = sp.factor(sp.diff(optimized, y))
    denominator_y = 90 * (d + 2)**2 * (d + 3)**2 * (d + 4) * (d + 5) * (4 * y + 3)**2
    positive_poly = sp.factor(-dy * denominator_y)
    assert sp.Poly(positive_poly, d, y).total_degree() == 8
    table = []
    for degree in range(6, -1, -1):
        coefficient = sp.Poly(positive_poly, d).coeff_monomial(d**degree)
        row = tuple(int(sp.Poly(coefficient, y).coeff_monomial(y**power)) for power in (2, 1, 0))
        table.append(row)
    target_table = [
        (512, 768, 273), (11520, 17280, 6015),
        (105472, 158208, 53583), (492160, 738240, 240705),
        (1231488, 1847232, 570612), (1571840, 2357760, 673620),
        (803328, 1204992, 306672),
    ]
    assert table == target_table and all(value > 0 for row in table for value in row)

    slack = sp.factor(1 - optimized.subs(y, sp.Rational(1, 3)))
    slack_numerator, slack_denominator = sp.fraction(slack)
    main_original = [-1774608, 607388, 3485988, 2534491, 766087, 102561, 4829]
    assert sp.Poly(slack_numerator, d).all_coeffs() == list(reversed(main_original))
    main_shift = shift_one(main_original)
    assert main_shift == [5726736, 18788964, 16784028, 6721029, 1351327, 131535, 4829]
    assert all(value > 0 for value in main_shift)

    b1_average = sp.factor(target.subs({y: 1, b: sp.Rational(2, 3), q: sp.Rational(9, 16), H0: sp.Rational(1, 2), H1: sp.Rational(1, 3)}))
    b1_target = (
        17591 * d**4 + 187970 * d**3 + 679425 * d**2 + 1233430 * d + 1075144
    ) / (69120 * (d + 2) * (d + 3) * (d + 4) * (d + 5))
    assert sp.simplify(b1_average - b1_target) == 0
    b1_slack = sp.factor(1 - b1_average)
    b1_num, b1_den = sp.fraction(b1_slack)
    b1_original = [7219256, 9411050, 4228095, 779710, 51529]
    assert sp.Poly(b1_num, d).all_coeffs() == list(reversed(b1_original))
    assert all(value > 0 for value in b1_original)

    named_obstruction = sp.factor(sbar.subs({d: 20, D: 20, y: sp.Rational(9, 16), b: sp.Rational(36, 125), q: sp.Rational(5, 24), H0: sp.Rational(2, 3), H1: sp.Rational(3, 5)}))
    # The direct Cayley values above are for B=3.
    assert named_obstruction == sp.Rational(10249528643, 7684875000)
    named_average = sp.factor(average.subs({d: 20, y: sp.Rational(9, 16), b: sp.Rational(36, 125), q: sp.Rational(5, 24), H0: sp.Rational(2, 3), H1: sp.Rational(3, 5)}))
    assert named_average == sp.Rational(443845801, 614790000)

    exterior_rows = {}
    for n in range(1, 31):
        direct = sum(((r + 1) * eta3(n, r) for r in range(1, n + 1)), Q(0))
        closed = Q(3, 2) * Q((n + 1)**n * (n + 2) * (n + 3), (n + 4)**(n + 2))
        assert direct == closed <= Q(36, 125)
        if n in (1, 2, 5, 30):
            exterior_rows[f"n{n}"] = qstr(direct)

    n = sp.symbols("n", integer=True, positive=True)
    exterior_upper = 3 * (n + 1)**2 * (n + 2) * (n + 3) / ((n + 4)**2 * (17 * n**2 + n + 2))
    exterior_slack = sp.factor(sp.Rational(36, 125) - exterior_upper)
    expected_exterior_slack = 3 * (n - 1) * (79 * n**3 + 848 * n**2 + 2107 * n + 366) / (125 * (n + 4)**2 * (17 * n**2 + n + 2))
    assert sp.simplify(exterior_slack - expected_exterior_slack) == 0

    G = sp.Matrix([
        [sp.Rational(1, 2), 0, 0],
        [0, sp.Rational(1, 5), -sp.sqrt(6) / 10],
        [0, -sp.sqrt(6) / 10, sp.Rational(18, 35)],
    ])
    rho = (25 + sp.sqrt(415)) / 70
    assert rho in G.eigenvals()
    assert 9 * 415 < 65**2
    eta0 = Q(3, 2) / w(4)
    assert eta0 == Q(9, 16)
    assert sp.simplify(sp.Rational(3, 8) - 9 * (25 + sp.sqrt(415)) / 1120) > 0
    assert sp.factor(b1_average.subs(d, 1)) == sp.Rational(2957, 23040)

    payload = {
        "schema": "M197-independent-symbolic-v1",
        "python": "SymPy exact arithmetic",
        "sympy": sp.__version__,
        "seed": None,
        "closed_average_identity": True,
        "b_derivative": qstr(db),
        "q_second_derivative": qstr(q_second),
        "qstar": qstr(qstar),
        "positive_y_table": table,
        "main_shifted_coefficients_ascending": main_shift,
        "B1_average": qstr(b1_average),
        "B1_slack_numerator": qstr(b1_num),
        "named_obstruction": qstr(named_obstruction),
        "named_degree_average": qstr(named_average),
        "exterior_rows": exterior_rows,
        "exterior_slack": qstr(exterior_slack),
        "n0": {
            "eta": qstr(eta0),
            "rho": qstr(rho),
            "B1_nominal_history": "2957/23040",
            "charge_ceiling_before_3over8": "9*(25+sqrt(415))/1120",
        },
        "assertions": {
            "raw_history_average_matches_closed_form": True,
            "B_ge_2_optimization_certificates_pass": True,
            "B1_certificate_passes": True,
            "pointwise_obstruction_but_average_passes": True,
            "exterior_includes_r_equals_n": True,
            "n0_exact_matrix_history_passes": True,
            "killed_a_equals_d_excluded": True,
        },
    }
    args.output.write_text(dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
