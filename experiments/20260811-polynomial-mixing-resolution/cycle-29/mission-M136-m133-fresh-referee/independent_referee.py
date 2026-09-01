#!/usr/bin/env python3
"""Clean-room exact referee checks for frozen mission M133.

The checker imports no M133 or M125 Python module.  It has four independent
views of the coefficient object:

* literal ordered pairs of set partitions, represented by restricted-growth
  strings;
* graph-theoretic leaf pruning to identify the unique multigraph cycle;
* the claimed positive core-plus-planted-tree recurrence; and
* a rooted multiset connected-component recurrence, using a dynamic root
  type, for the larger targeted coefficient triples.

All arithmetic is exact and deterministic.  There is no random seed.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path


Partition = tuple[tuple[int, ...], ...]
Poly = dict[tuple[int, int], Fraction]
Matrix = tuple[tuple[Fraction, ...], ...]


REPOSITORY = Path(__file__).resolve().parents[4]
M133 = (
    REPOSITORY
    / "experiments/20260811-polynomial-mixing-resolution/cycle-28"
    / "mission-M133-defect-coefficient-no-valley"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()


def integer_partitions(total: int, lower: int = 1):
    """Yield nondecreasing positive integer partitions of ``total``."""
    if total == 0:
        yield ()
        return
    for first in range(lower, total + 1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def fixed_length_partitions(total: int, parts: int, lower: int = 1):
    """Yield nondecreasing partitions with a prescribed number of parts."""
    if parts == 0:
        if total == 0:
            yield ()
        return
    if total < parts * lower:
        return
    for first in range(lower, total // parts + 1):
        for rest in fixed_length_partitions(total - first, parts - 1, first):
            yield (first,) + rest


@functools.cache
def set_partitions(count: int) -> tuple[Partition, ...]:
    """Set partitions of range(count), generated as restricted-growth strings."""
    if count == 0:
        return ((),)
    strings: list[tuple[int, ...]] = []

    def extend(prefix: list[int], largest: int) -> None:
        if len(prefix) == count:
            strings.append(tuple(prefix))
            return
        for label in range(largest + 2):
            prefix.append(label)
            extend(prefix, max(largest, label))
            prefix.pop()

    extend([0], 0)
    output: list[Partition] = []
    for labels in strings:
        blocks = tuple(
            tuple(index for index, label in enumerate(labels) if label == block)
            for block in range(max(labels) + 1)
        )
        output.append(blocks)
    return tuple(output)


def partitions_of_items(items: tuple[int, ...]):
    for pattern in set_partitions(len(items)):
        yield tuple(tuple(items[index] for index in block) for block in pattern)


def block_weight(atom_sizes: tuple[int, ...], block: tuple[int, ...]) -> Fraction:
    label_count = sum(atom_sizes[edge] for edge in block)
    return Fraction(label_count) ** (len(block) - 3)


def pair_weight(
    atom_sizes: tuple[int, ...], left: Partition, right: Partition
) -> Fraction:
    answer = Fraction(1)
    for block in left + right:
        answer *= block_weight(atom_sizes, block)
    return answer


def incidence_data(
    count: int, left: Partition, right: Partition
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    left_end = [-1] * count
    right_end = [-1] * count
    for vertex, block in enumerate(left):
        for edge in block:
            left_end[edge] = vertex
    for vertex, block in enumerate(right):
        for edge in block:
            right_end[edge] = vertex
    assert min(left_end) >= 0 and min(right_end) >= 0
    return tuple(left_end), tuple(right_end)


def connected_pair(count: int, left: Partition, right: Partition) -> bool:
    """Connectivity of the edge-labelled bipartite incidence multigraph."""
    left_end, right_end = incidence_data(count, left, right)
    vertices = [(0, index) for index in range(len(left))] + [
        (1, index) for index in range(len(right))
    ]
    adjacency = {vertex: set() for vertex in vertices}
    for edge in range(count):
        l_vertex = (0, left_end[edge])
        r_vertex = (1, right_end[edge])
        adjacency[l_vertex].add(r_vertex)
        adjacency[r_vertex].add(l_vertex)
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        current = stack.pop()
        for neighbour in adjacency[current]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return len(seen) == len(vertices)


def unique_core_audit(
    count: int, left: Partition, right: Partition
) -> dict:
    """Find the unique multigraph core by degree-one pruning.

    The input is required to be connected with E=V.  Parallel edges are kept
    as distinct labelled entries, so a two-edge cycle survives pruning.
    """
    left_end, right_end = incidence_data(count, left, right)
    vertices = [(0, index) for index in range(len(left))] + [
        (1, index) for index in range(len(right))
    ]
    incident: dict[tuple[int, int], list[int]] = {vertex: [] for vertex in vertices}
    endpoints = []
    for edge in range(count):
        pair = ((0, left_end[edge]), (1, right_end[edge]))
        endpoints.append(pair)
        incident[pair[0]].append(edge)
        incident[pair[1]].append(edge)
    alive = [True] * count
    degree = {vertex: len(edges) for vertex, edges in incident.items()}
    queue = [vertex for vertex, value in degree.items() if value == 1]
    cursor = 0
    while cursor < len(queue):
        vertex = queue[cursor]
        cursor += 1
        if degree[vertex] != 1:
            continue
        edge = next(edge for edge in incident[vertex] if alive[edge])
        alive[edge] = False
        for endpoint in endpoints[edge]:
            degree[endpoint] -= 1
            if degree[endpoint] == 1:
                queue.append(endpoint)
    core = tuple(edge for edge, status in enumerate(alive) if status)
    core_vertices = {
        endpoint for edge in core for endpoint in endpoints[edge]
    }
    if len(core) < 2 or len(core) % 2:
        raise AssertionError(("bad_core_size", left, right, core))
    if any(
        sum(alive[edge] for edge in incident[vertex]) != 2
        for vertex in core_vertices
    ):
        raise AssertionError(("core_not_cycle", left, right, core))

    # The least edge and its left endpoint canonically orient the cycle.
    first = min(core)
    first_left = (0, left_end[first])
    second = next(
        edge for edge in incident[first_left] if alive[edge] and edge != first
    )
    sequence = [first, second]
    while len(sequence) < len(core):
        previous_index = len(sequence) - 1
        previous = sequence[-1]
        vertex = (
            (1, right_end[previous])
            if previous_index % 2 == 1
            else (0, left_end[previous])
        )
        following = next(
            edge for edge in incident[vertex] if alive[edge] and edge != previous
        )
        if following in sequence:
            raise AssertionError(("premature_core_closure", sequence, following))
        sequence.append(following)
    last = sequence[-1]
    closing_vertex = (1, right_end[last])
    closing = next(
        edge for edge in incident[closing_vertex] if alive[edge] and edge != last
    )
    if closing != first:
        raise AssertionError(("core_does_not_close", sequence, closing))

    expected_left = [
        {sequence[index], sequence[index + 1]}
        for index in range(0, len(sequence), 2)
    ]
    expected_right = [
        {sequence[index], sequence[(index + 1) % len(sequence)]}
        for index in range(1, len(sequence), 2)
    ]
    actual_left = [
        {edge for edge in core if left_end[edge] == vertex}
        for vertex in sorted({left_end[edge] for edge in core})
    ]
    actual_right = [
        {edge for edge in core if right_end[edge] == vertex}
        for vertex in sorted({right_end[edge] for edge in core})
    ]
    normalize = lambda blocks: sorted(tuple(sorted(block)) for block in blocks)
    if normalize(expected_left) != normalize(actual_left):
        raise AssertionError(("left_orientation_mismatch", sequence, left, right))
    if normalize(expected_right) != normalize(actual_right):
        raise AssertionError(("right_orientation_mismatch", sequence, left, right))

    # Delete core edges.  Every nontrivial remaining component must meet one
    # and only one core vertex.  This is the unique root assignment used by
    # the planted-tree product.
    off_core = [edge for edge in range(count) if not alive[edge]]
    off_adjacency = {vertex: [] for vertex in vertices}
    for edge in off_core:
        for endpoint in endpoints[edge]:
            off_adjacency[endpoint].append(edge)
    visited_edges: set[int] = set()
    component_root_counts = []
    for initial_edge in off_core:
        if initial_edge in visited_edges:
            continue
        component_edges: set[int] = set()
        component_vertices: set[tuple[int, int]] = set()
        edge_stack = [initial_edge]
        while edge_stack:
            edge = edge_stack.pop()
            if edge in component_edges:
                continue
            component_edges.add(edge)
            visited_edges.add(edge)
            for vertex in endpoints[edge]:
                component_vertices.add(vertex)
                edge_stack.extend(off_adjacency[vertex])
        roots = component_vertices.intersection(core_vertices)
        component_root_counts.append(len(roots))
        if len(roots) != 1:
            raise AssertionError(("nonunique_tree_root", left, right, component_edges, roots))
        if len(component_edges) != len(component_vertices) - 1:
            raise AssertionError(("attachment_not_tree", left, right, component_edges))
    return {
        "core": core,
        "sequence": tuple(sequence),
        "off_core_component_root_counts": tuple(component_root_counts),
    }


def multiply(first: Poly, second: Poly) -> Poly:
    output: Poly = {}
    for (left, right), value in first.items():
        for (left2, right2), value2 in second.items():
            key = (left + left2, right + right2)
            output[key] = output.get(key, Fraction(0)) + value * value2
    return output


def add_scaled(
    target: Poly, source: Poly, factor: Fraction = Fraction(1), shift=(0, 0)
) -> None:
    for (left, right), value in source.items():
        key = (left + shift[0], right + shift[1])
        target[key] = target.get(key, Fraction(0)) + factor * value


def positive_profiles(atom_sizes: tuple[int, ...]) -> dict[int, Poly]:
    """The M133 positive recurrence, freshly implemented from its statement."""
    edges = tuple(range(len(atom_sizes)))

    @functools.cache
    def planted(
        colour: int, boundary: tuple[int, ...], internal: tuple[int, ...]
    ) -> tuple[tuple[tuple[int, int], Fraction], ...]:
        answer: Poly = {}
        for branches in partitions_of_items(internal):
            root_choices = itertools.product(*branches) if branches else [()]
            for roots in root_choices:
                incident = tuple(sorted(boundary + tuple(roots)))
                product: Poly = {(0, 0): Fraction(1)}
                for branch, root in zip(branches, roots):
                    descendants = tuple(edge for edge in branch if edge != root)
                    product = multiply(
                        product,
                        dict(planted(1 - colour, (root,), descendants)),
                    )
                shift = (1, 0) if colour == 0 else (0, 1)
                add_scaled(
                    answer,
                    product,
                    factor=block_weight(atom_sizes, incident),
                    shift=shift,
                )
        return tuple(sorted(answer.items()))

    profiles: dict[int, Poly] = {}
    edge_set = set(edges)
    for core_size in range(2, len(edges) + 1, 2):
        answer: Poly = {}
        for core in itertools.combinations(edges, core_size):
            first = min(core)
            others = tuple(edge for edge in core if edge != first)
            off_core = tuple(sorted(edge_set.difference(core)))
            for tail in itertools.permutations(others):
                sequence = (first,) + tail
                vertices = [
                    (0, (sequence[index], sequence[index + 1]))
                    for index in range(0, core_size, 2)
                ] + [
                    (1, (sequence[index], sequence[(index + 1) % core_size]))
                    for index in range(1, core_size, 2)
                ]
                for destinations in itertools.product(
                    range(core_size), repeat=len(off_core)
                ):
                    assigned = [[] for _ in range(core_size)]
                    for edge, destination in zip(off_core, destinations):
                        assigned[destination].append(edge)
                    product: Poly = {(0, 0): Fraction(1)}
                    for index, (colour, boundary) in enumerate(vertices):
                        product = multiply(
                            product,
                            dict(
                                planted(
                                    colour,
                                    tuple(sorted(boundary)),
                                    tuple(sorted(assigned[index])),
                                )
                            ),
                        )
                    add_scaled(answer, product)
        profiles[core_size] = answer
    return profiles


def literal_profiles(atom_sizes: tuple[int, ...]) -> tuple[dict[int, Poly], dict]:
    """Literal partition pairs, classified by graph-pruned core length."""
    count = len(atom_sizes)
    profiles: dict[int, Poly] = {}
    connected_diagonal_pairs = 0
    two_edge_cores = 0
    attachment_components = 0
    for left in set_partitions(count):
        for right in set_partitions(count):
            if len(left) + len(right) != count:
                continue
            if not connected_pair(count, left, right):
                continue
            audit = unique_core_audit(count, left, right)
            core_size = len(audit["core"])
            value = pair_weight(atom_sizes, left, right)
            key = (len(left), len(right))
            profile = profiles.setdefault(core_size, {})
            profile[key] = profile.get(key, Fraction(0)) + value
            connected_diagonal_pairs += 1
            two_edge_cores += core_size == 2
            attachment_components += len(audit["off_core_component_root_counts"])
    return profiles, {
        "connected_diagonal_pairs": connected_diagonal_pairs,
        "two_edge_core_pairs": two_edge_cores,
        "off_core_components_checked": attachment_components,
    }


def total_poly(profiles: dict[int, Poly]) -> Poly:
    answer: Poly = {}
    for profile in profiles.values():
        add_scaled(answer, profile)
    return answer


def orientation_inventory(max_core: int) -> list[dict]:
    """Check that fixed-first sequences encode coloured cores injectively."""
    records = []
    for core_size in range(2, max_core + 1, 2):
        keys: dict[tuple, int] = {}
        for tail in itertools.permutations(range(1, core_size)):
            sequence = (0,) + tail
            left = tuple(
                sorted(
                    tuple(sorted((sequence[index], sequence[index + 1])))
                    for index in range(0, core_size, 2)
                )
            )
            right = tuple(
                sorted(
                    tuple(
                        sorted((sequence[index], sequence[(index + 1) % core_size]))
                    )
                    for index in range(1, core_size, 2)
                )
            )
            key = (left, right)
            keys[key] = keys.get(key, 0) + 1
        records.append(
            {
                "core_size": core_size,
                "sequences": math.factorial(core_size - 1),
                "distinct_coloured_cores": len(keys),
                "maximum_multiplicity": max(keys.values()),
                "two_parallel_edge_boundary": core_size == 2,
            }
        )
    return records


def permutation_type_count(d: int, cycle_type: tuple[int, ...]) -> int:
    denominator = 1
    for size in set(cycle_type):
        multiplicity = cycle_type.count(size)
        denominator *= size**multiplicity * math.factorial(multiplicity)
    return math.factorial(d) // denominator


def atom_factor(size: int) -> Fraction:
    return Fraction(size**size, math.factorial(size - 1)) ** 2


def weighted_core_masses(
    d: int, cycle_type: tuple[int, ...], profiles: dict[int, Poly]
) -> dict[int, Fraction]:
    cycles = len(cycle_type)
    multiplier = Fraction(permutation_type_count(d, cycle_type))
    for size in cycle_type:
        multiplier *= atom_factor(size)
    answer: dict[int, Fraction] = {}
    for core_size, polynomial in profiles.items():
        subtotal = Fraction(0)
        for left in range(1, cycles):
            right = cycles - left
            coefficient = polynomial.get((left, right), Fraction(0))
            if coefficient:
                cut = d + cycles - 2 * left
                subtotal += (
                    multiplier
                    * math.factorial(cut)
                    * math.factorial(2 * d - cut)
                    * coefficient
                )
        answer[core_size] = subtotal
    return answer


def zero_matrix(size: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def freeze_matrix(matrix: list[list[Fraction]]) -> Matrix:
    return tuple(tuple(row) for row in matrix)


def outer(values: tuple[Fraction, ...]) -> Matrix:
    return tuple(tuple(left * right for right in values) for left in values)


def subtract_convolution(
    target: list[list[Fraction]],
    first: Matrix,
    second: Matrix,
    multiplicity: int,
) -> None:
    for left, row in enumerate(first):
        for right, value in enumerate(row):
            if not value:
                continue
            for left2, row2 in enumerate(second):
                for right2, value2 in enumerate(row2):
                    if value2:
                        target[left + left2][right + right2] -= (
                            multiplicity * value * value2
                        )


def multiset_connected_polynomial(atom_sizes: tuple[int, ...]) -> Matrix:
    """Fresh equal-size aggregation with a dynamic root-type convention."""
    sizes = tuple(sorted(set(atom_sizes)))
    initial = tuple(atom_sizes.count(size) for size in sizes)

    def root_index(counts: tuple[int, ...]) -> int:
        # Deliberately differs from both frozen M125's smallest-present and
        # M129's largest-present convention: maximize current multiplicity,
        # breaking ties toward the smaller atom size.
        return max(
            (index for index, count in enumerate(counts) if count),
            key=lambda index: (counts[index], -sizes[index]),
        )

    def rooted_submultisets(counts: tuple[int, ...]):
        root = root_index(counts)
        available = list(counts)
        available[root] -= 1
        for extras in itertools.product(*(range(value + 1) for value in available)):
            component = list(extras)
            component[root] += 1
            multiplicity = math.prod(
                math.comb(available[index], extras[index])
                for index in range(len(sizes))
            )
            yield tuple(component), multiplicity

    @functools.cache
    def one_colour(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        atoms = sum(counts)
        if atoms == 0:
            return (Fraction(1),)
        answer = [Fraction(0) for _ in range(atoms + 1)]
        for block, multiplicity in rooted_submultisets(counts):
            block_atoms = sum(block)
            labels = sum(size * value for size, value in zip(sizes, block))
            weight = Fraction(labels) ** (block_atoms - 3)
            remainder = tuple(
                counts[index] - block[index] for index in range(len(sizes))
            )
            for number, value in enumerate(one_colour(remainder)):
                answer[number + 1] += multiplicity * weight * value
        return tuple(answer)

    @functools.cache
    def arbitrary(counts: tuple[int, ...]) -> Matrix:
        return outer(one_colour(counts))

    @functools.cache
    def connected(counts: tuple[int, ...]) -> Matrix:
        answer = [list(row) for row in arbitrary(counts)]
        for component, multiplicity in rooted_submultisets(counts):
            if component == counts:
                continue
            remainder = tuple(
                counts[index] - component[index]
                for index in range(len(sizes))
            )
            subtract_convolution(
                answer,
                connected(component),
                arbitrary(remainder),
                multiplicity,
            )
        return freeze_matrix(answer)

    return connected(initial)


def type_mass(
    d: int, cycle_type: tuple[int, ...], incidence: Matrix
) -> Fraction:
    cycles = len(cycle_type)
    multiplier = Fraction(permutation_type_count(d, cycle_type))
    for size in cycle_type:
        multiplier *= atom_factor(size)
    answer = Fraction(0)
    for left in range(1, cycles):
        right = cycles - left
        coefficient = incidence[left][right]
        if coefficient:
            cut = d + cycles - 2 * left
            answer += (
                multiplier
                * math.factorial(cut)
                * math.factorial(2 * d - cut)
                * coefficient
            )
    return answer


def small_audit(max_d: int, direct_max_d: int) -> dict:
    failures: list[dict] = []
    cases = []
    aggregate: dict[int, dict[int, dict[int, Fraction]]] = {}
    literal_pair_count = 0
    literal_type_count = 0
    for d in range(2, max_d + 1):
        aggregate[d] = {}
        for cycle_type in integer_partitions(d):
            cycles = len(cycle_type)
            if cycles < 2:
                continue
            failures_before = len(failures)
            positive = positive_profiles(cycle_type)
            direct = None
            graph_stats = None
            if d <= direct_max_d:
                direct, graph_stats = literal_profiles(cycle_type)
                literal_type_count += 1
                literal_pair_count += len(set_partitions(cycles)) ** 2
                if direct != positive:
                    failures.append(
                        {
                            "kind": "literal_vs_positive",
                            "cycle_type": cycle_type,
                            "literal": stringify_profiles(direct),
                            "positive": stringify_profiles(positive),
                        }
                    )
            connected = multiset_connected_polynomial(cycle_type)
            diagonal = {
                (left, cycles - left): connected[left][cycles - left]
                for left in range(1, cycles)
                if connected[left][cycles - left]
            }
            if total_poly(positive) != diagonal:
                failures.append(
                    {
                        "kind": "positive_vs_connected_recurrence",
                        "cycle_type": cycle_type,
                    }
                )
            masses = weighted_core_masses(d, cycle_type, positive)
            aggregate[d].setdefault(cycles, {})
            for core_size, value in masses.items():
                aggregate[d][cycles][core_size] = (
                    aggregate[d][cycles].get(core_size, Fraction(0)) + value
                )
            cases.append(
                {
                    "d": d,
                    "cycle_type": cycle_type,
                    "literal_checked": direct is not None,
                    "graph_stats": graph_stats,
                    "positive_coefficients": sum(len(poly) for poly in positive.values()),
                    "match": len(failures) == failures_before,
                }
            )
        print(f"small d={d} complete", flush=True)

    serialized_aggregate = {
        str(d): {
            str(cycles): {
                str(core): fraction_text(value)
                for core, value in sorted(profile.items())
            }
            for cycles, profile in sorted(rows.items())
        }
        for d, rows in sorted(aggregate.items())
    }
    d4 = aggregate[4]
    core2 = [d4[cycles].get(2, Fraction(0)) for cycles in (2, 3, 4)]
    core4 = [d4[cycles].get(4, Fraction(0)) for cycles in (2, 3, 4)]
    polarized = (
        2 * core2[1] * core4[1]
        - core2[0] * core4[2]
        - core4[0] * core2[2]
    )
    expected_core2 = [Fraction(80136), Fraction(109440), Fraction(44928)]
    expected_core4 = [Fraction(0), Fraction(0), Fraction(216)]
    if core2 != expected_core2 or core4 != expected_core4:
        failures.append({"kind": "d4_profile_mismatch"})
    if polarized != -17309376:
        failures.append(
            {"kind": "d4_polarization_mismatch", "value": str(polarized)}
        )

    frozen = json.loads((M133 / "core_profile_results.json").read_text())
    frozen_profiles: dict[int, dict[int, dict[int, Fraction]]] = {}
    for record in frozen["records"]:
        d = int(record["d"])
        frozen_profiles[d] = {}
        for core, sequence in record["masses_by_core_and_cycles"].items():
            for cycles, value in sequence.items():
                frozen_profiles[d].setdefault(int(cycles), {})[int(core)] = Fraction(
                    value
                )
    # Build the same shape directly; this comparison is only a report-value
    # check, separate from all recurrence comparisons above.
    report_profile_mismatches = []
    for d, rows in aggregate.items():
        for cycles, profile in rows.items():
            for core, value in profile.items():
                frozen_value = frozen_profiles.get(d, {}).get(cycles, {}).get(
                    core, Fraction(0)
                )
                if value != frozen_value:
                    report_profile_mismatches.append(
                        {
                            "d": d,
                            "cycles": cycles,
                            "core": core,
                            "fresh": fraction_text(value),
                            "frozen": fraction_text(frozen_value),
                        }
                    )
    if report_profile_mismatches:
        failures.append(
            {
                "kind": "reported_core_profile_mismatch",
                "details": report_profile_mismatches,
            }
        )

    orientations = orientation_inventory(max_d if max_d % 2 == 0 else max_d - 1)
    if any(
        record["sequences"] != record["distinct_coloured_cores"]
        or record["maximum_multiplicity"] != 1
        for record in orientations
    ):
        failures.append({"kind": "core_sequence_not_injective"})
    return {
        "max_d": max_d,
        "direct_max_d": direct_max_d,
        "case_count": len(cases),
        "literal_type_count": literal_type_count,
        "literal_ordered_partition_pairs_examined": literal_pair_count,
        "orientation_inventory": orientations,
        "d4_core_2_profile": [fraction_text(value) for value in core2],
        "d4_core_4_profile": [fraction_text(value) for value in core4],
        "d4_pairwise_polarization_margin": fraction_text(polarized),
        "aggregate_profiles": serialized_aggregate,
        "reported_profile_mismatch_count": len(report_profile_mismatches),
        "failure_count": len(failures),
        "failures": failures,
        "cases": cases,
    }


def stringify_profiles(profiles: dict[int, Poly]) -> dict:
    return {
        str(core): {
            f"{left},{right}": fraction_text(value)
            for (left, right), value in sorted(polynomial.items())
        }
        for core, polynomial in sorted(profiles.items())
    }


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def load_frozen_frontier() -> dict[tuple[int, int], dict]:
    answer = {}
    for name in ("frontier_d23.json", "frontier_d24_d25.json", "frontier_d26.json"):
        payload = json.loads((M133 / name).read_text())
        for record in payload["records"]:
            answer[(record["d"], record["center_defect"])] = record
    return answer


def stored_frontier_consistency() -> dict:
    """Audit arithmetic and cycle-type counts in the frozen capped scans.

    This deliberately does not call the coefficient recurrence and is labelled
    separately from the independent recurrence recomputations.
    """
    failures = []
    records = []
    for (d, center_defect), record in sorted(load_frozen_frontier().items()):
        expected_counts = {}
        for defect in (center_defect - 1, center_defect, center_defect + 1):
            cycles = d - defect
            expected_counts[str(defect)] = sum(
                1 for _ in fixed_length_partitions(d, cycles)
            )
        masses = record["masses_by_defect"]
        lower = masses[str(center_defect - 1)]
        center = masses[str(center_defect)]
        upper = masses[str(center_defect + 1)]
        margin = center * center - lower * upper
        ratio = Fraction(center * center, lower * upper)
        checks = {
            "cycle_type_counts": expected_counts
            == record["cycle_type_counts_by_defect"],
            "margin": margin == record["lc_margin"],
            "ratio_numerator": ratio.numerator == record["lc_ratio_numerator"],
            "ratio_denominator": ratio.denominator
            == record["lc_ratio_denominator"],
            "positive_margin": margin > 0,
        }
        if not all(checks.values()):
            failures.append(
                {
                    "kind": "stored_frontier_internal_inconsistency",
                    "d": d,
                    "center_defect": center_defect,
                    "checks": checks,
                }
            )
        records.append(
            {
                "d": d,
                "center_defect": center_defect,
                "expected_cycle_type_counts": expected_counts,
                "checks": checks,
                "ratio_numerator": ratio.numerator,
                "ratio_denominator": ratio.denominator,
                "ratio_float": float(ratio),
            }
        )
    return {
        "scope": (
            "internal exact arithmetic and independent partition-type counts "
            "only; not an independent recomputation of the stored masses"
        ),
        "records": records,
        "failure_count": len(failures),
        "failures": failures,
    }


def frontier_audit(cases: list[tuple[int, int]]) -> dict:
    frozen = load_frozen_frontier()
    failures = []
    records = []
    mass_cache: dict[tuple[int, int], tuple[int, int]] = {}
    for d, center_defect in cases:
        started = time.time()
        masses = {}
        type_counts = {}
        for defect in (center_defect - 1, center_defect, center_defect + 1):
            key = (d, defect)
            if key not in mass_cache:
                cycles = d - defect
                total = Fraction(0)
                count = 0
                for cycle_type in fixed_length_partitions(d, cycles):
                    count += 1
                    total += type_mass(
                        d, cycle_type, multiset_connected_polynomial(cycle_type)
                    )
                if total.denominator != 1:
                    raise AssertionError(("frontier_noninteger", d, defect, total))
                mass_cache[key] = (total.numerator, count)
            masses[str(defect)], type_counts[str(defect)] = mass_cache[key]
        center = masses[str(center_defect)]
        lower = masses[str(center_defect - 1)]
        upper = masses[str(center_defect + 1)]
        margin = center * center - lower * upper
        ratio = Fraction(center * center, lower * upper)
        reference = frozen[(d, center_defect)]
        matches_frozen = (
            masses == reference["masses_by_defect"]
            and type_counts == reference["cycle_type_counts_by_defect"]
            and margin == reference["lc_margin"]
            and ratio.numerator == reference["lc_ratio_numerator"]
            and ratio.denominator == reference["lc_ratio_denominator"]
        )
        if not matches_frozen:
            failures.append(
                {
                    "kind": "frontier_mismatch",
                    "d": d,
                    "center_defect": center_defect,
                }
            )
        record = {
            "d": d,
            "center_defect": center_defect,
            "cycle_type_counts_by_defect": type_counts,
            "masses_by_defect": masses,
            "lc_margin": margin,
            "lc_ratio_numerator": ratio.numerator,
            "lc_ratio_denominator": ratio.denominator,
            "lc_ratio_float": float(ratio),
            "matches_frozen": matches_frozen,
            "elapsed_seconds": time.time() - started,
        }
        records.append(record)
        print(
            f"frontier d={d} r={center_defect} "
            f"ratio={float(ratio):.12g} match={matches_frozen}",
            flush=True,
        )
    return {
        "cases": [f"{d}:{defect}" for d, defect in cases],
        "records": records,
        "failure_count": len(failures),
        "failures": failures,
    }


def parse_case(text: str) -> tuple[int, int]:
    d_text, defect_text = text.split(":", 1)
    d, defect = int(d_text), int(defect_text)
    if d < 4 or not 1 <= defect <= d - 3:
        raise argparse.ArgumentTypeError(f"invalid case {text}")
    return d, defect


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--small-max-d", type=int, default=8)
    parser.add_argument("--direct-max-d", type=int, default=7)
    parser.add_argument("--skip-small", action="store_true")
    parser.add_argument("--frontier-case", action="append", type=parse_case, default=[])
    args = parser.parse_args()
    started = time.time()
    payload = {
        "claim_scope": (
            "fresh exact audit of M133; finite frontier signs are only finite "
            "facts and imply neither universal log-concavity nor a spectral gap"
        ),
        "target": "M113/M118 auxiliary incidence-key coefficients H[d,c]",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {
            "small_max_d": args.small_max_d,
            "direct_max_d": args.direct_max_d,
            "skip_small": args.skip_small,
            "frontier_case": [f"{d}:{r}" for d, r in args.frontier_case],
            "output": str(args.output),
        },
        "frozen_m133_hashes": {
            "report.md": sha256(M133 / "report.md"),
            "positive_unicycle_reduction.md": sha256(
                M133 / "positive_unicycle_reduction.md"
            ),
            "positive_unicycle_audit.py": sha256(M133 / "positive_unicycle_audit.py"),
            "positive_unicycle_results.json": sha256(
                M133 / "positive_unicycle_results.json"
            ),
            "core_profile_scan.py": sha256(M133 / "core_profile_scan.py"),
            "core_profile_results.json": sha256(M133 / "core_profile_results.json"),
            "freeze_manifest.md": sha256(M133 / "freeze_manifest.md"),
            "SHA256SUMS": sha256(M133 / "SHA256SUMS"),
        },
    }
    if not args.skip_small:
        payload["small_audit"] = small_audit(args.small_max_d, args.direct_max_d)
    payload["stored_frontier_consistency"] = stored_frontier_consistency()
    if args.frontier_case:
        payload["frontier_audit"] = frontier_audit(args.frontier_case)
    payload["failure_count"] = sum(
        payload[key]["failure_count"]
        for key in (
            "small_audit",
            "stored_frontier_consistency",
            "frontier_audit",
        )
        if key in payload
    )
    payload["elapsed_seconds"] = time.time() - started
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"failures={payload['failure_count']} "
        f"elapsed={payload['elapsed_seconds']:.3f}s",
        flush=True,
    )
    print(f"wrote {args.output} sha256={sha256(args.output)}", flush=True)


if __name__ == "__main__":
    main()
