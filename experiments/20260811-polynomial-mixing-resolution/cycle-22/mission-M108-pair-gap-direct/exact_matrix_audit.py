#!/usr/bin/env python3
"""No-import finite audit for M108's pair-to-complete comparison.

Enumerates raw transposition bridge fibers, constructs exact conditional
projection matrices in floating form, and tests the proved PSD inequalities.
All finite checks are diagnostics only.

Convention: (pq)(x)=p(q(x)); factors multiply left-to-right.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


Perm = tuple[int, ...]
Word = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, x: int, y: int) -> Perm:
    answer = list(range(n))
    answer[x], answer[y] = answer[y], answer[x]
    return tuple(answer)


def evaluate(word: Word, gates: list[Perm]) -> Perm:
    answer = tuple(range(len(gates[0])))
    for index in word:
        answer = compose(answer, gates[index])
    return answer


def projection(states: list[Word], keep: tuple[int, ...]) -> np.ndarray:
    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for row, state in enumerate(states):
        groups[tuple(state[index] for index in keep)].append(row)
    matrix = np.zeros((len(states), len(states)), dtype=np.float64)
    for rows in groups.values():
        weight = 1.0 / len(rows)
        matrix[np.ix_(rows, rows)] = weight
    return matrix


def heat_bath(states: list[Word], start: int, size: int) -> np.ndarray:
    block = set(range(start, start + size))
    keep = tuple(index for index in range(len(states[0])) if index not in block)
    return projection(states, keep)


def spectral_gap(matrix: np.ndarray) -> float:
    values = np.linalg.eigvalsh(matrix)
    return 1.0 - float(values[-2]) if len(values) > 1 else 1.0


def min_eigenvalue(matrix: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(matrix)[0])


def local_endpoint_audit(n: int) -> dict[str, object]:
    gates = [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]
    fibers: dict[Perm, list[Word]] = defaultdict(list)
    for word in itertools.product(range(len(gates)), repeat=4):
        fibers[evaluate(word, gates)].append(word)
    m_edges = len(gates)
    delta = 2.0 / (3.0 * m_edges ** 7)
    rows = []
    for endpoint, states in sorted(fibers.items()):
        kernels = [heat_bath(states, start, 2) for start in range(3)]
        local = sum(kernels) / 3.0
        whole = projection(states, ())
        gap = spectral_gap(local)
        comparison_min = min_eigenvalue(
            np.eye(len(states)) - local - delta * (np.eye(len(states)) - whole)
        )
        assert gap + 2e-12 >= delta
        assert comparison_min >= -2e-12
        rows.append({
            "endpoint": list(endpoint),
            "states": len(states),
            "gap": gap,
            "delta_bound": delta,
            "gap_over_bound": gap / delta,
            "min_eigenvalue_Dlocal_minus_delta_Dwhole": comparison_min,
        })
    return {
        "N": n,
        "M": m_edges,
        "endpoints": len(fibers),
        "total_words": sum(len(states) for states in fibers.values()),
        "minimum_gap": min(row["gap"] for row in rows),
        "minimum_gap_over_bound": min(row["gap_over_bound"] for row in rows),
        "minimum_psd_margin": min(
            row["min_eigenvalue_Dlocal_minus_delta_Dwhole"] for row in rows
        ),
        "fibers": rows,
    }


def global_audit(n: int, ell: int) -> dict[str, object]:
    gates = [transposition(n, x, y) for x in range(n) for y in range(x + 1, n)]
    length = 2 * ell
    identity = tuple(range(n))
    states = [
        word
        for word in itertools.product(range(len(gates)), repeat=length)
        if evaluate(word, gates) == identity
    ]
    dimension = len(states)
    pair = [heat_bath(states, start, 2) for start in range(length - 1)]
    aligned = [heat_bath(states, 2 * index, 4) for index in range(ell - 1)]
    complete = []
    for left in range(ell):
        for right in range(left + 1, ell):
            removed = {2 * left, 2 * left + 1, 2 * right, 2 * right + 1}
            keep = tuple(index for index in range(length) if index not in removed)
            complete.append(projection(states, keep))
    identity_matrix = np.eye(dimension)
    j_chain = 0.5 * identity_matrix + sum(pair) / (2.0 * (length - 1))
    b_chain = sum(aligned) / (ell - 1)
    c_chain = sum(complete) / math.comb(ell, 2)
    m_edges = len(gates)
    delta = 2.0 / (3.0 * m_edges ** 7)
    j_to_b = 3.0 * delta * (ell - 1) / (4.0 * (2 * ell - 1))
    sharp_j_to_c = (ell - 1) / (
        4.0 * m_edges ** 7 * ell ** 2 * (2 * ell - 1)
    )
    coarse_j_to_c = 1.0 / (12.0 * m_edges ** 7 * ell ** 2)
    d_j = identity_matrix - j_chain
    d_b = identity_matrix - b_chain
    d_c = identity_matrix - c_chain
    margins = {
        "J_minus_sharp_B": min_eigenvalue(d_j - j_to_b * d_b),
        "B_minus_C_over_2ell2": min_eigenvalue(d_b - d_c / (2 * ell ** 2)),
        "J_minus_sharp_C": min_eigenvalue(d_j - sharp_j_to_c * d_c),
        "J_minus_coarse_C": min_eigenvalue(d_j - coarse_j_to_c * d_c),
    }
    assert min(margins.values()) >= -3e-12
    return {
        "N": n,
        "M": m_edges,
        "ell": ell,
        "raw_length": length,
        "endpoint": "identity",
        "states": dimension,
        "gaps": {
            "J_lazy": spectral_gap(j_chain),
            "B_nonlazy": spectral_gap(b_chain),
            "C_nonlazy": spectral_gap(c_chain),
        },
        "constants": {
            "delta_4": delta,
            "J_to_B": j_to_b,
            "sharp_J_to_C": sharp_j_to_c,
            "coarse_J_to_C": coarse_j_to_c,
        },
        "minimum_psd_margins": margins,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "deterministic_finite_matrix_falsification_only",
        "claim": "M108 local four-letter gap and J-to-C Dirichlet comparisons",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "local_all_endpoint_checks": [local_endpoint_audit(n) for n in (3, 4)],
        "global_identity_checks": [global_audit(3, 3), global_audit(4, 2)],
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "command": " ".join(sys.argv),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    compact = {
        "local": [
            {key: value for key, value in row.items() if key != "fibers"}
            for row in payload["local_all_endpoint_checks"]
        ],
        "global": payload["global_identity_checks"],
    }
    print(json.dumps(compact, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
