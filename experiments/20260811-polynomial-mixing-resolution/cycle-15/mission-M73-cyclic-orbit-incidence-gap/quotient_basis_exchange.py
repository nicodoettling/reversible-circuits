#!/usr/bin/env python3
"""Exact finite comparison of quotient UST exchange with quotient Hurwitz heat bath.

This is a bounded diagnostic.  It computes the *stationary-flow* quotient of
the uniform Cayley-tree down-up chain under the cyclic action induced through
Stanley's bijection, and routes its directed edges along deterministic shortest
paths in the quotient adjacent-rank heat-bath graph.

Convention: (p q)(x)=p(q(x)); factor tuples multiply left-to-right.
"""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

from cyclic_tree_action import Edge, conjugate_edge, minimal_words, stanley_tree, transpositions


def tree_exchange_neighbors(
    n: int, tree: tuple[Edge, ...]
) -> list[tuple[tuple[Edge, ...], int, int, Edge, Edge]]:
    """Return off-diagonal basis exchanges and cut sizes."""
    adjacency = [set() for _ in range(n)]
    for a, b in tree:
        adjacency[a].add(b)
        adjacency[b].add(a)
    tree_set = set(tree)
    answer = []
    for removed in tree:
        a0, b0 = removed
        stack = [a0]
        first = {a0}
        while stack:
            a = stack.pop()
            for b in adjacency[a]:
                if tuple(sorted((a, b))) == removed or b in first:
                    continue
                first.add(b)
                stack.append(b)
        second = set(range(n)) - first
        for a in sorted(first):
            for b in sorted(second):
                added = tuple(sorted((a, b)))
                if added == removed:
                    continue
                changed = tuple(sorted((tree_set - {removed}) | {added}))
                answer.append((changed, len(first), len(second), removed, added))
    return answer


def analyze(n: int) -> dict[str, object]:
    r = n - 1
    edges, gates = transpositions(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    trees = {
        word: stanley_tree(n, tuple(edges[index] for index in word))
        for word in words
    }
    tree_to_word = {tree: word for word, tree in trees.items()}
    if len(tree_to_word) != len(words):
        raise AssertionError("Stanley map is not a bijection")

    def cyclic_conjugate(word: tuple[int, ...]) -> tuple[int, ...]:
        target = tuple(
            edge_index[tuple(sorted(((edges[index][0] - 1) % n, (edges[index][1] - 1) % n)))]
            for index in word
        )
        if target not in word_set:
            raise AssertionError("cyclic conjugation left state space")
        return target

    orbit_id: dict[tuple[int, ...], int] = {}
    orbit_phase: dict[tuple[int, ...], int] = {}
    orbit_members: list[list[tuple[int, ...]]] = []
    representatives: list[tuple[int, ...]] = []
    for word in words:
        if word in orbit_id:
            continue
        oid = len(representatives)
        representatives.append(word)
        orbit_members.append([])
        current = word
        for phase in range(n):
            if current in orbit_id:
                raise AssertionError("cyclic action was not free")
            orbit_id[current] = oid
            orbit_phase[current] = phase
            orbit_members[oid].append(current)
            current = cyclic_conjugate(current)
        if current != word:
            raise AssertionError("cyclic action did not have order n")
    qstates = len(representatives)
    if qstates != n ** (n - 3):
        raise AssertionError("quotient state count mismatch")

    def hurwitz_right(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        changed[i] = word[i + 1]
        changed[i + 1] = edge_index[
            conjugate_edge(edges[word[i]], edges[word[i + 1]])
        ]
        target = tuple(changed)
        if target not in word_set:
            raise AssertionError("Hurwitz move left state space")
        return target

    def hurwitz_inverse(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        changed[i] = edge_index[
            conjugate_edge(edges[word[i + 1]], edges[word[i]])
        ]
        changed[i + 1] = word[i]
        target = tuple(changed)
        if target not in word_set:
            raise AssertionError("inverse Hurwitz move left state space")
        return target

    def one_bubble_targets(word: tuple[int, ...]) -> set[int]:
        targets = {orbit_id[word]}
        for start in range(r):
            current = word
            for i in range(start, r - 1):
                current = hurwitz_right(current, i)
                targets.add(orbit_id[current])
            current = word
            for i in range(start - 1, -1, -1):
                current = hurwitz_inverse(current, i)
                targets.add(orbit_id[current])
        return targets

    # Exact quotient L_n transition rates.  For each phase, the local fiber is
    # the orbit under sigma_i and has size two or three.
    lrate: dict[tuple[int, int], Fraction] = collections.defaultdict(Fraction)
    ladjacency = [set() for _ in range(qstates)]
    fiber_sizes = set()
    for word in words:
        source = orbit_id[word]
        for i in range(r - 1):
            fiber = []
            current = word
            while current not in fiber:
                fiber.append(current)
                current = hurwitz_right(current, i)
            if current != word:
                raise AssertionError("local Hurwitz orbit did not close at source")
            size = len(fiber)
            fiber_sizes.add(size)
            for target_word in fiber:
                target = orbit_id[target_word]
                lrate[(source, target)] += Fraction(1, n * (r - 1) * size)
                if source != target:
                    ladjacency[source].add(target)
                    ladjacency[target].add(source)
    if fiber_sizes - {2, 3}:
        raise AssertionError(f"unexpected local fiber sizes: {fiber_sizes}")
    for source in range(qstates):
        if sum(rate for (a, _), rate in lrate.items() if a == source) != 1:
            raise AssertionError("quotient L row failed to normalize")

    # Exact stationary-flow quotient of UST down-up under the same partition.
    urate: dict[tuple[int, int], Fraction] = collections.defaultdict(Fraction)
    micro_pair_count: dict[tuple[int, int], int] = collections.defaultdict(int)
    ideal_micro_edges = 0
    bubble_covered_micro_edges = 0
    first_bubble_failure = None
    exchange_cache: dict[tuple[Edge, ...], list[tuple[tuple[Edge, ...], int, int, Edge, Edge]]] = {}
    bubble_cache: dict[tuple[int, ...], set[int]] = {}
    for word in words:
        source = orbit_id[word]
        tree = trees[word]
        exchanges = exchange_cache.setdefault(tree, tree_exchange_neighbors(n, tree))
        bubbles = bubble_cache.setdefault(word, one_bubble_targets(word))
        # The deleted edge may be reinserted; collect that diagonal probability
        # once per tree edge.
        for removed in tree:
            adjacency = [set() for _ in range(n)]
            for a, b in tree:
                adjacency[a].add(b)
                adjacency[b].add(a)
            a0, _ = removed
            stack = [a0]
            component = {a0}
            while stack:
                a = stack.pop()
                for b in adjacency[a]:
                    if tuple(sorted((a, b))) == removed or b in component:
                        continue
                    component.add(b)
                    stack.append(b)
            cut = len(component) * (n - len(component))
            urate[(source, source)] += Fraction(1, n * r * cut)
        for target_tree, a, b, removed, added in exchanges:
            target_word = tree_to_word[target_tree]
            target = orbit_id[target_word]
            urate[(source, target)] += Fraction(1, n * r * a * b)
            if source != target:
                micro_pair_count[(source, target)] += 1
            ideal_micro_edges += 1
            if target in bubbles:
                bubble_covered_micro_edges += 1
            elif first_bubble_failure is None:
                first_bubble_failure = {
                    "source_word": word,
                    "target_word": target_word,
                    "source_tree": tree,
                    "target_tree": target_tree,
                    "removed_edge": removed,
                    "added_edge": added,
                }
    for source in range(qstates):
        if sum(rate for (a, _), rate in urate.items() if a == source) != 1:
            raise AssertionError("quotient UST row failed to normalize")

    # Confirm reversibility under the uniform orbit law.
    for (source, target), rate in urate.items():
        if urate[(target, source)] != rate:
            raise AssertionError("quotient UST is not symmetric")
    for (source, target), rate in lrate.items():
        if lrate[(target, source)] != rate:
            raise AssertionError("quotient L is not symmetric")

    # Deterministic lexicographic shortest-path routing of every directed ideal
    # quotient edge.  Uniform stationary factors cancel in the congestion ratio.
    ideal_targets: list[set[int]] = [set() for _ in range(qstates)]
    for source, target in urate:
        if source != target and urate[(source, target)] > 0:
            ideal_targets[source].add(target)
    path_histogram = collections.Counter()
    path_load: dict[tuple[int, int], Fraction] = collections.defaultdict(Fraction)
    disconnected_targets = []
    recovery_record_count = 0
    for source in range(qstates):
        needed = ideal_targets[source]
        if not needed:
            continue
        parent = {source: -1}
        queue = collections.deque([source])
        remaining = set(needed)
        while queue and remaining:
            current = queue.popleft()
            for target in sorted(ladjacency[current]):
                if target in parent:
                    continue
                parent[target] = current
                queue.append(target)
                remaining.discard(target)
        if remaining:
            disconnected_targets.append((source, min(remaining)))
            continue
        for target in sorted(needed):
            reverse_path = [target]
            while reverse_path[-1] != source:
                reverse_path.append(parent[reverse_path[-1]])
            path = list(reversed(reverse_path))
            length = len(path) - 1
            path_histogram[length] += 1
            recovery_record_count += micro_pair_count[(source, target)] * length
            demand = urate[(source, target)] * length
            for a, b in zip(path, path[1:]):
                path_load[(a, b)] += demand
    if disconnected_targets:
        raise AssertionError(f"quotient L disconnected on ideal targets: {disconnected_targets[:3]}")

    max_congestion = Fraction(0)
    max_congestion_edge = None
    for edge, load in path_load.items():
        capacity = lrate[edge]
        if capacity <= 0:
            raise AssertionError("routed through zero-capacity L edge")
        ratio = load / capacity
        if ratio > max_congestion:
            max_congestion = ratio
            max_congestion_edge = {
                "edge": edge,
                "load": str(load),
                "capacity": str(capacity),
                "ratio": str(ratio),
                "ratio_float": float(ratio),
            }

    # Audit the proposed bounded recovery code for these lexicographic paths.
    # A physical directed quotient-L edge is supplemented with:
    #   removed/added Stanley Cayley edges, source U-phase, path time, and
    #   min/max labels of the root-away component cut off by the removed edge.
    # The latter is the precise finite interpretation of "local Stanley
    # subtree interval endpoints" used in this audit.
    word_index = {word: index for index, word in enumerate(words)}
    tree_edge_index = {edge: index for index, edge in enumerate(edges)}
    max_path_length = max(path_histogram, default=0)
    recovery_keys = np.empty(recovery_record_count, dtype=np.uint64)
    recovery_qcommodities = np.empty(recovery_record_count, dtype=np.uint64)
    recovery_microcommodities = np.empty(recovery_record_count, dtype=np.uint64)
    subtree_interval_cache: dict[tuple[tuple[Edge, ...], Edge], tuple[int, int]] = {}

    def subtree_interval(tree: tuple[Edge, ...], removed: Edge) -> tuple[int, int]:
        cache_key = (tree, removed)
        if cache_key in subtree_interval_cache:
            return subtree_interval_cache[cache_key]
        adjacency = [set() for _ in range(n)]
        for a, b in tree:
            adjacency[a].add(b)
            adjacency[b].add(a)
        component = {removed[0]}
        stack = [removed[0]]
        while stack:
            a = stack.pop()
            for b in adjacency[a]:
                if tuple(sorted((a, b))) == removed or b in component:
                    continue
                component.add(b)
                stack.append(b)
        if 0 in component:
            component = set(range(n)) - component
        answer = (min(component), max(component))
        subtree_interval_cache[cache_key] = answer
        return answer

    record = 0
    for source in range(qstates):
        needed = ideal_targets[source]
        if not needed:
            continue
        parent = {source: -1}
        queue = collections.deque([source])
        remaining = set(needed)
        while queue and remaining:
            current = queue.popleft()
            for target in sorted(ladjacency[current]):
                if target in parent:
                    continue
                parent[target] = current
                queue.append(target)
                remaining.discard(target)
        if remaining:
            raise AssertionError("recovery audit found a disconnected ideal target")
        paths: dict[int, list[int]] = {}
        for target in needed:
            reverse_path = [target]
            while reverse_path[-1] != source:
                reverse_path.append(parent[reverse_path[-1]])
            paths[target] = list(reversed(reverse_path))

        for word in orbit_members[source]:
            source_word_index = word_index[word]
            phase = orbit_phase[word]
            tree = trees[word]
            for target_tree, _, _, removed, added in exchange_cache[tree]:
                target_word = tree_to_word[target_tree]
                target = orbit_id[target_word]
                if target == source:
                    continue
                path = paths[target]
                removed_index = tree_edge_index[removed]
                added_index = tree_edge_index[added]
                interval_left, interval_right = subtree_interval(tree, removed)
                qcommodity = source * qstates + target
                microcommodity = source_word_index * len(words) + word_index[target_word]
                for path_time, (used_source, used_target) in enumerate(zip(path, path[1:])):
                    key = used_source
                    for value, radix in (
                        (used_target, qstates),
                        (removed_index, len(edges)),
                        (added_index, len(edges)),
                        (phase, n),
                        (path_time, max_path_length + 1),
                        (interval_left, n),
                        (interval_right, n),
                    ):
                        key = key * radix + value
                    recovery_keys[record] = key
                    recovery_qcommodities[record] = qcommodity
                    recovery_microcommodities[record] = microcommodity
                    record += 1
    if record != recovery_record_count:
        raise AssertionError(
            f"recovery record count mismatch: filled {record}, expected {recovery_record_count}"
        )

    order = np.argsort(recovery_keys, kind="stable")
    sorted_keys = recovery_keys[order]
    boundaries = np.concatenate(
        (
            np.array([0], dtype=np.int64),
            np.flatnonzero(sorted_keys[1:] != sorted_keys[:-1]) + 1,
            np.array([recovery_record_count], dtype=np.int64),
        )
    )
    duplicate_key_groups = 0
    quotient_collision_groups = 0
    micro_collision_groups = 0
    maximum_quotient_sources_per_key = 1 if recovery_record_count else 0
    maximum_micro_sources_per_key = 1 if recovery_record_count else 0
    first_quotient_collision = None
    first_micro_collision = None

    def decode_key(key: int) -> dict[str, object]:
        interval_right = key % n
        key //= n
        interval_left = key % n
        key //= n
        path_time = key % (max_path_length + 1)
        key //= max_path_length + 1
        phase = key % n
        key //= n
        added_index = key % len(edges)
        key //= len(edges)
        removed_index = key % len(edges)
        key //= len(edges)
        used_target = key % qstates
        used_source = key // qstates
        return {
            "used_directed_quotient_L_edge": (used_source, used_target),
            "removed_Stanley_tree_edge": edges[removed_index],
            "added_Stanley_tree_edge": edges[added_index],
            "source_U_phase": phase,
            "path_time_zero_based": path_time,
            "root_away_subtree_minmax": (interval_left, interval_right),
        }

    def quotient_witness(value: int) -> dict[str, object]:
        return {
            "source_orbit": value // qstates,
            "target_orbit": value % qstates,
        }

    def micro_witness(value: int) -> dict[str, object]:
        source_word_index, target_word_index = divmod(value, len(words))
        return {
            "source_word": words[source_word_index],
            "target_word": words[target_word_index],
            "source_orbit": orbit_id[words[source_word_index]],
            "target_orbit": orbit_id[words[target_word_index]],
        }

    for start, stop in zip(boundaries, boundaries[1:]):
        if stop - start <= 1:
            continue
        duplicate_key_groups += 1
        positions = order[start:stop]
        quotient_values = np.unique(recovery_qcommodities[positions])
        micro_values = np.unique(recovery_microcommodities[positions])
        maximum_quotient_sources_per_key = max(
            maximum_quotient_sources_per_key, len(quotient_values)
        )
        maximum_micro_sources_per_key = max(
            maximum_micro_sources_per_key, len(micro_values)
        )
        if len(quotient_values) > 1:
            quotient_collision_groups += 1
            if first_quotient_collision is None:
                first_quotient_collision = {
                    "metadata": decode_key(int(sorted_keys[start])),
                    "distinct_quotient_sources": [
                        quotient_witness(int(value)) for value in quotient_values[:3]
                    ],
                    "distinct_quotient_source_count": len(quotient_values),
                }
        if len(micro_values) > 1:
            micro_collision_groups += 1
            if first_micro_collision is None:
                first_micro_collision = {
                    "metadata": decode_key(int(sorted_keys[start])),
                    "distinct_micro_sources": [
                        micro_witness(int(value)) for value in micro_values[:3]
                    ],
                    "distinct_micro_source_count": len(micro_values),
                }

    recovery_audit = {
        "metadata_definition": (
            "used directed quotient-L edge; removed and added Stanley-tree edges; "
            "source U-orbit phase; zero-based path time; min/max labels of the "
            "root-away component after deleting the Stanley-tree edge"
        ),
        "path_use_records": recovery_record_count,
        "distinct_metadata_keys": len(boundaries) - 1,
        "duplicate_metadata_key_groups": duplicate_key_groups,
        "quotient_source_collision_groups": quotient_collision_groups,
        "micro_source_collision_groups": micro_collision_groups,
        "maximum_distinct_quotient_sources_per_key": maximum_quotient_sources_per_key,
        "maximum_distinct_micro_sources_per_key": maximum_micro_sources_per_key,
        "quotient_source_recovery_is_unique": quotient_collision_groups == 0,
        "micro_source_recovery_is_unique": micro_collision_groups == 0,
        "first_quotient_collision": first_quotient_collision,
        "first_micro_collision": first_micro_collision,
    }

    return {
        "n": n,
        "states": len(words),
        "quotient_states": qstates,
        "local_fiber_sizes": sorted(fiber_sizes),
        "quotient_L_off_diagonal_directed_edges": sum(
            1 for (a, b), rate in lrate.items() if a != b and rate > 0
        ),
        "quotient_UST_off_diagonal_directed_edges": sum(
            1 for (a, b), rate in urate.items() if a != b and rate > 0
        ),
        "ideal_micro_directed_edges": ideal_micro_edges,
        "ideal_micro_edges_reachable_by_one_contiguous_Hurwitz_bubble_mod_U": bubble_covered_micro_edges,
        "one_bubble_coverage_fraction": bubble_covered_micro_edges / ideal_micro_edges,
        "first_one_bubble_failure": first_bubble_failure,
        "shortest_quotient_L_path_length_histogram_for_UST_edges": {
            str(key): path_histogram[key] for key in sorted(path_histogram)
        },
        "maximum_shortest_path_length": max(path_histogram, default=0),
        "lexicographic_shortest_path_comparison_congestion": str(max_congestion),
        "lexicographic_shortest_path_comparison_congestion_float": float(max_congestion),
        "maximum_congestion_edge": max_congestion_edge,
        "lexicographic_recovery_metadata_audit": recovery_audit,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    parameters = sorted(set(args.n))
    payload = {
        "claim_tested": (
            "Every UST basis exchange becomes one contiguous Hurwitz bubble modulo "
            "simultaneous endpoint conjugation; failing that, deterministic quotient "
            "shortest paths have small finite stationary-flow congestion."
        ),
        "scope_warning": (
            "One-bubble failure is an exact structural refutation.  Finite path lengths "
            "and congestion do not prove an asymptotic comparison."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "parameters": parameters,
        "results": [analyze(n) for n in parameters],
        "python": platform.python_version(),
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
