#!/usr/bin/env python3
"""Standalone exact regeneration of the corrected auxiliary L=5 certificates.

The exceptional ordinary-baseline subtraction is source_mass*lambda, never
source_mass*lambda**2.  No predecessor source is imported.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


def record(x: F) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


@functools.lru_cache(None)
def weight(n: int) -> F:
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
        (F(p * falling(a, p), math.factorial(p + degree - 1) * a**p) for p in range(1, a + 1)),
        F(0),
    )


@functools.lru_cache(None)
def coefficient_c(s: int) -> F:
    return sum(
        (
            weight(a) * forest(s - a, degree - 1)
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


def support(excess: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    q = split(ratios)
    rows = []
    for h in range(excess + 1):
        bottom_product = math.prod(ratios[-h:]) if h else F(1)
        child_q = weight(h) * bottom_product if h else None
        for prefix in compositions(excess - h):
            degree = len(prefix) + 1
            mass = math.prod(weight(x) for x in prefix) / (
                math.factorial(degree) * weight(excess + 1) * bottom_product
            )
            mean = (
                degree * attachment(a, deficit, degree - 1, 0, z)
                if h == 0
                else child_q * (1 - attachment(a, deficit, degree, 0, z))
            )
            rows.append((h, prefix, mass, mean))
    assert len(rows) == 2**excess
    assert sum((mass * mean for _, _, mass, mean in rows), F(0)) == 1
    return tuple(rows), q


def in_basin(source: tuple[int, ...], endpoint: tuple[int, ...]) -> bool:
    return any(
        sum(source[:cut]) == endpoint[0] and source[cut:] == endpoint[1:]
        for cut in range(1, len(source) + 1)
    )


def endpoint_cuts(prefix: tuple[int, ...]):
    return tuple((sum(prefix[:cut]),) + prefix[cut:] for cut in range(1, len(prefix) + 1))


def exceptional(excess: int, ratios: tuple[F, ...], z: F, a: int, deficit: int):
    rows, q = support(excess, ratios, z, a, deficit)
    keyed = {(h, prefix): (mass, mean) for h, prefix, mass, mean in rows}
    endpoints = sorted(
        {(h, endpoint) for h, prefix, _, _ in rows for endpoint in endpoint_cuts(prefix)},
        key=lambda item: (item[0], len(item[1]), item[1]),
    )
    data = []
    for h, endpoint in endpoints:
        sources = tuple(
            (prefix, mass, mean)
            for hh, prefix, mass, mean in rows
            if hh == h and in_basin(prefix, endpoint)
        )
        theta = sum((mass * (mean - q) for _, mass, mean in sources), F(0))
        capacity = (len(endpoint) + 1) * keyed[(h, endpoint)][0]
        source_mass = sum((mass for _, mass, _ in sources), F(0))
        data.append((h, endpoint, theta, capacity, source_mass))
    return rows, q, tuple(data)


def coarse_reset(excess: int, ratios: tuple[F, ...], z: F, a: int, deficit: int, height: F) -> F:
    rows, q, data = exceptional(excess, ratios, z, a, deficit)
    occurrence_mass = sum((mass * len(prefix) for _, prefix, mass, _ in rows), F(0))
    return q * (height - q * occurrence_mass) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _ in data), F(0)
    )


def corrected_reset(ratios: tuple[F, ...], z: F, ordinary: F) -> tuple[F, int]:
    _, q, data = exceptional(5, ratios, z, 0, 1)
    assert len(data) == 31
    # This is the corrected one-power subtraction a_E*lambda_E.
    subtraction = sum(
        (source_mass * lam(endpoint[0], len(endpoint) + 1) for _, endpoint, _, _, source_mass in data),
        F(0),
    )
    reset = q * (ordinary - q * subtraction) + sum(
        (theta * theta / capacity for _, _, theta, capacity, _ in data), F(0)
    )
    return reset, len(data)


def group_mass(rows, h: int, degree: int) -> F:
    return sum((mass for hh, prefix, mass, _ in rows if hh == h and len(prefix) + 1 == degree), F(0))


def arbitrary_envelope(
    excess: int,
    ratios: tuple[F, ...],
    z: F,
    a: int,
    deficit: int,
    heights: dict[int, F],
) -> F:
    q = split(ratios)
    if excess == 0:
        return 1 - q
    assert excess <= 3
    rows, q2 = support(excess, ratios, z, a, deficit)
    assert q2 == q
    value = coarse_reset(excess, ratios, z, a, deficit, heights[excess])
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
                        heights,
                    )
                )
                value += mass * attachment(a, deficit, degree, j, z) * child
    return value


def l5_envelope(ratios: tuple[F, ...], z: F, heights: dict[int, F], ordinary: F):
    rows, q = support(5, ratios, z, 0, 1)
    reset, basin_count = corrected_reset(ratios, z, ordinary)
    value = reset
    live_count = 0
    rank_count = 0
    for h in range(1, 6):
        for degree in range(1, 7 - h):
            mass = group_mass(rows, h, degree)
            if not mass:
                continue
            live_count += 1
            child_ratios = ratios[-h:]
            child_q = split(child_ratios)
            for j in range(1, degree + 1):
                rank_count += 1
                child_excess = h - 1
                child_deficit = degree + 1 - j
                child = child_q * (
                    1 - child_q
                    if child_deficit == 1
                    else arbitrary_envelope(
                        child_excess,
                        child_ratios,
                        z,
                        degree,
                        child_deficit,
                        heights,
                    )
                )
                value += mass * attachment(0, 1, degree, j, z) * child
    assert live_count == 11 and rank_count == 31
    return value, q, basin_count


def actual_parameters(s: int):
    ratios = tuple(weight(s - i) / weight(s - i + 1) for i in range(6))
    bottom = s - 5
    heights = {ell: F(bottom + ell - 1, bottom + ell + 1) for ell in range(1, 6)}
    return ratios, heights


def cleared(ratios: tuple[F, ...], z: F, heights: dict[int, F], ordinary: F) -> F:
    envelope, q, _ = l5_envelope(ratios, z, heights, ordinary)
    return math.prod(1 + a * z for a in range(1, 6)) ** 2 * (1 - q - envelope)


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
        matrix.append([
            F(math.comb(degree, i)) * t**i * (1 - t) ** (degree - i)
            for i in range(degree + 1)
        ])
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
            output[index(i)] = sum((inverse[i][j] * samples[j] for j in range(degrees[axis] + 1)), F(0))
    return output


def tensor_bernstein(values: dict[tuple[int, ...], F], degrees: tuple[int, ...]):
    result = values
    for axis in range(len(degrees)):
        result = transform_axis(result, degrees, axis)
    return result


def bernstein_eval(coefficients, degrees, point) -> F:
    answer = F(0)
    for index, coefficient in coefficients.items():
        basis = F(1)
        for degree, i, t in zip(degrees, index, point):
            basis *= math.comb(degree, i) * t**i * (1 - t) ** (degree - i)
        answer += coefficient * basis
    return answer


def finite_difference_degree(values: list[F]) -> int:
    row = values[:]
    for degree in range(len(values) - 1):
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if all(x == 0 for x in row):
            return degree
    return len(values) - 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference-json", type=Path)
    args = parser.parse_args()
    failures = []

    finite_rows = []
    finite_all = []
    finite_indexed = []
    inverse12 = bernstein_inverse(12)
    for s in range(6, 100):
        ratios, heights = actual_parameters(s)
        ordinary = coefficient_c(s)
        samples = [cleared(ratios, F(j, 24), heights, ordinary) for j in range(13)]
        coefficients = [
            sum((inverse12[i][j] * samples[j] for j in range(13)), F(0))
            for i in range(13)
        ]
        direct = cleared(ratios, F(7, 38), heights, ordinary)
        t = F(7, 19)
        interpolated = sum(
            (coefficients[i] * math.comb(12, i) * t**i * (1 - t) ** (12 - i) for i in range(13)),
            F(0),
        )
        if direct != interpolated:
            failures.append({"kind": "finite-off-grid", "s": s})
        finite_all.extend(coefficients)
        finite_indexed.extend((x, s, i) for i, x in enumerate(coefficients))
        finite_rows.append({"s": s, "coefficients": [record(x) for x in coefficients]})
    finite_nonpositive = sum(x <= 0 for x in finite_all)
    finite_minimum, finite_minimum_s, finite_minimum_index = min(finite_indexed)
    if finite_nonpositive:
        failures.append({"kind": "finite-nonpositive", "count": finite_nonpositive})

    generic = (F(7, 20), F(9, 25), F(11, 30), F(3, 8), F(19, 50), F(23, 60))
    unit_heights = {ell: F(1) for ell in range(1, 6)}
    z_degree = finite_difference_degree([
        cleared(generic, F(j, 17), unit_heights, F(3, 4)) for j in range(15)
    ])
    ratio_degrees = []
    for axis in range(6):
        samples = []
        for j in range(4):
            point = list(generic)
            point[axis] += F(j, 100)
            samples.append(cleared(tuple(point), F(2, 7), unit_heights, F(3, 4)))
        ratio_degrees.append(finite_difference_degree(samples))
    degrees = tuple(ratio_degrees) + (z_degree,)
    if degrees != (1, 1, 2, 2, 2, 2, 12):
        failures.append({"kind": "degree", "degrees": list(degrees)})

    lo, hi = F(4, 11), F(187, 500)
    b95 = weight(95) / weight(96)
    e_upper = F(31967, 11760)
    assert b95 == F(95**94, 96**94) < hi
    assert e_upper < F(87, 32) < F(11, 4)  # Hence 1/e>4/11.
    grid = {}
    for index in itertools.product(*(range(d + 1) for d in degrees)):
        unit = tuple(F(i, d) if d else F(0) for i, d in zip(index, degrees))
        ratios = tuple(lo + (hi - lo) * unit[i] for i in range(6))
        grid[index] = cleared(ratios, unit[6] / 2, unit_heights, F(3, 4))
    tail = tensor_bernstein(grid, degrees)
    tail_nonpositive = sum(x <= 0 for x in tail.values())
    tail_min_index, tail_minimum = min(tail.items(), key=lambda item: item[1])
    if tail_nonpositive:
        failures.append({"kind": "tail-nonpositive", "count": tail_nonpositive})
    off_unit = (F(1, 7), F(2, 7), F(3, 7), F(4, 7), F(5, 7), F(6, 7), F(7, 11))
    off_ratios = tuple(lo + (hi - lo) * off_unit[i] for i in range(6))
    if bernstein_eval(tail, degrees, off_unit) != cleared(off_ratios, off_unit[6] / 2, unit_heights, F(3, 4)):
        failures.append({"kind": "tail-off-grid"})

    finite_digest_source = "\n".join(f"{x.numerator}/{x.denominator}" for x in finite_all) + "\n"
    tail_digest_source = "\n".join(
        f"{','.join(map(str, index))}:{x.numerator}/{x.denominator}"
        for index, x in sorted(tail.items())
    ) + "\n"

    # Fresh construction is complete before this optional immutable artifact
    # is opened.  The comparison is provenance only, not a proof input.
    comparison = None
    if args.reference_json:
        reference = json.loads(args.reference_json.read_text())
        reference_finite = [
            item
            for row in reference["finite_certificate"]["rows"]
            for item in row["coefficients"]
        ]
        reference_tail = reference["tail_certificate"]["coefficients"]
        fresh_finite = [item for row in finite_rows for item in row["coefficients"]]
        finite_equal = fresh_finite == reference_finite
        tail_equal = all(
            fresh["index"] == old["index"]
            and fresh["value"]["numerator"] == old["value"]["numerator"]
            and fresh["value"]["denominator"] == old["value"]["denominator"]
            for fresh, old in zip(
                [{"index": list(index), "value": record(x)} for index, x in sorted(tail.items())],
                reference_tail,
            )
        ) and len(tail) == len(reference_tail)
        comparison = {
            "reference": str(args.reference_json),
            "finite_count": len(fresh_finite),
            "finite_all_equal": finite_equal,
            "tail_count": len(tail),
            "tail_all_equal": tail_equal,
        }
        if not finite_equal or not tail_equal:
            failures.append({"kind": "posthoc-reference-mismatch", "comparison": comparison})
    payload = {
        "claim": "corrected one-power auxiliary L=5 Bernstein certificates",
        "scope": "full nonlazy stationary-flow parking-degree reset recurrence only",
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "exceptional_subtraction": "source_mass*lambda (equivalently a_E*lambda_E after restoring q); lambda^2 is rejected and unused",
        "structure": {
            "supported_roots": 32,
            "exceptional_occurrences": 31,
            "live_groups": 11,
            "nominal_positive_attachment_ranks": 31,
            "s6_actual_retained_children": 17,
        },
        "ratio_box": {
            "lower": record(lo),
            "upper": record(hi),
            "b95": record(b95),
            "e_upper": record(e_upper),
            "proof": "b_n decreases, b_n>1/e>4/11, and exact b_95<187/500",
        },
        "finite": {
            "range": "s=6,...,99; z in [0,1/2]",
            "count": len(finite_all),
            "nonpositive": finite_nonpositive,
            "minimum": record(finite_minimum),
            "minimum_s": finite_minimum_s,
            "minimum_index": finite_minimum_index,
            "coefficient_sha256": hashlib.sha256(finite_digest_source.encode()).hexdigest(),
            "row_minima": [
                {
                    "s": row["s"],
                    "minimum": min(row["coefficients"], key=lambda x: F(int(x["numerator"]), int(x["denominator"]))),
                }
                for row in finite_rows
            ],
            "s6_coefficients": finite_rows[0]["coefficients"],
        },
        "tail": {
            "range": "six ratios in [4/11,187/500], z in [0,1/2], heights=1, ordinary coefficient=3/4",
            "degrees": list(degrees),
            "count": len(tail),
            "nonpositive": tail_nonpositive,
            "minimum_index": list(tail_min_index),
            "minimum": record(tail_minimum),
            "coefficient_sha256": hashlib.sha256(tail_digest_source.encode()).hexdigest(),
            "minimum_row": {"index": list(tail_min_index), "value": record(tail_minimum)},
        },
        "posthoc_comparison": comparison,
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "failure_count": len(failures),
        "finite_count": len(finite_all),
        "finite_nonpositive": finite_nonpositive,
        "finite_minimum": record(finite_minimum),
        "tail_count": len(tail),
        "tail_nonpositive": tail_nonpositive,
        "tail_minimum": record(tail_minimum),
        "tail_minimum_index": list(tail_min_index),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
