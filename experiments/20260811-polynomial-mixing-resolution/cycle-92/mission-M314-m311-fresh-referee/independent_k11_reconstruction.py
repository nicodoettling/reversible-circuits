#!/usr/bin/env python3
"""Independent exact reconstruction of M311's sole k=11 guard.

This standard-library program is deliberately self-contained: it does not
read M311, predecessor code, predecessor data, or any project module.  The
rank and the maximal Abel-sign grouping are fixed in source.  It emits every
row aggregate and block value so that the positive aggregate census is fully
auditable.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations
from math import factorial
from pathlib import Path


K = 11
N = 33
CUTS = range(1, K)
LAGS = range(2, N - 1)
MIDDLE_CLASSES = range(1, (K + 1) // 2)

LEFT_ARC = tuple(range(1, K))
RIGHT_ARC = tuple(range(2 * K, 3 * K))
EXTERIOR_CYCLE = LEFT_ARC + RIGHT_ARC
MINUS_CYCLE = tuple(range(K))
PLUS_CYCLE = RIGHT_ARC
MIDDLE_CYCLE = tuple(range(K, 2 * K))


@cache
def tree_density(size: int) -> Fraction:
    if size <= 0:
        return Fraction(0)
    if size == 1:
        return Fraction(1)
    return Fraction(size ** (size - 2), factorial(size - 1))


@cache
def chord_weight(size: int, cut: int) -> Fraction:
    assert 1 <= cut < size
    return tree_density(cut) * tree_density(size - cut) / (
        (size - 1) * tree_density(size)
    )


def unordered_pair(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def cyclic_separation(cycle: tuple[int, ...], pair: tuple[int, int]) -> int:
    where = {vertex: index for index, vertex in enumerate(cycle)}
    gap = abs(where[pair[0]] - where[pair[1]])
    return min(gap, len(cycle) - gap)


def normalized_chord_law(cycle: tuple[int, ...]) -> dict[tuple[int, int], Fraction]:
    law = {
        unordered_pair(a, b): chord_weight(
            len(cycle), cyclic_separation(cycle, unordered_pair(a, b))
        )
        for a, b in combinations(cycle, 2)
    }
    assert sum(law.values(), Fraction()) == 1
    return law


LAW_EXTERIOR = normalized_chord_law(EXTERIOR_CYCLE)
LAW_MINUS = normalized_chord_law(MINUS_CYCLE)
LAW_PLUS = normalized_chord_law(PLUS_CYCLE)
LAW_MIDDLE = normalized_chord_law(MIDDLE_CYCLE)


def signed_exterior_coefficients() -> dict[tuple[int, int], Fraction]:
    coefficient: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for pair, mass in LAW_EXTERIOR.items():
        coefficient[pair] += mass
    for law in (LAW_MINUS, LAW_PLUS):
        for pair, mass in law.items():
            coefficient[pair] -= mass / 2
    return {pair: mass for pair, mass in coefficient.items() if mass != 0}


GAMMA = signed_exterior_coefficients()


def middle_pair(phase: int, cut: int) -> tuple[int, int]:
    return unordered_pair(K + phase, K + ((phase + cut) % K))


def swap_map(first: tuple[int, int], second: tuple[int, int]) -> dict[int, int]:
    assert set(first).isdisjoint(second)
    return {
        first[0]: first[1],
        first[1]: first[0],
        second[0]: second[1],
        second[1]: second[0],
    }


def owner_geometry(
    exterior: tuple[int, int], middle: tuple[int, int]
) -> tuple[tuple[int | None, ...], tuple[int, ...]]:
    """Build q=D after the long cycle, then label its three cycles."""

    swap = swap_map(exterior, middle)
    permutation = tuple(swap.get((x + 1) % N, (x + 1) % N) for x in range(N))
    owner = [-1] * N
    cycle_sizes: list[int] = []
    for start in range(N):
        if owner[start] >= 0:
            continue
        orbit: list[int] = []
        point = start
        while owner[point] < 0 and point not in orbit:
            orbit.append(point)
            point = permutation[point]
        assert point == start
        owner_id = len(cycle_sizes)
        for point in orbit:
            owner[point] = owner_id
        cycle_sizes.append(len(orbit))
    assert len(cycle_sizes) == 3 and sum(cycle_sizes) == N

    generic_owner: list[int | None] = []
    for x in range(N):
        head = (x + 1) % N
        generic_owner.append(None if head in swap else owner[x])
    return tuple(generic_owner), tuple(cycle_sizes)


def owner_response_vector(
    exterior: tuple[int, int], middle: tuple[int, int]
) -> dict[int, Fraction]:
    generic_owner, sizes = owner_geometry(exterior, middle)
    one_point = tuple(tree_density(size - 1) / tree_density(size) for size in sizes)
    two_point = tuple(tree_density(size - 2) / tree_density(size) for size in sizes)
    output: dict[int, Fraction] = {}
    for lag in LAGS:
        literal = Fraction()
        repaired = Fraction()
        for x, first_owner in enumerate(generic_owner):
            second_owner = generic_owner[(x + lag) % N]
            if first_owner is None or second_owner is None:
                continue
            if first_owner == second_owner:
                literal += two_point[first_owner]
            else:
                literal += one_point[first_owner] * one_point[second_owner]

            repaired += one_point[first_owner] * one_point[second_owner]
            if first_owner == second_owner and sizes[first_owner] >= 3:
                repaired += two_point[first_owner] - one_point[first_owner] ** 2
        assert literal == repaired
        output[lag] = literal
    return output


def coefficient_geometry() -> dict[str, object]:
    positive_mass: dict[int, Fraction] = {}
    negative_mass: dict[int, Fraction] = {}
    increment: dict[int, Fraction] = {}
    cumulative_difference: dict[int, Fraction] = {}
    cross_edges: dict[int, tuple[tuple[int, int], ...]] = {}
    internal_edges: dict[int, tuple[tuple[int, int], ...]] = {}
    running = Fraction()
    left_vertices, right_vertices = set(LEFT_ARC), set(RIGHT_ARC)

    for cut in CUTS:
        cut_class = {
            pair
            for pair in LAW_EXTERIOR
            if cyclic_separation(EXTERIOR_CYCLE, pair) == cut
        }
        cross = tuple(
            sorted(
                pair
                for pair in cut_class
                if (pair[0] in left_vertices and pair[1] in right_vertices)
                or (pair[1] in left_vertices and pair[0] in right_vertices)
            )
        )
        internal = tuple(sorted(cut_class.difference(cross)))
        assert len(cut_class) == 2 * K - 1
        assert len(cross) == 2 * cut
        assert len(internal) == 2 * K - 1 - 2 * cut

        internal_coefficient = chord_weight(K, cut) / 2 - chord_weight(2 * K - 1, cut)
        x = 2 * cut * chord_weight(2 * K - 1, cut)
        y = len(internal) * internal_coefficient + chord_weight(K, cut) / 2
        assert internal_coefficient > 0 and x > 0 and y > 0

        running += x - y
        positive_mass[cut] = x
        negative_mass[cut] = y
        increment[cut] = x - y
        cumulative_difference[cut] = running
        cross_edges[cut] = cross
        internal_edges[cut] = internal

    assert running == 0
    total_mass = sum(positive_mass.values(), Fraction())
    assert total_mass == sum(negative_mass.values(), Fraction()) > 0

    a_left: dict[int, Fraction] = {}
    a_right: dict[int, Fraction] = {}
    b_left: dict[int, Fraction] = {}
    b_right: dict[int, Fraction] = {}
    a_cursor = b_cursor = Fraction()
    for cut in CUTS:
        a_left[cut], b_left[cut] = a_cursor, b_cursor
        a_cursor += positive_mass[cut]
        b_cursor += negative_mass[cut]
        a_right[cut], b_right[cut] = a_cursor, b_cursor
        assert a_cursor - b_cursor == cumulative_difference[cut]
    assert a_cursor == b_cursor == total_mass

    # Construct the staircase from consecutive mass endpoints, not by sorting
    # a precomputed cell dictionary.
    endpoints = sorted(
        {Fraction(), total_mass}
        | set(a_right.values())
        | set(b_right.values())
    )
    segments: list[dict[str, object]] = []
    for left, right in zip(endpoints, endpoints[1:]):
        assert left < right
        probe = (left + right) / 2
        c = next(cut for cut in CUTS if a_left[cut] < probe <= a_right[cut])
        d = next(cut for cut in CUTS if b_left[cut] < probe <= b_right[cut])
        segments.append({"c": c, "d": d, "left": left, "right": right, "mass": right - left})
    assert len(segments) <= 2 * (K - 1) - 1
    assert segments[0]["c"] == segments[0]["d"] == 1
    assert segments[-1]["c"] == segments[-1]["d"] == K - 1

    for previous, following in zip(segments, segments[1:]):
        assert int(following["c"]) >= int(previous["c"])
        assert int(following["d"]) >= int(previous["d"])

    transport = {
        (int(segment["c"]), int(segment["d"])): Fraction(segment["mass"])
        for segment in segments
    }
    assert len(transport) == len(segments)
    for cut in CUTS:
        assert sum(
            (mass for (c, _), mass in transport.items() if c == cut), Fraction()
        ) == positive_mass[cut]
        assert sum(
            (mass for (_, d), mass in transport.items() if d == cut), Fraction()
        ) == negative_mass[cut]

    for c, d in transport:
        rung = min(c, d)
        if c > d:
            assert cumulative_difference[rung] < 0
        elif c < d:
            assert cumulative_difference[rung] > 0

    runs: list[tuple[int, int, int]] = []
    start = 1
    current_sign = (cumulative_difference[1] > 0) - (cumulative_difference[1] < 0)
    for cut in range(2, K):
        cut_sign = (cumulative_difference[cut] > 0) - (cumulative_difference[cut] < 0)
        if cut_sign != current_sign:
            runs.append((start, cut - 1, current_sign))
            start, current_sign = cut, cut_sign
    runs.append((start, K - 1, current_sign))

    maximum_endpoint = {0: Fraction()}
    for cut in CUTS:
        maximum_endpoint[cut] = max(a_right[cut], b_right[cut])
    blocks: list[dict[str, object]] = []
    covered: list[tuple[int, int]] = []
    path = tuple(transport)
    for index, (a, b, run_sign) in enumerate(runs):
        cells = tuple(cell for cell in path if a <= min(cell) <= b)
        assert cells
        assert sum((transport[cell] for cell in cells), Fraction()) == (
            maximum_endpoint[b] - maximum_endpoint[a - 1]
        )
        blocks.append({"index": index, "a": a, "b": b, "sign": run_sign, "cells": cells})
        covered.extend(cells)
    assert tuple(covered) == path

    return {
        "positive_mass": positive_mass,
        "negative_mass": negative_mass,
        "increment": increment,
        "R": cumulative_difference,
        "cross": cross_edges,
        "internal": internal_edges,
        "total": total_mass,
        "transport": transport,
        "path": path,
        "blocks": blocks,
        "maximum_endpoint": maximum_endpoint,
    }


def exact(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> dict[str, object]:
    assert K == 11 and N == 3 * K
    assert len(tuple(LAGS)) == 30
    assert set(LAW_MIDDLE) == {
        middle_pair(phase, cut)
        for cut in MIDDLE_CLASSES
        for phase in range(K)
    }
    assert sum(
        K * chord_weight(K, cut) for cut in MIDDLE_CLASSES
    ) == 1
    assert sum(GAMMA.values(), Fraction()) == 0
    assert sum(value > 0 for value in GAMMA.values()) == 110
    assert sum(value < 0 for value in GAMMA.values()) == 110

    geometry = coefficient_geometry()
    positive_mass = geometry["positive_mass"]
    negative_mass = geometry["negative_mass"]
    transport = geometry["transport"]
    path = geometry["path"]
    blocks = geometry["blocks"]
    cross_edges = geometry["cross"]
    internal_edges = geometry["internal"]

    rows: list[dict[str, object]] = []
    aggregate: dict[tuple[int, int], Fraction] = {}
    x_means: dict[tuple[int, int, int], Fraction] = {}
    y_means: dict[tuple[int, int, int], Fraction] = {}
    block_values: dict[tuple[int, int, int], Fraction] = {}
    first_negative: dict[str, object] | None = None
    negative_blocks = 0
    rows_with_negative = 0

    for middle_cut in MIDDLE_CLASSES:
        middle_pairs = tuple(middle_pair(phase, middle_cut) for phase in range(K))
        assert len(set(middle_pairs)) == K

        # A differently organized response census: form all lag vectors for
        # one exterior/middle pair, then accumulate them by lag.
        response_sum = {
            lag: {exterior: Fraction() for exterior in GAMMA}
            for lag in LAGS
        }
        for exterior in GAMMA:
            for middle in middle_pairs:
                vector = owner_response_vector(exterior, middle)
                for lag in LAGS:
                    response_sum[lag][exterior] += vector[lag]

        for lag in LAGS:
            g = response_sum[lag]
            xb: dict[int, Fraction] = {}
            yb: dict[int, Fraction] = {}
            for cut in CUTS:
                xb[cut] = sum((g[pair] for pair in cross_edges[cut]), Fraction()) / (2 * cut)
                internal_coefficient = chord_weight(K, cut) / 2 - chord_weight(2 * K - 1, cut)
                seam = unordered_pair(0, cut)
                yb[cut] = (
                    internal_coefficient
                    * sum((g[pair] for pair in internal_edges[cut]), Fraction())
                    + chord_weight(K, cut) * g[seam] / 2
                ) / negative_mass[cut]
                x_means[(middle_cut, lag, cut)] = xb[cut]
                y_means[(middle_cut, lag, cut)] = yb[cut]

            differences = {(c, d): xb[c] - yb[d] for c, d in path}
            direct = sum((coefficient * g[pair] for pair, coefficient in GAMMA.items()), Fraction())
            cut_sum = sum(
                (
                    positive_mass[cut] * xb[cut]
                    - negative_mass[cut] * yb[cut]
                    for cut in CUTS
                ),
                Fraction(),
            )
            transport_sum = sum(
                (transport[cell] * differences[cell] for cell in path), Fraction()
            )
            assert direct == cut_sum == transport_sum

            row_blocks: list[dict[str, object]] = []
            row_negative = False
            for block in blocks:
                index = int(block["index"])
                cells = tuple(block["cells"])
                value = sum(
                    (transport[cell] * differences[cell] for cell in cells), Fraction()
                )
                block_values[(middle_cut, lag, index)] = value
                terms = [
                    {
                        "c": c,
                        "d": d,
                        "pi": exact(transport[(c, d)]),
                        "difference": exact(differences[(c, d)]),
                        "weighted_contribution": exact(
                            transport[(c, d)] * differences[(c, d)]
                        ),
                    }
                    for c, d in cells
                ]
                if value < 0:
                    negative_blocks += 1
                    row_negative = True
                    if first_negative is None:
                        first_negative = {
                            "u": middle_cut,
                            "ell": lag,
                            "block_index": index,
                            "a": block["a"],
                            "b": block["b"],
                            "sign": block["sign"],
                            "value": exact(value),
                            "value_float": float(value),
                            "cell_terms": terms,
                        }
                row_blocks.append(
                    {
                        "block_index": index,
                        "value": exact(value),
                        "value_float": float(value),
                    }
                )
            assert sum(
                (block_values[(middle_cut, lag, int(block["index"]))] for block in blocks),
                Fraction(),
            ) == direct

            if row_negative:
                rows_with_negative += 1
            aggregate[(middle_cut, lag)] = direct
            rows.append(
                {
                    "u": middle_cut,
                    "ell": lag,
                    "blocks": row_blocks,
                    "has_negative_block": row_negative,
                    "aggregate": exact(direct),
                    "aggregate_float": float(direct),
                }
            )

    reflection_pairs = 0
    for middle_cut in MIDDLE_CLASSES:
        for lag in range(2, (N + 1) // 2):
            reflected = N - lag
            assert aggregate[(middle_cut, lag)] == aggregate[(middle_cut, reflected)]
            for cut in CUTS:
                assert x_means[(middle_cut, lag, cut)] == x_means[(middle_cut, reflected, cut)]
                assert y_means[(middle_cut, lag, cut)] == y_means[(middle_cut, reflected, cut)]
            for block in blocks:
                index = int(block["index"])
                assert block_values[(middle_cut, lag, index)] == block_values[(middle_cut, reflected, index)]
            reflection_pairs += 1

    assert first_negative is not None
    minimum = min(aggregate.values())
    return {
        "scope": {
            "k": K,
            "n": N,
            "new_ranks": [K],
            "middle_classes": list(MIDDLE_CLASSES),
            "middle_phases_per_class": K,
            "lags": list(LAGS),
            "alternate_groupings_or_searches": False,
            "reads_project_or_predecessor_code_or_data": False,
        },
        "geometry": {
            "support_cells": len(path),
            "path": [
                {"c": c, "d": d, "pi": exact(transport[(c, d)]), "rung": min(c, d)}
                for c, d in path
            ],
            "R_signs": {
                str(cut): (geometry["R"][cut] > 0) - (geometry["R"][cut] < 0)
                for cut in CUTS
            },
            "blocks": [
                {
                    "block_index": block["index"],
                    "a": block["a"],
                    "b": block["b"],
                    "sign": block["sign"],
                    "cells": [{"c": c, "d": d} for c, d in block["cells"]],
                }
                for block in blocks
            ],
        },
        "qbp": {
            "block_instances": len(block_values),
            "negative_blocks": negative_blocks,
            "rows_with_negative_block": rows_with_negative,
            "first_lexicographic_failure": first_negative,
        },
        "aggregates": {
            "tested": len(aggregate),
            "positive": sum(value > 0 for value in aggregate.values()),
            "zero": sum(value == 0 for value in aggregate.values()),
            "negative": sum(value < 0 for value in aggregate.values()),
            "minimum": exact(minimum),
            "minimum_float": float(minimum),
            "minimum_locations": [
                {"u": u, "ell": lag}
                for (u, lag), value in sorted(aggregate.items())
                if value == minimum
            ],
            "reflection_pairs": reflection_pairs,
            "rows": rows,
        },
        "exact_assertions": {
            "marginals": True,
            "staircase_and_rungs": True,
            "qti": True,
            "qbd": True,
            "reflection": True,
        },
        "downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    arguments.output.write_text(json.dumps(main(), indent=2, sort_keys=True) + "\n")
