#!/usr/bin/env python3
"""Independent exact referee checks for M78's voltage-lift obstruction.

This file intentionally imports no M78 code.  It uses only the Python
standard library and the convention (pq)(x)=p(q(x)), with factors evaluated
left-to-right and R(a,b)=(b,bab).
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
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path


sys.dont_write_bytecode = True

BASE_WORD = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def transposition_permutation(edge, n):
    out = list(range(n))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(word, n):
    """Return the left-to-right product t_1 ... t_k."""
    out = tuple(range(n))
    for edge in word:
        tau = transposition_permutation(edge, n)
        out = tuple(out[tau[x]] for x in range(n))
    return out


def conjugate(edge, pivot):
    p, q = pivot

    def act(x):
        return q if x == p else p if x == q else x

    return tuple(sorted((act(edge[0]), act(edge[1]))))


def connected(word, n):
    parent = list(range(n))

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in word:
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    return len({find(x) for x in range(n)}) == 1


def components(word, n):
    adjacency = [set() for _ in range(n)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(range(n))
    result = []
    while unseen:
        root = min(unseen)
        seen = {root}
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
        unseen -= seen
        result.append(tuple(sorted(seen)))
    return tuple(sorted(result))


def eliminate(word, requested_labels):
    values = tuple(word)
    labels = tuple(range(len(word)))
    outputs = []
    selected_positions = []
    for wanted in requested_labels:
        position = labels.index(wanted)
        pivot = values[position]
        outputs.append(pivot)
        selected_positions.append(position)
        values = (
            tuple(conjugate(edge, pivot) for edge in values[:position])
            + values[position + 1 :]
        )
        labels = labels[:position] + labels[position + 1 :]
    return tuple(outputs), values, labels, tuple(selected_positions)


def safe_prefix(word, requested_labels, n):
    outputs, residual, _labels, _positions = eliminate(word, requested_labels)
    return (
        len(outputs) >= 2
        and outputs[-1] == outputs[-2]
        and connected(outputs[:-2] + residual, n)
    )


def depth_counts(word, maximum_depth, n):
    counts = []
    for depth in range(maximum_depth + 1):
        counts.append(sum(
            safe_prefix(word, order, n)
            for order in itertools.permutations(range(len(word)), depth + 2)
        ))
    return counts


def first_safe_depth(word, maximum_depth, n):
    for depth in range(maximum_depth + 1):
        if any(
            safe_prefix(word, order, n)
            for order in itertools.permutations(range(len(word)), depth + 2)
        ):
            return depth
    return None


def exhaustive_small(n):
    edges = tuple(itertools.combinations(range(n), 2))
    length = 2 * n
    identity = tuple(range(n))
    histogram = Counter()
    count = 0
    for indices in itertools.product(range(len(edges)), repeat=length):
        word = tuple(edges[i] for i in indices)
        if evaluate(word, n) != identity or not connected(word, n):
            continue
        count += 1
        histogram[str(first_safe_depth(word, 1, n))] += 1
    return {
        "n": n,
        "length": length,
        "connected_identity_word_count": count,
        "first_safe_depth_histogram": dict(sorted(histogram.items())),
    }


def exact_prefix_hit_count(word, n):
    """Count full elimination orders with at least one safe prefix."""

    @lru_cache(maxsize=None)
    def recurse(values, retained_support, last):
        if not values:
            return 0
        answer = 0
        support_before_last = set(retained_support)
        next_support = (
            retained_support
            if last is None
            else tuple(sorted(support_before_last | {last}))
        )
        for position, pivot in enumerate(values):
            residual = (
                tuple(conjugate(edge, pivot) for edge in values[:position])
                + values[position + 1 :]
            )
            if last == pivot and connected(tuple(retained_support) + residual, n):
                answer += math.factorial(len(values) - 1)
            else:
                answer += recurse(residual, next_support, pivot)
        return answer

    hits = recurse(tuple(word), tuple(), None)
    return hits, recurse.cache_info()._asdict()


def rotation_faces(word, n):
    """Faces of the chronological rotation system, as factor indices."""
    darts = tuple((i, side) for i in range(len(word)) for side in range(2))
    dart_id = {dart: i for i, dart in enumerate(darts)}
    alpha = {}
    for i in range(len(word)):
        alpha[dart_id[(i, 0)]] = dart_id[(i, 1)]
        alpha[dart_id[(i, 1)]] = dart_id[(i, 0)]
    sigma = {}
    for vertex in range(n):
        incident = [
            dart_id[(i, side)]
            for i, edge in enumerate(word)
            for side, endpoint in enumerate(edge)
            if endpoint == vertex
        ]
        for j, dart in enumerate(incident):
            sigma[dart] = incident[(j + 1) % len(incident)]
    face_map = {dart: sigma[alpha[dart]] for dart in range(len(darts))}
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
            current = face_map[current]
        faces.append(tuple(face))
    return tuple(faces)


def finite_candidates():
    n5 = (
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 4),
        (2, 4), (0, 4), (2, 3), (1, 3), (3, 4),
    )
    n5_hits, n5_cache = exact_prefix_hit_count(n5, 5)

    k44_depths = depth_counts(BASE_WORD, 2, 8)
    faces = rotation_faces(BASE_WORD, 8)
    face_collisions = 0
    face_safe = 0
    isolated_histogram = Counter()
    for face in faces:
        for order in itertools.permutations(face):
            outputs, residual, _labels, _positions = eliminate(BASE_WORD, order)
            if outputs[-1] != outputs[-2]:
                continue
            face_collisions += 1
            remaining = outputs[:-2] + residual
            is_safe = connected(remaining, 8)
            face_safe += is_safe
            isolated = tuple(
                sorted(set(range(8)) - {x for edge in remaining for x in edge})
            )
            isolated_histogram[str(isolated)] += 1
    return {
        "n5": {
            "identity": evaluate(n5, 5) == tuple(range(5)),
            "connected": connected(n5, 5),
            "distinct": len(set(n5)) == len(n5),
            "depth_counts": depth_counts(n5, 1, 5),
            "full_hit_count": n5_hits,
            "full_order_count": math.factorial(10),
            "reduced_probability": [227, 525],
            "cache": n5_cache,
        },
        "k44": {
            "identity": evaluate(BASE_WORD, 8) == tuple(range(8)),
            "connected": connected(BASE_WORD, 8),
            "distinct": len(set(BASE_WORD)) == 16,
            "exact_support": set(BASE_WORD)
            == {(a, b) for a in range(4) for b in range(4, 8)},
            "depth_counts": k44_depths,
            "faces": [list(face) for face in faces],
            "face_lengths": [len(face) for face in faces],
            "facial_collision_orders": face_collisions,
            "facial_safe_orders": face_safe,
            "facial_isolated_histogram": dict(sorted(isolated_histogram.items())),
        },
    }


def base_token_trajectories():
    rows = []
    for token in range(8):
        location = token
        signed_indices = []
        dx = dy = 0
        for index, (a, b) in enumerate(BASE_WORD):
            if location == a:
                location = b
                sign = 1
            elif location == b:
                location = a
                sign = -1
            else:
                continue
            signed_indices.append(sign * (index + 1))
            dx += sign * VX[index]
            dy += sign * VY[index]
        rows.append({
            "token": token,
            "final_base_vertex": location,
            "signed_indices_one_based": signed_indices,
            "signed_voltage_sum": [dx, dy],
        })
    return rows


def base_four_cycle_table():
    index = {edge: i for i, edge in enumerate(BASE_WORD)}
    rows = []
    for a, c in itertools.combinations(range(4), 2):
        for b, d in itertools.combinations(range(4, 8), 2):
            indices = (
                index[(a, b)], index[(c, b)],
                index[(c, d)], index[(a, d)],
            )
            voltage = (
                VX[indices[0]] - VX[indices[1]]
                + VX[indices[2]] - VX[indices[3]],
                VY[indices[0]] - VY[indices[1]]
                + VY[indices[2]] - VY[indices[3]],
            )
            rows.append({
                "vertices": [a, b, c, d],
                "indices": list(indices),
                "index_set": sorted(indices),
                "integer_voltage": list(voltage),
            })
    distribution = Counter(tuple(row["integer_voltage"]) for row in rows)
    zero_sets = sorted(
        tuple(row["index_set"])
        for row in rows
        if row["integer_voltage"] == [0, 0]
    )
    facial_sets = sorted(tuple(sorted(face)) for face in rotation_faces(BASE_WORD, 8))
    return {
        "rows": rows,
        "voltage_distribution": {
            str(vector): count for vector, count in sorted(distribution.items())
        },
        "zero_cycle_index_sets": [list(row) for row in zero_sets],
        "facial_index_sets": [list(row) for row in facial_sets],
        "zero_cycles_equal_faces": zero_sets == facial_sets,
        "all_nonzero_vectors_nonzero_mod_every_L_ge_2": all(
            vector == (0, 0)
            or not (vector[0] % modulus == 0 and vector[1] % modulus == 0)
            for vector in distribution
            for modulus in range(2, 33)
        ) and all(
            vector == (0, 0) or max(abs(vector[0]), abs(vector[1])) == 1
            for vector in distribution
        ),
    }


def lifted_word(L):
    def label(vertex, x, y):
        return (vertex * L + x) * L + y

    word = []
    metadata = []
    for base_index, ((a, b), dx, dy) in enumerate(zip(BASE_WORD, VX, VY)):
        for x in range(L):
            for y in range(L):
                word.append(tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                ))))
                metadata.append((base_index, x, y))
    return tuple(word), tuple(metadata)


def all_four_cycles(word, n):
    adjacency = [set() for _ in range(n)]
    edge_index = {}
    for i, (a, b) in enumerate(word):
        adjacency[a].add(b)
        adjacency[b].add(a)
        edge_index[(a, b)] = i
    result = set()
    for a in range(n):
        for c in range(a + 1, n):
            for b, d in itertools.combinations(sorted(adjacency[a] & adjacency[c]), 2):
                result.add(tuple(sorted(
                    edge_index[tuple(sorted(edge))]
                    for edge in ((a, b), (b, c), (c, d), (d, a))
                )))
    return tuple(sorted(result))


def lifted_audit(L, zero_base_sets):
    word, metadata = lifted_word(L)
    n = 8 * L * L
    cycles = all_four_cycles(word, n)
    collision_count = 0
    safe_count = 0
    isolated_size_histogram = Counter()
    projected_sets = Counter()
    for cycle in cycles:
        projected = tuple(sorted(metadata[i][0] for i in cycle))
        projected_sets[projected] += 1
        for order in itertools.permutations(cycle):
            outputs, residual, _labels, _positions = eliminate(word, order)
            if outputs[-1] != outputs[-2]:
                continue
            collision_count += 1
            remaining = outputs[:-2] + residual
            safe_count += connected(remaining, n)
            used = {x for edge in remaining for x in edge}
            isolated_size_histogram[len(set(range(n)) - used)] += 1
    degrees = Counter(x for edge in word for x in edge)
    return {
        "L": L,
        "n": n,
        "length": len(word),
        "identity": evaluate(word, n) == tuple(range(n)),
        "connected": connected(word, n),
        "simple": len(set(word)) == len(word),
        "bipartite": all(
            ((a // (L * L)) < 4) != ((b // (L * L)) < 4)
            for a, b in word
        ),
        "degree_histogram": dict(sorted(Counter(degrees.values()).items())),
        "four_cycle_count": len(cycles),
        "all_four_cycles_project_to_zero_base_face": set(projected_sets)
        == set(zero_base_sets),
        "lifts_per_zero_base_face": dict(sorted(Counter(projected_sets.values()).items())),
        "collision_orders": collision_count,
        "safe_orders": safe_count,
        "isolated_vertex_count_histogram": dict(sorted(isolated_size_histogram.items())),
    }


def abstract_face_collision_table():
    """Exact four-case table for chronological AD,AB,CB,CD."""
    edges = ((0, 3), (0, 1), (1, 2), (2, 3))
    names = "ABCD"
    collision_rows = []
    for order in itertools.permutations(range(4)):
        outputs, _residual, _labels, _positions = eliminate(edges, order)
        if outputs[-1] == outputs[-2]:
            collision_rows.append({
                "order": list(order),
                "outputs": [names[a] + names[b] for a, b in outputs],
            })

    def permutation_for_edge(edge):
        result = list(range(4))
        a, b = edge
        result[a], result[b] = result[b], result[a]
        return tuple(result)

    def compose(p, q):
        return tuple(p[q[x]] for x in range(4))

    interval_maps = []
    for row in collision_rows:
        values = tuple(edges)
        labels = tuple(range(4))
        pivots = []
        for wanted in row["order"]:
            position = labels.index(wanted)
            pivot = values[position]
            pivots.append((wanted, pivot))
            values = (
                tuple(conjugate(edge, pivot) for edge in values[:position])
                + values[position + 1 :]
            )
            labels = labels[:position] + labels[position + 1 :]
        maps = []
        for region in range(5):
            current = tuple(range(4))
            for original_index, pivot in pivots:
                if original_index >= region:
                    current = compose(permutation_for_edge(pivot), current)
            maps.append("".join(names[current[x]] for x in range(4)))
        interval_maps.append(maps)
    return {
        "chronological_edges": [names[a] + names[b] for a, b in edges],
        "collision_rows": collision_rows,
        "endpoint_maps_on_intervals_I0_through_I4": interval_maps,
        "all_four_rows_have_same_interval_maps": len({tuple(x) for x in interval_maps}) == 1,
    }


def cycle_collision_calibration():
    rows = []
    for r in range(3, 10):
        word = tuple((i, i + 1) for i in range(r - 1)) + ((0, r - 1),)
        count = 0
        for order in itertools.permutations(range(r)):
            outputs, _residual, _labels, _positions = eliminate(word, order)
            count += outputs[-1] == outputs[-2]
        rows.append({
            "cycle_length": r,
            "collision_orders": count,
            "formula_2_times_r_minus_2_factorial": 2 * math.factorial(r - 2),
            "conditional_probability": [count, math.factorial(r)],
        })
    return rows


def artifact_hashes(paths):
    return {
        str(path): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--m78-dir", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"

    m78_files = sorted(path for path in args.m78_dir.iterdir() if path.is_file())
    base_cycles = base_four_cycle_table()
    zero_sets = [tuple(row) for row in base_cycles["zero_cycle_index_sets"]]
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": (
            "(pq)(x)=p(q(x)); tuple factors left-to-right; "
            "R(a,b)=(b,bab); elimination conjugates residual factors to the left"
        ),
        "scope": (
            "Fresh audit of M78's canonical positive-braid voltage family; "
            "not a stationary-flow or spectral-gap claim for the heat-bath chain."
        ),
        "m78_artifact_sha256": artifact_hashes(m78_files),
        "small_exhaustive": [exhaustive_small(3), exhaustive_small(4)],
        "finite_candidates": finite_candidates(),
        "base_token_trajectories": base_token_trajectories(),
        "base_four_cycles": base_cycles,
        "abstract_face_collision": abstract_face_collision_table(),
        "lifted_checks": [lifted_audit(L, zero_sets) for L in (2, 3, 4)],
        "literal_cycle_collision_calibration": cycle_collision_calibration(),
    }
    payload["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "small_exhaustive": payload["small_exhaustive"],
        "n5_depths": payload["finite_candidates"]["n5"]["depth_counts"],
        "k44_depths": payload["finite_candidates"]["k44"]["depth_counts"],
        "zero_base_cycles": len(base_cycles["zero_cycle_index_sets"]),
        "lifted_checks": payload["lifted_checks"],
        "cycle_calibration": payload["literal_cycle_collision_calibration"],
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
