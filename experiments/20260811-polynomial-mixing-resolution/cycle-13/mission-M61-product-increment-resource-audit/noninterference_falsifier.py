#!/usr/bin/env python3
"""Exact falsifier for Caputo's disjoint-pair non-interference hypothesis.

The state space is the raw microincrement bridge E^l with E=T_N^2.  For a
coordinate pair b, P_b is the exact heat-bath conditional expectation given
all raw coordinates outside b.  We compare P_b P_c and P_c P_b for disjoint
pairs.  A single rational matrix-entry mismatch disproves commutation; the
finite calculation is not evidence for an asymptotic spectral assertion.
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
Raw = tuple[Perm, Perm]
State = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q, so (pq)(x)=p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def transpositions(n: int) -> list[Perm]:
    out: list[Perm] = []
    for i in range(n):
        for j in range(i + 1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            out.append(tuple(p))
    return out


def product(perms: list[Perm] | tuple[Perm, ...], ident: Perm) -> Perm:
    out = ident
    for p in perms:
        out = compose(out, p)
    return out


def outside_key(x: State, pair: tuple[int, int]) -> tuple[int, ...]:
    pair_set = set(pair)
    return tuple(x[k] for k in range(len(x)) if k not in pair_set)


def buckets(states: list[State], pair: tuple[int, int]):
    out: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for idx, x in enumerate(states):
        out[outside_key(x, pair)].append(idx)
    return out


def first_commutator_witness(
    states: list[State], b: tuple[int, int], c: tuple[int, int]
):
    bb = buckets(states, b)
    cb = buckets(states, c)
    bkeys = [outside_key(x, b) for x in states]
    ckeys = [outside_key(x, c) for x in states]
    intersections: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = defaultdict(int)
    for bk, ck in zip(bkeys, ckeys):
        intersections[(bk, ck)] += 1
    for source in range(len(states)):
        source_bk, source_ck = bkeys[source], ckeys[source]
        for target in range(len(states)):
            target_bk, target_ck = bkeys[target], ckeys[target]
            bc = Fraction(
                intersections[(source_bk, target_ck)],
                len(bb[source_bk]) * len(cb[target_ck]),
            )
            cb_entry = Fraction(
                intersections[(target_bk, source_ck)],
                len(cb[source_ck]) * len(bb[target_bk]),
            )
            if bc != cb_entry:
                return {
                    "source_index": source,
                    "target_index": target,
                    "source": list(states[source]),
                    "target": list(states[target]),
                    "P_b_then_P_c": str(bc),
                    "P_c_then_P_b": str(cb_entry),
                    "difference": str(bc - cb_entry),
                }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=3)
    parser.add_argument("--length", type=int, default=4)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    ident = tuple(range(args.N))
    ts = transpositions(args.N)
    raw: list[Raw] = list(itertools.product(ts, repeat=2))
    raw_products = [compose(a, b) for a, b in raw]
    states = [
        tuple(indices)
        for indices in itertools.product(range(len(raw)), repeat=args.length)
        if product(tuple(raw_products[i] for i in indices), ident) == ident
    ]
    tests = [
        ((0, 1), (2, 3), "separated_complementary_pairs"),
        ((0, 2), (1, 3), "crossing_complementary_pairs"),
    ]
    records = []
    for b, c, label in tests:
        records.append(
            {
                "label": label,
                "b_zero_based": list(b),
                "c_zero_based": list(c),
                "witness": first_commutator_witness(states, b, c),
            }
        )
    payload = {
        "status": "complete",
        "deterministic": True,
        "seed": None,
        "python": platform.python_version(),
        "N": args.N,
        "length": args.length,
        "endpoint": "identity",
        "microincrement_count": len(raw),
        "bridge_state_count": len(states),
        "composition": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "claim_falsified_if_witness": (
            "all disjoint complete-pair bridge heat-bath projections commute"
        ),
        "scope_warning": (
            "An exact witness disproves the non-interference identity needed "
            "by the cited additive-conservation theorem. Absence of a witness "
            "in one finite bridge would prove nothing universally."
        ),
        "raw_microincrements": [
            {"index": i, "first": list(a), "second": list(b), "product": list(raw_products[i])}
            for i, (a, b) in enumerate(raw)
        ],
        "tests": records,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
