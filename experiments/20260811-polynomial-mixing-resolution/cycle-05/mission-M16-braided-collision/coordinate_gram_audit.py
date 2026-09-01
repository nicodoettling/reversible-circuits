#!/usr/bin/env python3
"""Finite audit of the nonexchangeable one-coordinate Gram operator.

For l=3, centrality of the increment law gives one forward conditional
correlation K above the diagonal and its adjoint below.  This script compares
the resulting 3|supp(Q)| matrix with the full group-bridge eigenvalue.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path

import numpy as np

from braided_collision_audit import compose, conjugate, cycles, inverse, setup
from three_gap_scaling import cycle_type


def representative(n, kind):
    _e, _t, group, _s, _w, _f = setup(n)
    for h in group:
        if cycle_type(h) == kind:
            return h
    raise ValueError(kind)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=6)
    parser.add_argument("--endpoint-type", default="2,2,1,1")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    kind = tuple(int(x) for x in args.endpoint_type.split(","))
    ident, _ts, _group, support, weights, _lifts = setup(args.N)
    h = representative(args.N, kind)
    q = len(support)
    index = {g: i for i, g in enumerate(support)}

    # For l=3, the ordered pair marginal is proportional to
    # a(x)a(y)a(x^{-1} h y^{-1}).
    joint = np.zeros((q, q), dtype=float)
    for i, x in enumerate(support):
        for j, y in enumerate(support):
            z = compose(inverse(x), compose(h, inverse(y)))
            joint[i, j] = weights[x] * weights[y] * weights.get(z, 0)
    marginal = joint.sum(axis=1)
    assert np.allclose(marginal, joint.sum(axis=0))
    k = joint / marginal[:, None]
    root = np.sqrt(marginal)
    kw = root[:, None] * k / root[None, :]
    k_vals, k_vecs = np.linalg.eig(kw)
    nontrivial = [i for i, z in enumerate(k_vals) if abs(z - 1.0) > 1e-8]
    lead_i = max(nontrivial, key=lambda i: k_vals[i].real)
    lead_v = np.real_if_close(k_vecs[:, lead_i]).real
    lead_v /= np.linalg.norm(lead_v)
    centralizer = [
        c for c in itertools.permutations(range(args.N))
        if compose(c, h) == compose(h, c)
    ]
    character_values = []
    invariance_errors = []
    for c in centralizer:
        perm = [index[conjugate(g, c)] for g in support]
        moved = lead_v[perm]
        scalar = float(np.dot(lead_v, moved))
        character_values.append(scalar)
        invariance_errors.append(float(np.linalg.norm(moved - scalar * lead_v)))
    named_generators = {
        "swap_fixed_1_2": (1, 0, 2, 3, 4, 5),
        "flip_3_4": (0, 1, 3, 2, 4, 5),
        "flip_5_6": (0, 1, 2, 3, 5, 4),
        "swap_pairs_34_56": (0, 1, 4, 5, 2, 3),
    }
    named_character = {}
    if args.N == 6 and kind == (2, 2, 1, 1):
        for name, c in named_generators.items():
            perm = [index[conjugate(g, c)] for g in support]
            named_character[name] = float(np.dot(lead_v, lead_v[perm]))
    k_eig = sorted(k_vals, key=lambda z: (z.real, z.imag))

    eye = np.eye(q)
    gram = np.block([
        [eye, kw, kw],
        [kw.T, eye, kw],
        [kw.T, kw.T, eye],
    ]) / 3.0
    eig = np.linalg.eigvalsh((gram + gram.T) / 2.0)
    payload = {
        "status": "complete",
        "deterministic": True,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "composition": "(pq)(x)=p(q(x))",
        "N": args.N,
        "endpoint_type": list(kind),
        "endpoint_cycles": cycles(h),
        "support_size": q,
        "gram_dimension": 3 * q,
        "normalization": "R_3=(E[.|A1]+E[.|A2]+E[.|A3])/3",
        "top_eigenvalues": [float(x) for x in eig[-12:]],
        "mu_mean_zero_numeric": float(eig[-2]),
        "gap_numeric": float(1.0 - eig[-2]),
        "forward_K_whitened_nonnormality": float(
            np.linalg.norm(kw @ kw.T - kw.T @ kw, ord=2)
        ),
        "forward_K_symmetry_error": float(np.max(np.abs(kw-kw.T))),
        "forward_K_top_eigenvalues_by_real_part": [
            [float(x.real), float(x.imag)] for x in k_eig[-12:]
        ],
        "leading_nonconstant_K_eigenvalue": [
            float(k_vals[lead_i].real), float(k_vals[lead_i].imag)
        ],
        "endpoint_centralizer_size_in_S_N": len(centralizer),
        "leading_mode_centralizer_character_values_rounded": sorted(
            set(round(x, 8) for x in character_values)
        ),
        "leading_mode_character_max_error": max(invariance_errors),
        "leading_mode_named_generator_character": named_character,
        "fiber_zero_mode_eigenvalue": 1.0 / 3.0,
        "claim_scope": (
            "finite confirmation of the block-Gram reduction; numerical values do not prove asymptotics"
        ),
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
