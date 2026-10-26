#!/usr/bin/env python3
"""Exact finite graph checks for bounded-endpoint single-coordinate refresh.

Only Python's standard library is required. No MCMC estimate is used as
evidence for a gap bound. Products act rightmost first.
"""
from array import array
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import random
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SEEDS = (20261026, 20261027)


def compose(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def cycles(p):
    seen = set()
    lengths = []
    for x in range(len(p)):
        if x in seen:
            continue
        y, length = x, 0
        while y not in seen:
            seen.add(y)
            length += 1
            y = p[y]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


class Group:
    def __init__(self, n):
        self.n = n
        self.edges = list(combinations(range(n), 2))
        self.M = len(self.edges)
        self.perms = list(permutations(range(n)))
        self.index = {p: i for i, p in enumerate(self.perms)}
        self.types = [cycles(p) for p in self.perms]
        self.defects = [n-len(t) for t in self.types]
        self.next = []
        for p in self.perms:
            row = []
            for a, b in self.edges:
                q = list(p)
                q[a], q[b] = q[b], q[a]
                row.append(self.index[tuple(q)])
            self.next.append(row)

    def endpoints(self, m):
        row = array('I', [0])
        for _ in range(m):
            row = array('I', (q for p in row for q in self.next[p]))
        return row

    def decode(self, code, m):
        word = [0]*m
        for i in range(m-1, -1, -1):
            code, word[i] = divmod(code, self.M)
        return word


def graph(G, m, k):
    ends = G.endpoints(m)
    codes = [c for c, p in enumerate(ends) if G.defects[p] <= k]
    index = array('i', [-1])*len(ends)
    for v, code in enumerate(codes):
        index[code] = v
    powers = [G.M**(m-1-i) for i in range(m)]
    rows = []
    changed_by_coordinate = [0]*m
    for code in codes:
        row = array('I')
        for i, power in enumerate(powers):
            old = (code//power) % G.M
            for new in range(G.M):
                if old == new:
                    continue
                dst = index[code+(new-old)*power]
                if dst >= 0:
                    row.append(dst)
                    changed_by_coordinate[i] += 1
        rows.append(row)
    return ends, codes, index, rows, changed_by_coordinate


def components(rows):
    seen = bytearray(len(rows))
    sizes = []
    for root in range(len(rows)):
        if seen[root]:
            continue
        todo = [root]
        seen[root] = 1
        count = 0
        while todo:
            x = todo.pop()
            count += 1
            for y in rows[x]:
                if not seen[y]:
                    seen[y] = 1
                    todo.append(y)
        sizes.append(count)
    return sorted(sizes, reverse=True)


def exact_diagnostics(G, m, ends, codes):
    endpoint = Counter()
    prefixes = [Counter() for _ in range(m+1)]
    position_edges = [Counter() for _ in range(m)]
    repeats, multiplicities, support, windows = Counter(), Counter(), Counter(), Counter()
    for code in codes:
        word = G.decode(code, m)
        p = 0
        prefixes[0][str(G.types[p])] += 1
        for i, t in enumerate(word):
            p = G.next[p][t]
            prefixes[i+1][str(G.types[p])] += 1
            position_edges[i][str(G.edges[t])] += 1
        assert p == ends[code]
        endpoint[str(G.types[p])] += 1
        repeats[sum(a == b for a, b in zip(word, word[1:]))] += 1
        multiplicities[str(tuple(sorted(Counter(word).values(), reverse=True)))] += 1
        parent = list(range(G.n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        for t in word:
            a, b = G.edges[t]
            parent[find(a)] = find(b)
        vertices, weights = Counter(find(a) for a in range(G.n)), Counter()
        for t in word:
            weights[find(G.edges[t][0])] += 1
        profile = tuple(sorted((v, weights[r]) for r, v in vertices.items()))
        support[str(profile)] += 1
        for i in range(m-1):
            q = G.next[G.next[0][word[i]]][word[i+1]]
            windows[str(G.types[q])] += 1
    if codes and G.M:
        for freq in position_edges:
            assert len(set(freq.values())) <= 1
    return {'endpoint_cycle_types':dict(endpoint),
            'prefix_cycle_types':[dict(x) for x in prefixes],
            'position_edge_counts':[dict(x) for x in position_edges],
            'adjacent_repeats':dict(repeats), 'edge_multiplicities':dict(multiplicities),
            'weighted_support_profiles':dict(support), 'length_two_window_types':dict(windows)}


def rayleigh_probes(rows, denominator, iterations):
    """Power iteration yields gap UPPER approximations, never lower bounds."""
    size = len(rows)
    if size <= 1:
        return []
    degree = [len(r) for r in rows]
    out = []
    for seed in SEEDS:
        rng = random.Random(seed)
        v = [rng.uniform(-1, 1) for _ in rows]
        for step in range(iterations+1):
            mean = sum(v)/size
            v = [x-mean for x in v]
            norm = math.sqrt(sum(x*x for x in v))
            v = [x/norm for x in v]
            # K=I-L/(2mM); graph edges count every distinct accepted replacement.
            z = [v[i]+(sum(v[j] for j in row)-degree[i]*v[i])/denominator
                 for i, row in enumerate(rows)]
            if step == iterations:
                lam = sum(a*b for a, b in zip(v, z))
                residual = math.sqrt(sum((b-lam*a)**2 for a, b in zip(v, z)))
                out.append({'seed':seed, 'iterations':iterations,
                            'gap_rayleigh_upper_estimate':1-lam,
                            'eigen_residual_l2':residual,
                            'certified_gap_lower_bound':False})
            else:
                v = z
    return out


def run_case(n, m, k, iterations):
    start = time.monotonic()
    G = Group(n)
    ends, codes, index, rows, coordinate_counts = graph(G, m, k)
    size = len(codes)
    comp = components(rows)
    denominator = 2*m*G.M if m else 1
    # Every off-diagonal probability is exactly 1/(2mM).
    reverse_checks = 0
    rowsets = [set(r) for r in rows]
    for i, row in enumerate(rows):
        assert len(row) == len(rowsets[i])
        assert denominator-len(row) >= denominator//2
        for j in row:
            assert i in rowsets[j]
            reverse_checks += 1
    del rowsets
    assert len(set(coordinate_counts)) <= 1
    identity_vertices = [i for i, c in enumerate(codes) if ends[c] == 0]
    distances = [-1]*size
    todo = deque(identity_vertices)
    for i in todo:
        distances[i] = 0
    while todo:
        i = todo.popleft()
        for j in rows[i]:
            if distances[j] < 0:
                distances[j] = distances[i]+1
                todo.append(j)
    # Exact stationary flux for simple candidate bottlenecks.
    cuts = {}
    for name, members in [
            ('exact_endpoint', set(identity_vertices)),
            ('endpoint_fixes_label_0', {i for i, c in enumerate(codes)
                                      if G.perms[ends[c]][0] == 0}),
            ('first_gate_contains_label_0', {i for i, c in enumerate(codes)
                  if m and 0 in G.edges[G.decode(c, m)[0]]})]:
        if 0 < len(members) < size:
            boundary = sum(sum(j not in members for j in rows[i]) for i in members)
            cuts[name] = {'size':len(members), 'boundary_directed_edges':boundary,
                         'conductance_min_side':str(Fraction(boundary,
                                                  denominator*min(len(members), size-len(members)))),
                         'indicator_rayleigh':str(Fraction(boundary*size,
                                                  denominator*len(members)*(size-len(members))))}
    ans = {'kind':'finite_graph', 'N':n, 'm':m, 'k':k,
           'all_words':len(ends), 'allowed_words':size, 'identity_words':len(identity_vertices),
           'component_count':len(comp), 'largest_components':comp[:10],
           'isolated_vertices':sum(not r for r in rows),
           'checked_directed_edges':reverse_checks,
           'distinct_move_probability_mean':str(Fraction(reverse_checks, size*denominator)) if size else None,
           'min_degree':min(map(len, rows), default=0), 'max_degree':max(map(len, rows), default=0),
           'distance_to_identity_histogram':dict(Counter(distances)), 'cuts':cuts,
           'diagnostics':exact_diagnostics(G, m, ends, codes),
           'spectral_probes':rayleigh_probes(rows, denominator, iterations) if iterations and len(comp)==1 else [],
           'seconds':time.monotonic()-start}
    if m and size == len(ends) and G.M > 1:
        ans['proved_unrestricted_gap'] = str(Fraction(1, 2*m))
    return ans


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--iterations', type=int, default=0)
    parser.add_argument('--case', action='append', help='N,m,k; repeatable')
    parser.add_argument('--output', type=Path, default=HERE/'results.jsonl')
    args = parser.parse_args()
    cases = [tuple(map(int, s.split(','))) for s in args.case] if args.case else [
        (2,0,0), (2,2,0), (2,3,0), (2,3,1),
        (3,2,0), (3,2,2), (3,3,1), (3,4,0), (3,4,1), (3,4,2),
        (4,4,2), (4,6,2), (5,4,2), (6,4,2)]
    manifest = {'kind':'manifest', 'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                'python':platform.python_version(), 'dependencies':'standard library only',
                'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'command':['python3','-B',str(Path(__file__).relative_to(ROOT))]+__import__('sys').argv[1:],
                'seeds':list(SEEDS), 'cases':cases}
    with args.output.open('w') as out:
        out.write(json.dumps(manifest, sort_keys=True)+'\n')
        out.flush()
        for case in cases:
            ans = run_case(*case, args.iterations)
            out.write(json.dumps(ans, sort_keys=True)+'\n')
            out.flush()
            print(json.dumps({key:ans[key] for key in ['N','m','k','allowed_words','identity_words',
                              'component_count','min_degree','max_degree','spectral_probes','seconds']}), flush=True)


if __name__ == '__main__':
    main()
