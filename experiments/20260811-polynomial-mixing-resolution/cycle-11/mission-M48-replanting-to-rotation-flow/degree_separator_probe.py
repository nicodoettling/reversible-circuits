#!/usr/bin/env python3
"""Exact bounded falsifier for the reversible-pebble separator theorem."""

from __future__ import annotations

import argparse
import collections
import json
import math
from fractions import Fraction

from rotation_replant_probe import (
    Tree,
    rotations,
    size,
    trees,
    weight_denominator,
)


def maximum_degree(t: Tree) -> int:
    return max([len(t)] + [maximum_degree(child) for child in t])


def root_prefix_set(t: Tree) -> frozenset[int]:
    total = 0
    prefixes = []
    for child in t[:-1]:
        total += 1 + size(child)
        prefixes.append(total)
    return frozenset(prefixes)


def pebble_component(n: int, cap: int, start: frozenset[int]):
    seen = {start}
    queue = collections.deque([start])
    while queue:
        state = queue.popleft()
        for i in range(1, n + 1):
            if i != 1 and i - 1 not in state:
                continue
            target = state ^ {i}
            target = frozenset(target)
            if len(target) <= cap and target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def connected_under_degree(source, target, adjacency, degree, bound):
    if degree[source] > bound or degree[target] > bound:
        return False
    seen = {source}
    queue = collections.deque([source])
    while queue:
        x = queue.popleft()
        if x == target:
            return True
        for y in adjacency[x]:
            if degree[y] <= bound and y not in seen:
                seen.add(y)
                queue.append(y)
    return False


def leaf_then_chain(r: int) -> Tree:
    chain: Tree = ()
    for _ in range(r - 2):
        chain = (chain,)
    return ((), chain)


def chain_then_leaf(r: int) -> Tree:
    chain: Tree = ()
    for _ in range(r - 2):
        chain = (chain,)
    return (chain, ())


def frac(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def run(r_max: int):
    records = []
    for r in range(3, r_max + 1):
        states = trees(r)
        adjacency = {t: rotations(t) for t in states}
        degree = {t: maximum_degree(t) for t in states}
        expected = 2 + math.ceil(math.log2(r - 1))
        source, target = leaf_then_chain(r), chain_then_leaf(r)
        minimum_bound = next(
            bound
            for bound in range(1, r + 1)
            if connected_under_degree(source, target, adjacency, degree, bound)
        )

        cap = expected - 2
        c0 = pebble_component(r - 1, cap, frozenset())
        high = {t for t in states if degree[t] >= expected}
        cut = {
            t
            for t in states
            if t not in high and root_prefix_set(t) in c0
        }
        bad_crossings = []
        for x in cut:
            for y in adjacency[x]:
                if y not in cut and y not in high:
                    bad_crossings.append((x, y))

        z = Fraction((r + 1) ** (r - 1), math.factorial(r))
        probability = {
            t: Fraction(1, weight_denominator(t)) / z for t in states
        }
        mass_high = sum((probability[t] for t in high), Fraction())
        mass_cut = sum((probability[t] for t in cut), Fraction())
        records.append(
            {
                "r": r,
                "states": len(states),
                "D": expected,
                "minimum_maximum_degree_between_endpoints": minimum_bound,
                "pebble_cap": cap,
                "empty_and_last_pebble_connected": (
                    frozenset({r - 1}) in c0
                ),
                "bad_low_degree_cut_crossings": len(bad_crossings),
                "mass_high_exact": frac(mass_high),
                "mass_high_float": float(mass_high),
                "mass_cut_exact": frac(mass_cut),
                "mass_cut_float": float(mass_cut),
                "mass_complement_float": float(1 - mass_cut),
            }
        )
    return {
        "claim_tested": (
            "Through r_max, D=2+ceil(log2(r-1)) is the exact minimum "
            "maximum degree for the leaf--chain swap; the root-prefix cut "
            "has no low-degree crossing. Finite success is not a proof."
        ),
        "deterministic": True,
        "seed": None,
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=10)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = run(args.r_max)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result["records"], indent=2))


if __name__ == "__main__":
    main()
