#!/usr/bin/env python3
"""Exact checks of labeled-tree kernels and the bridge-slide comparison."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import platform
import subprocess


def edge(a, b):
    assert a != b
    return tuple(sorted((a, b)))


def tree(edges):
    return tuple(sorted(edges))


def adjacency(n, edges):
    out = [set() for _ in range(n)]
    for a, b in edges:
        out[a].add(b)
        out[b].add(a)
    return out


def component(adj, start):
    seen, todo = {start}, [start]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen


def code_to_tree(n, code):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    out = []
    for x in code:
        leaf = next(v for v in range(n) if degree[v] == 1)
        out.append(edge(leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    last = [v for v in range(n) if degree[v] == 1]
    out.append(edge(*last))
    return tree(out)


def slides(n, t):
    out = []
    for e, f in combinations(t, 2):
        shared = set(e) & set(f)
        if not shared:
            continue
        assert len(shared) == 1
        b = next(iter(shared))
        a = next(v for v in e if v != b)
        c = next(v for v in f if v != b)
        for removed in (e, f):
            out.append(tree((set(t) - {removed}) | {edge(a, c)}))
    assert len(out) == len(set(out))
    return set(out)


def path(adj, u, v):
    parent, todo = {u: None}, [u]
    while v not in parent:
        assert todo
        z = todo.pop()
        for w in sorted(adj[z]):
            if w not in parent:
                parent[w] = z
                todo.append(w)
    out = [v]
    while out[-1] != u:
        out.append(parent[out[-1]])
    return out[::-1]


def orient(e, a):
    u, v = e
    if u not in a:
        u, v = v, u
    assert u in a and v not in a
    return u, v


def route(n, forest, a, old, new):
    adj = adjacency(n, forest)
    u, v = orient(old, a)
    x, y = orient(new, a)
    bridges = [old]
    bridges.extend(edge(z, v) for z in path(adj, u, x)[1:])
    bridges.extend(edge(x, z) for z in path(adj, v, y)[1:])
    return [tree(set(forest) | {e}) for e in bridges]


def check_n(n):
    if n <= 2:
        t = () if n == 1 else ((0, 1),)
        assert not slides(n, t)
        return {"N": n, "states": 1, "singleton_holding": True}
    states = set(code_to_tree(n, code)
                 for code in product(range(n), repeat=n - 2))
    assert len(states) == n ** (n - 2)
    # Independent edge-subset enumeration checks the Pruefer state universe.
    brute = {es for es in combinations(combinations(range(n), 2), n - 1)
             if len(component(adjacency(n, es), 0)) == n}
    assert states == brute
    neighbors = {t: slides(n, t) for t in states}
    wedges = {t: sum(len(ns) * (len(ns) - 1) // 2
                     for ns in adjacency(n, t)) for t in states}
    c, r, d = len(states), n - 1, (n - 1) * (n - 2) // 2
    total_w = sum(wedges.values())
    incoming = {k: defaultdict(Fraction) for k in ("P", "U", "M")}
    for t in states:
        assert n - 2 <= wedges[t] <= d
        assert len(neighbors[t]) == 2 * wedges[t]
        pi = {"P": Fraction(wedges[t], total_w),
              "U": Fraction(1, c), "M": Fraction(1, c)}
        remaining = {k: Fraction(1) for k in pi}
        for z in neighbors[t]:
            assert z in states and t in neighbors[z]
            row = {"P": Fraction(1, 4 * wedges[t]),
                   "U": Fraction(1, 4 * d),
                   "M": Fraction(1, 4 * max(wedges[t], wedges[z]))}
            assert row["M"] >= row["U"]
            for k in row:
                remaining[k] -= row[k]
                incoming[k][z] += pi[k] * row[k]
            assert pi["P"] * row["P"] == Fraction(1, 4 * total_w)
        for k in pi:
            assert remaining[k] >= Fraction(1, 2)
            incoming[k][t] += pi[k] * remaining[k]
    for t in states:
        assert incoming["P"][t] == Fraction(wedges[t], total_w)
        assert incoming["U"][t] == incoming["M"][t] == Fraction(1, c)
    seen, todo = {min(states)}, [min(states)]
    while todo:
        for t in neighbors[todo.pop()]:
            if t not in seen:
                seen.add(t)
                todo.append(t)
    assert seen == states

    loads, counts = defaultdict(Fraction), Counter()
    transitions = max_length = 0
    forest_cache = {}
    for t in sorted(states):
        row_total = Fraction(0)
        for old in t:
            forest = tree(set(t) - {old})
            if forest not in forest_cache:
                a = component(adjacency(n, forest), 0)
                b = set(range(n)) - a
                forest_cache[forest] = (a, b)
            a, b = forest_cache[forest]
            q = Fraction(1, r * len(a) * len(b))
            for x in sorted(a):
                for y in sorted(b):
                    new = edge(x, y)
                    row_total += q
                    if new == old:
                        continue
                    z = tree(set(forest) | {new})
                    assert z in states
                    seq = route(n, forest, a, old, new)
                    length = len(seq) - 1
                    assert seq[0] == t and seq[-1] == z
                    assert 1 <= length <= n - 2
                    assert len(set(seq)) == len(seq)
                    transitions += 1
                    max_length = max(max_length, length)
                    for s, sp in zip(seq, seq[1:]):
                        assert sp in neighbors[s]
                        removed = set(s) - set(sp)
                        assert len(removed) == 1
                        reconstructed = tree(set(s) - removed)
                        assert reconstructed == forest
                        assert tree(set(reconstructed) | {old}) == t
                        assert tree(set(reconstructed) | {new}) == z
                        loads[s, sp] += q * length
                        counts[s, sp] += 1
        assert row_total == 1
    assert len(loads) == sum(map(len, neighbors.values()))
    for (s, sp), count in counts.items():
        old = next(iter(set(s) - set(sp)))
        new = next(iter(set(sp) - set(s)))
        forest = tree(set(s) - {old})
        a, b = forest_cache[forest]
        fixed = set(old) & set(new)
        assert len(fixed) == 1
        p = next(iter(set(old) - fixed))
        q = next(iter(set(new) - fixed))
        internal = edge(p, q)
        assert internal in forest
        cut = adjacency(n, set(forest) - {internal})
        side = component(cut, p)
        moving, other = (a, b) if p in a else (b, a)
        assert q in moving and side < moving
        expected = len(side) * (len(moving) - len(side)) * len(other)
        assert count == expected
        assert loads[s, sp] <= Fraction(n - 2, 4)
    max_load = max(loads.values())
    comparison = 4 * d * max_load
    assert comparison <= d * (n - 2)
    if n == 3:
        assert all(w == 1 for w in wedges.values())
        assert all(len(v) == 2 for v in neighbors.values())
    return {"N": n, "states": c, "independent_edge_enumeration": True,
            "wedge_histogram": dict(sorted(Counter(wedges.values()).items())),
            "directed_slides": len(loads), "exchange_transitions": transitions,
            "two_component_forests": len(forest_cache),
            "all_three_stationarity_checks": True, "holding_at_least_half": True,
            "connected": True, "route_and_forest_reconstruction": True,
            "exact_load_count_formula": True, "max_route_length": max_length,
            "max_length_weighted_load_without_uniform_factor": str(max_load),
            "universal_load_bound": str(Fraction(n - 2, 4)),
            "measured_comparison_congestion": str(comparison),
            "universal_comparison_bound": d * (n - 2),
            "proved_gap_lower_bound": str(Fraction(1, r * d * (n - 2)))}


def evaluate(n, word):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def hurwitz(word, i, sign):
    a, b = word[i:i + 2]
    def conjugate(e, t):
        return edge(*(t[1] if x == t[0] else t[0] if x == t[1] else x
                      for x in e))
    pair = (b, conjugate(a, b)) if sign == 1 else (conjugate(b, a), a)
    return word[:i] + pair + word[i + 2:]


def circuit_witness():
    # One-based words in proof.md, translated to zero-based here.
    w = ((0, 2), (0, 1), (2, 3))
    z = ((0, 2), (2, 3), (0, 1))
    assert tree(w) == tree(z) and w != z
    assert evaluate(4, w) == evaluate(4, z) == (1, 2, 3, 0)
    rows = []
    for word in (w, z):
        row = Counter(tree(hurwitz(word, i, sign))
                      for i in range(2) for sign in (-1, 1))
        rows.append(row)
    assert rows[0] != rows[1]
    return {"words": [w, z], "product": evaluate(4, w),
            "same_ordinary_support": True,
            "different_projected_Hurwitz_rows": True,
            "projected_rows_numerators_denominator_4":
            [{str(k): v for k, v in sorted(row.items())} for row in rows]}


def main():
    here = Path(__file__).resolve().parent
    cases = [check_n(n) for n in range(1, 7)]
    results = {
        "metadata": {
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"],
                                               text=True).strip(),
            "python": platform.python_version(), "dependencies": "stdlib only",
            "command": "python3 -B experiments/20261014-tree-slides/check.py",
            "seed": 0, "stochastic_draws": 0,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "parameters": {"N": list(range(1, 7)), "laziness": "1/2"},
            "scope": "exact finite validation; asymptotic proof is in proof.md"},
        "tree_cases": cases, "circuit_forgetting_witness": circuit_witness()}
    (here / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    for case in cases:
        print(json.dumps(case, sort_keys=True))
    print("PASS: all exact tree and circuit-obstruction checks")


if __name__ == "__main__":
    main()
