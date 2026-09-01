#!/usr/bin/env python3
"""Exact finite falsifier for M29 peak/height/join-tree layer claims.

The script enumerates the *single* minimal connected Hurwitz orbit F_N from a
paired spanning-tree word.  Classification H is not inferred from the run;
the known exact cardinality (2N-2)! N^(N-3) is checked before any layer data
are emitted.  The universal claims this can falsify are explicitly recorded
in the JSON output:

* peak-count, area, maximum-height, and midpoint-height layer unimodality or
  log-concavity;
* join-tree leaf-count and maximum-degree layer unimodality/log-concavity.

Passing a finite N is not evidence for a uniform asymptotic shell theorem.
Convention: (pq)(x)=p(q(x)); project right Hurwitz
R(a,b)=(b,bab), R^{-1}(a,b)=(aba,a).
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
import time
from collections import Counter, deque
from pathlib import Path


def edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def apply_transposition(e: tuple[int, int], x: int) -> int:
    a, b = e
    if x == a:
        return b
    if x == b:
        return a
    return x


def conjugate(a: tuple[int, int], by: tuple[int, int]) -> tuple[int, int]:
    x, y = apply_transposition(by, a[0]), apply_transposition(by, a[1])
    return (x, y) if x < y else (y, x)


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.p[y] = x
        self.size[x] += self.size[y]
        return True


def stats(word: list[int], es: list[tuple[int, int]], n: int) -> dict[str, int]:
    dsu = DSU(n)
    h = 0
    heights = [0]
    join_edges: list[tuple[int, int]] = []
    steps: list[int] = []
    for idx in word:
        a, b = es[idx]
        if dsu.union(a, b):
            h += 1
            steps.append(1)
            join_edges.append((a, b))
        else:
            h -= 1
            steps.append(-1)
        heights.append(h)
    if h != 0 or len(join_edges) != n - 1 or min(heights) < 0:
        raise AssertionError("minimal-orbit Dyck/tree invariant failed")
    deg = [0] * n
    for a, b in join_edges:
        deg[a] += 1
        deg[b] += 1
    return {
        "area": sum(heights),
        "peaks": sum(steps[i] == 1 and steps[i + 1] == -1 for i in range(len(steps) - 1)),
        "maximum_height": max(heights),
        "midpoint_height": heights[n - 1],
        "join_tree_leaves": sum(d == 1 for d in deg),
        "join_tree_max_degree": max(deg),
    }


def minimum_cut_span(word: list[int], es: list[tuple[int, int]], n: int) -> int:
    """Minimum interval length containing all factors crossing a vertex cut.

    We represent each unordered nontrivial bipartition once by requiring
    vertex n-1 to lie outside S.  Connected support guarantees a nonempty
    crossing-position list.  If the answer exceeds five, no r<=5 update can
    disconnect the support: every factor outside its window is unchanged.
    """
    answer = len(word) + 1
    for mask in range(1, 1 << (n - 1)):
        positions = []
        for position, idx in enumerate(word):
            a, b = es[idx]
            in_a = a < n - 1 and ((mask >> a) & 1)
            in_b = b < n - 1 and ((mask >> b) & 1)
            if in_a != in_b:
                positions.append(position)
        if not positions:
            raise AssertionError("connected support has a cut with no edge")
        answer = min(answer, positions[-1] - positions[0] + 1)
    return answer


def is_unimodal(seq: list[int]) -> bool:
    if not seq:
        return True
    i = 1
    while i < len(seq) and seq[i] >= seq[i - 1]:
        i += 1
    while i < len(seq) and seq[i] <= seq[i - 1]:
        i += 1
    return i == len(seq)


def is_log_concave(seq: list[int]) -> bool:
    return all(seq[i] * seq[i] >= seq[i - 1] * seq[i + 1] for i in range(1, len(seq) - 1))


def feasible_lattice(counter: Counter[int]) -> tuple[list[int], list[int]]:
    """Return ordered nonzero layers.

    Area and a fixed-time height have a forced parity.  Inserting structural
    zeros between their feasible layers would create a spurious failure of
    unimodality/log-concavity, so these tests are on the actual support.
    """
    support = sorted(counter)
    return support, [counter[k] for k in support]


def enumerate_orbit(n: int) -> dict:
    es = edges(n)
    m = 2 * n - 2
    base = len(es)
    powers = [base**i for i in range(m)]
    edge_to_i = {e: i for i, e in enumerate(es)}
    conj = [[edge_to_i[conjugate(es[a], es[b])] for b in range(base)] for a in range(base)]

    # Star-tree paired representative: (01,01),(02,02),... .
    start_word = []
    for v in range(1, n):
        e = edge_to_i[(0, v)]
        start_word.extend((e, e))
    start = sum(d * powers[i] for i, d in enumerate(start_word))

    seen = {start}
    queue = deque([start])
    counters = {name: Counter() for name in (
        "area", "peaks", "maximum_height", "midpoint_height",
        "join_tree_leaves", "join_tree_max_degree",
    )}
    cut_span_counter: Counter[int] = Counter()
    first_no_local_disconnect = None
    t0 = time.time()
    while queue:
        code = queue.popleft()
        tmp = code
        word = [0] * m
        for i in range(m):
            word[i], tmp = tmp % base, tmp // base
        st = stats(word, es, n)
        for name, value in st.items():
            counters[name][value] += 1
        span = minimum_cut_span(word, es, n)
        cut_span_counter[span] += 1
        if span > 5 and first_no_local_disconnect is None:
            first_no_local_disconnect = [list(es[idx]) for idx in word]

        for i in range(m - 1):
            a, b = word[i], word[i + 1]
            # R(a,b)=(b,bab): conjugate a by b.
            u, v = b, conj[a][b]
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
            # R^{-1}(a,b)=(aba,a): conjugate b by a.
            u, v = conj[b][a], a
            nxt = code + (u - a) * powers[i] + (v - b) * powers[i + 1]
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

    expected = math.factorial(2 * n - 2) * n ** (n - 3)
    if len(seen) != expected:
        raise AssertionError(f"orbit size {len(seen)} != exact {expected}")

    layer_data = {}
    for name, counter in counters.items():
        support, counts = feasible_lattice(counter)
        layer_data[name] = {
            "support": support,
            "counts": counts,
            "unimodal": is_unimodal(counts),
            "log_concave": is_log_concave(counts),
        }
    return {
        "N": n,
        "m": m,
        "M": base,
        "orbit_size": len(seen),
        "expected_orbit_size": expected,
        "elapsed_seconds": time.time() - t0,
        "layers": layer_data,
        "minimum_vertex_cut_span_distribution": dict(sorted(cut_span_counter.items())),
        "states_certified_to_have_zero_macro_exit": sum(
            count for span, count in cut_span_counter.items() if span > 5
        ),
        "first_zero_macro_exit_witness_edges": first_no_local_disconnect,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "purpose": "Finite exact falsifier only; no asymptotic inference.",
        "claims_tested": [
            "Minimal-orbit area/peak/height layers are unimodal or log-concave.",
            "Minimal join-tree leaf/max-degree layers are unimodal or log-concave.",
            "Every minimal connected word has a one-step r<=5 full-K exit from full support.",
        ],
        "convention": "(pq)(x)=p(q(x)); word product left-to-right; R(a,b)=(b,bab)",
        "seed": None,
        "python": platform.python_version(),
        "argv": sys.argv,
        "result": enumerate_orbit(args.N),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
