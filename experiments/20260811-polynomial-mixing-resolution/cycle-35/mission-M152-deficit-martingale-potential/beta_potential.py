#!/usr/bin/env python3
"""Exact audit of the beta-mixture Jensen potential for M152.

Standard-library only.  Every theorem-critical calculation uses Fraction.
This file imports no predecessor source or output.
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


def trim(a: list[Q] | tuple[Q, ...]) -> Poly:
    b = list(a)
    while len(b) > 1 and not b[-1]:
        b.pop()
    return tuple(b)


def add(a: Poly, b: Poly) -> Poly:
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def scale(a: Poly, c: Q) -> Poly:
    return trim([c * x for x in a])


def mul(a: Poly, b: Poly) -> Poly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def monomial(n: int, c: Q = Q(1)) -> Poly:
    return tuple([Q(0)] * n + [c])


def one_minus_monomial(n: int) -> Poly:
    out = [Q(0)] * (n + 1)
    out[0] = 1
    out[n] -= 1
    return trim(out)


def evaluate(a: Poly, x: Q) -> Q:
    ans = Q(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def rise(x: int, n: int) -> int:
    return math.prod(range(x, x + n))


def beta_expectation(a: Poly, kappa: int, deficit: int) -> Q:
    assert 1 <= deficit < kappa
    return sum(
        (c * Q(rise(deficit, n), rise(kappa, n)) for n, c in enumerate(a)),
        Q(0),
    )


@functools.lru_cache(None)
def w(n: int) -> Q:
    assert n >= 1
    return Q(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in comps(n - a))


@functools.lru_cache(None)
def cayley(n: int, p: int) -> Q:
    if (n, p) == (0, 0):
        return Q(1)
    if not 1 <= p <= n:
        return Q(0)
    return Q(p * n ** (n - p), n * math.factorial(n - p))


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def rho(source: tuple[int, ...]) -> Q:
    return math.prod(w(a) for a in source) / (
        math.factorial(len(source)) * w(sum(source) + 1)
    )


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@functools.lru_cache(None)
def basin_structure(s: int):
    sources = comps(s)
    endpoints = sorted(
        {
            (sum(source[:cut]),) + source[cut:]
            for source in sources
            if len(source) >= 2
            for cut in range(1, len(source))
            if sum(source[:cut]) + source[cut] - 1 >= 2
        },
        key=lambda x: (len(x), x),
    )
    return tuple(
        (endpoint, tuple(source for source in sources if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


def point_context(source: tuple[int, ...], bottom: int) -> Poly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return monomial(degree - 1, Q(degree))
    return scale(one_minus_monomial(degree), qsplit(last - 1, bottom))


@functools.lru_cache(None)
def point_reset(s: int, bottom: int) -> Poly:
    """Pointwise Jensen reward r=A_point/q."""
    q = qsplit(s, bottom)
    ans: Poly = (Q(0),)
    for endpoint, sources in basin_structure(s):
        current: Poly = (Q(0),)
        for source in sources:
            centered = add(point_context(source, bottom), (Q(-q),))
            current = add(current, scale(centered, rho(source)))
        capacity = Q(len(endpoint)) * rho(endpoint)
        ans = add(ans, scale(mul(current, current), Q(1) / (q * capacity)))
    return ans


@functools.lru_cache(None)
def root_groups(s: int) -> tuple[tuple[int, int, Q], ...]:
    rows = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = w(last) * cayley(s - last, degree - 1) / (
                math.factorial(degree) * w(s + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return tuple(rows)


@functools.lru_cache(None)
def phi(bottom: int, excess: int) -> Poly:
    """Minimal beta-mixture/Jensen Bellman integrand."""
    s = bottom + excess
    q = qsplit(s, bottom)
    ans = point_reset(s, bottom)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        child = phi(bottom, last - 1 - bottom)
        coefficient = mass * qsplit(last - 1, bottom) / q
        ans = add(ans, scale(mul(one_minus_monomial(degree), child), coefficient))
    return ans


def attachment(kappa: int, deficit: int, degree: int, x: int) -> Q:
    """Beta-binomial mass for X=d-j."""
    assert 0 <= x <= degree
    return (
        Q(math.comb(degree, x))
        * rise(deficit, x)
        * rise(kappa - deficit, degree - x)
        / rise(kappa, degree)
    )


def contextual(
    degree: int, last: int, kappa: int, deficit: int, bottom: int
) -> Q:
    if last < bottom:
        return Q(0)
    if last == bottom:
        return Q(degree) * rise(deficit, degree - 1) / rise(kappa, degree - 1)
    return qsplit(last - 1, bottom) * (
        1 - Q(rise(deficit, degree), rise(kappa, degree))
    )


@functools.lru_cache(None)
def exact_reset(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    q = qsplit(s, bottom)
    ans = Q(0)
    for endpoint, sources in basin_structure(s):
        current = sum(
            (
                rho(source)
                * (
                    contextual(len(source), source[-1], kappa, deficit, bottom)
                    - q
                )
                for source in sources
            ),
            Q(0),
        )
        ans += current * current / (Q(len(endpoint)) * rho(endpoint))
    return ans


@functools.lru_cache(None)
def exact_h(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    ans = exact_reset(s, kappa, deficit, bottom)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        for x in range(degree):  # x=d-j; x=d, equivalently j=0, is killed.
            ans += (
                mass
                * attachment(kappa, deficit, degree, x)
                * exact_h(last - 1, kappa + degree, deficit + x, bottom)
            )
    return ans


@functools.lru_cache(None)
def discrete_jensen_v(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    """The Jensen Bellman majorant evaluated by the discrete child law."""
    q = qsplit(s, bottom)
    ans = beta_expectation(point_reset(s, bottom), kappa, deficit)
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        child_q = qsplit(last - 1, bottom)
        for x in range(degree):
            ans += (
                mass
                / q
                * child_q
                * attachment(kappa, deficit, degree, x)
                * discrete_jensen_v(
                    last - 1, kappa + degree, deficit + x, bottom
                )
            )
    return ans


def rec(x: Q) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-excess", type=int, default=5)
    parser.add_argument("--max-kappa", type=int, default=128)
    args = parser.parse_args()
    assert 0 <= args.max_excess <= 6
    assert 4 <= args.max_kappa <= 256
    failures: list[dict[str, object]] = []

    # Exact killed-atom Doob identity for monomials through degree six.
    doob_rows = 0
    for kappa in (2, 3, 5, 11, 35):
        for deficit in range(1, kappa):
            for degree in range(1, 7):
                for n in range(7):
                    child_full = sum(
                        (
                            attachment(kappa, deficit, degree, x)
                            * Q(rise(deficit + x, n), rise(kappa + degree, n))
                            for x in range(degree + 1)
                        ),
                        Q(0),
                    )
                    parent = Q(rise(deficit, n), rise(kappa, n))
                    killed = attachment(kappa, deficit, degree, degree) * Q(
                        rise(deficit + degree, n), rise(kappa + degree, n)
                    )
                    retained = child_full - killed
                    latent = parent - Q(rise(deficit, degree + n), rise(kappa, degree + n))
                    if child_full != parent or retained != latent:
                        failures.append(
                            {"kind": "doob", "state": [kappa, deficit, degree, n]}
                        )
                    doob_rows += 1

    # Jensen identities: beta expectations of point contexts are exact
    # contextual means, and the lifted reset dominates the exact reset.
    jensen_rows = []
    for bottom, excess, kappa, deficit in (
        (1, 2, 5, 1),
        (1, 3, 11, 7),
        (2, 1, 33, 31),
        (2, 3, 9, 4),
        (3, 2, 17, 1),
    ):
        s = bottom + excess
        q = qsplit(s, bottom)
        point = beta_expectation(point_reset(s, bottom), kappa, deficit)
        exact = exact_reset(s, kappa, deficit, bottom) / q
        for source in comps(s):
            lifted = beta_expectation(point_context(source, bottom), kappa, deficit)
            direct = contextual(len(source), source[-1], kappa, deficit, bottom)
            if lifted != direct:
                failures.append(
                    {
                        "kind": "point-context",
                        "state": [s, kappa, deficit, bottom],
                        "source": source,
                    }
                )
        if point < exact:
            failures.append({"kind": "jensen", "state": [s, kappa, deficit, bottom]})
        jensen_rows.append(
            {
                "state_s_kappa_D_B": [s, kappa, deficit, bottom],
                "exact_reset_over_q": rec(exact),
                "jensen_reset_over_q": rec(point),
                "jensen_slack": rec(point - exact),
            }
        )

    # Capped right-heavy audit of the globally defined beta potential.
    boundary_rows = []
    first_failure = None
    for bottom in (1, 2, 3):
        for excess in range(args.max_excess + 1):
            s = bottom + excess
            q = qsplit(s, bottom)
            poly = phi(bottom, excess)
            local_first = None
            for kappa in range(2, args.max_kappa + 1):
                value = beta_expectation(poly, kappa, 1)
                margin = value - (1 - q)
                if margin > 0 and local_first is None:
                    local_first = (kappa, value, margin)
                    if first_failure is None:
                        first_failure = (bottom, excess, kappa, value, margin)
            boundary_rows.append(
                {
                    "bottom": bottom,
                    "excess": excess,
                    "degree": len(poly) - 1,
                    "q": rec(q),
                    "first_failure": None
                    if local_first is None
                    else {
                        "kappa": local_first[0],
                        "value": rec(local_first[1]),
                        "margin": rec(local_first[2]),
                    },
                }
            )

    payload = {
        "claim": "beta-mixture Jensen Bellman potential and killed-atom audit",
        "scope": "auxiliary full unweighted reset excursion only",
        "python": platform.python_version(),
        "seed": None,
        "parameters": {"max_excess": args.max_excess, "max_kappa": args.max_kappa},
        "doob_rows": doob_rows,
        "jensen_rows": jensen_rows,
        "boundary_rows": boundary_rows,
        "first_boundary_failure_in_capped_grid": None
        if first_failure is None
        else {
            "bottom": first_failure[0],
            "excess": first_failure[1],
            "kappa": first_failure[2],
            "value": rec(first_failure[3]),
            "margin": rec(first_failure[4]),
        },
        "failure_count": len(failures),
        "failures": failures,
    }

    # One theorem-level exact obstruction to the natural Jensen lift.
    witness_bottom, witness_excess, witness_kappa, witness_deficit = (3, 6, 2, 1)
    witness_s = witness_bottom + witness_excess
    witness_q = qsplit(witness_s, witness_bottom)
    witness_poly = phi(witness_bottom, witness_excess)
    witness_value = beta_expectation(witness_poly, witness_kappa, witness_deficit)
    witness_discrete_value = discrete_jensen_v(
        witness_s, witness_kappa, witness_deficit, witness_bottom
    )
    witness_budget = 1 - witness_q
    witness_margin = witness_value - witness_budget
    witness_reset_lift = beta_expectation(
        point_reset(witness_s, witness_bottom), witness_kappa, witness_deficit
    )
    witness_exact_reset = exact_reset(
        witness_s, witness_kappa, witness_deficit, witness_bottom
    ) / witness_q
    witness_exact_h = exact_h(
        witness_s, witness_kappa, witness_deficit, witness_bottom
    ) / witness_q
    expected_q = Q(3176523, 25000000)
    expected_value = Q(
        200725034388752880197118033887607702918039504603683,
        223395363274892426079078092636160000000000000000000,
    )
    expected_margin = Q(
        5714491495302498676679596453643417785239504603683,
        223395363274892426079078092636160000000000000000000,
    )
    if (
        witness_q != expected_q
        or witness_value != expected_value
        or witness_discrete_value != witness_value
        or witness_margin != expected_margin
        or witness_margin <= 0
        or witness_exact_h > witness_budget
        or witness_value < witness_exact_h
    ):
        failures.append({"kind": "explicit-witness"})
    coefficient_encoding = ";".join(
        f"{c.numerator}/{c.denominator}" for c in witness_poly
    ).encode()
    payload["explicit_obstruction"] = {
        "state_s_kappa_D_B": [witness_s, witness_kappa, witness_deficit, witness_bottom],
        "suffix_excess": witness_excess,
        "q": rec(witness_q),
        "budget_1_minus_q": rec(witness_budget),
        "beta_jensen_value": rec(witness_value),
        "discrete_posterior_value": rec(witness_discrete_value),
        "positive_margin": rec(witness_margin),
        "point_reset_lift": rec(witness_reset_lift),
        "descendant_lift": rec(witness_value - witness_reset_lift),
        "exact_reset_over_q": rec(witness_exact_reset),
        "exact_descendant_over_q": rec(witness_exact_h - witness_exact_reset),
        "exact_H_over_q": rec(witness_exact_h),
        "exact_H_budget_slack": rec(witness_budget - witness_exact_h),
        "phi_degree": len(witness_poly) - 1,
        "phi_coefficients_ascending": [rec(c) for c in witness_poly],
        "phi_coefficient_sha256": hashlib.sha256(coefficient_encoding).hexdigest(),
    }
    payload["failure_count"] = len(failures)
    payload["failures"] = failures
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "failure_count": len(failures),
                "doob_rows": doob_rows,
                "boundary_cases": len(boundary_rows),
                "first_boundary_failure_in_capped_grid": payload[
                    "first_boundary_failure_in_capped_grid"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
