#!/usr/bin/env python3
"""Finite group-product quotient gaps for the complete three-pair chain.

These computations can falsify a claimed universal >1/3 three-coordinate
threshold but cannot prove such a threshold asymptotically or lower-bound the
full micro chain without the separate label-space decomposition argument.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
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


def cycle_type(p):
    seen = [False] * len(p)
    ans = []
    for i in range(len(p)):
        if seen[i]:
            continue
        length = 0
        j = i
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        ans.append(length)
    return tuple(sorted(ans, reverse=True))


def endpoint_gap(n: int, endpoint=None):
    ident, _ts, group, support, weights, _lifts = setup(n)
    if endpoint is None:
        endpoint = ident
    states = []
    for x in support:
        for y in support:
            z = compose(inverse(compose(x, y)), endpoint)
            if z in weights:
                states.append((x, y, z))
    index = {w: i for i, w in enumerate(states)}
    rows = []
    cols = []
    data = []
    for i, word in enumerate(states):
        accum = {}
        for pair in ((0, 1), (0, 2), (1, 2)):
            for out, probability in raw_pair_row(word, pair, support, weights, ident).items():
                j = index[out]
                accum[j] = accum.get(j, 0.0) + float(probability) / 3.0
        for j, probability in accum.items():
            rows.append(i)
            cols.append(j)
            data.append(probability)
    kernel = coo_matrix((data, (rows, cols)), shape=(len(states), len(states))).tocsr()
    stat = np.array([stationary_weight(w, weights) for w in states], dtype=float)
    stat /= stat.sum()
    root = np.sqrt(stat)
    sym = diags(root) @ kernel @ diags(1.0 / root)
    symmetry_error = float(abs(sym - sym.T).max())
    vals = eigsh((sym + sym.T) * 0.5, k=min(6, len(states) - 1), which="LA", return_eigenvectors=False)
    vals.sort()
    return {
        "N": n,
        "group_size": len(group),
        "support_size": len(support),
        "endpoint_cycles": cycles(endpoint),
        "endpoint_cycle_type": list(cycle_type(endpoint)),
        "group_state_count": len(states),
        "lambda_top": float(vals[-1]),
        "lambda2": float(vals[-2]),
        "group_function_gap": float(1.0 - vals[-2]),
        "symmetry_error": symmetry_error,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-N", type=int, default=6)
    parser.add_argument("--all-endpoint-types", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    records = []
    for n in range(3, args.max_N + 1):
        ident, _ts, group, _support, _weights, _lifts = setup(n)
        if args.all_endpoint_types:
            representatives = {}
            for endpoint in group:
                representatives.setdefault(cycle_type(endpoint), endpoint)
            for endpoint in representatives.values():
                records.append(endpoint_gap(n, endpoint))
        else:
            records.append(endpoint_gap(n, ident))
    payload = {
        "status": "complete",
        "deterministic": True,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "claim_scope": "finite upper-bound/falsification audit for the >1/3 three-coordinate threshold",
        "normalization": "complete heat bath (P_12+P_13+P_23)/3",
        "endpoint": "one representative of every S_N conjugacy type in A_N"
        if args.all_endpoint_types else "identity",
        "records": records,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
