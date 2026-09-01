#!/usr/bin/env python3
"""Clean-room exact audit of the frozen M300 k=7 claims.

Standard library only.  This script imports no project or predecessor code
or data and evaluates no rank other than k=7.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import factorial, lcm
from pathlib import Path


K = 7
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


def residual_owners(
    e: tuple[int, int], f: tuple[int, int]
) -> tuple[list[int | None], list[int]]:
    # q=s^{-1}h=s h because s is a double of disjoint transpositions.
    q = [apply_double((x + 1) % N, e, f) for x in range(N)]
    seen = [False] * N
    owner = [-1] * N
    sizes: list[int] = []
    for start in range(N):
        if seen[start]:
            continue
        cyc: list[int] = []
        x = start
        while not seen[x]:
            seen[x] = True
            owner[x] = len(sizes)
            cyc.append(x)
            x = q[x]
        assert x == start
        sizes.append(len(cyc))
    assert sorted(sizes) and sum(sizes) == N

    generic: list[int | None] = []
    for x in range(N):
        head = (x + 1) % N
        generic.append(owner[x] if apply_double(head, e, f) == head else None)
    return generic, sizes


@lru_cache(maxsize=None)
def response(
    e: tuple[int, int], f: tuple[int, int], ell: int
) -> Fraction:
    assert not (set(e) & set(f))
    generic, sizes = residual_owners(e, f)
    a_ratio = [tau(d - 1) / tau(d) for d in sizes]
    b_ratio = [tau(d - 2) / tau(d) for d in sizes]
    total = Fraction(0)
    for x, own_a in enumerate(generic):
        own_b = generic[(x + ell) % N]
        if own_a is None or own_b is None:
            continue
        if own_a == own_b:
            total += b_ratio[own_a]
        else:
            total += a_ratio[own_a] * a_ratio[own_b]
    return total


def middle_edge(a: int, u: int) -> tuple[int, int]:
    return edge(K + a, K + ((a + u) % K))


def fixed_cell(f: tuple[int, int], ell: int) -> Fraction:
    return sum((mass * response(e, f, ell) for e, mass in GAMMA.items()), Fraction(0))


def class_cell(u: int, ell: int) -> Fraction:
    return sum((fixed_cell(middle_edge(a, u), ell) for a in range(K)), Fraction(0))


def frac_record(x: Fraction) -> dict[str, object]:
    return {"exact": str(x), "float": float(x)}


def main() -> dict[str, object]:
    assert len(LAGS) == 18
    assert set(LAW_M) == {
        middle_edge(a, u) for u in range(1, (K + 1) // 2) for a in range(K)
    }
    assert sum(K * v(K, u) for u in range(1, (K + 1) // 2)) == 1

    positive = {e: g for e, g in GAMMA.items() if g > 0}
    negative = {e: g for e, g in GAMMA.items() if g < 0}
    assert sum(GAMMA.values(), Fraction(0)) == 0
    assert len(positive) == len(negative) == K * (K - 1)

    a_set, p_set = set(A), set(P)
    cross_seen: set[tuple[int, int]] = set()
    internal_seen: set[tuple[int, int]] = set()
    for e in LAW_L:
        c = cycle_cut(L, e)
        is_cross = ((e[0] in a_set and e[1] in p_set)
                    or (e[1] in a_set and e[0] in p_set))
        if is_cross:
            cross_seen.add(e)
            assert GAMMA[e] == v(D, c) > 0
        else:
            internal_seen.add(e)
            assert GAMMA[e] == v(D, c) - v(K, c) / 2 < 0
    seam_seen = {edge(0, c) for c in range(1, K)}
    for c in range(1, K):
        assert GAMMA[edge(0, c)] == -v(K, c) / 2 < 0
    assert cross_seen == set(positive)
    assert internal_seen | seam_seen == set(negative)
    assert not (internal_seen & seam_seen)

    cut_data: dict[int, dict[str, object]] = {}
    rs: list[Fraction] = []
    cumulative: list[Fraction] = []
    running = Fraction(0)
    for c in range(1, K):
        cut_edges = {e for e in LAW_L if cycle_cut(L, e) == c}
        x_edges = cut_edges & cross_seen
        j_edges = cut_edges & internal_seen
        assert len(cut_edges) == D
        assert len(x_edges) == 2 * c
        assert len(j_edges) == D - 2 * c
        q = v(K, c) / 2 - v(D, c)
        x = 2 * c * v(D, c)
        y = (D - 2 * c) * q + v(K, c) / 2
        assert q > 0 and y > 0
        assert y == (K - c) * v(K, c) - (D - 2 * c) * v(D, c)
        r = x - y
        assert r == D * v(D, c) - (K - c) * v(K, c)
        running += r
        rs.append(r)
        cumulative.append(running)
        cut_data[c] = {
            "X": tuple(sorted(x_edges)),
            "J": tuple(sorted(j_edges)),
            "q": q,
            "x": x,
            "y": y,
            "r": r,
            "R": running,
        }
    assert cumulative[-1] == 0
    common_denominator = 1
    for value in rs + cumulative:
        common_denominator = lcm(common_denominator, value.denominator)

    fixed: dict[tuple[int, int, int], Fraction] = {}
    classes: dict[tuple[int, int], Fraction] = {}
    etas: dict[int, Fraction] = {}
    eha_checks = 0
    state_reflection_checks = 0
    for u in range(1, (K + 1) // 2):
        for a in range(K):
            f = middle_edge(a, u)
            for ell in LAGS:
                value = fixed_cell(f, ell)
                fixed[(u, a, ell)] = value
                assert value == fixed_cell(f, N - ell)
                state_reflection_checks += 1
        for ell in LAGS:
            direct = sum(fixed[(u, a, ell)] for a in range(K))
            classes[(u, ell)] = direct
            assert direct == classes[(u, N - ell)] if (u, N - ell) in classes else True

            def g(edge_: tuple[int, int]) -> Fraction:
                return sum(response(edge_, middle_edge(a, u), ell) for a in range(K))

            first = Fraction(0)
            second = Fraction(0)
            raw = Fraction(0)
            for c in range(1, K):
                data = cut_data[c]
                xbar = sum((g(e) for e in data["X"]), Fraction(0)) / (2 * c)
                ybar = (
                    data["q"] * sum((g(e) for e in data["J"]), Fraction(0))
                    + v(K, c) * g(edge(0, c)) / 2
                ) / data["y"]
                raw += data["x"] * xbar - data["y"] * ybar
                first += data["y"] * (xbar - ybar)
                if c <= K - 2:
                    next_xbar = sum(
                        (g(e) for e in cut_data[c + 1]["X"]), Fraction(0)
                    ) / (2 * (c + 1))
                    second += data["R"] * (xbar - next_xbar)
            assert direct == raw == first + second
            eha_checks += 1

    for ell in LAGS:
        class_average = sum(
            v(K, u) * classes[(u, ell)] for u in range(1, (K + 1) // 2)
        )
        direct_average = sum(
            LAW_M[f] * fixed_cell(f, ell) for f in LAW_M
        )
        assert class_average == direct_average
        etas[ell] = class_average
        assert class_average == etas[N - ell] if N - ell in etas else True

    fixed_negative = {key: value for key, value in fixed.items() if value < 0}
    class_min = min(classes.values())
    fixed_min = min(fixed.values())
    eta_min = min(etas.values())
    assert all(value > 0 for value in classes.values())
    assert all(value > 0 for value in etas.values())
    assert len(classes) == 54 and len(fixed) == 378
    assert len(fixed_negative) == 44

    return {
        "scope": {
            "k": K,
            "n": N,
            "admissible_lags": list(LAGS),
            "new_ranks": [K],
            "imports_project_code_or_data": False,
        },
        "normalization": {
            "law_L": str(sum(LAW_L.values(), Fraction(0))),
            "law_M": str(sum(LAW_M.values(), Fraction(0))),
            "law_C_minus": str(sum(LAW_MINUS.values(), Fraction(0))),
            "law_C_plus": str(sum(LAW_PLUS.values(), Fraction(0))),
            "gamma": str(sum(GAMMA.values(), Fraction(0))),
            "middle_cut_classes": (K - 1) // 2,
            "middle_edges": len(LAW_M),
        },
        "hahn_support": {
            "positive_count": len(positive),
            "negative_count": len(negative),
            "cross_count": len(cross_seen),
            "internal_count": len(internal_seen),
            "seam_count": len(seam_seen),
        },
        "abel_coefficients": {
            "common_denominator": common_denominator,
            "r_numerators": [x.numerator * (common_denominator // x.denominator) for x in rs],
            "R_numerators": [x.numerator * (common_denominator // x.denominator) for x in cumulative],
            "R_signs": [(-1 if x < 0 else 1 if x > 0 else 0) for x in cumulative],
            "R_last": str(cumulative[-1]),
        },
        "finite_cells": {
            "class_cells": len(classes),
            "class_positive": sum(value > 0 for value in classes.values()),
            "class_minimum": frac_record(class_min),
            "class_minimum_locations": [
                {"u": u, "ell": ell}
                for (u, ell), value in sorted(classes.items()) if value == class_min
            ],
            "fixed_cells": len(fixed),
            "fixed_negative": len(fixed_negative),
            "fixed_minimum": frac_record(fixed_min),
            "fixed_minimum_locations": [
                {"u": u, "phase": a, "edge": list(middle_edge(a, u)), "ell": ell}
                for (u, a, ell), value in sorted(fixed.items()) if value == fixed_min
            ],
            "eta_cells": len(etas),
            "eta_positive": sum(value > 0 for value in etas.values()),
            "eta_minimum": frac_record(eta_min),
            "eta_minimum_locations": [ell for ell, value in sorted(etas.items()) if value == eta_min],
        },
        "guards": {
            "state_reflection_checks": state_reflection_checks,
            "eha_exact_checks": eha_checks,
            "direct_equals_cut_class_checks": len(LAGS),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = main()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
