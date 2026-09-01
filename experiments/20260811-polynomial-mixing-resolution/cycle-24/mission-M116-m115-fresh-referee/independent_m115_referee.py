#!/usr/bin/env python3
"""Fresh exact referee reconstruction of M115's auxiliary L=3 theorem.

This program imports no predecessor code.  It uses literal ordered
compositions and literal canonical basins for the finite-DAG checks.  Its
Bernstein transform is based on forward differences and Newton polynomials,
not the predecessor's Lagrange matrix.  A predecessor JSON file is read only
after every fresh value has been computed, and only for post-hoc equality
comparisons.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ZERO = Fraction(0)
ONE = Fraction(1)


@functools.lru_cache(maxsize=None)
def weight(n: int) -> Fraction:
    if n < 1:
        raise ValueError("weight index must be positive")
    return Fraction(n ** (n - 1), math.factorial(n))


@functools.lru_cache(maxsize=None)
def ordered_compositions(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    return tuple(
        (first,) + tail
        for first in range(1, n + 1)
        for tail in ordered_compositions(n - first)
    )


def product(values: Iterable[Fraction]) -> Fraction:
    answer = ONE
    for value in values:
        answer *= value
    return answer


def stationary_mass(parts: tuple[int, ...]) -> Fraction:
    return product(weight(part) for part in parts) / (
        math.factorial(len(parts)) * weight(sum(parts) + 1)
    )


def split_mass(rank: int, suffix: int) -> Fraction:
    return weight(rank + 1 - suffix) * weight(suffix) / weight(rank + 1)


def safe_binomial_ratio(a: int, b: int, c: int, d: int) -> Fraction:
    if not (0 <= b <= a and 0 <= d <= c):
        return ZERO
    return Fraction(math.comb(a, b), math.comb(c, d))


def contextual_mean(
    parts: tuple[int, ...], K: int, R: int, B: int
) -> Fraction:
    k = len(parts)
    t = parts[-1]
    if t < B:
        return ZERO
    if t == B:
        return K * safe_binomial_ratio(
            k + K - R - 2,
            K - R - 1,
            k + K - 1,
            K - 1,
        )
    return split_mass(t - 1, B) * (
        ONE - safe_binomial_ratio(K, R + 1, K + k, R + 1)
    )


def attachment_mass(K: int, R: int, k: int, j: int) -> Fraction:
    if not 0 <= j <= k:
        return ZERO
    return Fraction(
        math.comb(R + j, j)
        * math.comb(K - R - 1 + k - j, k - j),
        math.comb(K + k, k),
    )


def refinements_of_first(endpoint: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(alpha + endpoint[1:] for alpha in ordered_compositions(endpoint[0]))


def reset_edge_active(endpoint: tuple[int, ...]) -> bool:
    return len(endpoint) >= 2 and endpoint[0] + endpoint[1] - 1 >= 2


def basin_current(
    endpoint: tuple[int, ...], K: int, R: int, B: int
) -> Fraction:
    q = split_mass(sum(endpoint), B)
    return sum(
        (
            stationary_mass(source)
            * (contextual_mean(source, K, R, B) - q)
            for source in refinements_of_first(endpoint)
        ),
        ZERO,
    )


@functools.lru_cache(maxsize=None)
def literal_reset(s: int, K: int, R: int, B: int) -> Fraction:
    answer = ZERO
    for endpoint in ordered_compositions(s):
        if not reset_edge_active(endpoint):
            continue
        theta = basin_current(endpoint, K, R, B)
        capacity = len(endpoint) * stationary_mass(endpoint)
        answer += theta * theta / capacity
    return answer


@functools.lru_cache(maxsize=None)
def literal_children(
    state: tuple[int, int, int, int]
) -> tuple[tuple[Fraction, tuple[int, int, int, int], tuple[int, ...], int], ...]:
    s, K, R, B = state
    phase = s + K - R
    rows = []
    for parts in ordered_compositions(s):
        k = len(parts)
        t = parts[-1]
        if t <= B or t - 1 < 2:
            continue
        assert sum((attachment_mass(K, R, k, j) for j in range(k + 1)), ZERO) == 1
        for j in range(1, k + 1):
            nu = attachment_mass(K, R, k, j)
            if nu == 0:
                continue
            child = (t - 1, K + k, R + j, B)
            assert child[0] + child[1] - child[2] < phase
            rows.append((stationary_mass(parts) * nu, child, parts, j))
    return tuple(rows)


@functools.lru_cache(maxsize=None)
def literal_resolvent(state: tuple[int, int, int, int]) -> Fraction:
    return literal_reset(*state) + sum(
        (coefficient * literal_resolvent(child) for coefficient, child, _, _ in literal_children(state)),
        ZERO,
    )


def l3_parameters(s: int, K: int) -> dict[str, Fraction]:
    r = weight(s) / weight(s + 1)
    u = weight(s - 1) / weight(s)
    v = weight(s - 2) / weight(s - 1)
    y = weight(s - 3) / weight(s - 2)
    a = u * v * y
    z = Fraction(1, K + 1)
    return {
        "r": r,
        "u": u,
        "v": v,
        "y": y,
        "a": a,
        "b": v * y,
        "c": Fraction(3, 2) * a,
        "q": Fraction(8, 3) * r * a,
        "z": z,
        "d": 2 * z * z / (1 + z),
        "e": 6 * z ** 3 / ((1 + z) * (1 + 2 * z)),
        "hbar": Fraction(s - 1, s + 1),
        "h1": Fraction(s - 3, s - 1),
    }


def expected_support(s: int, K: int) -> dict[tuple[int, ...], tuple[Fraction, Fraction]]:
    p = l3_parameters(s, K)
    B = s - 3
    q = p["q"]
    z, d, e = p["z"], p["d"], p["e"]
    y, v, a = p["y"], p["v"], p["a"]
    return {
        (3, B): (Fraction(9, 32) * q, 2 * z),
        (1, 2, B): (q / 16, 3 * d),
        (2, 1, B): (q / 16, 3 * d),
        (1, 1, 1, B): (q / 64, 4 * e),
        (2, s - 2): (3 * q / (16 * y), y * (1 - d)),
        (1, 1, s - 2): (q / (16 * y), y * (1 - e)),
        (1, s - 1): (3 * q / (16 * v * y), v * y * (1 - d)),
        (s,): (p["r"], Fraction(3, 2) * a * (1 - z)),
    }


def expected_exceptional_sources(s: int) -> dict[tuple[int, ...], set[tuple[int, ...]]]:
    B = s - 3
    return {
        (1, 1, 1, B): {(1, 1, 1, B)},
        (2, 1, B): {(2, 1, B), (1, 1, 1, B)},
        (1, 2, B): {(1, 2, B)},
        (3, B): {(3, B), (1, 2, B), (2, 1, B), (1, 1, 1, B)},
        (1, 1, s - 2): {(1, 1, s - 2)},
        (2, s - 2): {(2, s - 2), (1, 1, s - 2)},
        (1, s - 1): {(1, s - 1)},
    }


def expected_exceptional_values(
    s: int, K: int
) -> dict[tuple[int, ...], tuple[Fraction, Fraction, Fraction]]:
    p = l3_parameters(s, K)
    B = s - 3
    q, z, d, e = p["q"], p["z"], p["d"], p["e"]
    v, y = p["v"], p["y"]
    rows = {
        (1, 1, 1, B): ((4 * e - q) / 64, Fraction(1, 16), (4 * e - q) ** 2 / 256),
        (2, 1, B): ((12 * d + 4 * e - 5 * q) / 64, Fraction(3, 16), (12 * d + 4 * e - 5 * q) ** 2 / 768),
        (1, 2, B): ((3 * d - q) / 16, Fraction(3, 16), (3 * d - q) ** 2 / 48),
        (3, B): ((36 * z + 24 * d + 4 * e - 27 * q) / 64, Fraction(9, 16), (36 * z + 24 * d + 4 * e - 27 * q) ** 2 / 2304),
        (1, 1, s - 2): ((y * (1 - e) - q) / (16 * y), Fraction(3, 16) / y, (y * (1 - e) - q) ** 2 / (48 * y)),
        (2, s - 2): ((4 * y - 3 * y * d - y * e - 4 * q) / (16 * y), Fraction(3, 8) / y, (4 * y - 3 * y * d - y * e - 4 * q) ** 2 / (96 * y)),
        (1, s - 1): (3 * (v * y * (1 - d) - q) / (16 * v * y), Fraction(3, 8) / (v * y), 3 * (v * y * (1 - d) - q) ** 2 / (32 * v * y)),
    }
    return rows


def l1_envelope(S: int, K: int, R: int) -> tuple[Fraction, Fraction]:
    D = K - R
    p = Fraction(D, K + 1)
    y = weight(S - 1) / weight(S)
    b = weight(S - 1) / weight(S + 1)
    h = Fraction(S - 1, S + 1)
    F = b * (h - b / 2) + (2 * p - b) ** 2 / 4 + (1 - p) * (1 - y)
    return b * F, b


def normalized_envelope(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    z: Fraction,
    hbar: Fraction,
    h1: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    a = u * v * y
    b = v * y
    c = Fraction(3, 2) * a
    q = Fraction(8, 3) * r * a
    d = 2 * z * z / (1 + z)
    e = 6 * z ** 3 / ((1 + z) * (1 + 2 * z))
    exceptional_height = Fraction(37, 64) + Fraction(5, 16) / y + Fraction(3, 16) / (v * y)
    reset = (
        q * (hbar - q * exceptional_height)
        + (4 * e - q) ** 2 / 256
        + (12 * d + 4 * e - 5 * q) ** 2 / 768
        + (3 * d - q) ** 2 / 48
        + (36 * z + 24 * d + 4 * e - 27 * q) ** 2 / 2304
        + (y * (1 - e) - q) ** 2 / (48 * y)
        + (4 * y - 3 * y * d - y * e - 4 * q) ** 2 / (96 * y)
        + 3 * (v * y * (1 - d) - q) ** 2 / (32 * v * y)
    )
    nu1 = 2 * z * (1 - z) / (1 + z)
    nu2 = (1 - z) / (1 + z)
    p1 = 2 * z / (1 + 2 * z)
    p2 = z / (1 + 2 * z)

    def one_layer(p_attach: Fraction) -> Fraction:
        return b * (h1 - b / 2) + (2 * p_attach - b) ** 2 / 4 + (1 - p_attach) * (1 - y)

    descendants = (
        (3 * (1 - d) + (1 - e)) * (1 - y) / 16
        + Fraction(3, 16) * (nu1 * one_layer(p1) + nu2 * one_layer(p2))
        + Fraction(9, 16) * (1 - z) * (1 - c)
    )
    return reset + descendants, q, reset, descendants


@functools.lru_cache(maxsize=None)
def cleared_slack(
    r: Fraction,
    u: Fraction,
    v: Fraction,
    y: Fraction,
    z: Fraction,
    hbar: Fraction,
    h1: Fraction,
) -> Fraction:
    envelope, q, _, _ = normalized_envelope(r, u, v, y, z, hbar, h1)
    return 1728 * (1 + z) ** 2 * (1 + 2 * z) ** 2 * (1 - q - envelope)


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    answer = [ZERO] * size
    for index in range(size):
        if index < len(left):
            answer[index] += left[index]
        if index < len(right):
            answer[index] += right[index]
    return answer


def poly_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def forward_difference(values: list[Fraction]) -> list[Fraction]:
    return [values[index + 1] - values[index] for index in range(len(values) - 1)]


def final_forward_difference(values: list[Fraction]) -> Fraction:
    row = values[:]
    while len(row) > 1:
        row = forward_difference(row)
    return row[0]


def values_at_integer_nodes_to_power(values: list[Fraction]) -> list[Fraction]:
    """Recover p(x) from p(0),...,p(n) via Newton forward differences."""
    differences = values[:]
    newton_coefficients = []
    while differences:
        newton_coefficients.append(differences[0])
        differences = forward_difference(differences)

    answer = [ZERO]
    binomial_basis = [ONE]
    for order, coefficient in enumerate(newton_coefficients):
        answer = poly_add(answer, poly_scale(binomial_basis, coefficient))
        binomial_basis = poly_scale(
            poly_multiply(binomial_basis, [Fraction(-order), ONE]),
            Fraction(1, order + 1),
        )
    return answer


def power_to_bernstein(power: list[Fraction], degree: int) -> list[Fraction]:
    padded = power + [ZERO] * (degree + 1 - len(power))
    return [
        sum(
            (
                padded[order]
                * Fraction(math.comb(index, order), math.comb(degree, order))
                for order in range(index + 1)
            ),
            ZERO,
        )
        for index in range(degree + 1)
    ]


def values_to_bernstein(values: list[Fraction], degree: int) -> list[Fraction]:
    if len(values) != degree + 1:
        raise ValueError("need exactly degree+1 interpolation values")
    return power_to_bernstein(values_at_integer_nodes_to_power(values), degree)


def tensor_values_to_bernstein(
    values: dict[tuple[int, ...], Fraction], degrees: tuple[int, ...]
) -> dict[tuple[int, ...], Fraction]:
    current = dict(values)
    full_ranges = [range(degree + 1) for degree in degrees]
    for axis, degree in enumerate(degrees):
        other_axes = [index for index in range(len(degrees)) if index != axis]
        other_ranges = [full_ranges[index] for index in other_axes]
        next_values: dict[tuple[int, ...], Fraction] = {}
        for other_index in itertools.product(*other_ranges):
            template = [0] * len(degrees)
            for slot, coordinate in zip(other_axes, other_index):
                template[slot] = coordinate
            row = []
            for node in range(degree + 1):
                template[axis] = node
                row.append(current[tuple(template)])
            coefficients = values_to_bernstein(row, degree)
            for index, coefficient in enumerate(coefficients):
                template[axis] = index
                next_values[tuple(template)] = coefficient
        current = next_values
    return current


def record(value: Fraction) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def parse_record(value: dict[str, str | float]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def finite_certificate(s: int) -> list[Fraction]:
    r = weight(s) / weight(s + 1)
    u = weight(s - 1) / weight(s)
    v = weight(s - 2) / weight(s - 1)
    y = weight(s - 3) / weight(s - 2)
    hbar = Fraction(s - 1, s + 1)
    h1 = Fraction(s - 3, s - 1)
    eight_values = [
        cleared_slack(r, u, v, y, Fraction(node, 2), hbar, h1)
        for node in range(8)
    ]
    assert final_forward_difference(eight_values) == 0
    return values_to_bernstein(eight_values[:7], 6)


def asymptotic_certificate() -> tuple[dict[tuple[int, ...], Fraction], int]:
    degrees = (2, 2, 2, 2, 6)
    lefts = (Fraction(1, 3),) * 4 + (ZERO,)
    steps = (Fraction(1, 15),) * 4 + (Fraction(1, 2),)
    ranges = [range(degree + 1) for degree in degrees]

    values = {}
    for index in itertools.product(*ranges):
        coordinates = tuple(left + step * node for left, step, node in zip(lefts, steps, index))
        values[index] = cleared_slack(*coordinates, ONE, ONE)
    coefficients = tensor_values_to_bernstein(values, degrees)

    degree_checks = 0
    for axis, degree in enumerate(degrees):
        other_axes = [position for position in range(5) if position != axis]
        other_ranges = [ranges[position] for position in other_axes]
        for other_index in itertools.product(*other_ranges):
            lattice = [0] * 5
            for position, node in zip(other_axes, other_index):
                lattice[position] = node
            row = []
            for node in range(degree + 2):
                lattice[axis] = node
                coordinates = tuple(left + step * value for left, step, value in zip(lefts, steps, lattice))
                row.append(cleared_slack(*coordinates, ONE, ONE))
            assert final_forward_difference(row) == 0
            degree_checks += 1
    return coefficients, degree_checks


def fresh_audit() -> dict[str, object]:
    failures: list[str] = []
    support_rows = []
    basin_rows = []
    finite_dag_rows = []

    for s, K in ((4, 1), (5, 2), (7, 5)):
        B = s - 3
        q = split_mass(s, B)
        supported = {
            parts: (stationary_mass(parts), contextual_mean(parts, K, K - 1, B))
            for parts in ordered_compositions(s)
            if contextual_mean(parts, K, K - 1, B) != 0
        }
        expected = expected_support(s, K)
        if supported != expected:
            failures.append(f"support mismatch at s={s},K={K}")
        if sum((mass * mean for mass, mean in supported.values()), ZERO) != q:
            failures.append(f"root mean mismatch at s={s},K={K}")

        expected_sources = expected_exceptional_sources(s)
        observed_sources = {}
        support_set = set(supported)
        for endpoint in ordered_compositions(s):
            if len(endpoint) < 2:
                continue
            intersection = set(refinements_of_first(endpoint)) & support_set
            if intersection:
                observed_sources[endpoint] = intersection
        if observed_sources != expected_sources:
            failures.append(f"exceptional nesting mismatch at s={s},K={K}")

        expected_values = expected_exceptional_values(s, K)
        for endpoint, (theta_over_q, cap_over_q, energy_over_q) in expected_values.items():
            theta = basin_current(endpoint, K, K - 1, B)
            capacity = len(endpoint) * stationary_mass(endpoint)
            actual = (theta / q, capacity / q, theta * theta / capacity / q)
            if actual != (theta_over_q, cap_over_q, energy_over_q):
                failures.append(f"exceptional current mismatch {s=} {K=} {endpoint=}")

        total_height = sum(
            (stationary_mass(parts) * (len(parts) - 1) for parts in ordered_compositions(s)),
            ZERO,
        )
        expected_height = Fraction(s - 1, s + 1)
        if total_height != expected_height:
            failures.append(f"path height mismatch at s={s}")
        supported_height = sum(
            (
                stationary_mass(source)
                for endpoint, sources in observed_sources.items()
                for source in sources
            ),
            ZERO,
        )
        p = l3_parameters(s, K)
        formula_height = q * (
            Fraction(37, 64)
            + Fraction(5, 16) / p["y"]
            + Fraction(3, 16) / (p["v"] * p["y"])
        )
        if supported_height != formula_height:
            failures.append(f"supported path-height mismatch at s={s},K={K}")

        support_rows.append(
            {
                "s": s,
                "K": K,
                "supported_count": len(supported),
                "exceptional_basin_count": len(observed_sources),
                "mean": record(q),
                "total_height": record(total_height),
                "supported_exceptional_height": record(supported_height),
            }
        )
        basin_rows.append(
            {
                "s": s,
                "K": K,
                "endpoints": [list(endpoint) for endpoint in sorted(observed_sources)],
                "currents_match": True,
                "capacities_match": True,
                "energies_match": True,
            }
        )

    l1_rows = []
    for S in range(2, 8):
        for K in range(2, 9):
            for R in range(1, K):
                actual = literal_resolvent((S, K, R, S - 1))
                upper, b = l1_envelope(S, K, R)
                if actual > upper:
                    failures.append(f"L1 envelope failure at {(S,K,R)}")
                l1_rows.append(
                    {
                        "context": [S, K, R, S - 1],
                        "deficit": K - R,
                        "actual_over_b": record(actual / b),
                        "envelope_over_b": record(upper / b),
                    }
                )

    for s in range(4, 9):
        for K in (1, 2, 5):
            B = s - 3
            p = l3_parameters(s, K)
            state = (s, K, K - 1, B)
            actual_reset = literal_reset(*state)
            actual = literal_resolvent(state)
            E, q, reset_over_q, descendants_over_q = normalized_envelope(
                p["r"], p["u"], p["v"], p["y"], p["z"], p["hbar"], p["h1"]
            )
            reset_bound = q * reset_over_q
            envelope = q * E
            target = q * (1 - q)
            if not actual_reset <= reset_bound:
                failures.append(f"reset envelope failure at {state}")
            if not actual <= envelope <= target:
                failures.append(f"full envelope failure at {state}")
            live_ranks = sorted(
                {
                    (len(parts), parts[-1], j)
                    for _, _, parts, j in literal_children(state)
                }
            )
            finite_dag_rows.append(
                {
                    "context": list(state),
                    "reset": record(actual_reset),
                    "reset_bound": record(reset_bound),
                    "resolvent": record(actual),
                    "envelope": record(envelope),
                    "target": record(target),
                    "resolvent_ratio": record(actual / target),
                    "envelope_ratio": record(envelope / target),
                    "live_group_ranks": [list(row) for row in live_ranks],
                    "descendant_envelope_over_q": record(descendants_over_q),
                }
            )

    finite_coefficients = {}
    for s in range(4, 21):
        coefficients = finite_certificate(s)
        if not all(value > 0 for value in coefficients):
            failures.append(f"finite Bernstein nonpositive at s={s}")
        finite_coefficients[str(s)] = [record(value) for value in coefficients]

    tensor_coefficients, tensor_degree_checks = asymptotic_certificate()
    if not all(value > 0 for value in tensor_coefficients.values()):
        failures.append("asymptotic tensor Bernstein nonpositive")
    minimum_index, minimum = min(tensor_coefficients.items(), key=lambda item: item[1])
    if minimum != Fraction(682328, 28125) or minimum_index != (2, 2, 2, 0, 0):
        failures.append("asymptotic tensor minimum mismatch")
    b18 = Fraction(18, 19) ** 17
    if not b18 < Fraction(2, 5):
        failures.append("b18 upper bound failure")

    return {
        "scope": "auxiliary full nonlazy minimal-long-cycle reset excursion, right-heavy L=3 only",
        "convention": "(pq)(x)=p(q(x)); factors displayed left-to-right",
        "arithmetic": "fractions.Fraction exact",
        "python": platform.python_version(),
        "seed": None,
        "support_and_basin_rows": support_rows,
        "exceptional_value_rows": basin_rows,
        "l1_arbitrary_deficit": {
            "row_count": len(l1_rows),
            "rows": l1_rows,
        },
        "finite_dag": {
            "row_count": len(finite_dag_rows),
            "rows": finite_dag_rows,
        },
        "finite_bernstein": {
            "range": "s=4,...,20; z in [0,1/2]",
            "degree": 6,
            "degree_seven_forward_differences_zero": True,
            "coefficients": finite_coefficients,
        },
        "asymptotic_bernstein": {
            "box": "[1/3,2/5]^4 x [0,1/2]",
            "degrees": [2, 2, 2, 2, 6],
            "degree_check_slice_count": tensor_degree_checks,
            "coefficient_count": len(tensor_coefficients),
            "minimum_index": list(minimum_index),
            "minimum": record(minimum),
            "b18": record(b18),
            "coefficients": [
                {"index": list(index), "value": record(value)}
                for index, value in sorted(tensor_coefficients.items())
            ],
        },
        "failure_count": len(failures),
        "failures": failures,
    }


def compare_reference(payload: dict[str, object], reference_path: Path) -> dict[str, object]:
    """Post-hoc comparison; never used to produce any fresh quantity."""
    reference = json.loads(reference_path.read_text())
    finite_reference = {
        str(row["s"]): [parse_record(value) for value in row["coefficients"]]
        for row in reference["finite_bernstein_certificate"]["rows"]
    }
    finite_fresh = {
        s: [parse_record(value) for value in values]
        for s, values in payload["finite_bernstein"]["coefficients"].items()
    }
    finite_equal = finite_reference == finite_fresh

    tensor_reference = {
        tuple(row["index"]): parse_record(row["value"])
        for row in reference["asymptotic_bernstein_certificate"]["coefficients"]
    }
    tensor_fresh = {
        tuple(row["index"]): parse_record(row["value"])
        for row in payload["asymptotic_bernstein"]["coefficients"]
    }
    tensor_equal = tensor_reference == tensor_fresh

    reference_rows = {
        (row["s"], row["K"]): parse_record(row["actual_ratio"])
        for row in reference["rows"]
    }
    shared_rows = 0
    full_resolvent_equal = True
    for row in payload["finite_dag"]["rows"]:
        key = (row["context"][0], row["context"][1])
        if key in reference_rows:
            shared_rows += 1
            full_resolvent_equal &= parse_record(row["resolvent_ratio"]) == reference_rows[key]

    return {
        "reference": str(reference_path),
        "finite_coefficient_count": sum(len(values) for values in finite_fresh.values()),
        "finite_coefficients_exactly_equal": finite_equal,
        "tensor_coefficient_count": len(tensor_fresh),
        "tensor_coefficients_exactly_equal": tensor_equal,
        "shared_full_resolvent_rows": shared_rows,
        "shared_full_resolvents_exactly_equal": full_resolvent_equal,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference-json", type=Path)
    args = parser.parse_args()

    payload = fresh_audit()
    if args.reference_json is not None:
        payload["posthoc_reference_comparison"] = compare_reference(payload, args.reference_json)
        comparison = payload["posthoc_reference_comparison"]
        if not all(
            comparison[key]
            for key in (
                "finite_coefficients_exactly_equal",
                "tensor_coefficients_exactly_equal",
                "shared_full_resolvents_exactly_equal",
            )
        ):
            payload["failures"].append("post-hoc frozen-reference mismatch")
            payload["failure_count"] = len(payload["failures"])

    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    digest = hashlib.sha256(encoded.encode()).hexdigest()
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": digest,
                "failure_count": payload["failure_count"],
                "finite_dag_rows": payload["finite_dag"]["row_count"],
                "l1_rows": payload["l1_arbitrary_deficit"]["row_count"],
                "tensor_coefficients": payload["asymptotic_bernstein"]["coefficient_count"],
            },
            sort_keys=True,
        )
    )
    if payload["failure_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
