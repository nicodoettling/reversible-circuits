#!/usr/bin/env python3
"""Finite exact audit of M35 moves under left-child/right-sibling encoding.

A plane tree with r edges maps to an ordered binary tree with r nodes by
discarding the plane root and encoding first child as binary left child and
next sibling as binary right child.  This script checks whether each exact
leaf rotation is one ordinary binary-tree rotation and records the smallest
mismatch.  It also checks that the comb--path pair is one ordinary rotation.
Finite enumeration illustrates the exact local identities; the local pointer
calculation in the report supplies the universal statement.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import leaf_chain_bridge_probe as base


def binary_encoding(children):
    def forest(row):
        if not row:
            return None
        first = row[0]
        return (forest(children[first]), forest(row[1:]))

    return forest(children[0])


def rotations(tree):
    """All shapes obtainable by exactly one standard left/right rotation."""
    answer = set()
    if tree is None:
        return answer
    left, right = tree
    # Right rotation: ((A,B),C) -> (A,(B,C)).
    if left is not None:
        a, b = left
        answer.add((a, (b, right)))
    # Left rotation: (A,(B,C)) -> ((A,B),C).
    if right is not None:
        b, c = right
        answer.add(((left, b), c))
    for changed in rotations(left):
        answer.add((changed, right))
    for changed in rotations(right):
        answer.add((left, changed))
    return answer


def run(r):
    states = list(base.degree_vectors(r))
    index = {state: i for i, state in enumerate(states)}
    encodings = [binary_encoding(base.children_from_degrees(state)) for state in states]
    moves = 0
    standard = 0
    first_mismatch = None
    for left, state in enumerate(states):
        children = base.children_from_degrees(state)
        neighbors = rotations(encodings[left])
        for parent, row in enumerate(children):
            for position, leaf in enumerate(row[:-1]):
                if state[leaf] != 0:
                    continue
                target = list(state)
                target[parent] -= 1
                target[leaf] += 1
                right = index[tuple(target)]
                moves += 1
                if encodings[right] in neighbors:
                    standard += 1
                elif first_mismatch is None:
                    next_child = row[position + 1]
                    first_mismatch = {
                        "source": list(state),
                        "target": target,
                        "parent": parent,
                        "leaf": leaf,
                        "next_sibling_root": next_child,
                        "next_sibling_is_leaf": state[next_child] == 0,
                        "source_binary": repr(encodings[left]),
                        "target_binary": repr(encodings[right]),
                    }
    comb = (2,) + (1,) * (r - 2) + (0,)
    path = (1,) * r
    comb_index, path_index = index[comb], index[path]
    return {
        "r": r,
        "states": len(states),
        "leaf_rotation_moves": moves,
        "moves_that_are_one_standard_binary_rotation": standard,
        "first_mismatch": first_mismatch,
        "comb_path_are_one_standard_rotation": encodings[path_index] in rotations(encodings[comb_index]),
        "comb": list(comb),
        "path": list(path),
        "scope": "finite exact falsifier; universal pointer identity is separate",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-min", type=int, default=2)
    parser.add_argument("--r-max", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [run(r) for r in range(args.r_min, args.r_max + 1)]
    args.output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
