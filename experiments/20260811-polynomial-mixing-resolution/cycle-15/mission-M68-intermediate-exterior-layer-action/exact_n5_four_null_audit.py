#!/usr/bin/env python3
"""Exact N=5 test of the genus-one four-null strand lemma.

For every genus-one connected component word occurring in an exterior
identity word at m=8, test whether some component label has four null
increments under prefix strand erasure and leaves a connected minimal word.
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
M64_SOURCE = (
    HERE.parent.parent
    / "cycle-14"
    / "mission-M64-multistep-minimal-exterior-closure-redteam"
    / "exact_n5_signature_closure.py"
)
M68_MACRO_SOURCE = HERE / "exact_n5_macro_saturation_audit.py"
M49_SOURCE = (
    HERE.parent.parent
    / "cycle-12"
    / "mission-M49-symmetric-branch-balance"
    / "strand_deletion_falsifier.py"
)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def connected(vertices, projected_word, projected_edges, deleted, ambient_n):
    old_to_new = {}
    next_index = 0
    for old in range(ambient_n):
        if old == deleted:
            continue
        old_to_new[old] = next_index
        next_index += 1
    wanted = {old_to_new[v] for v in vertices if v != deleted}
    if len(wanted) <= 1:
        return True
    parent = {v: v for v in wanted}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge_index in projected_word:
        a, b = projected_edges[edge_index]
        if a in wanted and b in wanted:
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
    return len({find(v) for v in wanted}) == 1


def has_deletable_adjacent_square(component_word, vertices, all_edges):
    for position in range(len(component_word) - 1):
        if component_word[position] != component_word[position + 1]:
            continue
        remaining = [
            edge_index for i, edge_index in enumerate(component_word)
            if i not in (position, position + 1)
        ]
        parent = {v: v for v in vertices}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for edge_index in remaining:
            a, b = all_edges[edge_index]
            x, y = find(a), find(b)
            if x != y:
                parent[y] = x
        if len({find(v) for v in vertices}) == 1:
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = load("m64_for_m68_four_null", M64_SOURCE)
    macro_source = load("m68_macro_for_four_null", M68_MACRO_SOURCE)
    deletion = load("m49_for_m68_four_null", M49_SOURCE)
    all_edges = source.M59.edges(source.N)
    _all_codes, exterior = source.identity_words(all_edges)
    cache = {}
    occurrence_count = 0
    for index, code in enumerate(exterior):
        word = macro_source.decode(code, source.LENGTH, source.M)
        signature = macro_source.macro_signature(code, source, all_edges)
        for mask, length in signature:
            vertices = tuple(v for v in range(source.N) if mask & (1 << v))
            genus = 0 if length == 0 else (length - 2 * (len(vertices) - 1)) // 2
            if genus != 1:
                continue
            component_word = tuple(
                edge_index for edge_index in word
                if mask & (1 << all_edges[edge_index][0])
            )
            key = (vertices, component_word)
            occurrence_count += 1
            if key in cache:
                continue
            witnesses = []
            if has_deletable_adjacent_square(component_word, vertices, all_edges):
                witnesses.append({"label": "adjacent_square", "null_positions": []})
            for v in vertices:
                projected, nulls, projected_edges = deletion.delete_strand(
                    list(component_word), all_edges, source.N, v
                )
                if len(nulls) == 4 and connected(
                    vertices, projected, projected_edges, v, source.N
                ):
                    witnesses.append({"label": v, "null_positions": list(nulls)})
            cache[key] = witnesses
        if index and index % 200000 == 0:
            print(json.dumps({
                "tested_exterior": index,
                "unique_genus_one_words": len(cache),
                "failures": sum(not value for value in cache.values()),
            }), flush=True)
    failures = [
        {
            "vertices": list(key[0]),
            "word_edge_indices": list(key[1]),
        }
        for key, value in cache.items() if not value
    ]
    witness_count = Counter(len(value) for value in cache.values())
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
        "convention": "(pq)(x)=p(q(x)); prefix strand erasure as in accepted M49",
        "claim_tested": "Every connected genus-one identity word either has a deletable adjacent square or a label with four null increments and connected minimal deletion output.",
        "scope_warning": "Finite component words through ambient N=5 can refute only the named universal lemma.",
        "ambient_N": source.N,
        "ambient_m": source.LENGTH,
        "genus_one_component_occurrences": occurrence_count,
        "unique_genus_one_component_words": len(cache),
        "failure_count": len(failures),
        "failure_examples": failures[:20],
        "witness_label_count_distribution": {str(k): v for k, v in sorted(witness_count.items())},
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
