#!/usr/bin/env python3
"""Exact positive-permutation-braid calibration on the N=6 witness."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
POSITIVE_SOURCE = HERE / "positive_permutation_braid_audit.py"
VERIFY_SOURCE = HERE / "verify_radius_one_counterexample.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    positive = load("m75_positive_for_counterexample", POSITIVE_SOURCE)
    verifier = load("m75_verify_for_positive", VERIFY_SOURCE)
    core = verifier.load_search()
    n = 5
    ambient_n = 6
    word = (0, 1, 2, 8, 1, 6, 8, 9, 1, 8)
    edges = positive.edge_list(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    perms = tuple(positive.perm(edge, n) for edge in edges)
    total = math.factorial(len(word))
    hits = 0
    hits_by_length = Counter()
    for count, order in enumerate(itertools.permutations(range(len(word))), 1):
        endpoint, move_count = positive.positive_lift(word, order, edges, lookup)
        marked = any(
            endpoint[i] == endpoint[i + 1]
            and core.connected_after_deletion(endpoint, i, i + 1, edges, n)
            for i in range(len(endpoint) - 1)
        )
        hits += int(marked)
        if marked:
            hits_by_length[move_count] += 1
        if count % 500000 == 0:
            print(json.dumps({"tested": count, "hits": hits}), flush=True)
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
        "convention": "(pq)(x)=p(q(x)); canonical positive permutation braid",
        "claim_tested": "The exact N=6 radius-one counterexample has positive marked-endpoint probability under a uniform positive permutation braid.",
        "scope_warning": "One finite positive probability cannot prove a uniform inverse-polynomial asymptotic bound.",
        "ambient_N": ambient_n,
        "ambient_m": len(word),
        "component_N": n,
        "word_edge_indices": list(word),
        "permutation_count": total,
        "marked_endpoint_count": hits,
        "marked_endpoint_probability": [hits, total],
        "marked_hits_by_braid_length": {
            str(length): count for length, count in sorted(hits_by_length.items())
        },
        "expected_braid_length": [len(word) * (len(word) - 1), 4],
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "permutation_count": total,
        "hits": hits,
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
