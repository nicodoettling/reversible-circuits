#!/usr/bin/env python3
"""Exact falsification checks for M92's tree--cotree metadata proposal.

The universal proof claims in M92 are mathematical.  This script has only two
finite roles:

1. verify the explicit path-supported unmarked genus-one family in small
   cases; and
2. find two actual chronological genus-one factorization tori for which a
   deterministic tree--cotree decomposition has the same two leftover factor
   positions and the same leftover transposition labels, but different
   primal fundamental paths.

The second item refutes the *specific* claim that the leftover positions and
their endpoint labels determine the contraction/surgery transcript.  It does
not refute every constant-metadata certificate or every signed cover law.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import subprocess
import sys
import time
from collections import deque
from pathlib import Path


sys.dont_write_bytecode = True


def compose(p, q):
    """Return pq, so (pq)(x)=p(q(x))."""
    return tuple(p[q[x]] for x in range(len(p)))


def transposition(n: int, edge):
    a, b = edge
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def evaluate(word, n: int):
    value = tuple(range(n))
    for edge in word:
        value = compose(value, transposition(n, edge))
    return value


def support_connected(word, n: int, omitted=()):
    omitted = set(omitted)
    adjacency = [set() for _ in range(n)]
    for index, (a, b) in enumerate(word):
        if index in omitted:
            continue
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == n


def marked_adjacent_pairs(word, n: int):
    return tuple(
        i
        for i in range(len(word) - 1)
        if word[i] == word[i + 1]
        and support_connected(word, n, omitted=(i, i + 1))
    )


def path_supported_word(d: int):
    if d < 3:
        raise ValueError("d must be at least 3")
    path = tuple((i, i + 1) for i in range(d - 1))
    word = [path[0], path[1]] * 3
    for edge in path[2:]:
        word.extend((edge, edge))
    return tuple(word)


def prufer_tree(sequence, d: int):
    degree = [1] * d
    for vertex in sequence:
        degree[vertex] += 1
    edges = []
    for vertex in sequence:
        leaf = min(index for index, value in enumerate(degree) if value == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degree[leaf] -= 1
        degree[vertex] -= 1
    last = [index for index, value in enumerate(degree) if value == 1]
    edges.append(tuple(sorted(last)))
    return tuple(sorted(edges))


def tree_supported_unmarked_word(tree):
    """Use an order-three alternating pair and square every other tree edge."""
    pair = None
    for first, second in itertools.combinations(tree, 2):
        if len(set(first) & set(second)) == 1:
            pair = (first, second)
            break
    if pair is None:
        raise AssertionError("a tree on at least three vertices has adjacent edges")
    first, second = pair
    word = [first, second] * 3
    for edge in tree:
        if edge not in pair:
            word.extend((edge, edge))
    return tuple(word)


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, a: int):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[b] = a
        return True


def chronological_faces(word, n: int):
    """Return face dart cycles and a dart-to-face map for sigma alpha."""
    darts = tuple((edge, side) for edge in range(len(word)) for side in (0, 1))
    dart_id = {dart: index for index, dart in enumerate(darts)}
    alpha = [0] * len(darts)
    for edge in range(len(word)):
        alpha[dart_id[(edge, 0)]] = dart_id[(edge, 1)]
        alpha[dart_id[(edge, 1)]] = dart_id[(edge, 0)]
    sigma = [0] * len(darts)
    for vertex in range(n):
        incident = [
            dart_id[(edge, side)]
            for edge, endpoints in enumerate(word)
            for side, endpoint in enumerate(endpoints)
            if endpoint == vertex
        ]
        for index, dart in enumerate(incident):
            sigma[dart] = incident[(index + 1) % len(incident)]
    phi = [sigma[alpha[dart]] for dart in range(len(darts))]
    seen = set()
    faces = []
    dart_face = {}
    for root in range(len(darts)):
        if root in seen:
            continue
        face_id = len(faces)
        face = []
        dart = root
        while dart not in seen:
            seen.add(dart)
            dart_face[darts[dart]] = face_id
            face.append(darts[dart])
            dart = phi[dart]
        faces.append(tuple(face))
    return tuple(faces), dart_face


def tree_path(tree_indices, word, start: int, finish: int):
    adjacency = [[] for _ in range(max(max(e) for e in word) + 1)]
    for index in tree_indices:
        a, b = word[index]
        adjacency[a].append((b, index))
        adjacency[b].append((a, index))
    queue = deque([start])
    previous = {start: None}
    while queue:
        a = queue.popleft()
        if a == finish:
            break
        for b, edge_index in sorted(adjacency[a], key=lambda item: item[1]):
            if b not in previous:
                previous[b] = (a, edge_index)
                queue.append(b)
    if finish not in previous:
        raise AssertionError("tree path missing")
    path = []
    a = finish
    while previous[a] is not None:
        a, edge_index = previous[a]
        path.append(edge_index)
    return tuple(reversed(path))


def tree_cotree_signature(word, n: int):
    """Ascending primal Kruskal, then ascending complementary dual Kruskal."""
    primal = UnionFind(n)
    tree = []
    for index, (a, b) in enumerate(word):
        if primal.union(a, b):
            tree.append(index)
    if len(tree) != n - 1:
        raise AssertionError("support not connected")

    faces, dart_face = chronological_faces(word, n)
    if len(faces) != n:
        raise AssertionError(("not a genus-one identity surface", len(faces), n))
    dual = UnionFind(len(faces))
    cotree = []
    tree_set = set(tree)
    for index in range(len(word)):
        if index in tree_set:
            continue
        left = dart_face[(index, 0)]
        right = dart_face[(index, 1)]
        if dual.union(left, right):
            cotree.append(index)
    if len(cotree) != n - 1:
        raise AssertionError(("dual complement not connected", tree, cotree))
    leftovers = tuple(
        index
        for index in range(len(word))
        if index not in tree_set and index not in set(cotree)
    )
    if len(leftovers) != 2:
        raise AssertionError((tree, cotree, leftovers))
    leftover_edges = tuple(word[index] for index in leftovers)
    paths = tuple(
        tree_path(tree, word, word[index][0], word[index][1])
        for index in leftovers
    )
    return {
        "tree": tuple(tree),
        "cotree": tuple(cotree),
        "leftovers": leftovers,
        "leftover_edges": leftover_edges,
        "fundamental_paths": paths,
        "face_count": len(faces),
    }


def find_metadata_collision(n: int):
    edges = tuple(itertools.combinations(range(n), 2))
    length = 2 * n
    identity = tuple(range(n))
    seen = {}
    checked = 0
    identity_count = 0
    connected_count = 0
    for indices in itertools.product(range(len(edges)), repeat=length):
        checked += 1
        word = tuple(edges[index] for index in indices)
        if evaluate(word, n) != identity:
            continue
        identity_count += 1
        if not support_connected(word, n):
            continue
        connected_count += 1
        signature = tree_cotree_signature(word, n)
        key = (signature["leftovers"], signature["leftover_edges"])
        path_signature = signature["fundamental_paths"]
        prior = seen.get(key)
        if prior is not None and prior[1]["fundamental_paths"] != path_signature:
            return {
                "found": True,
                "words_checked": checked,
                "identity_words_seen": identity_count,
                "connected_genus_one_words_seen": connected_count,
                "metadata": {
                    "leftover_positions": list(key[0]),
                    "leftover_edges": [list(edge) for edge in key[1]],
                },
                "first": {
                    "word": [list(edge) for edge in prior[0]],
                    **{name: list(value) if isinstance(value, tuple) else value
                       for name, value in prior[1].items()},
                },
                "second": {
                    "word": [list(edge) for edge in word],
                    **{name: list(value) if isinstance(value, tuple) else value
                       for name, value in signature.items()},
                },
            }
        seen[key] = (word, signature)
    return {
        "found": False,
        "words_checked": checked,
        "identity_words_seen": identity_count,
        "connected_genus_one_words_seen": connected_count,
    }


def nested_json(value):
    if isinstance(value, tuple):
        return [nested_json(item) for item in value]
    if isinstance(value, list):
        return [nested_json(item) for item in value]
    if isinstance(value, dict):
        return {key: nested_json(item) for key, item in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collision-n", type=int, default=4)
    parser.add_argument("--path-d-max", type=int, default=10)
    parser.add_argument("--all-tree-d-max", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    path_checks = []
    for d in range(3, args.path_d_max + 1):
        word = path_supported_word(d)
        item = {
            "d": d,
            "length": len(word),
            "identity": evaluate(word, d) == tuple(range(d)),
            "connected": support_connected(word, d),
            "marked_adjacent_positions": list(marked_adjacent_pairs(word, d)),
            "support_distinct_edges": len(set(word)),
            "cayley_tree_guess_probability": f"1/{d ** (d - 2)}",
        }
        assert item["length"] == 2 * d
        assert item["identity"] and item["connected"]
        assert not item["marked_adjacent_positions"]
        assert item["support_distinct_edges"] == d - 1
        path_checks.append(item)

    all_tree_checks = []
    for d in range(3, args.all_tree_d_max + 1):
        seen_trees = set()
        failures = []
        for sequence in itertools.product(range(d), repeat=d - 2):
            tree = prufer_tree(sequence, d)
            seen_trees.add(tree)
            word = tree_supported_unmarked_word(tree)
            if not (
                len(word) == 2 * d
                and evaluate(word, d) == tuple(range(d))
                and support_connected(word, d)
                and not marked_adjacent_pairs(word, d)
                and set(word) == set(tree)
            ):
                failures.append({
                    "tree": [list(edge) for edge in tree],
                    "word": [list(edge) for edge in word],
                })
                break
        assert len(seen_trees) == d ** (d - 2)
        assert not failures
        all_tree_checks.append({
            "d": d,
            "prufer_sequences": d ** (d - 2),
            "distinct_trees": len(seen_trees),
            "failures": failures,
        })

    collision = find_metadata_collision(args.collision_n)
    if not collision["found"]:
        raise AssertionError("no metadata collision found in requested exact search")
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
        "convention": "(pq)(x)=p(q(x)); chronological faces use phi=sigma alpha",
        "claim_tested": (
            "Leftover tree-cotree factor positions plus their transposition "
            "labels determine the primal fundamental paths needed by surgery."
        ),
        "scope_warning": (
            "The explicit collision refutes only this metadata sufficiency claim. "
            "Finite checks do not refute all tree-cotree certificates or prove an "
            "arbitrary-macro cover."
        ),
        "path_supported_unmarked_checks": path_checks,
        "all_cayley_tree_unmarked_checks": all_tree_checks,
        "tree_cotree_metadata_collision": nested_json(collision),
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
