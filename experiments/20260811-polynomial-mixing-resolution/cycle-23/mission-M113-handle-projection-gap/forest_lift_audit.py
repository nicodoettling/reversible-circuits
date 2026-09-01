#!/usr/bin/env python3
"""Falsify or validate a matroid-basis interpretation of the forest lift.

The ground set is the red/blue double cover of K_c.  An admissible size-c set
has each color class acyclic and its uncolored multigraph connected (hence
unicyclic).  If these sets were matroid bases, basis exchange would hold.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
from pathlib import Path


def ground(c):
    return tuple(
        (color, i, j)
        for color in (0, 1)
        for i in range(c)
        for j in range(i + 1, c)
    )


def forest(c, edge_set, color):
    parent = list(range(c))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge_color, i, j in edge_set:
        if edge_color != color:
            continue
        i, j = find(i), find(j)
        if i == j:
            return False
        parent[j] = i
    return True


def connected(c, edge_set):
    adjacency = [set() for _ in range(c)]
    for _, i, j in edge_set:
        adjacency[i].add(j)
        adjacency[j].add(i)
    seen = {0}
    todo = [0]
    while todo:
        x = todo.pop()
        for y in adjacency[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == c


def admissible(c, edge_set):
    return (
        len(edge_set) == c
        and forest(c, edge_set, 0)
        and forest(c, edge_set, 1)
        and connected(c, edge_set)
    )


def encode(base):
    return [["red" if color == 0 else "blue", i, j]
            for color, i, j in sorted(base)]


def run_case(c):
    elements = ground(c)
    bases = tuple(
        frozenset(candidate)
        for candidate in itertools.combinations(elements, c)
        if admissible(c, candidate)
    )
    base_set = set(bases)
    witness = None
    checks = 0
    for first in bases:
        if witness is not None:
            break
        for second in bases:
            first_only = first - second
            second_only = second - first
            for e in first_only:
                checks += 1
                successful = [
                    f for f in second_only
                    if frozenset((first - {e}) | {f}) in base_set
                ]
                if not successful:
                    witness = {
                        "first": encode(first),
                        "second": encode(second),
                        "removed_from_first": encode({e})[0],
                        "all_exchange_candidates": encode(second_only),
                    }
                    break
            if witness is not None:
                break
    return {
        "cycle_atom_count": c,
        "ground_size": len(elements),
        "admissible_size_c_sets": len(bases),
        "basis_exchange_checks_before_stop": checks,
        "basis_exchange_witness": witness,
        "basis_exchange_holds_exhaustively": witness is None,
    }


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if any(c < 2 or c > 5 for c in args.c):
        raise SystemExit("audit restricted to 2 <= c <= 5")
    payload = {
        "claim_scope": (
            "finite exhaustive falsification of the named matroid-basis lift"
        ),
        "git_commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "cases": [run_case(c) for c in args.c],
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
