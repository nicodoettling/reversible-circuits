#!/usr/bin/env python3
"""Exact finite checker for M199's literal double-profile formulas.

The script is standard-library only and capped at odd k<=9.  It validates the
closed B/A one-run and two-run formulas against the original
minimal-factorization recurrence.  Finite ratios make no universal claim.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path

Perm = tuple[int, ...]
Key = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for x, y in enumerate(p):
        ans[y] = x
    return tuple(ans)


def cycle_perm(n: int, entries: tuple[int, ...]) -> Perm:
    ans = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        ans[x] = y
    return tuple(ans)


def transposition(n: int, x: int, y: int) -> Perm:
    ans = list(range(n))
    ans[x], ans[y] = ans[y], ans[x]
    return tuple(ans)


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        part: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = p[x]
        out.append(tuple(part))
    return out


def internal_edges(p: Perm) -> list[Perm]:
    return [
        transposition(len(p), x, y)
        for part in cycles(p)
        for x, y in combinations(part, 2)
    ]


def edge_vertices(e: Perm) -> tuple[int, int]:
    moved = [x for x in range(len(e)) if e[x] != x]
    assert len(moved) == 2
    return moved[0], moved[1]


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def completion(p: Perm) -> Fraction:
    parts = cycles(p)
    rank = sum(len(c) - 1 for c in parts)
    ans = Fraction(math.factorial(rank))
    for part in parts:
        ans *= tau(len(part))
    return ans


def source(k: int, side: str) -> tuple[Perm, list[tuple[int, ...]]]:
    n = 3 * k
    if side == "B":
        part = tuple(range(1, k)) + tuple(range(2 * k, 3 * k))
        return cycle_perm(n, part), [part]
    lower = tuple(range(k))
    upper = tuple(range(2 * k, 3 * k))
    return compose(cycle_perm(n, lower), cycle_perm(n, upper)), [lower, upper]


def split_size(e: Perm, original: list[tuple[int, ...]]) -> int:
    x, y = edge_vertices(e)
    part = next(c for c in original if x in c)
    ix, iy = part.index(x), part.index(y)
    gap = (iy - ix) % len(part)
    return min(gap, len(part) - gap)


def ambient_runs(component: tuple[int, ...], n: int) -> int:
    support = set(component)
    starts = [x for x in support if (x - 1) % n not in support]
    assert starts
    return len(starts)


def profile(e: Perm, f: Perm, h: Perm) -> dict[Key, int]:
    residual = compose(inverse(compose(e, f)), h)
    parts = cycles(residual)
    assert len(parts) == 3
    out: defaultdict[Key, int] = defaultdict(int)
    for part in parts:
        run_type = ambient_runs(part, len(h))
        assert run_type in (1, 2)
        out[(run_type, len(part))] += 1
    return dict(out)


def literal_profiles(k: int, side: str) -> tuple[dict[int, dict[Key, Fraction]], dict[int, Fraction], int]:
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    src, original = source(k, side)
    denominator = completion(src)
    mass: defaultdict[int, Fraction] = defaultdict(Fraction)
    raw: dict[int, defaultdict[Key, Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    collisions = 0

    for e in internal_edges(src):
        first = compose(e, src)
        for f in internal_edges(first):
            if set(edge_vertices(e)) & set(edge_vertices(f)):
                continue
            s = split_size(e, original)
            weight = completion(compose(f, first)) / denominator
            counts = profile(e, f, h)
            mass[s] += weight
            for key, multiplicity in counts.items():
                raw[s][key] += weight * multiplicity
            if any(value > 1 for value in counts.values()):
                collisions += 1

    normalized = {
        s: {key: value / mass[s] for key, value in values.items()}
        for s, values in raw.items()
    }
    return normalized, dict(mass), collisions


def b(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def kernel(R: int, r: int, d: int) -> Fraction:
    return b(d) * b(r - d) / (R * b(r))


def gamma(k: int, side: str, s: int) -> Fraction:
    other = (2 * k - 1 - s) if side == "B" else (k - s)
    return Fraction(2, 2 * k - 3) * (
        2 - Fraction(1, s) - Fraction(1, other)
    )


def prefix(p: dict[Key, Fraction], ell: int, one_only: bool) -> Fraction:
    return sum(
        value
        for (run_type, size), value in p.items()
        if 2 <= size <= ell and (not one_only or run_type == 1)
    )



def closed_formula(k: int, side: str, s: int, ell: int, one_only: bool) -> Fraction:
    """Literal interval-kernel sum, independent of completion enumeration."""
    n = 3 * k
    h = cycle_perm(n, tuple(range(n)))
    src, original = source(k, side)
    R = 2 * k - 3
    total = Fraction()
    candidates = [
        e for e in internal_edges(src) if split_size(e, original) == s
    ]

    for e in candidates:
        first = compose(e, src)
        for f in internal_edges(first):
            if set(edge_vertices(e)) & set(edge_vertices(f)):
                continue
            parent = next(
                part
                for part in cycles(first)
                if set(edge_vertices(f)).issubset(part)
            )
            after = compose(f, first)
            children = [
                part for part in cycles(after) if set(part).issubset(parent)
            ]
            assert len(children) == 2
            weight = kernel(R, len(parent), len(children[0]))
            counts = {
                key: Fraction(value) for key, value in profile(e, f, h).items()
            }
            total += weight * prefix(counts, ell, one_only)

    return total / len(candidates) / (1 - gamma(k, side, s))


def run_case(k: int) -> dict:
    bprof, bmass, bcoll = literal_profiles(k, "B")
    aprof, amass, acoll = literal_profiles(k, "A")
    max_dv = {"X": 0.0, "Y": 0.0}
    max_point = {"X": 0.0, "Y": 0.0}
    checks = 0

    for ell in range(2, (3 * k - 1) // 2 + 1):
        for one_only, name in ((False, "X"), (True, "Y")):
            bvalues: dict[int, Fraction] = {}
            for s in range(1, k):
                expected = prefix(bprof[s], ell, one_only)
                closed = closed_formula(k, "B", s, ell, one_only)
                assert closed == expected
                bvalues[s] = closed
                checks += 1
            for s in aprof:
                expected = prefix(aprof[s], ell, one_only)
                closed = closed_formula(k, "A", s, ell, one_only)
                assert closed == expected
                max_point[name] = max(
                    max_point[name],
                    k * abs(float(bvalues[s] - closed)) / math.sqrt(ell),
                )
                checks += 1
            ratio = sum(
                math.sqrt(s) * abs(float(bvalues[s] - bvalues[s + 1]))
                for s in range(1, k - 1)
            ) / math.sqrt(ell)
            max_dv[name] = max(max_dv[name], ratio)

    return {
        "k": k,
        "literal_formula_assertions": checks,
        "disjoint_collision_events": {"B": bcoll, "A": acoll},
        "disjoint_masses": {
            "B": str(sum(bmass.values(), Fraction())),
            "A": str(sum(amass.values(), Fraction())),
        },
        "finite_max_DV_ratio": max_dv,
        "finite_max_pointwise_embedding_ratio": max_point,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "mission": "M199",
        "method": "exact literal interval-kernel reconstruction",
        "parameters": {"k": [3, 5, 7, 9], "seed": None},
        "python": platform.python_version(),
        "standard_library_only": True,
        "finite_only": True,
        "universal_inference": False,
        "results": [run_case(k) for k in (3, 5, 7, 9)],
        "status": "all exact profile-formula assertions passed; IKBE/DV/DE open",
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
