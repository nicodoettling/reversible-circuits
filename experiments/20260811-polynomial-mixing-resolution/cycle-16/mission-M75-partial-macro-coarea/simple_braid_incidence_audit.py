#!/usr/bin/env python3
"""Exact simple-positive-braid incidence/stabilizer audit on S_3,k=6."""

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


def load_core():
    spec = importlib.util.spec_from_file_location("m75_positive_incidence", CORE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(CORE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    core = load_core()
    n = 3
    k = 6
    edges = core.edge_list(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    perms = tuple(core.perm(edge, n) for edge in edges)
    identity = tuple(range(n))
    words = [
        word
        for word in itertools.product(range(len(edges)), repeat=k)
        if core.product(word, perms, n) == identity
        and core.connected_support(word, edges, n)
    ]
    orders = tuple(itertools.permutations(range(k)))
    row_hits = Counter()
    row_distinct_outputs = Counter()
    row_max_parallel = Counter()
    column_indegree = Counter()
    column_distinct_sources = {}
    for source in words:
        outputs = Counter()
        hits = 0
        for order in orders:
            target, _length = core.positive_lift(source, order, edges, lookup)
            outputs[target] += 1
            column_indegree[target] += 1
            hits += int(core.marked(target, edges, n))
        row_hits[hits] += 1
        row_distinct_outputs[len(outputs)] += 1
        row_max_parallel[max(outputs.values())] += 1
    marked_count = sum(core.marked(word, edges, n) for word in words)
    total_marked_incidence = sum(hits * frequency for hits, frequency in row_hits.items())
    expected_total = len(orders) * marked_count
    assert total_marked_incidence == expected_total
    assert set(column_indegree) == set(words)
    assert set(column_indegree.values()) == {len(orders)}
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
        "convention": "(pq)(x)=p(q(x)); canonical simple positive braid beta_pi",
        "claim_tested": "The simple-positive-braid multigraph is m!-regular on both sides, including stabilizer parallel-edge multiplicity, while marked row sums need not be constant.",
        "scope_warning": "Finite nonconstant row sums prove only that double regularity does not itself flatten worst-source marked probability.",
        "N": n,
        "component_length": k,
        "source_count": len(words),
        "simple_braid_count": len(orders),
        "marked_state_count": marked_count,
        "marked_state_density": [marked_count, len(words)],
        "row_marked_hit_count_histogram": {
            str(count): frequency for count, frequency in sorted(row_hits.items())
        },
        "row_distinct_output_count_histogram": {
            str(count): frequency
            for count, frequency in sorted(row_distinct_outputs.items())
        },
        "row_max_parallel_multiplicity_histogram": {
            str(count): frequency
            for count, frequency in sorted(row_max_parallel.items())
        },
        "column_indegree_distinct_values": sorted(set(column_indegree.values())),
        "total_marked_incidence": total_marked_incidence,
        "regularity_predicted_marked_incidence": expected_total,
        "marked_row_sums_constant": len(row_hits) == 1,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
