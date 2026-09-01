#!/usr/bin/env python3
"""Exact N=5 falsifier for macro-saturation shortcuts in the M64 closure.

This imports the accepted signature-clique enumerator, reconstructs E0, and
groups exterior states by labeled weighted support-component data.  It can
falsify a claim that E0 is a union of whole Hurwitz macroscopic fibers; it
cannot prove any asymptotic expansion statement.
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
    spec = importlib.util.spec_from_file_location("m64_signature_for_m68", SOURCE)
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


def macro_signature(code: int, source, all_edges):
    word = decode(code, source.LENGTH, source.M)
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

    for edge_index in word:
        union(*all_edges[edge_index])
    masks = Counter()
    for vertex in range(source.N):
        masks[find(vertex)] |= 1 << vertex
    factor_counts = Counter()
    for edge_index in word:
        factor_counts[find(all_edges[edge_index][0])] += 1
    return tuple(sorted((mask, factor_counts[root]) for root, mask in masks.items()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = load_source()
    all_edges = source.M59.edges(source.N)
    A, _distribution, _selected = source.balanced_core_A(all_edges)
    _all_codes, exterior = source.identity_words(all_edges)
    signatures = source.signature_sets(A)
    E0 = [code for code in exterior if source.touches(signatures, code)]
    total = Counter(macro_signature(code, source, all_edges) for code in exterior)
    inside = Counter(macro_signature(code, source, all_edges) for code in E0)
    total_by_components = Counter()
    inside_by_components = Counter()
    for signature, size in total.items():
        total_by_components[len(signature)] += size
        inside_by_components[len(signature)] += inside[signature]
    partial = []
    full = []
    missed = []
    for signature, size in total.items():
        hit = inside[signature]
        item = {
            "signature": [[mask, length] for mask, length in signature],
            "total": size,
            "E0": hit,
            "fraction": hit / size,
        }
        if hit == 0:
            missed.append(item)
        elif hit == size:
            full.append(item)
        else:
            partial.append(item)
    partial.sort(key=lambda item: (item["fraction"], item["signature"]))
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
        "convention": "(pq)(x)=p(q(x)); support macro=(label bitmask,length)",
        "claim_tested": "E0 is a union of whole labeled weighted support-component macrofibers.",
        "scope_warning": "Exact N=5 falsification cannot establish an asymptotic theorem.",
        "N": source.N,
        "m": source.LENGTH,
        "A_size": len(A),
        "exterior_size": len(exterior),
        "E0_size": len(E0),
        "macro_count": len(total),
        "full_macro_count": len(full),
        "partial_macro_count": len(partial),
        "missed_macro_count": len(missed),
        "mass_by_component_count": {
            str(count): {
                "exterior": total_by_components[count],
                "E0": inside_by_components[count],
                "fraction": inside_by_components[count] / total_by_components[count],
            }
            for count in sorted(total_by_components)
        },
        "partial_examples_lowest_fraction": partial[:20],
        "partial_examples_highest_fraction": partial[-20:],
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in (
        "E0_size", "macro_count", "full_macro_count", "partial_macro_count",
        "missed_macro_count", "elapsed_seconds")}, sort_keys=True))


if __name__ == "__main__":
    main()
