#!/usr/bin/env python3
"""Exact finite Hessian test for the natural Hurwitz-weighted Higgs lift.

For p=id on c=d singleton cycle atoms, a colored Higgs basis B projects to
two forest-component partitions.  Giving B coefficient

  (2r)! (2c-2r)! / product(component sizes)

makes its key marginal exactly the M113 Hurwitz cell weight, because each
component has |C|^(|C|-2) Cayley spanning trees.  The script tests the
quadratic-derivative signature required by Lorentzianity.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np


def ground(c):
    return tuple(
        (color, i, j)
        for color in (0, 1)
        for i in range(c)
        for j in range(i + 1, c)
    )


def partition(c, edge_set, color=None):
    parent = list(range(c))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge_color, i, j in edge_set:
        if color is not None and edge_color != color:
            continue
        i, j = find(i), find(j)
        if i != j:
            parent[j] = i
    blocks = {}
    for x in range(c):
        blocks.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(sorted(block)) for block in blocks.values()))


def forest(c, edge_set, color):
    selected = [e for e in edge_set if e[0] == color]
    return len(partition(c, selected, color)) == c - len(selected)


def bases(c):
    elements = ground(c)
    answer = []
    for candidate in itertools.combinations(range(len(elements)), c):
        edge_set = tuple(elements[i] for i in candidate)
        if not forest(c, edge_set, 0) or not forest(c, edge_set, 1):
            continue
        if len(partition(c, edge_set)) != 1:
            continue
        answer.append(frozenset(candidate))
    return elements, tuple(answer)


def weight(c, base, elements, include_factorial):
    edge_set = tuple(elements[i] for i in base)
    denominator = 1
    for color in (0, 1):
        for block in partition(c, edge_set, color):
            denominator *= len(block)
    numerator = 1
    if include_factorial:
        red = sum(elements[i][0] == 0 for i in base)
        numerator = math.factorial(2 * red) * math.factorial(2 * c - 2 * red)
    return Fraction(numerator, denominator)


def encode_edge(edge):
    color, i, j = edge
    return ["red" if color == 0 else "blue", i, j]


def determinant(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    answer = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work))
                      if work[row][column]), None)
        if pivot is None:
            return Fraction()
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            answer = -answer
        value = work[column][column]
        answer *= value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / value
            for j in range(column + 1, len(work)):
                work[row][j] -= ratio * work[column][j]
    return answer


def run_case(c, include_factorial):
    elements, family = bases(c)
    weights = {base: weight(c, base, elements, include_factorial)
               for base in family}
    max_second = -float("inf")
    witness = None
    derivative_count = 0
    for derivative in itertools.combinations(range(len(elements)), c - 2):
        derivative = frozenset(derivative)
        if not any(derivative <= base for base in family):
            continue
        derivative_count += 1
        remaining = [i for i in range(len(elements)) if i not in derivative]
        index = {value: pos for pos, value in enumerate(remaining)}
        hessian = np.zeros((len(remaining), len(remaining)), dtype=float)
        exact_hessian = [[Fraction() for _ in remaining] for _ in remaining]
        exact_entries = {}
        for base, coefficient in weights.items():
            if not derivative <= base:
                continue
            pair = tuple(base - derivative)
            if len(pair) != 2:
                raise AssertionError("wrong derivative degree")
            a, b = index[pair[0]], index[pair[1]]
            hessian[a, b] += float(coefficient)
            hessian[b, a] += float(coefficient)
            exact_hessian[a][b] += coefficient
            exact_hessian[b][a] += coefficient
            exact_entries[tuple(sorted(pair))] = coefficient
        eig = np.linalg.eigvalsh(hessian)
        second = float(eig[-2]) if len(eig) >= 2 else -float("inf")
        if second > max_second:
            max_second = second
        positives = int(np.sum(eig > 1e-9))
        if positives > 1:
            exact_minor = None
            for positions in itertools.combinations(range(len(remaining)), 4):
                matrix = [[exact_hessian[i][j] for j in positions]
                          for i in positions]
                value = determinant(matrix)
                if value > 0:
                    exact_minor = {
                        "variables": [encode_edge(elements[remaining[i]])
                                      for i in positions],
                        "matrix": [[
                            {"numerator": x.numerator,
                             "denominator": x.denominator}
                            for x in row] for row in matrix],
                        "determinant_numerator": value.numerator,
                        "determinant_denominator": value.denominator,
                    }
                    break
            witness = {
                "derivative": [encode_edge(elements[i])
                               for i in sorted(derivative)],
                "positive_eigenvalues": positives,
                "eigenvalues": [float(x) for x in eig],
                "exact_positive_determinant_principal_minor": exact_minor,
                "nonzero_quadratic_coefficients": [
                    {
                        "edge_pair": [encode_edge(elements[i]) for i in pair],
                        "numerator": coefficient.numerator,
                        "denominator": coefficient.denominator,
                    }
                    for pair, coefficient in sorted(exact_entries.items())
                ],
            }
            break
    return {
        "cycle_atom_count": c,
        "ground_size": len(elements),
        "basis_count": len(family),
        "include_cut_factorials": include_factorial,
        "quadratic_derivatives_checked_before_stop": derivative_count,
        "maximum_second_eigenvalue_seen": max_second,
        "lorentzian_signature_witness": witness,
        "passes_checked_quadratic_signatures": witness is None,
    }


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if any(c < 2 or c > 4 for c in args.c):
        raise SystemExit("audit restricted to 2 <= c <= 4")
    payload = {
        "claim_tested": (
            "The natural colored-Higgs-basis augmentation with reciprocal "
            "component-size tilt and exact cut factorials is Lorentzian."
        ),
        "logical_scope": (
            "An explicit quadratic derivative with two positive Hessian "
            "eigenvalues refutes the named Lorentzian claim."
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seed": None,
        "cases": [
            run_case(c, include_factorial)
            for c in args.c for include_factorial in (False, True)
        ],
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
