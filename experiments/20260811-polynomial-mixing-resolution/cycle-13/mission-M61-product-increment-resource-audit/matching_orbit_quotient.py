#!/usr/bin/env python3
"""Exact-count centralizer quotient for perfect-matching endpoints.

For even l, N=2l and h=(01)(23)..., this constructs the forward product
correlation kernel on functions invariant under C_{S_N}(h). Completion counts
come from exact character sums; only the final small quotient spectrum uses
floating point. It is a finite falsifier, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import platform
from collections import defaultdict
from pathlib import Path

import numpy as np

Perm = tuple[int, ...]


def load_character_module():
    path = Path(__file__).with_name("perfect_matching_square_mode.py")
    spec = importlib.util.spec_from_file_location("matching_character", path)
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


def matching_endpoint(n: int) -> Perm:
    p = list(range(n))
    for i in range(0, n, 2):
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def orbit_key(g: Perm, quotient: str) -> tuple[int, ...]:
    involved = sorted({v // 2 for v in range(len(g)) if g[v] != v})
    if quotient == "centralizer":
        fixed_pairs: list[int] = []
        movable = involved
        target_offset = 0
    elif quotient == "pair-stabilizer":
        fixed_pairs = [0]
        movable = [pair for pair in involved if pair != 0]
        target_offset = 1
    else:
        raise ValueError(quotient)
    domain_pairs = fixed_pairs + movable
    if not domain_pairs:
        return ()
    k = len(movable)
    best = None
    for order in itertools.permutations(range(k)):
        target_pair = {pair: pair for pair in fixed_pairs}
        target_pair.update({movable[i]: target_offset + order[i] for i in range(k)})
        for flips in itertools.product((0, 1), repeat=len(domain_pairs)):
            flip = {domain_pairs[i]: flips[i] for i in range(len(domain_pairs))}

            def phi(v: int) -> int:
                pair, bit = divmod(v, 2)
                return 2 * target_pair[pair] + (bit ^ flip[pair])

            q = [0] * (2 * len(domain_pairs))
            for pair in domain_pairs:
                for bit in (0, 1):
                    v = 2 * pair + bit
                    q[phi(v)] = phi(g[v])
            candidate = tuple(q)
            if best is None or candidate < best:
                best = candidate
    assert best is not None
    return best


def record(length: int, quotient: str) -> dict:
    n = 2 * length
    ident = tuple(range(n))
    h = matching_endpoint(n)
    weights: dict[Perm, int] = defaultdict(int)
    ts = transpositions(n)
    for a in ts:
        for b in ts:
            weights[compose(a, b)] += 1
    support = sorted(weights)
    orbits: dict[tuple[int, ...], list[Perm]] = defaultdict(list)
    for g in support:
        orbits[orbit_key(g, quotient)].append(g)
    keys = sorted(orbits, key=lambda x: (len(x), x))
    key_index = {key: i for i, key in enumerate(keys)}
    orbit_of = {g: key_index[orbit_key(g, quotient)] for g in support}

    shapes = list(CHAR.partitions(n))
    shape_data = [
        (shape, *CHAR.dimension_content(shape))
        for shape in shapes
    ]
    completion_cache: dict[tuple[int, tuple[int, ...]], int] = {}

    def completion(steps: int, ctype: tuple[int, ...]) -> int:
        cache_key = (steps, ctype)
        if cache_key not in completion_cache:
            completion_cache[cache_key] = sum(
                dimension * CHAR.character(shape, ctype) * content ** (2 * steps)
                for shape, dimension, content in shape_data
            )
        return completion_cache[cache_key]

    qdim = len(keys)
    kernel = np.zeros((qdim, qdim), dtype=float)
    stationary_raw = np.zeros(qdim, dtype=float)
    representatives = [orbits[key][0] for key in keys]
    for oi, g in enumerate(representatives):
        g_residual = compose(inverse(g), h)
        denominator = completion(length - 1, cycle_type(g_residual))
        assert denominator > 0
        row_numerators = [0] * qdim
        for s in support:
            residual = compose(inverse(compose(g, s)), h)
            row_numerators[orbit_of[s]] += (
                weights[s] * completion(length - 2, cycle_type(residual))
            )
        assert sum(row_numerators) == denominator
        kernel[oi] = np.array([x / denominator for x in row_numerators])
        stationary_raw[oi] = (
            len(orbits[keys[oi]]) * weights[g] * denominator
        )
    stationary = stationary_raw / stationary_raw.sum()
    root = np.sqrt(stationary)
    whitened = root[:, None] * kernel / root[None, :]
    detailed_balance_error = float(
        np.max(np.abs(stationary[:, None] * kernel - (stationary[:, None] * kernel).T))
    )
    self_adjoint_error = float(np.max(np.abs(whitened - whitened.T)))
    eigenvalues, eigenvectors = np.linalg.eigh((whitened + whitened.T) / 2)
    nonconstant = eigenvalues[:-1]
    gram_candidates = []
    for kappa in nonconstant:
        gram_candidates.extend([
            (1.0 + (length - 1) * kappa) / length,
            (1.0 - kappa) / length,
        ])
    quotient_mu = max([1.0 / length] + gram_candidates)
    leading_vector = eigenvectors[:, -2] / root
    if leading_vector[np.argmax(np.abs(leading_vector))] < 0:
        leading_vector *= -1

    feature_values = {
        "distinguished_pair_moved_count": np.array([
            int(g[0] != 0) + int(g[1] != 1) for g in representatives
        ], dtype=float),
        "distinguished_pair_setwise_preserved": np.array([
            float({g[0], g[1]} == {0, 1}) for g in representatives
        ], dtype=float),
        "distinguished_label_zero_moved": np.array([
            float(g[0] != 0) for g in representatives
        ], dtype=float),
    }
    feature_records = {}
    for name, values in feature_values.items():
        mean = float(stationary @ values)
        centered = values - mean
        variance = float(stationary @ (centered * centered))
        if variance == 0.0:
            continue
        covariance = float(stationary @ (centered * (kernel @ centered)))
        kappa = covariance / variance
        additive = (1.0 + (length - 1) * kappa) / length
        orthogonal = (1.0 - kappa) / length
        leading_covariance = float(stationary @ (centered * leading_vector))
        feature_records[name] = {
            "mean": mean,
            "kappa_rayleigh": kappa,
            "gram_rayleigh_max": max(additive, orthogonal),
            "length_times_gram_rayleigh_max": length * max(additive, orthogonal),
            "absolute_correlation_with_leading_kappa_mode": abs(leading_covariance) / math.sqrt(variance),
        }
    return {
        "N": n,
        "length": length,
        "endpoint_cycle_type": [2] * length,
        "quotient": quotient,
        "product_support_size": len(support),
        "centralizer_orbit_count": qdim,
        "completion_cycle_type_count": len(completion_cache),
        "detailed_balance_error": detailed_balance_error,
        "whitened_self_adjoint_error": self_adjoint_error,
        "quotient_kappa_eigenvalues": [float(x) for x in eigenvalues],
        "leading_nonconstant_kappa": float(eigenvalues[-2]),
        "leading_nonconstant_function_by_orbit": [float(x) for x in leading_vector],
        "feature_rayleigh": feature_records,
        "quotient_mu_lower_bound": float(quotient_mu),
        "length_times_quotient_mu": float(length * quotient_mu),
        "orbits": [
            {
                "index": i,
                "canonical_key": list(key),
                "size": len(orbits[key]),
                "representative": list(representatives[i]),
                "raw_lift_weight": weights[representatives[i]],
            }
            for i, key in enumerate(keys)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lengths", default="4,6,8")
    parser.add_argument(
        "--quotient",
        choices=("centralizer", "pair-stabilizer"),
        default="centralizer",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    lengths = [int(x) for x in args.lengths.split(",") if x]
    assert all(length >= 4 and length % 2 == 0 for length in lengths)
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "claim_falsifier": (
            "If l times the centralizer-invariant quotient mu grows without "
            "bound, then universal product-increment O(1/l) is false."
        ),
        "scope_warning": (
            "The quotient gives a rigorous lower bound after exact counting, "
            "but finite lengths cannot establish an asymptotic trend and it "
            "does not include nontrivial centralizer representations."
        ),
        "quotient": args.quotient,
        "records": [record(length, args.quotient) for length in lengths],
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
