#!/usr/bin/env python3
"""Exact positive-permutation-braid audit on frozen M68 hard witnesses.

The input is the frozen M68 direct-two-deletion JSON.  For each displayed
failure word, enumerate all 8! canonical positive permutation braids and test
for an adjacent equal square whose deletion preserves the support component.
This is an exact finite stress test of the stronger randomized cover; it does
not infer an asymptotic theorem from positive finite survival.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CORE_PATH = HERE / "positive_permutation_braid_audit.py"
DEFAULT_INPUT = (
    HERE.parent.parent
    / "cycle-15"
    / "mission-M68-intermediate-exterior-layer-action"
    / "exact-n5-two-deletion.json"
)


def load_core():
    spec = importlib.util.spec_from_file_location("m75_positive_core", CORE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(CORE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def support_components(word, edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    touched = set()
    for index in word:
        a, b = edges[index]
        touched.update((a, b))
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), set()).add(v)
    return tuple(sorted((tuple(sorted(group)) for group in groups.values())))


def connected_on(vertices, word, edges):
    if len(vertices) <= 1:
        return True
    vertices = set(vertices)
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index in word:
        a, b = edges[index]
        if a not in vertices or b not in vertices:
            continue
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    return len({find(v) for v in vertices}) == 1


def marked(word, edges, original_components):
    component_of = {
        vertex: component
        for component in original_components
        for vertex in component
    }
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continue
        a, _b = edges[word[i]]
        vertices = component_of[a]
        if len(vertices) <= 1:
            continue
        component_positions = [
            index
            for j, index in enumerate(word)
            if j not in (i, i + 1) and edges[index][0] in vertices
        ]
        if connected_on(vertices, component_positions, edges):
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    core = load_core()
    source = json.loads(args.input.read_text())
    n = source["N"]
    k = source["m"]
    edges = core.edge_list(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    edge_perms = tuple(core.perm(edge, n) for edge in edges)
    identity = tuple(range(n))
    orders = tuple(itertools.permutations(range(k)))
    results = []
    global_minimum = len(orders) + 1
    for item in source["failure_examples"]:
        word = tuple(item["word_edge_indices"])
        assert core.product(word, edge_perms, n) == identity
        components = support_components(word, edges, n)
        hits = 0
        histogram = Counter()
        for order in orders:
            endpoint, move_count = core.positive_lift(word, order, edges, lookup)
            assert core.product(endpoint, edge_perms, n) == identity
            is_marked = marked(endpoint, edges, components)
            hits += int(is_marked)
            histogram[move_count] += int(is_marked)
        global_minimum = min(global_minimum, hits)
        results.append({
            "word_edge_indices": list(word),
            "components": [list(component) for component in components],
            "marked_endpoint_count": hits,
            "marked_endpoint_probability": [hits, len(orders)],
            "marked_hits_by_braid_length": {
                str(length): count for length, count in sorted(histogram.items())
            },
        })
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab); canonical positive permutation braid",
        "claim_tested": "A uniform positive permutation braid has positive marked-endpoint probability on every displayed M68 direct-two-deletion failure.",
        "scope_warning": "This exhausts braids on the displayed finite witnesses only; positive survival is not asymptotic evidence.",
        "source_json": str(args.input),
        "N": n,
        "m": k,
        "witness_count": len(results),
        "permutation_count_per_witness": len(orders),
        "global_minimum_marked_endpoint_count": global_minimum,
        "global_minimum_marked_endpoint_probability": [global_minimum, len(orders)],
        "results": results,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "witness_count": len(results),
        "permutation_count": len(orders),
        "global_minimum": global_minimum,
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
