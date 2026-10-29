#!/usr/bin/env python3
"""Deterministic exact falsification checks; Python standard library only."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import platform
import subprocess


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def alphabet(n, triples=False):
    edges = [e for e in combinations(range(n), 2)
             if not triples or e[0] // 3 == e[1] // 3]
    gates = []
    for u, v in edges:
        p = list(range(n))
        p[u], p[v] = p[v], p[u]
        gates.append(tuple(p))
    return edges, gates


def words(gates, m):
    identity = tuple(range(len(gates[0])))
    if m == 0:
        return [()]
    if m % 2:
        return []
    index = {g: i for i, g in enumerate(gates)}
    out = []
    for prefix in product(range(len(gates)), repeat=m - 1):
        p = identity
        for a in prefix:
            p = compose(p, gates[a])
        if p in index:  # the last transposition must equal the prefix product
            out.append(prefix + (index[p],))
    return out


def tables(gates):
    index = {g: i for i, g in enumerate(gates)}
    h, hi, fibers = {}, {}, defaultdict(list)
    for a, b in product(range(len(gates)), repeat=2):
        ab = compose(gates[a], gates[b])
        fibers[ab].append((a, b))
        h[a, b] = (b, index[compose(gates[b], ab)])
        hi[a, b] = (index[compose(ab, gates[a])], a)
    return h, hi, fibers


def rows(states, q, h, hi):
    m = len(states[0])
    # General alphabet q: denominator 8*q*(m-1).
    den = 8 * q * (m - 1)
    out = {}
    for w in states:
        row = Counter({w: den // 2})
        for i in range(m - 1):
            a, b = w[i:i + 2]
            for table in (h, hi):
                pair = table[a, b]
                row[w[:i] + pair + w[i + 2:]] += q
            if a == b:
                for s in range(q):
                    row[w[:i] + (s, s) + w[i + 2:]] += 2
            else:
                row[w] += 2 * q
        assert sum(row.values()) == den
        out[w] = row
    return den, out


def cycle_type(p):
    seen, sizes = set(), []
    for i in range(len(p)):
        if i not in seen:
            j, size = i, 0
            while j not in seen:
                seen.add(j)
                size += 1
                j = p[j]
            sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def signature(w, edges, n):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a in w:
        u, v = edges[a]
        parent[find(u)] = find(v)
    vertices = defaultdict(set)
    weights = Counter()
    for a in w:
        u, v = edges[a]
        root = find(u)
        vertices[root].update((u, v))
        weights[root] += 1
    return tuple(sorted((tuple(sorted(vs)), weights[r])
                        for r, vs in vertices.items()))


def compositions(total, k):
    if k == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, k - 1):
                yield (first,) + tail


def g(r):
    return 0 if r == 0 else 6 if r == 1 else 2 * r * (2 * r - 1)


def move(c, j, h):
    d = list(c)
    d[j] -= 1
    d[h] += 1
    return tuple(d)


def check_count_coupling():
    cases = 0
    for k in (2, 3, 4):
        for total in range(1, 6):
            for c in compositions(total, k):
                for u, v in product(range(k), repeat=2):
                    if u == v or not c[u]:
                        continue
                    d = move(c, u, v)
                    # c-d=e_u-e_v; all rates below are multiplied by k.
                    joint = Counter()
                    for j, dest in product(range(k), repeat=2):
                        rate = min(g(c[j]), g(d[j]))
                        if rate:
                            joint[move(c, j, dest), move(d, j, dest)] += rate
                    a, b = g(c[u]) - g(d[u]), g(d[v]) - g(c[v])
                    assert min(a, b) >= 6
                    for dest in range(k):
                        joint[move(c, u, dest), move(d, v, dest)] += min(a, b)
                        if a > b:
                            joint[move(c, u, dest), d] += a - b
                        if b > a:
                            joint[c, move(d, v, dest)] += b - a
                    marginals = (Counter(), Counter())
                    drift = 0
                    for (x, y), rate in joint.items():
                        distance = sum(abs(xx - yy) for xx, yy in zip(x, y)) // 2
                        assert distance <= 1
                        drift += rate * (distance - 1)
                        if x != c:
                            marginals[0][x] += rate
                        if y != d:
                            marginals[1][y] += rate
                    assert drift <= -6 * k
                    for start, marginal in zip((c, d), marginals):
                        expected = Counter()
                        for j, dest in product(range(k), repeat=2):
                            if start[j] and j != dest:
                                expected[move(start, j, dest)] += g(start[j])
                        assert marginal == expected
                    cases += 1
    return {"neighbor_couplings": cases, "marginals_exact": True,
            "distance_drift_at_most_minus_6": True}


def check_case(n, m, triples=False, shuttles=False):
    edges, gates = alphabet(n, triples)
    q = len(gates)
    states = words(gates, m)
    h, hi, pair_fibers = tables(gates)
    den, transitions = rows(states, q, h, hi)
    identity = tuple(range(n))
    diagnostics = {name: Counter() for name in
                   ("prefix_cycle_types", "edge_multiplicities", "adjacent_repeats",
                    "weighted_support", "window_product_types")}
    position_edges = [Counter() for _ in range(m)]
    sig = {}
    for w in states:
        p = identity
        for i, a in enumerate(w):
            p = compose(p, gates[a])
            diagnostics["prefix_cycle_types"][str((i + 1, cycle_type(p)))] += 1
            position_edges[i][a] += 1
        assert p == identity
        sig[w] = signature(w, edges, n)
        diagnostics["weighted_support"][str(sig[w])] += 1
        diagnostics["edge_multiplicities"][str(tuple(sorted(Counter(w).values())))] += 1
        diagnostics["adjacent_repeats"][sum(a == b for a, b in zip(w, w[1:]))] += 1
        for a, b in zip(w, w[1:]):
            diagnostics["window_product_types"][str(cycle_type(compose(gates[a], gates[b])))] += 1
        for target, weight in transitions[w].items():
            assert target in transitions
            assert transitions[target][w] == weight
    assert all(set(c.values()) == {len(states) // q} and len(c) == q
               for c in position_edges)
    crosses = sum(sig[w] != sig[y] for w in states for y in transitions[w])
    # Signed Hurwitz must preserve weighted support, independently of refresh.
    for w in states:
        for i in range(m - 1):
            for table in (h, hi):
                y = w[:i] + table[w[i], w[i + 1]] + w[i + 2:]
                assert sig[w] == sig[y]
    result = {"model": "product_S3" if triples else "all_transpositions",
              "N": n, "m": m, "states": len(states),
              "identity_and_exact_detailed_balance": True,
              "crosses_weighted_support_edges": crosses,
              "position_edge_count": len(states) // q,
              "diagnostics": {name: dict(hist) for name, hist in diagnostics.items()}}
    # Exact connectivity is only a finite check, never the asymptotic argument.
    visited, todo = {states[0]}, [states[0]]
    while todo:
        w = todo.pop()
        for y in transitions[w]:
            if y not in visited:
                visited.add(y)
                todo.append(y)
    assert len(visited) == len(states)
    result["connected"] = True
    if not triples:
        return result
    k = n // 3
    colors = [u // 3 for u, _ in edges]
    counts = {}
    classes = defaultdict(list)
    for w in states:
        ns = Counter(colors[a] for a in w)
        assert all(x % 2 == 0 for x in ns.values())
        c = tuple(ns[j] // 2 for j in range(k))
        counts[w] = c
        classes[c].append(w)
    projected = defaultdict(Counter)
    for w in states:
        for y, weight in transitions[w].items():
            projected[counts[w]][counts[y]] += weight
    for c, members in classes.items():
        expected_size = Fraction(factorial(m))
        for r in c:
            expected_size *= Fraction(1 if r == 0 else 3 ** (2 * r - 1), factorial(2 * r))
        assert expected_size == len(members)
        allowed = {c}
        for j, dest in product(range(k), repeat=2):
            if c[j] and j != dest:
                d = move(c, j, dest)
                allowed.add(d)
                assert m * projected[c][d] == 2 * g(c[j]) * len(members)
        assert set(projected[c]) == allowed
    result["count_classes"] = {str(c): len(xs) for c, xs in classes.items()}
    result["exact_projection_formula"] = True
    if shuttles:
        encoding = Counter()
        edge_load = Counter()
        routes = 0
        for w in states:
            positions = defaultdict(list)
            for i, a in enumerate(w):
                positions[colors[a]].append(i)
            for indexes in positions.values():
                for u, v in zip(indexes, indexes[1:]):
                    a, b = w[u], w[v]
                    possible = [pair for pair in pair_fibers[compose(gates[a], gates[b])]
                                if colors[pair[0]] == colors[a] and colors[pair[1]] == colors[a]]
                    assert len(possible) == 3
                    for ap, bp in possible:
                        if (ap, bp) == (a, b):
                            continue
                        path = [w]
                        z = list(w)
                        for i in range(u, v - 1):
                            z[i], z[i + 1] = z[i + 1], z[i]
                            path.append(tuple(z))
                        z[v - 1:v + 1] = ap, bp
                        path.append(tuple(z))
                        for i in range(v - 2, u - 1, -1):
                            z[i], z[i + 1] = z[i + 1], z[i]
                            path.append(tuple(z))
                        y = list(w)
                        y[u], y[v] = ap, bp
                        assert path[-1] == tuple(y)
                        length = len(path) - 1
                        assert length == 2 * (v - u - 1) + 1 <= 2 * m
                        for phase, (x, y) in enumerate(zip(path, path[1:])):
                            assert counts[x] == counts[w] == counts[y]
                            assert transitions[x][y] > 0
                            encoding[x, y, u, v, phase] += 1
                            edge_load[x, y] += length
                        routes += 1
        max_preimages = max(encoding.values(), default=0)
        assert max_preimages <= 3
        max_congestion = max((Fraction(load * den, 6 * m * transitions[x][y])
                              for (x, y), load in edge_load.items()), default=Fraction(0))
        assert max_congestion <= 12 * k * m ** 5
        result["shuttles"] = {"routes": routes, "max_encoding_preimages": max_preimages,
                              "max_B_congestion_exact": str(max_congestion),
                              "upper_bound": 12 * k * m ** 5,
                              "all_steps_legal_and_count_preserving": True}
    return result


def main():
    out = {"python": platform.python_version(), "dependencies": "standard library only",
           "seed": 20261013, "randomness": "none; exhaustive deterministic checks",
           "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
           "command": "python3 -B experiments/20261013-product-s3-mixing/check.py",
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "coupling": check_count_coupling(), "cases": []}
    for n, m, triples, shuttles in [(3, 4, False, False), (4, 4, False, False),
                                    (4, 6, False, False), (3, 2, True, True),
                                    (3, 6, True, True), (6, 2, True, True),
                                    (6, 4, True, True), (6, 6, True, True),
                                    (9, 4, True, True), (9, 6, True, False)]:
        result = check_case(n, m, triples, shuttles)
        out["cases"].append(result)
        print(json.dumps({key: result[key] for key in ("model", "N", "m", "states", "connected")}))
    for n, triples in ((2, False), (3, True), (6, True)):
        _, gates = alphabet(n, triples)
        assert words(gates, 0) == [()]
        assert words(gates, 1) == [] and words(gates, 3) == []
    _, gates = alphabet(2)
    assert len(words(gates, 6)) == 1
    out["boundary_checks"] = "pass: m=0, odd lengths, N=2 singleton, m=2, k=1, empty blocks"
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": "PASS", "coupling_cases": out["coupling"]["neighbor_couplings"]}))


if __name__ == "__main__":
    main()
