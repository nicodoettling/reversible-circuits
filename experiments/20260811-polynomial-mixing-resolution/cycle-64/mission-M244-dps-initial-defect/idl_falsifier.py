#!/usr/bin/env python3
"""Tiny exact d=5,6 falsifier for the predeclared M244 stack recurrence.

This file imports no predecessor code or data.  It implements DPS Proposition
3 followed by the cyclic LIFO closure of Lemma 2/Theorem 5, then checks the
coordinatewise Initial-Defect Lemma.  Finite success is calibration only.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "idl_falsifier_results.json"


def edge(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def prufer(vertices, code):
    degree = {v: 1 for v in vertices}
    for v in code:
        degree[v] += 1
    ans = []
    for v in code:
        leaf = min(u for u in vertices if degree[u] == 1)
        ans.append(edge(leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    leaves = [v for v in vertices if degree[v] == 1]
    ans.append(edge(*leaves))
    return tuple(sorted(ans))


def trees(d):
    # Generate all trees on [d-1], then append the prescribed root leaf.
    vertices = tuple(range(1, d))
    return tuple(
        sorted(
            {
                tuple(sorted((*prufer(vertices, code), (1, d))))
                for code in itertools.product(vertices, repeat=d - 3)
            }
        )
    )


def parents(tree, root):
    adj = defaultdict(list)
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    p = {root: None}
    todo = [root]
    while todo:
        a = todo.pop()
        for b in adj[a]:
            if b not in p:
                p[b] = a
                todo.append(b)
    assert len(p) == root
    return p


def canonical_pi(d):
    return (2 * d - 3, 2 * d - 2, *range(1, 2 * d - 3))


def swap_values(pi, i):
    return tuple(i + 1 if x == i else i if x == i + 1 else x for x in pi)


def close(tree, pi, d, return_trace=False):
    """Accepted plus mirror, coded directly from the source recurrence."""
    p = parents(tree, d)
    incidence = defaultdict(dict)
    first_black = {}
    for a in range(1, d):
        left, right = pi[2 * a - 2 : 2 * a]
        for label, white in ((left, a), (right, p[a])):
            black = ("B", a)
            w = ("W", white)
            incidence[black][label] = w
            incidence[w][label] = black
            first_black[label] = a

    m = 2 * d - 2
    start = (("W", 1), 1)
    state = start
    seen = set()
    boundary = []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        step = 1 if vertex[0] == "W" else -1
        label = 1 + ((incoming - 1 + step) % m)
        if label in incidence[vertex]:
            boundary.append(("S",))
            state = incidence[vertex][label], label
        else:
            boundary.append(("H", vertex[0], vertex[1], label))
            state = vertex, label
    assert state == start

    tokens = boundary
    second_black = {}
    history = []
    while True:
        hp = [j for j, token in enumerate(tokens) if token[0] == "H"]
        match = None
        for k, left in enumerate(hp):
            right = hp[(k + 1) % len(hp)]
            if tokens[left][1] == "W" and tokens[right][1] == "B":
                match = left, right
                break
        if match is None:
            break
        left, right = match
        tokens = tokens[left:] + tokens[:left]
        right = (right - left) % len(tokens)
        white, black = tokens[0], tokens[right]
        assert white[3] == black[3]
        distance = sum(token[0] == "S" for token in tokens[1:right])
        assert distance in (1, 3)
        history.append((white[3], white[2], black[2], distance))
        if distance == 3:
            assert white[3] not in second_black
            second_black[white[3]] = black[2]
        tokens = [("S",), *tokens[right + 1 :]]

    remaining = [token for token in tokens if token[0] == "H"]
    assert len(remaining) == m
    assert all(token[1] == "W" for token in remaining)
    assert sorted(token[3] for token in remaining) == list(range(1, m + 1))
    word = tuple(
        edge(first_black[label] - 1, second_black.get(label, d) - 1)
        for label in range(1, m + 1)
    )
    if return_trace:
        return word, tuple(history), tuple(remaining)
    return word


def decreasing_path(p, v):
    path = [v]
    while path[-1] != 1:
        path.append(p[path[-1]])
    return tuple(path), all(a > b for a, b in zip(path, path[1:]))


def audit_row(tree, d, v):
    p = parents(tree, d)
    path, decreasing = decreasing_path(p, v)
    i = 2 * v - 3
    old = close(tree, swap_values(canonical_pi(d), i), d)
    naive = old + ((0, d), (0, d))
    plus_tree = tuple(sorted((*tree, (1, d + 1))))
    actual = close(plus_tree, swap_values(canonical_pi(d + 1), i), d + 1)
    failures = []
    if not decreasing:
        if naive != actual:
            failures.append({"kind": "closed_equality", "naive": naive, "actual": actual})
    else:
        x, y, z, n = v - 1, d - 1, 0, d
        expected_positions = {
            2 * v - 2: (edge(x, y), edge(x, n)),
            2 * d - 3: (edge(z, x), edge(z, y)),
            2 * d - 2: (edge(z, y), edge(z, y)),
            2 * d - 1: (edge(z, n), edge(z, x)),
            2 * d: (edge(z, n), edge(z, n)),
        }
        for r in range(v + 1, d):
            u = r - 1
            if p[r] == v:
                expected_positions[2 * r - 3] = (edge(u, y), edge(u, n))
                expected_positions[2 * r - 2] = (edge(u, y), edge(u, n))
            else:
                h = edge(r - 1, p[r] - 1)
                assert not (set(h) & {x, y, n})
                expected_positions[2 * r - 3] = (h, h)
                expected_positions[2 * r - 2] = (h, h)
        for pos in range(1, 2 * d + 1):
            pair = naive[pos - 1], actual[pos - 1]
            expected = expected_positions.get(pos)
            if expected is None:
                expected = (naive[pos - 1], naive[pos - 1])
            if pair != expected:
                failures.append(
                    {"kind": "coordinate", "position": pos, "got": pair, "expected": expected}
                )
    return {
        "d": d,
        "tree": tree,
        "v": v,
        "path": path,
        "decreasing": decreasing,
        "failures": failures,
    }


def main():
    rows = []
    for d in (5, 6):
        ts = trees(d)
        expected = (d - 1) ** (d - 3)
        assert len(ts) == expected
        for tree in ts:
            for v in range(2, d):
                rows.append(audit_row(tree, d, v))
    failures = [row for row in rows if row["failures"]]
    summary = {
        "mission": "M244 tiny IDL falsifier after analytic recurrence fixed",
        "status": "exact finite calibration only",
        "ranks": {
            str(d): {
                "trees": len(trees(d)),
                "rows": sum(row["d"] == d for row in rows),
                "open": sum(row["d"] == d and row["decreasing"] for row in rows),
                "closed": sum(row["d"] == d and not row["decreasing"] for row in rows),
                "failures": sum(row["d"] == d and bool(row["failures"]) for row in rows),
            }
            for d in (5, 6)
        },
        "total_rows": len(rows),
        "failures": failures,
        "rows_digest": hashlib.sha256(
            json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "environment": {
            "python": platform.python_version(),
            "nonstandard_dependencies": {},
            "seed": None,
        },
        "scope": {
            "proves_all_rank": False,
            "every_color": False,
            "gap_or_mixing": False,
        },
    }
    OUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    assert not failures


if __name__ == "__main__":
    main()
