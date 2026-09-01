#!/usr/bin/env python3
"""Exact product-path connectivity test for pair-length-four Q bridges."""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import shlex
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from l3_endpoint_quotient import (
    UnionFind,
    class_size,
    compose,
    edge_word,
    inverse,
    partitions,
    representative,
    transpositions,
)


def analyze_n(n: int) -> dict[str, object]:
    started = time.perf_counter()
    gates_full = transpositions(n)
    gate_edges = [(a, b) for a, b, _ in gates_full]
    gates = [p for _, _, p in gates_full]
    micro_pairs = list(itertools.product(range(len(gates)), repeat=2))
    product_to_micro: dict[tuple[int, ...], list[tuple[int, int]]] = defaultdict(list)
    for pair in micro_pairs:
        value = compose(gates[pair[0]], gates[pair[1]])
        product_to_micro[value].append(pair)
    support = sorted(product_to_micro)
    support_index = {value: index for index, value in enumerate(support)}
    support_inverse = [inverse(value) for value in support]
    multiplicity = [len(product_to_micro[value]) for value in support]

    block_fiber_count: Counter[tuple[int, ...]] = Counter()
    for i, a in enumerate(support):
        for j, b in enumerate(support):
            block_fiber_count[compose(a, b)] += multiplicity[i] * multiplicity[j]

    endpoint_types = [
        cycle_type
        for cycle_type in partitions(n)
        if (n - len(cycle_type)) % 2 == 0 and n - len(cycle_type) <= 8
    ]
    endpoints = []
    total_words_by_classes = 0
    all_connected = True

    for cycle_type in endpoint_types:
        endpoint = representative(cycle_type)
        paths: list[tuple[int, int, int, int]] = []
        path_weights: list[int] = []
        for ai, a in enumerate(support):
            a_inverse_endpoint = compose(support_inverse[ai], endpoint)
            for bi, _b in enumerate(support):
                b_inverse_a_inverse_endpoint = compose(
                    support_inverse[bi], a_inverse_endpoint
                )
                for ci, _c in enumerate(support):
                    d = compose(support_inverse[ci], b_inverse_a_inverse_endpoint)
                    di = support_index.get(d)
                    if di is None:
                        continue
                    paths.append((ai, bi, ci, di))
                    path_weights.append(
                        multiplicity[ai]
                        * multiplicity[bi]
                        * multiplicity[ci]
                        * multiplicity[di]
                    )

        uf = UnionFind(len(paths))
        representatives: dict[tuple[int, int, int], int] = {}
        for state_id, (ai, bi, ci, di) in enumerate(paths):
            # At a fixed endpoint the outside increment products determine
            # the refreshed adjacent-pair product, so no extra key is needed.
            keys = ((0, ci, di), (1, ai, di), (2, ai, bi))
            for key in keys:
                previous = representatives.setdefault(key, state_id)
                uf.union(state_id, previous)

        component_weights: Counter[int] = Counter()
        component_paths: Counter[int] = Counter()
        component_representatives: dict[int, list[list[int]]] = {}
        for state_id, ((ai, bi, ci, di), weight) in enumerate(zip(paths, path_weights)):
            root = uf.find(state_id)
            component_weights[root] += weight
            component_paths[root] += 1
            if root not in component_representatives:
                products = [support[index] for index in (ai, bi, ci, di)]
                micro = [product_to_micro[value][0] for value in products]
                component_representatives[root] = sum(
                    (edge_word(pair, gate_edges) for pair in micro), []
                )

        roots = sorted(component_weights)
        connected = len(roots) == 1
        all_connected &= connected
        fiber_size = sum(path_weights)
        total_words_by_classes += class_size(cycle_type) * fiber_size

        for word in component_representatives.values():
            value = tuple(range(n))
            edge_to_gate = {
                edge: gate for edge, gate in zip(gate_edges, gates)
            }
            for edge in word:
                value = compose(value, edge_to_gate[tuple(edge)])
            assert value == endpoint

        endpoints.append(
            {
                "cycle_type": list(cycle_type),
                "transposition_defect": n - len(cycle_type),
                "symmetric_group_class_size": class_size(cycle_type),
                "product_paths": len(paths),
                "microfactorized_fiber_size": fiber_size,
                "components": len(roots),
                "component_product_path_sizes": sorted(
                    component_paths.values(), reverse=True
                ),
                "component_microfactorized_sizes": sorted(
                    component_weights.values(), reverse=True
                ),
                "representative_words_by_component": [
                    component_representatives[root] for root in roots
                ],
                "connected": connected,
            }
        )

    assert total_words_by_classes == len(gates) ** 8
    return {
        "N": n,
        "transpositions": len(gates),
        "naive_eight_word_count": len(gates) ** 8,
        "ordered_micro_pairs": len(micro_pairs),
        "Q_support_size": len(support),
        "endpoint_cycle_types_tested": len(endpoint_types),
        "all_endpoint_types_connected": all_connected,
        "H4_conditional_fiber_min": min(block_fiber_count.values()),
        "H4_conditional_fiber_max": max(block_fiber_count.values()),
        "eight_word_class_mass_check": total_words_by_classes,
        "endpoints": endpoints,
        "elapsed_seconds": time.perf_counter() - started,
    }


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "For every N>=3 and every feasible endpoint h, the pair-length-four "
            "microfactorized Q bridge is connected under its three aligned H4 heat baths. "
            "A finite disconnected endpoint refutes this l=4 subclaim and the broader "
            "base-connectivity proposition; finite survival proves no universal claim or gap."
        ),
        "microfactor_quotient_lemma": (
            "Projection to Q-increment products preserves connectivity: every H4 move "
            "projects to adjacent-pair product resampling, while arbitrary ordered "
            "microfactor labels can be refreshed by an H4 outcome that retains both "
            "increment products. Thus components equal components of the product-path chain."
        ),
        "convention": "compose(p,q)=p after q; word=t1...t8; Q=P_transposition^2",
        "kernel_normalization": (
            "The nonlazy aligned chain chooses one of three H4 windows with probability 1/3 "
            "and then samples uniformly from its exact four-factor same-product fiber."
        ),
        "command": shlex.join([sys.executable, *sys.argv]),
        "seed": None,
        "python": platform.python_version(),
        "commit": git_commit(),
        "cases": [analyze_n(n) for n in args.N],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
