#!/usr/bin/env python3
"""Exact midpoint bridge-endpoint layer masses for the M64 thick shell."""

from __future__ import annotations

import argparse
import json
import math
import platform
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def edges(n):
    return tuple((a, b) for a in range(n) for b in range(a + 1, n))


def append_transposition(p, edge):
    # If p is the current product, p*t swaps the two domain entries.
    a, b = edge
    q = list(p)
    q[a], q[b] = q[b], q[a]
    return tuple(q)


def transposition_length(p):
    n = len(p)
    seen = [False] * n
    cycles = 0
    for start in range(n):
        if seen[start]:
            continue
        cycles += 1
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return n - cycles


def fraction_text(x):
    return f"{x.numerator}/{x.denominator}"


def one_n(n):
    j = n - 1
    identity = tuple(range(n))
    counts = {identity: 1}
    transpositions = edges(n)
    for _ in range(j):
        nxt = defaultdict(int)
        for p, count in counts.items():
            for edge in transpositions:
                nxt[append_transposition(p, edge)] += count
        counts = dict(nxt)
    weights = defaultdict(int)
    for p, count in counts.items():
        weights[transposition_length(p)] += count * count
    denominator = sum(weights.values())
    cumulative = 0
    layers = []
    quartile_candidates = []
    for length in sorted(weights):
        cumulative += weights[length]
        cdf = Fraction(cumulative, denominator)
        layer_ratio = Fraction(weights[length], cumulative)
        entry = {
            "length": length,
            "weight": weights[length],
            "mass": fraction_text(Fraction(weights[length], denominator)),
            "cdf": fraction_text(cdf),
            "layer_over_cdf": fraction_text(layer_ratio),
        }
        layers.append(entry)
        if Fraction(1, 4) <= cdf <= Fraction(1, 2):
            quartile_candidates.append(entry)
    return {
        "N": n,
        "m": 2 * n - 2,
        "midpoint_j": j,
        "reachable_endpoint_count": len(counts),
        "halfword_count": math.comb(n, 2) ** j,
        "bridge_count_from_square_sum": denominator,
        "layers": layers,
        "quartile_candidates": quartile_candidates,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = [one_n(n) for n in range(3, args.max_n + 1)]
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
        "convention": "(pq)(x)=p(q(x)); appending t swaps domain entries of p",
        "claim_tested": "The exact midpoint transposition-length bridge law has a quartile threshold with a polynomially visible boundary layer; failure or a tiny layer would falsify the proposed thick-shell anti-bottleneck route in that bounded N.",
        "scope_warning": "These finite endpoint weights can refute a universal finite-N formulation but cannot prove asymptotic shell expansion.",
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({r["N"]: r["quartile_candidates"] for r in results}, sort_keys=True))


if __name__ == "__main__":
    main()
