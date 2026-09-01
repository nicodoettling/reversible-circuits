#!/usr/bin/env python3
"""Exact falsifier for the M73 cyclic gap and four-schema formulas.

Convention: (p q)(x)=p(q(x)); factor tuples multiply left-to-right.
All probability comparisons use fractions.Fraction.
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
from pathlib import Path


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def cycle_perm(n: int, cycle: tuple[int, ...]) -> Perm:
    p = list(range(n))
    if len(cycle) > 1:
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            p[x] = y
    return tuple(p)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


def transpositions(n: int) -> list[Perm]:
    return [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]


def cycles(p: Perm) -> list[tuple[int, ...]]:
    seen: set[int] = set()
    answer = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        answer.append(tuple(cycle))
    return answer


def cycle_lengths(p: Perm) -> tuple[int, ...]:
    return tuple(sorted((len(c) for c in cycles(p)), reverse=True))


def moved_points(p: Perm) -> frozenset[int]:
    return frozenset(x for x, y in enumerate(p) if x != y)


def minimal_count(p: Perm, length: int) -> int:
    lengths = cycle_lengths(p)
    if len(p) - len(lengths) != length:
        return 0
    answer = math.factorial(length)
    for d in lengths:
        if d > 1:
            answer *= d ** (d - 2)
            answer //= math.factorial(d - 1)
    return answer


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def pair_counts(n: int) -> dict[Perm, int]:
    answer: collections.Counter[Perm] = collections.Counter()
    gates = transpositions(n)
    for u in gates:
        for v in gates:
            answer[compose(u, v)] += 1
    return dict(answer)


def theta(p: Perm, h: Perm, h_inv: Perm) -> Perm:
    return compose(h_inv, compose(p, h))


def orbit(p: Perm, h: Perm, h_inv: Perm) -> list[Perm]:
    answer = []
    current = p
    while current not in answer:
        answer.append(current)
        current = theta(current, h, h_inv)
    if current != p:
        raise AssertionError("theta trajectory did not close at its source")
    return answer


def kind_and_edges(p: Perm) -> tuple[str, list[frozenset[int]]]:
    nontrivial = [c for c in cycles(p) if len(c) > 1]
    lengths = sorted(len(c) for c in nontrivial)
    if lengths == [3]:
        return "3", []
    if lengths == [2, 2]:
        return "D", [frozenset(c) for c in nontrivial]
    raise AssertionError(f"unexpected rank-two state with cycle sizes {lengths}")


def local_first_edge_probability(component: Perm, edge: frozenset[int]) -> Fraction:
    vertices = next(c for c in cycles(component) if len(c) > 1)
    d = len(vertices)
    x, y = sorted(edge)
    remainder = compose(transposition(len(component), x, y), component)
    return Fraction(minimal_count(remainder, d - 2), d ** (d - 2))


def schema_probability(
    source: Perm,
    target: Perm,
    h: Perm,
    lifts: dict[Perm, int],
) -> Fraction:
    q = compose(inverse(source), h)
    component_cycles = cycles(q)
    components = [cycle_perm(len(q), c) for c in component_cycles]
    sizes = [len(c) for c in component_cycles]
    ranks = [d - 1 for d in sizes]
    total_rank = sum(ranks)
    denominator = total_rank * (total_rank - 1)
    target_support = moved_points(target)
    answer = Fraction(0)

    # Same residual-cycle schemas I3, IS, IN.
    for component, vertices, d, rank in zip(
        components, component_cycles, sizes, ranks
    ):
        if d < 3 or not target_support.issubset(vertices):
            continue
        local_completion = minimal_count(
            compose(inverse(target), component), d - 3
        )
        local_pair_probability = Fraction(
            lifts[target] * local_completion, d ** (d - 2)
        )
        answer += Fraction(rank * (rank - 1), denominator) * local_pair_probability

    # Cross-residual-cycle schema X.
    target_kind, edges = kind_and_edges(target)
    if target_kind == "D":
        for i in range(len(components)):
            for j in range(i + 1, len(components)):
                if ranks[i] == 0 or ranks[j] == 0:
                    continue
                edge_i = [e for e in edges if e.issubset(component_cycles[i])]
                edge_j = [e for e in edges if e.issubset(component_cycles[j])]
                if len(edge_i) != 1 or len(edge_j) != 1:
                    continue
                probability = (
                    Fraction(2 * ranks[i] * ranks[j], denominator)
                    * local_first_edge_probability(components[i], edge_i[0])
                    * local_first_edge_probability(components[j], edge_j[0])
                )
                answer += probability
    return answer


def frac(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def analyze(n: int) -> dict[str, object]:
    if n < 5 or n % 2 == 0:
        raise ValueError("n must be odd and at least five")
    h = tuple((x + 1) % n for x in range(n))
    h_inv = inverse(h)
    lifts = pair_counts(n)
    total = n ** (n - 2)
    marginal_counts: dict[Perm, int] = {}
    for g, multiplicity in lifts.items():
        completion = minimal_count(compose(inverse(g), h), n - 3)
        if completion:
            marginal_counts[g] = multiplicity * completion
    support = sorted(marginal_counts)
    if sum(marginal_counts.values()) != total:
        raise AssertionError("marginal count failed to normalize")

    seen: set[Perm] = set()
    orbit_count = 0
    short_three_orbits = 0
    complement_checks = 0
    stationary_checks = 0
    kind_counts: collections.Counter[str] = collections.Counter()
    kind_masses: collections.Counter[str] = collections.Counter()

    for g in support:
        state_kind, _ = kind_and_edges(g)
        kind_counts[state_kind] += 1
        kind_masses[state_kind] += Fraction(marginal_counts[g], total)
        q_sizes = cycle_lengths(compose(inverse(g), h))
        points = sorted(moved_points(g))
        if state_kind == "3":
            if g != cycle_perm(n, tuple(points)):
                raise AssertionError("admissible three-cycle had reverse orientation")
            x = points[1] - points[0]
            y = points[2] - points[1]
            z = n - points[2] + points[0]
            gaps = (x, y, z)
            predicted_sizes = tuple(sorted(gaps, reverse=True))
            stabilizer = 3 if x == y == z else 1
            predicted_orbit_size = n // stabilizer
            raw_mass = Fraction(
                3 * math.factorial(n - 3), total
            )
            for d in gaps:
                raw_mass *= tau(d)
            if x == y == z:
                short_three_orbits += int(g not in seen)
        else:
            p0, p1, p2, p3 = points
            x, y, z = p1 - p0, p2 - p1, p3 - p2
            w = n - p3 + p0
            edges = {frozenset(c) for c in cycles(g) if len(c) == 2}
            separated = {frozenset((p0, p1)), frozenset((p2, p3))}
            nested = {frozenset((p0, p3)), frozenset((p1, p2))}
            if edges == separated:
                predicted_sizes = tuple(sorted((x, z, y + w), reverse=True))
            elif edges == nested:
                predicted_sizes = tuple(sorted((x + z, y, w), reverse=True))
            else:
                raise AssertionError("crossing double transposition entered support")
            predicted_orbit_size = n
            raw_mass = Fraction(
                2 * math.factorial(n - 3), total
            )
            for d in predicted_sizes:
                raw_mass *= tau(d)
        if q_sizes != predicted_sizes:
            raise AssertionError(("complement gap mismatch", g, q_sizes, predicted_sizes))
        complement_checks += 1
        actual_raw_mass = Fraction(marginal_counts[g], total)
        if raw_mass != actual_raw_mass:
            raise AssertionError(("stationary gap weight mismatch", g))
        stationary_checks += 1
        if g not in seen:
            members = orbit(g, h, h_inv)
            if len(members) != predicted_orbit_size:
                raise AssertionError(("orbit-size mismatch", g, len(members), predicted_orbit_size))
            if any(x not in marginal_counts for x in members):
                raise AssertionError("theta orbit left support")
            seen.update(members)
            orbit_count += 1

    if kind_masses["3"] != Fraction(3, n):
        raise AssertionError("three-cycle total mass was not 3/n")
    if kind_masses["D"] != Fraction(n - 3, n):
        raise AssertionError("double total mass was not (n-3)/n")

    row_entry_checks = 0
    collapsed_checks = 0
    for g in support:
        denominator = minimal_count(compose(inverse(g), h), n - 3)
        row_sum = Fraction(0)
        three_mass = Fraction(0)
        for s in support:
            direct = Fraction(
                lifts[s]
                * minimal_count(compose(inverse(compose(g, s)), h), n - 5),
                denominator,
            )
            schema = schema_probability(g, s, h, lifts)
            if direct != schema:
                raise AssertionError(("four-schema row mismatch", g, s, direct, schema))
            row_entry_checks += 1
            row_sum += direct
            if kind_and_edges(s)[0] == "3":
                three_mass += direct
        if row_sum != 1:
            raise AssertionError(("row failed to normalize", g, row_sum))
        residual_sizes = [len(c) for c in cycles(compose(inverse(g), h))]
        harmonic_sum = sum((Fraction(1, d) for d in residual_sizes), Fraction(0))
        predicted_three_mass = Fraction(3, (n - 3) * (n - 4)) * (
            n - 9 + 2 * harmonic_sum
        )
        if three_mass != predicted_three_mass:
            raise AssertionError(("collapsed kind formula mismatch", g))
        collapsed_checks += 1

    return {
        "n": n,
        "support_size": len(support),
        "orbit_count": orbit_count,
        "kind_state_counts": dict(kind_counts),
        "kind_stationary_masses": {key: frac(value) for key, value in kind_masses.items()},
        "short_balanced_three_orbits": short_three_orbits,
        "complement_gap_checks": complement_checks,
        "stationary_gap_weight_checks": stationary_checks,
        "four_schema_row_entry_checks": row_entry_checks,
        "collapsed_kind_checks": collapsed_checks,
        "all_checks_passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[5, 7])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "unavailable"
    payload = {
        "status": "exact_finite_falsification_only",
        "claim_scope": "gap stationary formulas, orbit sizes, and four-schema row identity",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right; theta(g)=h^-1 g h",
        "command": "python3 -B gap_schema_verifier.py --n " + " ".join(map(str, args.n)),
        "python": platform.python_version(),
        "repository_commit": commit,
        "results": [analyze(n) for n in args.n],
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
