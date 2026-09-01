#!/usr/bin/env python3
"""Exact canonical-positive-elimination audits for M78.

The canonical positive lift used by M75 takes a requested original-label
order and repeatedly bubbles that label left.  Equivalently, selecting the
factor currently at residual position j outputs it and conjugates every
current factor strictly to its left by the selected transposition.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter
from functools import lru_cache
from pathlib import Path


sys.dont_write_bytecode = True


def setup(n: int):
    edges = tuple((a, b) for a in range(n) for b in range(a + 1, n))
    lookup = {edge: i for i, edge in enumerate(edges)}
    conjugates = []
    for pivot in edges:
        p, q = pivot
        row = []
        for x, y in edges:
            xx = q if x == p else p if x == q else x
            yy = q if y == p else p if y == q else y
            row.append(lookup[tuple(sorted((xx, yy)))])
        conjugates.append(tuple(row))
    edge_permutations = []
    for a, b in edges:
        permutation = list(range(n))
        permutation[a], permutation[b] = permutation[b], permutation[a]
        edge_permutations.append(tuple(permutation))
    return edges, lookup, tuple(conjugates), tuple(edge_permutations)


def product(word, edge_permutations, n: int):
    out = list(range(n))
    for edge in word:
        permutation = edge_permutations[edge]
        out = [out[permutation[x]] for x in range(n)]
    return tuple(out)


def connected(edge_values, edges, n: int):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge in edge_values:
        a, b = edges[edge]
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    return len({find(x) for x in range(n)}) == 1


def select(values, labels, wanted, conjugates):
    position = labels.index(wanted)
    pivot = values[position]
    remaining_values = tuple(
        conjugates[pivot][edge] for edge in values[:position]
    ) + values[position + 1 :]
    remaining_labels = labels[:position] + labels[position + 1 :]
    return pivot, remaining_values, remaining_labels, position


def prefix_state(word, order, conjugates):
    values = tuple(word)
    labels = tuple(range(len(word)))
    outputs = []
    positions = []
    for wanted in order:
        pivot, values, labels, position = select(
            values, labels, wanted, conjugates
        )
        outputs.append(pivot)
        positions.append(position)
    return tuple(outputs), values, labels, tuple(positions)


def safe_prefix(word, order, conjugates, edges, n: int):
    outputs, values, _labels, _positions = prefix_state(
        word, order, conjugates
    )
    return (
        len(outputs) >= 2
        and outputs[-1] == outputs[-2]
        and connected(outputs[:-2] + values, edges, n)
    )


def depth_counts(word, max_depth, conjugates, edges, n: int):
    counts = []
    examples = []
    for depth in range(max_depth + 1):
        count = 0
        for order in itertools.permutations(range(len(word)), depth + 2):
            if safe_prefix(word, order, conjugates, edges, n):
                count += 1
                if len(examples) < 8:
                    outputs, _values, _labels, _positions = prefix_state(
                        word, order, conjugates
                    )
                    examples.append(
                        {
                            "depth": depth,
                            "original_label_order": list(order),
                            "current_output_edges": [list(edges[x]) for x in outputs],
                        }
                    )
        counts.append(count)
    return counts, examples


def first_success_depth(word, max_depth, conjugates, edges, n: int):
    for depth in range(max_depth + 1):
        for order in itertools.permutations(range(len(word)), depth + 2):
            if safe_prefix(word, order, conjugates, edges, n):
                return depth
    return None


def exhaustive_small(n: int):
    edges, _lookup, conjugates, edge_permutations = setup(n)
    length = 2 * n
    identity = tuple(range(n))
    histogram = Counter()
    word_count = 0
    for word in itertools.product(range(len(edges)), repeat=length):
        if product(word, edge_permutations, n) != identity:
            continue
        if not connected(word, edges, n):
            continue
        word_count += 1
        depth = first_success_depth(word, 1, conjugates, edges, n)
        histogram[str(depth)] += 1
    return {
        "component_vertex_count": n,
        "component_length": length,
        "connected_genus_one_identity_word_count": word_count,
        "minimum_success_depth_histogram": dict(sorted(histogram.items())),
        "enumeration_complete": True,
    }


def exact_prefix_hit_count(word, conjugates, edges, n: int):
    """Count full label orders having any safe prefix by an exact recursion.

    `support_mask` records already output factors except `last`.  Multiplicity
    is irrelevant for the connectivity test.  Once a safe prefix occurs, all
    completions are successful because subsequent eliminations act only on
    the residual suffix and preserve its support components.
    """

    @lru_cache(maxsize=None)
    def recurse(values, support_mask, last):
        remaining_count = len(values)
        if remaining_count == 0:
            return 0
        answer = 0
        next_mask = support_mask if last < 0 else support_mask | (1 << last)
        anonymous_labels = tuple(range(remaining_count))
        for position, pivot in enumerate(values):
            remaining = tuple(
                conjugates[pivot][edge] for edge in values[:position]
            ) + values[position + 1 :]
            if last == pivot:
                residual_edges = [
                    edge for edge in range(len(edges)) if (support_mask >> edge) & 1
                ] + list(remaining)
                if connected(residual_edges, edges, n):
                    answer += math.factorial(remaining_count - 1)
                    continue
            # Labels are distinct even when their current factor values agree;
            # choosing each residual position is a separate branch.
            del anonymous_labels  # documents that positions, not values, branch
            answer += recurse(remaining, next_mask, pivot)
            anonymous_labels = tuple(range(remaining_count))
        return answer

    hits = recurse(tuple(word), 0, -1)
    return hits, recurse.cache_info()._asdict()


def face_cycles(edge_word, n: int):
    """Return the chronological rotation-system faces as original indices."""

    darts = tuple((i, side) for i in range(len(edge_word)) for side in range(2))
    dart_index = {dart: i for i, dart in enumerate(darts)}
    alpha = {}
    for i in range(len(edge_word)):
        alpha[dart_index[(i, 0)]] = dart_index[(i, 1)]
        alpha[dart_index[(i, 1)]] = dart_index[(i, 0)]
    sigma = {}
    for vertex in range(n):
        occurrences = [
            dart_index[(i, side)]
            for i, edge in enumerate(edge_word)
            for side, endpoint in enumerate(edge)
            if endpoint == vertex
        ]
        for j, dart in enumerate(occurrences):
            sigma[dart] = occurrences[(j + 1) % len(occurrences)]
    face_permutation = {dart: sigma[alpha[dart]] for dart in range(len(darts))}
    seen = set()
    faces = []
    for dart in range(len(darts)):
        if dart in seen:
            continue
        face = []
        current = dart
        while current not in seen:
            seen.add(current)
            face.append(darts[current][0])
            current = face_permutation[current]
        faces.append(tuple(face))
    return tuple(faces)


def candidate_audits():
    # Lexicographic edges on labels 0,...,4.
    all_distinct_n5_indices = (0, 1, 2, 4, 6, 8, 3, 7, 5, 9)
    edges5, _lookup5, conjugates5, permutations5 = setup(5)
    counts5, examples5 = depth_counts(
        all_distinct_n5_indices, 1, conjugates5, edges5, 5
    )
    hits5, cache5 = exact_prefix_hit_count(
        all_distinct_n5_indices, conjugates5, edges5, 5
    )

    edge_word8 = (
        (3, 5), (3, 4), (1, 5), (2, 5),
        (1, 6), (0, 4), (3, 7), (2, 7),
        (0, 5), (3, 6), (1, 4), (1, 7),
        (0, 6), (2, 4), (2, 6), (0, 7),
    )
    edges8, lookup8, conjugates8, permutations8 = setup(8)
    word8 = tuple(lookup8[edge] for edge in edge_word8)
    counts8, examples8 = depth_counts(word8, 2, conjugates8, edges8, 8)
    faces = face_cycles(edge_word8, 8)
    face_safe_orders = {}
    face_collision_orders = {}
    for face in faces:
        safe = []
        collisions = []
        for order in itertools.permutations(face):
            outputs, values, _labels, _positions = prefix_state(
                word8, order, conjugates8
            )
            if outputs[-1] == outputs[-2]:
                collisions.append(order)
                if connected(outputs[:-2] + values, edges8, 8):
                    safe.append(order)
        face_safe_orders[str(list(face))] = [list(order) for order in safe]
        face_collision_orders[str(list(face))] = [
            list(order) for order in collisions
        ]

    unsafe_face_order = (2, 4, 0, 9)
    safe_nonface_order = (1, 2, 0, 10)
    special = {}
    for name, order in (
        ("facial_collision_but_disconnected", unsafe_face_order),
        ("nonfacial_safe_cycle", safe_nonface_order),
    ):
        outputs, values, _labels, positions = prefix_state(
            word8, order, conjugates8
        )
        special[name] = {
            "original_label_order": list(order),
            "original_edges": [list(edge_word8[i]) for i in order],
            "current_output_edges": [list(edges8[x]) for x in outputs],
            "residual_positions_at_selection": list(positions),
            "last_two_equal": outputs[-1] == outputs[-2],
            "residual_connected_after_deletion": connected(
                outputs[:-2] + values, edges8, 8
            ),
        }

    return {
        "all_distinct_N5": {
            "component_vertex_count": 5,
            "component_length": 10,
            "word_edge_indices": list(all_distinct_n5_indices),
            "word_edges": [list(edges5[x]) for x in all_distinct_n5_indices],
            "product_is_identity": product(
                all_distinct_n5_indices, permutations5, 5
            ) == tuple(range(5)),
            "support_connected": connected(all_distinct_n5_indices, edges5, 5),
            "all_factors_distinct": len(set(all_distinct_n5_indices)) == 10,
            "successful_prefix_counts_by_depth": counts5,
            "successful_prefix_examples": examples5,
            "full_prefix_hit_count": hits5,
            "full_order_count": math.factorial(10),
            "full_prefix_hit_probability": [hits5, math.factorial(10)],
            "dynamic_program_cache": cache5,
        },
        "K44_N8": {
            "component_vertex_count": 8,
            "component_length": 16,
            "word_edges": [list(edge) for edge in edge_word8],
            "product_is_identity": product(word8, permutations8, 8)
            == tuple(range(8)),
            "support_connected": connected(word8, edges8, 8),
            "support_is_exactly_K44": set(edge_word8)
            == {(a, b) for a in range(4) for b in range(4, 8)},
            "all_factors_distinct": len(set(word8)) == 16,
            "successful_prefix_counts_by_depth": counts8,
            "successful_prefix_examples": examples8,
            "rotation_system_faces": [list(face) for face in faces],
            "face_lengths": [len(face) for face in faces],
            "facial_safe_order_count": sum(
                len(orders) for orders in face_safe_orders.values()
            ),
            "facial_collision_order_count": sum(
                len(orders) for orders in face_collision_orders.values()
            ),
            "facial_safe_orders": face_safe_orders,
            "facial_collision_orders": face_collision_orders,
            "special_prefixes": special,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    payload = {
        "argv": sys.argv,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": (
            "(pq)(x)=p(q(x)); tuple product left-to-right; "
            "R_i(a,b)=(b,bab); canonical positive lift bubbles each requested "
            "original label left"
        ),
        "depth_definition": (
            "Depth q means q preliminary selected/output factors followed by "
            "two equal current outputs; deleting those two leaves the prior "
            "q outputs plus current residual tuple connected."
        ),
        "claim_tested": (
            "Bounded-depth canonical positive elimination creates a connected "
            "two-deletion certificate in connected genus-one identity words."
        ),
        "scope_warning": (
            "Exact finite data can refute a proposed fixed-depth lemma but "
            "cannot prove an asymptotic row-probability lower bound."
        ),
    }
    try:
        payload["commit"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        payload["commit"] = "unavailable"
    payload["small_exhaustive"] = [exhaustive_small(3), exhaustive_small(4)]
    payload["candidates"] = candidate_audits()
    payload["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "small_exhaustive": payload["small_exhaustive"],
        "N5_depth_counts": payload["candidates"]["all_distinct_N5"]
            ["successful_prefix_counts_by_depth"],
        "K44_depth_counts": payload["candidates"]["K44_N8"]
            ["successful_prefix_counts_by_depth"],
        "K44_facial_safe": payload["candidates"]["K44_N8"]
            ["facial_safe_order_count"],
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
