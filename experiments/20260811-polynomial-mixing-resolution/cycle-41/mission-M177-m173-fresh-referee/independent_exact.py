#!/usr/bin/env python3
"""Independent compact rational audit of frozen M173; no predecessor imports."""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


Poly = tuple[F, ...]


def trim(values: list[F] | tuple[F, ...]) -> Poly:
    out = list(values)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(p: Poly, q: Poly) -> Poly:
    out = [F(0)] * max(len(p), len(q))
    for i, value in enumerate(p):
        out[i] += value
    for i, value in enumerate(q):
        out[i] += value
    return trim(out)


def scale(p: Poly, value: F) -> Poly:
    return trim([value * coefficient for coefficient in p])


def multiply(p: Poly, q: Poly) -> Poly:
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, left in enumerate(p):
        for j, right in enumerate(q):
            out[i + j] += left * right
    return trim(out)


def rising(x: int, n: int) -> int:
    return math.prod(range(x, x + n)) if n else 1


def beta_moment(alpha: int, beta: int, degree: int) -> F:
    return F(rising(alpha, degree), rising(alpha + beta, degree))


def expectation(p: Poly, alpha: int, beta: int) -> F:
    return sum(
        (coefficient * beta_moment(alpha, beta, i) for i, coefficient in enumerate(p)),
        F(0),
    )


def inner(p: Poly, q: Poly, alpha: int, beta: int) -> F:
    return expectation(multiply(p, q), alpha, beta)


def likelihood(d: int, a: int) -> Poly:
    # binom(d,a) u^a (1-u)^(d-a)
    out = [F(0)] * (d + 1)
    for j in range(d - a + 1):
        out[a + j] += F(math.comb(d, a) * math.comb(d - a, j) * (-1) ** j)
    return trim(out)


def vector_expect(polys: tuple[Poly, ...], alpha: int, beta: int) -> tuple[F, ...]:
    return tuple(expectation(poly, alpha, beta) for poly in polys)


def dot(left: tuple[F, ...], right: tuple[F, ...]) -> F:
    return sum((x * y for x, y in zip(left, right)), F(0))


def vector_inner(
    left: tuple[Poly, ...], right: tuple[Poly, ...], alpha: int, beta: int
) -> F:
    return sum((inner(x, y, alpha, beta) for x, y in zip(left, right)), F(0))


def record(value: F) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def w(n: int) -> F:
    return F(n ** (n - 1), math.factorial(n))


def cayley(n: int, r: int) -> F:
    if (n, r) == (0, 0) or r == n:
        return F(1)
    return F(r * n ** (n - r - 1), math.factorial(n - r))


def eta(n: int, r: int) -> F:
    return cayley(n, r) / (math.factorial(r + 1) * w(n + 2))


def split(B: int, L: int) -> F:
    return w(L + 1) * w(B) / w(B + L + 1)


def root_mass(B: int, L: int, r: int) -> F:
    n = L - 1
    return w(B + 1) * cayley(n, r) / (math.factorial(r + 1) * w(B + L + 1))


def r_formula(d: int) -> F:
    central = F(4**d, math.comb(2 * d, d))
    return (
        F(d + 1, 2 * d + 1) * (central - 1)
        - F(d, d + 2)
        + F(3 * d * d, (d + 1) * (d + 2) ** 2)
    )


def q_coordinate(d: int, a: int) -> F:
    like = likelihood(d, a)
    pi = F(1, d + 1)
    trace = inner(like, like, 1, 1) / pi
    centered = (F(-1, 2), F(1))
    covariance = inner(centered, like, 1, 1)
    return trace - covariance * covariance / (pi * F(1, 12))


def run() -> dict[str, object]:
    failures: list[str] = []

    # One asymmetric two-coordinate AMV identity, derived directly from beta moments.
    parent_alpha, parent_beta, d, a = 2, 3, 3, 1
    child_alpha, child_beta = parent_alpha + a, parent_beta + d - a
    p_parent = F(parent_alpha, parent_alpha + parent_beta)
    p_child = F(child_alpha, child_alpha + child_beta)
    delta = p_child - p_parent
    var_parent = F(
        parent_alpha * parent_beta,
        (parent_alpha + parent_beta) ** 2 * (parent_alpha + parent_beta + 1),
    )
    var_child = F(
        child_alpha * child_beta,
        (child_alpha + child_beta) ** 2 * (child_alpha + child_beta + 1),
    )
    like = likelihood(d, a)
    pi = expectation(like, parent_alpha, parent_beta)
    phi = ((F(1), F(-2), F(3), F(1)), (F(-3), F(4), F(0), F(2)))
    child_mean = vector_expect(phi, child_alpha, child_beta)
    child_x = (F(-p_child), F(1))
    child_covariance = vector_expect(
        tuple(multiply(child_x, poly) for poly in phi), child_alpha, child_beta
    )
    residual = tuple(
        add(add(poly, (F(-mean),)), scale(child_x, -cov / var_child))
        for poly, mean, cov in zip(phi, child_mean, child_covariance)
    )
    if vector_expect(residual, child_alpha, child_beta) != (F(0), F(0)):
        failures.append("AMV residual mean")
    if vector_expect(
        tuple(multiply(child_x, poly) for poly in residual), child_alpha, child_beta
    ) != (F(0), F(0)):
        failures.append("AMV residual first moment")

    eta_test = F(11, 23)
    lifted = tuple(multiply(like, poly) for poly in phi)
    trace_parent = eta_test / pi * vector_inner(
        lifted, lifted, parent_alpha, parent_beta
    )
    trace_bayes = eta_test * vector_inner(
        tuple(multiply(like, poly) for poly in phi), phi, child_alpha, child_beta
    )
    if trace_parent != trace_bayes:
        failures.append("eta/pi trace normalization")

    lam0 = expectation(like, child_alpha, child_beta)
    lam1 = expectation(multiply(like, child_x), child_alpha, child_beta)
    lam2 = expectation(
        multiply(multiply(like, child_x), child_x), child_alpha, child_beta
    )
    z0 = vector_expect(
        tuple(multiply(like, poly) for poly in residual), child_alpha, child_beta
    )
    z1 = vector_expect(
        tuple(multiply(multiply(like, child_x), poly) for poly in residual),
        child_alpha,
        child_beta,
    )
    z2 = vector_inner(
        tuple(multiply(like, poly) for poly in residual),
        residual,
        child_alpha,
        child_beta,
    )
    six_terms = (
        lam0 * dot(child_mean, child_mean),
        F(2) * lam1 / var_child * dot(child_mean, child_covariance),
        lam2 / (var_child * var_child) * dot(child_covariance, child_covariance),
        F(2) * dot(child_mean, z0),
        F(2) / var_child * dot(child_covariance, z1),
        z2,
    )
    trace_expanded = eta_test * sum(six_terms, F(0))
    if trace_parent != trace_expanded:
        failures.append("all six AMV trace terms")
    parent_x = (F(-p_parent), F(1))
    lifted_covariance = vector_expect(
        tuple(multiply(parent_x, poly) for poly in lifted), parent_alpha, parent_beta
    )
    first_direct = eta_test / pi * dot(lifted_covariance, lifted_covariance) / var_parent
    shifted = tuple(
        delta * mean + covariance
        for mean, covariance in zip(child_mean, child_covariance)
    )
    first_formula = eta_test * pi * dot(shifted, shifted) / var_parent
    if first_direct != first_formula:
        failures.append("covariance subtraction")

    # The two unrestricted finite-summary witnesses.
    witness_rows: list[dict[str, object]] = []
    for degree, poly, expected_norm, expected_charge in (
        (2, (F(1, 10), F(-4, 5), F(1)), F(1, 300), F(18, 35)),
        (3, (F(-1, 35), F(3, 7), F(-9, 7), F(1)), F(1, 4900), F(32, 63)),
    ):
        norm = inner(poly, poly, 1, 2)
        charge = inner((F(1), F(-1)), multiply(poly, poly), 1, 2) / norm
        orthogonal = (
            expectation(poly, 1, 2),
            inner((F(-1, 3), F(1)), poly, 1, 2),
        )
        if (norm, charge, orthogonal) != (
            expected_norm,
            expected_charge,
            (F(0), F(0)),
        ):
            failures.append(f"finite-summary witness degree {degree}")
        witness_rows.append({"degree": degree, "charge": record(charge)})

    # Exact R_d bases and selected coefficientwise-positivity/max checks.
    expected_slacks = {
        2: F(0),
        3: F(277, 1400),
        4: F(89, 210),
        5: F(8579, 12936),
        6: F(3365, 3696),
        7: F(89821, 77220),
    }
    r_rows: list[dict[str, object]] = []
    for degree, expected_slack in expected_slacks.items():
        coefficients = [q_coordinate(degree, obs) for obs in range(degree)]
        total = sum(coefficients, F(0))
        slack = F(3 * degree, 8) - total
        if min(coefficients) < 0 or total != r_formula(degree) or slack != expected_slack:
            failures.append(f"R_d base or coefficient positivity d={degree}")
        r_rows.append(
            {"degree": degree, "R_d": record(total), "linear_slack": record(slack)}
        )
    varying_norms = (F(2, 7), F(5, 7), F(1, 3), F(4, 5))
    coefficients = tuple(q_coordinate(4, obs) for obs in range(4))
    varying_charge = dot(coefficients, varying_norms)
    max_bound = max(varying_norms) * sum(coefficients, F(0))
    if varying_charge > max_bound:
        failures.append("observation-dependent maximum domination")

    # Exact h=1 exterior cancellation, first moment, and boundary rows.
    exterior_rows: list[dict[str, object]] = []
    for B, L, r in ((2, 2, 1), (3, 4, 1), (3, 4, 3), (5, 5, 2), (5, 5, 4)):
        n = L - 1
        product = root_mass(B, L, r) * split(B, 0) / split(B, L)
        closed = eta(n, r)
        if product != closed:
            failures.append(f"h=1 eta cancellation B={B},L={L},r={r}")
        exterior_rows.append(
            {"B": B, "L": L, "r": r, "eta": record(product), "r_equals_n": r == n}
        )

    aggregate_rows: list[dict[str, object]] = []
    for n in (1, 2, 4, 8):
        first_moment = sum(((r + 1) * eta(n, r) for r in range(1, n + 1)), F(0))
        closed_moment = F((n + 1) ** n, (n + 2) ** n)
        aggregate = sum((eta(n, r) * r_formula(r + 1) for r in range(1, n + 1)), F(0))
        if first_moment != closed_moment or first_moment > F(2, 3) or aggregate > F(1, 4):
            failures.append(f"terminal first moment/quarter bound n={n}")
        aggregate_rows.append(
            {
                "n": n,
                "first_moment": record(first_moment),
                "aggregate": record(aggregate),
            }
        )

    unary_eta = root_mass(2, 1, 0) * split(2, 0) / split(2, 1)
    if unary_eta != 1 or q_coordinate(1, 0) != F(1, 2):
        failures.append("L=1 unary eta or R_1")

    return {
        "claim": "independent audit of M173 AMV algebra and fresh h=1 terminal sector",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "environment": {
            "python": platform.python_version(),
            "dependencies": "Python standard library only",
            "seed": None,
        },
        "amv": {
            "parent_beta": [parent_alpha, parent_beta],
            "degree": d,
            "observation": a,
            "pi": record(pi),
            "six_terms": [record(value) for value in six_terms],
            "trace": record(trace_parent),
            "first_mode": record(first_direct),
            "T1": record(trace_parent - first_direct),
        },
        "operator_witnesses": witness_rows,
        "R_bases": r_rows,
        "varying_norm_max_domination": {
            "charge": record(varying_charge),
            "max_bound": record(max_bound),
        },
        "exterior_rows": exterior_rows,
        "aggregate_rows": aggregate_rows,
        "L1": {"eta": record(unary_eta), "R_1": record(q_coordinate(1, 0))},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(text, end="")
    else:
        args.output.write_text(text, encoding="utf-8")
    raise SystemExit(0 if result["status"] == "pass" else 1)
