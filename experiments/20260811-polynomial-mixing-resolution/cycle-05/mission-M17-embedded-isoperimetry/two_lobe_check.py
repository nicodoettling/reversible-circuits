#!/usr/bin/env python3
"""Exact falsifier for the balanced two-lobe midpoint-pinch cut."""

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
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Word = tuple[int, ...]


def compose(p: Permutation, q: Permutation) -> Permutation:
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> tuple[list[tuple[int, int]], list[Permutation]]:
    edges = []
    gates = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            edges.append((a, b))
            gates.append(tuple(p))
    return edges, gates


def product(word: Word, gates: list[Permutation], identity: Permutation) -> Permutation:
    value = identity
    for index in word:
        value = compose(value, gates[index])
    return value


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def irrep_dimension(shape: tuple[int, ...]) -> int:
    hooks = 1
    for row_index, row_length in enumerate(shape):
        for column in range(row_length):
            below = sum(row > column for row in shape[row_index + 1 :])
            hooks *= row_length - column + below
    return math.factorial(sum(shape)) // hooks


def content_scalar(shape: tuple[int, ...]) -> int:
    return sum(
        column - row_index
        for row_index, row_length in enumerate(shape)
        for column in range(row_length)
    )


def omega_count(n: int, m: int) -> int:
    numerator = sum(
        irrep_dimension(shape) ** 2 * content_scalar(shape) ** m
        for shape in partitions(n)
    )
    assert numerator % math.factorial(n) == 0
    return numerator // math.factorial(n)


def connected_identity_count(n: int) -> int:
    if n <= 2:
        return 1
    return math.factorial(2 * n - 2) * n ** (n - 3)


def fraction_record(value: Fraction) -> dict[str, object]:
    return {"fraction": str(value), "decimal": float(value)}


def support(word: Word, edges: list[tuple[int, int]]) -> frozenset[int]:
    return frozenset(v for index in word for v in edges[index])


def connected_on_set(
    word: Word, edges: list[tuple[int, int]], vertices: frozenset[int]
) -> bool:
    if not vertices:
        return False
    parent = {v: v for v in vertices}

    def find(v: int) -> int:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for index in word:
        a, b = edges[index]
        if a not in vertices or b not in vertices:
            return False
        union(a, b)
    return support(word, edges) == vertices and len({find(v) for v in vertices}) == 1


def is_two_lobe(
    word: Word,
    n: int,
    edges: list[tuple[int, int]],
    gates: list[Permutation],
    identity: Permutation,
) -> bool:
    if n % 2 == 0 or len(word) != 2 * (n - 1):
        return False
    half = n - 1
    left = word[:half]
    right = word[half:]
    if product(left, gates, identity) != identity:
        return False
    if product(right, gates, identity) != identity:
        return False
    left_support = support(left, edges)
    right_support = support(right, edges)
    s = (n - 1) // 2
    return (
        len(left_support) == s + 1
        and len(right_support) == s + 1
        and len(left_support & right_support) == 1
        and left_support | right_support == frozenset(range(n))
        and connected_on_set(left, edges, left_support)
        and connected_on_set(right, edges, right_support)
    )


def connected_half_words(
    vertices: frozenset[int],
    length: int,
    edges: list[tuple[int, int]],
    gates: list[Permutation],
    identity: Permutation,
) -> tuple[Word, ...]:
    allowed = [
        index
        for index, edge in enumerate(edges)
        if edge[0] in vertices and edge[1] in vertices
    ]
    words = []
    for word in itertools.product(allowed, repeat=length):
        if (
            product(word, gates, identity) == identity
            and connected_on_set(word, edges, vertices)
        ):
            words.append(word)
    return tuple(words)


def two_lobe_words(n: int) -> tuple[list[Word], list[tuple[int, int]], list[Permutation]]:
    assert n % 2 == 1 and n >= 3
    s = (n - 1) // 2
    half = 2 * s
    identity = tuple(range(n))
    edges, gates = transpositions(n)
    all_labels = frozenset(range(n))
    cache: dict[frozenset[int], tuple[Word, ...]] = {}
    answer: set[Word] = set()

    for articulation in range(n):
        others = [v for v in range(n) if v != articulation]
        for left_only in itertools.combinations(others, s):
            left_support = frozenset((articulation, *left_only))
            right_support = all_labels - frozenset(left_only)
            for vertices in (left_support, right_support):
                if vertices not in cache:
                    cache[vertices] = connected_half_words(
                        vertices, half, edges, gates, identity
                    )
            for left in cache[left_support]:
                for right in cache[right_support]:
                    word = left + right
                    assert is_two_lobe(word, n, edges, gates, identity)
                    answer.add(word)

    expected = (
        n
        * math.comb(2 * s, s)
        * connected_identity_count(s + 1) ** 2
    )
    assert len(answer) == expected
    return sorted(answer), edges, gates


def certificate_check(
    words: list[Word],
    n: int,
    edges: list[tuple[int, int]],
    gates: list[Permutation],
) -> dict[str, object]:
    identity = tuple(range(n))
    gate_index = {gate: index for index, gate in enumerate(gates)}
    half = n - 1
    unequal = 0
    equal = 0

    for word in words:
        a_index = word[half - 1]
        b_index = word[half]
        if a_index != b_index:
            a = gates[a_index]
            b = gates[b_index]
            bab = compose(compose(b, a), b)
            target = (
                word[: half - 1]
                + (b_index, gate_index[bab])
                + word[half + 1 :]
            )
            unequal += 1
        else:
            f_index = next(index for index in range(len(gates)) if index != a_index)
            target = (
                word[: half - 1]
                + (f_index, f_index)
                + word[half + 1 :]
            )
            equal += 1

        assert product(target, gates, identity) == identity
        assert product(target[:half], gates, identity) != identity
        assert not is_two_lobe(target, n, edges, gates, identity)

    return {
        "states_checked": len(words),
        "unequal_midpoint_pair": unequal,
        "equal_midpoint_pair": equal,
        "all_certificates_valid": True,
    }


def build_fibers(
    gates: list[Permutation], identity: Permutation, lengths: tuple[int, ...]
) -> dict[int, dict[Permutation, tuple[Word, ...]]]:
    result = {}
    for length in lengths:
        grouped: dict[Permutation, list[Word]] = defaultdict(list)
        for block in itertools.product(range(len(gates)), repeat=length):
            grouped[product(block, gates, identity)].append(block)
        result[length] = {key: tuple(value) for key, value in grouped.items()}
    return result


def exact_n3_flow() -> dict[str, object]:
    n, m = 3, 4
    identity = tuple(range(n))
    edges, gates = transpositions(n)
    lengths = (3, 4)
    fibers = build_fibers(gates, identity, lengths)
    omega = [
        word
        for word in itertools.product(range(len(gates)), repeat=m)
        if product(word, gates, identity) == identity
    ]
    flags = {
        word: is_two_lobe(word, n, edges, gates, identity)
        for word in omega
    }
    raw = {length: Fraction(0) for length in lengths}
    reverse = {length: Fraction(0) for length in lengths}

    for word in omega:
        source = flags[word]
        for length in lengths:
            windows = m - length + 1
            for start in range(windows):
                block_product = product(
                    word[start : start + length], gates, identity
                )
                outcomes = fibers[length][block_product]
                out_count = 0
                in_count = 0
                for block in outcomes:
                    target = word[:start] + block + word[start + length :]
                    target_flag = flags[target]
                    out_count += int(source and not target_flag)
                    in_count += int((not source) and target_flag)
                raw[length] += Fraction(out_count, windows * len(outcomes))
                reverse[length] += Fraction(in_count, windows * len(outcomes))

    scale = Fraction(1, 2 * len(lengths) * len(omega))
    by_length = {length: scale * raw[length] for length in lengths}
    by_length_reverse = {length: scale * reverse[length] for length in lengths}
    assert by_length == by_length_reverse
    flow = sum(by_length.values(), Fraction(0))
    pi_a = Fraction(sum(flags.values()), len(omega))
    return {
        "omega_size": len(omega),
        "A_count": sum(flags.values()),
        "pi_A": fraction_record(pi_a),
        "flow_by_block_length": {
            str(length): fraction_record(value)
            for length, value in by_length.items()
        },
        "flow": fraction_record(flow),
        "reverse_flow": fraction_record(
            sum(by_length_reverse.values(), Fraction(0))
        ),
        "outward_conductance": fraction_record(flow / pi_a),
        "smaller_side_conductance": fraction_record(
            flow / min(pi_a, 1 - pi_a)
        ),
    }


def formula_record(s: int) -> dict[str, object]:
    n = 2 * s + 1
    m = 4 * s
    connected_half = connected_identity_count(s + 1)
    cut_count = n * math.comb(2 * s, s) * connected_half**2
    full_count = connected_identity_count(n)
    total = omega_count(n, m)
    ratio = Fraction(cut_count, full_count)
    pi_a = Fraction(cut_count, total)
    M = n * (n - 1) // 2
    B = 2 if m == 4 else 3
    q = Fraction(1, 2 * B * (m - 2) * M * M)
    scaled = float(ratio * s * 16**s)
    return {
        "s": s,
        "N": n,
        "m": m,
        "cut_count": cut_count,
        "connected_half_count": connected_half,
        "full_macro_count": full_count,
        "omega_count": total,
        "conditional_mass_in_F": fraction_record(ratio),
        "global_pi_A": fraction_record(pi_a),
        "proved_conductance_lower": fraction_record(q),
        "scaled_conditional_mass_s_times_16_power_s": scaled,
    }


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()

    n3_words, n3_edges, n3_gates = two_lobe_words(3)
    n5_words, n5_edges, n5_gates = two_lobe_words(5)
    result = {
        "claim_tested": (
            "For every s>=1, the balanced two-lobe midpoint-pinch cut has "
            "the stated exact count and every state has one exact H3 exit. "
            "A failed count, product, midpoint, or small-case full-flow check "
            "would refute the universal construction; finite survival alone "
            "does not prove it."
        ),
        "target": "global uniform identity bridge law",
        "convention": "compose(p,q)=p after q; word=t1...tm",
        "kernel": (
            "K=I/2 plus total mass 1/2 split uniformly over R_m, legal "
            "windows, and exact same-product conditional blocks"
        ),
        "seed": None,
        "python": platform.python_version(),
        "commit": git_commit(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "calibration_counts": {
            "S3_m4": omega_count(3, 4),
            "S4_m4": omega_count(4, 4),
            "S4_m6": omega_count(4, 6),
        },
        "formula_cases": [formula_record(s) for s in range(1, 11)],
        "N3_certificate": certificate_check(n3_words, 3, n3_edges, n3_gates),
        "N5_certificate": certificate_check(n5_words, 5, n5_edges, n5_gates),
        "N3_full_K_flow": exact_n3_flow(),
        "asymptotic_target": {
            "expression": (
                "|A|/|F| ~ (8 sqrt(2) e / s) 16^(-s)"
            ),
            "limit_constant": 8 * math.sqrt(2) * math.e,
        },
    }
    result["elapsed_seconds"] = time.perf_counter() - started
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
