#!/usr/bin/env python3
"""Exact narrow calibration of the M174 fixed-cell PCS event defect.

The program enumerates only the first two ordered transposition factors from
the two balanced source residuals.  It never constructs a quotient matrix or
looks at another target cell.  For their rank-two product ``s`` it evaluates
M168's phase-collapsed response ``f(s)=S(s)/A_s``.  Contributions are retained
by source channel J=0,1,2 and intermediate kind triangle/double before the
signed source subtraction.

Convention: (pq)(x)=p(q(x)); displayed factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cyc(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def tr(n: int, x: int, y: int) -> Perm:
    return cyc(n, (x, y))


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    out: list[tuple[int, ...]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        c: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        out.append(tuple(c))
    return out


@lru_cache(maxsize=None)
def completion_sizes(sizes: tuple[int, ...], length: int) -> int:
    if sum(sizes) - len(sizes) != length:
        return 0
    ans = math.factorial(length)
    for d in sizes:
        if d > 1:
            ans = ans * d ** (d - 2) // math.factorial(d - 1)
    return ans


def completion(p: Perm, length: int) -> int:
    return completion_sizes(tuple(sorted(map(len, cycles(p)))), length)


def internal_edges(n: int, component: tuple[int, ...]):
    vertices = sorted(component)
    for i, j in combinations(vertices, 2):
        yield tr(n, i, j)


def response(n: int, h: Perm, s: Perm) -> Fraction:
    """M168 PC response S(s)/A_s for the first fixed boundary cell."""
    q = mul(inv(s), h)
    cs = cycles(q)
    owner: dict[int, int] = {}
    for i, c in enumerate(cs):
        for x in c:
            owner[x] = i
    sizes = [len(c) for c in cs]
    generic = [s[(r + 1) % n] == (r + 1) % n for r in range(n)]
    counts = [0] * len(cs)
    adjacent = [0] * len(cs)
    for r in range(n):
        if generic[r]:
            counts[owner[r]] += 1
        if generic[r] and generic[(r + 1) % n]:
            i = owner[r]
            assert owner[(r + 1) % n] == i
            adjacent[i] += 1

    total = 0
    for i, d in enumerate(sizes):
        ordered = counts[i] * (counts[i] - 1) - 2 * adjacent[i]
        if ordered:
            after = sizes[:i] + [1, 1, d - 2] + sizes[i + 1 :]
            total += ordered * completion_sizes(tuple(sorted(after)), n - 5)
    for i in range(len(sizes)):
        for j in range(i + 1, len(sizes)):
            ordered = 2 * counts[i] * counts[j]
            if ordered:
                after = [d for a, d in enumerate(sizes) if a not in (i, j)]
                after += [1, sizes[i] - 1, 1, sizes[j] - 1]
                total += ordered * completion_sizes(tuple(sorted(after)), n - 5)
    return Fraction(total, completion(q, n - 3))


def frac(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def source_expectation(
    k: int, label: str
) -> tuple[
    dict[tuple[int, str], Fraction],
    dict[tuple[int, str], Fraction],
    dict[str, tuple[Fraction, Fraction]],
]:
    n = 3 * k
    h = cyc(n, tuple(range(n)))
    if label == "A":
        source = cyc(n, (0, k, 2 * k))
    elif label == "B":
        source = mul(tr(n, 0, 1), tr(n, k, 2 * k))
    else:
        raise ValueError(label)
    residual = mul(inv(source), h)
    initial = cycles(residual)
    middle_index = next(i for i, c in enumerate(initial) if k in c)
    component_of = {x: i for i, c in enumerate(initial) for x in c}
    rank = n - len(initial)
    denominator = completion(residual, rank)
    ans: dict[tuple[int, str], Fraction] = defaultdict(Fraction)
    masses: dict[tuple[int, str], Fraction] = defaultdict(Fraction)
    response_cache: dict[Perm, Fraction] = {}
    kind_cache: dict[Perm, str] = {}
    mass = Fraction(0)

    for first_component, c in enumerate(initial):
        if len(c) == 1:
            continue
        first_is_exterior = first_component != middle_index
        for first in internal_edges(n, c):
            after_first = mul(first, residual)
            for c2 in cycles(after_first):
                if len(c2) == 1:
                    continue
                second_original = component_of[c2[0]]
                assert all(component_of[x] == second_original for x in c2)
                second_is_exterior = second_original != middle_index
                for second in internal_edges(n, c2):
                    s = mul(first, second)
                    numerator = completion(mul(inv(s), residual), rank - 2)
                    if not numerator:
                        continue
                    probability = Fraction(numerator, denominator)
                    support = sum(x != s[x] for x in range(n))
                    kind = "T" if support == 3 else "D"
                    assert support in (3, 4)
                    j = int(first_is_exterior) + int(second_is_exterior)
                    if s not in response_cache:
                        response_cache[s] = response(n, h, s)
                        kind_cache[s] = kind
                    ans[(j, kind)] += probability * response_cache[s]
                    masses[(j, kind)] += probability
                    mass += probability
    assert mass == 1
    ranges = {
        kind: (
            min(value for s, value in response_cache.items() if kind_cache[s] == kind),
            max(value for s, value in response_cache.items() if kind_cache[s] == kind),
        )
        for kind in ("T", "D")
        if kind in kind_cache.values()
    }
    return dict(ans), dict(masses), ranges


def analyze(k: int) -> dict[str, object]:
    if k < 3 or k > 7 or k % 2 == 0:
        raise ValueError("exact calibration is capped at odd 3<=k<=7")
    started = time.monotonic()
    a, amass, arange = source_expectation(k, "A")
    b, bmass, brange = source_expectation(k, "B")
    keys = [(j, kind) for j in range(3) for kind in ("T", "D")]
    pieces = {key: b.get(key, Fraction(0)) - a.get(key, Fraction(0)) for key in keys}
    assert sum((pieces[(0, kind)] for kind in ("T", "D")), Fraction(0)) == 0
    signed_masses = {
        key: bmass.get(key, Fraction(0)) - amass.get(key, Fraction(0))
        for key in keys
    }
    assert all(signed_masses[(0, kind)] == 0 for kind in ("T", "D"))
    assert all(signed_masses[(1, kind)] == 0 for kind in ("T", "D"))
    expected_transfer = Fraction(12 * (k - 1), 3 * k * (3 * k - 4) * (2 * k - 1))
    assert signed_masses[(2, "T")] == expected_transfer
    assert signed_masses[(2, "D")] == -expected_transfer
    delta = sum(pieces.values(), Fraction(0))

    n = 3 * k
    h = cyc(n, tuple(range(n)))
    target = mul(tr(n, 0, 1), tr(n, 2, 3))
    f_t = completion(mul(inv(target), h), n - 3)
    pi_y = Fraction(2 * n * f_t, n ** (n - 2))
    signed_sum = 2 * delta / pi_y
    boundary_response = math.exp(2) * (n - 3) * (n - 4) * float(delta)
    boundary_response -= 2 * n * float(expected_transfer)
    return {
        "k": k,
        "n": n,
        "event_delta_exact": frac(delta),
        "event_delta_float": float(delta),
        "signed_cell_sum_exact": frac(signed_sum),
        "signed_cell_sum_float": float(signed_sum),
        "k_times_signed_cell_sum": float(k * signed_sum),
        "n_squared_event_delta": float(n * n * delta),
        "boundary_response_coefficient_float": boundary_response,
        "source_channel_and_kind": {
            f"J{j}_{kind}": {
                "A_expectation_exact": frac(a.get((j, kind), Fraction(0))),
                "B_expectation_exact": frac(b.get((j, kind), Fraction(0))),
                "A_mass_exact": frac(amass.get((j, kind), Fraction(0))),
                "B_mass_exact": frac(bmass.get((j, kind), Fraction(0))),
                "signed_mass_exact": frac(
                    signed_masses[(j, kind)]
                ),
                "signed_exact": frac(pieces[(j, kind)]),
                "signed_float": float(pieces[(j, kind)]),
                "n_squared_signed": float(n * n * pieces[(j, kind)]),
            }
            for j, kind in keys
        },
        "accessible_response_ranges": {
            label: {
                kind: {"minimum": float(bounds[0]), "maximum": float(bounds[1])}
                for kind, bounds in ranges.items()
            }
            for label, ranges in (("A", arange), ("B", brange))
        },
        "J0_exactly_cancelled_after_kind_sum": True,
        "kind_transfer_formula_exact": frac(expected_transfer),
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frozen-m168", type=Path)
    args = parser.parse_args()
    results = [analyze(k) for k in args.k]
    frozen_checks = []
    if args.frozen_m168:
        frozen = json.loads(args.frozen_m168.read_text())
        by_k = {row["k"]: row for row in frozen["results"]}
        for row in results:
            if row["k"] in by_k:
                expected = sum(
                    (Fraction(x["score_exact"]) for x in by_k[row["k"]]["rows"]),
                    Fraction(0),
                )
                assert Fraction(row["signed_cell_sum_exact"]) == expected
                frozen_checks.append({"k": row["k"], "exact_match": True})
    payload = {
        "status": "exact finite calibration only; no sign or asymptotic inference",
        "target": "M168 PCS-bound for the first fixed boundary cell only",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "frozen_m168_checks": frozen_checks,
        "results": results,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
