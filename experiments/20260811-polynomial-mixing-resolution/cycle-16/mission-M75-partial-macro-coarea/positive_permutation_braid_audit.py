#!/usr/bin/env python3
"""Exact audit of a state-independent positive-permutation-braid cover.

For every connected genus-one identity word in S_3 at length six, apply the
canonical positive permutation braid associated with every permutation of
the six initial branch-point labels.  Test whether the endpoint contains an
adjacent equal square whose deletion leaves connected support.

The positive lift is defined by moving the requested label order into place
using adjacent right-Hurwitz generators R(a,b)=(b,bab).  Matsumoto's braid
relations make the endpoint independent of the chosen reduced sorting word;
the deterministic bubble implementation fixes one auditable representative.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


sys.dont_write_bytecode = True


def edge_list(n: int):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def perm(edge, n: int):
    out = list(range(n))
    i, j = edge
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def product(word, edge_perms, n: int):
    out = tuple(range(n))
    for e in word:
        out = compose(out, edge_perms[e])
    return out


def conjugate_edge(a: int, b: int, edges, lookup):
    x, y = edges[a]
    p, q = edges[b]

    def act(v):
        if v == p:
            return q
        if v == q:
            return p
        return v

    return lookup[tuple(sorted((act(x), act(y))))]


def right_hurwitz(word, i: int, edges, lookup):
    a, b = word[i], word[i + 1]
    out = list(word)
    out[i] = b
    out[i + 1] = conjugate_edge(a, b, edges, lookup)
    return tuple(out)


def positive_lift(word, target_order, edges, lookup):
    labels = list(range(len(word)))
    out = tuple(word)
    move_count = 0
    for destination, wanted in enumerate(target_order):
        position = labels.index(wanted, destination)
        while position > destination:
            out = right_hurwitz(out, position - 1, edges, lookup)
            labels[position - 1], labels[position] = labels[position], labels[position - 1]
            position -= 1
            move_count += 1
    assert tuple(labels) == tuple(target_order)
    return out, move_count


def connected_support(word, edges, n: int):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for e in word:
        a, b = edges[e]
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    return len({find(v) for v in range(n)}) == 1


def marked(word, edges, n: int):
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continue
        core = word[:i] + word[i + 2 :]
        if connected_support(core, edges, n):
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    n = 3
    k = 6
    edges = edge_list(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    edge_perms = tuple(perm(edge, n) for edge in edges)
    identity = tuple(range(n))
    words = [
        word
        for word in itertools.product(range(len(edges)), repeat=k)
        if product(word, edge_perms, n) == identity
        and connected_support(word, edges, n)
    ]
    orders = tuple(itertools.permutations(range(k)))
    hit_histogram = Counter()
    minimum_hits = len(orders) + 1
    minimum_words = []
    endpoint_checks = 0
    max_move_count = 0
    for word in words:
        hits = 0
        for order in orders:
            endpoint, move_count = positive_lift(word, order, edges, lookup)
            max_move_count = max(max_move_count, move_count)
            assert product(endpoint, edge_perms, n) == identity
            hits += int(marked(endpoint, edges, n))
            endpoint_checks += 1
        hit_histogram[hits] += 1
        if hits < minimum_hits:
            minimum_hits = hits
            minimum_words = [word]
        elif hits == minimum_hits and len(minimum_words) < 20:
            minimum_words.append(word)
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
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab); canonical positive permutation braid",
        "claim_tested": "Every connected genus-one S_3 length-six identity word has inverse-polynomial marked endpoint probability under a uniform positive permutation braid.",
        "scope_warning": "A finite S_3 result can refute this named universal statement if the minimum is zero, but positive survival cannot prove an asymptotic cover.",
        "N": n,
        "component_length": k,
        "edge_order": [list(edge) for edge in edges],
        "connected_identity_word_count": len(words),
        "permutation_count": len(orders),
        "endpoint_checks": endpoint_checks,
        "maximum_positive_braid_length": max_move_count,
        "minimum_marked_endpoint_count": minimum_hits,
        "minimum_marked_endpoint_probability": [minimum_hits, len(orders)],
        "minimum_words_edge_indices": [list(word) for word in minimum_words],
        "hit_count_histogram": {str(key): value for key, value in sorted(hit_histogram.items())},
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
