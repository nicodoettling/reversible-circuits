#!/usr/bin/env python3
"""Bounded N=7 calibration of the M67 exceptional Krylov sectors.

The state enumeration and every heat-bath application are exact combinatorial
operations. Final Rayleigh quotients/eigenvalues use double-precision ARPACK
and are only falsifiers for the universal formulas in the M70 proof.
"""

from __future__ import annotations

import argparse
import cmath
import collections
import json
import platform
import subprocess
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.sparse.linalg import LinearOperator, eigsh


Perm = tuple[int, ...]
Edge = tuple[int, int]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[x]] for x in range(len(p)))


def transpositions(n: int) -> tuple[list[Edge], list[Perm]]:
    edges, gates = [], []
    for a in range(n):
        for b in range(a + 1, n):
            p = list(range(n))
            p[a], p[b] = p[b], p[a]
            edges.append((a, b))
            gates.append(tuple(p))
    return edges, gates


def conjugate_edge(first: Edge, second: Edge) -> Edge:
    a, b = first
    c, d = second

    def s(x: int) -> int:
        return d if x == c else c if x == d else x

    return tuple(sorted((s(a), s(b))))  # type: ignore[return-value]


def long_cycle(n: int) -> Perm:
    return tuple((x + 1) % n for x in range(n))


def evaluate(word: tuple[int, ...], gates: list[Perm], n: int) -> Perm:
    out = tuple(range(n))
    for t in word:
        out = compose(out, gates[t])
    return out


def minimal_words(n: int, edges: list[Edge], gates: list[Perm]) -> list[tuple[int, ...]]:
    edge_index = {e: i for i, e in enumerate(edges)}
    start = tuple(edge_index[(0, j)] for j in range(n - 1, 0, -1))
    endpoint = long_cycle(n)
    assert evaluate(start, gates, n) == endpoint
    queue = collections.deque([start])
    seen = {start}
    while queue:
        word = queue.popleft()
        for i in range(n - 2):
            image = edge_index[conjugate_edge(edges[word[i]], edges[word[i + 1]])]
            changed = list(word)
            changed[i], changed[i + 1] = word[i + 1], image
            target = tuple(changed)
            if target not in seen:
                seen.add(target)
                queue.append(target)
    assert len(seen) == n ** (n - 2)
    return sorted(seen)


class Projection:
    def __init__(self, words: list[tuple[int, ...]], changed: frozenset[int]):
        key_to_group: dict[tuple[int, ...], int] = {}
        gids = np.empty(len(words), dtype=np.int32)
        for row, word in enumerate(words):
            key = tuple(x for i, x in enumerate(word) if i not in changed)
            gid = key_to_group.setdefault(key, len(key_to_group))
            gids[row] = gid
        self.gids = gids
        self.counts = np.bincount(gids).astype(float)
        self.members: list[list[int]] = [[] for _ in self.counts]
        for row, gid in enumerate(gids):
            self.members[int(gid)].append(row)

    def __call__(self, vector: np.ndarray) -> np.ndarray:
        real = np.bincount(self.gids, weights=vector.real, minlength=len(self.counts))
        imag = np.bincount(self.gids, weights=vector.imag, minlength=len(self.counts))
        means = (real + 1j * imag) / self.counts
        return means[self.gids]


def top_in_krylov(apply, size: int, start: np.ndarray) -> tuple[float, float]:
    op = LinearOperator((size, size), matvec=apply, dtype=np.complex128)
    value, vector = eigsh(op, k=1, which="LA", v0=start, tol=2e-11, maxiter=4000)
    residual = np.linalg.norm(apply(vector[:, 0]) - value[0] * vector[:, 0])
    return float(value[0]), float(residual)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    n, l, m = 7, 3, 6
    edges, gates = transpositions(n)
    words = minimal_words(n, edges, gates)
    size = len(words)

    raw_feature = {}
    omega = cmath.exp(2j * cmath.pi / n)
    for i, t in enumerate(gates):
        raw_feature[i] = sum(omega ** (-(v + t[v])) for v in range(n))
    sums: dict[Perm, complex] = collections.defaultdict(complex)
    counts: dict[Perm, int] = collections.defaultdict(int)
    for i, a in enumerate(gates):
        for j, b in enumerate(gates):
            g = compose(a, b)
            sums[g] += raw_feature[i] + raw_feature[j]
            counts[g] += 1
    product_feature = {g: sums[g] / counts[g] for g in sums}
    F = np.array([
        sum(product_feature[compose(gates[word[2 * i]], gates[word[2 * i + 1]])]
            for i in range(l))
        for word in words
    ], dtype=complex)
    F -= F.mean()

    # Enforce the exact cyclic-conjugation character during floating Lanczos.
    # Without this projection, roundoff at the 1e-16 level eventually leaks
    # into the constant eigenvector and produces a spurious top eigenvalue 1.
    state_index = {word: i for i, word in enumerate(words)}
    edge_index = {edge: i for i, edge in enumerate(edges)}
    conjugation_index = np.empty(size, dtype=np.int32)
    for row, word in enumerate(words):
        conjugated = []
        for t in word:
            a, b = edges[t]
            image = tuple(sorted(((a - 1) % n, (b - 1) % n)))
            conjugated.append(edge_index[image])
        conjugation_index[row] = state_index[tuple(conjugated)]

    def character_projection(vector: np.ndarray, character: complex) -> np.ndarray:
        answer = np.zeros_like(vector)
        shifted = vector
        for k in range(n):
            answer += character ** (-k) * shifted
            shifted = shifted[conjugation_index]
        return answer / n

    candidates = (omega**2, omega**-2)
    character = max(candidates, key=lambda z: np.linalg.norm(character_projection(F, z)))
    F_projected = character_projection(F, character)
    frequency_residual = np.linalg.norm(F - F_projected) / np.linalg.norm(F)
    F = F_projected

    pair_projections = {}
    for i in range(l):
        for j in range(i + 1, l):
            changed = frozenset((2 * i, 2 * i + 1, 2 * j, 2 * j + 1))
            pair_projections[(i, j)] = Projection(words, changed)
    raw_pair_projections = [
        Projection(words, frozenset((i, i + 1))) for i in range(m - 1)
    ]
    window_projections = {
        (r, i): Projection(words, frozenset(range(i, i + r)))
        for r in (3, 4, 5) for i in range(m - r + 1)
    }

    # Exact bounded check of the convention-sensitive full twist.
    def hurwitz(word: tuple[int, ...], i: int) -> tuple[int, ...]:
        changed = list(word)
        changed[i] = word[i + 1]
        changed[i + 1] = edge_index[
            conjugate_edge(edges[word[i]], edges[word[i + 1]])
        ]
        return tuple(changed)

    def delta(word: tuple[int, ...]) -> tuple[int, ...]:
        for i in range(m - 1):
            word = hurwitz(word, i)
        return word

    for row, word in enumerate(words):
        twisted = word
        for _ in range(m):
            twisted = delta(twisted)
        if state_index[twisted] != conjugation_index[row]:
            raise AssertionError("full twist disagrees with h^-1 conjugation")

    # Exact bounded falsifier for the full-state (not fixed-multiset) padding
    # comparison.  Check every directed raw-pair edge and retain the minimum
    # exact ratio B(x,y)/(M^-4 L(x,y)), using one selected aligned window.
    M = len(edges)
    minimum_padding_ratio: Fraction | None = None
    checked_directed_edges = 0
    for row in range(size):
        for i, raw_projection in enumerate(raw_pair_projections):
            raw_gid = int(raw_projection.gids[row])
            raw_count = int(raw_projection.counts[raw_gid])
            aligned_start = i if i % 2 == 0 and i <= m - 4 else i - 1 if i % 2 else m - 4
            aligned = window_projections[(4, aligned_start)]
            aligned_gid = int(aligned.gids[row])
            aligned_count = int(aligned.counts[aligned_gid])
            for target in raw_projection.members[raw_gid]:
                if target == row:
                    continue
                checked_directed_edges += 1
                if int(aligned.gids[target]) != aligned_gid:
                    raise AssertionError("raw-pair target absent from padded H4 fiber")
                ratio = Fraction(M**4 * (m - 1) * raw_count, (l - 1) * aligned_count)
                minimum_padding_ratio = ratio if minimum_padding_ratio is None else min(
                    minimum_padding_ratio, ratio
                )
    assert minimum_padding_ratio is not None and minimum_padding_ratio >= 1

    def apply_c(x):
        return sum((p(x) for p in pair_projections.values()), np.zeros_like(x)) / 3

    def apply_b(x):
        return (pair_projections[(0, 1)](x) + pair_projections[(1, 2)](x)) / 2

    def apply_l(x):
        return sum((p(x) for p in raw_pair_projections), np.zeros_like(x)) / 5

    def apply_k(x):
        out = 0.5 * x
        for r in (3, 4, 5):
            scan = sum(
                (window_projections[(r, i)](x) for i in range(m - r + 1)),
                np.zeros_like(x),
            ) / (m - r + 1)
            out += scan / 6
        return out

    norm2 = float(np.vdot(F, F).real)
    records = {}
    for name, apply in (("C", apply_c), ("B", apply_b), ("L", apply_l), ("K_h", apply_k)):
        restricted_apply = lambda x, base=apply: character_projection(
            base(character_projection(x, character)), character
        )
        image = restricted_apply(F)
        rayleigh = float((np.vdot(F, image) / norm2).real)
        top, residual = top_in_krylov(restricted_apply, size, F)
        records[name] = {
            "feature_transition_rayleigh": rayleigh,
            "feature_dirichlet_rayleigh": 1 - rayleigh,
            "krylov_top_transition_eigenvalue": top,
            "krylov_gap": 1 - top,
            "eigensolver_residual": residual,
        }

    payload = {
        "claim_tested": (
            "At N=7, the M67 feature belongs to a nontrivial invariant cyclic sector; "
            "its exact-kernel Krylov closures for C, B, raw adjacent L, and fixed-endpoint "
            "local K_h have positive gaps and respect the M70 scan normalizations."
        ),
        "scope_warning": (
            "Exact finite state/kernel construction plus floating ARPACK can falsify the "
            "sector formulas but cannot prove an asymptotic spectral bound or Terminal B."
        ),
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "endpoint": list(long_cycle(n)),
        "N": n,
        "raw_length": m,
        "pair_length": l,
        "states": size,
        "feature_mean_abs": float(abs(F.mean())),
        "cyclic_character_real": float(character.real),
        "cyclic_character_imag": float(character.imag),
        "feature_frequency_projection_relative_residual": float(frequency_residual),
        "feature_norm2": norm2,
        "full_twist_checked_all_states": True,
        "full_state_padding_directed_edges_checked": checked_directed_edges,
        "minimum_exact_B_over_Mminus4_L_ratio": {
            "numerator": minimum_padding_ratio.numerator,
            "denominator": minimum_padding_ratio.denominator,
            "decimal": float(minimum_padding_ratio),
        },
        "records": records,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": None,
        "deterministic": True,
        "elapsed_seconds": time.perf_counter() - started,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["records"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
