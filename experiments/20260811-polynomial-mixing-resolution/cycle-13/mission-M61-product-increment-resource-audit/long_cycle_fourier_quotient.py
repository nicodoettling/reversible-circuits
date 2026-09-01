#!/usr/bin/env python3
"""Exact-count cyclic Fourier reduction for minimal long-cycle endpoints.

Set N=2l+1 and h=(0 1 ... N-1), so the raw 2l-gate bridge is minimal.
The forward product kernel commutes with conjugation by h. This script
constructs all cyclic Fourier blocks using exact character completion counts;
only their final numerical spectra are floating point. Finite lengths are a
falsifier, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import cmath
import importlib.util
import json
import platform
from collections import defaultdict
from pathlib import Path

import numpy as np

Perm = tuple[int, ...]


def load_character_module():
    path = Path(__file__).with_name("perfect_matching_square_mode.py")
    spec = importlib.util.spec_from_file_location("long_cycle_character", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAR = load_character_module()


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(g: Perm, h: Perm) -> Perm:
    return compose(inverse(h), compose(g, h))


def transpositions(n: int) -> list[Perm]:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(tuple(p))
    return out


def cycle_type(p: Perm) -> tuple[int, ...]:
    seen = [False] * len(p)
    parts = []
    for start in range(len(p)):
        if seen[start]:
            continue
        x = start
        size = 0
        while not seen[x]:
            seen[x] = True
            size += 1
            x = p[x]
        parts.append(size)
    return tuple(sorted(parts, reverse=True))


def long_cycle(n: int) -> Perm:
    return tuple((i + 1) % n for i in range(n))


def scalar_gram(length: int, kappa: complex) -> float:
    gram = np.eye(length, dtype=complex)
    for i in range(length):
        for j in range(i + 1, length):
            gram[i, j] = kappa
            gram[j, i] = np.conjugate(kappa)
    return float(np.linalg.eigvalsh(gram / length)[-1])


def record(length: int) -> dict:
    n = 2 * length + 1
    h = long_cycle(n)
    weights: dict[Perm, int] = defaultdict(int)
    fiber_feature_sums: dict[Perm, complex] = defaultdict(complex)
    ts = transpositions(n)
    unit = cmath.exp(2j * cmath.pi / n)
    single_feature = {
        t: sum(unit ** (-(v + t[v])) for v in range(n))
        for t in ts
    }
    for a in ts:
        for b in ts:
            product = compose(a, b)
            weights[product] += 1
            fiber_feature_sums[product] += single_feature[a] + single_feature[b]
    fiber_feature = {
        g: fiber_feature_sums[g] / weights[g] for g in weights
    }
    support = sorted(weights)
    shapes = list(CHAR.partitions(n))
    shape_data = [(shape, *CHAR.dimension_content(shape)) for shape in shapes]
    completion_cache: dict[tuple[int, tuple[int, ...]], int] = {}

    def completion(steps: int, ctype: tuple[int, ...]) -> int:
        key = (steps, ctype)
        if key not in completion_cache:
            completion_cache[key] = sum(
                dimension * CHAR.character(shape, ctype) * content ** (2 * steps)
                for shape, dimension, content in shape_data
            )
        return completion_cache[key]

    denominators = {
        g: completion(length - 1, cycle_type(compose(inverse(g), h)))
        for g in support
    }
    active = sorted(g for g in support if denominators[g] > 0)
    orbit_data: list[list[Perm]] = []
    location: dict[Perm, tuple[int, int]] = {}
    unseen = set(active)
    while unseen:
        rep0 = min(unseen)
        raw_orbit = []
        x = rep0
        while x not in raw_orbit:
            raw_orbit.append(x)
            x = conjugate(x, h)
        assert x == rep0 and n % len(raw_orbit) == 0
        rep = min(raw_orbit)
        shift = raw_orbit.index(rep)
        orbit = raw_orbit[shift:] + raw_orbit[:shift]
        oi = len(orbit_data)
        orbit_data.append(orbit)
        for r, g in enumerate(orbit):
            location[g] = (oi, r)
            unseen.remove(g)

    qdim = len(orbit_data)
    transition_numerators = np.empty((qdim, qdim, n), dtype=object)
    transition_numerators.fill(0)
    stationary_raw = np.zeros(qdim, dtype=float)
    for oi, orbit in enumerate(orbit_data):
        g = orbit[0]
        denominator = denominators[g]
        row_sum = 0
        for s in active:
            residual = compose(inverse(compose(g, s)), h)
            numerator = weights[s] * completion(length - 2, cycle_type(residual))
            if numerator:
                oj, r = location[s]
                transition_numerators[oi, oj, r] += numerator
                row_sum += numerator
        assert row_sum == denominator
        stationary_raw[oi] = len(orbit) * weights[g] * denominator

    stationary = stationary_raw / stationary_raw.sum()
    root = np.sqrt(stationary)
    best_mu = 1.0 / length
    best = None
    maximum_normality_error = 0.0
    maximum_twist_error = 0.0
    block_dimensions = []
    feature_diagnostics = []
    for frequency in range(n):
        zeta = cmath.exp(2j * cmath.pi * frequency / n)
        # An orbit of size d has stabilizer generated by C^d, so the
        # frequency-k character occurs on it exactly when zeta^(k d)=1.
        compatible = [
            i for i, orbit in enumerate(orbit_data)
            if (frequency * len(orbit)) % n == 0
        ]
        block = np.zeros((len(compatible), len(compatible)), dtype=complex)
        for ii, i in enumerate(compatible):
            denominator = denominators[orbit_data[i][0]]
            for jj, j in enumerate(compatible):
                numerator = sum(
                    transition_numerators[i, j, r] * zeta**r
                    for r in range(len(orbit_data[j]))
                )
                block[ii, jj] = numerator / denominator
        block_root = root[compatible]
        whitened = block_root[:, None] * block / block_root[None, :]
        normality = float(np.max(np.abs(whitened @ whitened.conj().T - whitened.conj().T @ whitened)))
        twist = float(np.max(np.abs(whitened - zeta * whitened.conj().T)))
        maximum_normality_error = max(maximum_normality_error, normality)
        maximum_twist_error = max(maximum_twist_error, twist)
        eigenvalues = np.linalg.eigvals(whitened)
        block_dimensions.append(len(eigenvalues))
        if frequency in {0, 2, n - 2}:
            exponent_sign = -1 if frequency == 2 else 1
            features = {}
            if frequency in {2, n - 2}:
                features.update({
                    "moved_support_fourier": np.array([
                    sum(
                        unit ** (exponent_sign * 2 * v)
                        for v in range(n) if orbit_data[i][0][v] != v
                    )
                    for i in compatible
                ], dtype=complex),
                "permutation_matrix_fourier": np.array([
                    sum(
                        unit ** (exponent_sign * (v + orbit_data[i][0][v]))
                        for v in range(n)
                    )
                    for i in compatible
                ], dtype=complex),
                "fiber_averaged_single_transposition_fourier": np.array([
                    fiber_feature[orbit_data[i][0]]
                    if frequency == 2
                    else np.conjugate(fiber_feature[orbit_data[i][0]])
                    for i in compatible
                ], dtype=complex),
                })
            else:
                features["permutation_dirichlet_fourier"] = np.array([
                    sum(
                        unit ** (orbit_data[i][0][v] - v)
                        for v in range(n)
                    )
                    for i in compatible
                ], dtype=complex)
            weights_here = stationary[compatible]
            for name, feature in features.items():
                if frequency == 0:
                    feature = feature - np.sum(weights_here * feature)
                norm2 = float(np.sum(weights_here * np.abs(feature) ** 2))
                if norm2 < 1e-20:
                    continue
                image_feature = block @ feature
                rayleigh = np.sum(
                    weights_here * np.conjugate(feature) * image_feature
                ) / norm2
                residual2 = float(np.sum(
                    weights_here * np.abs(image_feature - rayleigh * feature) ** 2
                )) / norm2
                feature_diagnostics.append({
                    "frequency": frequency,
                    "feature": name,
                    "norm2": norm2,
                    "kappa_real": float(rayleigh.real),
                    "kappa_imag": float(rayleigh.imag),
                    "kappa_abs": float(abs(rayleigh)),
                    "relative_eigen_residual": float(residual2 ** 0.5),
                    "gram_mu_from_rayleigh": scalar_gram(length, rayleigh),
                })
        for kappa in eigenvalues:
            if frequency == 0 and abs(kappa - 1.0) < 1e-8:
                continue
            candidate = scalar_gram(length, complex(kappa))
            if candidate > best_mu:
                best_mu = candidate
                best = {
                    "frequency": frequency,
                    "kappa_real": float(kappa.real),
                    "kappa_imag": float(kappa.imag),
                    "kappa_abs": float(abs(kappa)),
                    "gram_mu": candidate,
                }
    return {
        "N": n,
        "length": length,
        "endpoint_cycle_type": [n],
        "product_support_size": len(support),
        "active_product_count": len(active),
        "cyclic_orbit_count": qdim,
        "orbit_size_histogram": {
            str(size): sum(len(x) == size for x in orbit_data)
            for size in sorted({len(x) for x in orbit_data})
        },
        "completion_cycle_type_count": len(completion_cache),
        "maximum_normality_error": maximum_normality_error,
        "maximum_twist_relation_error": maximum_twist_error,
        "mu_product": best_mu,
        "length_times_mu_product": length * best_mu,
        "best_mode": best,
        "feature_diagnostics": feature_diagnostics,
        "block_dimensions": block_dimensions,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lengths", default="3,4,5,6")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    lengths = [int(x) for x in args.lengths.split(",") if x]
    assert all(length >= 3 for length in lengths)
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "claim_falsifier": (
            "If l times the exact minimal-long-cycle product mu diverges, "
            "then the universal product-increment O(1/l) claim is false."
        ),
        "scope_warning": (
            "Exact integer completion counts with final floating spectra can "
            "falsify a proposed bound at the recorded lengths, but finite "
            "values cannot prove an asymptotic theorem."
        ),
        "records": [record(length) for length in lengths],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
