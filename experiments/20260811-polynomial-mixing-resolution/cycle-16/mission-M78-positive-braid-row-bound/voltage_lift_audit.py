#!/usr/bin/env python3
"""Exact bounded-depth audit for a Z_L^2 lift of the K4,4 M78 word."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path


sys.dont_write_bytecode = True

BASE_WORD = (
    (3, 5), (3, 4), (1, 5), (2, 5),
    (1, 6), (0, 4), (3, 7), (2, 7),
    (0, 5), (3, 6), (1, 4), (1, 7),
    (0, 6), (2, 4), (2, 6), (0, 7),
)

# Signed voltages use the displayed orientation from the smaller to the larger
# endpoint (the base graph is bipartite, so this is left-to-right).
VOLTAGE_X = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VOLTAGE_Y = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def lifted_word(L):
    def label(vertex, x, y):
        return (vertex * L + x) * L + y

    word = []
    metadata = []
    for base_index, ((a, b), dx, dy) in enumerate(
        zip(BASE_WORD, VOLTAGE_X, VOLTAGE_Y)
    ):
        for x in range(L):
            for y in range(L):
                edge = tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                )))
                word.append(edge)
                metadata.append((base_index, x, y))
    return tuple(word), tuple(metadata)


def product_is_identity(edge_word, n):
    permutation = list(range(n))
    for a, b in edge_word:
        permutation[a], permutation[b] = permutation[b], permutation[a]
    return permutation == list(range(n))


def connected_edges(edge_word, n):
    adjacency = [set() for _ in range(n)]
    for a, b in edge_word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in adjacency[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return len(seen) == n


def all_four_cycles(edge_word, n):
    adjacency = [set() for _ in range(n)]
    edge_index = {}
    for index, edge in enumerate(edge_word):
        a, b = edge
        adjacency[a].add(b)
        adjacency[b].add(a)
        edge_index[edge] = index
    cycles = set()
    for a in range(n):
        for c in range(a + 1, n):
            common = sorted(adjacency[a] & adjacency[c])
            for b, d in itertools.combinations(common, 2):
                cycles.add(tuple(sorted(
                    edge_index[tuple(sorted(edge))]
                    for edge in ((a, b), (b, c), (c, d), (d, a))
                )))
    return tuple(sorted(cycles))


def setup_elimination(edge_word, n):
    all_edges = tuple((a, b) for a in range(n) for b in range(a + 1, n))
    lookup = {edge: i for i, edge in enumerate(all_edges)}
    word = tuple(lookup[edge] for edge in edge_word)

    def conjugate(edge, pivot):
        p, q = all_edges[pivot]
        x, y = all_edges[edge]

        def act(z):
            return q if z == p else p if z == q else z

        return lookup[tuple(sorted((act(x), act(y))))]

    return all_edges, word, conjugate


def prefix(word, order, conjugate):
    values = tuple(word)
    labels = tuple(range(len(word)))
    outputs = []
    for wanted in order:
        position = labels.index(wanted)
        pivot = values[position]
        outputs.append(pivot)
        values = tuple(
            conjugate(edge, pivot) for edge in values[:position]
        ) + values[position + 1 :]
        labels = labels[:position] + labels[position + 1 :]
    return tuple(outputs), values


def connected_indices(values, all_edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge in values:
        a, b = all_edges[edge]
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[bb] = aa
    return len({find(x) for x in range(n)}) == 1


def audit(L):
    edge_word, metadata = lifted_word(L)
    n = 8 * L * L
    all_edges, word, conjugate = setup_elimination(edge_word, n)
    cycles = all_four_cycles(edge_word, n)
    collisions = 0
    safe = 0
    collision_example = None
    for cycle in cycles:
        for order in itertools.permutations(cycle):
            outputs, values = prefix(word, order, conjugate)
            if outputs[-1] != outputs[-2]:
                continue
            collisions += 1
            collision_example = collision_example or {
                "original_label_order": list(order),
                "current_outputs": [list(all_edges[x]) for x in outputs],
                "residual_connected": connected_indices(
                    outputs[:-2] + values, all_edges, n
                ),
            }
            if connected_indices(outputs[:-2] + values, all_edges, n):
                safe += 1
    return {
        "L": L,
        "component_vertex_count": n,
        "component_length": len(edge_word),
        "product_is_identity": product_is_identity(edge_word, n),
        "support_connected": connected_edges(edge_word, n),
        "support_simple": len(set(edge_word)) == len(edge_word),
        "support_bipartite": all(
            ((a // (L * L)) < 4) != ((b // (L * L)) < 4)
            for a, b in edge_word
        ),
        "support_degree_histogram": {
            str(degree): count
            for degree, count in sorted(Counter(Counter(
                endpoint
                for edge in edge_word
                for endpoint in edge
            ).values()).items())
        },
        "four_cycle_count": len(cycles),
        "four_cycle_collision_order_count": collisions,
        "four_cycle_safe_order_count": safe,
        "collision_example": collision_example,
        "first_word_metadata": [list(item) for item in metadata[:16]],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--L", nargs="+", type=int, default=[2, 3])
    args = parser.parse_args()
    started = time.perf_counter()
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": (
            "(pq)(x)=p(q(x)); left-to-right products; canonical positive "
            "elimination conjugates all residual factors to the left"
        ),
        "claim_tested": (
            "The explicit Z_L^2 voltage lifts are connected simple genus-one "
            "identity words with no safe canonical-elimination prefix through "
            "depth two."
        ),
        "scope_warning": (
            "This exact bounded-depth refutation is not an upper bound on the "
            "total full-prefix hit probability."
        ),
        "base_word": [list(edge) for edge in BASE_WORD],
        "voltage_x": list(VOLTAGE_X),
        "voltage_y": list(VOLTAGE_Y),
        "audits": [audit(L) for L in args.L],
    }
    payload["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "audits": payload["audits"],
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
