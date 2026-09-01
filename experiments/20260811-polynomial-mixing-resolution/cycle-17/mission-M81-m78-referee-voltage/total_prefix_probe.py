#!/usr/bin/env python3
"""Fixed-seed diagnostic for arbitrary canonical-elimination prefixes of W_L.

This is empirical.  It records all adjacent-output collisions, not only safe
ones, and audits the cycle rank and torus homology of the originally selected
edge set at each collision.
"""

from __future__ import annotations

import argparse
import json
import platform
import random
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
VX = (-1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
VY = (-1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def lifted_word(L):
    def label(vertex, x, y):
        return (vertex * L + x) * L + y

    word = []
    metadata = []
    for i, ((a, b), dx, dy) in enumerate(zip(BASE_WORD, VX, VY)):
        for x in range(L):
            for y in range(L):
                word.append(tuple(sorted((
                    label(a, x, y),
                    label(b, (x + dx) % L, (y + dy) % L),
                ))))
                metadata.append((i, x, y))
    return tuple(word), tuple(metadata)


def conjugate(edge, pivot):
    p, q = pivot

    def act(x):
        return q if x == p else p if x == q else x

    return tuple(sorted((act(edge[0]), act(edge[1]))))


def component_sizes(word, n):
    adjacency = [set() for _ in range(n)]
    for a, b in word:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = set()
    sizes = []
    for root in range(n):
        if root in seen:
            continue
        component = {root}
        seen.add(root)
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    component.add(y)
                    queue.append(y)
        sizes.append(len(component))
    return tuple(sorted(sizes, reverse=True))


def selected_topology(labels, word, metadata, L):
    """Cycle rank and nonzero Z^2 homology witnesses of selected lift edges."""
    adjacency = {}
    vertices = set()
    for label in labels:
        u, v = word[label]
        base_index, _x, _y = metadata[label]
        a, _b = BASE_WORD[base_index]
        if u // (L * L) == a:
            delta = (VX[base_index], VY[base_index])
        else:
            delta = (-VX[base_index], -VY[base_index])
        adjacency.setdefault(u, []).append((v, delta))
        adjacency.setdefault(v, []).append((u, (-delta[0], -delta[1])))
        vertices.update((u, v))

    potentials = {}
    homology = set()
    component_count = 0
    for root in sorted(vertices):
        if root in potentials:
            continue
        component_count += 1
        potentials[root] = (0, 0)
        queue = deque([root])
        while queue:
            u = queue.popleft()
            px, py = potentials[u]
            for v, (dx, dy) in adjacency[u]:
                expected = (px + dx, py + dy)
                if v not in potentials:
                    potentials[v] = expected
                    queue.append(v)
                else:
                    discrepancy = (
                        expected[0] - potentials[v][0],
                        expected[1] - potentials[v][1],
                    )
                    if discrepancy != (0, 0):
                        assert discrepancy[0] % L == 0
                        assert discrepancy[1] % L == 0
                        vector = (discrepancy[0] // L, discrepancy[1] // L)
                        if vector < (0, 0):
                            vector = (-vector[0], -vector[1])
                        homology.add(vector)
    cycle_rank = len(labels) - len(vertices) + component_count
    return cycle_rank, tuple(sorted(homology))


def trial(word, metadata, L, rng):
    n = 8 * L * L
    order = list(range(len(word)))
    rng.shuffle(order)
    values = list(word)
    labels = list(range(len(word)))
    outputs = []
    selected = []
    collisions = []
    for step, wanted in enumerate(order, start=1):
        position = labels.index(wanted)
        pivot = values[position]
        outputs.append(pivot)
        selected.append(wanted)
        values = [conjugate(edge, pivot) for edge in values[:position]] + values[position + 1 :]
        labels = labels[:position] + labels[position + 1 :]
        if len(outputs) < 2 or outputs[-1] != outputs[-2]:
            continue
        remaining = tuple(outputs[:-2] + values)
        sizes = component_sizes(remaining, n)
        cycle_rank, homology = selected_topology(selected, word, metadata, L)
        collisions.append({
            "prefix_length": step,
            "depth": step - 2,
            "safe": len(sizes) == 1,
            "remaining_component_sizes": sizes,
            "selected_cycle_rank": cycle_rank,
            "selected_nonzero_homology": homology,
        })
    return collisions


def run_case(L, trials, seed):
    rng = random.Random(seed)
    word, metadata = lifted_word(L)
    collision_orders = 0
    safe_orders = 0
    collision_prefixes = 0
    safe_prefixes = 0
    first_collision_depth = Counter()
    first_safe_depth = Counter()
    component_shape = Counter()
    topology = Counter()
    examples = []
    started = time.perf_counter()
    for trial_index in range(trials):
        collisions = trial(word, metadata, L, rng)
        if collisions:
            collision_orders += 1
            collision_prefixes += len(collisions)
            first_collision_depth[collisions[0]["depth"]] += 1
        safe = [item for item in collisions if item["safe"]]
        if safe:
            safe_orders += 1
            safe_prefixes += len(safe)
            first_safe_depth[safe[0]["depth"]] += 1
        for item in collisions:
            component_shape[str(item["remaining_component_sizes"])] += 1
            topology[str((
                item["selected_cycle_rank"],
                bool(item["selected_nonzero_homology"]),
            ))] += 1
        if collisions and len(examples) < 8:
            examples.append({"trial": trial_index, "collisions": collisions})
    return {
        "L": L,
        "n": 8 * L * L,
        "length": len(word),
        "trials": trials,
        "seed": seed,
        "orders_with_collision": collision_orders,
        "orders_with_safe_prefix": safe_orders,
        "collision_prefixes": collision_prefixes,
        "safe_prefixes": safe_prefixes,
        "first_collision_depth_histogram": dict(sorted(first_collision_depth.items())),
        "first_safe_depth_histogram": dict(sorted(first_safe_depth.items())),
        "remaining_component_shape_histogram": dict(sorted(component_shape.items())),
        "selected_topology_histogram": dict(sorted(topology.items())),
        "examples": examples,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seed", type=int, default=810081)
    parser.add_argument("--case", nargs=2, action="append", metavar=("L", "TRIALS"))
    args = parser.parse_args()
    cases = [(int(L), int(trials)) for L, trials in (args.case or [(1, 20000), (2, 20000), (3, 4000)])]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "nonstandard_dependencies": {},
        "method": (
            "Uniform random full original-label orders; exact canonical elimination; "
            "record every adjacent equal-output prefix and exact residual connectivity."
        ),
        "scope_warning": (
            "Fixed-seed Monte Carlo is empirical. Zero observed safe prefixes is neither "
            "a zero-row proof nor an asymptotic probability upper bound."
        ),
        "results": [
            run_case(L, trials, args.seed + 1000003 * index)
            for index, (L, trials) in enumerate(cases)
        ],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], sort_keys=True))


if __name__ == "__main__":
    main()
