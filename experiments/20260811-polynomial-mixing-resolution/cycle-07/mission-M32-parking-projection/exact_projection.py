#!/usr/bin/env python3
"""Exact falsifier for Dyck edges in the minimal parking-multiset projection."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path


Perm = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n: int, edge: Edge) -> Perm:
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def parking_macro(word: tuple[int, ...], edges: list[Edge]) -> tuple[int, ...]:
    return tuple(sorted(edges[i][0] for i in word))


def stanley_labels(
    n: int, word: tuple[int, ...], edges: list[Edge]
) -> tuple[int, ...]:
    """Stanley's cover labels for the corresponding maximal NC chain."""
    blocks = [{i} for i in range(n)]
    labels = []
    for edge_index in word:
        a, b = edges[edge_index]
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        left, right = blocks[ia], blocks[ib]
        if min(left) > min(right):
            left, right = right, left
            ia, ib = ib, ia
        right_minimum = min(right)
        labels.append(max(x for x in left if x < right_minimum))
        merged = left | right
        blocks = [
            block for j, block in enumerate(blocks) if j not in (ia, ib)
        ]
        blocks.append(merged)
    return tuple(labels)


def is_parking(macro: tuple[int, ...]) -> bool:
    return all(value <= rank for rank, value in enumerate(macro))


def dyck_raises(macro: tuple[int, ...]) -> set[tuple[int, ...]]:
    r = len(macro)
    counts = Counter(macro)
    ans = set()
    for x in range(r - 1):
        if counts[x + 1] == 0:
            continue
        moved = list(macro)
        moved.remove(x + 1)
        moved.append(x)
        target = tuple(sorted(moved))
        assert is_parking(target)
        ans.add(target)
    return ans


def run(n: int) -> dict:
    r = n - 1
    edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
    perms = [transposition(n, e) for e in edges]
    identity = tuple(range(n))
    cycle = tuple(list(range(1, n)) + [0])

    pair_fibers: dict[Perm, list[tuple[int, int]]] = defaultdict(list)
    for i, p in enumerate(perms):
        for j, q in enumerate(perms):
            pair_fibers[compose(p, q)].append((i, j))

    words: list[tuple[int, ...]] = []
    orbit_words: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    by_labels: dict[tuple[int, ...], tuple[int, ...]] = {}
    for word in itertools.product(range(len(edges)), repeat=r):
        product = identity
        for i in word:
            product = compose(product, perms[i])
        if product != cycle:
            continue
        labels = tuple(edges[i][0] for i in word)
        if labels != stanley_labels(n, word, edges):
            raise AssertionError("raw lower endpoints disagree with Stanley labels")
        macro = tuple(sorted(labels))
        assert is_parking(macro)
        if labels in by_labels:
            raise AssertionError("Stanley parking labels were not injective")
        by_labels[labels] = word
        words.append(word)
        orbit_words[macro].append(word)

    if len(words) != n ** (n - 2):
        raise AssertionError("Dénes count mismatch")

    flow_counts: dict[tuple[int, ...], Counter] = defaultdict(Counter)
    sorted_source_counts: dict[tuple[int, ...], Counter] = defaultdict(Counter)
    per_word_source_counts: dict[tuple[int, ...], list[Counter]] = defaultdict(list)
    per_word_position_counts: dict[
        tuple[int, ...], list[list[Counter]]
    ] = defaultdict(list)
    per_word_labels: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    projected: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction] = {}
    sorted_boundary_witnesses = []
    for macro, source_words in orbit_words.items():
        total = Counter()
        for word in source_words:
            labels = tuple(edges[i][0] for i in word)
            source_counter = Counter()
            position_counters = []
            for pos in range(r - 1):
                position_counter = Counter()
                product = compose(perms[word[pos]], perms[word[pos + 1]])
                fiber = pair_fibers[product]
                for a, b in fiber:
                    target_word = word[:pos] + (a, b) + word[pos + 2 :]
                    target_macro = parking_macro(target_word, edges)
                    increment = Fraction(1, (r - 1) * len(fiber))
                    total[target_macro] += increment
                    source_counter[target_macro] += increment
                    position_counter[target_macro] += increment
                position_counters.append(position_counter)
            per_word_source_counts[macro].append(source_counter)
            per_word_position_counts[macro].append(position_counters)
            per_word_labels[macro].append(labels)
            if labels == macro:
                sorted_source_counts[macro] = source_counter
                counts = Counter(macro)
                for x in range(r - 1):
                    if not (counts[x] and counts[x + 1]):
                        continue
                    pos = max(i for i, value in enumerate(macro) if value == x)
                    assert macro[pos + 1] == x + 1
                    e1, e2 = edges[word[pos]], edges[word[pos + 1]]
                    sorted_boundary_witnesses.append(
                        {
                            "macro": list(macro),
                            "x": x,
                            "position": pos,
                            "factor_pair": [list(e1), list(e2)],
                            "shared_vertices": sorted(set(e1).intersection(e2)),
                        }
                    )
        for target, summed in total.items():
            projected[(macro, target)] = summed / len(source_words)
            flow_counts[macro][target] = summed

    adjacency = {macro: set() for macro in orbit_words}
    off_diagonal_rates = []
    for (source, target), rate in projected.items():
        if source != target and rate > 0:
            adjacency[source].add(target)
            off_diagonal_rates.append(rate)

    def shortest_paths(source: tuple[int, ...]):
        answer = {source: 0}
        parent = {source: None}
        queue = deque([source])
        while queue:
            here = queue.popleft()
            for there in adjacency[here]:
                if there not in answer:
                    answer[there] = answer[here] + 1
                    parent[there] = here
                    queue.append(there)
        return answer, parent

    missing_projection = []
    missing_sorted = []
    rates = []
    dyck_edge_microstate_stats = []
    dyck_route_lengths = []
    disconnected_dyck_routes = []
    detailed_balance_failures = []
    for macro, source_words in orbit_words.items():
        for target in sorted(dyck_raises(macro)):
            rate = projected.get((macro, target), Fraction(0))
            source_counts = Counter(macro)
            target_counts = Counter(target)
            lower_value = next(
                value for value in target_counts if target_counts[value] > source_counts[value]
            )
            higher_value = next(
                value for value in source_counts if source_counts[value] > target_counts[value]
            )
            word_rates = [counter[target] for counter in per_word_source_counts[macro]]
            positive_word_rates = [value for value in word_rates if value > 0]
            position_stats = []
            for pos in range(r - 1):
                rates_at_position = [
                    counters[pos][target]
                    for counters in per_word_position_counts[macro]
                ]
                positive_at_position = sum(value > 0 for value in rates_at_position)
                label_xy_at_position = sum(
                    {labels[pos], labels[pos + 1]} == {lower_value, higher_value}
                    for labels in per_word_labels[macro]
                )
                position_stats.append(
                    {
                        "position": pos,
                        "positive_microstates": positive_at_position,
                        "positive_fraction": str(
                            Fraction(positive_at_position, len(word_rates))
                        ),
                        "distinct_label_microstates": label_xy_at_position,
                    }
                )
            dyck_edge_microstate_stats.append(
                {
                    "source": list(macro),
                    "target": list(target),
                    "lower_value": lower_value,
                    "higher_value": higher_value,
                    "positive_microstates": len(positive_word_rates),
                    "total_microstates": len(word_rates),
                    "positive_fraction": str(
                        Fraction(len(positive_word_rates), len(word_rates))
                    ),
                    "minimum_positive_microstate_rate": (
                        str(min(positive_word_rates)) if positive_word_rates else None
                    ),
                    "maximum_microstate_rate": str(max(word_rates)),
                    "projected_rate": str(rate),
                    "position_stats": position_stats,
                }
            )
            if rate == 0:
                missing_projection.append([list(macro), list(target)])
            else:
                rates.append(rate)
            if sorted_source_counts[macro][target] == 0:
                missing_sorted.append([list(macro), list(target)])
            distance_map, parent = shortest_paths(macro)
            distance = distance_map.get(target)
            if distance is None:
                disconnected_dyck_routes.append([list(macro), list(target)])
            else:
                path = []
                cursor = target
                while cursor is not None:
                    path.append(list(cursor))
                    cursor = parent[cursor]
                path.reverse()
                dyck_route_lengths.append(
                    {
                        "source": list(macro),
                        "target": list(target),
                        "distance": distance,
                        "path": path,
                    }
                )
        for target in orbit_words:
            lhs = Fraction(len(source_words), len(words)) * projected.get(
                (macro, target), Fraction(0)
            )
            rhs = Fraction(len(orbit_words[target]), len(words)) * projected.get(
                (target, macro), Fraction(0)
            )
            if lhs != rhs:
                detailed_balance_failures.append(
                    [list(macro), list(target), str(lhs), str(rhs)]
                )

    return {
        "n": n,
        "factorization_count": len(words),
        "denes_expected": n ** (n - 2),
        "parking_macro_count": len(orbit_words),
        "all_parking_label_sequences_unique": len(by_labels) == len(words),
        "missing_projected_dyck_raises": missing_projection,
        "missing_sorted_representative_dyck_raises": missing_sorted,
        "projected_off_diagonal_edge_count": sum(map(len, adjacency.values())),
        "projected_edge_list": [
            {
                "source": list(source),
                "target": list(target),
                "rate": str(projected[(source, target)]),
            }
            for source in sorted(adjacency)
            for target in sorted(adjacency[source])
        ],
        "sorted_adjacent_value_boundary_witnesses": sorted_boundary_witnesses,
        "minimum_positive_off_diagonal_rate": (
            str(min(off_diagonal_rates)) if off_diagonal_rates else None
        ),
        "minimum_positive_projected_dyck_rate": (
            str(min(rates)) if rates else None
        ),
        "dyck_edge_microstate_stats": dyck_edge_microstate_stats,
        "minimum_rate_float": float(min(rates)) if rates else None,
        "maximum_dyck_edge_route_length": (
            max(x["distance"] for x in dyck_route_lengths)
            if dyck_route_lengths else None
        ),
        "longest_dyck_edge_routes": sorted(
            dyck_route_lengths, key=lambda x: x["distance"], reverse=True
        )[:20],
        "disconnected_dyck_routes": disconnected_dyck_routes,
        "detailed_balance_failures": detailed_balance_failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 3 <= args.n_max <= 6:
        raise SystemExit("exhaustive range is 3<=n-max<=6")
    result = {
        "claim_tested": (
            "Every adjacent Dyck raising edge occurs in the stationary-flow "
            "parking-multiset projection, and possibly from its sorted representative."
        ),
        "scope_warning": (
            "A missing edge refutes the corresponding universal claim; finite "
            "positive rates do not prove a universal rate or spectral gap."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "kernel": (
            "nonlazy uniform scan of exact same-product adjacent raw rank-two heat baths"
        ),
        "seed": None,
        "python": platform.python_version(),
        "records": [run(n) for n in range(3, args.n_max + 1)],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
