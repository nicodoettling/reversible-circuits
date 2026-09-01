#!/usr/bin/env python3
"""Exact discovery and proof certificates for suffix excess four.

The script is standalone: it imports no predecessor implementation or output.
It reconstructs the accepted all-rank finite-DAG recurrence from its defining
formulas, enumerates the L=4 support and canonical basins literally, and tests
a closed reset-plus-descendant envelope.  All arithmetic is exact Fraction
arithmetic; finite rows are audits, while Bernstein coefficients (when
enabled below) are the algebraic sign certificates.
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
def ordered_compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for first in range(1, n + 1):
        for tail in ordered_compositions(n - first):
            rows.append((first,) + tail)
    return tuple(rows)


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
        numerator = K * safe_comb(k + K - R - 2, K - R - 1)
        denominator = safe_comb(k + K - 1, K - 1)
        return Fraction(numerator, denominator) if denominator else Fraction()
    ratio = Fraction(
        safe_comb(K, R + 1),
        safe_comb(K + k, R + 1),
    )
    return q_split(t - 1, B) * (1 - ratio)


def attachment(K: int, R: int, k: int, j: int) -> Fraction:
    return Fraction(
        safe_comb(R + j, j)
        * safe_comb(K - R - 1 + k - j, k - j),
        safe_comb(K + k, k),
    )


@functools.lru_cache(maxsize=None)
def groups(s: int) -> tuple[tuple[int, int, Fraction], ...]:
    rows: list[tuple[int, int, Fraction]] = []
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
    """Exact active canonical reset energy, grouped only after derivation."""
    q_parent = q_split(s, B)
    answer = Fraction()
    scalar_cache: dict[tuple[int, int, int], Fraction] = {}

    def scalar(first_total: int, tail_count: int, last: int) -> Fraction:
        key = (first_total, tail_count, last)
        if key not in scalar_cache:
            scalar_cache[key] = sum(
                (
                    cayley(first_total, p)
                    * (
                        contextual(p + tail_count, last, K, R, B)
                        - q_parent
                    )
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
                        * current
                        * current
                        / (w(first_total) * w(s + 1))
                    )
    return answer


@functools.lru_cache(maxsize=None)
def literal_basin_structure(s: int):
    """All active canonical endpoints and their literal source basins."""
    compositions = ordered_compositions(s)
    rows = []
    endpoints = sorted(
        {
            endpoint
            for source in compositions
            if len(source) >= 2
            for endpoint in (
                (sum(source[:cut]),) + source[cut:]
                for cut in range(1, len(source))
            )
            if endpoint[0] + endpoint[1] - 1 >= 2
        },
        key=lambda endpoint: (len(endpoint), endpoint),
    )
    for endpoint in endpoints:
        sources = tuple(
            source
            for source in compositions
            if source_in_prefix_basin(source, endpoint)
        )
        rows.append((endpoint, sources))
    return tuple(rows)


def literal_basin_rows(s: int, K: int, R: int, B: int):
    """Literal current/capacity rows, with no grouped basin formula."""
    q = q_split(s, B)
    root_mass = {
        parts: math.prod((w(part) for part in parts))
        / (math.factorial(len(parts)) * w(s + 1))
        for parts in ordered_compositions(s)
    }
    rows = []
    for endpoint, sources in literal_basin_structure(s):
        theta = sum(
            (
                root_mass[source]
                * (contextual(len(source), source[-1], K, R, B) - q)
                for source in sources
            ),
            Fraction(),
        )
        capacity = len(endpoint) * root_mass[endpoint]
        rows.append((endpoint, sources, theta, capacity))
    return tuple(rows)


def literal_reset_energy(s: int, K: int, R: int, B: int) -> Fraction:
    return sum(
        (theta * theta / capacity for _, _, theta, capacity in literal_basin_rows(s, K, R, B)),
        Fraction(),
    )


@functools.lru_cache(maxsize=None)
def children(x: tuple[int, int, int, int]):
    s, K, R, B = x
    rows = []
    phase = s + K - R
    for k, t, mass in groups(s):
        if t <= B or t - 1 < 2:
            continue
        assert sum(
            (attachment(K, R, k, j) for j in range(k + 1)),
            Fraction(),
        ) == 1
        for j in range(1, k + 1):
            coefficient = attachment(K, R, k, j)
            if coefficient:
                child = (t - 1, K + k, R + j, B)
                assert child[0] + child[1] - child[2] < phase
                rows.append((mass * coefficient, child, k, t, j))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def resolvent(x: tuple[int, int, int, int]) -> Fraction:
    return reset_energy(*x) + sum(
        (mass * resolvent(child) for mass, child, _, _, _ in children(x)),
        Fraction(),
    )


def delta(rank: int, z: Fraction) -> Fraction:
    """Fresh/right-heavy killed attachment mass for a rank-size group."""
    assert rank >= 1
    denominator = math.prod((1 + a * z for a in range(1, rank)))
    return math.factorial(rank) * z ** rank / denominator


def nu_right_heavy(k: int, j: int, z: Fraction) -> Fraction:
    assert 0 <= j <= k
    if j == 0:
        return delta(k, z)
    numerator = Fraction(math.factorial(k), math.factorial(j))
    numerator *= z ** (k - j) * (1 - z)
    numerator *= math.prod((1 + a * z for a in range(1, j - 1)))
    denominator = math.prod((1 + a * z for a in range(1, k)))
    return numerator / denominator


def l1_envelope_over_q(
    split: Fraction,
    terminal_ratio: Fraction,
    path_height: Fraction,
    p: Fraction,
) -> Fraction:
    """Accepted arbitrary-deficit L=1 envelope H/split."""
    return (
        split * (path_height - split / 2)
        + (2 * p - split) ** 2 / 4
        + (1 - p) * (1 - terminal_ratio)
    )


def l2_envelope_over_q(
    top_ratio: Fraction,
    middle_ratio: Fraction,
    terminal_ratio: Fraction,
    path_height: Fraction,
    child_path_height: Fraction,
    p: Fraction,
    killed_two: Fraction,
    child_p: Fraction,
) -> Fraction:
    """New arbitrary-deficit L=2 envelope H/q.

    The context split is q=(3/2)*top_ratio*middle_ratio*terminal_ratio.
    Here p=D/(K+1), killed_two=D(D+1)/[(K+1)(K+2)], and
    child_p=D/(K+2).  The proof is the L=2 basin calculation with p replacing
    the right-heavy z, followed by the all-deficit terminal theorem and the
    accepted arbitrary-deficit L=1 envelope.
    """
    reset, descendants = l2_envelope_parts_over_q(
        top_ratio,
        middle_ratio,
        terminal_ratio,
        path_height,
        child_path_height,
        p,
        killed_two,
        child_p,
    )
    return reset + descendants


def l2_envelope_parts_over_q(
    top_ratio: Fraction,
    middle_ratio: Fraction,
    terminal_ratio: Fraction,
    path_height: Fraction,
    child_path_height: Fraction,
    p: Fraction,
    killed_two: Fraction,
    child_p: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return the reset and descendant pieces of the L=2 bound."""
    a = middle_ratio * terminal_ratio
    q = Fraction(3, 2) * top_ratio * a
    d = killed_two
    reset = (
        q * (path_height - 5 * q / 9 - q / (3 * terminal_ratio))
        + (3 * d - q) ** 2 / 27
        + (3 * d + 6 * p - 4 * q) ** 2 / 54
        + (terminal_ratio * (1 - d) - q) ** 2
        / (6 * terminal_ratio)
    )
    descendants = (
        (1 - d) * (1 - terminal_ratio) / 3
        + Fraction(2, 3)
        * (1 - p)
        * l1_envelope_over_q(
            a,
            terminal_ratio,
            child_path_height,
            child_p,
        )
    )
    return reset, descendants


def support_records_generic(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    x: Fraction,
    z: Fraction,
):
    """Literal L=4 support as records `(h,prefix,mass/q,mean)`."""
    ratios = (x, y, v, u)
    q = w(5) * r * u * v * y * x
    rows = []
    for h in range(5):
        prefix_total = 4 - h
        ratio_product = math.prod(ratios[:h])
        child_split = w(h) * ratio_product if h else None
        for prefix in ordered_compositions(prefix_total):
            k = len(prefix) + 1
            prefix_weight = math.prod((w(part) for part in prefix))
            mass_over_q = prefix_weight / (
                math.factorial(k) * w(5) * ratio_product
            )
            if h == 0:
                mean = k * delta(k - 1, z)
            else:
                mean = child_split * (1 - delta(k, z))
            rows.append((h, prefix, mass_over_q, mean))
    assert len(rows) == 16
    mean_over_q = sum((mass * mean for _, _, mass, mean in rows), Fraction())
    assert mean_over_q == 1
    return tuple(rows), q


def canonical_prefix_endpoints(prefix: tuple[int, ...]):
    return tuple(
        (sum(prefix[:cut]),) + prefix[cut:]
        for cut in range(1, len(prefix) + 1)
    )


def source_in_prefix_basin(
    source: tuple[int, ...], endpoint: tuple[int, ...]
) -> bool:
    first = endpoint[0]
    tail = endpoint[1:]
    for cut in range(1, len(source) + 1):
        if sum(source[:cut]) == first and source[cut:] == tail:
            return True
    return False


def l4_reset_envelope_over_q_generic(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    x: Fraction,
    z: Fraction,
    path_height: Fraction,
) -> tuple[Fraction, tuple[dict[str, object], ...]]:
    rows, q = support_records_generic(r, u, v, y, x, z)
    by_key = {(h, prefix): (mass, mean) for h, prefix, mass, mean in rows}
    exceptional = sorted(
        {
            (h, endpoint)
            for h, prefix, _, _ in rows
            for endpoint in canonical_prefix_endpoints(prefix)
        },
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    assert len(exceptional) == 15
    supported_height_over_q = sum(
        (mass * len(prefix) for _, prefix, mass, _ in rows), Fraction()
    )
    reset = q * (path_height - q * supported_height_over_q)
    audit = []
    for h, endpoint in exceptional:
        sources = tuple(
            (prefix, mass, mean)
            for source_h, prefix, mass, mean in rows
            if source_h == h and source_in_prefix_basin(prefix, endpoint)
        )
        theta_over_q = sum(
            (mass * (mean - q) for _, mass, mean in sources), Fraction()
        )
        endpoint_mass, _ = by_key[(h, endpoint)]
        capacity_over_q = (len(endpoint) + 1) * endpoint_mass
        reset += theta_over_q ** 2 / capacity_over_q
        audit.append({
            "h": h,
            "endpoint_prefix": endpoint,
            "source_prefixes": tuple(source for source, _, _ in sources),
            "theta_over_q": theta_over_q,
            "capacity_over_q": capacity_over_q,
        })
    return reset, tuple(audit)


def l4_descendant_envelope_over_q_generic(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    x: Fraction,
    z: Fraction,
    l1_height: Fraction,
    l2_height: Fraction,
) -> tuple[Fraction, tuple[dict[str, object], ...]]:
    rows, q = support_records_generic(r, u, v, y, x, z)
    group_mass = {
        (h, k): sum(
            (
                mass
                for row_h, prefix, mass, _ in rows
                if row_h == h and len(prefix) + 1 == k
            ),
            Fraction(),
        )
        for h in range(1, 5)
        for k in range(1, 6)
    }
    answer = Fraction()
    audit = []
    for h in range(1, 5):
        for k in range(1, 6):
            mass_over_q = group_mass[(h, k)]
            if not mass_over_q:
                continue
            rank_terms = []
            for j in range(1, k + 1):
                nu = nu_right_heavy(k, j, z)
                deficit = k + 1 - j
                if h == 1:
                    child_bound = x * (1 - x)
                elif h == 2:
                    child_split = x * y
                    child_p = deficit * z / (1 + k * z)
                    child_bound = child_split * l1_envelope_over_q(
                        child_split, x, l1_height, child_p
                    )
                elif h == 3:
                    assert k == 2
                    child_split = Fraction(3, 2) * v * y * x
                    if deficit == 1:
                        # j=2 is right-heavy, so the accepted L=2 theorem is
                        # sharper than the arbitrary-deficit envelope.
                        child_bound = child_split * (1 - child_split)
                    else:
                        assert deficit == 2
                        child_p = deficit * z / (1 + 2 * z)
                        child_d = (
                            deficit
                            * (deficit + 1)
                            * z ** 2
                            / ((1 + 2 * z) * (1 + 3 * z))
                        )
                        grandchild_p = deficit * z / (1 + 3 * z)
                        child_bound = child_split * l2_envelope_over_q(
                            v,
                            y,
                            x,
                            l2_height,
                            l1_height,
                            child_p,
                            child_d,
                            grandchild_p,
                        )
                else:
                    assert h == 4 and k == 1 and deficit == 1
                    child_split = Fraction(8, 3) * u * v * y * x
                    child_bound = child_split * (1 - child_split)
                answer += mass_over_q * nu * child_bound
                rank_terms.append((j, nu, deficit, child_bound))
            audit.append({
                "h": h,
                "k": k,
                "mass_over_q": mass_over_q,
                "killed": nu_right_heavy(k, 0, z),
                "ranks": tuple(rank_terms),
            })
    assert len(audit) == 7
    return answer, tuple(audit)


def l4_envelope_over_q_generic(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    x: Fraction,
    z: Fraction,
    root_height: Fraction,
    l1_height: Fraction,
    l2_height: Fraction,
) -> tuple[Fraction, Fraction]:
    reset, _ = l4_reset_envelope_over_q_generic(
        r, u, v, y, x, z, root_height
    )
    descendants, _ = l4_descendant_envelope_over_q_generic(
        r, u, v, y, x, z, l1_height, l2_height
    )
    q = w(5) * r * u * v * y * x
    return reset + descendants, q


def cleared_slack_generic(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    x: Fraction,
    z: Fraction,
    root_height: Fraction,
    l1_height: Fraction,
    l2_height: Fraction,
) -> Fraction:
    envelope, q = l4_envelope_over_q_generic(
        r, u, v, y, x, z, root_height, l1_height, l2_height
    )
    denominator = math.prod((1 + a * z for a in range(1, 5))) ** 2
    return denominator * (1 - q - envelope)


def finite_difference_degree(values: list[Fraction]) -> int:
    """Return the exact degree detected from equally spaced values."""
    row = values[:]
    for degree in range(len(values) - 1):
        next_row = [
            row[index + 1] - row[index]
            for index in range(len(row) - 1)
        ]
        if all(value == 0 for value in next_row):
            return degree
        row = next_row
    return len(values) - 1


@functools.lru_cache(maxsize=None)
def lagrange_to_bernstein_matrix(degree: int):
    """Values at integer nodes 0..d to Bernstein coefficients on [0,1]."""
    lagrange_power = []
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
        lagrange_power.append(tuple(value / denominator for value in coefficients))
    return tuple(
        tuple(
            sum(
                (
                    lagrange_power[node][power]
                    * Fraction(math.comb(index, power), math.comb(degree, power))
                    for power in range(index + 1)
                ),
                Fraction(),
            )
            for node in range(degree + 1)
        )
        for index in range(degree + 1)
    )


def tensor_bernstein(
    values: dict[tuple[int, ...], Fraction],
    degrees: tuple[int, ...],
) -> dict[tuple[int, ...], Fraction]:
    transformed = values
    ranges = tuple(range(degree + 1) for degree in degrees)
    for axis, degree in enumerate(degrees):
        matrix = lagrange_to_bernstein_matrix(degree)
        next_values = {}
        for output_index in itertools.product(*ranges):
            next_values[output_index] = sum(
                (
                    matrix[output_index[axis]][node]
                    * transformed[
                        output_index[:axis]
                        + (node,)
                        + output_index[axis + 1 :]
                    ]
                    for node in range(degree + 1)
                ),
                Fraction(),
            )
        transformed = next_values
    return transformed


def tensor_bernstein_evaluate(
    coefficients: dict[tuple[int, ...], Fraction],
    degrees: tuple[int, ...],
    point: tuple[Fraction, ...],
) -> Fraction:
    assert len(degrees) == len(point)
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


def actual_parameters(s: int, K: int):
    assert s >= 5 and K >= 1
    return (
        w(s) / w(s + 1),
        w(s - 1) / w(s),
        w(s - 2) / w(s - 1),
        w(s - 3) / w(s - 2),
        w(s - 4) / w(s - 3),
        Fraction(1, K + 1),
        Fraction(s - 1, s + 1),
        Fraction(s - 4, s - 2),
        Fraction(s - 3, s - 1),
    )


def record(value: Fraction) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s-max", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--certify", action="store_true")
    args = parser.parse_args()
    started = time.time()

    K_values = (1, 2, 5, 64, 4096)
    rows = []
    failures = []
    support_audit = []
    basin_audit = []
    live_audit = []
    literal_reset_audit = []
    for s in range(5, args.s_max + 1):
        B = s - 4
        for K in K_values:
            params = actual_parameters(s, K)
            r, u, v, y, x, z, h0, h1, h2 = params
            support, q = support_records_generic(r, u, v, y, x, z)
            direct_support = []
            for h, prefix, expected_ratio, expected_mean in support:
                parts = prefix + (B + h,)
                k, t = len(parts), parts[-1]
                direct_mass = math.prod((w(part) for part in parts)) / (
                    math.factorial(k) * w(s + 1)
                )
                assert direct_mass / q == expected_ratio
                assert contextual(k, t, K, K - 1, B) == expected_mean
                direct_support.append(parts)
            assert len(direct_support) == 16
            nonzero_groups = tuple(
                (k, t)
                for k, t, _ in groups(s)
                if contextual(k, t, K, K - 1, B)
            )
            assert len(nonzero_groups) == 11

            reset_over_q, basins = l4_reset_envelope_over_q_generic(
                r, u, v, y, x, z, h0
            )
            descendant_over_q, live = l4_descendant_envelope_over_q_generic(
                r, u, v, y, x, z, h1, h2
            )
            assert len(basins) == 15 and len(live) == 7
            envelope_over_q = reset_over_q + descendant_over_q
            envelope = q * envelope_over_q
            target = q * (1 - q)
            state = (s, K, K - 1, B)
            actual_reset = reset_energy(*state)
            actual = resolvent(state)
            if actual_reset > q * reset_over_q:
                failures.append({"s": s, "K": K, "kind": "reset-bound"})
            if actual > envelope:
                failures.append({"s": s, "K": K, "kind": "resolvent-bound"})
            if envelope > target:
                failures.append({"s": s, "K": K, "kind": "envelope-sign"})
            if actual > target:
                failures.append({"s": s, "K": K, "kind": "actual-sign"})
            rows.append({
                "s": s,
                "K": K,
                "actual_ratio": record(actual / target),
                "envelope_ratio": record(envelope / target),
                "reset_ratio_to_envelope": record(actual_reset / (q * reset_over_q)),
                "slack": record(target - envelope),
            })
            if K == 1 and s in (5, 6, args.s_max):
                support_audit.append({
                    "s": s,
                    "K": K,
                    "compositions": [list(parts) for parts in direct_support],
                    "nonzero_groups": [list(pair) for pair in nonzero_groups],
                })
                basin_audit.append({
                    "s": s,
                    "K": K,
                    "basins": [
                        {
                            "h": row["h"],
                            "endpoint_prefix": list(row["endpoint_prefix"]),
                            "source_prefixes": [
                                list(source) for source in row["source_prefixes"]
                            ],
                        }
                        for row in basins
                    ],
                })
                live_audit.append({
                    "s": s,
                    "K": K,
                    "groups": [
                        {
                            "h": row["h"],
                            "k": row["k"],
                            "retained_j": [term[0] for term in row["ranks"]],
                        }
                        for row in live
                    ],
                })

            if s <= 9 and K in (1, 5):
                literal_rows = literal_basin_rows(*state)
                literal_reset = sum(
                    (
                        theta * theta / capacity
                        for _, _, theta, capacity in literal_rows
                    ),
                    Fraction(),
                )
                assert literal_reset == actual_reset
                literal_map = {
                    endpoint: (sources, theta / q, capacity / q)
                    for endpoint, sources, theta, capacity in literal_rows
                }
                active_exception_count = 0
                for generic_row in basins:
                    endpoint = tuple(generic_row["endpoint_prefix"]) + (
                        B + int(generic_row["h"]),
                    )
                    if endpoint[0] + endpoint[1] - 1 < 2:
                        continue
                    sources, theta_over_q, capacity_over_q = literal_map[endpoint]
                    expected_sources = tuple(
                        tuple(prefix) + (B + int(generic_row["h"]),)
                        for prefix in generic_row["source_prefixes"]
                    )
                    assert sources == expected_sources
                    assert theta_over_q == generic_row["theta_over_q"]
                    assert capacity_over_q == generic_row["capacity_over_q"]
                    active_exception_count += 1
                literal_reset_audit.append({
                    "s": s,
                    "K": K,
                    "literal_basin_count": len(literal_rows),
                    "active_exception_count": active_exception_count,
                    "grouped_equals_literal": True,
                    "exception_currents_and_capacities_match": True,
                })

    arbitrary_l2_audit = []
    for S in range(3, 10):
        B = S - 2
        top = w(S) / w(S + 1)
        middle = w(S - 1) / w(S)
        terminal = w(S - 2) / w(S - 1)
        a = middle * terminal
        q = Fraction(3, 2) * top * a
        assert q == q_split(S, B)
        for K0 in range(2, 10):
            for R0 in range(1, K0):
                deficit = K0 - R0
                p = Fraction(deficit, K0 + 1)
                d = Fraction(deficit * (deficit + 1), (K0 + 1) * (K0 + 2))
                child_p = Fraction(deficit, K0 + 2)
                reset_bound, descendant_bound = l2_envelope_parts_over_q(
                    top,
                    middle,
                    terminal,
                    Fraction(S - 1, S + 1),
                    Fraction(S - 2, S),
                    p,
                    d,
                    child_p,
                )
                expected_support = (
                    ((2, B), q / 3, 2 * p),
                    ((1, 1, B), q / 9, 3 * d),
                    ((1, S - 1), q / (3 * terminal), terminal * (1 - d)),
                    ((S,), top, a * (1 - p)),
                )
                assert sum(
                    (mass * mean for _, mass, mean in expected_support),
                    Fraction(),
                ) == q
                for parts, mass, mean in expected_support:
                    assert math.prod((w(part) for part in parts)) / (
                        math.factorial(len(parts)) * w(S + 1)
                    ) == mass
                    assert contextual(len(parts), parts[-1], K0, R0, B) == mean
                state = (S, K0, R0, B)
                actual_reset = reset_energy(*state)
                actual = resolvent(state)
                assert actual_reset <= q * reset_bound
                assert actual <= q * (reset_bound + descendant_bound)
                arbitrary_l2_audit.append({
                    "S": S,
                    "K": K0,
                    "R": R0,
                    "deficit": deficit,
                    "reset_ratio": record(actual_reset / (q * reset_bound)),
                    "resolvent_ratio": record(
                        actual / (q * (reset_bound + descendant_bound))
                    ),
                })

    certificates = None
    if args.certify:
        finite_certificates = []
        for s in range(5, 22):
            r, u, v, y, x, _, h0, h1, h2 = actual_parameters(s, 1)
            degree_values = [
                cleared_slack_generic(
                    r, u, v, y, x, Fraction(node, 2), h0, h1, h2
                )
                for node in range(12)
            ]
            detected_degree = finite_difference_degree(degree_values)
            coefficients = tensor_bernstein(
                {(node,): degree_values[node] for node in range(11)},
                (10,),
            )
            assert detected_degree == 10
            assert all(value > 0 for value in coefficients.values())
            test_coordinate = Fraction(2, 7)
            interpolated = tensor_bernstein_evaluate(
                coefficients, (10,), (test_coordinate,)
            )
            direct = cleared_slack_generic(
                r,
                u,
                v,
                y,
                x,
                Fraction(1, 2) * test_coordinate,
                h0,
                h1,
                h2,
            )
            assert interpolated == direct
            finite_certificates.append({
                "s": s,
                "detected_degree": detected_degree,
                "minimum": record(min(coefficients.values())),
                "nonpositive_count": sum(
                    value <= 0 for value in coefficients.values()
                ),
                "off_grid_identity": True,
                "coefficients": [
                    record(coefficients[(index,)]) for index in range(11)
                ],
            })

        degrees = (2, 2, 2, 2, 2, 10)
        lefts = (Fraction(1, 3),) * 5 + (Fraction(),)
        spans = (Fraction(1, 15),) * 5 + (Fraction(1, 2),)
        ranges = tuple(range(degree + 1) for degree in degrees)
        box_values = {}
        for index in itertools.product(*ranges):
            r, u, v, y, x, z = tuple(
                left + span * node
                for left, span, node in zip(lefts, spans, index)
            )
            box_values[index] = cleared_slack_generic(
                r, u, v, y, x, z, Fraction(1), Fraction(1), Fraction(1)
            )
        box_coefficients = tensor_bernstein(box_values, degrees)
        assert all(value > 0 for value in box_coefficients.values())
        minimum_index, minimum = min(
            box_coefficients.items(), key=lambda item: item[1]
        )
        tail_test_point = (
            Fraction(1, 7),
            Fraction(2, 7),
            Fraction(3, 7),
            Fraction(4, 7),
            Fraction(5, 7),
            Fraction(3, 8),
        )
        tail_interpolated = tensor_bernstein_evaluate(
            box_coefficients, degrees, tail_test_point
        )
        tail_physical = tuple(
            left + span * coordinate
            for left, span, coordinate in zip(lefts, spans, tail_test_point)
        )
        assert tail_interpolated == cleared_slack_generic(
            *tail_physical, Fraction(1), Fraction(1), Fraction(1)
        )

        representative = [
            Fraction(7, 20),
            Fraction(9, 25),
            Fraction(11, 30),
            Fraction(3, 8),
            Fraction(19, 50),
        ]
        ratio_degrees = []
        for axis in range(5):
            axis_values = []
            for node in range(4):
                variables = representative[:]
                variables[axis] = Fraction(1, 3) + Fraction(node, 15)
                axis_values.append(cleared_slack_generic(
                    *variables,
                    Fraction(2, 7),
                    Fraction(4, 5),
                    Fraction(3, 4),
                    Fraction(5, 6),
                ))
            ratio_degrees.append(finite_difference_degree(axis_values))
        z_degree = finite_difference_degree([
            cleared_slack_generic(
                *representative,
                Fraction(node, 2),
                Fraction(4, 5),
                Fraction(3, 4),
                Fraction(5, 6),
            )
            for node in range(12)
        ])
        assert tuple(ratio_degrees) == (2, 2, 2, 2, 2)
        assert z_degree == 10
        b18 = Fraction(18, 19) ** 17
        assert b18 < Fraction(2, 5)
        certificates = {
            "clearing": (
                "prod_(a=1)^4 (1+a*z)^2 * [1-q-E_4], "
                "degree <=10 in z"
            ),
            "finite": {
                "range": "s=5,...,21; z in [0,1/2]",
                "rows": finite_certificates,
                "nonpositive_count": sum(
                    row["nonpositive_count"] for row in finite_certificates
                ),
            },
            "tail": {
                "range": (
                    "r,u,v,y,x in [1/3,2/5], z in [0,1/2], "
                    "all path heights replaced by 1; contains all s>=22"
                ),
                "degrees": list(degrees),
                "coefficient_count": len(box_coefficients),
                "detected_degrees_at_generic_slice": ratio_degrees + [z_degree],
                "off_grid_tensor_identity": True,
                "minimum_index": list(minimum_index),
                "minimum": record(minimum),
                "b18": record(b18),
                "b18_below_two_fifths": True,
                "nonpositive_count": sum(
                    value <= 0 for value in box_coefficients.values()
                ),
                "coefficients": [
                    {"index": list(index), "value": record(value)}
                    for index, value in sorted(box_coefficients.items())
                ],
            },
        }

    assert not failures
    payload = {
        "claim_tested": (
            "literal L=4 support/basins/all-j recurrence and arbitrary-deficit "
            "L=2 descendant envelope"
        ),
        "status": (
            "exact finite audits plus complete Bernstein certificates; "
            "the analytic proof supplies their interpretation"
            if args.certify
            else "exact finite countersearch and formula audit only"
        ),
        "scope": "auxiliary nonlazy minimal-long-cycle reset operator",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "parameters": {
            "s_min": 5,
            "s_max": args.s_max,
            "K_values": list(K_values),
        },
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "support_audit": support_audit,
        "basin_audit": basin_audit,
        "live_audit": live_audit,
        "literal_reset_audit": literal_reset_audit,
        "arbitrary_deficit_l2_audit": arbitrary_l2_audit,
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
        "row_count": len(rows),
        "failure_count": len(failures),
        "max_actual_ratio": max(float(row["actual_ratio"]["decimal"]) for row in rows),
        "max_envelope_ratio": max(float(row["envelope_ratio"]["decimal"]) for row in rows),
        "finite_certificate_nonpositive": (
            certificates["finite"]["nonpositive_count"] if certificates else None
        ),
        "tail_certificate_nonpositive": (
            certificates["tail"]["nonpositive_count"] if certificates else None
        ),
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
