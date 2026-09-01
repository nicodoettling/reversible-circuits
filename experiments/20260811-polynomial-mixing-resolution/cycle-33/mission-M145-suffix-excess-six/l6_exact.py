#!/usr/bin/env python3
"""Exact structure, audits, and certificates for auxiliary suffix excess six.

This is a standalone implementation of the accepted finite-DAG recurrence.
It imports no predecessor code or output.  The L=6 reset uses the corrected
one-power exceptional subtraction ``source_mass * lambda``.  Every positive
attachment rank is retained; only j=0 and rank-one children are killed by the
literal recurrence.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import sys
from fractions import Fraction as F
from pathlib import Path


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def rec(x: F) -> dict[str, str | float]:
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal": float(x),
    }


@functools.lru_cache(None)
def weight(n: int) -> F:
    assert n >= 1
    return F(n ** (n - 1), math.factorial(n))


@functools.lru_cache(None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in compositions(n - a))


@functools.lru_cache(None)
def forest(n: int, p: int) -> F:
    if (n, p) == (0, 0):
        return F(1)
    if not 1 <= p <= n:
        return F(0)
    return F(p * n ** (n - p), n * math.factorial(n - p))


def falling(a: int, p: int) -> int:
    return math.prod(range(a - p + 1, a + 1))


@functools.lru_cache(None)
def lam(a: int, degree: int) -> F:
    return math.factorial(degree - 1) * sum(
        (
            F(p * falling(a, p), math.factorial(p + degree - 1) * a**p)
            for p in range(1, a + 1)
        ),
        F(0),
    )


@functools.lru_cache(None)
def coefficient_c(s: int) -> F:
    return sum(
        (
            weight(a)
            * forest(s - a, degree - 1)
            / (math.factorial(degree - 1) * weight(s + 1))
            * lam(a, degree) ** 2
            for degree in range(2, s + 1)
            for a in range(1, s - degree + 2)
        ),
        F(0),
    )


def rising(a: int, n: int) -> int:
    return math.prod(range(a, a + n))


def attachment(a: int, deficit: int, degree: int, j: int, z: F) -> F:
    """Attachment law when K+1=(1+a*z)/z and D=K-R=deficit."""
    den = math.prod(1 + (a + r) * z for r in range(degree))
    if j == 0:
        return F(rising(deficit, degree)) * z**degree / den
    return (
        F(math.comb(degree, j) * rising(deficit, degree - j))
        * z ** (degree - j)
        * math.prod(1 + (a - deficit + r) * z for r in range(j))
        / den
    )


def split(ratios: tuple[F, ...]) -> F:
    return weight(len(ratios)) * math.prod(ratios)


@functools.lru_cache(None)
def support_template(excess: int):
    return tuple(
        (h, prefix, len(prefix) + 1)
        for h in range(excess + 1)
        for prefix in compositions(excess - h)
    )


def support(excess: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    q = split(ratios)
    rows = []
    for h, prefix, degree in support_template(excess):
        bottom_product = math.prod(ratios[-h:]) if h else F(1)
        child_q = weight(h) * bottom_product if h else None
        mass = math.prod(weight(x) for x in prefix) / (
            math.factorial(degree) * weight(excess + 1) * bottom_product
        )
        mean = (
            degree * attachment(a, deficit, degree - 1, 0, z)
            if h == 0
            else child_q * (1 - attachment(a, deficit, degree, 0, z))
        )
        rows.append((h, prefix, degree, mass, mean))
    assert len(rows) == 2**excess
    assert sum((mass * mean for _, _, _, mass, mean in rows), F(0)) == 1
    return tuple(rows), q


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


def endpoint_cuts(prefix: tuple[int, ...]):
    return tuple((sum(prefix[:cut]),) + prefix[cut:] for cut in range(1, len(prefix) + 1))


@functools.lru_cache(None)
def basin_template(excess: int):
    templates = support_template(excess)
    by_key = {(h, prefix): i for i, (h, prefix, _) in enumerate(templates)}
    endpoints = sorted(
        {(h, endpoint) for h, prefix, _ in templates for endpoint in endpoint_cuts(prefix)},
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    rows = []
    for h, endpoint in endpoints:
        source_indices = tuple(
            i
            for i, (hh, prefix, _) in enumerate(templates)
            if hh == h and in_basin(prefix, endpoint)
        )
        rows.append((h, endpoint, by_key[(h, endpoint)], source_indices))
    return tuple(rows)


def exceptional(excess: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    rows, q = support(excess, ratios, z, a, deficit)
    data = []
    for h, endpoint, endpoint_index, source_indices in basin_template(excess):
        sources = tuple(rows[i] for i in source_indices)
        theta = sum((mass * (mean - q) for _, _, _, mass, mean in sources), F(0))
        capacity = (len(endpoint) + 1) * rows[endpoint_index][3]
        source_mass = sum((row[3] for row in sources), F(0))
        data.append((h, endpoint, theta, capacity, source_mass, source_indices))
    return rows, q, tuple(data)


def group_mass(rows, h: int, degree: int) -> F:
    return sum((mass for hh, _, dd, mass, _ in rows if hh == h and dd == degree), F(0))


def coarse_reset(
    excess: int,
    ratios: tuple[F, ...],
    z: F,
    a: int,
    deficit: int,
    height: F,
) -> F:
    rows, q, data = exceptional(excess, ratios, z, a, deficit)
    occurrence_mass = sum((mass * len(prefix) for _, prefix, _, mass, _ in rows), F(0))
    return q * (height - q * occurrence_mass) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _, _ in data), F(0)
    )


def corrected_reset(excess: int, ratios: tuple[F, ...], z: F, ordinary: F):
    _, q, data = exceptional(excess, ratios, z, 0, 1)
    subtraction = sum(
        (
            source_mass * lam(endpoint[0], len(endpoint) + 1)
            for _, endpoint, _, _, source_mass, _ in data
        ),
        F(0),
    )
    reset = q * (ordinary - q * subtraction) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _, _ in data), F(0)
    )
    return reset, len(data), subtraction


def full_basin_reset(excess: int, ratios: tuple[F, ...], z: F, ordinary: F):
    """Universal exact-baseline envelope using ``b_E*lambda_E``.

    Here capacities and source masses are normalized by q.  Since
    b_E=c_E*lambda_E, the normalized sum below is
    ``sum (c_E/q)*lambda_E**2 = sum (b_E/q)*lambda_E``.
    Thus the mathematical subtraction has one power of lambda on full basin
    mass b_E.  It is not the rejected ``a_E*lambda_E**2`` subtraction.
    """
    _, q, data = exceptional(excess, ratios, z, 0, 1)
    full_subtraction_over_q = sum(
        (
            capacity * lam(endpoint[0], len(endpoint) + 1) ** 2
            for _, endpoint, _, capacity, _, _ in data
        ),
        F(0),
    )
    reset = q * (ordinary - q * full_subtraction_over_q) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _, _ in data), F(0)
    )
    return reset, len(data), full_subtraction_over_q


@functools.lru_cache(None)
def arbitrary_envelope(
    excess: int,
    ratios: tuple[F, ...],
    z: F,
    a: int,
    deficit: int,
    heights_tuple: tuple[F, ...],
    ordinary_tuple: tuple[F, ...],
) -> F:
    """Return the refined all-deficit bound H/q for 0<=excess<=5."""
    q = split(ratios)
    if excess == 0:
        return 1 - q
    assert excess <= 5
    heights = {ell + 1: value for ell, value in enumerate(heights_tuple)}
    rows, q2 = support(excess, ratios, z, a, deficit)
    assert q2 == q
    # This is the same full-basin identity in an arbitrary attachment context.
    # The baseline C_S is contextual only through S; exceptional currents use
    # the actual (a,deficit) pair.
    _, _, data = exceptional(excess, ratios, z, a, deficit)
    full_subtraction_over_q = sum(
        (
            capacity * lam(endpoint[0], len(endpoint) + 1) ** 2
            for _, endpoint, _, capacity, _, _ in data
        ),
        F(0),
    )
    value = q * (ordinary_tuple[0] - q * full_subtraction_over_q) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _, _ in data), F(0)
    )
    for h in range(1, excess + 1):
        for degree in range(1, excess - h + 2):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            child_ratios = ratios[-h:]
            child_q = split(child_ratios)
            for j in range(1, degree + 1):
                child_excess = h - 1
                child_deficit = deficit + degree - j
                child = child_q * (
                    1 - child_q
                    if child_excess == 0
                    else arbitrary_envelope(
                        child_excess,
                        child_ratios,
                        z,
                        a + degree,
                        child_deficit,
                        heights_tuple,
                        ordinary_tuple[-h:],
                    )
                )
                value += mass * attachment(a, deficit, degree, j, z) * child
    return value


def l6_envelope(
    ratios: tuple[F, ...],
    z: F,
    heights_tuple: tuple[F, ...],
    ordinary_tuple: tuple[F, ...],
):
    rows, q = support(6, ratios, z, 0, 1)
    reset, basin_count, subtraction = full_basin_reset(6, ratios, z, ordinary_tuple[0])
    value = reset
    live_count = 0
    rank_count = 0
    group_rows = []
    for h in range(1, 7):
        for degree in range(1, 8 - h):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            live_count += 1
            child_ratios = ratios[-h:]
            child_q = split(child_ratios)
            ranks = []
            for j in range(1, degree + 1):
                rank_count += 1
                child_excess = h - 1
                child_deficit = degree + 1 - j
                if child_excess == 0:
                    child = child_q * (1 - child_q)
                    kind = "terminal"
                else:
                    child = child_q * arbitrary_envelope(
                        child_excess,
                        child_ratios,
                        z,
                        degree,
                        child_deficit,
                        heights_tuple,
                        ordinary_tuple[-h:],
                    )
                    kind = (
                        "refined-right-heavy"
                        if child_deficit == 1
                        else "refined-arbitrary-deficit"
                    )
                nu = attachment(0, 1, degree, j, z)
                value += mass * nu * child
                ranks.append((j, child_deficit, child_excess, nu, kind))
            group_rows.append((h, degree, mass, tuple(ranks)))
    assert live_count == 16 and rank_count == 51
    return value, q, reset, basin_count, subtraction, tuple(group_rows)


def budget_l6_envelope(
    ratios: tuple[F, ...],
    z: F,
    heights_tuple: tuple[F, ...],
    ordinary_tuple: tuple[F, ...],
) -> tuple[F, F]:
    """Rejected induction envelope charging each right-heavy child its budget."""
    rows, q = support(6, ratios, z, 0, 1)
    value, _, _ = full_basin_reset(6, ratios, z, ordinary_tuple[0])
    for h in range(1, 7):
        for degree in range(1, 8 - h):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            child_ratios = ratios[-h:]
            child_q = split(child_ratios)
            for j in range(1, degree + 1):
                child_excess = h - 1
                child_deficit = degree + 1 - j
                if child_excess == 0 or child_deficit == 1:
                    child = child_q * (1 - child_q)
                else:
                    child = child_q * arbitrary_envelope(
                        child_excess,
                        child_ratios,
                        z,
                        degree,
                        child_deficit,
                        heights_tuple,
                        ordinary_tuple[-h:],
                    )
                value += mass * attachment(0, 1, degree, j, z) * child
    return value, q


def actual_parameters(s: int):
    ratios = tuple(weight(s - i) / weight(s - i + 1) for i in range(7))
    bottom = s - 6
    heights = tuple(F(bottom + ell - 1, bottom + ell + 1) for ell in range(1, 7))
    ordinary = tuple(coefficient_c(s - i) for i in range(7))
    return ratios, heights, ordinary


def clearing_factor(z: F) -> F:
    return math.prod(1 + a * z for a in range(1, 7)) ** 2


def cleared(
    ratios: tuple[F, ...], z: F, heights: tuple[F, ...], ordinary: tuple[F, ...]
) -> F:
    envelope, q, _, _, _, _ = l6_envelope(ratios, z, heights, ordinary)
    return clearing_factor(z) * (1 - q - envelope)


# Independent literal recurrence in integer context coordinates.
def safe_comb(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def q_split(s: int, b: int) -> F:
    return weight(s + 1 - b) * weight(b) / weight(s + 1)


def contextual(k: int, t: int, K: int, R: int, B: int) -> F:
    if t < B:
        return F(0)
    if t == B:
        den = safe_comb(k + K - 1, K - 1)
        return F(K * safe_comb(k + K - R - 2, K - R - 1), den) if den else F(0)
    return q_split(t - 1, B) * (
        1 - F(safe_comb(K, R + 1), safe_comb(K + k, R + 1))
    )


def attachment_integer(K: int, R: int, k: int, j: int) -> F:
    return F(
        safe_comb(R + j, j) * safe_comb(K - R - 1 + k - j, k - j),
        safe_comb(K + k, k),
    )


@functools.lru_cache(None)
def groups(s: int):
    rows = tuple(
        (k, t, weight(t) * forest(s - t, k - 1) / (math.factorial(k) * weight(s + 1)))
        for k in range(1, s + 1)
        for t in range(1, s + 1)
        if forest(s - t, k - 1)
    )
    assert sum((mass for _, _, mass in rows), F(0)) == 1
    return rows


def source_in_full_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source))
    )


@functools.lru_cache(None)
def literal_basin_structure(s: int):
    comps = compositions(s)
    endpoints = sorted(
        {
            endpoint
            for source in comps
            if len(source) >= 2
            for endpoint in ((sum(source[:cut]),) + source[cut:] for cut in range(1, len(source)))
            if endpoint[0] + endpoint[1] - 1 >= 2
        },
        key=lambda endpoint: (len(endpoint), endpoint),
    )
    return tuple(
        (endpoint, tuple(source for source in comps if source_in_full_basin(source, endpoint)))
        for endpoint in endpoints
    )


@functools.lru_cache(None)
def literal_reset(s: int, K: int, R: int, B: int) -> F:
    q = q_split(s, B)
    root_mass = {
        parts: math.prod(weight(part) for part in parts)
        / (math.factorial(len(parts)) * weight(s + 1))
        for parts in compositions(s)
    }
    value = F(0)
    for endpoint, sources in literal_basin_structure(s):
        theta = sum(
            (
                root_mass[source]
                * (contextual(len(source), source[-1], K, R, B) - q)
                for source in sources
            ),
            F(0),
        )
        capacity = len(endpoint) * root_mass[endpoint]
        value += theta * theta / capacity
    return value


@functools.lru_cache(None)
def grouped_reset(s: int, K: int, R: int, B: int) -> F:
    q = q_split(s, B)
    value = F(0)
    scalar_cache: dict[tuple[int, int, int], F] = {}

    def scalar(first_total: int, tail_count: int, last: int) -> F:
        key = (first_total, tail_count, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum(
                (
                    forest(first_total, p)
                    * (contextual(p + tail_count, last, K, R, B) - q)
                    / math.factorial(p + tail_count)
                    for p in range(1, first_total + 1)
                ),
                F(0),
            )
        return scalar_cache[key]

    for tail_count in range(1, s):
        middle_count = tail_count - 1
        for first_total in range(1, s + 1):
            for next_part in range(1, s - first_total - middle_count + 1):
                middle_total = s - first_total - next_part
                if first_total + next_part - 1 < 2:
                    continue
                if middle_count == 0:
                    suffix_rows = (((next_part, weight(next_part))),) if middle_total == 0 else ()
                else:
                    suffix_rows = tuple(
                        (
                            last,
                            weight(next_part)
                            * forest(middle_total - last, middle_count - 1)
                            * weight(last),
                        )
                        for last in range(1, middle_total + 1)
                        if forest(middle_total - last, middle_count - 1)
                    )
                for last, suffix_weight in suffix_rows:
                    current = scalar(first_total, tail_count, last)
                    value += (
                        suffix_weight
                        * math.factorial(tail_count)
                        * current**2
                        / (weight(first_total) * weight(s + 1))
                    )
    return value


@functools.lru_cache(None)
def children(state: tuple[int, int, int, int]):
    s, K, R, B = state
    phase = s + K - R
    rows = []
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum((attachment_integer(K, R, k, j) for j in range(k + 1)), F(0)) == 1
        for j in range(1, k + 1):
            nu = attachment_integer(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            assert child[0] + child[1] - child[2] < phase
            rows.append((mass * nu, child, k, t, j))
    return tuple(rows)


@functools.lru_cache(None)
def resolvent_grouped(state: tuple[int, int, int, int]) -> F:
    return grouped_reset(*state) + sum(
        (mass * resolvent_grouped(child) for mass, child, _, _, _ in children(state)), F(0)
    )


@functools.lru_cache(None)
def resolvent_literal(state: tuple[int, int, int, int]) -> F:
    return literal_reset(*state) + sum(
        (mass * resolvent_literal(child) for mass, child, _, _, _ in children(state)), F(0)
    )


def invert(matrix: list[list[F]]) -> list[list[F]]:
    n = len(matrix)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            scale = aug[row][col]
            aug[row] = [x - scale * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


@functools.lru_cache(None)
def bernstein_inverse(degree: int):
    if degree == 0:
        return ((F(1),),)
    matrix = []
    for j in range(degree + 1):
        t = F(j, degree)
        matrix.append(
            [F(math.comb(degree, i)) * t**i * (1 - t) ** (degree - i) for i in range(degree + 1)]
        )
    return tuple(tuple(row) for row in invert(matrix))


def transform_axis(values: dict[tuple[int, ...], F], degrees: tuple[int, ...], axis: int):
    inverse = bernstein_inverse(degrees[axis])
    output = {}
    other_ranges = [range(d + 1) for i, d in enumerate(degrees) if i != axis]
    for other in itertools.product(*other_ranges):
        def index(j: int):
            iterator = iter(other)
            return tuple(j if i == axis else next(iterator) for i in range(len(degrees)))
        samples = [values[index(j)] for j in range(degrees[axis] + 1)]
        for i in range(degrees[axis] + 1):
            output[index(i)] = sum(
                (inverse[i][j] * samples[j] for j in range(degrees[axis] + 1)), F(0)
            )
    return output


def tensor_bernstein(values: dict[tuple[int, ...], F], degrees: tuple[int, ...]):
    result = values
    for axis in range(len(degrees)):
        result = transform_axis(result, degrees, axis)
    return result


def bernstein_eval(coefficients, degrees, point) -> F:
    value = F(0)
    for index, coefficient in coefficients.items():
        basis = F(1)
        for degree, i, t in zip(degrees, index, point):
            basis *= math.comb(degree, i) * t**i * (1 - t) ** (degree - i)
        value += coefficient * basis
    return value


def finite_difference_degree(values: list[F]) -> int:
    row = values[:]
    for degree in range(len(values) - 1):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if all(x == 0 for x in row):
            return degree
    return len(values) - 1


def digest_fractions(items) -> str:
    text = "\n".join(f"{x.numerator}/{x.denominator}" for x in items) + "\n"
    return hashlib.sha256(text.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--phase", choices=("discovery", "full"), default="full")
    args = parser.parse_args()
    failures = []

    # Exact structural identities and the minimum-boundary all-j table.
    ratios7, heights7, ordinary7 = actual_parameters(7)
    rows7, q7 = support(6, ratios7, F(1, 2), 0, 1)
    _, _, data7 = exceptional(6, ratios7, F(1, 2), 0, 1)
    env7, _, _, basins7, subtraction7, group_rows7 = l6_envelope(
        ratios7, F(1, 2), heights7, ordinary7
    )
    actual_retained7 = sum(
        1
        for _, _, _, ranks in group_rows7
        for _, _, child_excess, _, _ in ranks
        if not (child_excess == 0 and split(ratios7[-1:]) == 1)
    )
    structure = {
        "supported_roots": len(rows7),
        "exceptional_basins": len(data7),
        "positive_groups": 22,
        "live_groups": len(group_rows7),
        "nominal_positive_attachment_ranks": sum(len(ranks) for _, _, _, ranks in group_rows7),
        "s7_actual_retained_children": actual_retained7,
        "s7_mean_identity": rec(sum((mass * mean for _, _, _, mass, mean in rows7), F(0))),
        "s7_q": rec(q7),
        "s7_corrected_subtraction": rec(subtraction7),
        "s7_envelope_ratio": rec(env7 / (1 - q7)),
        "live_table": [
            {
                "h": h,
                "degree": degree,
                "mass_over_q": rec(mass),
                "ranks": [
                    {
                        "j": j,
                        "child_deficit": deficit,
                        "child_excess": excess,
                        "attachment": rec(nu),
                        "kind": kind,
                    }
                    for j, deficit, excess, nu, kind in ranks
                ],
            }
            for h, degree, mass, ranks in group_rows7
        ],
    }
    expected_structure = (64, 63, 16, 51, 31)
    observed_structure = (
        len(rows7), len(data7), len(group_rows7),
        sum(len(ranks) for _, _, _, ranks in group_rows7), actual_retained7,
    )
    if observed_structure != expected_structure:
        failures.append({"kind": "structure", "observed": list(observed_structure)})

    # Preserve the decisive falsifier for the one-number child-budget route.
    budget_at_zero, budget_q = budget_l6_envelope(
        ratios7, F(0), heights7, ordinary7
    )
    budget_128, _ = budget_l6_envelope(ratios7, F(1, 129), heights7, ordinary7)
    exact_128 = resolvent_grouped((7, 128, 127, 1))
    budget_obstruction = {
        "claim_refuted": "full-basin root reset plus q_child(1-q_child) for every right-heavy child proves L=6",
        "z0_cleared_slack": rec(1 - budget_q - budget_at_zero),
        "s7_K128_budget_target_ratio": rec(budget_128 / (1 - budget_q)),
        "s7_K128_exact_H_target_ratio": rec(exact_128 / (budget_q * (1 - budget_q))),
        "interpretation": "rigorous envelope obstruction; not an H counterexample",
    }
    if not (
        budget_obstruction["z0_cleared_slack"]["decimal"] < 0
        and budget_obstruction["s7_K128_budget_target_ratio"]["decimal"] > 1
        and budget_obstruction["s7_K128_exact_H_target_ratio"]["decimal"] < 1
    ):
        failures.append({"kind": "budget-obstruction-not-reproduced"})

    # Literal versus grouped exact resets/resolvents and envelope checks.
    root_audits = []
    for s in (7, 8):
        ratios, heights, ordinary = actual_parameters(s)
        for K in (1, 2, 5):
            state = (s, K, K - 1, s - 6)
            z = F(1, K + 1)
            lr = literal_reset(*state)
            gr = grouped_reset(*state)
            lh = resolvent_literal(state)
            gh = resolvent_grouped(state)
            envelope, q, *_ = l6_envelope(ratios, z, heights, ordinary)
            row = {
                "state": list(state),
                "literal_reset": rec(lr),
                "grouped_reset": rec(gr),
                "literal_H": rec(lh),
                "grouped_H": rec(gh),
                "envelope_over_q": rec(envelope),
                "target_over_q": rec(1 - q),
                "H_target_ratio": rec(gh / (q * (1 - q))),
                "envelope_target_ratio": rec(envelope / (1 - q)),
                "retained_children": len(children(state)),
            }
            root_audits.append(row)
            if lr != gr:
                failures.append({"kind": "literal-grouped-reset", "state": list(state)})
            if lh != gh:
                failures.append({"kind": "literal-grouped-H", "state": list(state)})
            if gh > q * envelope or envelope > 1 - q:
                failures.append({"kind": "root-bound", "state": list(state)})

    # Every arbitrary deficit through L=4 on a bounded exact domain.
    arbitrary_rows = []
    arbitrary_failure_count = 0
    for excess in range(1, 5):
        for S in range(excess + 1, 8):
            B = S - excess
            ratios = tuple(weight(S - i) / weight(S - i + 1) for i in range(excess + 1))
            heights = tuple(F(B + ell - 1, B + ell + 1) for ell in range(1, 7))
            q = split(ratios)
            for K in range(2, 7):
                z = F(1, K + 1)
                for R in range(1, K):
                    D = K - R
                    state = (S, K, R, B)
                    ordinary = tuple(coefficient_c(S - i) for i in range(excess + 1))
                    bound = q * arbitrary_envelope(
                        excess, ratios, z, 0, D, heights, ordinary
                    )
                    exact = resolvent_grouped(state)
                    ok = exact <= bound
                    arbitrary_failure_count += int(not ok)
                    arbitrary_rows.append((exact / bound if bound else F(0), state, ok))
    if arbitrary_failure_count:
        failures.append({"kind": "arbitrary-deficit-bound", "count": arbitrary_failure_count})

    # Finite exact Bernstein certificates.  Degree is discovered independently.
    generic = (F(7, 20), F(9, 25), F(11, 30), F(3, 8), F(19, 50), F(23, 60), F(29, 75))
    unit_heights = tuple(F(1) for _ in range(6))
    unit_ordinary = tuple(F(3, 4) for _ in range(7))
    z_degree = finite_difference_degree(
        [cleared(generic, F(j, 19), unit_heights, unit_ordinary) for j in range(18)]
    )
    ratio_degrees = []
    for axis in range(7):
        samples = []
        for j in range(4):
            point = list(generic)
            point[axis] += F(j, 100)
            samples.append(cleared(tuple(point), F(2, 7), unit_heights, unit_ordinary))
        ratio_degrees.append(finite_difference_degree(samples))
    degrees = tuple(ratio_degrees) + (z_degree,)

    finite_rows = []
    finite_values = []
    finite_indexed = []
    inverse_z = bernstein_inverse(z_degree)
    finite_stop = 16 if args.phase == "discovery" else 104
    for s in range(7, finite_stop + 1):
        ratios, heights, ordinary = actual_parameters(s)
        samples = [cleared(ratios, F(j, 2 * z_degree), heights, ordinary) for j in range(z_degree + 1)]
        coeffs = [
            sum((inverse_z[i][j] * samples[j] for j in range(z_degree + 1)), F(0))
            for i in range(z_degree + 1)
        ]
        t_direct = F(7, 19)
        direct = cleared(ratios, t_direct / 2, heights, ordinary)
        interpolated = sum(
            (
                coeffs[i]
                * math.comb(z_degree, i)
                * t_direct**i
                * (1 - t_direct) ** (z_degree - i)
                for i in range(z_degree + 1)
            ),
            F(0),
        )
        if direct != interpolated:
            failures.append({"kind": "finite-off-grid", "s": s})
        finite_values.extend(coeffs)
        finite_indexed.extend((x, s, i) for i, x in enumerate(coeffs))
        finite_rows.append({"s": s, "coefficients": [rec(x) for x in coeffs]})
    finite_nonpositive = sum(x <= 0 for x in finite_values)
    finite_min, finite_min_s, finite_min_i = min(finite_indexed)
    if finite_nonpositive:
        failures.append({"kind": "finite-nonpositive", "count": finite_nonpositive})

    tail_payload = None
    if args.phase == "full":
        lo, hi = F(4, 11), F(187, 500)
        b99 = weight(99) / weight(100)
        if not b99 < hi:
            failures.append({"kind": "ratio-upper", "b99": rec(b99)})
        grid = {}
        for index in itertools.product(*(range(d + 1) for d in degrees)):
            unit = tuple(F(i, d) if d else F(0) for i, d in zip(index, degrees))
            ratios = tuple(lo + (hi - lo) * unit[i] for i in range(7))
            grid[index] = cleared(ratios, unit[7] / 2, unit_heights, unit_ordinary)
        tail = tensor_bernstein(grid, degrees)
        tail_nonpositive = sum(x <= 0 for x in tail.values())
        tail_min_index, tail_min = min(tail.items(), key=lambda item: item[1])
        if tail_nonpositive:
            failures.append({"kind": "tail-nonpositive", "count": tail_nonpositive})
        off_unit = (F(1, 8), F(2, 8), F(3, 8), F(4, 8), F(5, 8), F(6, 8), F(7, 8), F(7, 11))
        off_ratios = tuple(lo + (hi - lo) * off_unit[i] for i in range(7))
        direct = cleared(off_ratios, off_unit[7] / 2, unit_heights, unit_ordinary)
        interp = bernstein_eval(tail, degrees, off_unit)
        if direct != interp:
            failures.append({"kind": "tail-off-grid"})
        tail_values = [x for _, x in sorted(tail.items())]
        tail_payload = {
            "range": "seven ratios in [4/11,187/500], z in [0,1/2], heights=1, C_s=3/4",
            "b99": rec(b99),
            "degrees": list(degrees),
            "count": len(tail),
            "nonpositive": tail_nonpositive,
            "minimum_index": list(tail_min_index),
            "minimum": rec(tail_min),
            "coefficient_sha256": digest_fractions(tail_values),
        }

    payload = {
        "claim": "corrected one-power auxiliary L=6 envelope and exact structure",
        "status": "proved relative to accepted M140/M144 scalar C_s<3/4 and the accepted recurrence",
        "scope": "full nonlazy stationary-flow parking-degree reset recurrence only",
        "target": "uniform fixed-length identity words in Omega(N,m); no chain-gap inference",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "seed": None,
        "phase": args.phase,
        "exceptional_subtraction": "source_mass*lambda (one power); lambda^2 is rejected",
        "structure": structure,
        "budget_obstruction": budget_obstruction,
        "root_audits": root_audits,
        "arbitrary_deficit_audit": {
            "range": "L=1..4, L+1<=S<=7, K=2..6, 1<=R<K",
            "count": len(arbitrary_rows),
            "failure_count": arbitrary_failure_count,
            "maximum_exact_to_bound": rec(max(x for x, _, _ in arbitrary_rows)),
            "maximizer": list(max(arbitrary_rows, key=lambda row: row[0])[1]),
        },
        "finite_certificate": {
            "range": f"s=7,...,{finite_stop}; z in [0,1/2]",
            "z_degree": z_degree,
            "count": len(finite_values),
            "nonpositive": finite_nonpositive,
            "minimum": rec(finite_min),
            "minimum_s": finite_min_s,
            "minimum_index": finite_min_i,
            "coefficient_sha256": digest_fractions(finite_values),
            "row_minima": [
                {
                    "s": row["s"],
                    "minimum": min(
                        row["coefficients"],
                        key=lambda x: F(int(x["numerator"]), int(x["denominator"])),
                    ),
                }
                for row in finite_rows
            ],
            "s7_coefficients": finite_rows[0]["coefficients"],
        },
        "tail_certificate": tail_payload,
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                "phase": args.phase,
                "degrees": list(degrees),
                "failure_count": len(failures),
                "finite_count": len(finite_values),
                "finite_nonpositive": finite_nonpositive,
                "finite_minimum": rec(finite_min),
                "tail": None
                if tail_payload is None
                else {
                    "count": tail_payload["count"],
                    "nonpositive": tail_payload["nonpositive"],
                    "minimum": tail_payload["minimum"],
                    "minimum_index": tail_payload["minimum_index"],
                },
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
