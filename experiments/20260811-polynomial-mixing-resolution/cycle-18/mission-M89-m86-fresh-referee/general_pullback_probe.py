#!/usr/bin/env python3
"""Exact combinatorial probe of M86 Lemma 7.1 on the base voltage torus.

Each current factor occurrence is stored as ``h^-1 t_label h``.  Besides the
permutation of ``h``, the code carries the integral voltage of the token path
realizing ``h`` from every starting vertex.  This avoids expanding the
conjugator as a potentially exponential free word.  At an adjacent equal
pair, the two pulled-back occurrence arcs give a closed contour on the
original chronological torus.  The script compares its nonzero homology with
literal deletion connectivity and tests the claimed ``2*q+2`` coordinate
bound.

This is a finite falsification probe.  Its update identities are checked after
every move against direct transposition Hurwitz algebra.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


sys.dont_write_bytecode = True

BASE_EDGES = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)

Edge = tuple[int, int]
Vector = tuple[int, int]


def edge(a: int, b: int) -> Edge:
    return (a, b) if a < b else (b, a)


def add(x: Vector, y: Vector) -> Vector:
    return x[0] + y[0], x[1] + y[1]


def neg(x: Vector) -> Vector:
    return -x[0], -x[1]


def move_point(x: int, e: Edge) -> int:
    a, b = e
    return b if x == a else a if x == b else x


def conjugate(a: Edge, by: Edge) -> Edge:
    return edge(move_point(a[0], by), move_point(a[1], by))


def connected_after_delete(edges: list[Edge], pair_index: int) -> bool:
    kept = edges[:pair_index] + edges[pair_index + 2:]
    adjacency = [[] for _ in range(8)]
    for a, b in kept:
        adjacency[a].append(b)
        adjacency[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == 8


@dataclass(frozen=True)
class Transport:
    """Token transport for a word h: x -> perm[x], with path voltage volt[x]."""

    perm: tuple[int, ...]
    volt: tuple[Vector, ...]


IDENTITY = Transport(tuple(range(8)), ((0, 0),) * 8)


def compose(h: Transport, g: Transport) -> Transport:
    """Transport of the algebraic product h*g, whose action is h after g."""
    return Transport(
        tuple(h.perm[g.perm[x]] for x in range(8)),
        tuple(add(g.volt[x], h.volt[g.perm[x]]) for x in range(8)),
    )


def inverse(h: Transport) -> Transport:
    pinv = [0] * 8
    for x, y in enumerate(h.perm):
        pinv[y] = x
    return Transport(
        tuple(pinv),
        tuple(neg(h.volt[pinv[x]]) for x in range(8)),
    )


def factor_transport(label: int) -> Transport:
    a, b = BASE_EDGES[label]
    perm = list(range(8))
    perm[a], perm[b] = b, a
    volt = [(0, 0)] * 8
    # The stored base voltage is oriented from the smaller displayed base
    # endpoint to the larger one; every BASE_EDGES entry is already sorted.
    volt[a] = (VX[label], VY[label])
    volt[b] = (-VX[label], -VY[label])
    return Transport(tuple(perm), tuple(volt))


FACTORS = tuple(factor_transport(i) for i in range(16))


@dataclass(frozen=True)
class Occurrence:
    label: int
    conjugator: Transport


def occurrence_transport(o: Occurrence) -> Transport:
    return compose(compose(inverse(o.conjugator), FACTORS[o.label]), o.conjugator)


def occurrence_edge(o: Occurrence) -> Edge:
    h_inv = inverse(o.conjugator)
    a, b = BASE_EDGES[o.label]
    return edge(h_inv.perm[a], h_inv.perm[b])


def right_move(word: list[Occurrence], i: int) -> None:
    a, b = word[i], word[i + 1]
    gb = occurrence_transport(b)
    word[i] = b
    word[i + 1] = Occurrence(a.label, compose(a.conjugator, gb))


def inverse_move(word: list[Occurrence], i: int) -> None:
    a, b = word[i], word[i + 1]
    ga = occurrence_transport(a)
    word[i] = Occurrence(b.label, compose(b.conjugator, ga))
    word[i + 1] = a


def occurrence_arc_voltage(o: Occurrence, start: int) -> tuple[int, Vector]:
    """Pull the current band arc back, oriented from current endpoint start."""
    h = o.conjugator
    hinv = inverse(h)
    original_start = h.perm[start]
    a, b = BASE_EDGES[o.label]
    assert original_start in (a, b)
    original_end = b if original_start == a else a
    end = hinv.perm[original_end]
    voltage = add(add(h.volt[start], FACTORS[o.label].volt[original_start]),
                  hinv.volt[original_end])
    return end, voltage


def collision_voltage(left: Occurrence, right: Occurrence) -> Vector:
    common = occurrence_edge(left)
    assert common == occurrence_edge(right)
    start, expected_end = common
    end_left, v_left = occurrence_arc_voltage(left, start)
    end_right, v_right = occurrence_arc_voltage(right, start)
    assert end_left == expected_end == end_right
    return add(v_left, neg(v_right))


def direct_right(a: Edge, b: Edge) -> tuple[Edge, Edge]:
    return b, conjugate(a, b)


def direct_inverse(a: Edge, b: Edge) -> tuple[Edge, Edge]:
    return conjugate(b, a), a


def run(seed: int, steps: int) -> dict:
    rng = random.Random(seed)
    word = [Occurrence(i, IDENTITY) for i in range(16)]
    equal_pairs = safe_pairs = homology_mismatches = 0
    first_bound_failure = None
    maximum_coordinate = 0
    maximum_excess = None
    first_safe = None
    started = time.perf_counter()
    for q in range(steps + 1):
        edges = [occurrence_edge(o) for o in word]
        for i in range(15):
            if edges[i] != edges[i + 1]:
                continue
            equal_pairs += 1
            safe = connected_after_delete(edges, i)
            safe_pairs += int(safe)
            voltage = collision_voltage(word[i], word[i + 1])
            nonzero = voltage != (0, 0)
            if safe != nonzero:
                homology_mismatches += 1
            coordinate = max(abs(voltage[0]), abs(voltage[1]))
            maximum_coordinate = max(maximum_coordinate, coordinate)
            excess = coordinate - (2 * q + 2)
            if maximum_excess is None or excess > maximum_excess["excess"]:
                maximum_excess = {
                    "q": q,
                    "pair_index": i,
                    "safe": safe,
                    "voltage": list(voltage),
                    "bound": 2 * q + 2,
                    "excess": excess,
                }
            if safe and first_safe is None:
                first_safe = {"q": q, "pair_index": i, "voltage": list(voltage)}
            if safe and coordinate > 2 * q + 2 and first_bound_failure is None:
                first_bound_failure = {
                    "q": q,
                    "pair_index": i,
                    "voltage": list(voltage),
                    "bound": 2 * q + 2,
                }
        if q == steps:
            break
        i = rng.randrange(15)
        sign = 1 if rng.randrange(2) else -1
        before = [occurrence_edge(o) for o in word]
        expected = (direct_right if sign == 1 else direct_inverse)(before[i], before[i + 1])
        (right_move if sign == 1 else inverse_move)(word, i)
        after = [occurrence_edge(o) for o in word]
        assert tuple(after[i:i + 2]) == expected
    return {
        "seed": seed,
        "steps": steps,
        "equal_adjacent_pairs_checked": equal_pairs,
        "safe_pairs_checked": safe_pairs,
        "safe_iff_nonzero_homology_mismatches": homology_mismatches,
        "first_safe_pair": first_safe,
        "maximum_coordinate": maximum_coordinate,
        "maximum_excess_record": maximum_excess,
        "first_safe_bound_failure": first_bound_failure,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", nargs=2, metavar=("SEED", "STEPS"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "schema": "m89-general-pullback-probe-v1",
        "status": "exact finite falsification probe; not a universal proof",
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab)",
        "method": "per-occurrence conjugators with exact all-token integral-voltage transport",
        "scope": "W_1 base torus only",
        "commit": commit,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "argv": sys.argv,
        "results": [run(int(seed), int(steps)) for seed, steps in args.case],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
