#!/usr/bin/env python3
"""Exact finite falsifier for M29 macro escape and removable-leaf flow.

Named claims tested: (i) every w in F_N has positive one-step probability
under exact full K to leave connected full support; and (ii) the analytic
removable-leaf-union mass/flow formulas agree with all r=3,4,5 contributions
in the calibration cases.  Finite survival proves no universal theorem.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import platform
from fractions import Fraction
from pathlib import Path


REUSED = Path("experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M13-nonnormal-schreier-redteam/exact_cut_check.py")


def load_helpers():
    spec = importlib.util.spec_from_file_location("m13_exact", REUSED)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load exact helper")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def analyze(n: int) -> dict:
    h = load_helpers()
    m = 2 * n - 2
    ident = tuple(range(n))
    edges, gates = h.transpositions(n)
    lengths = tuple(r for r in (3, 4, 5) if r <= m)
    fibers = h.build_fibers(gates, ident, lengths)
    states = [
        w for w in itertools.product(range(len(gates)), repeat=m)
        if h.product(w, gates, ident) == ident and h.connected_on_all(w, edges, n)
    ]
    exits: list[Fraction] = []
    zero_witness = None
    for word in states:
        probability = Fraction(0)
        for r in lengths:
            windows = m - r + 1
            for start in range(windows):
                p = h.product(word[start:start+r], gates, ident)
                fiber = fibers[r][p]
                bad = 0
                for block in fiber:
                    target = word[:start] + block + word[start+r:]
                    if not h.connected_on_all(target, edges, n):
                        bad += 1
                probability += Fraction(bad, 2 * len(lengths) * windows * len(fiber))
        exits.append(probability)
        if probability == 0 and zero_witness is None:
            zero_witness = [edges[i] for i in word]
    histogram = {}
    for value in exits:
        histogram[str(value)] = histogram.get(str(value), 0) + 1
    # Exact full-Omega cut: connected minimal words with at least one
    # removable adjacent leaf square.  This checks overlap accounting and
    # every r=3,4,5 boundary contribution for the analytic union theorem.
    all_identity = [
        w for w in itertools.product(range(len(gates)), repeat=m)
        if h.product(w, gates, ident) == ident
    ]
    mark_counts = {
        w: (
            len(h.removable_leaf_marks(w, edges, n))
            if h.connected_on_all(w, edges, n) else 0
        )
        for w in all_identity
    }
    flags = {w: mark_counts[w] >= 1 for w in all_identity}
    union_cut = h.analyze_cut(
        "at least one removable join-tree leaf square",
        all_identity, flags, fibers, gates, ident, lengths,
    )
    full_hist = {}
    for w in states:
        z = mark_counts[w]
        full_hist[str(z)] = full_hist.get(str(z), 0) + 1
    union_cut["conditional_mark_histogram_on_F"] = full_hist

    return {
        "N": n,
        "m": m,
        "F_size": len(states),
        "minimum_exit_probability": str(min(exits)),
        "maximum_exit_probability": str(max(exits)),
        "zero_exit_state_count": sum(x == 0 for x in exits),
        "zero_exit_witness_edges": zero_witness,
        "exit_probability_histogram": histogram,
        "removable_leaf_union_cut": union_cut,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, choices=(3, 4), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = {
        "purpose": "Finite exact falsifier only; no asymptotic inference.",
        "claims_tested": [
            "Every minimal connected full-support word has positive one-step full-K macro exit.",
            "The removable-leaf-union cut has the stated overlap counts and positive full-K boundary.",
        ],
        "convention": "(pq)(x)=p(q(x)); exact lazy r=3,4,5 heat baths",
        "seed": None,
        "python": platform.python_version(),
        "reused_exact_helper": str(REUSED),
        "result": analyze(args.N),
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
