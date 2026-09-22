#!/usr/bin/env python3
"""Positive DYZ count table, exact component assembly, minimal DPS sampler.

DYZ: Proposition 1 equation (13), with C(d,k)=d! k! h[g,d].
DPS closure: Proposition 3/Theorem 5; implementation adapted from the cited
M112 dps_local_audit.py, with unrelated local-chain code excluded.
All validation below is exact except explicitly labeled seeded smoke draws.
Products are maps p after q; append a transposition by swapping p's entries.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, log
from pathlib import Path
import json
import platform
import random
import subprocess
import time


def binomial_table(n_max, k_max=None):
    k_max = n_max if k_max is None else k_max
    table = []
    for n in range(n_max+1):
        row = [1] + [0]*min(n,k_max)
        for k in range(1,len(row)):
            row[k] = table[n-1][k-1] + (table[n-1][k] if k < len(table[n-1]) else 0)
        table.append(row)
    return table


def connected_counts(n_max: int, m_max: int):
    """C[d][k], O(n_max**2 m_max**2) positive integer arithmetic."""
    C = [[0] * (m_max + 1) for _ in range(n_max + 1)]
    if n_max:
        C[1][0] = 1
    choose = binomial_table(m_max)
    choose_degree = binomial_table(n_max,min(n_max,m_max//2+1))
    max_degree = min(n_max,m_max//2+1)
    powers = [[1]*(m_max+2) for _ in range(max_degree+1)]
    for a in range(1,max_degree+1):
        for r in range(1,m_max+2):
            powers[a][r] = powers[a][r-1]*a
    for d in range(2,max_degree+1):
        numerator = [0] * (m_max + 1)
        for a in range(1, d):
            b = d - a
            binconv = [0] * (m_max + 1)
            for j, x in enumerate(C[a]):
                if not x:
                    continue
                for h, y in enumerate(C[b][:m_max - j + 1]):
                    if y:
                        binconv[j + h] += choose[j + h][j] * x * y
            prefactor = 2 * choose_degree[d][a] * b * b
            for s, value in enumerate(binconv):
                if not value:
                    continue
                for r in range(2, m_max - s + 1, 2):
                    numerator[s + r] += (
                        prefactor * choose[s + r][r] * powers[a][r+1] * value
                    )
        divisor = d * d * (d - 1)
        for k, value in enumerate(numerator):
            C[d][k], remainder = divmod(value, divisor)
            assert remainder == 0, (d, k, value, divisor)
    return C


def assembly_counts(n_max: int, m_max: int, C, allowed=None):
    """Least-label recursion; allowed(v,k) declares an optional subset."""
    Z = [[0] * (m_max + 1) for _ in range(n_max + 1)]
    Z[0][0] = 1
    choose_labels = binomial_table(n_max,min(n_max,m_max//2+1))
    choose_positions = binomial_table(m_max)
    for n in range(1, n_max + 1):
        for k in range(m_max + 1):
            total = 0
            for v in range(1, min(n, len(C) - 1) + 1):
                for ell in range(k + 1):
                    cv = C[v][ell]
                    if cv and (allowed is None or allowed(v, ell)):
                        total += choose_labels[n-1][v-1] * choose_positions[k][ell] * cv * Z[n-v][k-ell]
            Z[n][k] = total
    return Z


def minimal_allowed(v, k):
    return k == 2 * (v - 1)


def evaluate(n, word):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def support_macro(n, word):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in word:
        parent[root(a)] = root(b)
    blocks = defaultdict(list)
    for x in range(n):
        blocks[root(x)].append(x)
    counts = Counter(root(a) for a, _ in word)
    return tuple(sorted((tuple(B), counts[r]) for r, B in blocks.items()))


def identity_words(n, m):
    edges = tuple(combinations(range(n), 2))
    identity = tuple(range(n))
    for word in product(edges, repeat=m):
        if evaluate(n, word) == identity:
            yield word


def marked_step(q, partition, edge):
    a,b = edge
    new_q = list(q)
    new_q[a],new_q[b] = new_q[b],new_q[a]
    old,new = partition[b],partition[a]
    merged = [new if x == old else x for x in partition]
    canonical = {}
    new_partition = []
    for block in merged:
        if block not in canonical:
            canonical[block] = len(canonical)
        new_partition.append(canonical[block])
    return tuple(new_q),tuple(new_partition)


def marked_completion_counter(n):
    """Connected backward DP on (permutation, exposed support partition)."""
    edges = tuple(combinations(range(n),2))
    identity = tuple(range(n))
    @lru_cache(None)
    def count(r,q,partition):
        if not r:
            return int(q == identity and len(set(partition)) == 1)
        return sum(count(r-1,*marked_step(q,partition,edge)) for edge in edges)
    return count


def sample_connected_marked(n,m,rng):
    count = marked_completion_counter(n)
    q,partition = tuple(range(n)),tuple(range(n))
    if not count(m,q,partition):
        raise ValueError('connected identity fiber is empty')
    word = []
    for r in range(m,0,-1):
        options = [(edge,count(r-1,*marked_step(q,partition,edge)))
                   for edge in combinations(range(n),2)]
        edge = weighted_choice(options,rng)
        word.append(edge)
        q,partition = marked_step(q,partition,edge)
    assert count(0,q,partition) == 1
    return tuple(word)


def assembly_word_probability(n, word, C, Z):
    """Probability computed from each literal least-label branch."""
    remaining = list(range(n))
    k = len(word)
    probability = Fraction(1)
    macro = support_macro(n, word)
    by_label = {x: (B, ell) for B, ell in macro for x in B}
    while remaining:
        B, ell = by_label[remaining[0]]
        v, n_current = len(B), len(remaining)
        weight = comb(n_current-1,v-1) * comb(k,ell) * C[v][ell] * Z[n_current-v][k-ell]
        probability *= Fraction(weight, Z[n_current][k])
        probability *= Fraction(1, comb(n_current-1,v-1))
        probability *= Fraction(1, comb(k,ell))
        probability *= Fraction(1, C[v][ell])
        remaining = [x for x in remaining if x not in B]
        k -= ell
    assert k == 0
    return probability


@dataclass(frozen=True)
class Half:
    color: str
    vertex: int
    label: int


@dataclass(frozen=True)
class Side:
    kind: str


def prufer_tree(d, code):
    """Simple O(d²) decoder; labels 1 through d."""
    if d == 1:
        return frozenset()
    degree = [0] + [1] * d
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(1, d+1) if degree[i] == 1)
        edges.append(tuple(sorted((leaf,x))))
        degree[leaf] -= 1
        degree[x] -= 1
    edges.append(tuple(i for i in range(1,d+1) if degree[i] == 1))
    return frozenset(edges)


def dps_word(tree, pi, d):
    """Accepted DPS rooted-product closure, conservative O(d^4) time."""
    if d == 1:
        return ()
    adjacency = defaultdict(list)
    for a,b in tree:
        adjacency[a].append(b)
        adjacency[b].append(a)
    parent, todo = {d:0}, [d]
    while todo:
        a = todo.pop()
        for b in adjacency[a]:
            if b not in parent:
                parent[b] = a
                todo.append(b)
    incidence = defaultdict(dict)
    black_of_label = {}
    for i in range(1,d):
        for lab,white in zip(pi[2*i-2:2*i], (i,parent[i])):
            incidence['b',i][lab] = ('w',white)
            incidence['w',white][lab] = ('b',i)
            black_of_label[lab] = i
    m = 2*d-2
    start = (('w',1),1)
    state, seen, tokens = start, set(), []
    while state not in seen:
        seen.add(state)
        vertex, incoming = state
        color, idx = vertex
        lab = 1 + ((incoming-1 + (1 if color == 'w' else -1)) % m)
        if lab in incidence[vertex]:
            tokens.append(Side('tree'))
            state = (incidence[vertex][lab],lab)
        else:
            tokens.append(Half(color,idx,lab))
            state = (vertex,lab)
    assert state == start and len(tokens) == (2*d-1)*m
    other_black = {}
    while True:
        positions = [i for i,x in enumerate(tokens) if isinstance(x,Half)]
        pair = None
        for j,wi in enumerate(positions):
            bj = positions[(j+1) % len(positions)]
            if tokens[wi].color == 'w' and tokens[bj].color == 'b':
                pair = wi,bj
                break
        if pair is None:
            break
        wi,bj = pair
        tokens = tokens[wi:] + tokens[:wi]
        bj = (bj-wi) % len(tokens)
        w,b = tokens[0],tokens[bj]
        assert w.label == b.label
        distance = sum(isinstance(x,Side) for x in tokens[1:bj])
        assert distance in (1,3)
        if distance == 3:
            assert w.label not in other_black
            other_black[w.label] = b.vertex
        tokens = [Side('closure')] + tokens[bj+1:]
    remaining = [x for x in tokens if isinstance(x,Half)]
    assert len(remaining) == m and all(x.color == 'w' for x in remaining)
    assert sorted(x.label for x in remaining) == list(range(1,m+1))
    word = tuple(tuple(sorted((black_of_label[lab]-1,other_black.get(lab,d)-1)))
                 for lab in range(1,m+1))
    assert all(a != b for a,b in word)
    return word


def sample_minimal_connected(d, rng):
    if d == 1:
        return ()
    tree = prufer_tree(d, [rng.randrange(1,d+1) for _ in range(d-2)])
    pi = list(range(1,2*d-1))
    rng.shuffle(pi)
    return dps_word(tree,pi,d)


def weighted_choice(options, rng):
    draw = rng.randrange(sum(weight for _,weight in options))
    for item,weight in options:
        if draw < weight:
            return item
        draw -= weight
    raise AssertionError('unreachable')


def sample_minimal_assembly(labels, m, C, Z0, rng):
    """Exact conditional all-minimal law; raises on an empty subset."""
    n = len(labels)
    if not Z0[n][m]:
        raise ValueError('all-minimal subset is empty')
    labels = list(labels)
    positions = list(range(m))
    result = [None] * m
    while labels:
        n,k = len(labels),len(positions)
        options = []
        for v in range(1,min(n,len(C)-1)+1):
            ell = 2*(v-1)
            if ell <= k:
                weight = comb(n-1,v-1)*comb(k,ell)*C[v][ell]*Z0[n-v][k-ell]
                if weight:
                    options.append(((v,ell),weight))
        v,ell = weighted_choice(options,rng)
        B = [labels[0]] + sorted(rng.sample(labels[1:],v-1))
        Bset = set(B)
        chosen_positions = sorted(rng.sample(positions,ell))
        chosen_set = set(chosen_positions)
        internal = tuple((B[a],B[b]) for a,b in sample_minimal_connected(v,rng))
        for j,edge in zip(chosen_positions,internal):
            result[j] = edge
        labels = [x for x in labels if x not in Bset]
        positions = [j for j in positions if j not in chosen_set]
    assert not positions and all(edge is not None for edge in result)
    return tuple(result)


def exact_checks(C,Z,Z0):
    results = []
    for n,m in [(1,0),(1,2),(2,0),(2,2),(2,4),(3,0),(3,1),(3,2),(3,4),(4,4),(4,6)]:
        words = list(identity_words(n,m))
        macro_counts = Counter(support_macro(n,w) for w in words)
        failures = []
        for macro,count in macro_counts.items():
            predicted = Fraction(factorial(m))
            for B,k in macro:
                predicted *= Fraction(C[len(B)][k],factorial(k))
            if predicted != count:
                failures.append(('macro',str(macro),count,str(predicted)))
        probabilities = Counter(assembly_word_probability(n,w,C,Z) for w in words)
        minimal_words = [w for w in words if all(minimal_allowed(len(B),k) for B,k in support_macro(n,w))]
        genus_histogram = Counter(sum(k//2-len(B)+1 for B,k in support_macro(n,w)) for w in words)
        minimal_probabilities = Counter(assembly_word_probability(n,w,C,Z0) for w in minimal_words)
        connected = sum(len(support_macro(n,w)) == 1 for w in words) if n else 0
        marked_count = marked_completion_counter(n)
        start = tuple(range(n))
        assert marked_count(m,start,start) == connected
        connected_probabilities = Counter()
        for w in words:
            if len(support_macro(n,w)) != 1:
                continue
            q,partition = start,start
            probability = Fraction(1)
            for j,edge in enumerate(w):
                next_q,next_partition = marked_step(q,partition,edge)
                probability *= Fraction(marked_count(m-j-1,next_q,next_partition),
                                        marked_count(m-j,q,partition))
                q,partition = next_q,next_partition
            connected_probabilities[probability] += 1
        assert not connected or connected_probabilities == {Fraction(1,connected):connected}
        assert Z[n][m] == len(words)
        assert Z0[n][m] == len(minimal_words)
        assert C[n][m] == connected
        assert not failures
        assert not words or probabilities == {Fraction(1,len(words)):len(words)}
        assert not minimal_words or minimal_probabilities == {Fraction(1,len(minimal_words)):len(minimal_words)}
        results.append(dict(N=n,m=m,word_count=len(words),connected_count=connected,
                            minimal_subset_count=len(minimal_words),macro_count=len(macro_counts),
                            total_surplus_counts=dict(genus_histogram),
                            per_word_probabilities={str(p):count for p,count in probabilities.items()},
                            minimal_per_word_probabilities={str(p):count for p,count in minimal_probabilities.items()},
                            marked_DP_connected_count=marked_count(m,start,start),
                            marked_DP_cached_states=marked_count.cache_info().currsize,
                            connected_per_word_probabilities={str(p):count for p,count in connected_probabilities.items()},
                            normalization_ok=True,endpoint_ok=True,failures=failures))
    rooted = []
    for d in (2,3,4):
        outputs = Counter()
        for code in product(range(1,d+1),repeat=d-2):
            tree = prufer_tree(d,code)
            for pi in permutations(range(1,2*d-1)):
                w = dps_word(tree,pi,d)
                assert evaluate(d,w) == tuple(range(d))
                assert len(support_macro(d,w)) == 1
                outputs[w] += 1
        assert len(outputs) == C[d][2*d-2]
        assert set(outputs.values()) == {d}
        rooted.append(dict(d=d,rooted_pairs=sum(outputs.values()),connected_words=len(outputs),
                           preimages_per_word=d,endpoint_ok=True,connected_ok=True))
    return results,rooted


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n-max',type=int,default=24)
    parser.add_argument('--m-max',type=int,default=48)
    parser.add_argument('--output',default='results.json')
    args = parser.parse_args()
    start = time.monotonic()
    C = connected_counts(args.n_max,args.m_max)
    for d in range(2,min(args.n_max,args.m_max//2+1)+1):
        expected = 1 if d == 2 else factorial(2*d-2)*d**(d-3)
        assert C[d][2*d-2] == expected
    Z = assembly_counts(args.n_max,args.m_max,C)
    Z0 = assembly_counts(args.n_max,args.m_max,C,minimal_allowed)
    exact,rooted = exact_checks(C,Z,Z0)
    certificates = []
    for n in sorted({4,8,12,16,20,args.n_max}):
        if n > args.n_max:
            continue
        for m in range(0,min(args.m_max,2*n)+1,2):
            tv = Fraction(Z[n][m]-Z0[n][m],Z[n][m])
            sparse_bound = min(Fraction(1),Fraction(m**4,48*(n-m+1)**2)) if m <= n else None
            assert sparse_bound is None or tv <= sparse_bound
            certificates.append(dict(N=n,m=m,total_count=Z[n][m],minimal_count=Z0[n][m],
                                     exact_tv=str(tv),tv_float=float(tv),
                                     sparse_bound=str(sparse_bound) if sparse_bound is not None else None))
    smoke = []
    for seed in (1729,2718,31415):
        rng = random.Random(seed)
        cases = []
        for n,m in ((3,4),(4,4),(4,6),(8,10),(12,18),(24,30)):
            if n > args.n_max or m > args.m_max:
                continue
            for _ in range(20):
                w = sample_minimal_assembly(list(range(n)),m,C,Z0,rng)
                assert len(w) == m and evaluate(n,w) == tuple(range(n))
                assert all(minimal_allowed(len(B),k) for B,k in support_macro(n,w))
            cases.append(dict(N=n,m=m,draws=20,valid=True))
        smoke.append(dict(seed=seed,cases=cases))
        for n,m in ((3,4),(3,6),(4,6),(4,8)):
            w = sample_connected_marked(n,m,rng)
            assert evaluate(n,w) == tuple(range(n)) and len(support_macro(n,w)) == 1
    obstruction_checks = []
    for n,m in ((100,50),(100,100),(100,38),(1000,500),(1000,1000),(1000,250),
                (10000,5000),(10000,10000),(10000,1584)):
        # The floating calculation only selects an integer r. The bound is
        # exact for every recorded r; its evaluation uses integer arithmetic.
        r = max(2,int(m/log(m)))
        numerator = factorial(m)*comb(n*(n-1)//2,m//2)*factorial(r)
        denominator = 2*(r*(r-1)//2)**m
        quotient = denominator//numerator
        exponent = max(0,quotient.bit_length()-1)
        obstruction_checks.append(dict(N=n,m=m,r=r,
                                        numerator_bits=numerator.bit_length(),
                                        denominator_bits=denominator.bit_length(),
                                        minimal_mass_upper_bound=f'2^(-{exponent})',
                                        exact_integer_bound=True))
    output = dict(experiment='r3 component/surplus positive count and minimal sampler audit',
                  commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                  python=platform.python_version(),dependencies={},exact_seed=None,
                  command=f'python3 -B component_audit.py --n-max {args.n_max} --m-max {args.m_max} --output {args.output}',
                  convention='(alpha beta)(x)=alpha(beta(x)); rightmost displayed factor acts first',
                  N_max=args.n_max,m_max=args.m_max,exact_checks=exact,rooted_DPS=rooted,
                  certificates=certificates,seeded_smoke_checks=smoke,
                  forest_obstruction_finite_checks=obstruction_checks,
                  max_connected_count_bits=max(x.bit_length() for row in C for x in row),
                  max_global_count_bits=max(x.bit_length() for row in Z for x in row),
                  elapsed_seconds=time.monotonic()-start)
    Path(args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(exact_cases=len(exact),rooted_DPS=rooted,
                          certificate_rows=len(certificates),elapsed_seconds=output['elapsed_seconds'])))


if __name__ == '__main__':
    main()
