#!/usr/bin/env python3
"""Exact full-K boundary audit for two Cycle-05 nonnormal candidate cuts."""

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
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, ...]
Word = tuple[int, ...]


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p after q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> tuple[list[tuple[int, int]], list[Permutation]]:
    edges: list[tuple[int, int]] = []
    gates: list[Permutation] = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            edges.append((a, b))
            gates.append(tuple(p))
    return edges, gates


def product(word: tuple[int, ...], gates: list[Permutation], identity: Permutation) -> Permutation:
    answer = identity
    for index in word:
        answer = compose(answer, gates[index])
    return answer


def connected_on_all(word: Word, edges: list[tuple[int, int]], n: int) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for index in word:
        union(*edges[index])
    return len({find(v) for v in range(n)}) == 1


def removable_leaf_marks(
    word: Word, edges: list[tuple[int, int]], n: int
) -> list[tuple[int, int, int]]:
    """Return (omitted vertex, zero-based pair start, neighbor) certificates."""
    marks: list[tuple[int, int, int]] = []
    for start in range(len(word) - 1):
        if word[start] != word[start + 1]:
            continue
        a, b = edges[word[start]]
        for omitted, neighbor in ((a, b), (b, a)):
            if any(
                omitted in edges[index]
                for position, index in enumerate(word)
                if position not in (start, start + 1)
            ):
                continue

            remaining = [v for v in range(n) if v != omitted]
            parent = {v: v for v in remaining}

            def find(x: int) -> int:
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(x: int, y: int) -> None:
                x, y = find(x), find(y)
                if x != y:
                    parent[y] = x

            for position, index in enumerate(word):
                if position in (start, start + 1):
                    continue
                x, y = edges[index]
                if omitted in (x, y):
                    raise AssertionError("omitted vertex occurs outside marked square")
                union(x, y)
            if len({find(v) for v in remaining}) == 1:
                marks.append((omitted, start, neighbor))
    return marks


def connected_minimal_count(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 1
    return math.factorial(2 * n - 2) * n ** (n - 3)


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
    hook_product = 1
    for row_index, row_length in enumerate(shape):
        for column in range(row_length):
            below = sum(
                lower_row > column for lower_row in shape[row_index + 1 :]
            )
            hook_product *= row_length - column + below
    return math.factorial(sum(shape)) // hook_product


def content_scalar(shape: tuple[int, ...]) -> int:
    return sum(
        column - row_index
        for row_index, row_length in enumerate(shape)
        for column in range(row_length)
    )


def identity_word_count_character(n: int, m: int) -> int:
    numerator = sum(
        irrep_dimension(shape) ** 2 * content_scalar(shape) ** m
        for shape in partitions(n)
    )
    assert numerator % math.factorial(n) == 0
    return numerator // math.factorial(n)


def fraction_record(value: Fraction) -> dict[str, object]:
    return {"fraction": str(value), "decimal": float(value)}


def build_fibers(
    gates: list[Permutation], identity: Permutation, lengths: tuple[int, ...]
) -> dict[int, dict[Permutation, tuple[Word, ...]]]:
    answer: dict[int, dict[Permutation, tuple[Word, ...]]] = {}
    for length in lengths:
        grouped: dict[Permutation, list[Word]] = defaultdict(list)
        for block in itertools.product(range(len(gates)), repeat=length):
            grouped[product(block, gates, identity)].append(block)
        answer[length] = {key: tuple(value) for key, value in grouped.items()}
    return answer


def analyze_cut(
    name: str,
    words: list[Word],
    flags: dict[Word, bool],
    fibers: dict[int, dict[Permutation, tuple[Word, ...]]],
    gates: list[Permutation],
    identity: Permutation,
    lengths: tuple[int, ...],
) -> dict[str, object]:
    m = len(words[0])
    block_types = len(lengths)
    raw_out = {length: Fraction(0) for length in lengths}
    raw_in = {length: Fraction(0) for length in lengths}

    for word in words:
        source_flag = flags[word]
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
                    if source_flag and not target_flag:
                        out_count += 1
                    elif not source_flag and target_flag:
                        in_count += 1
                denominator = windows * len(outcomes)
                raw_out[length] += Fraction(out_count, denominator)
                raw_in[length] += Fraction(in_count, denominator)

    scale = Fraction(1, 2 * block_types * len(words))
    by_length_out = {length: scale * raw_out[length] for length in lengths}
    by_length_in = {length: scale * raw_in[length] for length in lengths}
    flow_out = sum(by_length_out.values(), Fraction(0))
    flow_in = sum(by_length_in.values(), Fraction(0))
    assert flow_out == flow_in

    count_a = sum(flags.values())
    pi_a = Fraction(count_a, len(words))
    pi_b = 1 - pi_a
    conductance = flow_out / min(pi_a, pi_b)
    outward = flow_out / pi_a
    return {
        "name": name,
        "state_count": len(words),
        "A_count": count_a,
        "pi_A": fraction_record(pi_a),
        "flow_A_to_Ac": fraction_record(flow_out),
        "flow_Ac_to_A": fraction_record(flow_in),
        "flow_by_block_length": {
            str(length): fraction_record(by_length_out[length])
            for length in lengths
        },
        "outward_conductance": fraction_record(outward),
        "smaller_side_conductance": fraction_record(conductance),
    }


def analyze_case(n: int, m: int) -> dict[str, object]:
    started = time.perf_counter()
    identity = tuple(range(n))
    edges, gates = transpositions(n)
    lengths = tuple(length for length in (3, 4, 5) if length <= m)
    fibers = build_fibers(gates, identity, lengths)
    words = [
        word
        for word in itertools.product(range(len(gates)), repeat=m)
        if product(word, gates, identity) == identity
    ]
    word_set = set(words)
    assert len(word_set) == len(words)
    character_omega = identity_word_count_character(n, m)
    assert len(words) == character_omega

    fixed_vertex = 0
    star_flags = {
        word: fixed_vertex in edges[word[0]]
        for word in words
    }
    star = analyze_cut(
        "first-join star cut", words, star_flags, fibers, gates, identity, lengths
    )
    M = len(gates)
    B = len(lengths)
    q = Fraction(1, 2 * B * (m - 2) * M * M)
    assert star["pi_A"]["fraction"] == str(Fraction(2, n))
    assert Fraction(star["outward_conductance"]["fraction"]) >= q
    star["proved_one_outcome_lower_bound"] = fraction_record(q)

    result: dict[str, object] = {
        "N": n,
        "m": m,
        "M": M,
        "R_m": list(lengths),
        "omega_size": len(words),
        "character_sum_omega_size": character_omega,
        "conditional_fiber_size_ranges": {
            str(length): [
                min(len(fiber) for fiber in fibers[length].values()),
                max(len(fiber) for fiber in fibers[length].values()),
            ]
            for length in lengths
        },
        "star_cut": star,
        "elapsed_seconds_before_minimal_cut": time.perf_counter() - started,
    }

    if m == 2 * (n - 1):
        full_flags = {
            word: connected_on_all(word, edges, n)
            for word in words
        }
        full = analyze_cut(
            "minimal full-support macro",
            words,
            full_flags,
            fibers,
            gates,
            identity,
            lengths,
        )
        full_words = [word for word in words if full_flags[word]]
        marks_by_word = {
            word: removable_leaf_marks(word, edges, n)
            for word in full_words
        }
        total_marks = sum(len(marks) for marks in marks_by_word.values())
        certified_states = sum(bool(marks) for marks in marks_by_word.values())
        expected_marks = Fraction(total_marks, len(full_words))
        predicted_total_marks = (
            n
            * (n - 1)
            * (m - 1)
            * connected_minimal_count(n - 1)
        )
        assert len(full_words) == connected_minimal_count(n)
        assert total_marks == predicted_total_marks
        assert max(map(len, marks_by_word.values())) <= n
        certified_fraction = Fraction(certified_states, len(full_words))
        exact_certificate_lower = certified_fraction * q
        crude_universal_lower = Fraction(1, 16 * B * n * (m - 2) * M * M)
        assert Fraction(full["outward_conductance"]["fraction"]) >= exact_certificate_lower
        assert exact_certificate_lower >= crude_universal_lower
        full["connected_count_formula"] = connected_minimal_count(n)
        full["stationary_mass_formula"] = (
            "(2N-2)! N^(N-3) / |Omega(N,2N-2)|"
        )
        full["marked_leaf_square_total"] = total_marks
        full["marked_leaf_square_formula"] = (
            "N(N-1)(2N-3)|F_(N-1)|"
        )
        full["expected_marked_leaf_squares"] = fraction_record(expected_marks)
        full["states_with_certificate"] = certified_states
        full["certificate_probability"] = fraction_record(certified_fraction)
        full["exact_certificate_flow_lower_per_pi_A"] = fraction_record(
            exact_certificate_lower
        )
        full["proved_crude_lower_per_pi_A"] = fraction_record(
            crude_universal_lower
        )
        full["max_marks_in_case"] = max(map(len, marks_by_word.values()))
        full["mark_histogram"] = {
            str(value): count
            for value, count in sorted(
                Counter(map(len, marks_by_word.values())).items()
            )
        }
        result["minimal_full_support_cut"] = full

    result["elapsed_seconds"] = time.perf_counter() - started
    return result


def git_commit() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = [(3, 4), (4, 4), (4, 6)]
    result = {
        "claim_tested": (
            "The first-join star cut, and at m=2(N-1) the minimal full-support "
            "macro cut, have inverse-polynomial original-K boundary. A failed "
            "exact mass, leaf-square incidence, reversibility, or lower-bound "
            "check would refute the corresponding analytic accounting; finite "
            "survival proves no universal statement."
        ),
        "target": "uniform global identity bridge law",
        "convention": "compose(p,q)=p after q; word=t1...tm",
        "kernel": (
            "K=I/2 plus, with total mass 1/2, uniform block size in R_m, "
            "uniform legal window, and uniform exact same-product block"
        ),
        "boundary_scope": (
            "Every r=3,4,5 contribution is enumerated; for m=4 the r=4 "
            "term is the whole-word heat bath."
        ),
        "python": platform.python_version(),
        "seed": None,
        "commit": git_commit(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "cases": [analyze_case(n, m) for n, m in cases],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
