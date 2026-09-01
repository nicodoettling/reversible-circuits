#!/usr/bin/env python3
"""Fresh exact audit of M73's quotient kernel and shared-factor graph.

This implementation was written in the referee directory and does not import
M73 code. Convention: (p q)(x)=p(q(x)); tuple products are left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def transposition(n: int, i: int, j: int) -> Perm:
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def gates(n: int) -> list[Perm]:
    return [transposition(n, i, j) for i in range(n) for j in range(i + 1, n)]


def cycle_sizes(p: Perm) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for start in range(len(p)):
        if start in seen:
            continue
        x = start
        size = 0
        while x not in seen:
            seen.add(x)
            size += 1
            x = p[x]
        out.append(size)
    return out


def completion_count(p: Perm, r: int) -> int:
    sizes = cycle_sizes(p)
    if len(p) - len(sizes) != r:
        return 0
    out = math.factorial(r)
    for d in sizes:
        if d > 1:
            out = out * d ** (d - 2) // math.factorial(d - 1)
    return out


def rotate(p: Perm, h: Perm, h_inv: Perm) -> Perm:
    return mul(h_inv, mul(p, h))


def tv(row: list[Fraction], other: list[Fraction]) -> Fraction:
    return sum((abs(x - y) for x, y in zip(row, other)), Fraction()) / 2


def audit_n(n: int) -> dict[str, object]:
    if n < 5 or n % 2 == 0:
        raise ValueError("n must be odd and at least five")
    h = tuple((i + 1) % n for i in range(n))
    h_inv = inv(h)
    ts = gates(n)

    lifts: collections.Counter[Perm] = collections.Counter()
    lift_pairs: list[tuple[Perm, Perm, Perm]] = []
    for a in ts:
        for b in ts:
            g = mul(a, b)
            lifts[g] += 1
            lift_pairs.append((a, b, g))

    marginal: dict[Perm, int] = {}
    for g, a_g in lifts.items():
        value = a_g * completion_count(mul(inv(g), h), n - 3)
        if value:
            marginal[g] = value
    if sum(marginal.values()) != n ** (n - 2):
        raise AssertionError("one-coordinate law failed to normalize")

    orbit_of: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for g in sorted(marginal):
        if g in orbit_of:
            continue
        orbit: list[Perm] = []
        x = g
        while x not in orbit:
            orbit.append(x)
            x = rotate(x, h, h_inv)
        if x != g:
            raise AssertionError("cyclic orbit failed to return to source")
        oid = len(orbits)
        for x in orbit:
            if x in orbit_of:
                raise AssertionError("cyclic orbits overlapped")
            orbit_of[x] = oid
        orbits.append(orbit)

    q = len(orbits)
    z = n ** (n - 2)
    pi = [Fraction(len(o) * marginal[o[0]], z) for o in orbits]
    kernel = [[Fraction() for _ in range(q)] for _ in range(q)]
    for i, orbit in enumerate(orbits):
        g = orbit[0]
        denominator = completion_count(mul(inv(g), h), n - 3)
        for s in marginal:
            kernel[i][orbit_of[s]] += Fraction(
                lifts[s] * completion_count(mul(inv(mul(g, s)), h), n - 5),
                denominator,
            )
        if sum(kernel[i], Fraction()) != 1:
            raise AssertionError("quotient row failed to normalize")
    if sum(pi, Fraction()) != 1:
        raise AssertionError("orbit masses failed to normalize")
    if any(pi[i] * kernel[i][j] != pi[j] * kernel[j][i]
           for i in range(q) for j in range(q)):
        raise AssertionError("quotient detailed balance failed")

    squared = [[sum((kernel[i][k] * kernel[k][j] for k in range(q)), Fraction())
                for j in range(q)] for i in range(q)]

    tokens: dict[tuple[int, Perm], set[int]] = collections.defaultdict(set)
    for a, b, product in lift_pairs:
        if product in orbit_of:
            tokens[(0, a)].add(orbit_of[product])
            tokens[(1, b)].add(orbit_of[product])
    adjacency = [set() for _ in range(q)]
    for source_set in tokens.values():
        source_list = sorted(source_set)
        for offset, i in enumerate(source_list):
            for j in source_list[offset + 1:]:
                adjacency[i].add(j)
                adjacency[j].add(i)

    adjacent_max = Fraction(-1)
    adjacent_witness: tuple[int, int] | None = None
    edge_count = 0
    for i in range(q):
        for j in adjacency[i]:
            if j <= i:
                continue
            edge_count += 1
            distance = tv(squared[i], squared[j])
            if distance > adjacent_max:
                adjacent_max = distance
                adjacent_witness = (i, j)

    diameter = 0
    for source in range(q):
        distance = [-1] * q
        distance[source] = 0
        queue = collections.deque([source])
        while queue:
            i = queue.popleft()
            for j in adjacency[i]:
                if distance[j] < 0:
                    distance[j] = distance[i] + 1
                    queue.append(j)
        if -1 in distance:
            raise AssertionError("shared-factor graph disconnected")
        diameter = max(diameter, max(distance))

    # Independently test the constructive chord placement in Proposition 8.1:
    # every ordered chord pair a,d has a rotation d_r for which a*d_r is in X.
    constructive_failures = 0
    for a in ts:
        for d in ts:
            rotated = d
            found = False
            for _ in range(n):
                if mul(a, rotated) in marginal:
                    found = True
                    break
                rotated = rotate(rotated, h, h_inv)
            if not found:
                constructive_failures += 1
    if constructive_failures:
        raise AssertionError("constructive diameter chord placement failed")

    # Exact first-edge/Borel identity through all component sizes <=n.
    borel_checks = 0
    for d in range(2, n + 1):
        convolution = sum((Fraction(u ** (u - 1) * (d-u) ** (d-u-1),
                                    math.factorial(u) * math.factorial(d-u))
                           for u in range(1, d)), Fraction())
        for u in range(1, d):
            conditional = Fraction(u ** (u - 1) * (d-u) ** (d-u-1),
                                   math.factorial(u) * math.factorial(d-u)) / convolution
            # There are d oriented anchors for gap u; the fair orientation
            # contributes 1/2. This includes the even d,u=d/2 case, where
            # the d anchors represent d/2 unoriented chords twice.
            cayley = Fraction(d, 2) * Fraction(
                math.factorial(d - 2) * u ** (u - 1) * (d-u) ** (d-u-1),
                math.factorial(u) * math.factorial(d-u) * d ** (d - 2),
            )
            if conditional != cayley:
                raise AssertionError("conditioned-Borel identity failed")
            borel_checks += 1

    return {
        "n": n,
        "product_support": len(marginal),
        "quotient_states": q,
        "exact_normalization": True,
        "exact_reversibility": True,
        "shared_factor_edges": edge_count,
        "shared_factor_graph_diameter": diameter,
        "constructive_chord_pairs_checked": len(ts) ** 2,
        "constructive_chord_placement_failures": constructive_failures,
        "conditioned_borel_entries_checked": borel_checks,
        "maximum_adjacent_K2_TV_exact": str(adjacent_max),
        "maximum_adjacent_K2_TV_witness_orbits": list(adjacent_witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[5, 7, 9])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_scope": "fresh exact audit of M73 quotient kernel and shared-factor graph",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(__import__("sys").argv),
        "results": [audit_n(n) for n in args.n],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
