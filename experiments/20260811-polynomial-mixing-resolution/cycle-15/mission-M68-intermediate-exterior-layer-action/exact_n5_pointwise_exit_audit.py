#!/usr/bin/env python3
"""Exact N=5 falsifier for pointwise exterior-to-minimal leakage.

For every exterior identity word, compute its literal one-step K probability
to `F_N minus A`, retaining H3/H4/H5, the lazy/scan factors, and exact clique
sizes.  A zero disproves a universal pointwise escape lemma; positive finite
values do not establish an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent.parent
    / "cycle-14"
    / "mission-M64-multistep-minimal-exterior-closure-redteam"
    / "exact_n5_signature_closure.py"
)


def load_source():
    spec = importlib.util.spec_from_file_location("m64_signature_for_m68_exit", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decode(code: int, length: int, alphabet: int):
    word = []
    for _ in range(length):
        word.append(code % alphabet)
        code //= alphabet
    return tuple(word)


def component_count(code: int, source, all_edges):
    parent = list(range(source.N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for edge_index in decode(code, source.LENGTH, source.M):
        union(*all_edges[edge_index])
    return len({find(vertex) for vertex in range(source.N)})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = load_source()
    all_edges = source.M59.edges(source.N)
    A, _distribution, _selected = source.balanced_core_A(all_edges)
    all_codes, exterior = source.identity_words(all_edges)
    exterior_set = set(exterior)
    safe = [code for code in all_codes if code not in exterior_set and code not in A]
    total_counts = source.group_counts(all_codes)
    safe_counts = source.group_counts(safe)

    zero_by_components = Counter()
    total_by_components = Counter()
    minimum_float = None
    minimum_code = None
    for index, code in enumerate(exterior):
        value = 0.0
        for r, i in source.WINDOWS:
            key = source.outside_key(code, r, i)
            target_count = safe_counts[(r, i)].get(key, 0)
            if target_count:
                value += target_count / (
                    6 * (source.LENGTH - r + 1) * total_counts[(r, i)][key]
                )
        count = component_count(code, source, all_edges)
        total_by_components[count] += 1
        if value == 0.0:
            zero_by_components[count] += 1
        if minimum_float is None or value < minimum_float:
            minimum_float = value
            minimum_code = code
        if index and index % 200000 == 0:
            print(json.dumps({"processed": index, "current_min": minimum_float}), flush=True)

    exact = Fraction(0)
    if minimum_code is not None:
        for r, i in source.WINDOWS:
            key = source.outside_key(minimum_code, r, i)
            target_count = safe_counts[(r, i)].get(key, 0)
            if target_count:
                exact += Fraction(
                    target_count,
                    6 * (source.LENGTH - r + 1) * total_counts[(r, i)][key],
                )
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
        "convention": "(pq)(x)=p(q(x)); literal lazy K with r=3,4,5",
        "claim_tested": "Every exterior state has positive one-step K flow to F_N minus A.",
        "scope_warning": "A zero refutes the named pointwise lemma only; finite positive values cannot prove asymptotic expansion.",
        "N": source.N,
        "m": source.LENGTH,
        "exterior_size": len(exterior),
        "safe_target_size": len(safe),
        "total_by_component_count": {str(k): v for k, v in sorted(total_by_components.items())},
        "zero_by_component_count": {str(k): v for k, v in sorted(zero_by_components.items())},
        "minimum_probability": f"{exact.numerator}/{exact.denominator}",
        "minimum_probability_float": float(exact),
        "minimum_word_edge_indices": list(decode(minimum_code, source.LENGTH, source.M)),
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
