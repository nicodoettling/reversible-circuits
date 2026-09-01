#!/usr/bin/env python3
"""No-import exact referee reconstruction of the two M206 rows.

Standard library only.  Unlike M206's accepted engine, this checker uses
grouped Cayley root masses, not literal ordered-root expansion.  It evaluates
only (B,L)=(2,4),(3,4).
"""

from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from json import dumps
from math import comb, factorial, prod
from pathlib import Path


# Monomial polynomials and bivariate Gram kernels.
def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def padd(left, right):
    out = [Q(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def pscale(poly, scalar):
    return trim(scalar * value for value in poly)


def pmul(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def mono(degree):
    return (Q(0),) * degree + (Q(1),)


def kadd(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Q(0)) + value
    return {key: value for key, value in out.items() if value}


def kscale(kernel, scalar):
    return {key: scalar * value for key, value in kernel.items()
            if scalar * value}


def outer(left, right):
    return {(i, j): x * y
            for i, x in enumerate(left) if x
            for j, y in enumerate(right) if y}


def lift(kernel, left, right):
    out = {}
    for (i, j), gram in kernel.items():
        for a, x in enumerate(left):
            for b, y in enumerate(right):
                if x and y:
                    key = (i + a, j + b)
                    out[key] = out.get(key, Q(0)) + gram * x * y
    return {key: value for key, value in out.items() if value}


# Exact beta moments and first-Jacobi functional on a Gram kernel.
def rising(start, length):
    return prod(range(start, start + length))


def moment(kappa, deficit, degree):
    return Q(rising(deficit, degree), rising(kappa, degree))


def average(poly, kappa, deficit):
    return sum((coefficient * moment(kappa, deficit, degree)
                for degree, coefficient in enumerate(poly)), Q(0))


def diagonal(kernel, kappa, deficit):
    return sum((value * moment(kappa, deficit, i + j)
                for (i, j), value in kernel.items()), Q(0))


def centered_square(kernel, poly, kappa, deficit):
    total = Q(0)
    for (i, j), value in kernel.items():
        left = average(pmul(mono(i), poly), kappa, deficit)
        right = average(pmul(mono(j), poly), kappa, deficit)
        total += value * left * right
    return total


def first_jacobi_charge(kernel, kappa, deficit):
    mean = Q(deficit, kappa)
    center = (-mean, Q(1))
    variance = moment(kappa, deficit, 2) - mean * mean
    return diagonal(kernel, kappa, deficit) - centered_square(
        kernel, center, kappa, deficit
    ) / variance


# Tree/composition law and canonical reset basins.
@cache
def weight(size):
    return Q(size ** (size - 1), factorial(size))


@cache
def compositions(total):
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


def split(total, bottom):
    return weight(total + 1 - bottom) * weight(bottom) / weight(total + 1)


def root_probability(source):
    return prod(weight(part) for part in source) / (
        factorial(len(source)) * weight(sum(source) + 1)
    )


def reaches(source, endpoint):
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@cache
def basins(total):
    sources = compositions(total)
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    })
    return tuple(
        (endpoint, tuple(source for source in sources if reaches(source, endpoint)))
        for endpoint in endpoints
    )


def point_feature(source, bottom):
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return (Q(0),) * (degree - 1) + (Q(degree),)
    value = split(last - 1, bottom)
    out = [Q(0)] * (degree + 1)
    out[0], out[degree] = value, -value
    return trim(out)


@cache
def reset_kernel(total, bottom):
    parent_q = split(total, bottom)
    out = {}
    for endpoint, sources in basins(total):
        current = (Q(0),)
        for source in sources:
            centered = padd(point_feature(source, bottom), (Q(-parent_q),))
            current = padd(current, pscale(centered, root_probability(source)))
        capacity = Q(len(endpoint)) * root_probability(endpoint)
        out = kadd(out, kscale(outer(current, current), Q(1) / (parent_q * capacity)))
    return out


# Grouped Cayley roots: independent of M206's literal root loop.
def cayley(total, parts):
    if (total, parts) == (0, 0):
        return Q(1)
    if not 1 <= parts <= total:
        return Q(0)
    return Q(parts * total ** (total - parts), total * factorial(total - parts))


@cache
def grouped_roots(total):
    rows = []
    for degree in range(1, total + 1):
        for last in range(1, total + 1):
            mass = weight(last) * cayley(total - last, degree - 1) / (
                factorial(degree) * weight(total + 1)
            )
            if mass:
                rows.append((degree, last, mass))
    assert sum((mass for _, _, mass in rows), Q(0)) == 1
    return tuple(rows)


# Shared beta-binomial observation. observed=degree is killed.
def observation_mass(kappa, deficit, degree, observed):
    return Q(
        comb(degree, observed)
        * rising(deficit, observed)
        * rising(kappa - deficit, degree - observed),
        rising(kappa, degree),
    )


def likelihood(degree, observed):
    out = [Q(0)] * (degree + 1)
    for extra in range(degree - observed + 1):
        out[observed + extra] += Q(
            comb(degree, observed)
            * comb(degree - observed, extra)
            * (-1) ** extra
        )
    return trim(out)


@cache
def history_kernel(total, kappa, deficit, bottom):
    parent_q = split(total, bottom)
    out = dict(reset_kernel(total, bottom))
    for degree, last, root_mass in grouped_roots(total):
        if last <= bottom or last - 1 < 2:
            continue
        eta = root_mass * split(last - 1, bottom) / parent_q
        for observed in range(degree):  # observed=degree killed exactly
            pi = observation_mass(kappa, deficit, degree, observed)
            child = history_kernel(
                last - 1, kappa + degree, deficit + observed, bottom
            )
            like = likelihood(degree, observed)
            out = kadd(out, kscale(lift(child, like, like), eta / pi))
    return out


def sector_charges(bottom, height_limit):
    total, kappa, deficit = bottom + height_limit, 2, 1
    parent_q = split(total, bottom)
    pieces = {"reset": first_jacobi_charge(reset_kernel(total, bottom), 2, 1)}
    for degree, last, root_mass in grouped_roots(total):
        if last <= bottom or last - 1 < 2:
            continue
        eta = root_mass * split(last - 1, bottom) / parent_q
        height = last - bottom
        for observed in range(degree):  # killed atom excluded
            pi = observation_mass(2, 1, degree, observed)
            child = history_kernel(last - 1, 2 + degree, 1 + observed, bottom)
            like = likelihood(degree, observed)
            branch = kscale(lift(child, like, like), eta / pi)
            pieces[height] = pieces.get(height, Q(0)) + first_jacobi_charge(
                branch, 2, 1
            )
    assembled = first_jacobi_charge(history_kernel(total, 2, 1, bottom), 2, 1)
    assert assembled == sum(pieces.values(), Q(0))
    return pieces, assembled


# Same-parent accepted h=1,2,3 coefficients.
def prefix_mass(total, parts):
    if parts == total:
        return Q(1)
    return Q(parts * total ** (total - parts - 1), factorial(total - parts))


def terminal_factor(degree):
    return (
        Q(degree + 1, 2 * degree + 1)
        * (Q(4 ** degree, comb(2 * degree, degree)) - 1)
        - Q(degree, degree + 2)
        + Q(3 * degree * degree, (degree + 1) * (degree + 2) ** 2)
    )


def terminal_average(n):
    return sum((
        prefix_mass(n, r) * terminal_factor(r + 1)
        / (factorial(r + 1) * weight(n + 2))
        for r in range(1, n + 1)
    ), Q(0))


def compatible_bounds(bottom, height_limit):
    q = split(bottom + height_limit, bottom)
    q0 = weight(bottom) / weight(bottom + 1)
    u1 = (1 - q0) * terminal_average(height_limit - 1)
    n2 = height_limit - 2
    m2 = Q((n2 + 1) ** n2 * (n2 + 2), (n2 + 3) ** (n2 + 1))
    u2 = Q(2, 3) * m2
    n3 = height_limit - 3
    m3 = Q(3, 2) * Q(
        (n3 + 1) ** n3 * (n3 + 2) * (n3 + 3),
        (n3 + 4) ** (n3 + 2),
    )
    u3 = Q(3, 4) * m3
    return q, (u1, u2, u3), 1 - q - u1 - u2 - u3


def audited_row(bottom):
    q, bounds, delta = compatible_bounds(bottom, 4)
    charges, assembled = sector_charges(bottom, 4)
    slacks = tuple(bounds[h - 1] - charges[h] for h in range(1, 4))
    x = charges["reset"] + charges[4] - delta
    true_slack = 1 - q - assembled
    accounting = sum(slacks, Q(0)) - x
    assert accounting == true_slack
    return q, bounds, delta, charges, slacks, x, true_slack


def record(value):
    return {"exact": str(value), "decimal": float(value)}


def encode(row):
    q, bounds, delta, charges, slacks, x, true_slack = row
    return {
        "q": record(q),
        "U": {f"h{h}": record(bounds[h - 1]) for h in range(1, 4)},
        "Delta": record(delta),
        "T": {"reset": record(charges["reset"]),
              **{f"h{h}": record(charges[h]) for h in range(1, 5)}},
        "S": {f"h{h}": record(slacks[h - 1]) for h in range(1, 4)},
        "X": record(x),
        "S1_minus_X": record(slacks[0] - x),
        "S1_plus_S2_minus_X": record(slacks[0] + slacks[1] - x),
        "true_slack": record(true_slack),
        "accounting_identity_exact": True,
        "orthogonal_sum_equals_assembled_T1": True,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    # Structural proof data for Phi_(2,kappa,D,2)=0.
    assert compositions(2) == ((1, 1), (2,))
    assert basins(2) == () and reset_kernel(2, 2) == {}
    assert not any(last > 2 and last - 1 >= 2
                   for _, last, _ in grouped_roots(2))

    b2 = audited_row(2)
    b3 = audited_row(3)

    assert b2[0] == Q(3750, 16807)
    assert b2[1] == (Q(3299, 56250), Q(24, 125), Q(27, 125))
    assert b2[2] == Q(293289307, 945393750)
    assert b2[3] == {
        "reset": Q(6628367198857337, 21450464220937500),
        1: Q(0),
        2: Q(22259, 1575000),
        3: Q(6974311, 300000000),
        4: Q(1735419680239, 29524500000000),
    }
    assert b2[4][0] - b2[5] == Q(
        9103978211751469889, 8339940489100500000000
    ) > 0

    assert b3[0] == Q(39375, 262144)
    assert b3[1] == (Q(23093, 300000), Q(24, 125), Q(27, 125))
    assert b3[2] == Q(896580719, 2457600000)
    assert b3[3] == {
        "reset": Q(174263554388922831263, 487049291366400000000),
        1: Q(3299, 128000),
        2: Q(1091287163, 39375000000),
        3: Q(108582539519, 2835000000000),
        4: Q(16843312139080279639, 171603713767500000000),
    }
    assert b3[4][0] - b3[5] == -Q(
        58850574391835735352420545363,
        1474064677007114895360000000000,
    ) < 0
    assert b3[4][0] + b3[4][1] - b3[5] == Q(
        183315802718619702462160882861,
        1474064677007114895360000000000,
    ) > 0
    assert b3[6] == Q(
        445256035370256335108738960557,
        1474064677007114895360000000000,
    ) > 0

    result = {
        "schema": "M209-independent-referee-v1",
        "arithmetic": "standard-library Fraction",
        "seed": None,
        "predecessor_imports": False,
        "root_representation": "grouped Cayley masses",
        "rows_evaluated": [[2, 4], [3, 4]],
        "B2_suffix_zero_structure": {
            "compositions": [[1, 1], [2]],
            "active_reset_endpoints": 0,
            "live_root_groups": 0,
            "parameter_independent": True,
        },
        "rows": {"B2_L4": encode(b2), "B3_L4": encode(b3)},
        "guards": {
            "killed_a_equals_d_excluded": True,
            "all_within_branch_Gram_cross_terms_retained": True,
            "parent_covariance_subtraction_retained": True,
            "orthogonal_sector_additivity_checked": True,
            "no_additional_rows_or_scan": True,
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
