#!/usr/bin/env python3
"""Independent finite matrix falsifier for M108.

This script imports no predecessor code.  It enumerates raw transposition
bridges and builds conditional-expectation kernels directly from complement
partitions.  Enumeration is exact; spectral checks use float64 eigensolvers.

Convention: (pq)(x)=p(q(x)); displayed factors multiply left-to-right.
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


def multiply(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[x]] for x in range(len(left)))


def all_transpositions(n: int) -> list[Perm]:
    answer: list[Perm] = []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            answer.append(tuple(p))
    return answer


def product(word: Word, gates: list[Perm]) -> Perm:
    value = tuple(range(len(gates[0])))
    for label in word:
        value = multiply(value, gates[label])
    return value


def bridge_fibers(n: int, length: int) -> tuple[list[Perm], dict[Perm, list[Word]]]:
    gates = all_transpositions(n)
    fibers: dict[Perm, list[Word]] = defaultdict(list)
    for word in itertools.product(range(len(gates)), repeat=length):
        fibers[product(word, gates)].append(word)
    return gates, fibers


def conditional_projection(states: list[Word], refreshed: set[int]) -> np.ndarray:
    outside = tuple(i for i in range(len(states[0])) if i not in refreshed)
    cells: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for row, state in enumerate(states):
        cells[tuple(state[i] for i in outside)].append(row)
    kernel = np.zeros((len(states), len(states)), dtype=float)
    for rows in cells.values():
        kernel[np.ix_(rows, rows)] = 1.0 / len(rows)
    assert np.max(np.abs(kernel.sum(axis=1) - 1.0)) < 1e-13
    assert np.max(np.abs(kernel - kernel.T)) < 1e-13
    assert np.max(np.abs(kernel @ kernel - kernel)) < 2e-13
    return kernel


def hblock(states: list[Word], start: int, width: int) -> np.ndarray:
    return conditional_projection(states, set(range(start, start + width)))


def gap(kernel: np.ndarray) -> float:
    if len(kernel) == 1:
        return 1.0
    eigenvalues = np.linalg.eigvalsh(kernel)
    return 1.0 - float(eigenvalues[-2])


def mineig(form: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(form)[0])


def local_check(n: int) -> dict[str, object]:
    gates, fibers = bridge_fibers(n, 4)
    m_edges = len(gates)
    delta = 2.0 / (3.0 * m_edges**7)
    endpoint_rows: list[dict[str, object]] = []
    for endpoint, states in sorted(fibers.items()):
        scans = [hblock(states, k, 2) for k in range(3)]
        local = sum(scans) / 3.0
        whole = conditional_projection(states, set(range(4)))
        identity = np.eye(len(states))
        local_gap = gap(local)
        margin = mineig((identity - local) - delta * (identity - whole))
        assert local_gap >= delta - 3e-12
        assert margin >= -3e-12
        endpoint_rows.append(
            {
                "endpoint": list(endpoint),
                "states": len(states),
                "gap": local_gap,
                "delta": delta,
                "psd_margin": margin,
            }
        )
    return {
        "N": n,
        "M": m_edges,
        "endpoint_count": len(endpoint_rows),
        "total_words": sum(int(row["states"]) for row in endpoint_rows),
        "minimum_gap": min(float(row["gap"]) for row in endpoint_rows),
        "minimum_psd_margin": min(float(row["psd_margin"]) for row in endpoint_rows),
        "fibers": endpoint_rows,
    }


def global_check(n: int, ell: int) -> dict[str, object]:
    gates, fibers = bridge_fibers(n, 2 * ell)
    identity_endpoint = tuple(range(n))
    states = fibers[identity_endpoint]
    dimension = len(states)
    eye = np.eye(dimension)

    h2 = [hblock(states, k, 2) for k in range(2 * ell - 1)]
    h4 = [hblock(states, 2 * i, 4) for i in range(ell - 1)]
    complete: list[np.ndarray] = []
    for i in range(ell):
        for j in range(i + 1, ell):
            complete.append(
                conditional_projection(
                    states, {2 * i, 2 * i + 1, 2 * j, 2 * j + 1}
                )
            )

    j_kernel = 0.5 * eye + sum(h2) / (2.0 * (2 * ell - 1))
    b_kernel = sum(h4) / (ell - 1)
    c_kernel = sum(complete) / math.comb(ell, 2)
    d_j, d_b, d_c = eye - j_kernel, eye - b_kernel, eye - c_kernel

    m_edges = len(gates)
    delta = 2.0 / (3.0 * m_edges**7)
    j_b = 3.0 * delta * (ell - 1) / (4.0 * (2 * ell - 1))
    b_c = 1.0 / (2.0 * ell**2)
    sharp = (ell - 1) / (4.0 * m_edges**7 * ell**2 * (2 * ell - 1))
    coarse = 1.0 / (12.0 * m_edges**7 * ell**2)
    assert abs(sharp - j_b * b_c) < 1e-20
    margins = {
        "J_ge_sharp_B": mineig(d_j - j_b * d_b),
        "B_ge_C_over_2ell2": mineig(d_b - b_c * d_c),
        "J_ge_sharp_C": mineig(d_j - sharp * d_c),
        "J_ge_coarse_C": mineig(d_j - coarse * d_c),
    }
    assert min(margins.values()) >= -4e-12
    return {
        "N": n,
        "ell": ell,
        "raw_length": 2 * ell,
        "states": dimension,
        "gaps": {"J": gap(j_kernel), "B": gap(b_kernel), "C": gap(c_kernel)},
        "coefficients": {
            "delta_4": delta,
            "J_to_B": j_b,
            "B_to_C": b_c,
            "sharp_J_to_C": sharp,
            "coarse_J_to_C": coarse,
        },
        "psd_margins": margins,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = {
        "status": "deterministic_finite_falsification_only",
        "claim": "independent M111 audit of M108 local and global comparisons",
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "local": [local_check(3), local_check(4)],
        "global": [global_check(3, 3), global_check(4, 2)],
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
    summary = {
        "local": [
            {key: value for key, value in item.items() if key != "fibers"}
            for item in payload["local"]
        ],
        "global": payload["global"],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
