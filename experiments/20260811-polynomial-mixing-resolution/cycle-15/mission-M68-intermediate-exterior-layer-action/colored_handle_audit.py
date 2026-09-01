#!/usr/bin/env python3
"""Exact bounded audit of the colors-only marked-Hurwitz proposal.

Start from a connected genus-one identity factorization with a marked
deletable surplus square.  Transport only the two branch-point colors under
right/inverse Hurwitz generators.  Search the finite colored orbit for a
state in which the two colors are adjacent but their transposition factors
are unequal.  Such a state proves that positions/colors do not retain the
canceling arc/handle data.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from collections import deque
from pathlib import Path


sys.dont_write_bytecode = True


def edge_list(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def conjugate_edge(a, b, edges, lookup):
    x, y = edges[a]
    p, q = edges[b]

    def act(v):
        if v == p:
            return q
        if v == q:
            return p
        return v

    return lookup[tuple(sorted((act(x), act(y))))]


def move(state, i, sign, edges, lookup):
    a, color_a = state[i]
    b, color_b = state[i + 1]
    out = list(state)
    if sign == 1:
        # R(a,b)=(b,bab).
        out[i] = (b, color_b)
        out[i + 1] = (conjugate_edge(a, b, edges, lookup), color_a)
    else:
        # R^{-1}(a,b)=(aba,a).
        out[i] = (conjugate_edge(b, a, edges, lookup), color_b)
        out[i + 1] = (a, color_a)
    return tuple(out)


def permutation(edge, n):
    p = list(range(n))
    i, j = edge
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def product(indices, edges, n):
    answer = tuple(range(n))
    for index in indices:
        answer = compose(answer, permutation(edges[index], n))
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = 3
    edges = edge_list(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    # (02)^2 is the marked surplus square; deleting it leaves the connected
    # minimal word (01)^2(12)^2 on all three labels.
    indices = (lookup[(0, 2)], lookup[(0, 2)], lookup[(0, 1)],
               lookup[(0, 1)], lookup[(1, 2)], lookup[(1, 2)])
    start = tuple((index, position < 2) for position, index in enumerate(indices))
    queue = deque([start])
    parent = {start: None}
    parent_move = {}
    witness = None
    while queue:
        state = queue.popleft()
        marks = [i for i, (_edge, marked) in enumerate(state) if marked]
        if (
            state != start
            and marks[1] == marks[0] + 1
            and state[marks[0]][0] != state[marks[1]][0]
        ):
            witness = state
            break
        for i in range(len(state) - 1):
            for sign in (-1, 1):
                target = move(state, i, sign, edges, lookup)
                if target not in parent:
                    parent[target] = state
                    parent_move[target] = (i, sign)
                    queue.append(target)
    if witness is None:
        raise AssertionError("finite orbit had no counterexample")
    path = []
    cursor = witness
    while parent[cursor] is not None:
        path.append(parent_move[cursor])
        cursor = parent[cursor]
    path.reverse()
    marked_positions = [i for i, (_edge, marked) in enumerate(witness) if marked]
    remaining = [
        edge_index for i, (edge_index, _marked) in enumerate(witness)
        if i not in marked_positions
    ]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        commit = "unavailable"
    payload = {
        "argv": sys.argv,
        "commit": commit,
        "python": platform.python_version(),
        "seed": None,
        "nonstandard_dependencies": {},
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab); colors swap with branch points",
        "claim_tested": "Transporting only two marked branch-point colors preserves the property that adjacent marks form a canceling equal square.",
        "scope_warning": "One exact orbit witness refutes the colors-only invariant; it does not refute an enriched arc/history state space.",
        "N": n,
        "edges": [list(edge) for edge in edges],
        "start": [[edge, marked] for edge, marked in start],
        "start_product": list(product(indices, edges, n)),
        "start_deleted_product": list(product(indices[2:], edges, n)),
        "orbit_states_discovered_before_witness": len(parent),
        "path_zero_based_generator_and_sign": [[i, sign] for i, sign in path],
        "path_length": len(path),
        "witness": [[edge, marked] for edge, marked in witness],
        "marked_positions_zero_based": marked_positions,
        "marked_edges": [witness[i][0] for i in marked_positions],
        "marked_edges_equal": witness[marked_positions[0]][0] == witness[marked_positions[1]][0],
        "witness_product": list(product([edge for edge, _mark in witness], edges, n)),
        "witness_deleted_product": list(product(remaining, edges, n)),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
