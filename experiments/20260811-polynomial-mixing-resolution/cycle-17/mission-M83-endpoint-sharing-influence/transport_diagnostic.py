#!/usr/bin/env python3
"""Finite max-flow test for local transport of K-row differences on Lambda_n.

For each tested Lambda edge (x,y), write K(x,.)-K(y,.) as positive minus
negative mass.  Test whether all Jordan mass can be transported along one
Lambda edge between its positive and negative supports.  This is an exact
combinatorial question once the rational kernel is built, but this diagnostic
uses floating capacities and reports a numerical tolerance explicitly.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import subprocess
import sys
from collections import deque
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("m83_influence", HERE / "influence_diagnostic.py")
assert SPEC is not None and SPEC.loader is not None
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class Dinic:
    def __init__(self, n: int):
        self.g: list[list[list[float | int]]] = [[] for _ in range(n)]

    def add(self, u: int, v: int, cap: float) -> None:
        a = [v, cap, len(self.g[v])]
        b = [u, 0.0, len(self.g[u])]
        self.g[u].append(a)
        self.g[v].append(b)

    def flow(self, source: int, sink: int, tolerance: float) -> float:
        total = 0.0
        while True:
            level = [-1] * len(self.g)
            level[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for v, cap, _ in self.g[u]:
                    if cap > tolerance and level[int(v)] < 0:
                        level[int(v)] = level[u] + 1
                        q.append(int(v))
            if level[sink] < 0:
                return total
            it = [0] * len(self.g)

            def dfs(u: int, amount: float) -> float:
                if u == sink:
                    return amount
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, cap, rev = int(e[0]), float(e[1]), int(e[2])
                    if cap > tolerance and level[v] == level[u] + 1:
                        sent = dfs(v, min(amount, cap))
                        if sent > tolerance:
                            e[1] = cap - sent
                            self.g[v][rev][1] = float(self.g[v][rev][1]) + sent
                            return sent
                    it[u] += 1
                return 0.0

            while True:
                sent = dfs(source, float("inf"))
                if sent <= tolerance:
                    break
                total += sent


def transport_fraction(eta: np.ndarray, adjacency: list[set[int]], radius: int,
                       tolerance: float) -> tuple[float, int, int]:
    positive = [i for i, x in enumerate(eta) if x > tolerance]
    negative = [i for i, x in enumerate(eta) if x < -tolerance]
    mass = float(np.sum(eta[positive]))
    if mass <= tolerance:
        return 1.0, len(positive), len(negative)

    reachable: list[set[int]] = []
    for i in positive:
        seen = {i}
        frontier = {i}
        for _ in range(radius):
            frontier = {v for u in frontier for v in adjacency[u]} - seen
            seen |= frontier
        reachable.append(seen)

    offset_p = 1
    offset_n = offset_p + len(positive)
    sink = offset_n + len(negative)
    net = Dinic(sink + 1)
    for pidx, i in enumerate(positive):
        net.add(0, offset_p + pidx, float(eta[i]))
    for nidx, j in enumerate(negative):
        net.add(offset_n + nidx, sink, float(-eta[j]))
    for pidx, seen in enumerate(reachable):
        for nidx, j in enumerate(negative):
            if j in seen:
                net.add(offset_p + pidx, offset_n + nidx, mass)
    value = net.flow(0, sink, tolerance)
    return min(1.0, value / mass), len(positive), len(negative)


def analyze(n: int, all_edges_through: int, tolerance: float) -> dict[str, object]:
    _, orbits, kernel, squared, _, witnesses = MOD.build(n, False)
    adjacency = [set() for _ in orbits]
    for i, j in witnesses:
        adjacency[i].add(j)
        adjacency[j].add(i)
    distances = []
    for source in range(len(orbits)):
        row = [-1] * len(orbits)
        row[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if row[v] < 0:
                    row[v] = row[u] + 1
                    queue.append(v)
        distances.append(row)
    edges = list(witnesses)
    one_tv = []
    two_tv = []
    for i, j in edges:
        one_tv.append(0.5 * float(np.sum(np.abs(kernel[i] - kernel[j]))))
        two_tv.append(0.5 * float(np.sum(np.abs(squared[i] - squared[j]))))
    order = sorted(range(len(edges)), key=lambda k: max(one_tv[k], two_tv[k]), reverse=True)
    tested = order if n <= all_edges_through else sorted(set(order[:20] + [int(x) for x in np.linspace(0, len(edges)-1, 20)]))
    rows = []
    minima = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0}
    for index in tested:
        i, j = edges[index]
        eta = kernel[i] - kernel[j]
        positive_indices = [u for u, x in enumerate(eta) if x > tolerance]
        negative_indices = [v for v, x in enumerate(eta) if x < -tolerance]
        maximum_cross_sign_distance = max(
            distances[u][v] for u in positive_indices for v in negative_indices
        )
        fractions = {}
        for radius in minima:
            fraction, pos, neg = transport_fraction(eta, adjacency, radius, tolerance)
            fractions[str(radius)] = fraction
            minima[radius] = min(minima[radius], fraction)
        rows.append({
            "edge": [i, j],
            "source_descriptors": [
                MOD.descriptor(orbits[i][0], tuple((x + 1) % n for x in range(n))),
                MOD.descriptor(orbits[j][0], tuple((x + 1) % n for x in range(n))),
            ],
            "TV_K": one_tv[index],
            "TV_K2": two_tv[index],
            "positive_support": pos,
            "negative_support": neg,
            "maximum_positive_to_negative_graph_distance": maximum_cross_sign_distance,
            "transported_fraction_by_radius": fractions,
        })
    return {
        "n": n,
        "quotient_states": len(orbits),
        "Lambda_edges": len(edges),
        "tested_edges": len(tested),
        "all_edges_tested": len(tested) == len(edges),
        "minimum_transported_fraction_by_radius": {str(k): v for k, v in minima.items()},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, required=True)
    parser.add_argument("--all-edges-through", type=int, default=9)
    parser.add_argument("--tolerance", type=float, default=1e-12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = {
        "status": "finite_floating_transport_diagnostic_only",
        "claim_tested": "Jordan transport for K-row differences on Lambda_n",
        "convention": "(pq)(x)=p(q(x)); tuple products left-to-right",
        "deterministic": True,
        "seed": None,
        "tolerance": args.tolerance,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "repository_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "command": " ".join(sys.argv),
        "results": [analyze(n, args.all_edges_through, args.tolerance) for n in args.n],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps([{k: v for k, v in row.items() if k != "rows"} for row in payload["results"]], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
