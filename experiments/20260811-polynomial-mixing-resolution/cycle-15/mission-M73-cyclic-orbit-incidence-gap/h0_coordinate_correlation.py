#!/usr/bin/env python3
"""Exact H0 product-coordinate correlation kernel for minimal long cycles.

For odd n=2l+1 and h=(0 1 ... n-1), group the n-1 raw transpositions into
l ordered pair-products G_i.  This script constructs M16's forward
correlation operator

    K(g,s) = Pr(G_j=s | G_i=g),  i<j,

on functions of one pair-product, then restricts it to functions invariant
under theta(g)=h^{-1}gh.  All kernel and detailed-balance arithmetic is exact.
Only the final eigenvalue calculation is floating point.

The count uses no state enumeration.  If q has transposition length k, its
number of length-k transposition factorizations is

    k! prod_{cycles C, |C|>1} |C|^(|C|-2) / (|C|-1)!.

This is the independent Dénes factorization of each disjoint cycle followed
by an interleaving.  Minimality of h forces every nonzero completion after
one or two fixed pair-products to be minimal as well.

Convention: (p q)(x)=p(q(x)); tuples multiply left-to-right.
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

import numpy as np


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: Perm) -> Perm:
    answer = [0] * len(p)
    for x, y in enumerate(p):
        answer[y] = x
    return tuple(answer)


def transpositions(n: int) -> list[Perm]:
    answer = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append(tuple(p))
    return answer


def cycle_lengths(p: Perm) -> tuple[int, ...]:
    seen = set()
    lengths = []
    for start in range(len(p)):
        if start in seen:
            continue
        length = 0
        x = start
        while x not in seen:
            seen.add(x)
            length += 1
            x = p[x]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def nontrivial_cycles(p: Perm) -> list[list[int]]:
    seen = set()
    cycles = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        if len(cycle) > 1:
            cycles.append(cycle)
    return cycles


def canonical_cyclic_rotation(values: tuple[int, ...]) -> tuple[int, ...]:
    return min(values[offset:] + values[:offset] for offset in range(len(values)))


def circular_support_gaps(p: Perm) -> tuple[int, ...]:
    moved = sorted(x for x in range(len(p)) if p[x] != x)
    gaps = tuple(
        (moved[(index + 1) % len(moved)] - moved[index]) % len(p)
        for index in range(len(moved))
    )
    return canonical_cyclic_rotation(gaps)


def increment_kind(p: Perm) -> str:
    lengths = sorted(len(cycle) for cycle in nontrivial_cycles(p))
    if lengths == [3]:
        return "oriented_3_cycle"
    if lengths == [2, 2]:
        return "noncrossing_double_transposition"
    return str(lengths)


def increment_descriptor(p: Perm, h: Perm) -> dict[str, object]:
    complement = compose(inverse(p), h)
    return {
        "kind": increment_kind(p),
        "cycles": nontrivial_cycles(p),
        "support_circular_gaps_canonical": list(circular_support_gaps(p)),
        "complement_cycle_sizes_sorted": list(cycle_lengths(complement)),
    }


def gap_parameter(p: Perm) -> dict[str, object]:
    """Canonical cyclic-composition parameter, including double color."""
    n = len(p)
    moved = sorted(x for x in range(n) if p[x] != x)
    gaps = tuple(
        (moved[(index + 1) % len(moved)] - moved[index]) % n
        for index in range(len(moved))
    )
    kind = increment_kind(p)
    if kind == "oriented_3_cycle":
        rotations = [gaps[offset:] + gaps[:offset] for offset in range(3)]
        return {"cyclic_composition": list(min(rotations)), "color": "3"}
    if kind != "noncrossing_double_transposition":
        raise AssertionError("gap parameter requested outside rank-two support")
    edges = {
        frozenset(cycle)
        for cycle in nontrivial_cycles(p)
    }
    p0, p1, p2, p3 = moved
    separated = {frozenset((p0, p1)), frozenset((p2, p3))}
    nested = {frozenset((p0, p3)), frozenset((p1, p2))}
    if edges == separated:
        base_color = "S"
    elif edges == nested:
        base_color = "N"
    else:
        raise AssertionError("crossing matching entered rank-two support")
    encodings = []
    for offset in range(4):
        rotated = gaps[offset:] + gaps[:offset]
        color = base_color if offset % 2 == 0 else ("N" if base_color == "S" else "S")
        encodings.append((rotated, color))
    composition, color = min(encodings)
    return {"cyclic_composition": list(composition), "color": color}


def minimal_factorization_count(p: Perm, length: int) -> int:
    lengths = cycle_lengths(p)
    if len(p) - len(lengths) != length:
        return 0
    answer = math.factorial(length)
    for size in lengths:
        if size > 1:
            answer *= size ** (size - 2)
            answer //= math.factorial(size - 1)
    return answer


def pair_product_multiplicities(n: int) -> dict[Perm, int]:
    counts: collections.Counter[Perm] = collections.Counter()
    gates = transpositions(n)
    for first in gates:
        for second in gates:
            counts[compose(first, second)] += 1
    return dict(counts)


def theta(p: Perm, h: Perm, h_inverse: Perm) -> Perm:
    return compose(h_inverse, compose(p, h))


def rational_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def analyze(n: int) -> dict[str, object]:
    if n < 5 or n % 2 == 0:
        raise ValueError("expected odd n>=5")
    l = (n - 1) // 2
    h = tuple((x + 1) % n for x in range(n))
    h_inverse = inverse(h)
    identity = tuple(range(n))
    pair_counts = pair_product_multiplicities(n)

    # Identity pair-products cannot occur in a minimal factorization of h:
    # the remaining n-3 raw factors would be too few.  The positive marginal
    # support is discovered from the exact one-coordinate completion count.
    marginal_count: dict[Perm, int] = {}
    for g, lifts in pair_counts.items():
        completion = minimal_factorization_count(
            compose(inverse(g), h), n - 3
        )
        count = lifts * completion
        if count:
            marginal_count[g] = count
    support = sorted(marginal_count)
    if identity in marginal_count:
        raise AssertionError("identity increment had positive minimal marginal")
    total_states = n ** (n - 2)
    if sum(marginal_count.values()) != total_states:
        raise AssertionError("one-coordinate counts do not sum to Dénes count")

    # theta orbit decomposition of the product support.
    orbit_id: dict[Perm, int] = {}
    orbits: list[list[Perm]] = []
    for g in support:
        if g in orbit_id:
            continue
        orbit = []
        current = g
        while current not in orbit:
            orbit.append(current)
            current = theta(current, h, h_inverse)
        if current != g:
            raise AssertionError("theta trajectory entered a prior orbit off source")
        oid = len(orbits)
        for member in orbit:
            if member in orbit_id:
                raise AssertionError("theta orbits overlap")
            orbit_id[member] = oid
        orbits.append(orbit)

    q = len(orbits)
    kernel: list[list[Fraction]] = [[Fraction(0) for _ in range(q)] for _ in range(q)]
    joint_nonzero = 0
    joint_total = 0
    for source, orbit in enumerate(orbits):
        g = orbit[0]
        denominator = marginal_count[g]
        for s in support:
            completion = minimal_factorization_count(
                compose(inverse(compose(g, s)), h), n - 5
            )
            joint = pair_counts[g] * pair_counts[s] * completion
            if joint:
                joint_nonzero += 1
                joint_total += len(orbit) * joint
                kernel[source][orbit_id[s]] += Fraction(joint, denominator)
        if sum(kernel[source], Fraction(0)) != 1:
            raise AssertionError(f"H0 correlation row {source} does not normalize")
    if joint_total != total_states:
        raise AssertionError("two-coordinate counts do not sum to Dénes count")

    orbit_mass = [
        Fraction(len(orbit) * marginal_count[orbit[0]], total_states)
        for orbit in orbits
    ]
    if sum(orbit_mass, Fraction(0)) != 1:
        raise AssertionError("H0 marginal masses do not normalize")
    for a in range(q):
        for b in range(q):
            if orbit_mass[a] * kernel[a][b] != orbit_mass[b] * kernel[b][a]:
                raise AssertionError("H0 restriction is not exactly reversible")

    # Similarity to a real symmetric matrix in L2(orbit_mass).
    sym = np.zeros((q, q), dtype=float)
    for a in range(q):
        for b in range(q):
            sym[a, b] = float(kernel[a][b]) * math.sqrt(
                float(orbit_mass[a] / orbit_mass[b])
            )
    symmetry_residual = float(np.max(np.abs(sym - sym.T)))
    eigenvalues = np.linalg.eigvalsh(sym)
    eigenvalues.sort()
    kernel_numeric = np.array(kernel, dtype=float)
    orbit_mass_numeric = np.array(orbit_mass, dtype=float)
    constant_residual = float(np.max(np.abs(kernel_numeric.sum(axis=1) - 1)))
    one_multiplicity = int(np.count_nonzero(np.abs(eigenvalues - 1) < 1e-10))
    if abs(eigenvalues[-1] - 1) > 1e-10:
        raise AssertionError("constant eigenvalue was not one")
    mean_zero_eigenvalues = eigenvalues[:-1]
    kappa_max = float(mean_zero_eigenvalues[-1]) if len(mean_zero_eigenvalues) else -math.inf
    kappa_min = float(mean_zero_eigenvalues[0]) if len(mean_zero_eigenvalues) else math.inf

    kernel_squared_numeric = kernel_numeric @ kernel_numeric
    kernel_cubed_numeric = kernel_squared_numeric @ kernel_numeric
    centered_kernel_squared_numeric = (
        kernel_squared_numeric - orbit_mass_numeric[None, :]
    )
    centered_kernel_cubed_numeric = (
        kernel_cubed_numeric - orbit_mass_numeric[None, :]
    )
    kernel_squared_relative_numeric = (
        kernel_squared_numeric / orbit_mass_numeric[None, :]
    )
    kernel_squared_nonzero = int(np.count_nonzero(kernel_squared_numeric > 0.0))
    kernel_squared_min_flat = int(np.argmin(kernel_squared_relative_numeric))
    kernel_squared_max_flat = int(np.argmax(kernel_squared_relative_numeric))
    kernel_squared_min_source, kernel_squared_min_target = np.unravel_index(
        kernel_squared_min_flat, kernel_squared_relative_numeric.shape
    )
    kernel_squared_max_source, kernel_squared_max_target = np.unravel_index(
        kernel_squared_max_flat, kernel_squared_relative_numeric.shape
    )
    max_kernel_squared_centered_row_l1 = float(np.max(np.sum(
        np.abs(centered_kernel_squared_numeric), axis=1
    )))
    kernel_squared_centered_row_l1 = np.sum(
        np.abs(centered_kernel_squared_numeric), axis=1
    )
    max_kernel_squared_centered_row_l1_source = int(np.argmax(
        kernel_squared_centered_row_l1
    ))
    max_kernel_squared_centered_row_chi_square = float(np.max(np.sum(
        centered_kernel_squared_numeric ** 2 / orbit_mass_numeric[None, :],
        axis=1,
    )))
    dobrushin_l1 = 0.0
    dobrushin_pair = None
    for first in range(q):
        distances = np.sum(
            np.abs(kernel_numeric[first][None, :] - kernel_numeric), axis=1
        )
        second = int(np.argmax(distances))
        if float(distances[second]) > dobrushin_l1:
            dobrushin_l1 = float(distances[second])
            dobrushin_pair = (first, second)
    kernel_squared_dobrushin_l1 = 0.0
    kernel_squared_dobrushin_pair = None
    source_kinds = [increment_kind(orbit[0]) for orbit in orbits]
    kernel_squared_dobrushin_by_type: dict[tuple[str, str], tuple[float, int, int]] = {}
    for first in range(q):
        distances = np.sum(
            np.abs(
                kernel_squared_numeric[first][None, :] - kernel_squared_numeric
            ),
            axis=1,
        )
        second = int(np.argmax(distances))
        if float(distances[second]) > kernel_squared_dobrushin_l1:
            kernel_squared_dobrushin_l1 = float(distances[second])
            kernel_squared_dobrushin_pair = (first, second)
        for second_kind in sorted(set(source_kinds)):
            candidates = [
                second
                for second, kind in enumerate(source_kinds)
                if kind == second_kind
            ]
            second = max(candidates, key=lambda index: distances[index])
            key = tuple(sorted((source_kinds[first], second_kind)))
            value = float(distances[second])
            if key not in kernel_squared_dobrushin_by_type or value > (
                kernel_squared_dobrushin_by_type[key][0]
            ):
                kernel_squared_dobrushin_by_type[key] = (value, first, second)

    relative_by_type = []
    for source_kind in sorted(set(source_kinds)):
        source_indices = [
            index for index, kind in enumerate(source_kinds) if kind == source_kind
        ]
        for target_kind in sorted(set(source_kinds)):
            target_indices = [
                index for index, kind in enumerate(source_kinds) if kind == target_kind
            ]
            block = kernel_squared_relative_numeric[np.ix_(source_indices, target_indices)]
            relative_by_type.append({
                "source_kind": source_kind,
                "target_kind": target_kind,
                "minimum_relative_to_stationarity": float(np.min(block)),
                "maximum_relative_to_stationarity": float(np.max(block)),
            })

    # Separate the already-small target-kind mass error from the conditional
    # distribution within each kind.  This tests the proposed common-measure
    # decomposition without assuming that either product kind is lumpable.
    conditional_target_kind_diagnostics = []
    conditional_rows_by_kind: dict[str, np.ndarray] = {}
    target_mass_by_kind: dict[str, np.ndarray] = {}
    for target_kind in sorted(set(source_kinds)):
        indices = np.array([
            index for index, kind in enumerate(source_kinds) if kind == target_kind
        ], dtype=int)
        block = kernel_squared_numeric[:, indices]
        row_masses = np.sum(block, axis=1)
        conditional_rows = block / row_masses[:, None]
        stationary_mass = float(np.sum(orbit_mass_numeric[indices]))
        stationary_conditional = orbit_mass_numeric[indices] / stationary_mass
        row_to_stationary_tv = 0.5 * np.sum(
            np.abs(conditional_rows - stationary_conditional[None, :]), axis=1
        )
        pair_tv_max = 0.0
        pair_tv_pair = (0, 0)
        for first in range(q):
            distances = 0.5 * np.sum(
                np.abs(conditional_rows[first][None, :] - conditional_rows),
                axis=1,
            )
            second = int(np.argmax(distances))
            if float(distances[second]) > pair_tv_max:
                pair_tv_max = float(distances[second])
                pair_tv_pair = (first, second)
        worst_row = int(np.argmax(row_to_stationary_tv))
        conditional_target_kind_diagnostics.append({
            "target_kind": target_kind,
            "stationary_kind_mass": stationary_mass,
            "minimum_two_step_row_kind_mass": float(np.min(row_masses)),
            "maximum_two_step_row_kind_mass": float(np.max(row_masses)),
            "maximum_absolute_kind_mass_error": float(np.max(
                np.abs(row_masses - stationary_mass)
            )),
            "n_squared_times_maximum_absolute_kind_mass_error": float(
                n * n * np.max(np.abs(row_masses - stationary_mass))
            ),
            "maximum_conditional_row_TV_from_stationary": float(
                row_to_stationary_tv[worst_row]
            ),
            "n_times_maximum_conditional_row_TV_from_stationary": float(
                n * row_to_stationary_tv[worst_row]
            ),
            "n_squared_times_maximum_conditional_row_TV_from_stationary": float(
                n * n * row_to_stationary_tv[worst_row]
            ),
            "worst_row_descriptor": increment_descriptor(orbits[worst_row][0], h),
            "conditional_pairwise_Dobrushin_TV": pair_tv_max,
            "n_times_conditional_pairwise_Dobrushin_TV": n * pair_tv_max,
            "n_squared_times_conditional_pairwise_Dobrushin_TV": n * n * pair_tv_max,
            "conditional_pairwise_Dobrushin_source_descriptors": [
                increment_descriptor(orbits[source][0], h)
                for source in pair_tv_pair
            ],
        })
        conditional_rows_by_kind[target_kind] = conditional_rows
        target_mass_by_kind[target_kind] = row_masses

    conditional_common_measure_upper_bounds = []
    kind_names = sorted(conditional_rows_by_kind)
    for source in range(q):
        kind_mass_error = 0.5 * sum(
            abs(
                target_mass_by_kind[kind][source]
                - sum(orbit_mass_numeric[index]
                      for index, source_kind in enumerate(source_kinds)
                      if source_kind == kind)
            )
            for kind in kind_names
        )
        conditional_term = 0.0
        for kind in kind_names:
            indices = [
                index for index, source_kind in enumerate(source_kinds)
                if source_kind == kind
            ]
            stationary_kind_mass = float(sum(orbit_mass_numeric[indices]))
            stationary_conditional = orbit_mass_numeric[indices] / stationary_kind_mass
            conditional_tv = 0.5 * float(np.sum(np.abs(
                conditional_rows_by_kind[kind][source] - stationary_conditional
            )))
            conditional_term += min(
                float(target_mass_by_kind[kind][source]), stationary_kind_mass
            ) * conditional_tv
        conditional_common_measure_upper_bounds.append(
            kind_mass_error + conditional_term
        )

    # Does the two-step coarse kind mass remember only the unordered residual
    # sizes of g^{-1}h, or also their embedding/matching color?  A positive
    # spread within one size class is an exact finite obstruction to the
    # simplest three-size closure ansatz.
    two_step_kind_mass_residual_size_closure = []
    residual_size_classes: dict[tuple[int, ...], list[int]] = collections.defaultdict(list)
    for source, orbit in enumerate(orbits):
        residual_size_classes[
            cycle_lengths(compose(inverse(orbit[0]), h))
        ].append(source)
    for target_kind in sorted(set(source_kinds)):
        target_indices = [
            target for target, kind in enumerate(source_kinds)
            if kind == target_kind
        ]
        values = np.sum(kernel_squared_numeric[:, target_indices], axis=1)
        maximum_spread = 0.0
        witness_class = None
        witness_sources = None
        for residual_sizes, source_indices in residual_size_classes.items():
            if len(source_indices) < 2:
                continue
            class_values = values[source_indices]
            spread = float(np.max(class_values) - np.min(class_values))
            if spread > maximum_spread:
                maximum_spread = spread
                low = source_indices[int(np.argmin(class_values))]
                high = source_indices[int(np.argmax(class_values))]
                witness_class = residual_sizes
                witness_sources = (low, high)
        two_step_kind_mass_residual_size_closure.append({
            "target_kind": target_kind,
            "maximum_numeric_spread_within_one_residual_size_class": maximum_spread,
            "witness_residual_cycle_sizes": (
                list(witness_class) if witness_class is not None else None
            ),
            "witness_source_gap_parameters": (
                [gap_parameter(orbits[source][0]) for source in witness_sources]
                if witness_sources is not None else None
            ),
            "witness_source_descriptors": (
                [increment_descriptor(orbits[source][0], h) for source in witness_sources]
                if witness_sources is not None else None
            ),
        })

    # Natural source metric: two quotient product states are adjacent when
    # some ordered transposition-pair lifts agree in one raw coordinate.
    # This is the one-factor replacement graph on rank-two increments, after
    # cyclic quotienting.  If local K^2 row TV were O(n^-3) and this graph had
    # diameter O(n), path coupling would prove the desired O(n^-2) global
    # Dobrushin bound.  The diagnostic tests both scalings.
    lift_token_to_orbits: dict[tuple[int, Perm], set[int]] = collections.defaultdict(set)
    gates = transpositions(n)
    for first in gates:
        for second in gates:
            product = compose(first, second)
            source = orbit_id.get(product)
            if source is None:
                continue
            lift_token_to_orbits[(0, first)].add(source)
            lift_token_to_orbits[(1, second)].add(source)
    source_metric_adjacency = [set() for _ in range(q)]
    for source_set in lift_token_to_orbits.values():
        ordered_sources = sorted(source_set)
        for offset, first in enumerate(ordered_sources):
            for second in ordered_sources[offset + 1:]:
                source_metric_adjacency[first].add(second)
                source_metric_adjacency[second].add(first)
    local_max_tv = 0.0
    local_max_pair = None
    source_metric_edges = 0
    for first in range(q):
        for second in source_metric_adjacency[first]:
            if second <= first:
                continue
            source_metric_edges += 1
            distance = 0.5 * float(np.sum(np.abs(
                kernel_squared_numeric[first] - kernel_squared_numeric[second]
            )))
            if distance > local_max_tv:
                local_max_tv = distance
                local_max_pair = (first, second)
    graph_distances = []
    graph_diameter = 0
    graph_connected = True
    for start in range(q):
        distances = [-1] * q
        distances[start] = 0
        queue = collections.deque([start])
        while queue:
            current_source = queue.popleft()
            for neighbor in source_metric_adjacency[current_source]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current_source] + 1
                    queue.append(neighbor)
        if -1 in distances:
            graph_connected = False
        else:
            graph_diameter = max(graph_diameter, max(distances))
        graph_distances.append(distances)
    local_metric_diagnostic = {
        "definition": (
            "quotient states adjacent iff ordered pair lifts share their first "
            "or share their second raw transposition"
        ),
        "edges": source_metric_edges,
        "connected": graph_connected,
        "diameter": graph_diameter if graph_connected else None,
        "maximum_adjacent_two_step_row_TV": local_max_tv,
        "n_squared_times_maximum_adjacent_two_step_row_TV": n * n * local_max_tv,
        "n_cubed_times_maximum_adjacent_two_step_row_TV": n ** 3 * local_max_tv,
        "maximizing_pair_gap_parameters": (
            [gap_parameter(orbits[source][0]) for source in local_max_pair]
            if local_max_pair is not None else None
        ),
        "maximizing_pair_descriptors": (
            [increment_descriptor(orbits[source][0], h) for source in local_max_pair]
            if local_max_pair is not None else None
        ),
        "diameter_times_local_max_TV": (
            graph_diameter * local_max_tv if graph_connected else None
        ),
        "n_squared_times_diameter_times_local_max_TV": (
            n * n * graph_diameter * local_max_tv if graph_connected else None
        ),
    }

    def row_difference_kind_breakdown(first: int, second: int) -> list[dict[str, object]]:
        difference = kernel_squared_numeric[first] - kernel_squared_numeric[second]
        records = []
        for target_kind in sorted(set(source_kinds)):
            indices = [
                index for index, kind in enumerate(source_kinds)
                if kind == target_kind
            ]
            values = difference[indices]
            records.append({
                "target_kind": target_kind,
                "signed_difference": float(np.sum(values)),
                "absolute_difference": float(np.sum(np.abs(values))),
                "positive_target_orbits": int(np.count_nonzero(values > 1e-15)),
                "negative_target_orbits": int(np.count_nonzero(values < -1e-15)),
                "zero_target_orbits_numeric": int(np.count_nonzero(np.abs(values) <= 1e-15)),
            })
        return records

    # For the exact n=7,9 certificates, exhaust all rational two-step row
    # pairs, then retain the complete signed difference at an exact maximizer.
    exact_dobrushin_pair_certificate = None
    exact_two_step_chi_square_certificate = None
    exact_residual_size_closure_certificate = None
    if q <= 40:
        exact_kernel_squared = [
            [
                sum(
                    (kernel[source][middle] * kernel[middle][target]
                     for middle in range(q)),
                    Fraction(0),
                )
                for target in range(q)
            ]
            for source in range(q)
        ]
        exact_tv = Fraction(-1)
        exact_maximizers = []
        for first_candidate in range(q):
            for second_candidate in range(first_candidate + 1, q):
                distance = sum((
                    abs(exact_kernel_squared[first_candidate][target]
                        - exact_kernel_squared[second_candidate][target])
                    for target in range(q)
                ), Fraction(0)) / 2
                if distance > exact_tv:
                    exact_tv = distance
                    exact_maximizers = [(first_candidate, second_candidate)]
                elif distance == exact_tv:
                    exact_maximizers.append((first_candidate, second_candidate))
        first, second = exact_maximizers[0]
        if set((first, second)) != set(kernel_squared_dobrushin_pair):
            raise AssertionError("floating and exact Dobrushin maximizers differ")
        exact_difference = [
            exact_kernel_squared[first][target]
            - exact_kernel_squared[second][target]
            for target in range(q)
        ]
        exact_tv = sum(map(abs, exact_difference), Fraction(0)) / 2
        exact_kind_records = []
        for target_kind in sorted(set(source_kinds)):
            indices = [
                target
                for target, kind in enumerate(source_kinds)
                if kind == target_kind
            ]
            exact_kind_records.append({
                "target_kind": target_kind,
                "signed_difference_exact": rational_string(sum(
                    (exact_difference[target] for target in indices), Fraction(0)
                )),
                "absolute_difference_exact": rational_string(sum(
                    (abs(exact_difference[target]) for target in indices), Fraction(0)
                )),
            })
        target_records = [
            {
                "target_orbit": target,
                "target_gap_parameter": gap_parameter(orbits[target][0]),
                "target_descriptor": increment_descriptor(orbits[target][0], h),
                "signed_difference_exact": rational_string(exact_difference[target]),
            }
            for target in range(q)
        ]
        target_records.sort(
            key=lambda record: abs(Fraction(record["signed_difference_exact"])),
            reverse=True,
        )
        exact_dobrushin_pair_certificate = {
            "source_orbits": [first, second],
            "exhaustive_exact_maximization": True,
            "number_of_unordered_maximizing_pairs": len(exact_maximizers),
            "source_gap_parameters": [
                gap_parameter(orbits[source][0]) for source in (first, second)
            ],
            "source_descriptors": [
                increment_descriptor(orbits[source][0], h)
                for source in (first, second)
            ],
            "TV_distance_exact": rational_string(exact_tv),
            "kind_breakdown_exact": exact_kind_records,
            "target_signed_difference_vector_sorted_by_absolute_value": target_records,
        }
        exact_adjacent_tv = Fraction(-1)
        exact_adjacent_pairs = []
        for first_candidate in range(q):
            for second_candidate in source_metric_adjacency[first_candidate]:
                if second_candidate <= first_candidate:
                    continue
                distance = sum((
                    abs(exact_kernel_squared[first_candidate][target]
                        - exact_kernel_squared[second_candidate][target])
                    for target in range(q)
                ), Fraction(0)) / 2
                if distance > exact_adjacent_tv:
                    exact_adjacent_tv = distance
                    exact_adjacent_pairs = [(first_candidate, second_candidate)]
                elif distance == exact_adjacent_tv:
                    exact_adjacent_pairs.append((first_candidate, second_candidate))
        local_metric_diagnostic.update({
            "maximum_adjacent_two_step_row_TV_exact": rational_string(
                exact_adjacent_tv
            ),
            "number_of_exact_adjacent_maximizing_pairs": len(exact_adjacent_pairs),
            "exact_adjacent_maximizing_pair_gap_parameters": [
                gap_parameter(orbits[source][0])
                for source in exact_adjacent_pairs[0]
            ],
        })

        exact_max_chi_square = Fraction(-1)
        exact_max_chi_square_sources = []
        for source in range(q):
            chi_square = sum((
                (exact_kernel_squared[source][target] - orbit_mass[target]) ** 2
                / orbit_mass[target]
                for target in range(q)
            ), Fraction(0))
            if chi_square > exact_max_chi_square:
                exact_max_chi_square = chi_square
                exact_max_chi_square_sources = [source]
            elif chi_square == exact_max_chi_square:
                exact_max_chi_square_sources.append(source)
        exact_two_step_chi_square_certificate = {
            "exhaustive_exact_maximization": True,
            "maximum_row_chi_square_exact": rational_string(exact_max_chi_square),
            "number_of_maximizing_source_orbits": len(exact_max_chi_square_sources),
            "maximizing_source_gap_parameters": [
                gap_parameter(orbits[source][0])
                for source in exact_max_chi_square_sources
            ],
            "maximizing_source_descriptors": [
                increment_descriptor(orbits[source][0], h)
                for source in exact_max_chi_square_sources
            ],
        }
        exact_residual_size_closure_certificate = []
        for target_kind in sorted(set(source_kinds)):
            target_indices = [
                target for target, kind in enumerate(source_kinds)
                if kind == target_kind
            ]
            exact_kind_masses = [
                sum((exact_kernel_squared[source][target]
                     for target in target_indices), Fraction(0))
                for source in range(q)
            ]
            maximum_spread = Fraction(-1)
            witness = None
            witness_sizes = None
            for residual_sizes, source_indices in residual_size_classes.items():
                if len(source_indices) < 2:
                    continue
                low = min(source_indices, key=lambda source: exact_kind_masses[source])
                high = max(source_indices, key=lambda source: exact_kind_masses[source])
                spread = exact_kind_masses[high] - exact_kind_masses[low]
                if spread > maximum_spread:
                    maximum_spread = spread
                    witness = (low, high)
                    witness_sizes = residual_sizes
            exact_residual_size_closure_certificate.append({
                "target_kind": target_kind,
                "maximum_spread_exact": rational_string(maximum_spread),
                "witness_residual_cycle_sizes": list(witness_sizes),
                "witness_source_gap_parameters": [
                    gap_parameter(orbits[source][0]) for source in witness
                ],
            })

    # Resolve the extremal two-step row into target product/complement types.
    target_type_breakdown: dict[tuple[str, tuple[int, ...]], dict[str, float | int]] = {}
    extremal_row = centered_kernel_squared_numeric[
        max_kernel_squared_centered_row_l1_source
    ]
    for target, deviation in enumerate(extremal_row):
        representative = orbits[target][0]
        key = (
            increment_kind(representative),
            cycle_lengths(compose(inverse(representative), h)),
        )
        record = target_type_breakdown.setdefault(key, {
            "target_orbits": 0,
            "target_stationary_mass": 0.0,
            "signed_deviation": 0.0,
            "absolute_deviation": 0.0,
        })
        record["target_orbits"] += 1
        record["target_stationary_mass"] += float(orbit_mass[target])
        record["signed_deviation"] += float(deviation)
        record["absolute_deviation"] += abs(float(deviation))
    target_type_records = [
        {
            "target_kind": key[0],
            "target_complement_cycle_sizes_sorted": list(key[1]),
            **record,
        }
        for key, record in target_type_breakdown.items()
    ]
    target_type_records.sort(
        key=lambda record: record["absolute_deviation"], reverse=True
    )

    # Test two elementary gap-dependent envelopes for every source orbit.
    scaled_two_step_rows = l * l * kernel_squared_centered_row_l1
    min_gap_envelope = []
    reciprocal_gap_envelope = []
    min_gap_histogram: dict[int, list[float]] = collections.defaultdict(list)
    for source, orbit in enumerate(orbits):
        complement_sizes = cycle_lengths(compose(inverse(orbit[0]), h))
        minimum_gap = min(complement_sizes)
        reciprocal_sum = sum(1.0 / size for size in complement_sizes)
        scaled = float(scaled_two_step_rows[source])
        min_gap_envelope.append(scaled * minimum_gap)
        reciprocal_gap_envelope.append(scaled / reciprocal_sum)
        min_gap_histogram[minimum_gap].append(scaled)

    # Diagnostics for elementary norm-bound proof attempts.  Since K is
    # self-adjoint in L2(orbit_mass), the centered Hilbert--Schmidt norm is
    # trace(K^2)-1.  The rowwise quantities test direct total-variation and
    # chi-square bounds; rare rows can make them much weaker than the true
    # operator norm.
    centered_hilbert_schmidt_squared = Fraction(-1)
    max_centered_row_l1 = Fraction(0)
    max_centered_row_chi_square = Fraction(0)
    max_centered_row_l1_source = None
    max_centered_row_chi_square_source = None
    centered_row_chi_squares: list[Fraction] = []
    for a in range(q):
        centered_hilbert_schmidt_squared += sum(
            kernel[a][b] * kernel[b][a] for b in range(q)
        )
        row_l1 = sum(abs(kernel[a][b] - orbit_mass[b]) for b in range(q))
        row_chi_square = sum(
            (kernel[a][b] - orbit_mass[b]) ** 2 / orbit_mass[b]
            for b in range(q)
        )
        centered_row_chi_squares.append(row_chi_square)
        if row_l1 > max_centered_row_l1:
            max_centered_row_l1 = row_l1
            max_centered_row_l1_source = a
        if row_chi_square > max_centered_row_chi_square:
            max_centered_row_chi_square = row_chi_square
            max_centered_row_chi_square_source = a

    # On a U-invariant one-coordinate eigenfunction kappa is real.  M16's
    # l-coordinate Gram block has one symmetric eigenvalue and l-1 transverse
    # eigenvalues.  Maximize both formulas over the exact finite spectrum.
    gram_candidates = []
    for value in mean_zero_eigenvalues:
        gram_candidates.append((float((1 + (l - 1) * value) / l), "symmetric", float(value)))
        gram_candidates.append((float((1 - value) / l), "transverse", float(value)))
    gram_candidates.append((1 / l, "microfiber", 0.0))
    mu_h0, mu_sector, mu_kappa = max(gram_candidates)

    cycle_type_counts = collections.Counter(cycle_lengths(g) for g in support)
    orbit_size_counts = collections.Counter(len(orbit) for orbit in orbits)
    marginal_count_values = sorted(set(marginal_count.values()))

    # Store the exact compressed kernel compactly as sparse rational triples.
    sparse_kernel = []
    for a in range(q):
        for b in range(q):
            if kernel[a][b]:
                sparse_kernel.append((a, b, rational_string(kernel[a][b])))

    top_row_contributions = sorted(
        range(q),
        key=lambda source: orbit_mass[source] * centered_row_chi_squares[source],
        reverse=True,
    )[:10]

    # Resolve trace two and trace four into positive source-row contributions.
    # For a reversible kernel, these are respectively
    # pi(g) chi^2(K(g,.),pi) and pi(g) chi^2(K^2(g,.),pi).  Grouping by the
    # smallest residual cycle tests for a harmonic boundary divergence while
    # preserving positivity (unlike the signed phase-overlap split).
    trace_moments_by_minimum_residual_size: dict[int, dict[str, float | int]] = {}
    trace_moments_by_source_kind: dict[str, dict[str, float | int]] = {}
    for source, orbit in enumerate(orbits):
        representative = orbit[0]
        minimum_residual = min(cycle_lengths(compose(inverse(representative), h)))
        source_kind = increment_kind(representative)
        trace_two_contribution = float(
            orbit_mass[source] * centered_row_chi_squares[source]
        )
        trace_four_row_chi_square = float(np.sum(
            centered_kernel_squared_numeric[source] ** 2 / orbit_mass_numeric
        ))
        trace_four_contribution = float(
            orbit_mass_numeric[source] * trace_four_row_chi_square
        )
        for table, key in (
            (trace_moments_by_minimum_residual_size, minimum_residual),
            (trace_moments_by_source_kind, source_kind),
        ):
            record = table.setdefault(key, {
                "source_orbits": 0,
                "stationary_mass": 0.0,
                "trace_two_contribution": 0.0,
                "trace_four_contribution": 0.0,
                "trace_six_contribution": 0.0,
            })
            record["source_orbits"] += 1
            record["stationary_mass"] += float(orbit_mass[source])
            record["trace_two_contribution"] += trace_two_contribution
            record["trace_four_contribution"] += trace_four_contribution
            trace_six_row_chi_square = float(np.sum(
                centered_kernel_cubed_numeric[source] ** 2 / orbit_mass_numeric
            ))
            record["trace_six_contribution"] += float(
                orbit_mass_numeric[source] * trace_six_row_chi_square
            )

    minimum_residual_records = [
        {
            "minimum_residual_cycle_size": minimum_residual,
            **record,
            "l_squared_times_trace_two_contribution": (
                l * l * record["trace_two_contribution"]
            ),
            "l_fourth_times_trace_four_contribution": (
                l ** 4 * record["trace_four_contribution"]
            ),
            "l_sixth_times_trace_six_contribution": (
                l ** 6 * record["trace_six_contribution"]
            ),
        }
        for minimum_residual, record in sorted(
            trace_moments_by_minimum_residual_size.items()
        )
    ]
    source_kind_moment_records = [
        {
            "source_kind": source_kind,
            **record,
            "l_squared_times_trace_two_contribution": (
                l * l * record["trace_two_contribution"]
            ),
            "l_fourth_times_trace_four_contribution": (
                l ** 4 * record["trace_four_contribution"]
            ),
            "l_sixth_times_trace_six_contribution": (
                l ** 6 * record["trace_six_contribution"]
            ),
        }
        for source_kind, record in sorted(trace_moments_by_source_kind.items())
    ]

    return {
        "n": n,
        "l": l,
        "raw_states": total_states,
        "product_support_size": len(support),
        "product_support_cycle_types": {
            str(key): value for key, value in sorted(cycle_type_counts.items())
        },
        "theta_orbits": q,
        "theta_orbit_size_histogram": {
            str(key): value for key, value in sorted(orbit_size_counts.items())
        },
        "distinct_one_coordinate_microstate_counts": marginal_count_values,
        "joint_nonzero_ordered_product_pairs_per_representatives": joint_nonzero,
        "exact_row_normalization": True,
        "exact_reversibility": True,
        "constant_numeric_residual": constant_residual,
        "symmetric_similarity_numeric_residual": symmetry_residual,
        "eigenvalue_one_numeric_multiplicity": one_multiplicity,
        "H0_K_eigenvalues_ascending_numeric": [float(value) for value in eigenvalues],
        "H0_K_top_mean_zero_eigenvalue_numeric": kappa_max,
        "H0_K_bottom_mean_zero_eigenvalue_numeric": kappa_min,
        "l_times_H0_K_top_mean_zero_numeric": l * kappa_max,
        "centered_H0_K_Hilbert_Schmidt_squared_exact": rational_string(
            centered_hilbert_schmidt_squared
        ),
        "l_squared_times_centered_H0_K_Hilbert_Schmidt_squared_numeric": (
            l * l * float(centered_hilbert_schmidt_squared)
        ),
        "centered_H0_K_Schatten_fourth_trace_numeric": float(
            np.sum(mean_zero_eigenvalues ** 4)
        ),
        "l_fourth_times_centered_H0_K_Schatten_fourth_trace_numeric": float(
            l ** 4 * np.sum(mean_zero_eigenvalues ** 4)
        ),
        "centered_H0_K_Schatten_sixth_trace_numeric": float(
            np.sum(mean_zero_eigenvalues ** 6)
        ),
        "max_centered_H0_K_squared_row_L1_numeric": (
            max_kernel_squared_centered_row_l1
        ),
        "H0_K_squared_full_support": kernel_squared_nonzero == q * q,
        "H0_K_squared_nonzero_entries": kernel_squared_nonzero,
        "H0_K_squared_total_entries": q * q,
        "H0_K_squared_min_relative_to_stationarity_numeric": float(
            kernel_squared_relative_numeric[
                kernel_squared_min_source, kernel_squared_min_target
            ]
        ),
        "H0_K_squared_min_relative_source_descriptor": increment_descriptor(
            orbits[kernel_squared_min_source][0], h
        ),
        "H0_K_squared_min_relative_target_descriptor": increment_descriptor(
            orbits[kernel_squared_min_target][0], h
        ),
        "H0_K_squared_max_relative_to_stationarity_numeric": float(
            kernel_squared_relative_numeric[
                kernel_squared_max_source, kernel_squared_max_target
            ]
        ),
        "H0_K_squared_max_relative_source_descriptor": increment_descriptor(
            orbits[kernel_squared_max_source][0], h
        ),
        "H0_K_squared_max_relative_target_descriptor": increment_descriptor(
            orbits[kernel_squared_max_target][0], h
        ),
        "H0_K_squared_Dobrushin_coefficient_numeric": (
            0.5 * kernel_squared_dobrushin_l1
        ),
        "l_squared_times_H0_K_squared_Dobrushin_coefficient_numeric": (
            0.5 * l * l * kernel_squared_dobrushin_l1
        ),
        "H0_K_squared_Dobrushin_maximizing_orbit_pair_descriptors": [
            increment_descriptor(orbits[source][0], h)
            for source in kernel_squared_dobrushin_pair
        ],
        "H0_K_squared_Dobrushin_maximizing_pair_target_kind_breakdown": (
            row_difference_kind_breakdown(*kernel_squared_dobrushin_pair)
        ),
        "H0_K_squared_Dobrushin_exact_pair_certificate": (
            exact_dobrushin_pair_certificate
        ),
        "H0_K_squared_Dobrushin_by_source_kind": [
            {
                "source_kinds": list(key),
                "coefficient_numeric": 0.5 * value[0],
                "l_squared_times_coefficient_numeric": 0.5 * l * l * value[0],
                "maximizing_pair_descriptors": [
                    increment_descriptor(orbits[source][0], h)
                    for source in value[1:]
                ],
                "target_kind_breakdown": row_difference_kind_breakdown(
                    value[1], value[2]
                ),
            }
            for key, value in sorted(kernel_squared_dobrushin_by_type.items())
        ],
        "H0_K_squared_relative_extrema_by_source_target_kind": relative_by_type,
        "H0_K_squared_conditional_target_kind_diagnostics": (
            conditional_target_kind_diagnostics
        ),
        "max_common_measure_TV_upper_bound_from_kind_conditioning_numeric": max(
            conditional_common_measure_upper_bounds
        ),
        "l_squared_times_max_common_measure_TV_upper_bound_numeric": (
            l * l * max(conditional_common_measure_upper_bounds)
        ),
        "H0_K_squared_kind_mass_residual_size_closure_test": (
            two_step_kind_mass_residual_size_closure
        ),
        "H0_K_squared_exact_residual_size_closure_certificate": (
            exact_residual_size_closure_certificate
        ),
        "H0_K_squared_one_factor_replacement_source_metric": (
            local_metric_diagnostic
        ),
        "max_centered_H0_K_squared_row_L1_source_orbit": (
            max_kernel_squared_centered_row_l1_source
        ),
        "max_centered_H0_K_squared_row_L1_source_descriptor": increment_descriptor(
            orbits[max_kernel_squared_centered_row_l1_source][0], h
        ),
        "l_squared_times_max_centered_H0_K_squared_row_L1_numeric": (
            l * l * max_kernel_squared_centered_row_l1
        ),
        "max_centered_H0_K_squared_row_target_type_breakdown": (
            target_type_records
        ),
        "gap_envelope_diagnostics": {
            "max_over_sources_of_l2_rowL1_times_min_complement_gap": max(
                min_gap_envelope
            ),
            "max_over_sources_of_l2_rowL1_divided_by_sum_reciprocal_complement_gaps": max(
                reciprocal_gap_envelope
            ),
            "max_l2_rowL1_by_min_complement_gap": {
                str(gap): max(values)
                for gap, values in sorted(min_gap_histogram.items())
            },
        },
        "max_centered_H0_K_squared_row_chi_square_numeric": (
            max_kernel_squared_centered_row_chi_square
        ),
        "H0_K_squared_exact_uniform_row_chi_square_certificate": (
            exact_two_step_chi_square_certificate
        ),
        "H0_K_Dobrushin_coefficient_numeric": 0.5 * dobrushin_l1,
        "n_times_H0_K_Dobrushin_coefficient_numeric": (
            0.5 * n * dobrushin_l1
        ),
        "H0_K_Dobrushin_maximizing_orbit_pair": list(dobrushin_pair),
        "H0_K_Dobrushin_maximizing_orbit_pair_descriptors": [
            increment_descriptor(orbits[source][0], h)
            for source in dobrushin_pair
        ],
        "l_sixth_times_centered_H0_K_Schatten_sixth_trace_numeric": float(
            l ** 6 * np.sum(mean_zero_eigenvalues ** 6)
        ),
        "max_centered_H0_K_row_L1_exact": rational_string(max_centered_row_l1),
        "n_times_max_centered_H0_K_row_L1_numeric": (
            n * float(max_centered_row_l1)
        ),
        "max_centered_H0_K_row_L1_source_orbit": max_centered_row_l1_source,
        "max_centered_H0_K_row_L1_source_cycles": nontrivial_cycles(
            orbits[max_centered_row_l1_source][0]
        ),
        "max_centered_H0_K_row_L1_source_descriptor": increment_descriptor(
            orbits[max_centered_row_l1_source][0], h
        ),
        "max_centered_H0_K_row_chi_square_exact": rational_string(
            max_centered_row_chi_square
        ),
        "max_centered_H0_K_row_chi_square_source_orbit": (
            max_centered_row_chi_square_source
        ),
        "max_centered_H0_K_row_chi_square_source_cycles": nontrivial_cycles(
            orbits[max_centered_row_chi_square_source][0]
        ),
        "top_centered_row_chi_square_weighted_contributions_numeric": [
            {
                "source_orbit": source,
                "source_cycles": nontrivial_cycles(orbits[source][0]),
                "orbit_mass": float(orbit_mass[source]),
                "row_chi_square": float(centered_row_chi_squares[source]),
                "weighted_contribution": float(
                    orbit_mass[source] * centered_row_chi_squares[source]
                ),
            }
            for source in top_row_contributions
        ],
        "trace_moments_by_minimum_residual_cycle_size_numeric": (
            minimum_residual_records
        ),
        "trace_moments_by_source_kind_numeric": source_kind_moment_records,
        "H0_coordinate_Gram_top_mean_zero_numeric": mu_h0,
        "l_times_H0_coordinate_Gram_top_mean_zero_numeric": l * mu_h0,
        "H0_coordinate_Gram_top_source": {
            "coefficient_sector": mu_sector,
            "K_eigenvalue_numeric": mu_kappa,
        },
        "orbit_masses_exact": [rational_string(value) for value in orbit_mass],
        "H0_K_sparse_exact": sparse_kernel,
        "finite_spectrum_warning": (
            "The compressed kernel and its checks are exact; the displayed eigenvalues "
            "are floating diagnostics and prove no asymptotic correlation bound."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--compact",
        action="store_true",
        help="omit the sparse matrix, mass vector, and full eigenvalue list",
    )
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    rows = [analyze(n) for n in parameters]
    if args.compact:
        for row in rows:
            del row["orbit_masses_exact"]
            del row["H0_K_sparse_exact"]
            del row["H0_K_eigenvalues_ascending_numeric"]
    payload = {
        "claim_tested": (
            "After restricting M16's one-coordinate correlation operator to "
            "theta-invariant functions for the minimal long-cycle endpoint, its top "
            "mean-zero eigenvalue is O(1/l), despite M67's nonzero-frequency "
            "Omega(l^-1/2) witness."
        ),
        "scope_warning": (
            "Exact finite kernels can refute a proposed bound with a fixed constant "
            "at tested sizes but cannot prove a universal asymptotic bound."
        ),
        "convention": "(p q)(x)=p(q(x)); tuple products left-to-right",
        "parameters": parameters,
        "compact": args.compact,
        "results": rows,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            [
                {
                    "n": row["n"],
                    "l": row["l"],
                    "support": row["product_support_size"],
                    "H0_dimension": row["theta_orbits"],
                    "kappa_max_mean_zero": row["H0_K_top_mean_zero_eigenvalue_numeric"],
                    "l_kappa_max": row["l_times_H0_K_top_mean_zero_numeric"],
                    "kappa_min_mean_zero": row["H0_K_bottom_mean_zero_eigenvalue_numeric"],
                    "mu_H0": row["H0_coordinate_Gram_top_mean_zero_numeric"],
                    "l_mu_H0": row["l_times_H0_coordinate_Gram_top_mean_zero_numeric"],
                    "mu_source": row["H0_coordinate_Gram_top_source"],
                }
                for row in payload["results"]
            ],
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
