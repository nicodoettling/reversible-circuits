#!/usr/bin/env python3
"""Fresh exact referee checker for M120.

The program imports no code from M120, M118, M113, or any other mission.  It
constructs the connected-unicyclic key space directly, obtains adjacent-cut
flows from independent one-sided genus-zero counts, and checks the formulas
and inequalities assigned to M124.  All reported arithmetic is exact.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import subprocess
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Partition = tuple[tuple[int, ...], ...]
Permutation = tuple[int, ...]
Key = tuple[int, Permutation, Partition, Partition]


FROZEN = {
    "report.md": "9f1cdd5f137b32b3ded80d951b6067565edac2ade9032d18cb0251e7c92803db",
    "incidence_gap_audit.py": "2649acb303c910f1d526f446572eb6fd674aa17c26c78bc175843fc76b94f368",
    "results.json": "9285dc8958a59cd62fccd2cd8cdc95053dd1ecb033c6a3562925962bc1af28f9",
    "checkpoint.md": "a5bff43d77a568255537b4db4f2faf33c6ee6ed538cf65f647398e59671d8580",
    "freeze_manifest.md": "9e70cb1f3db32ae602f99c7ff78e5800e66069ce893b546e7c3f46212a8f515b",
}
M120_DIR = Path(
    "experiments/20260811-polynomial-mixing-resolution/cycle-25/"
    "mission-M120-local-unicycle-incidence-gap"
)


def multiply(p: Permutation, q: Permutation) -> Permutation:
    """Return p*q with (p*q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def invert(p: Permutation) -> Permutation:
    ans = [0] * len(p)
    for x, image in enumerate(p):
        ans[image] = x
    return tuple(ans)


def swap_perm(d: int, edge: tuple[int, int]) -> Permutation:
    ans = list(range(d))
    x, y = edge
    ans[x], ans[y] = ans[y], ans[x]
    return tuple(ans)


def cycle_atoms(p: Permutation) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(p)))
    atoms = []
    while unseen:
        start = min(unseen)
        orbit = []
        x = start
        while x in unseen:
            unseen.remove(x)
            orbit.append(x)
            x = p[x]
        atoms.append(tuple(sorted(orbit)))
    return tuple(sorted(atoms, key=lambda a: (a[0], len(a), a)))


def index_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Set partitions in restricted-growth order."""
    answer: list[tuple[tuple[int, ...], ...]] = []

    def extend(x: int, blocks: list[list[int]]) -> None:
        if x == n:
            answer.append(tuple(tuple(block) for block in blocks))
            return
        for block in blocks:
            block.append(x)
            extend(x + 1, blocks)
            block.pop()
        blocks.append([x])
        extend(x + 1, blocks)
        blocks.pop()

    extend(0, [])
    return tuple(answer)


def lift_partition(
    atom_part: tuple[tuple[int, ...], ...], atoms: tuple[tuple[int, ...], ...]
) -> Partition:
    blocks = [
        tuple(sorted(label for atom_index in block for label in atoms[atom_index]))
        for block in atom_part
    ]
    return tuple(sorted(blocks, key=lambda b: b[0]))


def containing_block(partition: Partition, label: int) -> tuple[int, ...]:
    return next(block for block in partition if label in block)


def merge_blocks(partition: Partition, edge: tuple[int, int]) -> Partition:
    x, y = edge
    bx = containing_block(partition, x)
    by = containing_block(partition, y)
    if bx == by:
        return partition
    merged = tuple(sorted(bx + by))
    survivors = tuple(b for b in partition if b not in (bx, by))
    return tuple(sorted(survivors + (merged,), key=lambda b: b[0]))


def incidence_is_connected(atoms: tuple[tuple[int, ...], ...], left: Partition, right: Partition) -> bool:
    vertex_count = len(left) + len(right)
    adjacency = [[] for _ in range(vertex_count)]
    for atom in atoms:
        representative = atom[0]
        u = next(i for i, block in enumerate(left) if representative in block)
        v = len(left) + next(i for i, block in enumerate(right) if representative in block)
        adjacency[u].append(v)
        adjacency[v].append(u)
    visited = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return len(visited) == vertex_count


def build_keys(d: int) -> list[Key]:
    partition_cache = {c: index_partitions(c) for c in range(1, d + 1)}
    answer: list[Key] = []
    for p_raw in itertools.permutations(range(d)):
        p = tuple(p_raw)
        atoms = cycle_atoms(p)
        coarsenings = [lift_partition(part, atoms) for part in partition_cache[len(atoms)]]
        for left in coarsenings:
            for right in coarsenings:
                # E=c and connected-unicyclic require V=c.
                if len(left) + len(right) != len(atoms):
                    continue
                if not incidence_is_connected(atoms, left, right):
                    continue
                j = d + len(right) - len(left)
                answer.append((j, p, left, right))
    return sorted(set(answer))


def h(length: int) -> Fraction:
    return Fraction(length**length, math.factorial(length - 1))


def one_side_count(p: Permutation, partition: Partition, length: int) -> int:
    atoms = cycle_atoms(p)
    value = Fraction(math.factorial(length), 1)
    for block in partition:
        block_set = set(block)
        atom_count = sum(set(atom) <= block_set for atom in atoms)
        value *= Fraction(len(block), 1) ** (atom_count - 3)
    for atom in atoms:
        value *= h(len(atom))
    if value.denominator != 1:
        raise AssertionError((p, partition, length, value))
    return value.numerator


def counts_for_key(d: int, key: Key) -> tuple[int, int, int]:
    j, p, left, right = key
    prefix = one_side_count(p, left, j)
    suffix = one_side_count(p, right, 2 * d - j)
    return prefix, suffix, prefix * suffix


def adjacent_edges(
    d: int, keys: list[Key], counts: list[tuple[int, int, int]]
) -> dict[tuple[int, int], int]:
    """Generate every low-cut/high-cut overlap without pairwise cell scanning."""
    buckets: dict[tuple[int, Permutation], list[int]] = defaultdict(list)
    for i, (j, p, _, _) in enumerate(keys):
        buckets[(j, p)].append(i)
    transpositions = tuple(itertools.combinations(range(d), 2))
    trans_perms = {edge: swap_perm(d, edge) for edge in transpositions}
    edges: dict[tuple[int, int], int] = {}
    for low_i, (j, p, left, right) in enumerate(keys):
        for edge in transpositions:
            p_high = multiply(p, trans_perms[edge])
            for high_i in buckets.get((j + 1, p_high), ()):  # adjacent cut only
                _, _, left_high, right_high = keys[high_i]
                if merge_blocks(left, edge) != left_high:
                    continue
                if merge_blocks(right_high, edge) != right:
                    continue
                overlap = counts[low_i][0] * counts[high_i][1]
                old = edges.setdefault((low_i, high_i), overlap)
                if old != overlap:
                    raise AssertionError("inconsistent overlap generation")
    return edges


def pair_key(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def fraction_record(value: Fraction) -> dict[str, int | float]:
    return {"numerator": value.numerator, "denominator": value.denominator, "float": float(value)}


def key_record(key: Key) -> dict:
    return {
        "j": key[0],
        "p": list(key[1]),
        "Q_L": [list(block) for block in key[2]],
        "Q_R": [list(block) for block in key[3]],
    }


def split_off_singleton(source: Iterable[tuple[int, ...]], target: Iterable[tuple[int, ...]]) -> bool:
    old = [frozenset(atom) for atom in source]
    new = [frozenset(atom) for atom in target]
    if len(new) != len(old) + 1:
        return False
    for singleton in new:
        if len(singleton) != 1:
            continue
        for residual in new:
            if residual == singleton:
                continue
            merged = singleton | residual
            if merged not in old:
                continue
            old_rest = sorted((a for a in old if a != merged), key=lambda a: tuple(sorted(a)))
            new_rest = sorted((a for a in new if a not in (singleton, residual)), key=lambda a: tuple(sorted(a)))
            if old_rest == new_rest:
                return True
    return False


def singleton_edge(a: Key, b: Key) -> bool:
    aa, bb = cycle_atoms(a[1]), cycle_atoms(b[1])
    if len(aa) < len(bb):
        return split_off_singleton(aa, bb)
    if len(bb) < len(aa):
        return split_off_singleton(bb, aa)
    return False


def graph_component_count(size: int, edges: Iterable[tuple[int, int]]) -> int:
    parent = list(range(size))

    def root(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[rb] = ra
    return len({root(i) for i in range(size)})


def replace_by_singleton(partition: Partition, old: tuple[int, ...], x: int) -> Partition:
    residual = tuple(y for y in old if y != x)
    survivors = tuple(b for b in partition if b != old)
    return tuple(sorted(survivors + ((x,), residual), key=lambda b: b[0]))


def all_join_candidates(d: int, key: Key) -> list[tuple[Key, Fraction, str, int, int, int, int]]:
    """Candidate joins: target, formula, color, a, b, B, side length."""
    j, p, left, right = key
    atoms = cycle_atoms(p)
    output = []
    for block in right:
        incident = [a for a in atoms if set(a) <= set(block)]
        for first, second in itertools.combinations(incident, 2):
            if containing_block(left, first[0]) == containing_block(left, second[0]):
                continue
            edge = tuple(sorted((first[0], second[0])))
            target = (j + 1, multiply(p, swap_perm(d, edge)), merge_blocks(left, edge), right)
            ratio = h(len(first) + len(second)) / (h(len(first)) * h(len(second)))
            formula = ratio / (2 * (2 * d - j) * len(block))
            output.append((target, formula, "right", len(first), len(second), len(block), 2 * d - j))
    for block in left:
        incident = [a for a in atoms if set(a) <= set(block)]
        for first, second in itertools.combinations(incident, 2):
            if containing_block(right, first[0]) == containing_block(right, second[0]):
                continue
            edge = tuple(sorted((first[0], second[0])))
            target = (j - 1, multiply(p, swap_perm(d, edge)), left, merge_blocks(right, edge))
            ratio = h(len(first) + len(second)) / (h(len(first)) * h(len(second)))
            formula = ratio / (2 * j * len(block))
            output.append((target, formula, "left", len(first), len(second), len(block), j))
    return output


def check_binomial_inequality(d: int) -> dict:
    failures = []
    minimum_slack: Fraction | None = None
    tested = 0
    for n in range(2, d + 1):
        for a in range(1, n):
            b = n - a
            pmf = Fraction(math.comb(n, a) * (a**a) * (b**b), n**n)
            ratio = h(n) / (h(a) * h(b))
            identity_rhs = Fraction(n, a * b) / pmf
            inequalities = (
                pmf <= 1,
                ratio == identity_rhs,
                ratio >= Fraction(n, a * b),
                Fraction(n, a * b) >= Fraction(4, n),
                Fraction(4, n) >= Fraction(4, d),
            )
            if not all(inequalities):
                failures.append({"n": n, "a": a, "b": b, "pmf": str(pmf), "ratio": str(ratio)})
            slack = ratio / Fraction(4, d)
            minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
            tested += 1
    return {
        "tested_pairs": tested,
        "failures": failures,
        "minimum_ratio_over_4_over_d": fraction_record(minimum_slack or Fraction(1)),
    }


def check_case(d: int) -> dict:
    started = time.time()
    identity = tuple(range(d))
    keys = build_keys(d)
    index = {key: i for i, key in enumerate(keys)}
    counts = [counts_for_key(d, key) for key in keys]
    weights = [triple[2] for triple in counts]
    edges = adjacent_edges(d, keys, counts)
    undirected_overlap = {pair_key(a, b): overlap for (a, b), overlap in edges.items()}

    def transition(source: int, target: int) -> Fraction | None:
        overlap = undirected_overlap.get(pair_key(source, target))
        return None if overlap is None else Fraction(overlap, 2 * weights[source])

    off_diagonal = [Fraction(0) for _ in keys]
    upward = [Fraction(0) for _ in keys]
    downward = [Fraction(0) for _ in keys]
    singleton_rates = [Fraction(0) for _ in keys]
    edge_defect_failures = []
    level_overlaps: dict[tuple[int, int], int] = defaultdict(int)
    for (low, high), overlap in edges.items():
        r_low = d - len(cycle_atoms(keys[low][1]))
        r_high = d - len(cycle_atoms(keys[high][1]))
        if abs(r_low - r_high) != 1:
            edge_defect_failures.append((low, high, r_low, r_high))
        level_overlaps[tuple(sorted((r_low, r_high)))] += overlap
        for source, target, source_r, target_r in (
            (low, high, r_low, r_high),
            (high, low, r_high, r_low),
        ):
            rate = Fraction(overlap, 2 * weights[source])
            off_diagonal[source] += rate
            if target_r == source_r + 1:
                upward[source] += rate
            elif target_r == source_r - 1:
                downward[source] += rate
            if singleton_edge(keys[low], keys[high]):
                singleton_rates[source] += rate

    row_failures = [i for i, total in enumerate(off_diagonal) if total > 1]
    formula_failures = []
    split_tests = 0
    split_sources = set()
    split_values: list[Fraction] = []
    inv_cache = {p: invert(p) for _, p, _, _ in keys}
    for source_i, (j, p, left, right) in enumerate(keys):
        if p == identity:
            continue
        atoms = cycle_atoms(p)
        for atom in atoms:
            if len(atom) < 2:
                continue
            for x in atom:
                edge = tuple(sorted((x, inv_cache[p][x])))
                p_target = multiply(p, swap_perm(d, edge))
                old_block = containing_block(right, x)
                target = (j + 1, p_target, left, replace_by_singleton(right, old_block, x))
                target_i = index.get(target)
                a = len(atom)
                b = len(old_block)
                s = sum(set(other) <= set(old_block) for other in atoms)
                expected = Fraction(1, 2 * (2 * d - j))
                expected *= Fraction(a - 1, a) ** a
                expected *= Fraction(b - 1, b) ** (s - 3)
                actual = None if target_i is None else transition(source_i, target_i)
                if actual != expected or expected < Fraction(1, 64 * d):
                    formula_failures.append(
                        {
                            "kind": "singleton_split",
                            "source": key_record(keys[source_i]),
                            "target": key_record(target),
                            "actual": None if actual is None else str(actual),
                            "expected": str(expected),
                        }
                    )
                split_tests += 1
                split_sources.add(source_i)
                split_values.append(expected)

    identity_reverse_failures = []
    identity_candidate_counts = {}
    identity_values: list[Fraction] = []
    join_formula_failures = []
    join_values: list[Fraction] = []
    join_sources = set()
    join_tests = 0
    for source_i, key in enumerate(keys):
        atoms = cycle_atoms(key[1])
        candidates = all_join_candidates(d, key)
        if len(atoms) >= 3:
            if not candidates:
                join_formula_failures.append({"kind": "missing_join", "source": key_record(key)})
            for target, expected, color, a, b, block_size, side_length in candidates:
                target_i = index.get(target)
                actual = None if target_i is None else transition(source_i, target_i)
                n = a + b
                pmf = Fraction(math.comb(n, a) * a**a * b**b, n**n)
                ratio = h(n) / (h(a) * h(b))
                inequality_ok = (
                    ratio == Fraction(n, a * b) / pmf
                    and pmf <= 1
                    and ratio >= Fraction(4, d)
                    and expected >= Fraction(1, d**3)
                )
                if actual != expected or not inequality_ok:
                    join_formula_failures.append(
                        {
                            "kind": f"{color}_join",
                            "source": key_record(key),
                            "target": key_record(target),
                            "actual": None if actual is None else str(actual),
                            "expected": str(expected),
                            "a": a,
                            "b": b,
                            "B": block_size,
                            "side_length": side_length,
                            "pmf": str(pmf),
                        }
                    )
                join_tests += 1
                join_sources.add(source_i)
                join_values.append(expected)

        if key[1] == identity and d >= 3:
            identity_candidate_counts[str(source_i)] = len(candidates)
            if not candidates:
                identity_reverse_failures.append({"kind": "missing_identity_reverse", "source": key_record(key)})
            for target, expected, color, a, b, block_size, side_length in candidates:
                specialized = Fraction(2, side_length * block_size)
                target_i = index.get(target)
                actual = None if target_i is None else transition(source_i, target_i)
                if a != 1 or b != 1 or expected != specialized or actual != specialized or specialized < Fraction(1, d * d):
                    identity_reverse_failures.append(
                        {
                            "kind": f"identity_{color}_reverse",
                            "source": key_record(key),
                            "target": key_record(target),
                            "actual": None if actual is None else str(actual),
                            "expected": str(specialized),
                        }
                    )
                identity_values.append(specialized)

    required_split_sources = {i for i, key in enumerate(keys) if key[1] != identity}
    required_join_sources = {i for i, key in enumerate(keys) if len(cycle_atoms(key[1])) >= 3}
    state_bound_failures = {
        "nonidentity_split_construction_missing": sorted(required_split_sources - split_sources),
        "nontop_join_construction_missing": sorted(required_join_sources - join_sources),
        "downward_rate": [
            i
            for i, key in enumerate(keys)
            if d - len(cycle_atoms(key[1])) >= 1 and downward[i] < Fraction(1, 64 * d)
        ],
        "upward_rate": [
            i
            for i, key in enumerate(keys)
            if d - len(cycle_atoms(key[1])) <= d - 3 and upward[i] < Fraction(1, d**3)
        ],
        "singleton_aggregate": [
            i for i in range(len(keys)) if d >= 3 and singleton_rates[i] < Fraction(1, 64 * d * d)
        ],
    }

    level_weight: dict[int, int] = defaultdict(int)
    for i, key in enumerate(keys):
        level_weight[d - len(cycle_atoms(key[1]))] += weights[i]
    observed_levels = sorted(level_weight)
    expected_levels = list(range(d - 1))
    level_records = []
    projected_failures = []
    for r in expected_levels:
        weight = level_weight.get(r, 0)
        if not weight:
            projected_failures.append({"kind": "missing_level", "r": r})
            continue
        down = None if r == 0 else Fraction(level_overlaps[(r - 1, r)], 2 * weight)
        up = None if r == d - 2 else Fraction(level_overlaps[(r, r + 1)], 2 * weight)
        if down is not None and down < Fraction(1, 64 * d):
            projected_failures.append({"kind": "down_bound", "r": r, "value": str(down)})
        if up is not None and up < Fraction(1, d**3):
            projected_failures.append({"kind": "up_bound", "r": r, "value": str(up)})
        if r < d - 2:
            next_weight = level_weight[r + 1]
            next_down = Fraction(level_overlaps[(r, r + 1)], 2 * next_weight)
            if weight * up != next_weight * next_down:
                projected_failures.append({"kind": "detailed_balance", "r": r})
        level_records.append(
            {
                "r": r,
                "weight": weight,
                "down": None if down is None else fraction_record(down),
                "up": None if up is None else fraction_record(up),
            }
        )

    sequence = [level_weight[r] for r in expected_levels]
    maximum = max(sequence)
    first_mode = sequence.index(maximum)
    last_mode = len(sequence) - 1 - list(reversed(sequence)).index(maximum)
    unimodal = (
        all(sequence[i] <= sequence[i + 1] for i in range(first_mode))
        and all(sequence[i] == maximum for i in range(first_mode, last_mode + 1))
        and all(sequence[i] >= sequence[i + 1] for i in range(last_mode, len(sequence) - 1))
    )
    log_concave = all(sequence[i] ** 2 >= sequence[i - 1] * sequence[i + 1] for i in range(1, len(sequence) - 1))

    singleton_pairs = [pair for pair in undirected_overlap if singleton_edge(keys[pair[0]], keys[pair[1]])]
    exception_ok = None
    if d == 2:
        exception_ok = (
            len(keys) == 1
            and not edges
            and keys[0][1] == identity
            and observed_levels == [0]
            and off_diagonal[0] == 0
        )

    failures = {
        "row": row_failures,
        "edge_defect": edge_defect_failures,
        "singleton_formula": formula_failures,
        "identity_reverse": identity_reverse_failures,
        "join_formula": join_formula_failures,
        "state_bounds": state_bound_failures,
        "projection": projected_failures,
    }
    failure_count = sum(
        len(value) if isinstance(value, list) else sum(len(v) for v in value.values())
        for value in failures.values()
    )
    return {
        "d": d,
        "keys": len(keys),
        "undirected_edges": len(edges),
        "components": graph_component_count(len(keys), edges),
        "singleton_skeleton_edges": len(singleton_pairs),
        "singleton_skeleton_components": graph_component_count(len(keys), singleton_pairs),
        "total_stationary_weight": sum(weights),
        "maximum_off_diagonal_rate": fraction_record(max(off_diagonal)),
        "minimum_singleton_aggregate_rate": fraction_record(min(singleton_rates)),
        "minimum_downward_rate_nonbottom": None
        if d == 2
        else fraction_record(min(downward[i] for i, key in enumerate(keys) if d - len(cycle_atoms(key[1])) >= 1)),
        "minimum_upward_rate_nontop": None
        if d == 2
        else fraction_record(min(upward[i] for i, key in enumerate(keys) if d - len(cycle_atoms(key[1])) <= d - 3)),
        "singleton_formula_tests": split_tests,
        "minimum_singleton_formula_rate": None if not split_values else fraction_record(min(split_values)),
        "identity_keys": sum(key[1] == identity for key in keys),
        "identity_reverse_formula_tests": len(identity_values),
        "minimum_identity_reverse_rate": None if not identity_values else fraction_record(min(identity_values)),
        "join_formula_tests": join_tests,
        "minimum_join_formula_rate": None if not join_values else fraction_record(min(join_values)),
        "observed_defect_levels": observed_levels,
        "defect_projection": level_records,
        "finite_defect_mass_unimodal": unimodal,
        "finite_defect_mass_log_concave": log_concave,
        "binomial_pmf_check": check_binomial_inequality(d),
        "d2_exception_ok": exception_ok,
        "failure_count": failure_count,
        "failures": failures,
        "elapsed_seconds": time.time() - started,
    }


def valley_attack(delta: Fraction = Fraction(1, 8), max_l: int = 10) -> dict:
    if not (0 < delta <= Fraction(1, 2)):
        raise ValueError("delta must lie in (0,1/2]")
    rows = []
    all_ok = True
    geometric_ratio = 2 * delta
    for length in range(1, max_l + 1):
        last = 2 * length
        right = [Fraction(0) for _ in range(last + 1)]
        left = [Fraction(0) for _ in range(last + 1)]
        for state in range(last + 1):
            if state < last:
                right[state] = delta if state < length else Fraction(1, 2)
            if state > 0:
                left[state] = Fraction(1, 2) if state <= length else delta
        holds = [1 - right[i] - left[i] for i in range(last + 1)]
        weights = [Fraction(1)]
        for state in range(last):
            weights.append(weights[-1] * right[state] / left[state + 1])
        balance_ok = all(weights[i] * right[i] == weights[i + 1] * left[i + 1] for i in range(last))
        shape_ok = all(weights[i] == geometric_ratio ** min(i, last - i) for i in range(last + 1))
        rate_floor = min(rate for rate in right + left if rate)
        boundary = weights[length] * right[length]
        left_mass = sum(weights[: length + 1])
        right_mass = sum(weights[length + 1 :])
        conductance = boundary / min(left_mass, right_mass)
        scaled = conductance / (geometric_ratio**length)
        ok = balance_ok and shape_ok and rate_floor >= delta and min(holds) >= 0
        all_ok &= ok
        rows.append(
            {
                "L": length,
                "rate_floor": fraction_record(rate_floor),
                "middle_weight_relative_to_endpoint": fraction_record(weights[length]),
                "middle_cut_conductance": fraction_record(conductance),
                "conductance_over_(2delta)^L": fraction_record(scaled),
                "detailed_balance_ok": balance_ok,
                "geometric_shape_ok": shape_ok,
                "nonnegative_holding_ok": min(holds) >= 0,
            }
        )
    return {
        "delta": fraction_record(delta),
        "geometric_ratio_2delta": fraction_record(geometric_ratio),
        "all_checks_pass": all_ok,
        "cases": rows,
    }


def frozen_hashes() -> dict:
    rows = {}
    for name, expected in FROZEN.items():
        path = M120_DIR / name
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        rows[name] = {"expected": expected, "observed": observed, "match": expected == observed}
    return {"all_match": all(row["match"] for row in rows.values()), "files": rows}


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", nargs="+", type=int, default=[2, 3, 4, 5])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(d < 2 or d > 5 for d in args.d):
        raise SystemExit("fresh exact audit is restricted to 2<=d<=5")
    started = time.time()
    integrity = frozen_hashes()
    cases = [check_case(d) for d in args.d]
    valley = valley_attack()
    payload = {
        "scope": "exact finite referee reconstruction and universal-formula falsification; no spectral-gap inference",
        "target": "rho(kappa)=|C_kappa|/Z_inc on realizable connected-unicyclic keys",
        "kernel": "Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2 Z_inc), unused row mass held",
        "convention": "(p q)(x)=p(q(x)); factors multiply left-to-right",
        "independence": "imports no M120/M118/M113 code and enumerates no transposition words",
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "arguments": {"d": args.d, "output": str(args.output)},
        "frozen_integrity": integrity,
        "cases": cases,
        "exponential_valley": valley,
        "all_checks_pass": (
            integrity["all_match"]
            and all(case["failure_count"] == 0 for case in cases)
            and all(case["binomial_pmf_check"]["failures"] == [] for case in cases)
            and all(case["d2_exception_ok"] is not False for case in cases)
            and valley["all_checks_pass"]
        ),
        "elapsed_seconds": time.time() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
