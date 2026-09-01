#!/usr/bin/env python3
"""Exact sole-rank falsifier for M307's pre-frozen QCP_1 candidate.

Standard library only.  This script fixes k=9, imports no project or
predecessor code/data, and retains all middle phases in every response mean.
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


K = 9
N = 3 * K
D = 2 * K - 1
LAGS = tuple(range(2, N - 1))
A = tuple(range(1, K))
P = tuple(range(2 * K, 3 * K))
L = A + P
M = tuple(range(K, 2 * K))
C_MINUS = tuple(range(0, K))
C_PLUS = P


def tau(d: int) -> Fraction:
    if d == 1:
        return Fraction(1)
    if d <= 0:
        return Fraction(0)
    return Fraction(d ** (d - 2), factorial(d - 1))


def v(d: int, c: int) -> Fraction:
    assert 1 <= c <= d - 1
    return tau(c) * tau(d - c) / ((d - 1) * tau(d))


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
LAW_M = chord_law(M)
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


@lru_cache(maxsize=None)
def response(e: tuple[int, int], f: tuple[int, int], ell: int) -> Fraction:
    generic, sizes = owner_data(e, f)
    a = tuple(tau(d - 1) / tau(d) for d in sizes)
    b = tuple(tau(d - 2) / tau(d) for d in sizes)
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
            e for e in all_c
            if ((e[0] in a_set and e[1] in p_set)
                or (e[1] in a_set and e[0] in p_set))
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

    x_left: dict[int, Fraction] = {}
    x_right: dict[int, Fraction] = {}
    y_left: dict[int, Fraction] = {}
    y_right: dict[int, Fraction] = {}
    running_x = running_y = Fraction(0)
    for c in range(1, K):
        x_left[c], y_left[c] = running_x, running_y
        running_x += x_mass[c]
        running_y += y_mass[c]
        x_right[c], y_right[c] = running_x, running_y
    assert running_x == running_y == mu

    pi: dict[tuple[int, int], Fraction] = {}
    for c in range(1, K):
        for d in range(1, K):
            overlap = min(x_right[c], y_right[d]) - max(x_left[c], y_left[d])
            if overlap > 0:
                pi[(c, d)] = overlap
    for c in range(1, K):
        assert sum((mass for (i, _), mass in pi.items() if i == c), Fraction(0)) == x_mass[c]
    for d in range(1, K):
        assert sum((mass for (_, j), mass in pi.items() if j == d), Fraction(0)) == y_mass[d]
    assert sum(pi.values(), Fraction(0)) == mu
    return cut_edges, x_mass, y_mass, r_mass, R_mass, mu, pi


def main() -> dict[str, object]:
    assert len(LAGS) == 24
    assert set(LAW_M) == {
        middle_edge(a, u) for u in range(1, (K + 1) // 2) for a in range(K)
    }
    assert sum(K * v(K, u) for u in range(1, (K + 1) // 2)) == 1
    assert sum(GAMMA.values(), Fraction(0)) == 0
    assert sum(g > 0 for g in GAMMA.values()) == K * (K - 1)
    assert sum(g < 0 for g in GAMMA.values()) == K * (K - 1)

    cut_edges, x_mass, y_mass, r_mass, R_mass, mu, pi = transport_data()
    rows: list[dict[str, object]] = []
    qcp_cells = 0
    negative_cells = 0
    first_negative = None
    minimum_difference = None
    minimum_contribution = None
    mclp_values: dict[tuple[int, int], Fraction] = {}
    x_means: dict[tuple[int, int, int], Fraction] = {}
    y_means: dict[tuple[int, int, int], Fraction] = {}

    for u in range(1, (K + 1) // 2):
        middle = tuple(middle_edge(a, u) for a in range(K))
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

            direct = sum((mass * g[e] for e, mass in GAMMA.items()), Fraction(0))
            transported = sum(
                (mass * (xb[c] - yb[d]) for (c, d), mass in pi.items()),
                Fraction(0),
            )
            cut_form = sum(
                (x_mass[c] * xb[c] - y_mass[c] * yb[c] for c in range(1, K)),
                Fraction(0),
            )
            assert direct == transported == cut_form
            mclp_values[(u, ell)] = direct

            row_negative = 0
            row_minimum = None
            row_first = None
            for c, d in sorted(pi):
                difference = xb[c] - yb[d]
                contribution = pi[(c, d)] * difference
                qcp_cells += 1
                if minimum_difference is None or difference < minimum_difference[0]:
                    minimum_difference = (difference, u, ell, c, d, pi[(c, d)])
                if minimum_contribution is None or contribution < minimum_contribution[0]:
                    minimum_contribution = (contribution, difference, u, ell, c, d, pi[(c, d)])
                if difference < 0:
                    negative_cells += 1
                    row_negative += 1
                    witness = {
                        "u": u,
                        "ell": ell,
                        "c": c,
                        "d": d,
                        "pi": qstr(pi[(c, d)]),
                        "Xbar": qstr(xb[c]),
                        "Ybar": qstr(yb[d]),
                        "difference": qstr(difference),
                        "weighted_contribution": qstr(contribution),
                    }
                    if first_negative is None:
                        first_negative = witness
                    if row_first is None:
                        row_first = witness
                if row_minimum is None or difference < row_minimum:
                    row_minimum = difference
            rows.append(
                {
                    "u": u,
                    "ell": ell,
                    "transport_cells": len(pi),
                    "negative_qcp_cells": row_negative,
                    "first_negative": row_first,
                    "minimum_difference": qstr(row_minimum),
                    "mclp_value": qstr(direct),
                    "mclp_value_float": float(direct),
                }
            )

    for u in range(1, (K + 1) // 2):
        for ell in LAGS:
            assert mclp_values[(u, ell)] == mclp_values[(u, N - ell)]
            for c in range(1, K):
                assert x_means[(u, ell, c)] == x_means[(u, N - ell, c)]
                assert y_means[(u, ell, c)] == y_means[(u, N - ell, c)]

    mclp_minimum = min(mclp_values.values())
    assert minimum_difference is not None and minimum_contribution is not None
    return {
        "status": "exact sole-rank test of pre-frozen QCP_1; all-rank MCLP_1 remains separate",
        "scope": {
            "k": K,
            "n": N,
            "cut_classes": list(range(1, (K + 1) // 2)),
            "admissible_lags": list(LAGS),
            "new_ranks": [K],
            "imports_project_or_predecessor_code_or_data": False,
        },
        "normalization": {
            "gamma_mass": qstr(sum(GAMMA.values(), Fraction(0))),
            "positive_exterior_atoms": sum(g > 0 for g in GAMMA.values()),
            "negative_exterior_atoms": sum(g < 0 for g in GAMMA.values()),
            "positive_cut_mass": qstr(mu),
            "negative_cut_mass": qstr(sum(y_mass.values(), Fraction(0))),
            "transport_mass": qstr(sum(pi.values(), Fraction(0))),
            "transport_support_cells": len(pi),
            "transport": [
                {"c": c, "d": d, "pi": qstr(mass)}
                for (c, d), mass in sorted(pi.items())
            ],
        },
        "abel_coefficients": {
            "r": {str(c): qstr(r_mass[c]) for c in range(1, K)},
            "R": {str(c): qstr(R_mass[c]) for c in range(1, K)},
            "R_signs": {
                str(c): (-1 if R_mass[c] < 0 else 1 if R_mass[c] > 0 else 0)
                for c in range(1, K)
            },
        },
        "qcp": {
            "cells_tested": qcp_cells,
            "negative_cells": negative_cells,
            "survives_k9": negative_cells == 0,
            "first_lexicographic_negative": first_negative,
            "minimum_difference": {
                "value": record(minimum_difference[0]),
                "u": minimum_difference[1],
                "ell": minimum_difference[2],
                "c": minimum_difference[3],
                "d": minimum_difference[4],
                "pi": qstr(minimum_difference[5]),
            },
            "minimum_weighted_contribution": {
                "value": record(minimum_contribution[0]),
                "difference": qstr(minimum_contribution[1]),
                "u": minimum_contribution[2],
                "ell": minimum_contribution[3],
                "c": minimum_contribution[4],
                "d": minimum_contribution[5],
                "pi": qstr(minimum_contribution[6]),
            },
        },
        "mclp": {
            "cells_tested": len(mclp_values),
            "negative_cells": sum(value < 0 for value in mclp_values.values()),
            "all_positive": all(value > 0 for value in mclp_values.values()),
            "minimum": record(mclp_minimum),
            "minimum_locations": [
                {"u": u, "ell": ell}
                for (u, ell), value in sorted(mclp_values.items())
                if value == mclp_minimum
            ],
        },
        "rows": rows,
        "reflection_exact": True,
        "downstream_inference": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(main(), indent=2, sort_keys=True) + "\n")
