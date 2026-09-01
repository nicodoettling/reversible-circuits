#!/usr/bin/env python3
"""Exact falsifier for a marked-leaf strand-deletion decomposition of Z_d.

The named claims are:
  (A) every fixed (deleted label v, deleted word z) fiber is connected under
      literal signed adjacent-Hurwitz moves retaining v and z;
  (B) strand deletion sends one physical signed Hurwitz proposal to either a
      self-loop or one signed adjacent-Hurwitz proposal of z;
  (C) every oriented base proposal z->z' has at least one one-step physical
      lift from every nonempty marked fiber (v,z).

Only d=2,3,4 are enumerated.  A pass cannot prove a universal statement; a
failure is an exact counterexample.  Convention: (pq)(x)=p(q(x)).
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path


sys.dont_write_bytecode = True


Edge = tuple[int, int]
Word = tuple[Edge, ...]


def edges(n: int) -> list[Edge]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def move_vertex(e: Edge, x: int) -> int:
    if x == e[0]:
        return e[1]
    if x == e[1]:
        return e[0]
    return x


def conjugate(a: Edge, b: Edge) -> Edge:
    """Return b a b."""
    x, y = move_vertex(b, a[0]), move_vertex(b, a[1])
    return (x, y) if x < y else (y, x)


def append_edge(p: tuple[int, ...], e: Edge) -> tuple[int, ...]:
    q = list(p)
    q[e[0]], q[e[1]] = q[e[1]], q[e[0]]
    return tuple(q)


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.parent[y] = x
        return True


def evaluate(n: int, word: Word) -> tuple[int, ...]:
    p = tuple(range(n))
    for e in word:
        p = append_edge(p, e)
    return p


def join_tree(n: int, word: Word) -> tuple[Edge, ...]:
    dsu = DSU(n)
    out = []
    for e in word:
        if dsu.union(*e):
            out.append(e)
    if len(out) != n - 1:
        raise AssertionError(("not minimal connected", n, word, out))
    return tuple(sorted(out))


def leaves(n: int, tree: tuple[Edge, ...]) -> tuple[int, ...]:
    deg = [0] * n
    for a, b in tree:
        deg[a] += 1
        deg[b] += 1
    return tuple(i for i, x in enumerate(deg) if x == 1)


def erase_label(p: tuple[int, ...], v: int) -> tuple[int, ...]:
    labels = [x for x in range(len(p)) if x != v]
    rank = {x: i for i, x in enumerate(labels)}
    out = []
    for x in labels:
        y = p[x]
        if y == v:
            y = p[v]
        out.append(rank[y])
    return tuple(out)


def delete_strand(n: int, word: Word, v: int) -> tuple[Word, tuple[int, int]]:
    labels = [x for x in range(n) if x != v]
    small_edges = edges(n - 1)
    p = tuple(range(n))
    old = erase_label(p, v)
    out: list[Edge] = []
    nulls: list[int] = []
    for j, e in enumerate(word):
        p = append_edge(p, e)
        new = erase_label(p, v)
        delta = compose(inverse(old), new)
        moved = [x for x in range(n - 1) if delta[x] != x]
        if not moved:
            nulls.append(j)
        elif len(moved) == 2 and delta[moved[0]] == moved[1] and delta[moved[1]] == moved[0]:
            out.append(tuple(sorted((moved[0], moved[1]))))
        else:
            raise AssertionError(("bad deletion increment", n, word, v, j, delta))
        old = new
    if len(nulls) != 2 or any(e not in small_edges for e in out):
        raise AssertionError(("bad deletion", n, word, v, out, nulls))
    return tuple(out), (nulls[0], nulls[1])


def proposals(word: Word):
    for i in range(len(word) - 1):
        a, b = word[i], word[i + 1]
        yield i, 1, word[:i] + (b, conjugate(a, b)) + word[i + 2 :]
        yield i, -1, word[:i] + (conjugate(b, a), a) + word[i + 2 :]


def enumerate_z(n: int) -> list[Word]:
    m = 2 * n - 2
    es = edges(n)
    ans = []
    # d<=4 only: 6^6 candidates at the largest size.
    def rec(prefix: list[Edge], p: tuple[int, ...]):
        if len(prefix) == m:
            if p == tuple(range(n)):
                word = tuple(prefix)
                dsu = DSU(n)
                for e in word:
                    dsu.union(*e)
                if len({dsu.find(i) for i in range(n)}) == 1:
                    ans.append(word)
            return
        for e in es:
            prefix.append(e)
            rec(prefix, append_edge(p, e))
            prefix.pop()
    rec([], tuple(range(n)))
    return ans


def word_json(word: Word):
    return [list(e) for e in word]


def audit_d(d: int) -> dict:
    started = time.perf_counter()
    states = enumerate_z(d)
    state_set = set(states)
    expected = 1 if d == 2 else __import__("math").factorial(2 * d - 2) * d ** (d - 3)
    if len(states) != expected:
        raise AssertionError((d, len(states), expected))

    marked = []
    fibers: dict[tuple[int, Word], list[Word]] = defaultdict(list)
    leaf_counts = Counter()
    null_separations = Counter()
    for w in states:
        vs = leaves(d, join_tree(d, w))
        leaf_counts[len(vs)] += 1
        for v in vs:
            z, nulls = delete_strand(d, w, v)
            if evaluate(d - 1, z) != tuple(range(d - 1)):
                raise AssertionError("deleted word not identity")
            fibers[(v, z)].append(w)
            marked.append((w, v))
            null_separations[nulls[1] - nulls[0]] += 1

    components = Counter()
    disconnected = []
    internal_directed_edges = 0
    for (v, z), ws in fibers.items():
        bucket = set(ws)
        adj = {w: set() for w in ws}
        for w in ws:
            for _i, _sgn, wp in proposals(w):
                if wp in bucket:
                    adj[w].add(wp)
                    if wp != w:
                        internal_directed_edges += 1
        unseen = set(ws)
        comps = []
        while unseen:
            root = next(iter(unseen))
            seen = {root}
            queue = deque([root])
            while queue:
                x = queue.popleft()
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y)
                        queue.append(y)
            unseen.difference_update(seen)
            comps.append(seen)
        components[len(comps)] += 1
        if len(comps) > 1 and len(disconnected) < 5:
            reps = [next(iter(c)) for c in comps[:4]]
            disconnected.append({
                "v": v,
                "z": word_json(z),
                "fiber_size": len(ws),
                "component_sizes": sorted((len(c) for c in comps), reverse=True),
                "component_representatives": [word_json(x) for x in reps],
            })

    # Deletion-equivariance audit and the strong one-step lifting test.
    deletion_images = Counter()
    bad_equivariance = []
    strong_lift_failures = []
    strong_lift_failure_count = 0
    strong_lift_tests = 0
    base_neighbors: dict[Word, list[tuple[int, int, Word]]] = {}
    for _v, z in fibers:
        if z not in base_neighbors:
            base_neighbors[z] = list(proposals(z)) if len(z) >= 2 else []
    for (v, z), ws in fibers.items():
        # A base self-loop requires no simulated edge and is irrelevant to
        # Dirichlet-form comparison.  Claim C concerns off-diagonal moves.
        wanted = {(i, sgn, zp) for i, sgn, zp in base_neighbors[z] if zp != z}
        for w in ws:
            achieved = set()
            for i, sgn, wp in proposals(w):
                if wp not in state_set:
                    raise AssertionError("Hurwitz proposal left Z_d")
                if v not in leaves(d, join_tree(d, wp)):
                    deletion_images["mark_lost"] += 1
                    continue
                zp, _ = delete_strand(d, wp, v)
                if zp == z:
                    deletion_images["identity"] += 1
                else:
                    matches = [(j, o) for j, o, zz in base_neighbors[z] if zz == zp]
                    if not matches:
                        deletion_images["not_one_base_move"] += 1
                        if len(bad_equivariance) < 5:
                            bad_equivariance.append({
                                "v": v, "z": word_json(z), "w": word_json(w),
                                "physical_site": i, "physical_orientation": sgn,
                                "image": word_json(zp),
                            })
                    else:
                        deletion_images["one_base_move"] += 1
                        for item in matches:
                            achieved.add((item[0], item[1], zp))
            for item in wanted:
                strong_lift_tests += 1
                if item not in achieved:
                    strong_lift_failure_count += 1
                    if len(strong_lift_failures) < 10:
                        strong_lift_failures.append({
                            "v": v, "z": word_json(z), "w": word_json(w),
                            "base_site": item[0], "base_orientation": item[1],
                            "base_target": word_json(item[2]),
                        })

    sizes = [len(ws) for ws in fibers.values()]
    return {
        "d": d,
        "length": 2 * d - 2,
        "states": len(states),
        "marked_incidences": len(marked),
        "leaf_count_histogram": dict(sorted(leaf_counts.items())),
        "fibers": len(fibers),
        "fiber_size_min": min(sizes),
        "fiber_size_max": max(sizes),
        "fiber_size_histogram": dict(sorted(Counter(sizes).items())),
        "null_separation_histogram": dict(sorted(null_separations.items())),
        "fiber_component_count_histogram": dict(sorted(components.items())),
        "internal_directed_nonself_edges": internal_directed_edges,
        "disconnected_examples": disconnected,
        "deletion_image_classes": dict(sorted(deletion_images.items())),
        "bad_equivariance_examples": bad_equivariance,
        "strong_one_step_lift_tests": strong_lift_tests,
        "strong_one_step_lift_failure_count": strong_lift_failure_count,
        "strong_one_step_lift_failures_recorded": strong_lift_failures,
        "elapsed_seconds": time.perf_counter() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if any(d < 2 or d > 4 for d in args.d):
        raise SystemExit("exact audit is intentionally restricted to 2<=d<=4")
    started = time.perf_counter()
    rows = [audit_d(d) for d in args.d]
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
        "claims_tested": {
            "A": "Every fixed (v,Del_v(w)) marked-leaf fiber is connected by literal signed adjacent-Hurwitz moves preserving that key.",
            "B": "Every physical proposal retaining v deletes to a self-loop or one signed adjacent-Hurwitz proposal.",
            "C": "Every nontrivial oriented base proposal has a one-step physical lift from every state in every marked fiber.",
        },
        "scope_warning": "Finite passes are falsification checks only; any failure is an exact counterexample.",
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"rows": [{k: row[k] for k in ("d", "states", "marked_incidences", "fibers", "fiber_size_min", "fiber_size_max", "fiber_component_count_histogram", "deletion_image_classes", "strong_one_step_lift_tests", "strong_one_step_lift_failures_recorded")} for row in rows], "elapsed_seconds": payload["elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
