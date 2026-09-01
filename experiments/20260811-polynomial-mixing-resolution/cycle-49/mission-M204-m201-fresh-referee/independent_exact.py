#!/usr/bin/env python3
"""Independent exact referee check of the single M201 witness.

The implementation is standard-library only, imports no M201 code, and
expands the root law over literal ordered compositions rather than M201's
grouped Cayley rows.  It evaluates only B=2, L=4.
"""

from argparse import ArgumentParser
from fractions import Fraction as F
from functools import cache
from json import dumps
from math import comb, factorial, prod
from pathlib import Path


# Univariate polynomials and bivariate Gram kernels, both in monomial bases.
def ptrim(values):
    values = list(values)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def psum(left, right):
    values = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        values[index] += value
    for index, value in enumerate(right):
        values[index] += value
    return ptrim(values)


def pscale(poly, scalar):
    return ptrim(scalar * value for value in poly)


def pproduct(left, right):
    values = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            values[i + j] += x * y
    return ptrim(values)


def monomial(degree):
    return (F(0),) * degree + (F(1),)


def ksum(left, right):
    values = dict(left)
    for key, value in right.items():
        values[key] = values.get(key, F(0)) + value
    return {key: value for key, value in values.items() if value}


def kscale(kernel, scalar):
    return {key: scalar * value for key, value in kernel.items()
            if scalar * value}


def rank_one(left, right):
    return {(i, j): x * y
            for i, x in enumerate(left) if x
            for j, y in enumerate(right) if y}


def likelihood_lift(kernel, left, right):
    values = {}
    for (i, j), gram in kernel.items():
        for a, x in enumerate(left):
            for b, y in enumerate(right):
                if x and y:
                    key = (i + a, j + b)
                    values[key] = values.get(key, F(0)) + gram * x * y
    return {key: value for key, value in values.items() if value}


# Beta(D,kappa-D) moments.
def rising(start, length):
    return prod(range(start, start + length))


def beta_power(kappa, deficit, degree):
    return F(rising(deficit, degree), rising(kappa, degree))


def beta_average(poly, kappa, deficit):
    return sum((coefficient * beta_power(kappa, deficit, degree)
                for degree, coefficient in enumerate(poly)), F(0))


def gram_diagonal_average(kernel, kappa, deficit):
    return sum((value * beta_power(kappa, deficit, i + j)
                for (i, j), value in kernel.items()), F(0))


def gram_product_average(kernel, left, right, kappa, deficit):
    total = F(0)
    for (i, j), value in kernel.items():
        li = beta_average(pproduct(monomial(i), left), kappa, deficit)
        rj = beta_average(pproduct(monomial(j), right), kappa, deficit)
        total += value * li * rj
    return total


def trace_charge(kernel, kappa, deficit):
    mean = F(deficit, kappa)
    centered_coordinate = (-mean, F(1))
    variance = beta_power(kappa, deficit, 2) - mean * mean
    raw_trace = gram_diagonal_average(kernel, kappa, deficit)
    removed_linear_mode = gram_product_average(
        kernel, centered_coordinate, centered_coordinate, kappa, deficit
    ) / variance
    return raw_trace - removed_linear_mode


# Parking/composition law.
@cache
def tree_weight(size):
    return F(size ** (size - 1), factorial(size))


@cache
def ordered_compositions(total):
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in ordered_compositions(total - head)
    )


def split_probability(total, bottom):
    return tree_weight(total + 1 - bottom) * tree_weight(bottom) / tree_weight(total + 1)


def literal_root_mass(source):
    return (prod(tree_weight(part) for part in source)
            / (factorial(len(source)) * tree_weight(sum(source) + 1)))


@cache
def literal_roots(total):
    rows = tuple((source, literal_root_mass(source))
                 for source in ordered_compositions(total))
    assert sum((mass for _, mass in rows), F(0)) == 1
    return rows


# Canonical reset basins and currents.
def reaches_endpoint(source, endpoint):
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


@cache
def reset_basins(total):
    sources = ordered_compositions(total)
    endpoints = sorted({
        (sum(source[:cut]),) + source[cut:]
        for source in sources
        for cut in range(1, len(source))
        if sum(source[:cut]) + source[cut] - 1 >= 2
    })
    return tuple(
        (endpoint, tuple(source for source in sources
                         if reaches_endpoint(source, endpoint)))
        for endpoint in endpoints
    )


def point_polynomial(source, bottom):
    degree = len(source)
    last = source[-1]
    if last < bottom:
        return (F(0),)
    if last == bottom:
        return (F(0),) * (degree - 1) + (F(degree),)
    split = split_probability(last - 1, bottom)
    values = [F(0)] * (degree + 1)
    values[0] = split
    values[degree] = -split
    return ptrim(values)


@cache
def reset_gram(total, bottom):
    parent_q = split_probability(total, bottom)
    gram = {}
    for endpoint, sources in reset_basins(total):
        current = (F(0),)
        for source in sources:
            centered = psum(point_polynomial(source, bottom), (F(-parent_q),))
            current = psum(current, pscale(centered, literal_root_mass(source)))
        capacity = F(len(endpoint)) * literal_root_mass(endpoint)
        gram = ksum(gram, kscale(rank_one(current, current), F(1) / (parent_q * capacity)))
    return gram


# Beta-binomial observation block. observed=degree is killed and never called.
def observation_probability(kappa, deficit, degree, observed):
    numerator = (comb(degree, observed)
                 * rising(deficit, observed)
                 * rising(kappa - deficit, degree - observed))
    return F(numerator, rising(kappa, degree))


def observation_likelihood(degree, observed):
    # C(d,a) u^a (1-u)^(d-a), expanded in u.
    values = [F(0)] * (degree + 1)
    for extra in range(degree - observed + 1):
        values[observed + extra] += F(
            comb(degree, observed)
            * comb(degree - observed, extra)
            * (-1) ** extra
        )
    return ptrim(values)


@cache
def full_history_gram(total, kappa, deficit, bottom):
    parent_q = split_probability(total, bottom)
    gram = dict(reset_gram(total, bottom))

    # This literal-source expansion is independent of grouped Cayley rows.
    for source, source_mass in literal_roots(total):
        degree = len(source)
        last = source[-1]
        if last <= bottom or last - 1 < 2:
            continue
        child_q = split_probability(last - 1, bottom)
        eta = source_mass * child_q / parent_q
        child_total = last - 1
        for observed in range(degree):  # killed observed=degree deleted here
            pi = observation_probability(kappa, deficit, degree, observed)
            child = full_history_gram(
                child_total, kappa + degree, deficit + observed, bottom
            )
            likelihood = observation_likelihood(degree, observed)
            branch = likelihood_lift(child, likelihood, likelihood)
            gram = ksum(gram, kscale(branch, eta / pi))
    return gram


def parent_height_charges(bottom, height_limit):
    total = bottom + height_limit
    kappa, deficit = 2, 1
    parent_q = split_probability(total, bottom)
    pieces = {"reset": trace_charge(reset_gram(total, bottom), kappa, deficit)}

    for source, source_mass in literal_roots(total):
        degree = len(source)
        last = source[-1]
        if last <= bottom or last - 1 < 2:
            continue
        eta = source_mass * split_probability(last - 1, bottom) / parent_q
        height = last - bottom
        for observed in range(degree):  # killed atom omitted
            pi = observation_probability(kappa, deficit, degree, observed)
            child = full_history_gram(
                last - 1, kappa + degree, deficit + observed, bottom
            )
            likelihood = observation_likelihood(degree, observed)
            branch = kscale(
                likelihood_lift(child, likelihood, likelihood), eta / pi
            )
            pieces[height] = pieces.get(height, F(0)) + trace_charge(
                branch, kappa, deficit
            )
    return pieces


# Accepted same-parent coefficients, recomputed from their closed formulas.
def cayley_coefficient(total, parts):
    if parts == total:
        return F(1)
    return F(parts * total ** (total - parts - 1), factorial(total - parts))


def terminal_matrix_factor(degree):
    return (
        F(degree + 1, 2 * degree + 1)
        * (F(4 ** degree, comb(2 * degree, degree)) - 1)
        - F(degree, degree + 2)
        + F(3 * degree * degree, (degree + 1) * (degree + 2) ** 2)
    )


def h1_operator_average(n):
    terms = []
    for r in range(1, n + 1):
        eta = F(cayley_coefficient(n, r), factorial(r + 1) * tree_weight(n + 2))
        terms.append((r, eta, terminal_matrix_factor(r + 1)))
    return terms, sum((eta * factor for _, eta, factor in terms), F(0))


def shown(value):
    return {"exact": str(value), "decimal": float(value)}


def main():
    parser = ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    bottom, height_limit = 2, 4
    total = bottom + height_limit
    q = split_probability(total, bottom)
    q0 = tree_weight(bottom) / tree_weight(bottom + 1)

    h1_terms, a1 = h1_operator_average(height_limit - 1)
    reserve1 = (1 - q0) * a1
    n2 = height_limit - 2
    exterior2 = F((n2 + 1) ** n2 * (n2 + 2), (n2 + 3) ** (n2 + 1))
    reserve2 = F(2, 3) * exterior2
    n3 = height_limit - 3
    exterior3 = F(3, 2) * F(
        (n3 + 1) ** n3 * (n3 + 2) * (n3 + 3),
        (n3 + 4) ** (n3 + 2),
    )
    reserve3 = F(3, 4) * exterior3
    residual = 1 - q - reserve1 - reserve2 - reserve3

    charges = parent_height_charges(bottom, height_limit)
    total_charge = sum(charges.values(), F(0))
    excess = charges["reset"] + charges[4] - residual
    true_slack = 1 - q - total_charge

    assert q == F(3750, 16807) == F(26250, 117649)
    assert q0 == F(2, 3)
    assert h1_terms == [
        (1, F(18, 125), F(3, 4)),
        (2, F(8, 125), F(649, 700)),
        (3, F(1, 125), F(113, 105)),
    ]
    assert a1 == F(3299, 18750)
    assert reserve1 == F(3299, 56250)
    assert exterior2 == exterior3 == F(36, 125)
    assert reserve2 == F(24, 125) and reserve3 == F(27, 125)
    assert residual == F(293289307, 945393750)
    assert charges == {
        "reset": F(6628367198857337, 21450464220937500),
        1: F(0),
        2: F(22259, 1575000),
        3: F(6974311, 300000000),
        4: F(1735419680239, 29524500000000),
    }
    assert excess == F(480024264873449410111, 8339940489100500000000) > 0
    assert total_charge == F(
        422384074903914714287, 1042492561137562500000
    )
    assert true_slack == F(
        387506171468022785713, 1042492561137562500000
    ) > 0

    result = {
        "schema": "M204-independent-referee-v1",
        "method": "literal ordered-composition root expansion; exact Gram history",
        "imports_from_m201": False,
        "seed": None,
        "state": {"B": bottom, "L": height_limit, "s": total,
                  "kappa": 2, "D": 1},
        "root_mass_checks": {
            str(size): shown(sum((mass for _, mass in literal_roots(size)), F(0)))
            for size in range(2, total + 1)
        },
        "parent": {"q": shown(q), "q0": shown(q0),
                   "true_budget": shown(1 - q)},
        "compatible_reservations": {
            "h1_rows_r_eta_R": [
                {"r": r, "eta": shown(eta), "R": shown(factor)}
                for r, eta, factor in h1_terms
            ],
            "A1": shown(a1),
            "U1": shown(reserve1),
            "M2": shown(exterior2),
            "U2": shown(reserve2),
            "M3": shown(exterior3),
            "U3": shown(reserve3),
            "Delta": shown(residual),
        },
        "actual_T1": {
            "reset": shown(charges["reset"]),
            "h1": shown(charges[1]),
            "h2": shown(charges[2]),
            "h3": shown(charges[3]),
            "h4": shown(charges[4]),
            "total": shown(total_charge),
            "true_contraction_slack": shown(true_slack),
        },
        "route_obstruction": {
            "reset_plus_h4_minus_Delta": shown(excess),
            "strictly_positive": True,
        },
        "logic": {
            "refuted": "independent addition/reservation route only",
            "not_refuted": [
                "true parent contraction inequality",
                "accepted h1 theorem",
                "accepted h2 theorem",
                "accepted h3 theorem",
            ],
        },
        "implementation_guards": {
            "literal_root_mass_normalized": True,
            "killed_observation_a_equals_d_deleted": True,
            "full_bivariate_Gram_cross_terms_retained": True,
            "linear_mode_covariance_subtracted": True,
            "only_named_B2_L4_state": True,
        },
    }
    args.output.write_text(dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
