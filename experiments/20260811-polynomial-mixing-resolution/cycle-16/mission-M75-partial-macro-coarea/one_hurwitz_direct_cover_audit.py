#!/usr/bin/env python3
"""Exact N=5 audit of a one-Hurwitz-then-direct marked cover.

For each exterior word lacking a connected identity-preserving two-deletion
pair, apply every adjacent right and inverse Hurwitz generator.  Test whether
some target has such a pair.  If yes, one more fixed position-indexed bubble
exposes a connected-deletable adjacent square.  The resulting candidate
family has polynomial size and length; a surviving finite audit is not an
asymptotic proof.
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
M68 = (
    HERE.parent.parent
    / "cycle-15"
    / "mission-M68-intermediate-exterior-layer-action"
)
DELETE_SOURCE = M68 / "exact_n5_two_deletion_audit.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def conjugate_edge(a, b, edges, lookup):
    x, y = edges[a]
    p, q = edges[b]

    def act(v):
        if v == p:
            return q
        if v == q:
            return p
        return v

    return lookup[tuple(sorted((act(x), act(y))))]


def hurwitz(word, i, sign, edges, lookup):
    a, b = word[i], word[i + 1]
    out = list(word)
    if sign == 1:
        out[i] = b
        out[i + 1] = conjugate_edge(a, b, edges, lookup)
    else:
        out[i] = conjugate_edge(b, a, edges, lookup)
        out[i + 1] = a
    return tuple(out)


def direct_pair(word, signature, source, all_edges):
    identity = tuple(range(source.N))
    for mask, length in signature:
        vertices = [v for v in range(source.N) if mask & (1 << v)]
        genus = (length - 2 * (len(vertices) - 1)) // 2 if length else 0
        if genus < 1:
            continue
        positions = [
            i for i, edge_index in enumerate(word)
            if mask & (1 << all_edges[edge_index][0])
        ]
        for i, j in itertools.combinations(positions, 2):
            remaining = tuple(x for p, x in enumerate(word) if p not in (i, j))
            if source.M59.evaluate(source.N, all_edges, remaining) != identity:
                continue
            component_core = [word[p] for p in positions if p not in (i, j)]
            if source_delete.connected(vertices, component_core, all_edges):
                return i, j
    return None


source_delete = None


def main():
    global source_delete
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    source_delete = load("m68_delete_for_m75", DELETE_SOURCE)
    source = load("m64_for_m75", source_delete.M64_SOURCE)
    macro_source = load("m68_macro_for_m75", source_delete.M68_MACRO_SOURCE)
    all_edges = source.M59.edges(source.N)
    lookup = {edge: i for i, edge in enumerate(all_edges)}
    _all_codes, exterior = source.identity_words(all_edges)
    initial_failures = 0
    one_move_success = 0
    residual = []
    successful_generator_count = Counter()
    first_success_distance = Counter()
    for index, code in enumerate(exterior):
        word = macro_source.decode(code, source.LENGTH, source.M)
        signature = macro_source.macro_signature(code, source, all_edges)
        if direct_pair(word, signature, source, all_edges) is not None:
            continue
        initial_failures += 1
        successes = []
        for i in range(source.LENGTH - 1):
            for sign in (-1, 1):
                target = hurwitz(word, i, sign, all_edges, lookup)
                pair = direct_pair(target, signature, source, all_edges)
                if pair is not None:
                    successes.append((i, sign, pair))
                    first_success_distance[pair[1] - pair[0]] += 1
        successful_generator_count[len(successes)] += 1
        if successes:
            one_move_success += 1
        elif len(residual) < 20:
            residual.append({
                "word_edge_indices": list(word),
                "signature": [[mask, length] for mask, length in signature],
            })
        if index and index % 200000 == 0:
            print(json.dumps({
                "tested": index,
                "initial_failures": initial_failures,
                "residual_count": initial_failures - one_move_success,
            }), flush=True)
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
        "claim_tested": "Every N=5,m=8 exterior word either has a connected identity-preserving direct two-deletion pair or acquires one after one adjacent Hurwitz move.",
        "scope_warning": "Exact N=5 survival cannot prove the universal one-Hurwitz cover.",
        "N": source.N,
        "m": source.LENGTH,
        "exterior_size": len(exterior),
        "initial_direct_pair_failure_count": initial_failures,
        "one_hurwitz_success_count": one_move_success,
        "residual_failure_count": initial_failures - one_move_success,
        "residual_examples": residual,
        "successful_generator_count_histogram": {
            str(count): frequency
            for count, frequency in sorted(successful_generator_count.items())
        },
        "successful_pair_distance_histogram_over_generators": {
            str(distance): count
            for distance, count in sorted(first_success_distance.items())
        },
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
