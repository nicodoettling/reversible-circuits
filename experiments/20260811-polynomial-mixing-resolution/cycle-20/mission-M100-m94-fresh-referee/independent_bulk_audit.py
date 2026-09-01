#!/usr/bin/env python3
"""Fresh audit of M94's central-double reduction.

This program imports no M94 or predecessor implementation.  It reconstructs
the literal ordered-transposition-pair marginal, the cyclic quotient kernel,
the two-step signed row, the Borel/tree-weight convolution, and the central
double event over ``Fraction`` for k=3,5.  It also checks the retained compact
k=11 payload arithmetically and evaluates finite Abel diagnostics.  Finite
checks are not asymptotic proofs.

Convention: (pq)(x)=p(q(x)); tuple factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


Perm = tuple[int, ...]
Vector = list[Fraction]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    out = list(range(n))
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def cycle_permutation(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def cycles(p: Perm) -> list[list[int]]:
    seen: set[int] = set()
    answer: list[list[int]] = []
    for start in range(len(p)):
        if start in seen:
            continue
        block: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            block.append(x)
            x = p[x]
        answer.append(block)
    return answer


def transposition_length(p: Perm) -> int:
    return len(p) - len(cycles(p))


def minimal_factorization_count(p: Perm, length: int) -> int:
    blocks = cycles(p)
    if len(p) - len(blocks) != length:
        return 0
    numerator = math.factorial(length)
    denominator = 1
    for block in blocks:
        d = len(block)
        if d > 1:
            numerator *= d ** (d - 2)
            denominator *= math.factorial(d - 1)
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def tree_weight(p: Perm, length: int) -> Fraction:
    return Fraction(minimal_factorization_count(p, length), math.factorial(length))


def theta(p: Perm, h: Perm) -> Perm:
    return compose(inverse(h), compose(p, h))


def kind(p: Perm) -> str:
    nontrivial = sorted(len(block) for block in cycles(p) if len(block) > 1)
    if nontrivial == [3]:
        return "T"
    if nontrivial == [2, 2]:
        return "D"
    raise AssertionError(nontrivial)


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


def row_times_kernel(row: Vector, kernel: list[Vector]) -> Vector:
    dimension = len(row)
    return [
        sum((row[source] * kernel[source][target] for source in range(dimension)), Fraction(0))
        for target in range(dimension)
    ]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def tau(d: int) -> Fraction:
    return Fraction(d ** (d - 1), math.factorial(d))


def event_mass_formula(n: int, threshold: int) -> Fraction:
    total = Fraction(0)
    for x in range(threshold, n + 1):
        for y in range(threshold, n - x + 1):
            for z in range(threshold, n - x - y + 1):
                w = n - x - y - z
                if w >= threshold:
                    total += tau(x) * tau(z) * tau(y + w)
    return Fraction(n * math.factorial(n - 3), n ** (n - 2)) * total


def construct_exact(k: int) -> dict[str, Any]:
    if k < 3 or k % 2 == 0:
        raise ValueError("k must be odd and at least three")
    n = 3 * k
    h = cycle_permutation(n, tuple(range(n)))
    gates = [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]
    lifts: collections.Counter[Perm] = collections.Counter()
    for first in gates:
        for second in gates:
            lifts[compose(first, second)] += 1

    f3: dict[Perm, int] = {}
    t3: dict[Perm, Fraction] = {}
    for state, multiplicity in lifts.items():
        residual = compose(inverse(state), h)
        count = minimal_factorization_count(residual, n - 3)
        if count:
            assert multiplicity in (2, 3)
            assert (kind(state), multiplicity) in (("T", 3), ("D", 2))
            f3[state] = count
            t3[state] = tree_weight(residual, n - 3)
            assert count == math.factorial(n - 3) * t3[state]

    orbit_id: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for state in sorted(f3):
        if state in orbit_id:
            continue
        orbit: list[Perm] = []
        current = state
        while current not in orbit:
            assert current in f3
            orbit.append(current)
            current = theta(current, h)
        assert current == state
        index = len(orbits)
        for member in orbit:
            assert member not in orbit_id
            orbit_id[member] = index
        orbits.append(orbit)

    dimension = len(orbits)
    kernel = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    raw_states = list(f3)
    r_n = (n - 3) * (n - 4)
    borel_kernel_checks = 0
    for source_index, orbit in enumerate(orbits):
        source = orbit[0]
        denominator = f3[source]
        for target in raw_states:
            residual = compose(inverse(compose(source, target)), h)
            f5 = minimal_factorization_count(residual, n - 5)
            if not f5:
                continue
            direct = Fraction(lifts[target] * f5, denominator)
            t5 = tree_weight(residual, n - 5)
            borel = Fraction(lifts[target], r_n) * t5 / t3[source]
            assert direct == borel
            kernel[source_index][orbit_id[target]] += direct
            borel_kernel_checks += 1
        assert sum(kernel[source_index], Fraction(0)) == 1

    z_n = n ** (n - 2)
    stationary = [
        Fraction(len(orbit) * lifts[orbit[0]] * f3[orbit[0]], z_n)
        for orbit in orbits
    ]
    assert sum(stationary, Fraction(0)) == 1
    for i in range(dimension):
        for j in range(dimension):
            assert stationary[i] * kernel[i][j] == stationary[j] * kernel[j][i]

    a = cycle_permutation(n, (0, k, 2 * k))
    b = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))
    ai, bi = orbit_id[a], orbit_id[b]
    assert len(orbits[ai]) == k
    assert len(orbits[bi]) == n
    assert all(len(orbit) == n for orbit in orbits if kind(orbit[0]) == "D")

    eta = [kernel[bi][j] - kernel[ai][j] for j in range(dimension)]
    delta = row_times_kernel(eta, kernel)
    assert sum(delta, Fraction(0)) == 0
    score = [delta[j] / stationary[j] for j in range(dimension)]
    ba2 = sum((stationary[j] * score[j] ** 2 for j in range(dimension)), Fraction(0))
    tv = sum((abs(value) for value in delta), Fraction(0)) / 2

    threshold = (k + 1) // 2
    event = [
        index
        for index, orbit in enumerate(orbits)
        if kind(orbit[0]) == "D" and min(support_gaps(orbit[0])) >= threshold
    ]
    event_raw = [member for index in event for member in orbits[index]]
    event_mass = sum((stationary[index] for index in event), Fraction(0))
    event_delta = sum((delta[index] for index in event), Fraction(0))
    event_l2 = sum((delta[index] ** 2 / stationary[index] for index in event), Fraction(0))
    event_cauchy = event_delta ** 2 / event_mass
    assert event_mass == event_mass_formula(n, threshold)
    expected_event_orbits = math.comb(n - 4 * threshold + 3, 3) // 2
    assert len(event) == expected_event_orbits
    assert event_cauchy <= event_l2 <= ba2

    def joint_tree(first: Perm, second: Perm) -> Fraction:
        residual = compose(inverse(compose(first, second)), h)
        return tree_weight(residual, n - 5)

    d_tau: dict[Perm, Fraction] = {
        state: joint_tree(b, state) / t3[b] - joint_tree(a, state) / t3[a]
        for state in raw_states
    }

    def convolution_score(target_index: int) -> Fraction:
        target = orbits[target_index][0]
        orbit = orbits[target_index]
        total = Fraction(0)
        for state in raw_states:
            q = sum((joint_tree(state, target_lift) for target_lift in orbit), Fraction(0)) / len(orbit)
            total += lifts[state] * d_tau[state] * q / t3[state]
        return Fraction(z_n, math.factorial(n - 3) * r_n * r_n) * total / t3[target]

    if k == 3:
        checked_targets = list(range(dimension))
    else:
        triangle = next(i for i, orbit in enumerate(orbits) if kind(orbit[0]) == "T" and i != ai)
        double = next(i for i, orbit in enumerate(orbits) if kind(orbit[0]) == "D" and i not in event)
        checked_targets = sorted(set([ai, bi, triangle, double] + event[:2]))
    for target_index in checked_targets:
        assert convolution_score(target_index) == score[target_index]

    event_convolution = Fraction(0)
    for state in raw_states:
        positive_target_sum = sum(
            (lifts[target] * joint_tree(state, target) for target in event_raw),
            Fraction(0),
        )
        event_convolution += lifts[state] * d_tau[state] * positive_target_sum / t3[state]
    event_convolution /= r_n * r_n
    assert event_convolution == event_delta

    shell_mass: collections.defaultdict[int, Fraction] = collections.defaultdict(Fraction)
    for index, orbit in enumerate(orbits):
        residual = compose(inverse(orbit[0]), h)
        minimum = min(len(block) for block in cycles(residual))
        shell_mass[minimum] += stationary[index]
    assert set(shell_mass).issubset(set(range(1, k + 1)))

    return {
        "k": k,
        "n": n,
        "raw_states": len(raw_states),
        "quotient_states": dimension,
        "borel_raw_kernel_entries_checked": borel_kernel_checks,
        "source_orbit_sizes_A_B": [len(orbits[ai]), len(orbits[bi])],
        "convolution_target_orbits_checked": len(checked_targets),
        "event_orbits": len(event),
        "event_stationary_mass": fraction_text(event_mass),
        "event_signed_two_step_difference": fraction_text(event_delta),
        "event_BA2_contribution": fraction_text(event_l2),
        "event_partition_BA2_lower_bound": fraction_text(event_cauchy),
        "actual_BA2_L2": fraction_text(ba2),
        "actual_two_step_TV": fraction_text(tv),
        "scaled_float": {
            "k_pi_E": float(k * event_mass),
            "k2_Delta_E": float(k * k * event_delta),
            "k4_event_L2": float(k ** 4 * event_l2),
            "k4_event_Cauchy": float(k ** 4 * event_cauchy),
            "k4_BA2": float(k ** 4 * ba2),
            "k2_TV": float(k * k * tv),
        },
        "shell_stationary_mass": {
            str(d): fraction_text(mass) for d, mass in sorted(shell_mass.items())
        },
        "checks": {
            "raw_Borel_kernel": True,
            "quotient_rows_and_detailed_balance": True,
            "short_A_orbit_and_double_orbits": True,
            "orbit_aware_score_convolution": True,
            "event_convolution": True,
            "event_composition_mass": True,
            "stationary_Cauchy": True,
        },
    }


def log_b(d: int) -> float:
    return -d + (d - 1) * math.log(d) - math.lgamma(d + 1)


def split_laws(k: int) -> tuple[list[float], list[float]]:
    p = [0.0] * k
    q = [0.0] * k
    long = 2 * k - 1
    for s in range(1, k):
        p[s] = math.exp(log_b(s) + log_b(long - s) - log_b(long)) / (1 - 1 / long)
        if s <= (k - 1) // 2:
            q[s] = math.exp(log_b(s) + log_b(k - s) - log_b(k)) / (1 - 1 / k)
    assert abs(sum(p) - 1.0) < 2e-10
    assert abs(sum(q) - 1.0) < 2e-10
    return p, q


def simpson(function, left: float, right: float, panels: int = 40000) -> float:
    if left == right:
        return 0.0
    if panels % 2:
        panels += 1
    step = (right - left) / panels
    total = function(left) + function(right)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(left + index * step)
    return total * step / 3


def abel_limit(x: float) -> float:
    c = 1 / math.sqrt(2 * math.pi)

    def transformed_both(t: float) -> float:
        if t == 0:
            return -1.5 * c
        y = t * t
        p = c * y ** -1.5 * (1 - y / 2) ** -1.5
        q = c * y ** -1.5 * (1 - y) ** -1.5
        return 2 * t * (p - q)

    def transformed_p(t: float) -> float:
        y = t * t
        return 2 * t * c * y ** -1.5 * (1 - y / 2) ** -1.5

    cutoff = min(x, 0.5)
    value = simpson(transformed_both, 0.0, math.sqrt(cutoff))
    if x > 0.5:
        value += simpson(transformed_p, math.sqrt(0.5), math.sqrt(x))
    return value


def abel_diagnostics() -> list[dict[str, Any]]:
    answer = []
    c = 1 / math.sqrt(2 * math.pi)
    limits = {x: abel_limit(x) for x in (0.25, 0.75)}
    for k in (101, 401, 1601):
        p, q = split_laws(k)
        cumulative: list[float] = []
        running = 0.0
        for s in range(1, k):
            running += p[s] - q[s]
            cumulative.append(running)
        u = int(math.sqrt(k))
        boundary_prediction = -1.5 * c * math.sqrt(u) / k
        answer.append({
            "k": k,
            "bulk": {
                str(x): {
                    "sqrt_k_D": math.sqrt(k) * cumulative[math.floor(k * x) - 1],
                    "integral_limit": limits[x],
                }
                for x in limits
            },
            "boundary_u": u,
            "boundary_D": cumulative[u - 1],
            "boundary_prediction": boundary_prediction,
            "boundary_ratio": cumulative[u - 1] / boundary_prediction,
            "maximum_positive_D": max(cumulative),
            "endpoint_D": cumulative[-1],
        })
    return answer


def check_compact(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text())
    checks = []
    for row in payload["results"]:
        k = int(row["k"])
        n = int(row["n"])
        event = row["central_event"]
        complete = row["complete_kernel"]
        mass_formula = event_mass_formula(n, int(event["threshold"]))
        expected_orbits = math.comb(n - 4 * int(event["threshold"]) + 3, 3) // 2
        tolerance = 5e-12
        assert abs(float(mass_formula) - event["stationary_mass"]) < tolerance
        assert event["orbit_count"] == expected_orbits
        assert abs(k * event["stationary_mass"] - event["k_times_stationary_mass"]) < tolerance
        assert abs(k * k * event["signed_delta"] - event["k_squared_signed_delta"]) < tolerance
        assert abs(k ** 4 * event["l2_contribution"] - event["k_fourth_l2_contribution"]) < tolerance
        cauchy = event["signed_delta"] ** 2 / event["stationary_mass"]
        assert abs(cauchy - event["cauchy_partition_lower_bound"]) < tolerance
        assert abs(k ** 4 * cauchy - event["k_fourth_cauchy_partition_lower_bound"]) < tolerance
        assert event["cauchy_partition_lower_bound"] <= event["l2_contribution"] + tolerance
        assert abs(complete["stationary_mass_sum"] - 1.0) < tolerance
        assert abs(complete["signed_delta_sum"]) < tolerance
        assert abs(complete["summed_BA2_L2"] - complete["actual_BA2_L2"]) < tolerance
        assert abs(complete["summed_two_step_TV"] - complete["actual_two_step_TV"]) < tolerance
        assert abs(k ** 4 * complete["actual_BA2_L2"] - complete["k_fourth_actual_BA2_L2"]) < tolerance
        assert abs(k * k * complete["actual_two_step_TV"] - complete["k_squared_actual_two_step_TV"]) < tolerance
        checks.append({
            "k": k,
            "event_mass_formula": fraction_text(mass_formula),
            "event_mass_formula_float": float(mass_formula),
            "event_orbit_count_formula": expected_orbits,
            "compact_arithmetic_consistent": True,
            "source_file_retained": (path.parent / row["source_file"]).exists(),
            "source_sha256_recorded": row["source_sha256"],
        })
    return {
        "path": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "rows": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", nargs="+", type=int, default=[3, 5])
    parser.add_argument("--compact", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "fresh_exact_finite_and_formula_audit_not_asymptotic_evidence",
        "target": "M94 central-double obstruction reduction for balanced BA2",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "exact_results": [construct_exact(k) for k in args.k],
        "abel_finite_diagnostics": abel_diagnostics(),
        "compact_check": check_compact(args.compact),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "exact": [row["scaled_float"] for row in payload["exact_results"]],
        "compact": payload["compact_check"]["rows"],
        "abel": payload["abel_finite_diagnostics"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
