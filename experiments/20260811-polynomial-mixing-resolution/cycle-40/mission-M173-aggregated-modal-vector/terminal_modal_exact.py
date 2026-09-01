#!/usr/bin/env python3
"""Compact exact audits for M173; standard library, deterministic, no scan."""

from __future__ import annotations

import argparse
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


Poly = tuple[Q, ...]


def trim(p: list[Q] | tuple[Q, ...]) -> Poly:
    out = list(p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(p: Poly, q: Poly) -> Poly:
    out = [Q(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def scale(p: Poly, x: Q) -> Poly:
    return trim([x * y for y in p])


def mul(p: Poly, q: Poly) -> Poly:
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def rise(x: int, n: int) -> int:
    return math.prod(range(x, x + n)) if n else 1


def moment(alpha: int, beta: int, degree: int) -> Q:
    return Q(rise(alpha, degree), rise(alpha + beta, degree))


def expect(p: Poly, alpha: int, beta: int) -> Q:
    return sum((x * moment(alpha, beta, i) for i, x in enumerate(p)), Q(0))


def inner(p: Poly, q: Poly, alpha: int, beta: int) -> Q:
    return expect(mul(p, q), alpha, beta)


def likelihood(d: int, a: int) -> Poly:
    out = [Q(0)] * (d + 1)
    for j in range(d - a + 1):
        out[a + j] += Q(
            math.comb(d, a) * math.comb(d - a, j) * ((-1) ** j)
        )
    return trim(out)


def beta_binomial(kappa: int, deficit: int, d: int, a: int) -> Q:
    return Q(
        math.comb(d, a)
        * rise(deficit, a)
        * rise(kappa - deficit, d - a),
        rise(kappa, d),
    )


def rec(x: Q) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def r_charge(d: int) -> Q:
    central_ratio = Q(4**d, math.comb(2 * d, d))
    return (
        Q(d + 1, 2 * d + 1) * (central_ratio - 1)
        - Q(d, d + 2)
        + Q(3 * d * d, (d + 1) * (d + 2) ** 2)
    )


def cayley(n: int, r: int) -> Q:
    if (n, r) == (0, 0):
        return Q(1)
    if r == n:
        return Q(1)
    return Q(r * n ** (n - r - 1), math.factorial(n - r))


def w(n: int) -> Q:
    return Q(n ** (n - 1), math.factorial(n))


def eta(n: int, r: int) -> Q:
    return cayley(n, r) / (math.factorial(r + 1) * w(n + 2))


def vector_inner(xs: tuple[Poly, ...], ys: tuple[Poly, ...], a: int, b: int) -> Q:
    return sum((inner(x, y, a, b) for x, y in zip(xs, ys)), Q(0))


def vector_expect(xs: tuple[Poly, ...], a: int, b: int) -> tuple[Q, ...]:
    return tuple(expect(x, a, b) for x in xs)


def dot(x: tuple[Q, ...], y: tuple[Q, ...]) -> Q:
    return sum((a * b for a, b in zip(x, y)), Q(0))


def main() -> dict[str, object]:
    failures: list[str] = []

    # One asymmetric two-coordinate audit of every AMV term.
    kappa, deficit, d, obs = 5, 2, 3, 1
    parent_alpha, parent_beta = deficit, kappa - deficit
    child_alpha = deficit + obs
    child_beta = kappa - deficit + d - obs
    p = Q(deficit, kappa)
    p_child = Q(child_alpha, child_alpha + child_beta)
    delta = p_child - p
    var = Q(deficit * (kappa - deficit), kappa * kappa * (kappa + 1))
    var_child = Q(
        child_alpha * child_beta,
        (child_alpha + child_beta) ** 2 * (child_alpha + child_beta + 1),
    )
    like = likelihood(d, obs)
    pi = beta_binomial(kappa, deficit, d, obs)
    if expect(like, parent_alpha, parent_beta) != pi:
        failures.append("beta-binomial likelihood normalization")
    phi = ((Q(2), Q(-3), Q(1), Q(4)), (Q(-1), Q(5), Q(2)))
    mean = vector_expect(phi, child_alpha, child_beta)
    xpoly = (Q(-p_child), Q(1))
    centered = tuple(mul(xpoly, f) for f in phi)
    cov = vector_expect(centered, child_alpha, child_beta)
    z = tuple(
        add(add(f, (Q(-m),)), scale(xpoly, -c / var_child))
        for f, m, c in zip(phi, mean, cov)
    )
    if vector_expect(z, child_alpha, child_beta) != (Q(0), Q(0)):
        failures.append("Z mean orthogonality")
    if vector_expect(tuple(mul(xpoly, f) for f in z), child_alpha, child_beta) != (
        Q(0),
        Q(0),
    ):
        failures.append("Z first-mode orthogonality")

    exterior = Q(7, 13)
    lifted = tuple(scale(mul(like, f), Q(1)) for f in phi)
    trace_direct = exterior / pi * vector_inner(
        lifted, lifted, parent_alpha, parent_beta
    )
    parent_x = (Q(-p), Q(1))
    parent_cov_unscaled = vector_expect(
        tuple(mul(parent_x, f) for f in lifted), parent_alpha, parent_beta
    )
    first_direct = exterior / pi * dot(parent_cov_unscaled, parent_cov_unscaled) / var
    q_direct = trace_direct - first_direct

    lam0 = expect(like, child_alpha, child_beta)
    lam1 = expect(mul(like, xpoly), child_alpha, child_beta)
    lam2 = expect(mul(mul(like, xpoly), xpoly), child_alpha, child_beta)
    z0 = vector_expect(tuple(mul(like, f) for f in z), child_alpha, child_beta)
    z1 = vector_expect(
        tuple(mul(mul(like, xpoly), f) for f in z), child_alpha, child_beta
    )
    z2 = vector_inner(
        tuple(mul(like, f) for f in z), z, child_alpha, child_beta
    )
    trace_six = (
        lam0 * dot(mean, mean)
        + Q(2) * lam1 / var_child * dot(mean, cov)
        + lam2 / (var_child * var_child) * dot(cov, cov)
        + Q(2) * dot(mean, z0)
        + Q(2) / var_child * dot(cov, z1)
        + z2
    )
    first_formula = pi / var * dot(
        tuple(delta * m + c for m, c in zip(mean, cov)),
        tuple(delta * m + c for m, c in zip(mean, cov)),
    )
    q_formula = exterior * (trace_six - first_formula)
    if trace_direct != exterior * trace_six:
        failures.append("six-term trace expansion")
    if first_direct != exterior * first_formula:
        failures.append("delta-M-plus-C subtraction")
    if q_direct != q_formula:
        failures.append("complete branch AMV identity")

    # Unrestricted operator nonclosure witness under child Beta(1,2).
    p2 = (Q(1, 10), Q(-4, 5), Q(1))
    p3 = (Q(-1, 35), Q(3, 7), Q(-9, 7), Q(1))
    witness_rows = []
    for degree, poly, expected_norm, expected_charge in (
        (2, p2, Q(1, 300), Q(18, 35)),
        (3, p3, Q(1, 4900), Q(32, 63)),
    ):
        norm = inner(poly, poly, 1, 2)
        orth = (expect(poly, 1, 2), inner((Q(-1, 3), Q(1)), poly, 1, 2))
        charge = inner((Q(1), Q(-1)), mul(poly, poly), 1, 2) / norm
        if norm != expected_norm or orth != (Q(0), Q(0)) or charge != expected_charge:
            failures.append(f"operator witness degree {degree}")
        witness_rows.append(
            {"degree": degree, "norm_before_unit_scaling": rec(norm), "charge": rec(charge)}
        )

    # Exact finite bases for the analytic R_d <= 3d/8 proof.
    base_rows = []
    expected_slacks = {
        2: Q(0),
        3: Q(277, 1400),
        4: Q(89, 210),
        5: Q(8579, 12936),
        6: Q(3365, 3696),
        7: Q(89821, 77220),
    }
    for degree, expected in expected_slacks.items():
        charge = r_charge(degree)
        slack = Q(3 * degree, 8) - charge
        if slack != expected or slack < 0:
            failures.append(f"R base degree {degree}")
        base_rows.append({"degree": degree, "R_d": rec(charge), "slack": rec(slack)})

    # Selected exact checks of the Cayley first moment and final aggregate.
    aggregate_rows = []
    for n in (1, 2, 3, 5, 9):
        moment_sum = sum(((r + 1) * eta(n, r) for r in range(1, n + 1)), Q(0))
        moment_closed = Q((n + 1) ** n, (n + 2) ** n)
        aggregate = sum(
            (eta(n, r) * r_charge(r + 1) for r in range(1, n + 1)), Q(0)
        )
        if moment_sum != moment_closed or moment_sum > Q(2, 3):
            failures.append(f"eta moment n={n}")
        if aggregate > Q(1, 4):
            failures.append(f"terminal aggregate n={n}")
        aggregate_rows.append(
            {
                "n": n,
                "eta_first_moment": rec(moment_sum),
                "aggregate": rec(aggregate),
                "quarter_slack": rec(Q(1, 4) - aggregate),
            }
        )

    return {
        "claim": "exact AMV branch identity, finite-summary obstruction, and terminal fresh-sector quarter bound",
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "environment": {
            "python": platform.python_version(),
            "dependencies": "Python standard library only",
            "seed": None,
        },
        "amv_audit": {
            "parent": [kappa, deficit],
            "degree": d,
            "retained_observation": obs,
            "pi": rec(pi),
            "exterior": rec(exterior),
            "trace": rec(trace_direct),
            "first_mode": rec(first_direct),
            "branch_T1": rec(q_direct),
        },
        "operator_witnesses": witness_rows,
        "R_base_rows": base_rows,
        "aggregate_rows": aggregate_rows,
        "counts": {
            "six_term_vector_identities": 3,
            "operator_witnesses": len(witness_rows),
            "R_base_rows": len(base_rows),
            "selected_aggregate_rows": len(aggregate_rows),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    raise SystemExit(0 if result["status"] == "pass" else 1)
