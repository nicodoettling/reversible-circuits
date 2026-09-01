#!/usr/bin/env python3
"""Fresh finite k=7,9 check of the central-double event calculation.

The implementation imports no predecessor code.  It constructs ordered
transposition-pair multiplicities, the exact integer completion-count kernel,
and the cyclic quotient directly.  Matrix arithmetic is then floating, so
the output is a deterministic finite formula check, not asymptotic evidence.

Convention: (pq)(x)=p(q(x)); tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def transposition(n: int, x: int, y: int) -> Perm:
    answer = list(range(n))
    answer[x], answer[y] = answer[y], answer[x]
    return tuple(answer)


def cycle_permutation(n: int, entries: tuple[int, ...]) -> Perm:
    answer = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        answer[x] = y
    return tuple(answer)


def cycle_sizes(p: Perm) -> tuple[int, ...]:
    seen: set[int] = set()
    answer: list[int] = []
    for start in range(len(p)):
        if start in seen:
            continue
        x = start
        size = 0
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        answer.append(size)
    return tuple(sorted(answer, reverse=True))


@lru_cache(maxsize=None)
def completion_from_sizes(sizes: tuple[int, ...], length: int) -> int:
    n = sum(sizes)
    if n - len(sizes) != length:
        return 0
    answer = math.factorial(length)
    for size in sizes:
        if size > 1:
            answer = answer * size ** (size - 2) // math.factorial(size - 1)
    return answer


def support_gaps(p: Perm) -> tuple[int, int, int, int]:
    moved = sorted(x for x, y in enumerate(p) if x != y)
    assert len(moved) == 4
    n = len(p)
    return (
        moved[1] - moved[0],
        moved[2] - moved[1],
        moved[3] - moved[2],
        n + moved[0] - moved[3],
    )


def state_kind(p: Perm) -> str:
    nontrivial = sorted(size for size in cycle_sizes(p) if size > 1)
    if nontrivial == [3]:
        return "T"
    if nontrivial == [2, 2]:
        return "D"
    raise AssertionError(nontrivial)


def event_mass_formula(n: int, threshold: int) -> Fraction:
    def tau(d: int) -> Fraction:
        return Fraction(d ** (d - 1), math.factorial(d))

    total = Fraction(0)
    for x in range(threshold, n + 1):
        for y in range(threshold, n - x + 1):
            for z in range(threshold, n - x - y + 1):
                w = n - x - y - z
                if w >= threshold:
                    total += tau(x) * tau(z) * tau(y + w)
    return Fraction(n * math.factorial(n - 3), n ** (n - 2)) * total


def color(p: Perm, h: Perm) -> str:
    gaps = support_gaps(p)
    x, y, z, w = gaps
    residual = cycle_sizes(compose(inverse(p), h))
    separated = tuple(sorted((x, z, y + w), reverse=True))
    nested = tuple(sorted((x + z, y, w), reverse=True))
    matches = []
    if residual == separated:
        matches.append("S")
    if residual == nested:
        matches.append("N")
    return "".join(matches) or "?"


def analyze(k: int) -> dict[str, object]:
    if k < 3 or not k % 2:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h = cycle_permutation(n, tuple(range(n)))
    h_inverse = inverse(h)
    gates = [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]
    multiplicity: collections.Counter[Perm] = collections.Counter()
    for first in gates:
        for second in gates:
            multiplicity[compose(first, second)] += 1

    completion3: dict[Perm, int] = {}
    for state in multiplicity:
        residual = compose(inverse(state), h)
        count = completion_from_sizes(cycle_sizes(residual), n - 3)
        if count:
            completion3[state] = count
            assert (state_kind(state), multiplicity[state]) in (("T", 3), ("D", 2))

    def theta(state: Perm) -> Perm:
        return compose(h_inverse, compose(state, h))

    orbit_id: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for state in sorted(completion3):
        if state in orbit_id:
            continue
        orbit: list[Perm] = []
        current = state
        while current not in orbit:
            orbit.append(current)
            current = theta(current)
        assert current == state
        index = len(orbits)
        for member in orbit:
            orbit_id[member] = index
        orbits.append(orbit)

    raw_states = list(completion3)
    raw_inverses = [inverse(state) for state in raw_states]
    raw_multiplicities = [multiplicity[state] for state in raw_states]
    dimension = len(orbits)
    kernel = np.zeros((dimension, dimension), dtype=np.float64)
    for source_index, orbit in enumerate(orbits):
        source = orbit[0]
        source_inverse_h = compose(inverse(source), h)
        denominator = completion3[source]
        row = kernel[source_index]
        for state, state_inverse, lift in zip(raw_states, raw_inverses, raw_multiplicities):
            # (source*state)^-1 h = state^-1 source^-1 h.
            residual = compose(state_inverse, source_inverse_h)
            numerator = completion_from_sizes(cycle_sizes(residual), n - 5)
            if numerator:
                row[orbit_id[state]] += lift * numerator / denominator
        assert abs(float(np.sum(row)) - 1.0) < 2e-11

    stationary = np.array(
        [
            len(orbit) * multiplicity[orbit[0]] * completion3[orbit[0]] / n ** (n - 2)
            for orbit in orbits
        ],
        dtype=np.float64,
    )
    assert abs(float(np.sum(stationary)) - 1.0) < 2e-12

    source_a = cycle_permutation(n, (0, k, 2 * k))
    source_b = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    ai, bi = orbit_id[source_a], orbit_id[source_b]
    assert len(orbits[ai]) == k and len(orbits[bi]) == n
    assert all(len(orbit) == n for orbit in orbits if state_kind(orbit[0]) == "D")
    eta = kernel[bi] - kernel[ai]
    delta = eta @ kernel
    threshold = (k + 1) // 2
    event = [
        index
        for index, orbit in enumerate(orbits)
        if state_kind(orbit[0]) == "D" and min(support_gaps(orbit[0])) >= threshold
    ]
    mass = float(np.sum(stationary[event]))
    signed = float(np.sum(delta[event]))
    mass_exact = event_mass_formula(n, threshold)
    assert abs(mass - float(mass_exact)) < 2e-12
    expected_orbits = math.comb(n - 4 * threshold + 3, 3) // 2
    assert len(event) == expected_orbits

    rows = []
    for index in event:
        score = float(delta[index] / stationary[index])
        rows.append(
            {
                "orbit": index,
                "gaps": list(support_gaps(orbits[index][0])),
                "color": color(orbits[index][0], h),
                "k_times_score": k * score,
            }
        )
    negative = [row for row in rows if row["k_times_score"] < 0]
    return {
        "k": k,
        "n": n,
        "raw_states": len(raw_states),
        "quotient_states": dimension,
        "event_orbits": len(event),
        "event_mass_exact": f"{mass_exact.numerator}/{mass_exact.denominator}",
        "event_mass": mass,
        "event_signed": signed,
        "k_times_mass": k * mass,
        "k_squared_signed": k * k * signed,
        "k_times_mean_score": k * signed / mass,
        "negative_event_orbits": len(negative),
        "minimum_k_times_score": min(row["k_times_score"] for row in rows),
        "maximum_k_times_score": max(row["k_times_score"] for row in rows),
        "negative_rows": negative,
        "checks": {
            "quotient_rows_normalized": True,
            "stationary_normalized": True,
            "source_orbit_sizes": True,
            "all_double_orbits_have_size_n": True,
            "exact_event_mass_formula": True,
            "event_orbit_formula": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "independent_deterministic_floating_finite_check_only",
        "target": "M102 k=7,9 central-double event and pointwise scores",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(k) for k in args.k],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    compact = []
    for row in payload["results"]:
        compact.append({key: value for key, value in row.items() if key != "negative_rows"})
    print(json.dumps(compact, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
