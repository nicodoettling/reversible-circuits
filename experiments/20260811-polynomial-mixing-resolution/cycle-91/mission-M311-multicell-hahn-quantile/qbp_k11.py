#!/usr/bin/env python3
"""Exact sole-rank guard for M311's pre-frozen QBP_1.

Standard library only.  This script fixes k=11, imports no project or
predecessor code/data, retains every middle phase and supported transport
cell, and tests no alternate grouping.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path


K = 11
N = 3 * K
D = 2 * K - 1
M_MAX = K - 1
LAGS = tuple(range(2, N - 1))
A = tuple(range(1, K))
P = tuple(range(2 * K, 3 * K))
L = A + P
MIDDLE_VERTICES = tuple(range(K, 2 * K))
C_MINUS = tuple(range(0, K))
C_PLUS = P


@lru_cache(maxsize=None)
def tau(d: int) -> Fraction:
    if d == 1:
        return Fraction(1)
    if d <= 0:
        return Fraction(0)
    return Fraction(d ** (d - 2), factorial(d - 1))


@lru_cache(maxsize=None)
def v(d: int, c: int) -> Fraction:
    assert 1 <= c <= d - 1
    return tau(c) * tau(d - c) / ((d - 1) * tau(d))


@lru_cache(maxsize=None)
def alpha(d: int) -> Fraction:
    return tau(d - 1) / tau(d)


@lru_cache(maxsize=None)
def beta(d: int) -> Fraction:
    return tau(d - 2) / tau(d)


def edge(a: int, b: int) -> tuple[int, int]:
    assert a != b
    return (a, b) if a < b else (b, a)


def cycle_cut(cycle: tuple[int, ...], e: tuple[int, int]) -> int:
    pos = {x: i for i, x in enumerate(cycle)}
    delta = abs(pos[e[0]] - pos[e[1]])
    return min(delta, len(cycle) - delta)


def chord_law(cycle: tuple[int, ...]) -> dict[tuple[int, int], Fraction]:
    law: dict[tuple[int, int], Fraction] = {}
    for a, b in combinations(cycle, 2):
        e = edge(a, b)
        law[e] = v(len(cycle), cycle_cut(cycle, e))
    assert sum(law.values(), Fraction(0)) == 1
    return law


LAW_L = chord_law(L)
LAW_M = chord_law(MIDDLE_VERTICES)
LAW_MINUS = chord_law(C_MINUS)
LAW_PLUS = chord_law(C_PLUS)


def signed_exterior_law() -> dict[tuple[int, int], Fraction]:
    out: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for e, mass in LAW_L.items():
        out[e] += mass
    for law in (LAW_MINUS, LAW_PLUS):
        for e, mass in law.items():
            out[e] -= mass / 2
    return {e: mass for e, mass in out.items() if mass}


GAMMA = signed_exterior_law()


def apply_double(x: int, e: tuple[int, int], f: tuple[int, int]) -> int:
    for a, b in (e, f):
        if x == a:
            return b
        if x == b:
            return a
    return x


@lru_cache(maxsize=None)
def owner_data(
    e: tuple[int, int], f: tuple[int, int]
) -> tuple[tuple[int | None, ...], tuple[int, ...]]:
    assert not (set(e) & set(f))
    q = tuple(apply_double((x + 1) % N, e, f) for x in range(N))
    seen = [False] * N
    owner = [-1] * N
    sizes: list[int] = []
    for start in range(N):
        if seen[start]:
            continue
        x = start
        size = 0
        while not seen[x]:
            seen[x] = True
            owner[x] = len(sizes)
            size += 1
            x = q[x]
        assert x == start
        sizes.append(size)
    assert len(sizes) == 3 and sum(sizes) == N
    generic: list[int | None] = []
    for x in range(N):
        head = (x + 1) % N
        generic.append(owner[x] if apply_double(head, e, f) == head else None)
    return tuple(generic), tuple(sizes)


def response(e: tuple[int, int], f: tuple[int, int], ell: int) -> Fraction:
    generic, sizes = owner_data(e, f)
    a = tuple(alpha(d) for d in sizes)
    b = tuple(beta(d) for d in sizes)
    literal = Fraction(0)
    repaired = Fraction(0)
    for x, i in enumerate(generic):
        j = generic[(x + ell) % N]
        if i is None or j is None:
            continue
        literal += b[i] if i == j else a[i] * a[j]
        repaired += a[i] * a[j]
        if i == j and sizes[i] >= 3:
            repaired += b[i] - a[i] ** 2
    assert literal == repaired
    return literal


def middle_edge(a: int, u: int) -> tuple[int, int]:
    return edge(K + a, K + ((a + u) % K))


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def record(x: Fraction) -> dict[str, object]:
    return {"exact": qstr(x), "float": float(x)}


def sign(x: Fraction) -> int:
    return -1 if x < 0 else 1 if x > 0 else 0


def transport_data():
    cut_edges: dict[int, tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]] = {}
    x_mass: dict[int, Fraction] = {}
    y_mass: dict[int, Fraction] = {}
    r_mass: dict[int, Fraction] = {}
    R_mass: dict[int, Fraction] = {}
    a_set, p_set = set(A), set(P)
    running = Fraction(0)
    for c in range(1, K):
        all_c = {e for e in LAW_L if cycle_cut(L, e) == c}
        cross = {
            e
            for e in all_c
            if (
                (e[0] in a_set and e[1] in p_set)
                or (e[1] in a_set and e[0] in p_set)
            )
        }
        internal = all_c - cross
        assert len(all_c) == D and len(cross) == 2 * c
        assert len(internal) == D - 2 * c
        cut_edges[c] = (tuple(sorted(cross)), tuple(sorted(internal)))
        q = v(K, c) / 2 - v(D, c)
        x = 2 * c * v(D, c)
        y = (D - 2 * c) * q + v(K, c) / 2
        assert q > 0 and x > 0 and y > 0
        r = x - y
        running += r
        x_mass[c], y_mass[c], r_mass[c], R_mass[c] = x, y, r, running
    assert running == 0
    mu = sum(x_mass.values(), Fraction(0))
    assert mu == sum(y_mass.values(), Fraction(0)) > 0

    A_left: dict[int, Fraction] = {}
    A_right: dict[int, Fraction] = {}
    B_left: dict[int, Fraction] = {}
    B_right: dict[int, Fraction] = {}
    running_x = running_y = Fraction(0)
    for c in range(1, K):
        A_left[c], B_left[c] = running_x, running_y
        running_x += x_mass[c]
        running_y += y_mass[c]
        A_right[c], B_right[c] = running_x, running_y
        assert R_mass[c] == running_x - running_y
    assert running_x == running_y == mu

    pi: dict[tuple[int, int], Fraction] = {}
    for c in range(1, K):
        for d in range(1, K):
            overlap = min(A_right[c], B_right[d]) - max(A_left[c], B_left[d])
            if overlap > 0:
                pi[(c, d)] = overlap
    for c in range(1, K):
        assert sum((mass for (i, _), mass in pi.items() if i == c), Fraction(0)) == x_mass[c]
    for d in range(1, K):
        assert sum((mass for (_, j), mass in pi.items() if j == d), Fraction(0)) == y_mass[d]
    assert sum(pi.values(), Fraction(0)) == mu

    path = tuple(sorted(pi))
    assert path[0] == (1, 1) and path[-1] == (M_MAX, M_MAX)
    assert len(path) <= 2 * M_MAX - 1
    for (c0, d0), (c1, d1) in zip(path, path[1:]):
        assert c1 >= c0 and d1 >= d0 and (c1, d1) != (c0, d0)
    for c, d in path:
        h = min(c, d)
        if c > d:
            assert R_mass[h] < 0
        elif c < d:
            assert R_mass[h] > 0
        else:
            assert c == d

    runs: list[tuple[int, int, int]] = []
    start = 1
    current_sign = sign(R_mass[1])
    for h in range(2, K):
        next_sign = sign(R_mass[h])
        if next_sign != current_sign:
            runs.append((start, h - 1, current_sign))
            start = h
            current_sign = next_sign
    runs.append((start, M_MAX, current_sign))

    M_endpoint = {0: Fraction(0)}
    for h in range(1, K):
        M_endpoint[h] = max(A_right[h], B_right[h])
        if R_mass[h] < 0:
            assert M_endpoint[h] == B_right[h]
        elif R_mass[h] > 0:
            assert M_endpoint[h] == A_right[h]
        else:
            assert A_right[h] == B_right[h] == M_endpoint[h]

    blocks: list[dict[str, object]] = []
    covered: set[tuple[int, int]] = set()
    path_positions = {cell: i for i, cell in enumerate(path)}
    for block_index, (a, b, block_sign) in enumerate(runs):
        cells = tuple(cell for cell in path if a <= min(cell) <= b)
        assert cells
        assert not (covered & set(cells))
        covered.update(cells)
        positions = [path_positions[cell] for cell in cells]
        assert positions == list(range(positions[0], positions[-1] + 1))
        block_mass = sum((pi[cell] for cell in cells), Fraction(0))
        assert block_mass == M_endpoint[b] - M_endpoint[a - 1] > 0
        blocks.append(
            {
                "block_index": block_index,
                "a": a,
                "b": b,
                "sign": block_sign,
                "cells": cells,
                "mass": block_mass,
            }
        )
    assert covered == set(path)
    assert sum((block["mass"] for block in blocks), Fraction(0)) == mu
    return (
        cut_edges,
        x_mass,
        y_mass,
        r_mass,
        R_mass,
        mu,
        pi,
        path,
        blocks,
        M_endpoint,
    )


def main() -> dict[str, object]:
    assert len(LAGS) == 30
    assert set(LAW_M) == {
        middle_edge(a, u)
        for u in range(1, (K + 1) // 2)
        for a in range(K)
    }
    assert sum(K * v(K, u) for u in range(1, (K + 1) // 2)) == 1
    assert sum(GAMMA.values(), Fraction(0)) == 0
    assert sum(g > 0 for g in GAMMA.values()) == K * (K - 1)
    assert sum(g < 0 for g in GAMMA.values()) == K * (K - 1)

    (
        cut_edges,
        x_mass,
        y_mass,
        r_mass,
        R_mass,
        mu,
        pi,
        path,
        blocks,
        M_endpoint,
    ) = transport_data()

    rows: list[dict[str, object]] = []
    first_negative_block = None
    minimum_block = None
    negative_blocks = 0
    rows_with_negative_block = 0
    block_values: dict[tuple[int, int, int], Fraction] = {}
    mclp_values: dict[tuple[int, int], Fraction] = {}
    x_means: dict[tuple[int, int, int], Fraction] = {}
    y_means: dict[tuple[int, int, int], Fraction] = {}

    for u in range(1, (K + 1) // 2):
        middle = tuple(middle_edge(a, u) for a in range(K))
        assert len(set(middle)) == K
        for ell in LAGS:
            g = {
                e: sum((response(e, f, ell) for f in middle), Fraction(0))
                for e in GAMMA
            }
            xb: dict[int, Fraction] = {}
            yb: dict[int, Fraction] = {}
            for c in range(1, K):
                cross, internal = cut_edges[c]
                q = v(K, c) / 2 - v(D, c)
                xb[c] = sum((g[e] for e in cross), Fraction(0)) / (2 * c)
                yb[c] = (
                    q * sum((g[e] for e in internal), Fraction(0))
                    + v(K, c) * g[edge(0, c)] / 2
                ) / y_mass[c]
                x_means[(u, ell, c)] = xb[c]
                y_means[(u, ell, c)] = yb[c]

            differences = {(c, d): xb[c] - yb[d] for c, d in path}
            direct = sum((mass * g[e] for e, mass in GAMMA.items()), Fraction(0))
            transported = sum((pi[cell] * differences[cell] for cell in path), Fraction(0))
            cut_form = sum(
                (x_mass[c] * xb[c] - y_mass[c] * yb[c] for c in range(1, K)),
                Fraction(0),
            )
            assert direct == transported == cut_form
            mclp_values[(u, ell)] = direct

            row_blocks: list[dict[str, object]] = []
            row_has_negative = False
            for block in blocks:
                block_index = int(block["block_index"])
                cells = block["cells"]
                value = sum((pi[cell] * differences[cell] for cell in cells), Fraction(0))
                block_values[(u, ell, block_index)] = value
                witness = {
                    "u": u,
                    "ell": ell,
                    "block_index": block_index,
                    "a": block["a"],
                    "b": block["b"],
                    "sign": block["sign"],
                    "value": qstr(value),
                    "value_float": float(value),
                    "cell_terms": [
                        {
                            "c": c,
                            "d": d,
                            "pi": qstr(pi[(c, d)]),
                            "difference": qstr(differences[(c, d)]),
                            "weighted_contribution": qstr(pi[(c, d)] * differences[(c, d)]),
                        }
                        for c, d in cells
                    ],
                }
                if value < 0:
                    negative_blocks += 1
                    row_has_negative = True
                    if first_negative_block is None:
                        first_negative_block = witness
                if minimum_block is None or value < minimum_block[0]:
                    minimum_block = (value, witness)
                row_blocks.append(
                    {
                        "block_index": block_index,
                        "value": qstr(value),
                        "value_float": float(value),
                    }
                )
            assert sum((block_values[(u, ell, int(block["block_index"]))] for block in blocks), Fraction(0)) == direct

            prefix = Fraction(0)
            for block in blocks:
                block_index = int(block["block_index"])
                prefix += block_values[(u, ell, block_index)]
                b = int(block["b"])
                direct_prefix = sum(
                    (pi[cell] * differences[cell] for cell in path if min(cell) <= b),
                    Fraction(0),
                )
                assert prefix == direct_prefix

            if row_has_negative:
                rows_with_negative_block += 1
            rows.append(
                {
                    "u": u,
                    "ell": ell,
                    "blocks": row_blocks,
                    "has_negative_block": row_has_negative,
                    "mclp_value": qstr(direct),
                    "mclp_value_float": float(direct),
                }
            )

    for u in range(1, (K + 1) // 2):
        for ell in LAGS:
            reflected = N - ell
            assert mclp_values[(u, ell)] == mclp_values[(u, reflected)]
            for c in range(1, K):
                assert x_means[(u, ell, c)] == x_means[(u, reflected, c)]
                assert y_means[(u, ell, c)] == y_means[(u, reflected, c)]
            for block in blocks:
                block_index = int(block["block_index"])
                assert block_values[(u, ell, block_index)] == block_values[(u, reflected, block_index)]

    assert minimum_block is not None
    mclp_minimum = min(mclp_values.values())
    return {
        "status": "exact sole-rank test of pre-frozen QBP_1; all-rank MCLP_1 remains separate",
        "scope": {
            "k": K,
            "n": N,
            "middle_cut_classes": list(range(1, (K + 1) // 2)),
            "middle_phases_per_class": K,
            "admissible_lags": list(LAGS),
            "new_ranks": [K],
            "imports_project_or_predecessor_code_or_data": False,
            "alternate_groupings_tested": False,
        },
        "normalization": {
            "gamma_mass": qstr(sum(GAMMA.values(), Fraction(0))),
            "positive_exterior_atoms": sum(g > 0 for g in GAMMA.values()),
            "negative_exterior_atoms": sum(g < 0 for g in GAMMA.values()),
            "positive_cut_mass": qstr(mu),
            "negative_cut_mass": qstr(sum(y_mass.values(), Fraction(0))),
            "transport_mass": qstr(sum(pi.values(), Fraction(0))),
            "transport_support_cells": len(pi),
        },
        "abel_coefficients": {
            "r": {str(c): qstr(r_mass[c]) for c in range(1, K)},
            "R": {str(c): qstr(R_mass[c]) for c in range(1, K)},
            "R_signs": {str(c): sign(R_mass[c]) for c in range(1, K)},
            "M": {str(c): qstr(M_endpoint[c]) for c in range(0, K)},
        },
        "transport_path": [
            {"c": c, "d": d, "pi": qstr(pi[(c, d)]), "rung": min(c, d)}
            for c, d in path
        ],
        "blocks": [
            {
                "block_index": block["block_index"],
                "a": block["a"],
                "b": block["b"],
                "sign": block["sign"],
                "mass": qstr(block["mass"]),
                "cells": [{"c": c, "d": d} for c, d in block["cells"]],
            }
            for block in blocks
        ],
        "qbp": {
            "block_instances_tested": len(block_values),
            "negative_block_instances": negative_blocks,
            "rows_tested": len(mclp_values),
            "rows_with_negative_block": rows_with_negative_block,
            "survives_k11": negative_blocks == 0,
            "first_lexicographic_negative_block": first_negative_block,
            "minimum_block": {
                "value": record(minimum_block[0]),
                "witness": minimum_block[1],
            },
        },
        "mclp": {
            "aggregates_tested": len(mclp_values),
            "negative_aggregates": sum(value < 0 for value in mclp_values.values()),
            "zero_aggregates": sum(value == 0 for value in mclp_values.values()),
            "all_positive": all(value > 0 for value in mclp_values.values()),
            "minimum": record(mclp_minimum),
            "minimum_locations": [
                {"u": u, "ell": ell}
                for (u, ell), value in sorted(mclp_values.items())
                if value == mclp_minimum
            ],
        },
        "rows": rows,
        "qti_exact": True,
        "qbd_exact": True,
        "reflection_exact": True,
        "downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(), indent=2, sort_keys=True) + "\n")
