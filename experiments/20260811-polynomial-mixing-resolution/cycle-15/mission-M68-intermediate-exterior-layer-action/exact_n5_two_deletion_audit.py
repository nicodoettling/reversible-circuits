#!/usr/bin/env python3
"""Exact N=5 test of connected two-deletion surplus extraction.

For each exterior word, test whether some two positions inside a positive-
genus support component can be deleted while preserving the identity product
and connected support on that component.  Such a pair can be exposed as an
adjacent square by one fixed right-Hurwitz bubble indexed only by its two
positions.
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
M64_SOURCE = (
    HERE.parent.parent
    / "cycle-14"
    / "mission-M64-multistep-minimal-exterior-closure-redteam"
    / "exact_n5_signature_closure.py"
)
M68_MACRO_SOURCE = HERE / "exact_n5_macro_saturation_audit.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def connected(vertices, edge_indices, all_edges):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index in edge_indices:
        a, b = all_edges[index]
        if a in parent and b in parent:
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
    return len({find(v) for v in vertices}) == 1


def has_pair(code, source, macro_source, all_edges):
    word = macro_source.decode(code, source.LENGTH, source.M)
    signature = macro_source.macro_signature(code, source, all_edges)
    for mask, length in signature:
        vertices = [v for v in range(source.N) if mask & (1 << v)]
        if length == 0 or (length - 2 * (len(vertices) - 1)) // 2 < 1:
            continue
        positions = [
            i for i, edge_index in enumerate(word)
            if mask & (1 << all_edges[edge_index][0])
        ]
        for i, j in itertools.combinations(positions, 2):
            remaining = tuple(x for p, x in enumerate(word) if p not in (i, j))
            if source.M59.evaluate(source.N, all_edges, remaining) != tuple(range(source.N)):
                continue
            remaining_component = [word[p] for p in positions if p not in (i, j)]
            if connected(vertices, remaining_component, all_edges):
                return i, j
    return None


def pair_audit(code, source, macro_source, all_edges):
    word = macro_source.decode(code, source.LENGTH, source.M)
    signature = macro_source.macro_signature(code, source, all_edges)
    positive = []
    for mask, length in signature:
        vertices = [v for v in range(source.N) if mask & (1 << v)]
        if length and (length - 2 * (len(vertices) - 1)) // 2 >= 1:
            positive.append((mask, vertices))
    answer = []
    for mask, vertices in positive:
        positions = [
            i for i, edge_index in enumerate(word)
            if mask & (1 << all_edges[edge_index][0])
        ]
        for i, j in itertools.combinations(positions, 2):
            remaining = tuple(x for p, x in enumerate(word) if p not in (i, j))
            product = source.M59.evaluate(source.N, all_edges, remaining)
            remaining_component = [word[p] for p in positions if p not in (i, j)]
            answer.append({
                "positions_zero_based": [i, j],
                "product": list(product),
                "identity": product == tuple(range(source.N)),
                "component_connected": connected(vertices, remaining_component, all_edges),
            })
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = load("m64_for_m68_delete", M64_SOURCE)
    macro_source = load("m68_macro_for_delete", M68_MACRO_SOURCE)
    all_edges = source.M59.edges(source.N)
    _all_codes, exterior = source.identity_words(all_edges)
    failures = []
    first_failure_code = None
    failure_by_components = Counter()
    success_distance = Counter()
    for index, code in enumerate(exterior):
        pair = has_pair(code, source, macro_source, all_edges)
        if pair is None:
            if first_failure_code is None:
                first_failure_code = code
            signature = macro_source.macro_signature(code, source, all_edges)
            failure_by_components[len(signature)] += 1
            if len(failures) < 20:
                failures.append({
                    "word_edge_indices": list(macro_source.decode(code, source.LENGTH, source.M)),
                    "signature": [[mask, length] for mask, length in signature],
                })
        else:
            success_distance[pair[1] - pair[0]] += 1
        if index and index % 200000 == 0:
            print(json.dumps({"tested": index, "failures": sum(failure_by_components.values())}), flush=True)
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
        "convention": "(pq)(x)=p(q(x)); direct deletion preserves ordered remaining word",
        "claim_tested": "Every exterior word has a connected identity-preserving two-deletion pair inside a positive-genus component.",
        "scope_warning": "Finite N=5 can refute only the named two-deletion lemma.",
        "N": source.N,
        "m": source.LENGTH,
        "exterior_size": len(exterior),
        "failure_count": sum(failure_by_components.values()),
        "failure_by_component_count": {str(k): v for k, v in sorted(failure_by_components.items())},
        "failure_examples": failures,
        "first_failure_pair_audit": (
            pair_audit(first_failure_code, source, macro_source, all_edges)
            if first_failure_code is not None else []
        ),
        "first_success_pair_distance_distribution": {str(k): v for k, v in sorted(success_distance.items())},
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
