#!/usr/bin/env python3
"""Independent compact falsifier for the frozen M104 fixed-seam claims.

This standard-library script imports no predecessor implementation.  It
exhausts the full d=2,3 genus-one spaces and the decisive d=4 circular cell.
Finite success is calibration, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


def ident(d):
    return tuple(range(d))


def compose(p, q):
    """Return p q under (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(d, e):
    p = list(range(d))
    a, b = e
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edges(d):
    return tuple((a, b) for a in range(d) for b in range(a + 1, d))


def evaluate(d, word):
    p = ident(d)
    for e in word:
        p = compose(p, edge_perm(d, e))
    return p


def cycles(p):
    seen = set()
    ans = []
    for x in range(len(p)):
        if x in seen:
            continue
        block = []
        y = x
        while y not in seen:
            seen.add(y)
            block.append(y)
            y = p[y]
        ans.append(tuple(sorted(block)))
    return tuple(sorted(ans))


def support_partition(d, word):
    parent = list(range(d))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in word:
        x, y = root(a), root(b)
        if x != y:
            parent[y] = x
    out = defaultdict(list)
    for x in range(d):
        out[root(x)].append(x)
    return tuple(sorted(tuple(v) for v in out.values()))


def genus(d, word):
    value = len(word) - d - len(cycles(evaluate(d, word)))
    value += 2 * len(support_partition(d, word))
    assert value % 2 == 0
    return value // 2


def central_cuts(d, word):
    return tuple(j for j in range(1, 2 * d)
                 if genus(d, word[:j]) == 0
                 and genus(d, word[j:]) == 0)


def conjugate(e, by):
    a, b = e
    x, y = by

    def t(z):
        return y if z == x else x if z == y else z

    return tuple(sorted((t(a), t(b))))


def move(word, i, orientation):
    a, b = word[i:i + 2]
    out = list(word)
    if orientation == 1:
        out[i:i + 2] = (b, conjugate(a, b))
    else:
        out[i:i + 2] = (conjugate(b, a), a)
    return tuple(out)


def key(d, word, j):
    return (j, evaluate(d, word[:j]),
            support_partition(d, word[:j]),
            support_partition(d, word[j:]))


def incidence_signature(d, p, q_left, q_right):
    left = {x: i for i, block in enumerate(q_left) for x in block}
    right = {x: i for i, block in enumerate(q_right) for x in block}
    adjacency = defaultdict(set)
    for cyc in cycles(p):
        li, ri = left[cyc[0]], right[cyc[0]]
        assert all(left[x] == li and right[x] == ri for x in cyc)
        adjacency[(0, li)].add((1, ri))
        adjacency[(1, ri)].add((0, li))
    vertices = [(0, i) for i in range(len(q_left))]
    vertices += [(1, i) for i in range(len(q_right))]
    seen, stack = set(), [vertices[0]]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adjacency[x] - seen)
    return {
        "vertices": len(vertices),
        "edges": len(cycles(p)),
        "connected": len(seen) == len(vertices),
        "unicyclic": len(cycles(p)) == len(vertices),
    }


def component_lengths_hold(d, word, p, partition):
    pcycles = cycles(p)
    for block in partition:
        bset = set(block)
        actual = sum(set(e) <= bset for e in word)
        c_block = sum(set(cyc) <= bset for cyc in pcycles)
        if actual != len(block) + c_block - 2:
            return False
    return True


def enumerate_x(d):
    es = edges(d)
    return tuple(w for w in itertools.product(es, repeat=2 * d)
                 if evaluate(d, w) == ident(d)
                 and len(support_partition(d, w)) == 1)


def audit_full(d):
    states = enumerate_x(d)
    cut_map = {w: central_cuts(d, w) for w in states}
    assert all(cut_map.values())
    cells = defaultdict(lambda: {
        "words": [], "left": set(), "right": set(),
        "left_r": defaultdict(set), "right_r": defaultdict(set),
    })
    failures = Counter()
    internal = seam = 0
    integral_checks = 0
    for w, cuts_w in cut_map.items():
        assert cuts_w == tuple(range(min(cuts_w), max(cuts_w) + 1))
        b, h = min(cuts_w), max(cuts_w) + 1
        for j in cuts_w:
            k = key(d, w, j)
            rec = cells[k]
            rec["words"].append(w)
            rec["left"].add(w[:j])
            rec["right"].add(w[j:])
            r_left, r_right = j - b + 1, h - j
            rec["left_r"][w[:j]].add(r_left)
            rec["right_r"][w[j:]].add(r_right)
            ell = len(cuts_w)
            if ell != r_left + r_right - 1:
                failures["ell_sum"] += 1
            if Fraction(1, ell) != Fraction(1, r_left + r_right - 1):
                failures["integral"] += 1
            integral_checks += 1
            _, p, ql, qr = k
            sig = incidence_signature(d, p, ql, qr)
            if not sig["connected"] or not sig["unicyclic"]:
                failures["incidence"] += 1
            if not component_lengths_hold(d, w[:j], p, ql):
                failures["left_component_length"] += 1
            pinv = tuple(p.index(x) for x in range(d))
            if not component_lengths_hold(d, w[j:], pinv, qr):
                failures["right_component_length"] += 1

            for i in range(2 * d - 1):
                for orientation in (1, -1):
                    w2 = move(w, i, orientation)
                    cuts2 = central_cuts(d, w2)
                    if i != j - 1:
                        internal += 1
                        if j not in cuts2 or key(d, w2, j) != k:
                            failures["internal_move"] += 1
                    else:
                        seam += 1
                        if w2 != w and j in cuts2 and key(d, w2, j) == k:
                            failures["nontrivial_seam_same_key"] += 1

    density_min, density_max = None, None
    flow_min, flow_max = None, None
    for rec in cells.values():
        if len(rec["words"]) != len(rec["left"]) * len(rec["right"]):
            failures["cartesian_count"] += 1
        if any(len(vals) != 1 for vals in rec["left_r"].values()):
            failures["left_side_dependence"] += 1
        if any(len(vals) != 1 for vals in rec["right_r"].values()):
            failures["right_side_dependence"] += 1
        csize = len(rec["words"])
        ells = {w: len(cut_map[w]) for w in rec["words"]}
        normalizer = sum((Fraction(1, ell) for ell in ells.values()),
                         Fraction())
        for w, ell in ells.items():
            rho = Fraction(csize, 1) / (normalizer * ell)
            density_min = rho if density_min is None else min(density_min, rho)
            density_max = rho if density_max is None else max(density_max, rho)
            for i in range(2 * d - 1):
                for orientation in (1, -1):
                    w2 = move(w, i, orientation)
                    if w2 == w or w2 not in ells:
                        continue
                    ratio = Fraction(csize, 1) / (
                        normalizer * ell * ells[w2])
                    flow_min = ratio if flow_min is None else min(flow_min, ratio)
                    flow_max = ratio if flow_max is None else max(flow_max, ratio)
    D = 2 * d - 1
    assert density_min >= Fraction(1, D) and density_max <= D
    if flow_min is not None:
        assert flow_min >= Fraction(1, D * D) and flow_max <= D
    assert not failures
    return {
        "d": d,
        "states": len(states),
        "lifted_states": sum(map(len, cut_map.values())),
        "cells": len(cells),
        "integral_checks": integral_checks,
        "internal_proposals": internal,
        "seam_proposals": seam,
        "density_ratio_range": [str(density_min), str(density_max)],
        "flow_ratio_range": [str(flow_min), str(flow_max)],
        "failures": dict(failures),
    }


def audit_d4_circular():
    d, e, j = 4, (0, 1), 6
    zs = tuple(z for z in itertools.product(edges(d), repeat=2 * d - 2)
               if evaluate(d, z) == ident(d)
               and len(support_partition(d, z)) == 1)
    expected_key = (j, ident(d), ((0, 1, 2, 3),),
                    ((0, 1), (2,), (3,)))
    failures = Counter()
    ell_hist = Counter()
    internal = seam = integral_checks = 0
    for z in zs:
        w = z + (e, e)
        cuts = central_cuts(d, w)
        if j not in cuts or key(d, w, j) != expected_key:
            failures["cell_membership"] += 1
            continue
        b, h = min(cuts), max(cuts) + 1
        r_left, r_right = j - b + 1, h - j
        ell_hist[len(cuts)] += 1
        if len(cuts) != r_left + r_right - 1:
            failures["ell_sum"] += 1
        if Fraction(1, len(cuts)) != Fraction(1, r_left + r_right - 1):
            failures["integral"] += 1
        integral_checks += 1
        sig = incidence_signature(d, ident(d), expected_key[2], expected_key[3])
        if not sig["connected"] or not sig["unicyclic"]:
            failures["incidence"] += 1
        for i in range(2 * d - 1):
            for orientation in (1, -1):
                w2 = move(w, i, orientation)
                cuts2 = central_cuts(d, w2)
                if i != j - 1:
                    internal += 1
                    if j not in cuts2 or key(d, w2, j) != expected_key:
                        failures["internal_move"] += 1
                else:
                    seam += 1
                    if w2 != w and j in cuts2 and key(d, w2, j) == expected_key:
                        failures["nontrivial_seam_same_key"] += 1
    assert len(zs) == 2880
    assert not failures
    D = 2 * d - 1
    return {
        "d": 4,
        "cell": "kappa_e with e=(0,1)",
        "left_words": len(zs),
        "right_words": 1,
        "cartesian_cell_size": len(zs),
        "ell_histogram": {str(k): v for k, v in sorted(ell_hist.items())},
        "integral_checks": integral_checks,
        "internal_proposals": internal,
        "seam_proposals": seam,
        "scan_identity": {
            "D": D,
            "active_left_positions": D - 2,
            "held_right_or_seam_positions": 2,
            "P0_weight": str(Fraction(D - 2, D)),
            "identity_weight": str(Fraction(2, D)),
        },
        "failures": dict(failures),
    }


def git_commit():
    return subprocess.check_output(["git", "rev-parse", "HEAD"],
                                   text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.time()
    payload = {
        "claim_tested": (
            "M104 literal fixed-seam product, side handle dependence, "
            "1/ell identity, internal/seam classification, RN bounds, and "
            "the d=4 same-size circular cell"
        ),
        "scope_warning": (
            "Full exact d=2,3 and the decisive d=4 circular cell only; "
            "finite success is not an asymptotic gap proof."
        ),
        "convention": "(pq)(x)=p(q(x)); factors multiply left-to-right",
        "target": "uniform connected identity words of length 2d",
        "commit": git_commit(),
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "full_cases": [audit_full(2), audit_full(3)],
        "d4_circular": audit_d4_circular(),
    }
    payload["elapsed_seconds"] = time.time() - start
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output),
                      "elapsed_seconds": payload["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
