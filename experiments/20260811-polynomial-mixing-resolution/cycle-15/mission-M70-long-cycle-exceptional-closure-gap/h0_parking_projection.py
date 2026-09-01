#!/usr/bin/env python3
"""Exact bounded diagnostic for cyclic averaging of parking macros.

For the minimal long-cycle bridge, this enumerates all Dénes factorizations by
Hurwitz BFS, computes Stanley's parking multiplicity vector, and computes the
exact rank of the map

    f(d(w)) -> (1/n) sum_q f(d(U^q w)).

The rank is a finite falsifier only.  It cannot establish an asymptotic gap.
"""

from __future__ import annotations

import argparse
import collections
import json
import platform
import subprocess
from pathlib import Path

import numpy as np
import sympy

from n7_exceptional_krylov import Edge, Perm, conjugate_edge, minimal_words, transpositions


def parking_labels(n: int, word_edges: tuple[Edge, ...]) -> tuple[int, ...]:
    blocks = [{i} for i in range(n)]
    labels: list[int] = []
    for a, b in word_edges:
        ia = next(i for i, block in enumerate(blocks) if a in block)
        ib = next(i for i, block in enumerate(blocks) if b in block)
        first, second = blocks[ia], blocks[ib]
        if min(first) > min(second):
            first, second = second, first
            ia, ib = ib, ia
        minimum_second = min(second)
        labels.append(max(x for x in first if x < minimum_second))
        merged = first | second
        blocks = [block for j, block in enumerate(blocks) if j not in (ia, ib)]
        blocks.append(merged)
    return tuple(labels)


def parking_macro(n: int, word: tuple[int, ...], edges: list[Edge]) -> tuple[int, ...]:
    labels = parking_labels(n, tuple(edges[i] for i in word))
    return tuple(labels.count(i) for i in range(n))


def support_degrees(n: int, word: tuple[int, ...], edges: list[Edge]) -> tuple[int, ...]:
    degrees = [0] * n
    for index in word:
        a, b = edges[index]
        degrees[a] += 1
        degrees[b] += 1
    return tuple(sorted(degrees))


def rank_mod_prime(rows: list[tuple[int, ...]], prime: int) -> int:
    """Dense modular elimination; a full column rank certifies the Q-rank."""
    array = np.asarray(rows, dtype=np.int64) % prime
    nrows, ncols = array.shape
    pivot_row = 0
    for column in range(ncols):
        candidates = np.flatnonzero(array[pivot_row:, column])
        if not len(candidates):
            continue
        selected = pivot_row + int(candidates[0])
        if selected != pivot_row:
            array[[pivot_row, selected]] = array[[selected, pivot_row]]
        inverse = pow(int(array[pivot_row, column]), -1, prime)
        array[pivot_row] = (array[pivot_row] * inverse) % prime
        factors = array[:, column].copy()
        factors[pivot_row] = 0
        nonzero = np.flatnonzero(factors)
        array[nonzero] = (
            array[nonzero] - factors[nonzero, None] * array[pivot_row]
        ) % prime
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def analyze(n: int) -> dict[str, object]:
    edges, gates = transpositions(n)
    words = minimal_words(n, edges, gates)
    word_set = set(words)
    edge_index = {edge: i for i, edge in enumerate(edges)}

    def cyclic_conjugate(word: tuple[int, ...]) -> tuple[int, ...]:
        answer = []
        for index in word:
            a, b = edges[index]
            answer.append(edge_index[tuple(sorted(((a - 1) % n, (b - 1) % n)))])
        return tuple(answer)

    macros = {word: parking_macro(n, word, edges) for word in words}
    macro_values = sorted(set(macros.values()))
    macro_index = {macro: i for i, macro in enumerate(macro_values)}
    unseen = set(words)
    rows: list[tuple[int, ...]] = []
    row_degree_multisets: list[tuple[int, ...]] = []
    orbit_representatives: list[tuple[int, ...]] = []
    while unseen:
        representative = min(unseen)
        orbit = []
        current = representative
        for _ in range(n):
            if current in orbit:
                raise AssertionError("cyclic action was not free")
            orbit.append(current)
            current = cyclic_conjugate(current)
        if current != representative or any(word not in word_set for word in orbit):
            raise AssertionError("invalid cyclic orbit")
        unseen.difference_update(orbit)
        counts = [0] * len(macro_values)
        for word in orbit:
            counts[macro_index[macros[word]]] += 1
        rows.append(tuple(counts))
        row_degree_multisets.append(support_degrees(n, representative, edges))
        orbit_representatives.append(representative)

    primes = (1000003, 1000033)
    modular_ranks = {str(prime): rank_mod_prime(rows, prime) for prime in primes}
    max_modular_rank = max(modular_ranks.values())
    if max_modular_rank == len(macro_values):
        # A nonzero full minor modulo a prime is a nonzero integer minor, so
        # the rational rank is at least the number of columns and hence equal.
        rational_rank = len(macro_values)
        rank_certificate = "full column rank certified by a modular nonzero minor"
    else:
        # This branch is modest in the bounded cases where it occurs. Use an
        # exact domain-matrix calculation rather than call a modular lower
        # bound the rational rank.
        matrix = sympy.polys.matrices.DomainMatrix.from_list(
            [list(row) for row in rows], sympy.ZZ
        ).convert_to(sympy.QQ)
        rational_rank = int(matrix.rank())
        rank_certificate = "exact DomainMatrix rank over ZZ/QQ"

    # Two simple exact tests of possible "small unrooted statistic" collapse.
    distributions_by_degree: dict[tuple[int, ...], set[tuple[int, ...]]] = collections.defaultdict(set)
    for degree_multiset, row in zip(row_degree_multisets, rows):
        distributions_by_degree[degree_multiset].add(row)
    first_degree_collision = None
    for degree_multiset, distributions in sorted(distributions_by_degree.items()):
        if len(distributions) > 1:
            first_degree_collision = {
                "support_degree_multiset": degree_multiset,
                "distinct_cyclic_macro_distributions": len(distributions),
                "examples": sorted(distributions)[:2],
            }
            break

    # Averaged symmetric square statistic.  This is constant only if every
    # orbit has the same value; comparison with support degrees may reveal an
    # unrooted-tree interpretation without assuming it universally.
    square_averages = []
    square_by_degrees: dict[tuple[int, ...], set[int]] = collections.defaultdict(set)
    for degree_multiset, row in zip(row_degree_multisets, rows):
        total = sum(
            multiplicity * sum(x * x for x in macro)
            for multiplicity, macro in zip(row, macro_values)
        )
        square_averages.append(total)  # denominator is n for every orbit
        square_by_degrees[degree_multiset].add(total)

    return {
        "N": n,
        "states": len(words),
        "cyclic_orbits": len(rows),
        "parking_macros": len(macro_values),
        "A0_macro_rank_over_Q": rational_rank,
        "modular_rank_lower_bounds": modular_ranks,
        "rank_certificate": rank_certificate,
        "A0_macro_is_constant": rational_rank == 1,
        "distinct_cyclic_macro_distributions": len(set(rows)),
        "support_degree_multisets": len(distributions_by_degree),
        "cyclic_distribution_determined_by_support_degree_multiset": all(
            len(values) == 1 for values in distributions_by_degree.values()
        ),
        "first_same_degree_different_distribution": first_degree_collision,
        "distinct_n_times_average_sum_macro_squares": sorted(set(square_averages)),
        "square_average_determined_by_support_degree_multiset": all(
            len(values) == 1 for values in square_by_degrees.values()
        ),
        "first_orbit_representative": orbit_representatives[0],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=7)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "claim_tested": (
            "Cyclic averaging A0 annihilates every centered function of the "
            "Stanley parking multiplicity macro, equivalently its bounded exact rank is one."
        ),
        "scope_warning": (
            "A rank greater than one rigorously refutes constancy; finite ranks cannot prove "
            "an asymptotic H0 gap or identify the universal quotient."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "results": [analyze(n) for n in range(3, args.n_max + 1)],
        "python": platform.python_version(),
        "sympy": sympy.__version__,
        "seed": None,
        "deterministic": True,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["results"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
