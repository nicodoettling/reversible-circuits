#!/usr/bin/env python3
"""Exact weighted product-sector test of disjoint heat-bath commutation.

The raw microincrement product law has integer weight
w(g)=#{(a,b) in T_N^2:ab=g}.  Functions of coordinate products see the
weighted bridge on supp(w)^l.  Noncommutation there is automatically
noncommutation of the raw bridge projections.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

Perm = tuple[int, ...]
State = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def transpositions(n: int) -> list[Perm]:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(tuple(p))
    return out


def tuple_product(xs: tuple[Perm, ...], ident: Perm) -> Perm:
    out = ident
    for x in xs:
        out = compose(out, x)
    return out


def outside_key(x: State, pair: tuple[int, int]) -> tuple[int, ...]:
    p = set(pair)
    return tuple(x[k] for k in range(len(x)) if k not in p)


def build_fibers(states: list[State], state_weights: list[int], pair: tuple[int, int]):
    members: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for i, state in enumerate(states):
        members[outside_key(state, pair)].append(i)
    totals = {
        key: sum(state_weights[i] for i in indices)
        for key, indices in members.items()
    }
    return members, totals


def row(
    source: int,
    pair: tuple[int, int],
    states: list[State],
    weights: list[int],
    members,
    totals,
) -> dict[int, Fraction]:
    key = outside_key(states[source], pair)
    return {i: Fraction(weights[i], totals[key]) for i in members[key]}


def composed_row(
    source: int,
    first: tuple[int, int],
    second: tuple[int, int],
    states: list[State],
    weights: list[int],
    first_data,
    second_data,
) -> dict[int, Fraction]:
    out: dict[int, Fraction] = defaultdict(Fraction)
    for mid, p1 in row(source, first, states, weights, *first_data).items():
        for target, p2 in row(mid, second, states, weights, *second_data).items():
            out[target] += p1 * p2
    return dict(out)


def witness(states, state_weights, b, c):
    bd = build_fibers(states, state_weights, b)
    cd = build_fibers(states, state_weights, c)
    for source in range(len(states)):
        bc = composed_row(source, b, c, states, state_weights, bd, cd)
        cb = composed_row(source, c, b, states, state_weights, cd, bd)
        for target in sorted(set(bc) | set(cb)):
            if bc.get(target, Fraction()) != cb.get(target, Fraction()):
                return {
                    "source_index": source,
                    "target_index": target,
                    "source": list(states[source]),
                    "target": list(states[target]),
                    "P_b_then_P_c": str(bc.get(target, Fraction())),
                    "P_c_then_P_b": str(cb.get(target, Fraction())),
                    "difference": str(bc.get(target, Fraction()) - cb.get(target, Fraction())),
                }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--length", type=int, default=4)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    ident = tuple(range(args.N))
    ws: dict[Perm, int] = defaultdict(int)
    ts = transpositions(args.N)
    for a in ts:
        for b in ts:
            ws[compose(a, b)] += 1
    support = sorted(ws)
    states = [
        tuple(ix)
        for ix in itertools.product(range(len(support)), repeat=args.length)
        if tuple_product(tuple(support[i] for i in ix), ident) == ident
    ]
    state_weights = [
        __import__("math").prod(ws[support[i]] for i in state)
        for state in states
    ]
    tests = []
    for b, c, label in [
        ((0, 1), (2, 3), "separated_complementary_pairs"),
        ((0, 2), (1, 3), "crossing_complementary_pairs"),
    ]:
        tests.append({
            "label": label,
            "b_zero_based": list(b),
            "c_zero_based": list(c),
            "witness": witness(states, state_weights, b, c),
        })
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "N": args.N,
        "length": args.length,
        "endpoint": "identity",
        "support_size": len(support),
        "weighted_product_bridge_state_count": len(states),
        "weighted_raw_bridge_mass": sum(state_weights),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "claim_falsified_if_witness": (
            "all disjoint complete-pair bridge heat-bath projections commute"
        ),
        "scope_warning": (
            "This exact product-sector witness proves failure for the raw bridge, "
            "but says nothing by itself about an asymptotic spectral gap."
        ),
        "support": [
            {"index": i, "permutation": list(g), "raw_lift_weight": ws[g]}
            for i, g in enumerate(support)
        ],
        "tests": tests,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
