#!/usr/bin/env python3
"""Exact falsification harness for prefix-standard-character closure.

Universal lemma tested (a finite counterexample refutes it): for every N,m,
the span of the constant function and the standard characters
chi_std(X_j), 1<=j<=m-1, is invariant under the exact lazy {3,4,5}
same-product heat-bath K.  The script constructs K acting on these features
without materializing the full transition matrix and checks exact rational
column-space membership.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import sympy

COMMIT = "502a6f031c6d5a4bc0064ee5b370a4fa3914f993"


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def transpositions(n: int):
    answer = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append((a, b, tuple(p)))
    return answer


def product(word, n: int):
    value = identity(n)
    for factor in word:
        value = compose(value, factor)
    return value


def prefix_standard_characters(word, n: int):
    value = identity(n)
    features = []
    for factor in word[:-1]:
        value = compose(value, factor)
        fixed = sum(value[x] == x for x in range(n))
        features.append(fixed - 1)
    return tuple(features)


def edge_word(word, permutation_to_edge):
    return [list(permutation_to_edge[p]) for p in word]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n, m = args.N, args.m
    trans = transpositions(n)
    factors = [p for _, _, p in trans]
    permutation_to_edge = {p: (a, b) for a, b, p in trans}
    e = identity(n)
    states = [word for word in itertools.product(factors, repeat=m) if product(word, n) == e]
    feature_rows = [(1,) + prefix_standard_characters(word, n) for word in states]
    rset = [r for r in (3, 4, 5) if r <= m]

    @lru_cache(maxsize=None)
    def fiber(r: int, target: tuple[int, ...]):
        return tuple(
            block
            for block in itertools.product(factors, repeat=r)
            if product(block, n) == target
        )

    # Exact K action on every feature column.
    acted_rows = []
    for state, row in zip(states, feature_rows):
        acted = [Fraction(x, 2) for x in row]  # lazy half
        for r in rset:
            starts = m - r + 1
            for i in range(starts):
                old_product = product(state[i : i + r], n)
                options = fiber(r, old_product)
                coefficient = Fraction(1, 2 * len(rset) * starts * len(options))
                for block in options:
                    candidate = state[:i] + block + state[i + r :]
                    candidate_row = (1,) + prefix_standard_characters(candidate, n)
                    for column, value in enumerate(candidate_row):
                        acted[column] += coefficient * value
        acted_rows.append(tuple(acted))

    feature_matrix = sympy.Matrix(feature_rows)
    base_rank = feature_matrix.rank()
    failures = []
    for column in range(len(feature_rows[0])):
        target = sympy.Matrix([sympy.Rational(row[column].numerator, row[column].denominator) for row in acted_rows])
        augmented_rank = feature_matrix.row_join(target).rank()
        if augmented_rank > base_rank:
            # A same-feature/different-image pair is the most transparent
            # witness when available.
            buckets = {}
            witness = None
            for index, (source_features, image) in enumerate(zip(feature_rows, acted_rows)):
                key = source_features
                value = image[column]
                if key in buckets and buckets[key][1] != value:
                    first = buckets[key]
                    witness = {
                        "source_features": list(key),
                        "word_1": edge_word(states[first[0]], permutation_to_edge),
                        "word_2": edge_word(states[index], permutation_to_edge),
                        "K_feature_word_1": f"{first[1].numerator}/{first[1].denominator}",
                        "K_feature_word_2": f"{value.numerator}/{value.denominator}",
                    }
                    break
                buckets[key] = (index, value)
            failures.append(
                {
                    "feature_column": column,
                    "feature_name": "constant" if column == 0 else f"chi_std_X_{column}",
                    "base_rank": base_rank,
                    "augmented_rank": augmented_rank,
                    "same_feature_witness": witness,
                }
            )

    payload = {
        "repository_commit": COMMIT,
        "claim_tested": (
            "The span of 1 and chi_std(X_j), 1<=j<=m-1, is invariant under "
            "the exact lazy {3,4,5} heat-bath K. One exact finite failure "
            "refutes the universal closure lemma but says nothing by itself "
            "about asymptotic mixing."
        ),
        "convention": "(pq)(x)=p(q(x)); word=t_1...t_m",
        "parameters": {"N": n, "m": m, "R_m": rset},
        "deterministic": True,
        "random_seed": None,
        "environment": {"python": platform.python_version(), "sympy": sympy.__version__},
        "state_count": len(states),
        "feature_column_count": len(feature_rows[0]),
        "feature_rank": base_rank,
        "fiber_sizes": {
            f"r={r},type={target}": len(fiber(r, target))
            for r in rset
            for target in sorted({product(state[i : i + r], n) for state in states for i in range(m - r + 1)})
        },
        "closure_failure_count": len(failures),
        "failures": failures,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
