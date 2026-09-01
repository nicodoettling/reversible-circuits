#!/usr/bin/env python3
"""Independent exact checks for the M193 h=3 coupled trace aggregate.

Standard library only; no predecessor imports and no state enumeration.
The universal inequalities are certified analytically in
``coupled_trace_theorem.md``.  This checker verifies the closed average
against direct beta integration on the named bounded grid and regenerates
the decisive integer certificates.
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from json import dumps
from math import comb, factorial
from pathlib import Path


def rising(x: int, n: int) -> Q:
    out = Q(1)
    for j in range(n):
        out *= x + j
    return out


def beta_moment(alpha: int, beta: int, i: int, j: int = 0) -> Q:
    return rising(alpha, i) * rising(beta, j) / rising(alpha + beta, i + j)


def square_expect(coeffs: list[Q], alpha: int, beta: int) -> Q:
    return sum(
        (ci * cj * beta_moment(alpha, beta, i + j)
         for i, ci in enumerate(coeffs)
         for j, cj in enumerate(coeffs)),
        Q(0),
    )


def w(n: int) -> Q:
    return Q(n ** (n - 1), factorial(n))


def likelihood_ratio(alpha: int, beta: int, a: int) -> Q:
    choose = comb(2, a)
    pi = choose * beta_moment(alpha, beta, a, 2 - a)
    second = choose * choose * beta_moment(alpha, beta, 2 * a, 4 - 2 * a)
    return second / pi


def trace_envelope(B: int, d: int, a: int) -> Q:
    """M185's accepted nominal actual-history envelope Sbar_(B,d,a)."""
    k, alpha, beta = d + 2, a + 1, d - a + 1
    y = w(B) / w(B + 1)
    b = w(B) / w(B + 2)
    q = Q(3, 2) * w(B) / w(B + 3)
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
    unary = (
        (1 - p1) * b * (h1 - b / 2)
        + exceptional
        + beta_moment(alpha, beta1, 0, 3) * (1 - y) / (1 - p1)
    )
    return reset + height_one + Q(2, 3) * unary


def closed_average(B: int, d: int) -> Q:
    """Closed form for d^{-1} sum_{a=0}^{d-1} Sbar_(B,d,a)."""
    y = w(B) / w(B + 1)
    b = w(B) / w(B + 2)
    q = Q(3, 2) * w(B) / w(B + 3)
    h0, h1 = Q(B + 1, B + 3), Q(B, B + 2)
    pbar = Q(d + 1, 2 * (d + 2))
    m2 = Q(d + 1, 3 * (d + 3))
    m3 = Q(d + 1, 4 * (d + 4))
    m4 = Q(d + 1, 5 * (d + 5))
    reset = (
        m2 * (Q(2, 3) - (q + y) / 3)
        + Q(2, 3) * m3
        + (Q(1, 2) + y / 6) * m4
        + q * q * (-Q(2, 9) - Q(1, 6) / y)
        + q * (h0 - Q(1, 3) - Q(8, 9) * pbar)
        + y / 6
    )
    height_one = Q(2 * (d + 7), 9 * (d + 4)) * (1 - y)
    numerator = (
        12 * h1 * b * d**3 + 168 * h1 * b * d**2
        + 780 * h1 * b * d + 1200 * h1 * b
        - 3 * b * b * d**3 - 42 * b * b * d**2
        - 195 * b * b * d - 300 * b * b
        - 4 * b * d**3 - 56 * b * d**2 - 212 * b * d - 160 * b
        + 10 * d**3 + 148 * d**2 + 734 * d + 1172
        - y * (8 * d**3 + 120 * d**2 + 664 * d + 1128)
    )
    unary = Q(numerator, 24 * (d + 3) * (d + 4) * (d + 5))
    return reset + height_one + Q(2, 3) * unary


def shift_one(coefficients: list[int]) -> list[int]:
    """Coefficients of P(e+1), inputs and outputs in ascending order."""
    return [
        sum(coefficients[k] * comb(k, j) for k in range(j, len(coefficients)))
        for j in range(len(coefficients))
    ]


def c(n: int, r: int) -> Q:
    if r == n:
        return Q(1)
    return Q(r * n ** (n - r - 1), factorial(n - r))


def eta3(n: int, r: int) -> Q:
    return Q(3, 2) * c(n, r) / (factorial(r + 1) * w(n + 4))


def qstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    grid = {}
    for B in (1, 2, 3, 8, 16):
        rows = []
        for d in range(1, 31):
            direct = sum((trace_envelope(B, d, a) for a in range(d)), Q(0)) / d
            closed = closed_average(B, d)
            assert direct == closed
            assert closed < 1
            rows.append((closed, d))
        maximum, degree = max(rows)
        grid[f"B{B}"] = {"max_d_le_30": degree, "max_average": qstr(maximum)}

    trace_obstruction = trace_envelope(3, 20, 19)
    trace_obstruction_average = closed_average(3, 20)
    assert trace_obstruction > 1 and trace_obstruction_average < 1

    main_shift = shift_one([-1774608, 607388, 3485988, 2534491, 766087, 102561, 4829])
    b1_shift = shift_one([7219256, 9411050, 4228095, 779710, 51529])
    assert main_shift == [5726736, 18788964, 16784028, 6721029, 1351327, 131535, 4829]
    assert b1_shift == [21689640, 20412486, 6876399, 985826, 51529]
    assert all(x > 0 for x in main_shift + b1_shift)

    exterior = {}
    for n in range(1, 31):
        direct = sum(((r + 1) * eta3(n, r) for r in range(1, n + 1)), Q(0))
        closed = Q(3, 2) * Q((n + 1) ** n * (n + 2) * (n + 3), (n + 4) ** (n + 2))
        assert direct == closed and direct <= Q(36, 125)
        if n in (1, 2, 5, 30):
            exterior[f"n{n}"] = qstr(direct)

    eta_n0 = Q(3, 2) / w(4)
    assert eta_n0 == Q(9, 16)
    # rho_1=(25+sqrt(415))/70 < 2/3 iff 9*415 < 65^2.
    assert 9 * 415 < 65 * 65

    b1_formula = Q(
        17591 + 187970 + 679425 + 1233430 + 1075144,
        69120 * 3 * 4 * 5 * 6,
    )
    assert b1_formula == closed_average(1, 1) == Q(2957, 23040)

    result = {
        "schema": "M193-coupled-trace-v1",
        "arithmetic": "standard-library Fraction",
        "seed": None,
        "named_grid": {"B": [1, 2, 3, 8, 16], "d": "1..30", "summary": grid},
        "trace_obstruction": {
            "B3_d20_a19": qstr(trace_obstruction),
            "B3_d20_average": qstr(trace_obstruction_average),
        },
        "analytic_integer_certificates": {
            "main_slack_shifted_ascending": main_shift,
            "B1_slack_shifted_ascending": b1_shift,
        },
        "exterior_rows": exterior,
        "n0": {
            "eta": qstr(eta_n0),
            "rho": "(25+sqrt(415))/70",
            "rho_lt_2over3_certificate": "9*415 < 65^2",
            "B1_d1_nominal_history": qstr(b1_formula),
            "loose_charge_bound": "3/8",
        },
        "assertions": {
            "direct_average_matches_closed_grid": True,
            "all_named_averages_below_one": True,
            "individual_over_one_but_average_below_one": True,
            "shifted_coefficients_positive": True,
            "exterior_identity_and_36over125_bound": True,
            "r_equals_n_included": True,
            "killed_a_equals_d_excluded": True,
            "n0_exact_boundary_checked": True,
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
