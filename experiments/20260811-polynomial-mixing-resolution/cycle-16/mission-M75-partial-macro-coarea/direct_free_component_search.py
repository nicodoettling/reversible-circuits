#!/usr/bin/env python3
"""Bounded exact search in the direct-certificate-free Hurwitz subgraph.

Start with the M68 four-label genus-one obstruction and attach adjacent leaf
squares to obtain a connected genus-one word on d labels.  Explore only
Hurwitz neighbors that still lack a connected identity-preserving
two-deletion certificate.  A visited vertex with no neighbor having a
certificate is an exact counterexample to one-Hurwitz domination.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path


sys.dont_write_bytecode = True


def edges_of(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def edge_perm(edge, n):
    out = list(range(n))
    a, b = edge
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def evaluate(word, perms, n):
    out = tuple(range(n))
    for index in word:
        out = compose(out, perms[index])
    return out


def connected_after_deletion(word, skip_i, skip_j, edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for position, index in enumerate(word):
        if position in (skip_i, skip_j):
            continue
        a, b = edges[index]
        x, y = find(a), find(b)
        if x != y:
            parent[y] = x
    return len({find(v) for v in range(n)}) == 1


def direct_certificate(word, perms, edges, n):
    identity = tuple(range(n))
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word)):
            remaining = word[:i] + word[i + 1 : j] + word[j + 1 :]
            if evaluate(remaining, perms, n) != identity:
                continue
            if connected_after_deletion(word, i, j, edges, n):
                return i, j
    return None


def conjugate_edge(a, b, edges, lookup):
    x, y = edges[a]
    p, q = edges[b]

    def act(v):
        if v == p:
            return q
        if v == q:
            return p
        return v

    return lookup[tuple(sorted((act(x), act(y))))]


def hurwitz(word, i, sign, edges, lookup):
    a, b = word[i], word[i + 1]
    out = list(word)
    if sign == 1:
        out[i] = b
        out[i + 1] = conjugate_edge(a, b, edges, lookup)
    else:
        out[i] = conjugate_edge(b, a, edges, lookup)
        out[i + 1] = a
    return tuple(out)


def initial_word(n, lookup):
    if n < 4:
        raise ValueError("n must be at least four")
    # M68 obstruction on labels 0,1,2,3.
    word = [
        lookup[(0, 1)], lookup[(0, 2)], lookup[(0, 3)], lookup[(0, 2)],
        lookup[(0, 1)], lookup[(0, 2)], lookup[(0, 3)], lookup[(0, 2)],
    ]
    # Attach each further label as an adjacent leaf square.
    for v in range(4, n):
        edge = lookup[(v - 1, v)]
        word.extend((edge, edge))
    return tuple(word)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=5)
    parser.add_argument("--max-states", type=int, default=200000)
    parser.add_argument("--stop-on-counterexample", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    n = args.N
    edges = edges_of(n)
    lookup = {edge: i for i, edge in enumerate(edges)}
    perms = tuple(edge_perm(edge, n) for edge in edges)
    identity = tuple(range(n))
    start = initial_word(n, lookup)
    assert evaluate(start, perms, n) == identity
    assert direct_certificate(start, perms, edges, n) is None
    queue = deque([start])
    distance = {start: 0}
    parent = {start: None}
    parent_move = {}
    direct_neighbor_histogram = Counter()
    free_adjacency = {}
    boundary_free_states = []
    max_distance = 0
    counterexample = None
    complete = True
    stopped_early = False
    while queue:
        word = queue.popleft()
        max_distance = max(max_distance, distance[word])
        direct_neighbors = 0
        free_neighbors = []
        seen_targets = set()
        for i in range(len(word) - 1):
            for sign in (-1, 1):
                target = hurwitz(word, i, sign, edges, lookup)
                if target in seen_targets:
                    continue
                seen_targets.add(target)
                certificate = direct_certificate(target, perms, edges, n)
                if certificate is not None:
                    direct_neighbors += 1
                else:
                    free_neighbors.append((target, i, sign))
        direct_neighbor_histogram[direct_neighbors] += 1
        free_adjacency[word] = tuple(target for target, _i, _sign in free_neighbors)
        if direct_neighbors:
            boundary_free_states.append(word)
        elif counterexample is None:
            counterexample = word
            if args.stop_on_counterexample:
                stopped_early = True
                queue.clear()
                break
        for target, i, sign in free_neighbors:
            if target in distance:
                continue
            if len(distance) >= args.max_states:
                complete = False
                queue.clear()
                break
            distance[target] = distance[word] + 1
            parent[target] = word
            parent_move[target] = (i, sign)
            queue.append(target)
    distance_to_certificate = {
        word: 1 for word in boundary_free_states
    }
    distance_queue = deque(boundary_free_states)
    while distance_queue:
        word = distance_queue.popleft()
        for target in free_adjacency.get(word, ()):
            if target not in distance or target in distance_to_certificate:
                continue
            distance_to_certificate[target] = distance_to_certificate[word] + 1
            distance_queue.append(target)
    maximum_certificate_distance = (
        max(distance_to_certificate.values())
        if distance_to_certificate else None
    )
    farthest_words = (
        [
            list(word) for word, value in distance_to_certificate.items()
            if value == maximum_certificate_distance
        ][:20]
        if maximum_certificate_distance is not None else []
    )
    path = []
    if counterexample is not None:
        cursor = counterexample
        while parent[cursor] is not None:
            path.append(parent_move[cursor])
            cursor = parent[cursor]
        path.reverse()
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
        "convention": "(pq)(x)=p(q(x)); R(a,b)=(b,bab) and its inverse",
        "claim_tested": "Every connected genus-one identity word has a connected identity-preserving two-deletion certificate after at most one adjacent Hurwitz move.",
        "scope_warning": "A witness is an exact universal refutation; exhaustion from one start covers only its direct-free induced component.",
        "N": n,
        "length": len(start),
        "max_states": args.max_states,
        "start_word_edge_indices": list(start),
        "visited_direct_free_states": len(distance),
        "maximum_direct_free_distance_from_start": max_distance,
        "component_exhausted": complete and not queue and counterexample is None,
        "search_exhausted_without_state_limit": (
            complete and not queue and not stopped_early
        ),
        "direct_neighbor_count_histogram": {
            str(count): frequency
            for count, frequency in sorted(direct_neighbor_histogram.items())
        },
        "counterexample_found": counterexample is not None,
        "counterexample_word_edge_indices": (
            list(counterexample) if counterexample is not None else None
        ),
        "path_to_counterexample": [[i, sign] for i, sign in path],
        "partial_explored_maximum_distance_to_direct_certificate_set": maximum_certificate_distance,
        "farthest_words_edge_indices": farthest_words,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
