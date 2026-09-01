#!/usr/bin/env python3
"""Exact all-cycle-type connectivity test for pair-length-three Q bridges.

The state graph on six transposition microfactors is represented exactly as
the edge-incidence graph between the ordered first and last transposition
pairs.  No six-letter word enumeration is performed.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import shlex
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p after q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(p)
    for i, value in enumerate(p):
        answer[value] = i
    return tuple(answer)


def transpositions(n: int) -> list[tuple[int, int, tuple[int, ...]]]:
    answer = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append((a, b, tuple(p)))
    return answer


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def representative(cycle_type: tuple[int, ...]) -> tuple[int, ...]:
    n = sum(cycle_type)
    p = list(range(n))
    start = 0
    for length in cycle_type:
        labels = list(range(start, start + length))
        for i, label in enumerate(labels):
            p[label] = labels[(i + 1) % length]
        start += length
    return tuple(p)


def class_size(cycle_type: tuple[int, ...]) -> int:
    multiplicities = Counter(cycle_type)
    denominator = 1
    for length, count in multiplicities.items():
        denominator *= (length**count) * math.factorial(count)
    return math.factorial(sum(cycle_type)) // denominator


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = bytearray(size)

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        first = self.find(first)
        second = self.find(second)
        if first == second:
            return
        if self.rank[first] < self.rank[second]:
            first, second = second, first
        self.parent[second] = first
        if self.rank[first] == self.rank[second]:
            self.rank[first] += 1


def edge_word(
    micro_pair: tuple[int, int],
    gate_edges: list[tuple[int, int]],
) -> list[list[int]]:
    return [list(gate_edges[index]) for index in micro_pair]


def analyze_n(n: int, verify_micro: bool) -> dict[str, object]:
    started = time.perf_counter()
    gates_full = transpositions(n)
    gate_edges = [(a, b) for a, b, _ in gates_full]
    gates = [p for _, _, p in gates_full]
    identity = tuple(range(n))
    micro_pairs = list(itertools.product(range(len(gates)), repeat=2))
    pair_product = {
        pair: compose(gates[pair[0]], gates[pair[1]]) for pair in micro_pairs
    }
    product_to_micro: dict[tuple[int, ...], list[tuple[int, int]]] = defaultdict(list)
    for pair, value in pair_product.items():
        product_to_micro[value].append(pair)
    support = sorted(product_to_micro)
    support_index = {value: index for index, value in enumerate(support)}
    support_inverse = {value: inverse(value) for value in support}
    multiplicity = {value: len(product_to_micro[value]) for value in support}

    endpoint_types = [
        cycle_type
        for cycle_type in partitions(n)
        if (n - len(cycle_type)) % 2 == 0 and n - len(cycle_type) <= 6
    ]
    endpoints = []
    total_words_by_classes = 0
    all_connected = True

    for cycle_type in endpoint_types:
        endpoint = representative(cycle_type)
        endpoint_inverse = inverse(endpoint)
        size = len(support)
        product_uf = UnionFind(2 * size)
        product_active: set[int] = set()
        product_edges: list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]] = []
        state_count = 0
        incidence_micro_edge_count = 0

        for a in support:
            left = support_index[a]
            a_inverse_endpoint = compose(support_inverse[a], endpoint)
            weight_a = multiplicity[a]
            for c in support:
                required_b = compose(a_inverse_endpoint, support_inverse[c])
                if required_b not in support_index:
                    continue
                right = size + support_index[c]
                product_uf.union(left, right)
                product_active.add(left)
                product_active.add(right)
                product_edges.append((a, c, required_b))
                weight_c = multiplicity[c]
                incidence_micro_edge_count += weight_a * weight_c
                state_count += weight_a * multiplicity[required_b] * weight_c

        product_roots = {product_uf.find(node) for node in product_active}
        component_state_sizes: Counter[int] = Counter()
        component_representative: dict[int, list[list[int]]] = {}
        for a, c, required_b in product_edges:
            root = product_uf.find(support_index[a])
            weight = multiplicity[a] * multiplicity[required_b] * multiplicity[c]
            component_state_sizes[root] += weight
            if root not in component_representative:
                pair_a = product_to_micro[a][0]
                pair_b = product_to_micro[required_b][0]
                pair_c = product_to_micro[c][0]
                component_representative[root] = (
                    edge_word(pair_a, gate_edges)
                    + edge_word(pair_b, gate_edges)
                    + edge_word(pair_c, gate_edges)
                )

        micro_components = None
        if verify_micro:
            micro_size = len(micro_pairs)
            micro_index = {pair: index for index, pair in enumerate(micro_pairs)}
            micro_uf = UnionFind(2 * micro_size)
            micro_active: set[int] = set()
            micro_edges_seen = 0
            for pair_a in micro_pairs:
                a = pair_product[pair_a]
                left = micro_index[pair_a]
                a_inverse_endpoint = compose(inverse(a), endpoint)
                for pair_c in micro_pairs:
                    c = pair_product[pair_c]
                    required_b = compose(a_inverse_endpoint, inverse(c))
                    if required_b not in product_to_micro:
                        continue
                    right = micro_size + micro_index[pair_c]
                    micro_uf.union(left, right)
                    micro_active.add(left)
                    micro_active.add(right)
                    micro_edges_seen += 1
            micro_components = len({micro_uf.find(node) for node in micro_active})
            assert micro_components == len(product_roots)
            assert micro_edges_seen == incidence_micro_edge_count

        component_sizes = sorted(component_state_sizes.values(), reverse=True)
        assert sum(component_sizes) == state_count
        connected = len(product_roots) == 1
        all_connected &= connected
        total_words_by_classes += class_size(cycle_type) * state_count

        endpoints.append(
            {
                "cycle_type": list(cycle_type),
                "transposition_defect": n - len(cycle_type),
                "symmetric_group_class_size": class_size(cycle_type),
                "fiber_size": state_count,
                "product_support_left_right_vertices": 2 * len(product_active) // 2,
                "product_support_incidence_edges": len(product_edges),
                "ordered_micro_incidence_edges": incidence_micro_edge_count,
                "components": len(product_roots),
                "component_state_sizes": component_sizes,
                "micro_graph_components_when_checked": micro_components,
                "representative_words_by_component": [
                    component_representative[root] for root in sorted(product_roots)
                ],
                "connected": connected,
            }
        )

    assert total_words_by_classes == len(gates) ** 6

    def length_four_fiber(endpoint: tuple[int, ...]) -> int:
        answer = 0
        for a in support:
            required = compose(support_inverse[a], endpoint)
            if required in multiplicity:
                answer += multiplicity[a] * multiplicity[required]
        return answer

    q4_identity = length_four_fiber(identity)
    q4_sizes = [length_four_fiber(representative(cycle_type)) for cycle_type in endpoint_types]
    return {
        "N": n,
        "transpositions": len(gates),
        "naive_six_word_count": len(gates) ** 6,
        "ordered_micro_pairs": len(micro_pairs),
        "Q_support_size": len(support),
        "endpoint_cycle_types_tested": len(endpoint_types),
        "all_endpoint_types_connected": all_connected,
        "micro_graph_crosscheck_enabled": verify_micro,
        "length_four_identity_fiber_size": q4_identity,
        "length_four_feasible_fiber_min": min(size for size in q4_sizes if size),
        "length_four_feasible_fiber_max": max(q4_sizes),
        "six_word_class_mass_check": total_words_by_classes,
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
    parser.add_argument("--verify-micro-through", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "For every N>=3 and every feasible endpoint h, the pair-length-three "
            "microfactorized Q bridge is connected under its two aligned H4 heat baths. "
            "A finite disconnected endpoint refutes this l=3 universal subclaim and the "
            "broader arbitrary-length base-connectivity proposition. Finite survival "
            "cannot prove either claim or a gap."
        ),
        "quotient_lemma": (
            "At l=3, state components equal components of the bipartite graph on "
            "ordered first/last transposition pairs, with A--C iff "
            "prod(A)^(-1) h prod(C)^(-1) lies in supp(Q). Product copies have "
            "identical neighborhoods; the product-support quotient preserves components."
        ),
        "convention": "compose(p,q)=p after q; word=t1...t6; Q=P_transposition^2",
        "kernel_normalization": (
            "The nonlazy aligned chain chooses either H4 window with probability 1/2 "
            "and then samples uniformly from its exact same-product four-factor fiber. "
            "Connectivity uses only positive support."
        ),
        "command": shlex.join([sys.executable, *sys.argv]),
        "seed": None,
        "python": platform.python_version(),
        "commit": git_commit(),
        "cases": [analyze_n(n, n <= args.verify_micro_through) for n in args.N],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
