#!/usr/bin/env python3
"""Exact-count / numerical-spectrum falsifier for the CGL correlation operator.

The universal identities proved in the accompanying report do not depend on
this script.  The finite calculation can falsify proposed quantitative bounds
on mu_l, such as mu_l <= 1/(l-1), but cannot prove their asymptotic validity.

The bridge consists of microincrements E=T_N^2, while the computation uses
the exact product multiplicity w(g)=#{x in E:p(x)=g}.  All convolution counts
are Python integers.  Only the final small Gram matrix is diagonalized in
floating point.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.linalg import null_space


Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)


def transpositions(n: int) -> list[Perm]:
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            ans.append(tuple(p))
    return ans


def parity(p: Perm) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def cycle_type(p: Perm) -> tuple[int, ...]:
    seen = [False] * len(p)
    parts = []
    for i in range(len(p)):
        if seen[i]:
            continue
        x = i
        size = 0
        while not seen[x]:
            seen[x] = True
            size += 1
            x = p[x]
        parts.append(size)
    return tuple(sorted(parts, reverse=True))


def setup(n: int):
    ident = tuple(range(n))
    ts = transpositions(n)
    weights: dict[Perm, int] = defaultdict(int)
    for a in ts:
        for b in ts:
            weights[compose(a, b)] += 1
    group = [p for p in itertools.permutations(range(n)) if parity(p) == 0]
    return ident, group, dict(weights)


def convolution_counts(
    ident: Perm, group: list[Perm], weights: dict[Perm, int], maximum: int
) -> list[dict[Perm, int]]:
    counts = [{g: 0 for g in group} for _ in range(maximum + 1)]
    counts[0][ident] = 1
    for r in range(1, maximum + 1):
        current = counts[r]
        previous = counts[r - 1]
        for a, mass in previous.items():
            if not mass:
                continue
            for s, weight in weights.items():
                current[compose(a, s)] += mass * weight
    return counts


def centered_basis(probability: np.ndarray) -> np.ndarray:
    root = np.sqrt(probability)
    # In whitened coordinates the constant vector is sqrt(probability).
    return null_space(root.reshape(1, -1))


def conjugate(x: Perm, h: Perm) -> Perm:
    """Return h^{-1} x h."""
    return compose(inverse(h), compose(x, h))


def scalar_gram(length: int, kappa: complex) -> np.ndarray:
    ans = np.eye(length, dtype=complex)
    for i in range(length):
        for j in range(i + 1, length):
            ans[i, j] = kappa
            ans[j, i] = np.conjugate(kappa)
    return ans / length


def endpoint_mu(
    endpoint: Perm,
    length: int,
    weights: dict[Perm, int],
    counts: list[dict[Perm, int]],
):
    support = list(weights)
    z = counts[length][endpoint]
    if not z:
        return None
    active = []
    marginal_numerators = []
    for g in support:
        completion = counts[length - 1][compose(inverse(g), endpoint)]
        if completion:
            active.append(g)
            marginal_numerators.append(weights[g] * completion)
    assert sum(marginal_numerators) == z
    probability = np.array(marginal_numerators, dtype=float)
    probability /= probability.sum()
    q = len(active)
    forward = np.zeros((q, q), dtype=float)
    for i, g in enumerate(active):
        denominator = counts[length - 1][compose(inverse(g), endpoint)]
        for j, s in enumerate(active):
            residual = compose(inverse(compose(g, s)), endpoint)
            numerator = weights[s] * counts[length - 2][residual]
            forward[i, j] = numerator / denominator
        assert abs(float(forward[i].sum()) - 1.0) < 1e-11
    root = np.sqrt(probability)
    whitened = root[:, None] * forward / root[None, :]
    basis = centered_basis(probability)
    centered_forward = basis.T @ whitened @ basis
    active_index = {g: i for i, g in enumerate(active)}
    theta = np.zeros((q, q), dtype=float)
    for i, g in enumerate(active):
        transformed = conjugate(g, endpoint)
        assert transformed in active_index
        theta[i, active_index[transformed]] = 1.0
    centered_theta = basis.T @ theta @ basis
    block_dimension = length * centered_forward.shape[0]
    gram = np.zeros((block_dimension, block_dimension), dtype=float)
    d = centered_forward.shape[0]
    for i in range(length):
        gram[i * d : (i + 1) * d, i * d : (i + 1) * d] = np.eye(d)
        for j in range(i + 1, length):
            gram[i * d : (i + 1) * d, j * d : (j + 1) * d] = centered_forward
            gram[j * d : (j + 1) * d, i * d : (i + 1) * d] = centered_forward.T
    gram /= length
    eigenvalues = np.linalg.eigvalsh((gram + gram.T) / 2.0)
    kappa_values = np.linalg.eigvals(centered_forward)
    predicted = np.sort(np.concatenate([
        np.linalg.eigvalsh(scalar_gram(length, kappa))
        for kappa in kappa_values
    ]).real)
    scalar_spectrum_error = float(np.max(np.abs(predicted - eigenvalues)))
    product_mu = float(eigenvalues[-1]) if len(eigenvalues) else 0.0
    # Every active product fiber has at least two micro lifts, so the
    # fiber-centered sector contributes the exact eigenvalue 1/length.
    full_mu = max(product_mu, 1.0 / length)
    adjoint_error = float(
        np.max(
            np.abs(
                probability[:, None] * forward
                - (probability[:, None] * forward).T
            )
        )
    )
    cyclic_relation_error = float(
        np.max(np.abs(centered_forward - centered_forward.T @ centered_theta))
    )
    theta_commutator_error = float(
        np.max(np.abs(centered_forward @ centered_theta - centered_theta @ centered_forward))
    )
    normality_error = float(
        np.max(
            np.abs(
                centered_forward @ centered_forward.T
                - centered_forward.T @ centered_forward
            )
        )
    )
    ident = tuple(range(len(endpoint)))
    square_kappa = None
    label_moved_kappa = None
    support_size_kappa = None
    def rayleigh(values: np.ndarray):
        mean = float(probability @ values)
        variance = float(probability @ (values * values)) - mean * mean
        if variance <= 0.0:
            return None
        pair_form = float(np.sum(probability[:, None] * forward * values[:, None] * values[None, :]))
        return (pair_form - mean * mean) / variance
    if endpoint == ident:
        square_probability = weights[ident] * counts[length - 1][ident] / z
        square_pair_probability = (
            weights[ident] ** 2 * counts[length - 2][ident] / z
        )
        if 0.0 < square_probability < 1.0:
            square_kappa = (square_pair_probability - square_probability ** 2) / (
                square_probability * (1.0 - square_probability)
            )
        label_values = np.array([float(g[0] != 0) for g in active])
        label_moved_kappa = rayleigh(label_values)
        support_values = np.array([float(sum(g[i] != i for i in range(len(g)))) for g in active])
        support_size_kappa = rayleigh(support_values)
    return {
        "endpoint": list(endpoint),
        "length": length,
        "cycle_type": list(cycle_type(endpoint)),
        "bridge_microstate_count": z,
        "active_product_count": q,
        "product_gram_dimension": block_dimension,
        "mu_product": product_mu,
        "mu_full": full_mu,
        "one_minus_mu": 1.0 - full_mu,
        "l_times_mu": length * full_mu,
        "forward_kernel_self_adjoint_error": adjoint_error,
        "cyclic_relation_K_eq_Kstar_U_error": cyclic_relation_error,
        "K_U_commutator_error": theta_commutator_error,
        "K_normality_error": normality_error,
        "scalar_block_spectrum_error": scalar_spectrum_error,
        "max_abs_kappa": float(max(abs(x) for x in kappa_values)),
        "identity_square_indicator_kappa": square_kappa,
        "identity_label_moved_kappa": label_moved_kappa,
        "identity_product_support_size_kappa": support_size_kappa,
        "candidate_mu_le_1_over_l_minus_1": (
            full_mu <= 1.0 / (length - 1) + 1e-11
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--l-max", type=int, default=7)
    parser.add_argument("--identity-only", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    ident, group, weights = setup(args.N)
    counts = convolution_counts(ident, group, weights, args.l_max)
    records = []
    endpoints = [ident] if args.identity_only else group
    for length in range(2, args.l_max + 1):
        by_type = {}
        for endpoint in endpoints:
            endpoint_type = cycle_type(endpoint)
            if endpoint_type in by_type:
                continue
            record = endpoint_mu(endpoint, length, weights, counts)
            if record is not None:
                by_type.setdefault(tuple(record["cycle_type"]), record)
        records.extend(by_type.values())
    maxima_by_length = []
    for length in range(2, args.l_max + 1):
        subset = [r for r in records if r["length"] == length]
        if subset:
            maxima_by_length.append({
                "length": length,
                "max_mu": max(r["mu_full"] for r in subset),
                "max_abs_kappa": max(r["max_abs_kappa"] for r in subset),
                "max_l_times_abs_kappa": max(
                    length * r["max_abs_kappa"] for r in subset
                ),
            })
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "N": args.N,
        "l_max": args.l_max,
        "identity_only": args.identity_only,
        "composition": "(pq)(x)=p(q(x)); tuple product left-to-right",
        "claim_falsifiers": [
            "mu_2^*<1",
            "for all l>=3 and endpoints, mu_l<=1/(l-1)",
            "the oriented forward coordinate kernel is always self-adjoint",
        ],
        "scope_warning": (
            "Exact bridge counts with floating diagonalization can falsify "
            "quantitative candidates but cannot prove uniform asymptotics."
        ),
        "increment_product_support_size": len(weights),
        "maxima_by_length": maxima_by_length,
        "records": records,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
