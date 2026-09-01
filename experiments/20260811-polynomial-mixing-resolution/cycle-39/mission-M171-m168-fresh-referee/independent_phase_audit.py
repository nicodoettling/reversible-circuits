#!/usr/bin/env python3
"""Clean-room exact audit of M168 at k=3,5.

The supported rank-two products and their lift multiplicities are rebuilt from
literal ordered pairs of distinct transpositions.  No predecessor module is
imported.  The direct two-step fixed-cell convolution is evaluated first; the
frozen M168 JSON is read only afterward for an exact comparison.

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for x, y in enumerate(p):
        out[y] = x
    return tuple(out)


def cycle_perm(n: int, entries: tuple[int, ...]) -> Perm:
    out = list(range(n))
    for x, y in zip(entries, entries[1:] + entries[:1]):
        out[x] = y
    return tuple(out)


def transposition(n: int, x: int, y: int) -> Perm:
    return cycle_perm(n, (x, y))


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


def cycle_sizes(p: Perm) -> tuple[int, ...]:
    return tuple(sorted(map(len, cycles(p))))


def rank(p: Perm) -> int:
    return len(p) - len(cycles(p))


@lru_cache(maxsize=None)
def completion_from_sizes(sizes: tuple[int, ...], length: int) -> int:
    if not sizes or any(d <= 0 for d in sizes):
        return 0
    if sum(sizes) - len(sizes) != length:
        return 0
    value = Fraction(math.factorial(length))
    for d in sizes:
        if d > 1:
            value *= Fraction(d ** (d - 2), math.factorial(d - 1))
    if value.denominator != 1:
        raise AssertionError((sizes, length, value))
    return value.numerator


def completion(p: Perm, length: int) -> int:
    return completion_from_sizes(cycle_sizes(p), length)


def raw_rank_two_products(n: int) -> tuple[dict[Perm, int], int]:
    edges = [transposition(n, a, b) for a, b in combinations(range(n), 2)]
    counts: collections.Counter[Perm] = collections.Counter()
    raw_pairs = 0
    for i, first in enumerate(edges):
        for j, second in enumerate(edges):
            if i == j:
                continue
            counts[compose(first, second)] += 1
            raw_pairs += 1
    return dict(counts), raw_pairs


def shifted_boundary_target(n: int, phase: int, lag: int) -> Perm:
    return compose(
        transposition(n, phase, (phase + 1) % n),
        transposition(n, (phase + lag) % n, (phase + lag + 1) % n),
    )


def orbit_key(n: int, lag: int) -> tuple[Perm, ...]:
    return tuple(sorted(shifted_boundary_target(n, phase, lag) for phase in range(n)))


def component_metadata(q: Perm):
    cs = cycles(q)
    owner: dict[int, int] = {}
    position: dict[int, int] = {}
    for i, cycle in enumerate(cs):
        for j, vertex in enumerate(cycle):
            owner[vertex] = i
            position[vertex] = j
    return cs, owner, position


def topology(
    first: tuple[int, int],
    second: tuple[int, int],
    owner: dict[int, int],
    position: dict[int, int],
) -> str:
    first_owners = {owner[x] for x in first}
    second_owners = {owner[x] for x in second}
    if len(first_owners) != 1 or len(second_owners) != 1:
        return "inadmissible"
    i = next(iter(first_owners))
    j = next(iter(second_owners))
    if i != j:
        return "X"
    ordered = sorted(first + second, key=lambda vertex: position[vertex])
    if len(set(ordered)) != 4:
        raise AssertionError("the boundary edges must be disjoint")
    index = {vertex: offset for offset, vertex in enumerate(ordered)}
    matching = {
        tuple(sorted((index[first[0]], index[first[1]]))),
        tuple(sorted((index[second[0]], index[second[1]]))),
    }
    if matching == {(0, 1), (2, 3)}:
        return "IS"
    if matching == {(0, 3), (1, 2)}:
        return "IN"
    if matching == {(0, 2), (1, 3)}:
        return "crossing"
    raise AssertionError(matching)


def replace_same_component(sizes: list[int], i: int) -> tuple[int, ...]:
    answer = [d for j, d in enumerate(sizes) if j != i]
    answer.extend((1, 1, sizes[i] - 2))
    return tuple(sorted(answer))


def replace_cross_components(sizes: list[int], i: int, j: int) -> tuple[int, ...]:
    answer = [d for a, d in enumerate(sizes) if a not in (i, j)]
    answer.extend((1, sizes[i] - 1, 1, sizes[j] - 1))
    return tuple(sorted(answer))


def qstr(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def analyze(k: int) -> dict[str, object]:
    if k not in (3, 5):
        raise ValueError("the independent audit is intentionally capped at k=3,5")
    started = time.monotonic()
    n = 3 * k
    identity = tuple(range(n))
    h = cycle_perm(n, tuple(range(n)))
    source_a = cycle_perm(n, (0, k, 2 * k))
    source_b = compose(transposition(n, 0, 1), transposition(n, k, 2 * k))

    raw_counts, raw_pair_count = raw_rank_two_products(n)
    supported = {
        state: lift
        for state, lift in raw_counts.items()
        if completion(compose(inverse(state), h), n - 3)
    }
    lift_histogram = collections.Counter(supported.values())
    if set(lift_histogram) != {2, 3}:
        raise AssertionError(lift_histogram)

    f_a = completion(compose(inverse(source_a), h), n - 3)
    f_b = completion(compose(inverse(source_b), h), n - 3)
    if supported.get(source_a) != 3 or supported.get(source_b) != 2:
        raise AssertionError("source raw-pair lifts are wrong")

    stationary_numerator = sum(
        lift * completion(compose(inverse(state), h), n - 3)
        for state, lift in supported.items()
    )
    if stationary_numerator != n ** (n - 2):
        raise AssertionError("rank-two marginal does not normalize")

    source_row_a = Fraction(0)
    source_row_b = Fraction(0)
    source_difference: dict[Perm, Fraction] = {}
    source_completion_a: dict[Perm, int] = {}
    source_completion_b: dict[Perm, int] = {}
    residuals: dict[Perm, Perm] = {}
    residual_counts: dict[Perm, int] = {}
    direct_phase_sums: dict[Perm, int] = {}
    collapsed_phase_sums: dict[Perm, int] = {}

    edge_iff_checks = 0
    ordered_pair_checks = 0
    component_count_checks = 0
    topology_counts: collections.Counter[str] = collections.Counter()

    boundary_edges = [transposition(n, r, (r + 1) % n) for r in range(n)]

    for state, lift in supported.items():
        q = compose(inverse(state), h)
        residuals[state] = q
        f_state = completion(q, n - 3)
        residual_counts[state] = f_state
        c_a = completion(compose(inverse(compose(source_a, state)), h), n - 5)
        c_b = completion(compose(inverse(compose(source_b, state)), h), n - 5)
        source_completion_a[state] = c_a
        source_completion_b[state] = c_b
        k_a = Fraction(lift * c_a, f_a)
        k_b = Fraction(lift * c_b, f_b)
        source_row_a += k_a
        source_row_b += k_b
        source_difference[state] = k_b - k_a

        cs, owner, position = component_metadata(q)
        if len(cs) != 3:
            raise AssertionError((state, cycle_sizes(q)))
        sizes = list(map(len, cs))
        generic = []
        for r in range(n):
            head = (r + 1) % n
            by_fixed_head = state[head] == head
            by_directed_edge = q[r] == head
            by_same_component = owner[r] == owner[head]
            by_rank_drop = rank(compose(boundary_edges[r], q)) == rank(q) - 1
            if len({by_fixed_head, by_directed_edge, by_same_component, by_rank_drop}) != 1:
                raise AssertionError((r, by_fixed_head, by_directed_edge, by_same_component, by_rank_drop))
            generic.append(by_fixed_head)
            edge_iff_checks += 1

        g = [0, 0, 0]
        adjacent = [0, 0, 0]
        for r in range(n):
            if generic[r]:
                g[owner[r]] += 1
            if generic[r] and generic[(r + 1) % n]:
                if owner[r] != owner[(r + 1) % n]:
                    raise AssertionError("adjacent generic edges changed component")
                adjacent[owner[r]] += 1

        direct_same = [0, 0, 0]
        direct_cross: collections.Counter[tuple[int, int]] = collections.Counter()
        direct_sum = 0
        for r in range(n):
            first_vertices = {r, (r + 1) % n}
            for lag in range(2, n - 1):
                t = (r + lag) % n
                second_vertices = {t, (t + 1) % n}
                if first_vertices & second_vertices:
                    raise AssertionError("lag range included intersecting edges")
                ordered_pair_checks += 1
                product_residual = compose(compose(boundary_edges[r], boundary_edges[t]), q)
                f_pair = completion(product_residual, n - 5)
                both_generic = generic[r] and generic[t]
                if bool(f_pair) != both_generic:
                    raise AssertionError((r, t, f_pair, generic[r], generic[t]))
                if not f_pair:
                    continue
                i, j = owner[r], owner[t]
                if i == j:
                    direct_same[i] += 1
                    predicted = replace_same_component(sizes, i)
                else:
                    direct_cross[tuple(sorted((i, j)))] += 1
                    predicted = replace_cross_components(sizes, i, j)
                if cycle_sizes(product_residual) != predicted:
                    raise AssertionError((cycle_sizes(product_residual), predicted))
                if completion_from_sizes(predicted, n - 5) != f_pair:
                    raise AssertionError("completion-size insertion mismatch")
                label = topology(
                    (r, (r + 1) % n),
                    (t, (t + 1) % n),
                    owner,
                    position,
                )
                if label not in {"IS", "IN", "X"}:
                    raise AssertionError(label)
                topology_counts[label] += 1
                direct_sum += f_pair

        collapsed_sum = 0
        for i in range(3):
            expected = g[i] * (g[i] - 1) - 2 * adjacent[i]
            if direct_same[i] != expected:
                raise AssertionError((direct_same[i], expected))
            component_count_checks += 1
            collapsed_sum += expected * completion_from_sizes(
                replace_same_component(sizes, i), n - 5
            )
        for i in range(3):
            for j in range(i + 1, 3):
                expected = 2 * g[i] * g[j]
                if direct_cross[(i, j)] != expected:
                    raise AssertionError((direct_cross[(i, j)], expected))
                component_count_checks += 1
                collapsed_sum += expected * completion_from_sizes(
                    replace_cross_components(sizes, i, j), n - 5
                )
        if direct_sum != collapsed_sum:
            raise AssertionError((direct_sum, collapsed_sum))
        direct_phase_sums[state] = direct_sum
        collapsed_phase_sums[state] = collapsed_sum

    if source_row_a != 1 or source_row_b != 1:
        raise AssertionError((source_row_a, source_row_b))
    if not all(topology_counts[label] for label in ("IS", "IN", "X")):
        raise AssertionError(topology_counts)

    ys = list(range(1, n - 2))
    z_values: list[Fraction] = []
    event_deltas: list[Fraction] = []
    cell_orbits: collections.defaultdict[tuple[Perm, ...], list[int]] = collections.defaultdict(list)
    pi_values = []
    for y in ys:
        lag = y + 1
        target_orbit = [shifted_boundary_target(n, phase, lag) for phase in range(n)]
        if len(set(target_orbit)) != n:
            raise AssertionError("target orbit is not free")
        cell_orbits[tuple(sorted(target_orbit))].append(y)
        target_weight = sum(
            raw_counts[target]
            * completion(compose(inverse(target), h), n - 3)
            for target in target_orbit
        )
        pi_y = Fraction(target_weight, n ** (n - 2))
        pi_values.append(pi_y)
        delta_y = Fraction(0)
        for state in supported:
            q = residuals[state]
            f_state = residual_counts[state]
            phase_weight = sum(
                raw_counts[target] * completion(compose(target, q), n - 5)
                for target in target_orbit
            )
            delta_y += source_difference[state] * Fraction(phase_weight, f_state)
        event_deltas.append(delta_y)
        z_values.append(delta_y / pi_y)

    if len(set(pi_values)) != 1:
        raise AssertionError("fixed-cell target mass is not constant")
    if len(cell_orbits) != (n - 3) // 2 or set(map(len, cell_orbits.values())) != {2}:
        raise AssertionError({key: value for key, value in cell_orbits.items()})

    signed_sum = sum(z_values, Fraction(0))
    direct_event = sum(event_deltas[ys.index(members[0])] for members in cell_orbits.values())
    half_formula_event = pi_values[0] * signed_sum / 2
    if direct_event != half_formula_event:
        raise AssertionError((direct_event, half_formula_event))

    f_target = completion(
        compose(inverse(shifted_boundary_target(n, 0, 2)), h), n - 3
    )
    pcs_sum = Fraction(n ** (n - 2), n * f_target) * sum(
        Fraction(supported[state] * collapsed_phase_sums[state], residual_counts[state])
        * (
            Fraction(source_completion_b[state], f_b)
            - Fraction(source_completion_a[state], f_a)
        )
        for state in supported
    )
    if pcs_sum != signed_sum:
        raise AssertionError((pcs_sum, signed_sum))

    return {
        "k": k,
        "n": n,
        "raw_ordered_distinct_transposition_pairs": raw_pair_count,
        "raw_rank_two_products": len(raw_counts),
        "supported_states": len(supported),
        "supported_lift_histogram": {str(a): b for a, b in sorted(lift_histogram.items())},
        "rank_two_stationary_normalization_exact": True,
        "source_rows_normalize_exact": True,
        "generic_edge_iff_checks": edge_iff_checks,
        "ordered_disjoint_pair_checks": ordered_pair_checks,
        "component_pair_count_checks": component_count_checks,
        "completion_size_checks": ordered_pair_checks,
        "topology_nonzero_counts": dict(sorted(topology_counts.items())),
        "all_IS_IN_X_retained": set(topology_counts) == {"IS", "IN", "X"},
        "direct_phase_sum_equals_component_moment_for_every_state": True,
        "pcs_normalization_exact": True,
        "colored_appearances_per_physical_orbit": 2,
        "distinct_physical_cell_orbits": len(cell_orbits),
        "physical_factor_one_half_exact": True,
        "target_cell_mass_exact": qstr(pi_values[0]),
        "signed_sum_exact": qstr(signed_sum),
        "signed_sum_float": float(signed_sum),
        "k_times_signed_sum_exact": qstr(k * signed_sum),
        "k_times_signed_sum_float": float(k * signed_sum),
        "physical_event_delta_exact": qstr(direct_event),
        "physical_event_delta_float": float(direct_event),
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-m168", type=Path, required=True)
    args = parser.parse_args()

    # Complete the independent reconstruction before consulting frozen output.
    results = [analyze(3), analyze(5)]
    frozen = json.loads(args.frozen_m168.read_text())
    frozen_by_k = {row["k"]: row for row in frozen["results"]}
    frozen_checks = []
    for row in results:
        match = row["signed_sum_exact"] == frozen_by_k[row["k"]]["signed_sum_exact"]
        if not match:
            raise AssertionError((row, frozen_by_k[row["k"]]))
        frozen_checks.append({"k": row["k"], "signed_sum_exact_match": True})

    payload = {
        "status": "fresh exact finite referee; no asymptotic inference",
        "target": "M168 fixed first physical cell of the M73 nonlazy cyclic rank-two quotient",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "scope_cap": [3, 5],
        "raw_pair_reconstruction": True,
        "imports_m168_code": False,
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "nonstandard_dependencies": None,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "frozen_m168_comparisons": frozen_checks,
        "results": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

