#!/usr/bin/env python3
"""Standalone exact certificate for the M216 Bernstein-envelope obstruction."""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path

UPoly = tuple[Q, ...]
BPoly = dict[tuple[int, int], Q]


def trim(a: list[Q] | tuple[Q, ...]) -> UPoly:
    out = list(a)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def uadd(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def uscale(a: UPoly, c: Q) -> UPoly:
    return trim([c * x for x in a])


def umul(a: UPoly, b: UPoly) -> UPoly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def umonomial(n: int, c: Q = Q(1)) -> UPoly:
    return tuple([Q(0)] * n + [c])


def bclean(a: BPoly) -> BPoly:
    return {ij: c for ij, c in a.items() if c}


def badd(a: BPoly, b: BPoly) -> BPoly:
    out = dict(a)
    for ij, c in b.items():
        out[ij] = out.get(ij, Q(0)) + c
    return bclean(out)


def bscale(a: BPoly, c: Q) -> BPoly:
    return bclean({ij: c * x for ij, x in a.items()})


def bouter(a: UPoly, b: UPoly) -> BPoly:
    return bclean({
        (i, j): x * y
        for i, x in enumerate(a)
        for j, y in enumerate(b)
    })


def bmul_separable(a: BPoly, left: UPoly, right: UPoly) -> BPoly:
    out: BPoly = {}
    for (i, j), c in a.items():
        for r, x in enumerate(left):
            for t, y in enumerate(right):
                if x and y:
                    out[i + r, j + t] = out.get((i + r, j + t), Q(0)) + c * x * y
    return bclean(out)


def rise(x: int, n: int) -> int:
    return math.prod(range(x, x + n))


def beta_moment(kappa: int, deficit: int, n: int) -> Q:
    return Q(rise(deficit, n), rise(kappa, n))


def beta_expect(a: UPoly, kappa: int, deficit: int) -> Q:
    return sum((c * beta_moment(kappa, deficit, i)
                for i, c in enumerate(a)), Q(0))


@functools.lru_cache(None)
def w(n: int) -> Q:
    return Q(n ** (n - 1), math.factorial(n))


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


@functools.lru_cache(None)
def comps(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1)
                 for tail in comps(n - a))


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
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources
        if len(source) >= 2
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    }, key=lambda x: (len(x), x))
    return tuple(
        (endpoint, tuple(source for source in sources
                         if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


def point_context(source: tuple[int, ...], bottom: int) -> UPoly:
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return umonomial(degree - 1, Q(degree))
    split = qsplit(last - 1, bottom)
    out = [Q(0)] * (degree + 1)
    out[0], out[degree] = split, -split
    return trim(out)


@functools.lru_cache(None)
def basin_currents(s: int, bottom: int):
    q = qsplit(s, bottom)
    rows = []
    for endpoint, sources in basin_structure(s):
        current: UPoly = (Q(0),)
        for source in sources:
            centered = uadd(point_context(source, bottom), (Q(-q),))
            current = uadd(current, uscale(centered, rho(source)))
        rows.append((current, Q(len(endpoint)) * rho(endpoint)))
    return tuple(rows)


@functools.lru_cache(None)
def reset_kernel(s: int, bottom: int) -> BPoly:
    q = qsplit(s, bottom)
    out: BPoly = {}
    for current, capacity in basin_currents(s, bottom):
        out = badd(out, bscale(bouter(current, current), Q(1) / (q * capacity)))
    return out


@functools.lru_cache(None)
def cayley(n: int, p: int) -> Q:
    if (n, p) == (0, 0):
        return Q(1)
    if not 1 <= p <= n:
        return Q(0)
    return Q(p * n ** (n - p), n * math.factorial(n - p))


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


def likelihood(degree: int, a: int) -> UPoly:
    out = [Q(0)] * (degree + 1)
    for r in range(degree - a + 1):
        out[a + r] += Q(
            math.comb(degree, a)
            * math.comb(degree - a, r)
            * (-1) ** r
        )
    return trim(out)


def attachment(kappa: int, deficit: int, degree: int, a: int) -> Q:
    return (
        Q(math.comb(degree, a))
        * rise(deficit, a)
        * rise(kappa - deficit, degree - a)
        / rise(kappa, degree)
    )


@functools.lru_cache(None)
def signed_kernel(s: int, kappa: int, deficit: int, bottom: int) -> BPoly:
    q = qsplit(s, bottom)
    out = dict(reset_kernel(s, bottom))
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        eta = mass * qsplit(last - 1, bottom) / q
        for a in range(degree):  # a=degree is killed exactly
            pi = attachment(kappa, deficit, degree, a)
            child = signed_kernel(
                last - 1, kappa + degree, deficit + a, bottom
            )
            like = likelihood(degree, a)
            out = badd(
                out,
                bscale(bmul_separable(child, like, like), eta / pi),
            )
    return bclean(out)


def monomial_to_bernstein(kernel: BPoly, degree: int) -> list[list[Q]]:
    out = [[Q(0) for _ in range(degree + 1)]
           for _ in range(degree + 1)]
    for (i, j), c in kernel.items():
        assert i <= degree and j <= degree
        for a in range(i, degree + 1):
            left = Q(math.comb(a, i), math.comb(degree, i))
            for b in range(j, degree + 1):
                right = Q(math.comb(b, j), math.comb(degree, j))
                out[a][b] += c * left * right
    return out


def q_rank_one(feature: UPoly) -> Q:
    centered = umul((Q(-1, 2), Q(1)), feature)
    return (
        beta_expect(umul(feature, feature), 2, 1)
        - 12 * beta_expect(centered, 2, 1) ** 2
    )


def q_kernel(kernel: BPoly) -> Q:
    centered_moments = [
        beta_moment(2, 1, i + 1) - Q(1, 2) * beta_moment(2, 1, i)
        for i in range(7)
    ]
    trace = sum(
        (c * beta_moment(2, 1, i + j) for (i, j), c in kernel.items()),
        Q(0),
    )
    subtraction = 12 * sum(
        (c * centered_moments[i] * centered_moments[j]
         for (i, j), c in kernel.items()),
        Q(0),
    )
    return trace - subtraction


def qstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_hash(a: list[list[Q]]) -> str:
    encoded = ";".join(
        f"{i},{j}:{x.numerator}/{x.denominator}"
        for i, row in enumerate(a)
        for j, x in enumerate(row)
    )
    return hashlib.sha256(encoded.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    # Three fixed algebra checks of exact Bernstein multiplication.
    for d, a, ell, j in ((1, 0, 1, 0), (2, 1, 3, 1), (3, 0, 2, 2)):
        ratio = Q(
            math.comb(d, a) * math.comb(ell, j),
            math.comb(d + ell, a + j),
        )
        assert umul(likelihood(d, a), likelihood(ell, j)) == uscale(
            likelihood(d + ell, a + j), ratio
        )

    bottom, excess, kappa, deficit = 1, 6, 2, 1
    s = bottom + excess
    kernel = signed_kernel(s, kappa, deficit, bottom)
    assert len(kernel) == 49
    assert all(kernel.get((i, j), Q(0)) == kernel.get((j, i), Q(0))
               for i in range(7) for j in range(7))
    coeff = monomial_to_bernstein(kernel, excess)
    assert all(coeff[i][j] == coeff[j][i]
               for i in range(7) for j in range(7))

    weights = [q_rank_one(likelihood(6, j)) for j in range(7)]
    expected_weights = [
        Q(433, 10192), Q(747, 28028), Q(3491, 112112), Q(100, 3003),
        Q(3491, 112112), Q(747, 28028), Q(433, 10192),
    ]
    assert weights == expected_weights

    signs = [-1, -1, -1, 1, 1, 1, 1]
    radii = [
        Q(1, 5), Q(4, 25), Q(17, 100), Q(9, 50),
        Q(17, 100), Q(4, 25), Q(1, 5),
    ]
    vector = [Q(signs[j]) * radii[j] for j in range(7)]
    remainders = [weights[j] - radii[j] ** 2 for j in range(7)]
    expected_remainders = [
        Q(633, 254800), Q(18427, 17517500), Q(39213, 17517500),
        Q(6757, 7507500), Q(39213, 17517500),
        Q(18427, 17517500), Q(633, 254800),
    ]
    assert remainders == expected_remainders
    assert all(x >= 0 for x in remainders)

    dual = [
        [
            vector[i] * vector[j] + (remainders[i] if i == j else Q(0))
            for j in range(7)
        ]
        for i in range(7)
    ]
    assert [dual[j][j] for j in range(7)] == weights

    objective = sum(
        (coeff[i][j] * dual[i][j] for i in range(7) for j in range(7)),
        Q(0),
    )
    q = qsplit(s, bottom)
    budget = 1 - q
    margin = objective - budget
    expected_objective = Q(
        27574523089250503170656957870808157889213,
        48209994003606915089647408250880000000000,
    )
    expected_margin = Q(
        1000948704365931347999936328408157889213,
        48209994003606915089647408250880000000000,
    )
    assert q == Q(117649, 262144)
    assert budget == Q(144495, 262144)
    assert objective == expected_objective
    assert margin == expected_margin > 0

    actual_t1 = q_kernel(kernel)
    actual_slack = budget - actual_t1
    assert actual_t1 == Q(
        100831060869578347854833692341308821,
        459142800034351572282356269056000000,
    )
    assert actual_slack == Q(
        152250599938846145694280798538691179,
        459142800034351572282356269056000000,
    )
    assert actual_slack > 0

    kernel_encoded = ";".join(
        f"{i},{j}:{c.numerator}/{c.denominator}"
        for (i, j), c in sorted(kernel.items())
    )
    payload = {
        "schema": "M216-Bernstein-envelope-obstruction-v1",
        "python": platform.python_version(),
        "seed": None,
        "method": "one exact Fraction row; no scan; no predecessor import",
        "state_B_L_kappa_D": [bottom, excess, kappa, deficit],
        "exact_recursion": {
            "eta_over_pi": True,
            "killed_a_equals_d_absent": True,
            "kernel_terms": len(kernel),
            "kernel_sha256": hashlib.sha256(kernel_encoded.encode()).hexdigest(),
            "bernstein_coefficient_sha256": matrix_hash(coeff),
        },
        "dual_certificate": {
            "weights": [qstr(x) for x in weights],
            "signs": signs,
            "radii": [qstr(x) for x in radii],
            "diagonal_remainders": [qstr(x) for x in remainders],
            "psd_reason": "X=vv^T+diag(nonnegative remainders)",
            "q": qstr(q),
            "budget": qstr(budget),
            "objective": qstr(objective),
            "positive_excess": qstr(margin),
        },
        "actual_kernel": {
            "T1": qstr(actual_t1),
            "positive_budget_slack": qstr(actual_slack),
            "contraction_counterexample": False,
        },
        "all_checks_pass": True,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "all_checks_pass": True,
        "dual_positive_excess": qstr(margin),
        "actual_positive_slack": qstr(actual_slack),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
