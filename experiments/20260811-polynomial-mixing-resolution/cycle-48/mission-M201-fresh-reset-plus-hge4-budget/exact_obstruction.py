#!/usr/bin/env python3
"""Clean-room exact M201 compatibility-obstruction check.

Standard library only and no predecessor imports.  The script reconstructs
the actual-history Gram kernel at the single decisive fresh state B=2,L=4,
decomposes its exact parent T1 by root height, and compares reset+h4 with the
same-L slack left by the accepted h1--h3 upper bounds.
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import lru_cache
from json import dumps
from math import comb, factorial, prod
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and not poly[-1]:
        poly.pop()
    return tuple(poly)


def add(left, right):
    out = [Q(0)] * max(len(left), len(right))
    for j, value in enumerate(left):
        out[j] += value
    for j, value in enumerate(right):
        out[j] += value
    return trim(out)


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, z in enumerate(right):
            out[i + j] += x * z
    return trim(out)


def monomial(degree):
    return tuple([Q(0)] * degree + [Q(1)])


def badd(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Q(0)) + value
    return {key: value for key, value in out.items() if value}


def bscale(kernel, scalar):
    return {key: scalar * value for key, value in kernel.items() if scalar * value}


def outer(left, right):
    return {
        (i, j): x * z
        for i, x in enumerate(left) if x
        for j, z in enumerate(right) if z
    }


def lift(kernel, left, right):
    out = {}
    for (i, j), coefficient in kernel.items():
        for r, x in enumerate(left):
            for t, z in enumerate(right):
                if x and z:
                    out[i + r, j + t] = out.get((i + r, j + t), Q(0)) + coefficient * x * z
    return {key: value for key, value in out.items() if value}


def rising(start, length):
    return prod(range(start, start + length))


def beta_moment(kappa, deficit, degree):
    return Q(rising(deficit, degree), rising(kappa, degree))


def expectation(poly, kappa, deficit):
    return sum((coefficient * beta_moment(kappa, deficit, degree)
                for degree, coefficient in enumerate(poly)), Q(0))


def diagonal(kernel, kappa, deficit):
    return sum((coefficient * beta_moment(kappa, deficit, i + j)
                for (i, j), coefficient in kernel.items()), Q(0))


def bilinear(kernel, left, right, kappa, deficit):
    return sum(
        (coefficient
         * expectation(multiply(monomial(i), left), kappa, deficit)
         * expectation(multiply(monomial(j), right), kappa, deficit)
         for (i, j), coefficient in kernel.items()),
        Q(0),
    )


@lru_cache(None)
def w(n):
    return Q(n ** (n - 1), factorial(n))


@lru_cache(None)
def compositions(total):
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


def qsplit(s, bottom):
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


def rho(source):
    return prod(w(part) for part in source) / (factorial(len(source)) * w(sum(source) + 1))


def in_basin(source, endpoint):
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@lru_cache(None)
def basin_structure(s):
    sources = compositions(s)
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources if len(source) >= 2
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    })
    return tuple(
        (endpoint, tuple(source for source in sources if in_basin(source, endpoint)))
        for endpoint in endpoints
    )


def point_context(source, bottom):
    degree, last = len(source), source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return tuple([Q(0)] * (degree - 1) + [Q(degree)])
    out = [Q(0)] * (degree + 1)
    out[0] = qsplit(last - 1, bottom)
    out[degree] = -out[0]
    return trim(out)


@lru_cache(None)
def basin_currents(s, bottom):
    q = qsplit(s, bottom)
    rows = []
    for endpoint, sources in basin_structure(s):
        current = (Q(0),)
        for source in sources:
            centered = add(point_context(source, bottom), (Q(-q),))
            current = add(current, scale(centered, rho(source)))
        rows.append((current, Q(len(endpoint)) * rho(endpoint)))
    return tuple(rows)


@lru_cache(None)
def reset_kernel(s, bottom):
    q = qsplit(s, bottom)
    out = {}
    for current, capacity in basin_currents(s, bottom):
        out = badd(out, bscale(outer(current, current), Q(1) / (q * capacity)))
    return out


def cayley(total, parts):
    if (total, parts) == (0, 0):
        return Q(1)
    if not 1 <= parts <= total:
        return Q(0)
    return Q(parts * total ** (total - parts), total * factorial(total - parts))


@lru_cache(None)
def root_groups(s):
    rows = []
    for degree in range(1, s + 1):
        for last in range(1, s + 1):
            mass = w(last) * cayley(s - last, degree - 1) / (factorial(degree) * w(s + 1))
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return tuple(rows)


def attachment(kappa, deficit, degree, observed):
    return Q(comb(degree, observed) * rising(deficit, observed)
             * rising(kappa - deficit, degree - observed), rising(kappa, degree))


def likelihood(degree, observed):
    out = [Q(0)] * (degree + 1)
    for extra in range(degree - observed + 1):
        out[observed + extra] += Q(
            comb(degree, observed) * comb(degree - observed, extra) * (-1) ** extra
        )
    return trim(out)


@lru_cache(None)
def history_kernel(s, kappa, deficit, bottom):
    q = qsplit(s, bottom)
    out = dict(reset_kernel(s, bottom))
    for degree, last, mass in root_groups(s):
        if last <= bottom or last - 1 < 2:
            continue
        exterior = mass * qsplit(last - 1, bottom) / q
        for observed in range(degree):  # observed=degree is killed
            probability = attachment(kappa, deficit, degree, observed)
            child = history_kernel(last - 1, kappa + degree, deficit + observed, bottom)
            like = likelihood(degree, observed)
            out = badd(out, bscale(lift(child, like, like), exterior / probability))
    return out


def t1(kernel, kappa, deficit):
    mean = Q(deficit, kappa)
    center = (-mean, Q(1))
    variance = beta_moment(kappa, deficit, 2) - mean * mean
    return diagonal(kernel, kappa, deficit) - bilinear(kernel, center, center, kappa, deficit) / variance


def first_level_by_height(B, L):
    s, kappa, deficit = B + L, 2, 1
    q = qsplit(s, B)
    result = {"reset": t1(reset_kernel(s, B), kappa, deficit)}
    for degree, last, mass in root_groups(s):
        if last <= B or last - 1 < 2:
            continue
        exterior = mass * qsplit(last - 1, B) / q
        height = last - B
        for observed in range(degree):
            probability = attachment(kappa, deficit, degree, observed)
            child = history_kernel(last - 1, kappa + degree, deficit + observed, B)
            like = likelihood(degree, observed)
            branch = bscale(lift(child, like, like), exterior / probability)
            result[height] = result.get(height, Q(0)) + t1(branch, kappa, deficit)
    return result


def c(total, parts):
    if parts == total:
        return Q(1)
    return Q(parts * total ** (total - parts - 1), factorial(total - parts))


def R(degree):
    return (
        Q(degree + 1, 2 * degree + 1) * (Q(4**degree, comb(2 * degree, degree)) - 1)
        - Q(degree, degree + 2)
        + Q(3 * degree * degree, (degree + 1) * (degree + 2)**2)
    )


def terminal_coefficient(n):
    return sum(
        (c(n, r) * R(r + 1) / (factorial(r + 1) * w(n + 2))
         for r in range(1, n + 1)),
        Q(0),
    )


def record(value):
    return {"exact": str(value), "decimal": float(value)}


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    B, L = 2, 4
    q = qsplit(B + L, B)
    q0 = w(B) / w(B + 1)
    h1_coefficient = terminal_coefficient(L - 1)
    h1_reserved = (1 - q0) * h1_coefficient
    m2 = Q((L - 1) ** (L - 2) * L, (L + 1) ** (L - 1))
    h2_reserved = Q(2, 3) * m2
    n3 = L - 3
    m3 = Q(3, 2) * Q((n3 + 1)**n3 * (n3 + 2) * (n3 + 3), (n3 + 4) ** (n3 + 2))
    h3_reserved = Q(3, 4) * m3
    delta = 1 - q - h1_reserved - h2_reserved - h3_reserved

    pieces = first_level_by_height(B, L)
    total = sum(pieces.values(), Q(0))
    reset_tail = pieces["reset"] + pieces[4]
    obstruction = reset_tail - delta

    assert q == Q(26250, 117649) and q0 == Q(2, 3)
    assert h1_coefficient == Q(3299, 18750)
    assert h1_reserved == Q(3299, 56250)
    assert h2_reserved == Q(24, 125) and h3_reserved == Q(27, 125)
    assert delta == Q(293289307, 945393750)
    assert pieces == {
        "reset": Q(6628367198857337, 21450464220937500),
        1: Q(0),
        2: Q(22259, 1575000),
        3: Q(6974311, 300000000),
        4: Q(1735419680239, 29524500000000),
    }
    assert obstruction == Q(480024264873449410111, 8339940489100500000000) > 0
    assert total == Q(422384074903914714287, 1042492561137562500000)
    assert total < 1 - q

    result = {
        "schema": "M201-compatibility-obstruction-v1",
        "arithmetic": "standard-library Fraction",
        "seed": None,
        "state": {"B": B, "L": L, "s": B + L, "kappa": 2, "D": 1},
        "parent": {"q": record(q), "budget_1_minus_q": record(1 - q)},
        "compatible_reservations": {
            "q0": record(q0),
            "h1_operator_coefficient": record(h1_coefficient),
            "h1_bound": record(h1_reserved),
            "h2_bound": record(h2_reserved),
            "h3_bound": record(h3_reserved),
            "remaining_delta": record(delta),
        },
        "exact_actual_T1": {
            "reset": record(pieces["reset"]),
            "h1": record(pieces[1]),
            "h2": record(pieces[2]),
            "h3": record(pieces[3]),
            "h4": record(pieces[4]),
            "total": record(total),
            "true_budget_slack": record(1 - q - total),
        },
        "obstruction": {
            "reset_plus_h4_minus_reserved_delta": record(obstruction),
            "route_refuted": "independent reservation of accepted h1-h3 bounds",
            "not_refuted": "true parent T1<=1-q",
        },
        "assertions": {
            "killed_observation_excluded": True,
            "all_history_cross_terms_retained_by_exact_Gram_T1": True,
            "compatible_reservation_is_same_L": True,
            "reset_plus_h4_exceeds_delta": True,
            "exact_total_remains_below_true_budget": True,
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
