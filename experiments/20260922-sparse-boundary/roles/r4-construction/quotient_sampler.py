#!/usr/bin/env python3
"""H2-QC.v1: exact support-size restricted identity-word sampler.

Labels 0..N-1, rightmost-first permutation composition. This is a research
prototype with exact conditional law, not a T0 negligible-error claim.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from types import ModuleType
import hashlib
import random
import sys

ROOT = Path(__file__).resolve().parents[4]
COUNT_SOURCE = 'experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py'
COUNT_HASH = 'a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2'

def load_counts():
    path = ROOT / COUNT_SOURCE
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != COUNT_HASH:
        raise RuntimeError('read-only count dependency hash mismatch before execution')
    module = ModuleType('r4_qc_checked_counts')
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(raw, str(path), 'exec'), module.__dict__)
    return module

counts = load_counts()

def canon(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))

def signature(permutation, partition):
    """Complete simultaneous-conjugacy invariant, retaining support history."""
    blocks = {}
    seen = set()
    for start in range(len(permutation)):
        if start in seen:
            continue
        cursor, length = start, 0
        while cursor not in seen:
            seen.add(cursor)
            assert partition[cursor] == partition[start]
            length += 1
            cursor = permutation[cursor]
        blocks.setdefault(partition[start], []).append(length)
    return canon(blocks.values())

def literal_step(permutation, partition, edge):
    a, b = edge
    next_p = list(permutation)
    next_p[a], next_p[b] = next_p[b], next_p[a]
    old, new = partition[b], partition[a]
    names, next_pi = {}, []
    for value in partition:
        value = new if value == old else value
        if value not in names:
            names[value] = len(names)
        next_pi.append(names[value])
    return tuple(next_p), tuple(next_pi)

def transition_counts(state):
    """Counts literal edges by orbit successor; duplicate objects indexed."""
    out = Counter()
    for i, block in enumerate(state):
        # Splitting one cycle; i and j denote actual indexed objects.
        for j, length in enumerate(block):
            for left in range(1, length // 2 + 1):
                right = length - left
                new_block = block[:j] + block[j+1:] + (left, right)
                new_state = canon(state[:i] + state[i+1:] + (new_block,))
                out[new_state] += length if left != right else length // 2
        # Joining distinct cycles inside a support block.
        for j in range(len(block)):
            for k in range(j+1, len(block)):
                new_block = tuple(x for h,x in enumerate(block) if h not in (j,k)) + (block[j]+block[k],)
                new_state = canon(state[:i] + state[i+1:] + (new_block,))
                out[new_state] += block[j]*block[k]
        # Joining two support blocks and one cycle from each.
        for j in range(i+1, len(state)):
            other = state[j]
            for a, x in enumerate(block):
                for b, y in enumerate(other):
                    merged = block[:a] + block[a+1:] + other[:b] + other[b+1:] + (x+y,)
                    rest = tuple(z for k,z in enumerate(state) if k not in (i,j))
                    out[canon(rest + (merged,))] += x*y
    v = sum(map(sum, state))
    assert sum(out.values()) == comb(v, 2)
    return tuple(sorted(out.items()))

def randbelow(rng, bound):
    if bound <= 0:
        raise ValueError('empty integer choice')
    if hasattr(rng, 'exact_index'):
        return rng.exact_index((1,) * bound)
    if bound == 1:
        return 0
    bits = (bound-1).bit_length()
    while True:
        candidate = rng.getrandbits(bits)
        if candidate < bound:
            return candidate

def weighted_index(rng, weights):
    if not weights or sum(weights) <= 0 or min(weights) < 0:
        raise ValueError('empty/nonpositive conditional law')
    if hasattr(rng, 'exact_index'):
        return rng.exact_index(tuple(weights))
    ticket = randbelow(rng, sum(weights))
    for i, w in enumerate(weights):
        if ticket < w:
            return i
        ticket -= w
    raise AssertionError('unreachable')

def unrank_subset(n, k, rank):
    if not 0 <= rank < comb(n,k):
        raise ValueError('bad subset rank')
    result = []
    for value in range(n):
        if not k:
            break
        take = comb(n-value-1, k-1)
        if rank < take:
            result.append(value)
            k -= 1
        else:
            rank -= take
    assert not k and rank == 0
    return tuple(result)

class QuotientCounter:
    def __init__(self, v):
        if not isinstance(v,int) or v < 1:
            raise ValueError('positive integer degree required')
        self.v = v
        self.identity = tuple(range(v))
        self.initial = ((1,),) * v
        self.terminal = ((1,) * v,)
        self.edges = tuple(combinations(range(v), 2))
        self.cache = {}
        self.transitions = {}

    def successors(self, state):
        if state not in self.transitions:
            self.transitions[state] = transition_counts(state)
        return self.transitions[state]

    def count(self, remaining, state):
        if remaining < 0:
            return 0
        root = (remaining, state)
        tasks = [(root, False)]
        while tasks:
            key, finish = tasks.pop()
            if key in self.cache:
                continue
            r, q = key
            if r == 0:
                self.cache[key] = int(q == self.terminal)
                continue
            if len(q)-1 > r:
                self.cache[key] = 0
                continue
            children = [((r-1, child), multiplicity) for child,multiplicity in self.successors(q)]
            if finish:
                self.cache[key] = sum(self.cache[child]*multiplicity for child,multiplicity in children)
            else:
                tasks.append((key, True))
                tasks.extend((child, False) for child,_ in children if child not in self.cache)
        return self.cache[root]

    def connected_count(self, length):
        return self.count(length, self.initial)

    def sample(self, length, rng=None):
        rng = random.SystemRandom() if rng is None else rng
        if not self.connected_count(length):
            raise ValueError('empty connected identity fiber')
        p = pi = self.identity
        result = []
        for remaining in range(length,0,-1):
            children = [literal_step(p,pi,edge) for edge in self.edges]
            weights = [self.count(remaining-1,signature(*child)) for child in children]
            assert sum(weights) == self.count(remaining,signature(p,pi))
            i = weighted_index(rng,weights)
            result.append(self.edges[i])
            p,pi = children[i]
        assert p == self.identity and len(set(pi)) == 1
        return tuple(result)

    def word_probability(self, word):
        denominator = self.connected_count(len(word))
        if not denominator:
            return Fraction(0)
        p = pi = self.identity
        probability = Fraction(1)
        for i,edge in enumerate(word):
            child = literal_step(p,pi,edge)
            numerator = self.count(len(word)-i-1,signature(*child))
            if not numerator:
                return Fraction(0)
            probability *= Fraction(numerator,self.count(len(word)-i,signature(p,pi)))
            p,pi = child
        return probability

def cutoff(n,m):
    if not isinstance(n,int) or not isinstance(m,int) or min(n,m) < 0:
        raise ValueError('nonnegative integer inputs required')
    bound, power, v = (n+m+2)**4, 1, 0
    while v < n and power*3 <= bound:
        v += 1
        power *= 3
    return v

class PreparedH2:
    """Exactly Unif(D): every nontrivial support component has v<=fixed L."""
    def __init__(self,n,m,cutoff_override=None):
        if not isinstance(n,int) or not isinstance(m,int) or min(n,m) < 0:
            raise ValueError('nonnegative integer inputs required')
        if m%2 or (n<2 and m):
            raise ValueError('empty identity fiber')
        self.n,self.m = n,m
        self.original_cutoff = cutoff(n,m)
        self.cutoff = self.original_cutoff if cutoff_override is None else cutoff_override
        if not isinstance(self.cutoff,int) or not 0 <= self.cutoff <= n:
            raise ValueError('invalid diagnostic cutoff')
        self.candidate = 'H2-QC.v1' if cutoff_override is None else 'H2-QC.v1-diagnostic-cutoff'
        self.C = counts.connected_counts(n,m)
        self.Z = counts.assembly_counts(n,m,self.C)
        self.D = counts.assembly_counts(n,m,self.C,self.allowed)
        self.counters = {}
        if not self.D[n][m]:
            raise ValueError('empty restricted identity fiber')

    def allowed(self,v,ell):
        return (v==1 and ell==0) or (2<=v<=self.cutoff and ell>=2*v-2 and ell%2==0)

    @property
    def global_tv(self):
        return Fraction(self.Z[self.n][self.m]-self.D[self.n][self.m],self.Z[self.n][self.m])

    def branches(self,n,m):
        choices,weights = [],[]
        for v in range(1,min(n,m//2+1)+1):
            for ell in range(0,m+1,2):
                if self.allowed(v,ell) and self.C[v][ell]:
                    weight = comb(n-1,v-1)*comb(m,ell)*self.C[v][ell]*self.D[n-v][m-ell]
                    if weight:
                        choices.append((v,ell))
                        weights.append(weight)
        assert sum(weights) == self.D[n][m]
        return choices,weights

    def sample(self,rng=None):
        rng = random.SystemRandom() if rng is None else rng
        labels,positions = list(range(self.n)),list(range(self.m))
        result = [None]*self.m
        while labels:
            n,m = len(labels),len(positions)
            choices,weights = self.branches(n,m)
            v,ell = choices[weighted_index(rng,weights)]
            other = unrank_subset(n-1,v-1,randbelow(rng,comb(n-1,v-1)))
            chosen_labels = [labels[0]]+[labels[j+1] for j in other]
            chosen_positions = unrank_subset(m,ell,randbelow(rng,comb(m,ell)))
            if v not in self.counters:
                self.counters[v] = QuotientCounter(v)
            oracle = self.counters[v]
            assert oracle.connected_count(ell) == self.C[v][ell]
            local = oracle.sample(ell,rng)
            for i,(a,b) in zip(chosen_positions,local):
                result[positions[i]] = (chosen_labels[a],chosen_labels[b])
            label_set,position_set = set(chosen_labels),set(chosen_positions)
            labels = [x for x in labels if x not in label_set]
            positions = [x for i,x in enumerate(positions) if i not in position_set]
        assert not positions and all(x is not None for x in result)
        return tuple(result)
