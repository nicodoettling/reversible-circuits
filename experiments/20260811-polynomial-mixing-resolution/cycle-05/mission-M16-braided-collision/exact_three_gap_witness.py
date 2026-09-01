#!/usr/bin/env python3
"""Build and certify an exact Rayleigh witness for the complete three-site gap.

The output tests the universal Caputo input `inf_h gap(C_3(h)) > 1/3`.
It first optimizes numerically over functions of the first group increment,
rounds that vector to integers, and then evaluates its Rayleigh quotient using
only exact integer/Fraction arithmetic under the microfactor multiplicities.
"""

from __future__ import annotations

import argparse
import json
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh

from braided_collision_audit import (
    compose,
    cycles,
    inverse,
    raw_pair_row,
    setup,
    stationary_weight,
)
from three_gap_scaling import cycle_type


def endpoint_representative(n, requested_type):
    _ident, _ts, group, _support, _weights, _lifts = setup(n)
    for g in group:
        if cycle_type(g) == requested_type:
            return g
    raise ValueError(f"no endpoint of type {requested_type}")


def group_states(n, endpoint):
    ident, _ts, _group, support, weights, _lifts = setup(n)
    states = []
    for x in support:
        for y in support:
            z = compose(inverse(compose(x, y)), endpoint)
            if z in weights:
                states.append((x, y, z))
    return ident, support, weights, states


def conditional_quadratic_matrix(states, weights, support_index, outside):
    """Matrix B with phi^T B phi = <phi(g1),P_pair phi(g1)>_unnormalized."""
    classes = defaultdict(list)
    for word in states:
        classes[word[outside]].append(word)
    q = len(support_index)
    ans = np.zeros((q, q), dtype=float)
    for words in classes.values():
        mass = sum(stationary_weight(w, weights) for w in words)
        vector = np.zeros(q, dtype=float)
        for w in words:
            vector[support_index[w[0]]] += stationary_weight(w, weights)
        ans += np.outer(vector, vector) / mass
    return ans


def exact_rayleigh(states, weights, coefficients):
    total = sum(stationary_weight(w, weights) for w in states)
    first = sum(stationary_weight(w, weights) * coefficients[w[0]] for w in states)
    second = sum(
        stationary_weight(w, weights) * coefficients[w[0]] ** 2 for w in states
    )
    mean = Fraction(first, total)
    variance = Fraction(second, total) - mean * mean
    projection_forms = []
    # P_12 leaves coordinate 3, P_13 leaves 2, P_23 leaves 1.
    for outside in (2, 1, 0):
        classes = defaultdict(list)
        for w in states:
            classes[w[outside]].append(w)
        raw = Fraction(0)
        for words in classes.values():
            mass = sum(stationary_weight(w, weights) for w in words)
            moment = sum(
                stationary_weight(w, weights) * coefficients[w[0]] for w in words
            )
            raw += Fraction(moment * moment, total * mass)
        projection_forms.append(raw - mean * mean)
    p_form = sum(projection_forms, Fraction(0)) / 3
    gap_rayleigh = Fraction(1) - p_form / variance
    return {
        "total_micro_words_in_group_quotient": total,
        "mean": [mean.numerator, mean.denominator],
        "variance": [variance.numerator, variance.denominator],
        "centered_projection_forms": [
            [x.numerator, x.denominator] for x in projection_forms
        ],
        "markov_rayleigh": [
            (p_form / variance).numerator,
            (p_form / variance).denominator,
        ],
        "gap_rayleigh": [gap_rayleigh.numerator, gap_rayleigh.denominator],
        "gap_rayleigh_decimal": float(gap_rayleigh),
        "strictly_below_one_third": gap_rayleigh < Fraction(1, 3),
    }


def exact_full_rayleigh(states, weights, coefficients):
    total = sum(stationary_weight(w, weights) for w in states)
    first = sum(stationary_weight(w, weights) * coefficients[w] for w in states)
    second = sum(stationary_weight(w, weights) * coefficients[w] ** 2 for w in states)
    mean = Fraction(first, total)
    variance = Fraction(second, total) - mean * mean
    projection_forms = []
    for outside in (2, 1, 0):
        classes = defaultdict(list)
        for w in states:
            classes[w[outside]].append(w)
        raw = Fraction(0)
        for words in classes.values():
            mass = sum(stationary_weight(w, weights) for w in words)
            moment = sum(stationary_weight(w, weights) * coefficients[w] for w in words)
            raw += Fraction(moment * moment, total * mass)
        projection_forms.append(raw - mean * mean)
    p_form = sum(projection_forms, Fraction(0)) / 3
    gap_rayleigh = Fraction(1) - p_form / variance
    return {
        "total_micro_words_in_group_quotient": total,
        "mean": [mean.numerator, mean.denominator],
        "variance": [variance.numerator, variance.denominator],
        "centered_projection_forms": [[x.numerator, x.denominator] for x in projection_forms],
        "markov_rayleigh": [(p_form / variance).numerator, (p_form / variance).denominator],
        "gap_rayleigh": [gap_rayleigh.numerator, gap_rayleigh.denominator],
        "gap_rayleigh_decimal": float(gap_rayleigh),
        "strictly_below_one_third": gap_rayleigh < Fraction(1, 3),
    }


def full_numerical_eigenvector(states, support, weights, ident):
    index = {w: i for i, w in enumerate(states)}
    rows, cols, data = [], [], []
    for i, word in enumerate(states):
        accum = defaultdict(float)
        for pair in ((0, 1), (0, 2), (1, 2)):
            for out, probability in raw_pair_row(word, pair, support, weights, ident).items():
                accum[index[out]] += float(probability) / 3.0
        for j, probability in accum.items():
            rows.append(i)
            cols.append(j)
            data.append(probability)
    kernel = coo_matrix((data, (rows, cols)), shape=(len(states), len(states))).tocsr()
    stat = np.array([stationary_weight(w, weights) for w in states], dtype=float)
    stat /= stat.sum()
    root = np.sqrt(stat)
    sym = diags(root) @ kernel @ diags(1.0 / root)
    vals, vecs = eigsh((sym + sym.T) * 0.5, k=3, which="LA")
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]
    f = vecs[:, -2] / root
    f /= np.max(np.abs(f))
    return float(vals[-2]), f


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=6)
    parser.add_argument("--endpoint-type", default="2,2,1,1")
    parser.add_argument("--round-scale", type=int, default=1_000_000)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    requested_type = tuple(int(x) for x in args.endpoint_type.split(","))
    endpoint = endpoint_representative(args.N, requested_type)
    _ident, support, weights, states = group_states(args.N, endpoint)
    index = {g: i for i, g in enumerate(support)}
    total = float(sum(stationary_weight(w, weights) for w in states))
    marginal = np.zeros(len(support), dtype=float)
    for w in states:
        marginal[index[w[0]]] += stationary_weight(w, weights)
    # Unnormalized quadratic form for the average of the three projections.
    b = np.diag(marginal)
    b += conditional_quadratic_matrix(states, weights, index, 2)
    b += conditional_quadratic_matrix(states, weights, index, 1)
    b /= 3.0
    droot_inv = np.diag(1.0 / np.sqrt(marginal))
    sym = droot_inv @ b @ droot_inv
    vals, vecs = eigh((sym + sym.T) / 2.0)
    # The top eigenvector is constant.  Use the second eigenvector and convert
    # back from the whitened coordinates to values phi(g).
    phi = droot_inv @ vecs[:, -2]
    phi /= np.max(np.abs(phi))
    integer_values = np.rint(args.round_scale * phi).astype(np.int64)
    coefficients = {g: int(integer_values[index[g]]) for g in support}
    exact = exact_rayleigh(states, weights, coefficients)

    lambda2_full, full_phi = full_numerical_eigenvector(
        states, support, weights, _ident
    )
    full_integer_values = np.rint(args.round_scale * full_phi).astype(np.int64)
    full_coefficients = {
        w: int(full_integer_values[i]) for i, w in enumerate(states)
    }
    full_exact = exact_full_rayleigh(states, weights, full_coefficients)

    payload = {
        "status": "complete",
        "deterministic": True,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "claim_tested": "inf over feasible endpoints of gap((P12+P13+P23)/3) > 1/3",
        "composition": "(pq)(x)=p(q(x))",
        "N": args.N,
        "endpoint_cycle_type": list(requested_type),
        "endpoint_cycles": cycles(endpoint),
        "endpoint_tuple": list(endpoint),
        "group_state_count": len(states),
        "support_size": len(support),
        "rounded_single_coordinate_test": True,
        "round_scale": args.round_scale,
        "numerical_restricted_lambda": float(vals[-2]),
        "numerical_restricted_gap": float(1.0 - vals[-2]),
        "exact_certificate": exact,
        "numerical_full_lambda2": lambda2_full,
        "numerical_full_gap": 1.0 - lambda2_full,
        "exact_full_certificate": full_exact,
        "support_order": [list(g) for g in support],
        "single_coordinate_integer_vector_in_support_order": integer_values.tolist(),
        "full_state_order": (
            "lexicographic x,y in support_order; z=(xy)^(-1)h; retain iff z is in support"
        ),
        "full_integer_coefficient_vector_in_state_order": full_integer_values.tolist(),
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        k: v for k, v in payload.items()
        if k not in (
            "support_order",
            "single_coordinate_integer_vector_in_support_order",
            "full_integer_coefficient_vector_in_state_order",
        )
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
