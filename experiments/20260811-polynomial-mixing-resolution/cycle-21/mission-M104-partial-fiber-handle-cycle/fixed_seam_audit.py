#!/usr/bin/env python3
"""Exact finite falsification audit for M104 fixed central-cut fibers.

The universal statements in the accompanying proof note are algebraic.  This
script exhausts only d<=4 and is used to detect missing conditioning, move,
or multiplicity factors.  It does not supply asymptotic gap evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import subprocess
import time
from collections import Counter, defaultdict
from pathlib import Path


def compose(p, q):
    """p q, with (p q)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(d, e):
    a, b = e
    p = list(range(d))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def transpositions(d):
    return tuple((a, b) for a in range(d) for b in range(a + 1, d))


def eval_word(d, word, edge_perms):
    p = tuple(range(d))
    for e in word:
        p = compose(p, edge_perms[e])
    return p


def cycle_blocks(p):
    seen = set()
    out = []
    for x in range(len(p)):
        if x in seen:
            continue
        cyc = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            y = p[y]
        out.append(tuple(sorted(cyc)))
    return tuple(sorted(out))


def support_partition(d, word, edges):
    parent = list(range(d))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for idx in word:
        union(*edges[idx])
    blocks = defaultdict(list)
    for x in range(d):
        blocks[find(x)].append(x)
    return tuple(sorted(tuple(v) for v in blocks.values()))


def genus(d, word, edges, edge_perms):
    p = eval_word(d, word, edge_perms)
    c = len(cycle_blocks(p))
    q = len(support_partition(d, word, edges))
    numerator = len(word) - d - c + 2 * q
    assert numerator % 2 == 0
    return numerator // 2


def central_cuts(d, word, edges, edge_perms):
    return tuple(
        j for j in range(1, 2 * d)
        if genus(d, word[:j], edges, edge_perms) == 0
        and genus(d, word[j:], edges, edge_perms) == 0
    )


def conjugate_edge(e, by, edges):
    a, b = edges[e]
    x, y = edges[by]

    def t(z):
        if z == x:
            return y
        if z == y:
            return x
        return z

    z = tuple(sorted((t(a), t(b))))
    return edges.index(z)


def right_move(word, i, edges):
    a, b = word[i], word[i + 1]
    out = list(word)
    out[i:i + 2] = (b, conjugate_edge(a, b, edges))
    return tuple(out)


def inverse_move(word, i, edges):
    a, b = word[i], word[i + 1]
    out = list(word)
    out[i:i + 2] = (conjugate_edge(b, a, edges), a)
    return tuple(out)


def seam_key(d, word, j, edges, edge_perms):
    return (
        j,
        eval_word(d, word[:j], edge_perms),
        support_partition(d, word[:j], edges),
        support_partition(d, word[j:], edges),
    )


def encode(word, base):
    ans = 0
    for x in word:
        ans = ans * base + x
    return ans


def block_index(partition):
    ans = {}
    for i, block in enumerate(partition):
        for x in block:
            ans[x] = i
    return ans


def incidence_ok(d, p, q_left, q_right):
    li = block_index(q_left)
    ri = block_index(q_right)
    cycles = cycle_blocks(p)
    adjacency = defaultdict(set)
    for cyc in cycles:
        left = (0, li[cyc[0]])
        right = (1, ri[cyc[0]])
        if any(li[x] != left[1] or ri[x] != right[1] for x in cyc):
            return False, "cycle_not_contained"
        adjacency[left].add(right)
        adjacency[right].add(left)
    vertices = [(0, i) for i in range(len(q_left))]
    vertices += [(1, i) for i in range(len(q_right))]
    seen = set()
    stack = [vertices[0]]
    while stack:
        z = stack.pop()
        if z in seen:
            continue
        seen.add(z)
        stack.extend(adjacency[z] - seen)
    if len(seen) != len(vertices):
        return False, "disconnected"
    if len(cycles) != len(vertices):
        return False, "not_unicyclic"
    return True, None


def component_lengths_ok(d, word, p, partition, edges):
    for block in partition:
        bset = set(block)
        actual = sum(set(edges[e]) <= bset for e in word)
        p_block = tuple(p[x] for x in block)
        # Count cycles of p restricted to this invariant block without
        # relabeling.  Every p-cycle is either wholly inside or outside.
        c = sum(set(cyc) <= bset for cyc in cycle_blocks(p))
        expected = len(block) + c - 2
        if actual != expected:
            return False
        if len(block) == 1 and p_block != block:
            return False
    return True


def json_word(word, edges):
    return [list(edges[e]) for e in word]


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def run_case(d):
    edges = transpositions(d)
    edge_perms = tuple(edge_perm(d, e) for e in edges)
    ident = tuple(range(d))
    states = {}
    candidates = len(edges) ** (2 * d)
    for word in itertools.product(range(len(edges)), repeat=2 * d):
        if eval_word(d, word, edge_perms) != ident:
            continue
        if len(support_partition(d, word, edges)) != 1:
            continue
        cuts = central_cuts(d, word, edges, edge_perms)
        assert cuts
        states[word] = cuts

    cells = {}
    internal = Counter()
    seam = Counter()
    incidence_failures = Counter()
    component_length_failures = 0
    additive_side_failures = 0
    lifted_states = 0
    for word, cuts in states.items():
        ell = len(cuts)
        lo, hi = min(cuts), max(cuts)
        for j in cuts:
            lifted_states += 1
            key = seam_key(d, word, j, edges, edge_perms)
            rec = cells.setdefault(key, {
                "count": 0, "left": set(), "right": set(),
                "ells": Counter(), "right_distance": defaultdict(set),
                "left_distance": defaultdict(set), "witness": {},
            })
            lc = encode(word[:j], len(edges))
            rc = encode(word[j:], len(edges))
            r_plus = hi + 1 - j
            r_minus = j - lo + 1
            assert ell == r_plus + r_minus - 1
            rec["count"] += 1
            rec["left"].add(lc)
            rec["right"].add(rc)
            rec["ells"][ell] += 1
            rec["right_distance"][rc].add(r_plus)
            rec["left_distance"][lc].add(r_minus)
            rec["witness"].setdefault(ell, word)

            _, p, ql, qr = key
            ok, why = incidence_ok(d, p, ql, qr)
            if not ok:
                incidence_failures[why] += 1
            if not component_lengths_ok(d, word[:j], p, ql, edges):
                component_length_failures += 1
            pinv = tuple(p.index(x) for x in range(d))
            if not component_lengths_ok(d, word[j:], pinv, qr, edges):
                component_length_failures += 1

            for i in range(2 * d - 1):
                for mover in (right_move, inverse_move):
                    new = mover(word, i, edges)
                    if i != j - 1:
                        internal["proposals"] += 1
                        if new not in states:
                            internal["left_X"] += 1
                            continue
                        if j not in states[new]:
                            internal["lost_admissibility"] += 1
                        if seam_key(d, new, j, edges, edge_perms) != key:
                            internal["changed_key"] += 1
                    else:
                        seam["proposals"] += 1
                        if new == word:
                            seam["self"] += 1
                        elif j not in states[new]:
                            seam["offdiag_lost_admissibility"] += 1
                        elif seam_key(d, new, j, edges, edge_perms) == key:
                            seam["offdiag_same_key"] += 1
                        else:
                            seam["offdiag_changed_key"] += 1

    product_failures = 0
    side_dependence_failures = 0
    max_ell_ratio = 1.0
    tilted_nonproduct = None
    max_cell = 0
    for key, rec in cells.items():
        if rec["count"] != len(rec["left"]) * len(rec["right"]):
            product_failures += 1
        if any(len(v) != 1 for v in rec["right_distance"].values()):
            side_dependence_failures += 1
        if any(len(v) != 1 for v in rec["left_distance"].values()):
            side_dependence_failures += 1
        emin, emax = min(rec["ells"]), max(rec["ells"])
        max_ell_ratio = max(max_ell_ratio, emax / emin)
        max_cell = max(max_cell, rec["count"])
        if tilted_nonproduct is None and emin != emax:
            w0, w1 = rec["witness"][emin], rec["witness"][emax]
            tilted_nonproduct = {
                "j": key[0], "p": list(key[1]),
                "Q_L": [list(x) for x in key[2]],
                "Q_R": [list(x) for x in key[3]],
                "ell_values": [emin, emax],
                "words": [json_word(w0, edges), json_word(w1, edges)],
            }

    extreme = []
    whole = (tuple(range(d)),)
    for e in edges:
        pair = tuple(sorted((e,)))
        # Desired right partition: edge block plus all other isolates.
        qr = tuple(sorted((tuple(sorted(e)),) + tuple(
            (x,) for x in range(d) if x not in e)))
        key = (2 * d - 2, ident, whole, qr)
        rec = cells.get(key)
        extreme.append({
            "edge": list(e),
            "present": rec is not None,
            "cell_size": 0 if rec is None else rec["count"],
            "left_words": 0 if rec is None else len(rec["left"]),
            "right_words": 0 if rec is None else len(rec["right"]),
            "ell_histogram": {} if rec is None else {
                str(k): v for k, v in sorted(rec["ells"].items())
            },
        })

    return {
        "d": d,
        "candidate_words": candidates,
        "connected_genus_one_states": len(states),
        "lifted_states": lifted_states,
        "seam_cells": len(cells),
        "largest_cell": max_cell,
        "product_count_failures": product_failures,
        "one_side_handle_distance_failures": side_dependence_failures,
        "incidence_failures": dict(incidence_failures),
        "component_length_failures": component_length_failures,
        "internal_move_counts": dict(internal),
        "seam_move_counts": dict(seam),
        "maximum_within_cell_ell_ratio": max_ell_ratio,
        "first_cell_where_lift_tilt_is_nonconstant": tilted_nonproduct,
        "p_identity_full_minimal_left_square_right_cells": extreme,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if any(d < 2 or d > 4 for d in args.d):
        raise SystemExit("This finite audit is deliberately restricted to 2<=d<=4")
    started = time.time()
    cases = [run_case(d) for d in args.d]
    payload = {
        "claim_tested": (
            "At a fixed admissible (j,p,Q_L,Q_R), the raw word fiber is a "
            "side product; the lift has only the 1/ell tilt; internal signed "
            "moves preserve the key while nontrivial seam moves do not."
        ),
        "scope_warning": (
            "Exact finite enumeration only for d<=4. Positive observations "
            "are proof calibration, never asymptotic gap evidence."
        ),
        "target": "uniform connected identity words of length 2d, genus one",
        "convention": "(pq)(x)=p(q(x)); tuple factors left-to-right",
        "kernel_proposals": "both signed adjacent Hurwitz orientations; laziness omitted from proposal counts",
        "commit": git_commit(),
        "python": platform.python_version(),
        "dependencies": {},
        "seed": None,
        "arguments": {"d": args.d, "output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "cases": cases,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(json.dumps({"output": str(args.output), "sha256": digest,
                      "states": [c["connected_genus_one_states"] for c in cases],
                      "lifted": [c["lifted_states"] for c in cases]}))


if __name__ == "__main__":
    main()
