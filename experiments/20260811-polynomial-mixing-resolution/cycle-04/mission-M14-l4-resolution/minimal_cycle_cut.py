#!/usr/bin/env python3
"""Exact balanced-tree crossing cut for the first nontrivial minimal bridge.

This is a bounded falsification test, not an asymptotic mixing experiment.
It tests whether the balanced crossing-count threshold is invariant or has
zero boundary already for the N=7, length-six minimal 7-cycle bridge.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import platform
import shlex
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p after q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> tuple[list[Edge], list[Permutation]]:
    edges: list[Edge] = []
    permutations: list[Permutation] = []
    for a in range(n):
        for b in range(a + 1, n):
            value = list(range(n))
            value[a], value[b] = value[b], value[a]
            edges.append((a, b))
            permutations.append(tuple(value))
    return edges, permutations


def word_product(word: tuple[int, ...], gates: list[Permutation], n: int) -> Permutation:
    value = tuple(range(n))
    for index in word:
        value = compose(value, gates[index])
    return value


def cycle_endpoint(n: int) -> Permutation:
    return tuple((i + 1) % n for i in range(n))


def conjugate_edge(first: Edge, second: Edge) -> Edge:
    """Return second * first * second for transposition edges."""
    a, b = first
    c, d = second

    def apply_second(x: int) -> int:
        if x == c:
            return d
        if x == d:
            return c
        return x

    return tuple(sorted((apply_second(a), apply_second(b))))  # type: ignore[return-value]


def hurwitz_orbit(n: int, edges: list[Edge], gates: list[Permutation]) -> list[tuple[int, ...]]:
    edge_index = {edge: i for i, edge in enumerate(edges)}
    # (0,n-1)(0,n-2)...(0,1) is (0 1 ... n-1) in the project convention.
    start = tuple(edge_index[(0, j)] for j in range(n - 1, 0, -1))
    endpoint = cycle_endpoint(n)
    assert word_product(start, gates, n) == endpoint
    queue = collections.deque([start])
    seen = {start}
    while queue:
        word = queue.popleft()
        for position in range(len(word) - 1):
            first = edges[word[position]]
            second = edges[word[position + 1]]
            image = edge_index[conjugate_edge(first, second)]
            changed = list(word)
            changed[position] = word[position + 1]
            changed[position + 1] = image
            new_word = tuple(changed)
            if new_word not in seen:
                seen.add(new_word)
                queue.append(new_word)
    answer = sorted(seen)
    assert len(answer) == n ** (n - 2)
    assert all(word_product(word, gates, n) == endpoint for word in answer)
    return answer


def polynomial_multiply(first: list[int], second: list[int]) -> list[int]:
    answer = [0] * (len(first) + len(second) - 1)
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            answer[i + j] += x * y
    return answer


def tree_crossing_coefficients(a: int, b: int) -> list[int]:
    # Weighted matrix-tree polynomial z(a+bz)^(a-1)(b+az)^(b-1).
    answer = [0, 1]
    for _ in range(a - 1):
        answer = polynomial_multiply(answer, [a, b])
    for _ in range(b - 1):
        answer = polynomial_multiply(answer, [b, a])
    return answer


def analyze(n: int) -> dict[str, object]:
    if n != 7:
        raise ValueError("This bounded certificate is intentionally fixed at N=7")
    started = time.perf_counter()
    edges, gates = transpositions(n)
    words = hurwitz_orbit(n, edges, gates)
    m = n - 1
    pair_length = m // 2
    left_size = n // 2
    left = set(range(left_size))
    crosses = [int((a in left) != (b in left)) for a, b in edges]

    histogram = collections.Counter(sum(crosses[index] for index in word) for word in words)
    coefficients = tree_crossing_coefficients(left_size, n - left_size)
    coefficient_histogram = {
        degree: count for degree, count in enumerate(coefficients) if count
    }
    histogram_matches_uniform_cayley_tree = (
        dict(sorted(histogram.items())) == coefficient_histogram
    )

    cumulative = 0
    threshold = min(histogram)
    for value in sorted(histogram):
        proposed = cumulative + histogram[value]
        if 2 * proposed <= len(words):
            cumulative = proposed
            threshold = value
        else:
            break
    assert 0 < cumulative <= len(words) // 2

    block_cross_multiplicity: dict[Permutation, collections.Counter[int]] = {}
    for block in itertools.product(range(len(edges)), repeat=4):
        product = word_product(block, gates, n)
        crossing_count = sum(crosses[index] for index in block)
        block_cross_multiplicity.setdefault(product, collections.Counter())[crossing_count] += 1

    window_starts = range(0, m - 3, 2)
    ratio_instances: collections.Counter[tuple[int, int]] = collections.Counter()
    reverse_ratio_instances: collections.Counter[tuple[int, int]] = collections.Counter()
    boundary_states = 0
    reverse_boundary_states = 0
    for word in words:
        x_value = sum(crosses[index] for index in word)
        state_crosses = False
        for start in window_starts:
            old_block = word[start : start + 4]
            old_crossing = sum(crosses[index] for index in old_block)
            product = word_product(old_block, gates, n)
            multiplicities = block_cross_multiplicity[product]
            fiber_size = sum(multiplicities.values())
            if x_value <= threshold:
                outside = sum(
                    count
                    for new_crossing, count in multiplicities.items()
                    if x_value - old_crossing + new_crossing > threshold
                )
                if outside:
                    state_crosses = True
                    ratio_instances[(outside, fiber_size)] += 1
            else:
                inside = sum(
                    count
                    for new_crossing, count in multiplicities.items()
                    if x_value - old_crossing + new_crossing <= threshold
                )
                if inside:
                    state_crosses = True
                    reverse_ratio_instances[(inside, fiber_size)] += 1
        if state_crosses:
            if x_value <= threshold:
                boundary_states += 1
            else:
                reverse_boundary_states += 1

    raw_ratio_sum = sum(
        instances * Fraction(outside, fiber_size)
        for (outside, fiber_size), instances in ratio_instances.items()
    )
    stationary_flow = raw_ratio_sum / ((pair_length - 1) * len(words))
    reverse_raw_ratio_sum = sum(
        instances * Fraction(inside, fiber_size)
        for (inside, fiber_size), instances in reverse_ratio_instances.items()
    )
    reverse_stationary_flow = reverse_raw_ratio_sum / (
        (pair_length - 1) * len(words)
    )
    assert reverse_stationary_flow == stationary_flow
    stationary_mass = Fraction(cumulative, len(words))
    conductance = stationary_flow / stationary_mass
    band_count = sum(
        count for value, count in histogram.items() if threshold - 3 <= value <= threshold
    )
    elapsed = time.perf_counter() - started

    return {
        "N": n,
        "endpoint": list(cycle_endpoint(n)),
        "microfactor_length": m,
        "pair_length": pair_length,
        "transpositions": len(edges),
        "states": len(words),
        "balanced_label_cut": [sorted(left), sorted(set(range(n)) - left)],
        "crossing_count_histogram": dict(sorted(histogram.items())),
        "matrix_tree_histogram": coefficient_histogram,
        "threshold_A_is_X_at_most": threshold,
        "A_size": cumulative,
        "A_stationary_mass": {
            "numerator": stationary_mass.numerator,
            "denominator": stationary_mass.denominator,
            "float": float(stationary_mass),
        },
        "boundary_state_count_in_A": boundary_states,
        "boundary_state_count_in_complement": reverse_boundary_states,
        "four_step_boundary_band_count": band_count,
        "stationary_boundary_flow": {
            "numerator": stationary_flow.numerator,
            "denominator": stationary_flow.denominator,
            "float": float(stationary_flow),
        },
        "reverse_stationary_boundary_flow": {
            "numerator": reverse_stationary_flow.numerator,
            "denominator": reverse_stationary_flow.denominator,
            "float": float(reverse_stationary_flow),
        },
        "conductance_of_A": {
            "numerator": conductance.numerator,
            "denominator": conductance.denominator,
            "float": float(conductance),
        },
        "distinct_outside_over_fiber_ratios": [
            {"outside": outside, "fiber_size": fiber_size, "instances": instances}
            for (outside, fiber_size), instances in sorted(ratio_instances.items())
        ],
        "elapsed_seconds": elapsed,
        "checks": {
            "hurwitz_orbit_equals_Denes_count": True,
            "raw_factorization_graph_is_uniform_Cayley_tree": (
                histogram_matches_uniform_cayley_tree
            ),
            "boundary_flow_positive": stationary_flow > 0,
            "forward_flow_equals_reverse_flow": True,
        },
    }


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "claim_tested": (
            "Two bounded claims for the first nontrivial odd-N minimal full-cycle "
            "bridge: (i) its raw factorization graph is uniform over Cayley trees; "
            "(ii) the balanced label-crossing threshold is invariant or has zero "
            "boundary. Failure of (i) or positive flow in (ii) refutes only those "
            "bounded shortcuts, not an asymptotic bottleneck or another cut."
        ),
        "target_distribution": "uniform fixed-product length-six transposition bridge",
        "convention": "compose(p,q)=p after q; word=t1...t6",
        "kernel": (
            "nonlazy aligned B_3: choose starts 1 or 3 with probability 1/2, "
            "then uniformly resample the exact same-product four-factor fiber"
        ),
        "command": shlex.join([sys.executable, *sys.argv]),
        "python": platform.python_version(),
        "seed": None,
        "commit": git_commit(),
        "result": analyze(args.N),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
