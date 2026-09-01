#!/usr/bin/env python3
"""Finite exact comb-to-path max-flow audit in the leaf-rotation graph.

The comb C=(2,1,...,1,0) and path P=(1,...,1) are one leaf-replanting
move apart.  Leaf-rotation edge capacities are stored without their common
factor 2/[3*r*(r-1)*(r+1)^(r-1)].  An asymptotically tiny C--P min cut would
obstruct a polynomial comparison for this Y-edge.  Finite output is only a
falsifier and does not establish an asymptotic cut.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import maximum_flow

import leaf_chain_bridge_probe as base


def run(r):
    states = list(base.degree_vectors(r))
    index = {state: i for i, state in enumerate(states)}
    weights = [base.orbit_weight(state) for state in states]
    rows, cols, values = [], [], []
    adjacency = [[] for _ in states]
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
                capacity = weights[left] * state[parent]
                if capacity != weights[right]:
                    raise AssertionError((state, target, capacity, weights[right]))
                rows.extend((left, right))
                cols.extend((right, left))
                values.extend((capacity, capacity))
                adjacency[left].append((right, capacity))
                adjacency[right].append((left, capacity))
    matrix = sp.csr_matrix(
        (np.asarray(values, dtype=np.int64), (rows, cols)),
        shape=(len(states), len(states)),
        dtype=np.int64,
    )
    comb = (2,) + (1,) * (r - 2) + (0,)
    path = (1,) * r
    source, sink = index[comb], index[path]
    result = maximum_flow(matrix, source, sink)

    # Recover the source side of the residual network.  scipy stores a
    # skew-symmetric flow matrix, so residual(u,v)=capacity(u,v)-flow(u,v).
    flow = result.flow.tocsr()
    seen = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        capacity_row = matrix.getrow(u)
        flow_row = flow.getrow(u)
        neighbors = set(capacity_row.indices) | set(flow_row.indices)
        for v in neighbors:
            residual = matrix[u, v] - flow[u, v]
            if residual > 0 and v not in seen:
                seen.add(v)
                queue.append(v)
    cut_capacity = sum(
        capacity
        for u in seen
        for v, capacity in adjacency[u]
        if v not in seen
    )
    if cut_capacity != result.flow_value:
        raise AssertionError((cut_capacity, result.flow_value))
    total = sum(weights)
    side_weight = sum(weights[u] for u in seen)
    common = 2 / (3 * r * (r - 1))
    conductance = common * cut_capacity / min(side_weight, total - side_weight)

    # Effective resistance after scaling every conductance by 1/w(comb).
    # Thus resistance_scaled = w(comb)*R in the unnormalized-capacity
    # network.  Multiplying by the Y-edge demand and restoring the common
    # leaf capacity leaves resistance_scaled/(4*r^2*common), a lower bound
    # on any Dirichlet-form comparison constant for this one commodity.
    scaled = matrix.astype(float) / weights[source]
    degree = np.asarray(scaled.sum(axis=1)).ravel()
    laplacian = sp.diags(degree) - scaled
    keep = np.arange(len(states)) != sink
    grounded = laplacian[keep][:, keep]
    source_grounded = source - (1 if source > sink else 0)
    rhs = np.zeros(len(states) - 1)
    rhs[source_grounded] = 1.0
    voltage, info = spla.cg(grounded, rhs, tol=1e-11, maxiter=200_000)
    if info != 0:
        raise AssertionError(("cg", r, info))
    resistance_scaled = float(voltage[source_grounded])
    single_commodity_comparison_lb = resistance_scaled / (4 * r * r * common)
    return {
        "r": r,
        "states": len(states),
        "comb_weight": weights[source],
        "path_weight": weights[sink],
        "maxflow_capacity_numerator": int(result.flow_value),
        "maxflow_over_comb_weight": result.flow_value / weights[source],
        "source_side_states": len(seen),
        "source_side_weight": side_weight,
        "source_side_mass": side_weight / total,
        "mincut_conductance": conductance,
        "effective_resistance_scaled_by_comb_weight": resistance_scaled,
        "single_Y_edge_dirichlet_comparison_lower_bound": single_commodity_comparison_lb,
        "scope": "finite exact max-flow/min-cut falsifier only",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=3)
    parser.add_argument("--r-max", type=int, default=9)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [run(r) for r in range(args.r_min, args.r_max + 1)]
    args.output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
