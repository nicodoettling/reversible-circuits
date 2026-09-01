#!/usr/bin/env python3
"""Exact L=5 reset-excursion reduction and certificate search.

This is a standalone standard-library implementation.  It reconstructs the
accepted all-attachment finite-DAG recurrence from definitions, derives the
canonical-basin envelope for arbitrary fixed suffix excess, and specializes
it to the first open right-heavy boundary L=5.  All mathematical arithmetic
uses ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path


@functools.lru_cache(maxsize=None)
def w(n: int) -> Fraction:
    assert n >= 1
    return Fraction(n ** (n - 1), math.factorial(n))


@functools.lru_cache(maxsize=None)
def compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple(
        (first,) + tail
        for first in range(1, n + 1)
        for tail in compositions(n - first)
    )


@functools.lru_cache(maxsize=None)
def cayley(total: int, parts: int) -> Fraction:
    if parts == 0:
        return Fraction(int(total == 0))
    if not 1 <= parts <= total:
        return Fraction()
    return Fraction(
        parts * total ** (total - parts),
        total * math.factorial(total - parts),
    )


def q_split(s: int, B: int) -> Fraction:
    return w(s + 1 - B) * w(B) / w(s + 1)


def safe_comb(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def contextual(k: int, t: int, K: int, R: int, B: int) -> Fraction:
    if t < B:
        return Fraction()
    if t == B:
        den = safe_comb(k + K - 1, K - 1)
        num = K * safe_comb(k + K - R - 2, K - R - 1)
        return Fraction(num, den) if den else Fraction()
    killed = Fraction(safe_comb(K, R + 1), safe_comb(K + k, R + 1))
    return q_split(t - 1, B) * (1 - killed)


def attachment(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        safe_comb(R + j, j)
        * safe_comb(K - R - 1 + k - j, k - j),
        safe_comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def groups(s: int) -> tuple[tuple[int, int, Fraction], ...]:
    rows = []
    total = Fraction()
    for k in range(1, s + 1):
        for t in range(1, s + 1):
            mass = w(t) * cayley(s - t, k - 1) / (
                math.factorial(k) * w(s + 1)
            )
            if mass:
                rows.append((k, t, mass))
                total += mass
    assert total == 1
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def reset_energy(s: int, K: int, R: int, B: int) -> Fraction:
    """Exact active canonical reset energy via grouped prefix refinements."""
    q = q_split(s, B)
    answer = Fraction()
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def scalar(first_total: int, tail_count: int, last: int) -> Fraction:
        key = (first_total, tail_count, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum(
                (
                    cayley(first_total, p)
                    * (contextual(p + tail_count, last, K, R, B) - q)
                    / math.factorial(p + tail_count)
                    for p in range(1, first_total + 1)
                ),
                Fraction(),
            )
        return scalar_cache[key]

    for tail_count in range(1, s):
        middle_count = tail_count - 1
        for first_total in range(1, s + 1):
            for next_part in range(1, s - first_total - middle_count + 1):
                middle_total = s - first_total - next_part
                child_rank = first_total + next_part - 1
                if child_rank < 2:
                    continue
                if middle_count == 0:
                    suffix_rows = (
                        ((next_part, w(next_part)),)
                        if middle_total == 0
                        else ()
                    )
                else:
                    suffix_rows = tuple(
                        (
                            last,
                            w(next_part)
                            * cayley(middle_total - last, middle_count - 1)
                            * w(last),
                        )
                        for last in range(1, middle_total + 1)
                        if cayley(middle_total - last, middle_count - 1)
                    )
                for last, suffix_weight in suffix_rows:
                    current = scalar(first_total, tail_count, last)
                    answer += (
                        suffix_weight
                        * math.factorial(tail_count)
                        * current * current
                        / (w(first_total) * w(s + 1))
                    )
    return answer


@functools.lru_cache(maxsize=None)
def children(state: tuple[int, int, int, int]):
    s, K, R, B = state
    phase = s + K - R
    rows = []
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum((attachment(K, R, k, j) for j in range(k + 1)), Fraction()) == 1
        for j in range(1, k + 1):
            nu = attachment(K, R, k, j)
            if not nu:
                continue
            child = (t - 1, K + k, R + j, B)
            assert child[0] + child[1] - child[2] < phase
            rows.append((mass * nu, child, k, t, j))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def resolvent(state: tuple[int, int, int, int]) -> Fraction:
    return reset_energy(*state) + sum(
        (coefficient * resolvent(child) for coefficient, child, _, _, _ in children(state)),
        Fraction(),
    )


def rising(start: int, length: int) -> int:
    return math.prod(range(start, start + length))


def nu_symbolic(a: int, D: int, k: int, j: int, z: Fraction) -> Fraction:
    """Attachment law when K+1=(1+a*z)/z and K-R=D.

    The displayed rational expression is regular at z=0 and avoids using an
    artificial infinite K at the certificate endpoint.
    """
    assert a >= 0 and D >= 1 and 0 <= j <= k
    denominator = math.prod((1 + (a + r) * z for r in range(k)))
    if j == 0:
        return Fraction(rising(D, k)) * z ** k / denominator
    numerator = Fraction(math.comb(k, j) * rising(D, k - j))
    numerator *= z ** (k - j)
    numerator *= math.prod((1 + (a - D + r) * z for r in range(j)))
    return numerator / denominator


def canonical_endpoints(prefix: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        (sum(prefix[:cut]),) + prefix[cut:]
        for cut in range(1, len(prefix) + 1)
    )


def in_prefix_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    for cut in range(1, len(source) + 1):
        if sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]:
            return True
    return False


@functools.lru_cache(maxsize=None)
def literal_basin_structure(s: int):
    """All active full-composition canonical basins by literal enumeration."""
    roots = compositions(s)
    endpoints = sorted(
        {
            endpoint
            for source in roots
            if len(source) >= 2
            for endpoint in (
                (sum(source[:cut]),) + source[cut:]
                for cut in range(1, len(source))
            )
            if endpoint[0] + endpoint[1] - 1 >= 2
        },
        key=lambda endpoint: (len(endpoint), endpoint),
    )
    return tuple(
        (
            endpoint,
            tuple(source for source in roots if in_prefix_basin(source, endpoint)),
        )
        for endpoint in endpoints
    )


def literal_basin_rows(s: int, K: int, R: int, B: int):
    q = q_split(s, B)
    root_mass = {
        source: math.prod((w(part) for part in source))
        / (math.factorial(len(source)) * w(s + 1))
        for source in compositions(s)
    }
    return tuple(
        (
            endpoint,
            sources,
            sum(
                (
                    root_mass[source]
                    * (contextual(len(source), source[-1], K, R, B) - q)
                    for source in sources
                ),
                Fraction(),
            ),
            len(endpoint) * root_mass[endpoint],
        )
        for endpoint, sources in literal_basin_structure(s)
    )


def literal_reset_energy(s: int, K: int, R: int, B: int) -> Fraction:
    return sum(
        (
            theta * theta / capacity
            for _, _, theta, capacity in literal_basin_rows(s, K, R, B)
        ),
        Fraction(),
    )


def split_for_excess(ratios: tuple[Fraction, ...]) -> Fraction:
    excess = len(ratios) - 1
    return w(excess + 1) * math.prod(ratios)


def support_records(
    excess: int,
    ratios: tuple[Fraction, ...],
    z: Fraction,
    a: int,
    D: int,
):
    """Supported rows `(h,prefix,rho/q,contextual_mean)`.

    Ratios are top-down `(b_S,...,b_B)`, hence the product for last-part
    displacement h is the product of the bottom h entries.
    """
    assert excess >= 1 and len(ratios) == excess + 1
    q = split_for_excess(ratios)
    rows = []
    for h in range(excess + 1):
        prefix_total = excess - h
        bottom_product = math.prod(ratios[-h:]) if h else Fraction(1)
        child_split = w(h) * bottom_product if h else None
        for prefix in compositions(prefix_total):
            k = len(prefix) + 1
            prefix_weight = math.prod((w(part) for part in prefix))
            mass_over_q = prefix_weight / (
                math.factorial(k) * w(excess + 1) * bottom_product
            )
            if h == 0:
                mean = k * nu_symbolic(a, D, k - 1, 0, z)
            else:
                mean = child_split * (1 - nu_symbolic(a, D, k, 0, z))
            rows.append((h, prefix, mass_over_q, mean))
    assert len(rows) == 2 ** excess
    assert sum((mass * mean for _, _, mass, mean in rows), Fraction()) == 1
    return tuple(rows), q


def reset_envelope_over_q(
    excess: int,
    ratios: tuple[Fraction, ...],
    z: Fraction,
    a: int,
    D: int,
    path_height: Fraction,
    ordinary_constant: Fraction | None = None,
    lambda_degree_two: Fraction | None = None,
    exact_degree_two: bool = False,
    exact_all_degrees: bool = False,
):
    rows, q = support_records(excess, ratios, z, a, D)
    by_key = {(h, prefix): (mass, mean) for h, prefix, mass, mean in rows}
    exceptional = sorted(
        {
            (h, endpoint)
            for h, prefix, _, _ in rows
            for endpoint in canonical_endpoints(prefix)
        },
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    assert len(exceptional) == 2 ** excess - 1
    supported_height_over_q = sum(
        (mass * len(prefix) for _, prefix, mass, _ in rows), Fraction()
    )
    reset = Fraction()
    audit = []
    for h, endpoint in exceptional:
        sources = tuple(
            (prefix, mass, mean)
            for source_h, prefix, mass, mean in rows
            if source_h == h and in_prefix_basin(prefix, endpoint)
        )
        theta_over_q = sum(
            (mass * (mean - q) for _, mass, mean in sources), Fraction()
        )
        endpoint_mass, _ = by_key[(h, endpoint)]
        capacity_over_q = (len(endpoint) + 1) * endpoint_mass
        reset += theta_over_q * theta_over_q / capacity_over_q
        audit.append((h, endpoint, tuple(source for source, _, _ in sources), theta_over_q, capacity_over_q))
    if ordinary_constant is None:
        assert lambda_degree_two is None
        reset += q * (path_height - q * supported_height_over_q)
    else:
        assert lambda_degree_two is not None
        supported_weighted_over_q = sum(
            (
                sum(
                    (
                        mass
                        for source_h, prefix, mass, _ in rows
                        if source_h == h and in_prefix_basin(prefix, endpoint)
                    ),
                    Fraction(),
                )
                * (
                    basin_lambda(endpoint[0], len(endpoint) + 1)
                    if exact_all_degrees
                    else Fraction(endpoint[0], endpoint[0] + 1)
                    if len(endpoint) + 1 == 2 and exact_degree_two
                    else lambda_degree_two
                    if len(endpoint) + 1 == 2
                    else Fraction(2, len(endpoint) + 1)
                )
                for h, endpoint in exceptional
            ),
            Fraction(),
        )
        reset += q * (ordinary_constant - q * supported_weighted_over_q)
    return reset, tuple(audit)


def root_degree_tail_mass(s: int, degree: int) -> Fraction:
    """P[1+Bin(s-1,1/(s+1)) >= degree]."""
    threshold = degree - 1
    return sum(
        (
            Fraction(
                math.comb(s - 1, count) * s ** (s - 1 - count),
                (s + 1) ** (s - 1),
            )
            for count in range(threshold, s)
        ),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def basin_lambda(first_total: int, degree: int) -> Fraction:
    """Exact beta_E/degree for a canonical basin endpoint."""
    beta = Fraction(math.factorial(degree), 1) / w(first_total) * sum(
        (
            cayley(first_total, parts)
            / math.factorial(parts + degree - 1)
            for parts in range(1, first_total + 1)
        ),
        Fraction(),
    )
    return beta / degree


def finite_ordinary_constant(s: int) -> Fraction:
    """Exact all-basin coefficient sum before exceptional subtraction."""
    return sum(
        (
            w(first)
            * cayley(s - first, degree - 1)
            / (math.factorial(degree) * w(s + 1))
            * degree
            * basin_lambda(first, degree) ** 2
            for degree in range(2, s + 1)
            for first in range(1, s - degree + 2)
        ),
        Fraction(),
    )


def grouped_mass_over_q(rows, h: int, k: int) -> Fraction:
    return sum(
        (mass for row_h, prefix, mass, _ in rows if row_h == h and len(prefix) + 1 == k),
        Fraction(),
    )


def arbitrary_envelope_over_q(
    excess: int,
    ratios: tuple[Fraction, ...],
    z: Fraction,
    a: int,
    D: int,
    heights: dict[int, Fraction],
) -> Fraction:
    """All-deficit envelope needed only through excess three.

    Base excess zero is the accepted universal all-deficit terminal theorem.
    Higher levels use the exact basin envelope and recurse rank by rank.
    """
    q = split_for_excess(ratios)
    if excess == 0:
        return 1 - q
    assert excess <= 3
    reset, _ = reset_envelope_over_q(excess, ratios, z, a, D, heights[excess])
    rows, q_again = support_records(excess, ratios, z, a, D)
    assert q_again == q
    descendants = Fraction()
    for h in range(1, excess + 1):
        for k in range(1, excess - h + 2):
            mass = grouped_mass_over_q(rows, h, k)
            if not mass:
                continue
            for j in range(1, k + 1):
                nu = nu_symbolic(a, D, k, j, z)
                child_excess = h - 1
                child_ratios = ratios[-h:]
                child_q = split_for_excess(child_ratios)
                child_a = a + k
                child_D = D + k - j
                if child_excess == 0:
                    child_bound = child_q * (1 - child_q)
                else:
                    child_bound = child_q * arbitrary_envelope_over_q(
                        child_excess,
                        child_ratios,
                        z,
                        child_a,
                        child_D,
                        heights,
                    )
                descendants += mass * nu * child_bound
    return reset + descendants


def l5_envelope_over_q(
    ratios: tuple[Fraction, ...],
    z: Fraction,
    heights: dict[int, Fraction],
    ordinary_constant: Fraction,
    lambda_degree_two: Fraction,
):
    assert len(ratios) == 6
    rows, q = support_records(5, ratios, z, 0, 1)
    reset, basins = reset_envelope_over_q(
        5,
        ratios,
        z,
        0,
        1,
        heights[5],
        ordinary_constant,
        lambda_degree_two,
        True,
        True,
    )
    descendants = Fraction()
    live = []
    for h in range(1, 6):
        for k in range(1, 7 - h):
            mass = grouped_mass_over_q(rows, h, k)
            if not mass:
                continue
            ranks = []
            for j in range(1, k + 1):
                nu = nu_symbolic(0, 1, k, j, z)
                child_excess = h - 1
                child_ratios = ratios[-h:]
                child_q = split_for_excess(child_ratios)
                child_a = k
                child_D = 1 + k - j
                if child_D == 1:
                    # Accepted right-heavy contraction through L=4.
                    child_bound = child_q * (1 - child_q)
                    source = "accepted-right-heavy"
                else:
                    assert child_excess <= 3
                    child_bound = child_q * arbitrary_envelope_over_q(
                        child_excess,
                        child_ratios,
                        z,
                        child_a,
                        child_D,
                        heights,
                    )
                    source = "arbitrary-deficit-envelope"
                descendants += mass * nu * child_bound
                ranks.append((j, nu, child_D, child_bound, source))
            live.append((h, k, mass, nu_symbolic(0, 1, k, 0, z), tuple(ranks)))
    assert len(live) == 11
    return reset + descendants, q, basins, tuple(live)


def actual_parameters(s: int, K: int):
    assert s >= 6 and K >= 1
    ratios = tuple(w(s - offset) / w(s - offset + 1) for offset in range(6))
    z = Fraction(1, K + 1)
    B = s - 5
    heights = {
        ell: Fraction(B + ell - 1, B + ell + 1)
        for ell in range(1, 6)
    }
    heights[5] = Fraction(s - 1, s + 1)
    return ratios, z, heights


def cleared_slack(
    ratios: tuple[Fraction, ...],
    z: Fraction,
    heights: dict[int, Fraction],
    ordinary_constant: Fraction,
    lambda_degree_two: Fraction,
) -> Fraction:
    envelope, q, _, _ = l5_envelope_over_q(
        ratios,
        z,
        heights,
        ordinary_constant,
        lambda_degree_two,
    )
    clearing = math.prod((1 + a * z for a in range(1, 6))) ** 2
    return clearing * (1 - q - envelope)


def finite_difference_degree(values: list[Fraction]) -> int:
    row = values[:]
    for degree in range(len(values) - 1):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if all(value == 0 for value in row):
            return degree
    return len(values) - 1


@functools.lru_cache(maxsize=None)
def lagrange_to_bernstein(degree: int):
    powers = []
    for node in range(degree + 1):
        coefficients = [Fraction(1)]
        denominator = 1
        for other in range(degree + 1):
            if other == node:
                continue
            product = [Fraction()] * (len(coefficients) + 1)
            for power, coefficient in enumerate(coefficients):
                product[power] -= other * coefficient
                product[power + 1] += coefficient
            coefficients = product
            denominator *= node - other
        powers.append(tuple(value / denominator for value in coefficients))
    return tuple(
        tuple(
            sum(
                (
                    powers[node][power]
                    * Fraction(math.comb(index, power), math.comb(degree, power))
                    for power in range(index + 1)
                ),
                Fraction(),
            )
            for node in range(degree + 1)
        )
        for index in range(degree + 1)
    )


def tensor_bernstein(values: dict[tuple[int, ...], Fraction], degrees: tuple[int, ...]):
    transformed = values
    ranges = tuple(range(degree + 1) for degree in degrees)
    for axis, degree in enumerate(degrees):
        matrix = lagrange_to_bernstein(degree)
        next_values = {}
        for out in itertools.product(*ranges):
            next_values[out] = sum(
                (
                    matrix[out[axis]][node]
                    * transformed[out[:axis] + (node,) + out[axis + 1:]]
                    for node in range(degree + 1)
                ),
                Fraction(),
            )
        transformed = next_values
    return transformed


def tensor_evaluate(coefficients, degrees, point):
    answer = Fraction()
    for index, coefficient in coefficients.items():
        basis = Fraction(1)
        for degree, position, coordinate in zip(degrees, index, point):
            basis *= (
                math.comb(degree, position)
                * coordinate ** position
                * (1 - coordinate) ** (degree - position)
            )
        answer += coefficient * basis
    return answer


def record(value: Fraction):
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def direct_l1_formula(split, terminal, height, p):
    return split * (height - split / 2) + (2 * p - split) ** 2 / 4 + (1 - p) * (1 - terminal)


def direct_l2_formula(ratios, height2, height1, p, killed2, child_p):
    top, middle, terminal = ratios
    q = Fraction(3, 2) * top * middle * terminal
    a = middle * terminal
    reset = (
        q * (height2 - 5 * q / 9 - q / (3 * terminal))
        + (3 * killed2 - q) ** 2 / 27
        + (3 * killed2 + 6 * p - 4 * q) ** 2 / 54
        + (terminal * (1 - killed2) - q) ** 2 / (6 * terminal)
    )
    descendants = (1 - killed2) * (1 - terminal) / 3 + Fraction(2, 3) * (1 - p) * direct_l1_formula(a, terminal, height1, child_p)
    return reset + descendants


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=14)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--certify", action="store_true")
    args = parser.parse_args()
    started = time.time()
    failures = []
    rows = []
    support_audit = []
    basin_audit = []
    live_audit = []
    literal_reset_audit = []
    K_values = (1, 2, 5, 64, 4096)

    for s in range(6, args.s_max + 1):
        B = s - 5
        for K in K_values:
            ratios, z, heights = actual_parameters(s, K)
            ordinary_constant = finite_ordinary_constant(s)
            lambda_two = Fraction(s - 1, s)
            envelope_over_q, q, basins, live = l5_envelope_over_q(
                ratios, z, heights, ordinary_constant, lambda_two
            )
            state = (s, K, K - 1, B)
            actual_reset = reset_energy(*state)
            actual = resolvent(state)
            target = q * (1 - q)
            reset_bound, _ = reset_envelope_over_q(
                5,
                ratios,
                z,
                0,
                1,
                heights[5],
                ordinary_constant,
                lambda_two,
                True,
                True,
            )
            if actual_reset > q * reset_bound:
                failures.append({"kind": "root-reset", "s": s, "K": K})
            if actual > q * envelope_over_q:
                failures.append({"kind": "root-envelope", "s": s, "K": K})
            if q * envelope_over_q > target:
                failures.append({"kind": "scalar-sign", "s": s, "K": K})
            if actual > target:
                failures.append({"kind": "actual-sign", "s": s, "K": K})
            rows.append({
                "s": s,
                "K": K,
                "actual_ratio": record(actual / target),
                "envelope_ratio": record(envelope_over_q / (1 - q)),
                "reset_ratio_to_envelope": record(actual_reset / (q * reset_bound)),
                "slack": record(target - q * envelope_over_q),
            })
            if K == 1 and s in (6, 7, args.s_max):
                supported, _ = support_records(5, ratios, z, 0, 1)
                support_audit.append({
                    "s": s,
                    "count": len(supported),
                    "compositions": [list(prefix + (B + h,)) for h, prefix, _, _ in supported],
                })
                basin_audit.append({
                    "s": s,
                    "count": len(basins),
                    "basins": [
                        {
                            "h": h,
                            "endpoint": list(endpoint),
                            "sources": [list(source) for source in sources],
                            "theta_over_q": record(theta),
                            "capacity_over_q": record(capacity),
                        }
                        for h, endpoint, sources, theta, capacity in basins
                    ],
                })
                live_audit.append({
                    "s": s,
                    "count": len(live),
                    "groups": [
                        {
                            "h": h,
                            "k": k,
                            "retained": [
                                {"j": term[0], "deficit": term[2], "source": term[4]}
                                for term in ranks
                            ],
                        }
                        for h, k, _, _, ranks in live
                    ],
                })

            if s in (6, 7) and K in (1, 5):
                literal_rows = literal_basin_rows(*state)
                literal_reset = sum(
                    (theta * theta / capacity for _, _, theta, capacity in literal_rows),
                    Fraction(),
                )
                assert literal_reset == actual_reset == literal_reset_energy(*state)
                literal_map = {
                    endpoint: (sources, theta / q, capacity / q)
                    for endpoint, sources, theta, capacity in literal_rows
                }
                active_exception_count = 0
                for h, endpoint_prefix, source_prefixes, theta, capacity in basins:
                    endpoint = endpoint_prefix + (B + h,)
                    if endpoint[0] + endpoint[1] - 1 < 2:
                        continue
                    sources, literal_theta, literal_capacity = literal_map[endpoint]
                    expected_sources = tuple(source + (B + h,) for source in source_prefixes)
                    assert sources == expected_sources
                    assert literal_theta == theta and literal_capacity == capacity
                    active_exception_count += 1
                literal_reset_audit.append({
                    "s": s,
                    "K": K,
                    "literal_basin_count": len(literal_rows),
                    "active_exception_count": active_exception_count,
                    "grouped_equals_literal": True,
                    "exception_currents_and_capacities_match": True,
                })

    child_audit = []
    for excess in (1, 2, 3):
        for S in range(excess + 1, 9):
            B = S - excess
            ratios = tuple(w(S - offset) / w(S - offset + 1) for offset in range(excess + 1))
            heights = {ell: Fraction(B + ell - 1, B + ell + 1) for ell in range(1, excess + 1)}
            q = split_for_excess(ratios)
            assert q == q_split(S, B)
            for K in range(2, 9):
                for R in range(1, K):
                    D = K - R
                    z = Fraction(1, K + 1)
                    envelope = arbitrary_envelope_over_q(excess, ratios, z, 0, D, heights)
                    state = (S, K, R, B)
                    actual = resolvent(state)
                    if actual > q * envelope:
                        failures.append({"kind": f"child-L{excess}", "state": list(state)})
                    if excess == 1:
                        direct = direct_l1_formula(ratios[0] * ratios[1], ratios[1], heights[1], Fraction(D, K + 1))
                        assert envelope == direct
                    elif excess == 2:
                        direct = direct_l2_formula(
                            ratios,
                            heights[2],
                            heights[1],
                            Fraction(D, K + 1),
                            Fraction(D * (D + 1), (K + 1) * (K + 2)),
                            Fraction(D, K + 2),
                        )
                        assert envelope == direct
                    child_audit.append({
                        "excess": excess,
                        "S": S,
                        "K": K,
                        "R": R,
                        "deficit": D,
                        "ratio": (
                            record(actual / (q * envelope))
                            if q * envelope
                            else {"numerator": "0", "denominator": "1", "decimal": 0.0}
                        ),
                    })

    certificates = None
    if args.certify:
        finite = []
        detected = []
        # Overclear by prod_(a=1)^5(1+a z)^2.  Exact differences determine
        # the actual degree before any Bernstein assertion is made.
        for s in range(6, 100):
            ratios, _, heights = actual_parameters(s, 1)
            ordinary_constant = finite_ordinary_constant(s)
            lambda_two = Fraction(s - 1, s)
            values = [
                cleared_slack(
                    ratios,
                    Fraction(node, 2),
                    heights,
                    ordinary_constant,
                    lambda_two,
                )
                for node in range(16)
            ]
            degree = finite_difference_degree(values)
            detected.append(degree)
            coefficients = tensor_bernstein(
                {(node,): values[node] for node in range(degree + 1)},
                (degree,),
            )
            finite.append({
                "s": s,
                "degree": degree,
                "minimum": record(min(coefficients.values())),
                "nonpositive_count": sum(value <= 0 for value in coefficients.values()),
                "coefficients": [record(coefficients[(i,)]) for i in range(degree + 1)],
            })
        assert len(set(detected)) == 1
        z_degree = detected[0]

        representative = (
            Fraction(7, 20), Fraction(9, 25), Fraction(11, 30),
            Fraction(3, 8), Fraction(19, 50), Fraction(23, 60),
        )
        unit_heights = {ell: Fraction(1) for ell in range(1, 6)}
        tail_ordinary_constant = Fraction(3, 4)
        tail_lambda_two = Fraction(1)
        ratio_degrees = []
        for axis in range(6):
            axis_values = []
            for node in range(4):
                variables = list(representative)
                variables[axis] = Fraction(1, 3) + Fraction(node, 15)
                axis_values.append(cleared_slack(
                    tuple(variables),
                    Fraction(2, 7),
                    unit_heights,
                    tail_ordinary_constant,
                    tail_lambda_two,
                ))
            ratio_degrees.append(finite_difference_degree(axis_values))
        degrees = tuple(ratio_degrees) + (z_degree,)
        ratio_left = Fraction(4, 11)
        ratio_right = Fraction(187, 500)
        lefts = (ratio_left,) * 6 + (Fraction(),)
        spans = (ratio_right - ratio_left,) * 6 + (Fraction(1, 2),)
        ranges = tuple(range(degree + 1) for degree in degrees)
        box_values = {}
        for index in itertools.product(*ranges):
            physical = tuple(left + span * node for left, span, node in zip(lefts, spans, index))
            box_values[index] = cleared_slack(
                tuple(physical[:-1]),
                physical[-1],
                unit_heights,
                tail_ordinary_constant,
                tail_lambda_two,
            )
        box_coefficients = tensor_bernstein(box_values, degrees)
        minimum_index, minimum = min(box_coefficients.items(), key=lambda item: item[1])
        test_point = tuple(Fraction(i + 1, 10) for i in range(7))
        interpolated = tensor_evaluate(box_coefficients, degrees, test_point)
        physical = tuple(left + span * coordinate for left, span, coordinate in zip(lefts, spans, test_point))
        assert interpolated == cleared_slack(
            tuple(physical[:-1]),
            physical[-1],
            unit_heights,
            tail_ordinary_constant,
            tail_lambda_two,
        )
        certificates = {
            "clearing": "prod_(a=1)^5(1+a*z)^2 [1-q-E5]",
            "detected_degrees": list(degrees),
            "finite": {
                "range": "s=6,...,99; z in [0,1/2]",
                "rows": finite,
                "nonpositive_count": sum(row["nonpositive_count"] for row in finite),
            },
            "tail": {
                "range": "six ratios in [4/11,187/500], z in [0,1/2], heights=1; contains all s>=100; conditional on ordinary coefficient <=3/4",
                "coefficient_count": len(box_coefficients),
                "minimum_index": list(minimum_index),
                "minimum": record(minimum),
                "nonpositive_count": sum(value <= 0 for value in box_coefficients.values()),
                "off_grid_identity": True,
                "coefficients": [
                    {"index": list(index), "value": record(value)}
                    for index, value in sorted(box_coefficients.items())
                ],
            },
        }

    coarse_s, coarse_K = 7, 4096
    coarse_ratios, coarse_z, coarse_heights = actual_parameters(coarse_s, coarse_K)
    refined_total, coarse_q, _, _ = l5_envelope_over_q(
        coarse_ratios,
        coarse_z,
        coarse_heights,
        finite_ordinary_constant(coarse_s),
        Fraction(coarse_s - 1, coarse_s),
    )
    refined_reset, _ = reset_envelope_over_q(
        5,
        coarse_ratios,
        coarse_z,
        0,
        1,
        coarse_heights[5],
        finite_ordinary_constant(coarse_s),
        Fraction(coarse_s - 1, coarse_s),
        True,
        True,
    )
    coarse_reset, _ = reset_envelope_over_q(
        5, coarse_ratios, coarse_z, 0, 1, coarse_heights[5]
    )
    coarse_total = coarse_reset + refined_total - refined_reset
    coarse_target = coarse_q * (1 - coarse_q)
    coarse_actual = resolvent((coarse_s, coarse_K, coarse_K - 1, coarse_s - 5))
    assert coarse_q * coarse_total > coarse_target
    assert coarse_actual < coarse_target

    boundary_state = (6, 1, 0, 1)
    boundary_children = children(boundary_state)
    assert all(child[0] >= 2 for _, child, _, _, _ in boundary_children)
    assert all(t >= 3 for _, _, _, t, _ in boundary_children)

    ratio_95 = w(95) / w(96)
    ratio_lower = Fraction(4, 11)
    ratio_upper = Fraction(187, 500)
    assert ratio_95 == Fraction(95 ** 94, 96 ** 94)
    assert ratio_95 < ratio_upper
    e_lower_partial = sum(
        (Fraction(1, math.factorial(n)) for n in range(6)),
        Fraction(),
    )
    assert e_lower_partial == Fraction(163, 60)
    assert 2 * (3 - e_lower_partial) == Fraction(17, 30)

    scalar_ranks = (6, 7, 30, 50, 99, 100)
    scalar_audit = [{"s": s, "C_s": record(finite_ordinary_constant(s))} for s in scalar_ranks]
    for A in range(1, 51):
        assert basin_lambda(A, 2) == Fraction(A, A + 1)
        for degree in range(2, 12):
            assert basin_lambda(A, degree) <= Fraction(2 * A, degree * (A + 1))

    payload = {
        "claim_tested": "auxiliary right-heavy complete unweighted contraction at L=5",
        "scope": "nonlazy minimal-long-cycle parking reset operator only",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "command": "python3 -B l5_exact.py --s-max %d%s --output %s" % (args.s_max, " --certify" if args.certify else "", args.output),
        "parameters": {"s_min": 6, "s_max": args.s_max, "K_values": list(K_values)},
        "support_audit": support_audit,
        "basin_audit": basin_audit,
        "live_audit": live_audit,
        "literal_reset_audit": literal_reset_audit,
        "boundary_s6": {
            "state": list(boundary_state),
            "actual_retained_children": [
                {"k": k, "t": t, "j": j, "child": list(child)}
                for _, child, k, t, j in boundary_children
            ],
            "all_t_equals_2_children_inactive": True,
        },
        "ratio_box_audit": {
            "lower_endpoint": record(ratio_lower),
            "upper_endpoint": record(ratio_upper),
            "b_95": record(ratio_95),
            "upper_slack": record(ratio_upper - ratio_95),
            "lower_proof": "b_n>1/e and e<11/4 by a geometric factorial-tail bound",
            "e_lower_partial_for_17_over_30": record(e_lower_partial),
        },
        "coarse_template_obstruction": {
            "state": [coarse_s, coarse_K, coarse_K - 1, coarse_s - 5],
            "coarse_envelope_ratio": record(coarse_total / (1 - coarse_q)),
            "actual_ratio": record(coarse_actual / coarse_target),
            "status": "refutes only inherited beta<=degree envelope sign",
        },
        "scalar_audit": scalar_audit,
        "child_audit": child_audit,
        "rows": rows,
        "failure_count": len(failures),
        "failures": failures,
        "certificates": certificates,
        "elapsed_seconds": time.time() - started,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "failure_count": len(failures),
        "max_actual_ratio": max(float(row["actual_ratio"]["decimal"]) for row in rows),
        "max_envelope_ratio": max(float(row["envelope_ratio"]["decimal"]) for row in rows),
        "finite_nonpositive": certificates["finite"]["nonpositive_count"] if certificates else None,
        "tail_nonpositive": certificates["tail"]["nonpositive_count"] if certificates else None,
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
