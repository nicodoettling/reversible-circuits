"""Deterministic falsification checks; no finite test certifies asymptotics."""
import itertools
import json
import math
import platform
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def setup(n):
    edges = list(itertools.combinations(range(n), 2))
    perms = []
    for a, b in edges:
        p = list(range(n))
        p[a], p[b] = p[b], p[a]
        perms.append(tuple(p))
    return edges, perms


def product(word, perms, n):
    p = tuple(range(n))
    for t in word:
        p = compose(p, perms[t])
    return p


def components(word, edges, n):
    parent = list(range(n))

    def root(a):
        while a != parent[a]:
            a = parent[a]
        return a

    for t in word:
        a, b = edges[t]
        parent[root(a)] = root(b)
    vertices, gates = defaultdict(list), defaultdict(list)
    for a in range(n):
        vertices[root(a)].append(a)
    for j, t in enumerate(word):
        gates[root(edges[t][0])].append(j)
    return [(tuple(v), tuple(gates[r])) for r, v in vertices.items()]


def face_count(word, edges):
    rotations = defaultdict(list)
    for j, t in enumerate(word):
        a, b = edges[t]
        rotations[a].append(2*j)
        rotations[b].append(2*j+1)
    sigma = {}
    for darts in rotations.values():
        for x, y in zip(darts, darts[1:] + darts[:1]):
            sigma[x] = y
    unseen = set(sigma)
    faces = 0
    while unseen:
        x = next(iter(unseen))
        faces += 1
        while x in unseen:
            unseen.remove(x)
            x = sigma[x ^ 1]
    return faces


def finite_fibers(n, m, check_blocks=False):
    edges, perms = setup(n)
    d = len(edges)
    words = list(itertools.product(range(d), repeat=m))
    endpoints = [product(w, perms, n) for w in words]
    index = {w: i for i, w in enumerate(words)}
    pair_fibers = defaultdict(list)
    for pair in itertools.product(range(d), repeat=2):
        pair_fibers[product(pair, perms, n)].append(pair)
    parent = list(range(len(words)))

    def root(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for i, w in enumerate(words):
        for j in range(m-1):
            for pair in pair_fibers[product(w[j:j+2], perms, n)]:
                z = w[:j] + pair + w[j+2:]
                q = index[z]
                assert endpoints[i] == endpoints[q]
                parent[root(i)] = root(q)
    roots_by_endpoint = defaultdict(set)
    for i, g in enumerate(endpoints):
        roots_by_endpoint[g].add(root(i))
    assert all(len(rs) == 1 for rs in roots_by_endpoint.values())
    identity = tuple(range(n))
    bridges = [w for w, g in zip(words, endpoints) if g == identity]
    sizes, profiles = {}, {}
    minimal_connected = 0
    for w in bridges:
        comps = components(w, edges, n)
        sizes[w] = max((len(js)//2 for _, js in comps), default=0)
        profiles[w] = tuple(sorted((v, len(js)) for v, js in comps))
        for v, js in comps:
            if not js:
                continue
            subword = tuple(w[j] for j in js)
            assert product(subword, perms, n) == identity
            assert len(js) % 2 == 0 and len(js) >= 2*(len(v)-1)
            assert face_count(subword, edges) == len(v)
            genus = len(js)//2 + 1 - len(v)
            assert genus >= 0
            minimal_connected += genus == 0
    flows = {}
    if bridges and m >= 2:
        for kernel, lengths in [('pair', [2])]+(
                [('project', [r for r in (3, 4, 5) if r <= m])]
                if check_blocks else []):
            cut_flow = [Fraction(0) for _ in range(m//2)]
            profile_changes = 0
            for r in lengths:
                coefficient = Fraction(1, 2*len(lengths)*(m-r+1)*len(bridges))
                for j in range(m-r+1):
                    fibers = defaultdict(list)
                    for w in bridges:
                        fibers[(w[:j], w[j+r:])].append(w)
                    for fiber in fibers.values():
                        profile_changes += len({profiles[w] for w in fiber}) > 1
                        for cap in range(1, m//2):
                            inside = [w for w in fiber if sizes[w] <= cap]
                            outside_count = len(fiber)-len(inside)
                            cut_flow[cap] += coefficient*Fraction(
                                len(inside)*outside_count, len(fiber))
                            if outside_count:
                                threshold = (Fraction(cap)-Fraction(r, 2))/(r+1)
                                assert all(sizes[w] > threshold for w in inside)
                                if r == 2:
                                    assert all(sizes[w] >= Fraction(cap, 2) for w in inside)
            flows[kernel] = {
                'crosses_profiles': bool(profile_changes),
                'cuts': [{'cap': cap, 'mass': str(Fraction(
                    sum(sizes[w] <= cap for w in bridges), len(bridges))),
                    'flow': str(cut_flow[cap])} for cap in range(1, m//2)]}
    emit(test='finite_fibers', N=n, m=m, words=len(words),
         endpoints=len(roots_by_endpoint), all_endpoint_fibers_connected=True,
         identity_words=len(bridges), map_genus_checks=True,
         genus_zero_component_occurrences=minimal_connected, kernels=flows)


@lru_cache(None)
def return_counts(n, length):
    if n < 2:
        return int(length == 0)
    _, perms = setup(n)
    identity = tuple(range(n))
    counts = {identity: 1}
    for _ in range(length):
        next_counts = defaultdict(int)
        for p, count in counts.items():
            for t in perms:
                next_counts[compose(p, t)] += count
        counts = next_counts
    return counts.get(identity, 0)


@lru_cache(None)
def connected(v, length):
    if v < 2 or length < 2*(v-1) or length % 2:
        return 0
    count = return_counts(v, length)-return_counts(v-1, length)
    for s in range(2, v+1):
        for ell in range(2, length+1, 2):
            if (s, ell) == (v, length):
                continue
            count -= (math.comb(v-1, s-1)*math.comb(length, ell)
                      *connected(s, ell)*return_counts(v-s, length-ell))
    assert count >= 0
    return count


@lru_cache(None)
def capped(n, length, cap):
    if length == 0:
        return 1
    if n < 2 or length % 2:
        return 0
    count = capped(n-1, length, cap)
    for ell in range(2, min(length, 2*cap)+1, 2):
        for v in range(2, min(n, ell//2+1)+1):
            count += (math.comb(n-1, v-1)*math.comb(length, ell)
                      *connected(v, ell)*capped(n-v, length-ell, cap))
    return count


def disjoint(n, k):
    if n < 2*k:
        return 0
    return math.factorial(n)//math.factorial(n-2*k)*math.factorial(2*k)//(4**k*math.factorial(k))


def switching_checks():
    for n in (2, 3, 4, 5):
        for m in (0, 2, 4, 6, 8):
            assert capped(n, m, m//2) == return_counts(n, m)
    tested = 0
    worst = Fraction(0)
    for n in (32, 40, 64):
        for m in (4, 6, 8):
            assert capped(n, m, 1) == disjoint(n, m//2)
            for cap in range(2, m//2+1):
                for k in range(2, cap+1):
                    numerator = sum(math.comb(n, v)*math.comb(m, 2*k)
                        *connected(v, 2*k)*capped(n-v, m-2*k, cap)
                        for v in range(2, k+2))
                    moment = Fraction(numerator, capped(n, m, cap))
                    upper = math.comb(m//2, k)*max(Fraction(
                        sum(math.comb(a, v)*connected(v, 2*k)
                            for v in range(2, k+2)), disjoint(a, k))
                        for a in range(n-2*m, n+1))
                    assert moment <= upper
                    worst = max(worst, moment/upper)
                    tested += 1
    emit(test='switching', exact_conditional_moments_tested=tested,
         N=[32, 40, 64], m=[4, 6, 8], max_actual_over_bound=str(worst),
         component_assembly_matches_group_DP=True)


if __name__ == '__main__':
    emit(test='manifest', python=platform.python_version(), seed=0,
         stochastic=False, dependencies='standard library only',
         commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
         command='python3 -B experiments/20261124-conductance-audit/check.py > experiments/20261124-conductance-audit/results.jsonl')
    for n, m in [(2, 0), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3),
                 (3, 4), (3, 6), (4, 4), (4, 6)]:
        finite_fibers(n, m, check_blocks=m >= 4)
    switching_checks()
    emit(test='summary', verdict='all exact checks passed; asymptotic proof separate')
