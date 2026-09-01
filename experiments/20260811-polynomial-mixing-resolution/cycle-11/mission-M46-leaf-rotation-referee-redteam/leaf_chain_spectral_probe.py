#!/usr/bin/env python3
"""Bounded spectral falsifier for the exact weighted leaf-rotation chain.

This computes the smallest eigenvalues of I-P for the nonlazy chain whose
canonical forward rate is 2*d_parent/[3*r*(r-1)] and whose reverse rate is
2/[3*r*(r-1)].  It can refute finite normalization or a proposed exact gap
formula; no finite run proves an asymptotic lower bound.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

import leaf_chain_bridge_probe as base


def run(r: int):
    states = list(base.degree_vectors(r))
    index = {state: i for i, state in enumerate(states)}
    weights = np.array([base.orbit_weight(state) for state in states], dtype=float)
    rows = []
    cols = []
    values = []
    diagonal = np.zeros(len(states), dtype=float)
    c = 2.0 / (3.0 * r * (r - 1))
    seen = set()
    for left, state in enumerate(states):
        children = base.children_from_degrees(state)
        for parent, child_row in enumerate(children):
            for leaf in child_row[:-1]:
                if state[leaf] != 0:
                    continue
                target = list(state)
                target[parent] -= 1
                target[leaf] += 1
                right = index[tuple(target)]
                edge = (min(left, right), max(left, right))
                if edge in seen:
                    raise AssertionError(("duplicate", state, target))
                seen.add(edge)
                # Similarity transform of I-P: off diagonal is
                # -Q(x,y)/sqrt(pi(x)pi(y)).  Detailed balance gives the
                # symmetric magnitude c*sqrt(d_parent).
                magnitude = c * np.sqrt(state[parent])
                rows.extend((left, right))
                cols.extend((right, left))
                values.extend((-magnitude, -magnitude))
                diagonal[left] += c * state[parent]
                diagonal[right] += c
    rows.extend(range(len(states)))
    cols.extend(range(len(states)))
    values.extend(diagonal.tolist())
    laplacian = sp.csr_matrix((values, (rows, cols)), shape=(len(states), len(states)))
    if len(states) <= 2:
        eigvals = np.linalg.eigvalsh(laplacian.toarray())
    else:
        eigvals = spla.eigsh(laplacian, k=min(5, len(states) - 1), which="SM", return_eigenvectors=False)
        eigvals.sort()
    if abs(eigvals[0]) > 1e-9:
        raise AssertionError(("stationary eigenvalue", r, eigvals))
    row_exit_max = float(diagonal.max())
    if row_exit_max > 1.0 + 1e-12:
        raise AssertionError(("invalid Markov normalization", r, row_exit_max))
    return {
        "r": r,
        "states": len(states),
        "edges": len(seen),
        "gap": float(eigvals[1]),
        "scaled_gap_r2": float(eigvals[1] * r * r),
        "scaled_gap_r3": float(eigvals[1] * r * r * r),
        "first_eigenvalues": [float(x) for x in eigvals],
        "maximum_exit_probability": row_exit_max,
        "scope": "bounded numerical eigensolve; asymptotic inference prohibited",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = [run(r) for r in range(args.r_min, args.r_max + 1)]
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
