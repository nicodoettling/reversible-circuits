#!/usr/bin/env python3
"""Exact falsification audit for the genus-one prefix handle time.

This enumerates only d=2,3,4.  Its positive observations are not asymptotic
proofs; universal assertions in the accompanying note have separate algebraic
proofs.
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


def transpositions(d: int):
    return tuple((a, b) for a in range(d) for b in range(a + 1, d))


def compose(p, q):
    """p after q: (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(d: int, e):
    p = list(range(d))
    a, b = e
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate(a, b):
    """bab for involutory transpositions, returned as an edge."""
    x, y = a
    u, v = b
    def act(z):
        return v if z == u else u if z == v else z
    return tuple(sorted((act(x), act(y))))


def right_move(w, i):
    a, b = w[i], w[i + 1]
    return w[:i] + (b, conjugate(a, b)) + w[i + 2 :]


def inverse_move(w, i):
    a, b = w[i], w[i + 1]
    return w[:i] + (conjugate(b, a), a) + w[i + 2 :]


def ncycles(p):
    seen = [False] * len(p)
    ans = 0
    for x in range(len(p)):
        if not seen[x]:
            ans += 1
            y = x
            while not seen[y]:
                seen[y] = True
                y = p[y]
    return ans


def support_components(d: int, edges):
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
    for a, b in edges:
        union(a, b)
    return len({find(x) for x in range(d)})


def eval_word(d: int, w):
    p = tuple(range(d))
    perms = {e: edge_perm(d, e) for e in transpositions(d)}
    for e in w:
        p = compose(p, perms[e])
    return p


def prefix_genera(d: int, w):
    p = tuple(range(d))
    perms = {e: edge_perm(d, e) for e in transpositions(d)}
    ans = [0]
    pref = []
    for j, e in enumerate(w, 1):
        pref.append(e)
        p = compose(p, perms[e])
        c_supp = support_components(d, pref)
        defect = j - (d + ncycles(p) - 2 * c_supp)
        assert defect >= 0 and defect % 2 == 0
        ans.append(defect // 2)
    return ans


def handle_time(d: int, w):
    g = prefix_genera(d, w)
    jumps = [j for j in range(1, len(g)) if g[j] == g[j - 1] + 1]
    assert len(jumps) == 1 and g[-1] == 1
    return jumps[0]


def connected_after_delete(d: int, w, i: int):
    z = w[:i] + w[i + 2 :]
    return eval_word(d, z) == tuple(range(d)) and support_components(d, z) == 1


def marks(d: int, w):
    return tuple(i + 1 for i in range(len(w) - 1)
                 if w[i] == w[i + 1] and connected_after_delete(d, w, i))


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unavailable"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", nargs="+", type=int, default=[2, 3, 4])
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    started = time.time()
    cases = []
    for d in args.d:
        es = transpositions(d)
        ident = tuple(range(d))
        states = []
        for w in itertools.product(es, repeat=2 * d):
            if eval_word(d, w) == ident and support_components(d, w) == 1:
                states.append(w)
        h_hist = Counter()
        pair_hist = Counter()
        mark_hist = Counter()
        transition_by_h = Counter()
        row_signatures = defaultdict(set)
        max_move = 0
        marked_not_bracketing = None
        deletion_multiplicity = Counter()
        for w in states:
            h = handle_time(d, w)
            hr = handle_time(d, tuple(reversed(w)))
            right_handle = 2 * d + 1 - hr
            h_hist[h] += 1
            pair_hist[(h, right_handle)] += 1
            ms = marks(d, w)
            mark_hist[len(ms)] += 1
            if ms:
                deletion_multiplicity[len(ms)] += 1
                if marked_not_bracketing is None:
                    # Test the tempting claim that a safe square must contain
                    # both oriented handle positions.
                    ok = any({p, p + 1} == {h, right_handle} for p in ms)
                    if not ok:
                        marked_not_bracketing = {
                            "word": w, "left_handle": h,
                            "right_handle": right_handle, "marks": ms,
                        }
            sig = Counter()
            for i in range(2 * d - 1):
                for mover in (right_move, inverse_move):
                    v = mover(w, i)
                    hv = handle_time(d, v)
                    max_move = max(max_move, abs(hv - h))
                    sig[hv] += 1
                    transition_by_h[(h, hv)] += 1
            row_signatures[h].add(tuple(sorted(sig.items())))
        cases.append({
            "d": d,
            "candidate_words": len(es) ** (2 * d),
            "states": len(states),
            "handle_histogram": {str(k): v for k, v in sorted(h_hist.items())},
            "oriented_handle_pair_histogram": {
                f"{a},{b}": v for (a, b), v in sorted(pair_hist.items())
            },
            "mark_count_histogram": {
                str(k): v for k, v in sorted(mark_hist.items())
            },
            "max_handle_displacement_one_move": max_move,
            "number_of_distinct_row_signatures_by_handle": {
                str(k): len(v) for k, v in sorted(row_signatures.items())
            },
            "handle_projection_is_strong_lump": all(
                len(v) == 1 for v in row_signatures.values()),
            "first_marked_word_refuting_handle_pair_square": marked_not_bracketing,
        })
    payload = {
        "claim_tested": (
            "Prefix genus has one handle jump, one Hurwitz move moves it at "
            "most one; falsify strong lumping and handle-pair mark shortcuts."
        ),
        "scope_warning": (
            "Exact finite enumeration only. Positive finite behavior is not "
            "evidence for an asymptotic spectral gap."
        ),
        "convention": "(pq)(x)=p(q(x)); factors left-to-right",
        "kernel_proposals": "both signed R_i and R_i^-1; laziness omitted from counts",
        "commit": git_commit(),
        "python": platform.python_version(),
        "seed": None,
        "dependencies": {},
        "arguments": {"d": args.d, "output": str(args.output)},
        "elapsed_seconds": time.time() - started,
        "cases": cases,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "sha256": hashlib.sha256(
        args.output.read_bytes()).hexdigest(), "cases": [c["states"] for c in cases]}))


if __name__ == "__main__":
    main()
