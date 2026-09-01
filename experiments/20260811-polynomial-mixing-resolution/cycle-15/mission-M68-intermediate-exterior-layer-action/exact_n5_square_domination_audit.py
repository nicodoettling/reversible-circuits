#!/usr/bin/env python3
"""Exact N=5 falsifier for one-step marked-square domination of each macro.

A marked state has an adjacent square inside a positive-genus support
component whose deletion leaves that component connected.  We test whether
every exterior state is itself marked or shares some H3/H4/H5 outside-window
signature with a marked state in the same labeled weighted macro.
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


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def connected_on(vertices, edge_indices, all_edges):
    if len(vertices) <= 1:
        return True
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


def marked(code, source, macro_source, all_edges):
    word = macro_source.decode(code, source.LENGTH, source.M)
    signature = macro_source.macro_signature(code, source, all_edges)
    vertex_component = {}
    for component_index, (mask, length) in enumerate(signature):
        if length == 0:
            continue
        for vertex in range(source.N):
            if mask & (1 << vertex):
                vertex_component[vertex] = component_index
    by_component = [[] for _ in signature]
    for position, edge_index in enumerate(word):
        a, _b = all_edges[edge_index]
        by_component[vertex_component[a]].append((position, edge_index))
    for position in range(source.LENGTH - 1):
        if word[position] != word[position + 1]:
            continue
        a, _b = all_edges[word[position]]
        component_index = vertex_component[a]
        mask, length = signature[component_index]
        vertices = [v for v in range(source.N) if mask & (1 << v)]
        genus = (length - 2 * (len(vertices) - 1)) // 2
        if genus < 1:
            continue
        remaining = [
            edge_index
            for old_position, edge_index in by_component[component_index]
            if old_position not in (position, position + 1)
        ]
        if connected_on(vertices, remaining, all_edges):
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    source = load("m64_for_m68_domination", M64_SOURCE)
    macro_source = load("m68_macro_for_domination", M68_MACRO_SOURCE)
    all_edges = source.M59.edges(source.N)
    _all_codes, exterior = source.identity_words(all_edges)
    macros = {}
    marked_codes = []
    for index, code in enumerate(exterior):
        signature = macro_source.macro_signature(code, source, all_edges)
        macros[code] = signature
        if marked(code, source, macro_source, all_edges):
            marked_codes.append(code)
        if index and index % 200000 == 0:
            print(json.dumps({"classified": index, "marked": len(marked_codes)}), flush=True)

    target_keys = set()
    marked_by_macro = Counter()
    for code in marked_codes:
        signature = macros[code]
        marked_by_macro[signature] += 1
        for r, i in source.WINDOWS:
            target_keys.add((signature, r, i, source.outside_key(code, r, i)))

    undominated_by_macro = Counter()
    dominated_by_macro = Counter()
    examples = []
    marked_set = set(marked_codes)
    for index, code in enumerate(exterior):
        signature = macros[code]
        dominated = code in marked_set or any(
            (signature, r, i, source.outside_key(code, r, i)) in target_keys
            for r, i in source.WINDOWS
        )
        if dominated:
            dominated_by_macro[signature] += 1
        else:
            undominated_by_macro[signature] += 1
            if len(examples) < 20:
                examples.append({
                    "word_edge_indices": list(macro_source.decode(code, source.LENGTH, source.M)),
                    "signature": [[mask, length] for mask, length in signature],
                })
        if index and index % 200000 == 0:
            print(json.dumps({"tested": index, "undominated": sum(undominated_by_macro.values())}), flush=True)

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
        "convention": "(pq)(x)=p(q(x)); literal H3/H4/H5 outside-window adjacency",
        "claim_tested": "Every exterior state is at literal K graph distance at most one from a deletable-surplus-square state in the same macro.",
        "scope_warning": "Finite N=5 can refute only the named domination lemma.",
        "N": source.N,
        "m": source.LENGTH,
        "exterior_size": len(exterior),
        "marked_size": len(marked_codes),
        "marked_macro_count": len(marked_by_macro),
        "macro_count": len(set(macros.values())),
        "dominated_size": sum(dominated_by_macro.values()),
        "undominated_size": sum(undominated_by_macro.values()),
        "undominated_macro_count": len(undominated_by_macro),
        "undominated_examples": examples,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
