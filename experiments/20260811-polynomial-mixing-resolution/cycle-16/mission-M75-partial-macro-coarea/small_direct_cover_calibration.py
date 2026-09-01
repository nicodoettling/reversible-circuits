#!/usr/bin/env python3
"""Exact N=3,4 minimal-exterior calibration for direct certificates."""

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
CORE_PATH = HERE / "direct_free_component_search.py"


def load_core():
    spec = importlib.util.spec_from_file_location("m75_direct_core_small", CORE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(CORE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def components(word, edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    lengths = Counter()
    for index in word:
        a, b = edges[index]
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), []).append(v)
    for index in word:
        a, _b = edges[index]
        lengths[find(a)] += 1
    return tuple((tuple(vertices), lengths[root]) for root, vertices in groups.items())


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
        if a not in vertices:
            continue
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    return len({find(v) for v in vertices}) == 1


def direct_pair(word, data, core, perms, edges, n):
    identity = tuple(range(n))
    for vertices, length in data:
        genus = (length - 2 * (len(vertices) - 1)) // 2 if length else 0
        if genus < 1:
            continue
        positions = [
            position for position, index in enumerate(word)
            if edges[index][0] in vertices
        ]
        for i, j in itertools.combinations(positions, 2):
            remaining = word[:i] + word[i + 1 : j] + word[j + 1 :]
            if core.evaluate(remaining, perms, n) != identity:
                continue
            component_core = [
                index for position, index in enumerate(word)
                if position not in (i, j) and edges[index][0] in vertices
            ]
            if connected_on(vertices, component_core, edges):
                return i, j
    return None


def case(n, core):
    m = 2 * n - 2
    edges = core.edges_of(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    perms = tuple(core.edge_perm(edge, n) for edge in edges)
    identity = tuple(range(n))
    identity_count = 0
    exterior_count = 0
    direct_failures = 0
    radius_one_failures = 0
    success_generator_histogram = Counter()
    for word in itertools.product(range(len(edges)), repeat=m):
        if core.evaluate(word, perms, n) != identity:
            continue
        identity_count += 1
        data = components(word, edges, n)
        if len(data) == 1:
            continue
        exterior_count += 1
        if direct_pair(word, data, core, perms, edges, n) is not None:
            continue
        direct_failures += 1
        successes = 0
        for i in range(m - 1):
            for sign in (-1, 1):
                target = core.hurwitz(word, i, sign, edges, lookup)
                if direct_pair(target, data, core, perms, edges, n) is not None:
                    successes += 1
        success_generator_histogram[successes] += 1
        radius_one_failures += int(successes == 0)
    return {
        "N": n,
        "m": m,
        "identity_count": identity_count,
        "exterior_count": exterior_count,
        "direct_certificate_failure_count": direct_failures,
        "radius_one_failure_count": radius_one_failures,
        "successful_signed_generator_count_histogram": {
            str(count): frequency
            for count, frequency in sorted(success_generator_histogram.items())
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    core = load_core()
    cases = [case(n, core) for n in (3, 4)]
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
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab) and its inverse",
        "claim_tested": "At minimal ambient N=3,4, every exterior word has a direct connected deletion certificate or acquires one after one signed Hurwitz generator.",
        "scope_warning": "Finite survival cannot prove the universal statement.",
        "cases": cases,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
