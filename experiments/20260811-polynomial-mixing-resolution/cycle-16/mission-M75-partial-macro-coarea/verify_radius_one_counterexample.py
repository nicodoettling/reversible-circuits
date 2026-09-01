#!/usr/bin/env python3
"""Verify the exact ambient-N=6 radius-one direct-certificate obstruction."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import platform
import subprocess
import sys
import time
from pathlib import Path


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SEARCH_SOURCE = HERE / "direct_free_component_search.py"


def load_search():
    spec = importlib.util.spec_from_file_location("m75_direct_search", SEARCH_SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(SEARCH_SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def all_certificate_pairs(word, core, perms, edges, n):
    identity = tuple(range(n))
    answer = []
    for i, j in itertools.combinations(range(len(word)), 2):
        remaining = word[:i] + word[i + 1 : j] + word[j + 1 :]
        product = core.evaluate(remaining, perms, n)
        connected = core.connected_after_deletion(word, i, j, edges, n)
        if product == identity:
            answer.append({
                "positions_zero_based": [i, j],
                "connected": connected,
            })
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    core = load_search()
    component_n = 5
    ambient_n = 6
    edges = core.edges_of(component_n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    perms = tuple(core.edge_perm(edge, component_n) for edge in edges)
    word = (0, 1, 2, 8, 1, 6, 8, 9, 1, 8)
    identity = tuple(range(component_n))
    assert core.evaluate(word, perms, component_n) == identity
    assert core.direct_certificate(word, perms, edges, component_n) is None
    source_pairs = all_certificate_pairs(word, core, perms, edges, component_n)
    neighbor_audit = []
    two_step_paths = []
    distinct_neighbors = set()
    for i in range(len(word) - 1):
        for sign in (-1, 1):
            target = core.hurwitz(word, i, sign, edges, lookup)
            distinct_neighbors.add(target)
            pairs = all_certificate_pairs(target, core, perms, edges, component_n)
            assert not any(item["connected"] for item in pairs)
            neighbor_audit.append({
                "first_generator": [i, sign],
                "target_edge_indices": list(target),
                "identity_deletion_pairs": pairs,
            })
            for j in range(len(word) - 1):
                for sign2 in (-1, 1):
                    target2 = core.hurwitz(target, j, sign2, edges, lookup)
                    certificate = core.direct_certificate(
                        target2, perms, edges, component_n
                    )
                    if certificate is not None:
                        two_step_paths.append({
                            "generators": [[i, sign], [j, sign2]],
                            "target_edge_indices": list(target2),
                            "certificate_positions_zero_based": list(certificate),
                        })
    assert two_step_paths
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
        "claim_tested": "At minimal ambient N=6,m=10 there is a two-component exterior word whose positive-genus component is at Hurwitz distance exactly two from the connected direct-deletion-certificate set.",
        "scope_warning": "This refutes radius-one direct-certificate domination only; radius two succeeds for this finite witness and no asymptotic bottleneck follows.",
        "ambient_N": ambient_n,
        "ambient_m": len(word),
        "isolated_ambient_labels": [5],
        "positive_component_labels": list(range(component_n)),
        "positive_component_genus": 1,
        "component_edge_order": [list(edge) for edge in edges],
        "word_edge_indices": list(word),
        "word_edges": [list(edges[index]) for index in word],
        "word_product": list(core.evaluate(word, perms, component_n)),
        "source_identity_deletion_pairs": source_pairs,
        "source_connected_certificate_count": sum(
            item["connected"] for item in source_pairs
        ),
        "signed_generator_count": 2 * (len(word) - 1),
        "distinct_neighbor_count": len(distinct_neighbors),
        "neighbor_connected_certificate_count": 0,
        "neighbor_audit": neighbor_audit,
        "two_step_certificate_path_count": len(two_step_paths),
        "first_two_step_certificate_path": two_step_paths[0],
        "exact_distance_to_certificate_set": 2,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "source_identity_pairs": len(source_pairs),
        "distinct_neighbors": len(distinct_neighbors),
        "two_step_paths": len(two_step_paths),
        "distance": 2,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
