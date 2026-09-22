#!/usr/bin/env python3
"""H0 v1 / H1 v1: exact restricted samplers and mass certificates.

Python labels are 0,...,N-1; products act rightmost first. The law is
Unif(A(N,m)) for ONE fixed top-level integer K. It is globally uniform only
when the returned exact global_tv is zero. No negligible-error claim is
made by this module. Independent fair getrandbits are the exactness model;
a seeded random.Random is only a reproducible diagnostic implementation.

Dependencies are read-only historical sources, SHA256 checked BEFORE code
execution. compile/exec avoids creating bytecode beside historical files.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import random
import sys
from types import ModuleType

ROOT = Path(__file__).resolve().parents[4]
SOURCES = {
    'g01': ('experiments/20260907-genus-one-sampler/roles/r1-recursive/sampler.py',
            'd9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d'),
    'counts': ('experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py',
               'a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2'),
}


def _checked_source(name):
    relative, expected = SOURCES[name]
    path = ROOT / relative
    source = path.read_bytes()
    observed = hashlib.sha256(source).hexdigest()
    if observed != expected:
        raise RuntimeError(f'historical dependency hash mismatch: {relative}')
    module = ModuleType('h0_checked_' + name)
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(source, str(path), 'exec'), module.__dict__)
    return module


g01 = _checked_source('g01')
counts = _checked_source('counts')


def top_level_cutoff(n: int, m: int) -> int:
    """Exact largest 1<=v<=N with v**(2*v)<=(N+m+2)**4; N=0 gives0.

Integer-only binary search exploits strict increase of v**(2*v).
The cutoff is computed once by PreparedSampler, never on its subproblems.
"""
    if n < 0 or m < 0:
        raise ValueError('N and m must be nonnegative')
    budget, low, high = (n + m + 2) ** 4, 0, n + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** (2 * mid) <= budget:
            low = mid
        else:
            high = mid
    return low


def allowed(v: int, ell: int, cutoff: int) -> bool:
    if v == 1:
        return ell == 0
    if v < 2 or ell < 2 * v - 2 or ell % 2:
        return False
    genus = (ell - 2 * v + 2) // 2
    return genus <= 1 or v <= cutoff


def marked_step(q: tuple, partition: tuple, edge: tuple) -> tuple:
    """Right multiplication plus canonical exposed-support partition join."""
    a, b = edge
    p = list(q)
    p[a], p[b] = p[b], p[a]
    old, new = partition[b], partition[a]
    canonical, joined = {}, []
    for block in partition:
        block = new if block == old else block
        if block not in canonical:
            canonical[block] = len(canonical)
        joined.append(canonical[block])
    return tuple(p), tuple(joined)


class MarkedCounter:
    """Iterative completion DP, including the complete remaining-length index.

F(r,q,pi) counts length-r suffixes ending at identity whose union with the
exposed support pi is connected. Cache size <= (m+1)*v!*Bell(v); no Python
recursion or interpreter-limit change occurs, even for unbounded length.
"""
    def __init__(self, v: int):
        if v < 1:
            raise ValueError('connected support needs at least one label')
        self.v = v
        self.identity = tuple(range(v))
        self.edges = tuple(combinations(range(v), 2))
        self.cache = {}

    def count(self, remaining: int, q: tuple, partition: tuple) -> int:
        if remaining < 0:
            return 0
        root = (remaining, q, partition)
        tasks = [(root, False)]
        while tasks:
            key, finish = tasks.pop()
            if key in self.cache:
                continue
            r, state, support = key
            if r == 0:
                self.cache[key] = int(state == self.identity and len(set(support)) == 1)
                continue
            # Every new support edge joins at most two current components.
            if len(set(support)) - 1 > r:
                self.cache[key] = 0
                continue
            children = [(r - 1, *marked_step(state, support, edge)) for edge in self.edges]
            if finish:
                self.cache[key] = sum(self.cache[child] for child in children)
            else:
                tasks.append((key, True))
                tasks.extend((child, False) for child in children if child not in self.cache)
        return self.cache[root]

    def connected_count(self, ell: int) -> int:
        return self.count(ell, self.identity, self.identity)

    def sample(self, ell: int, rng=None) -> tuple:
        rng = random.SystemRandom() if rng is None else rng
        total = self.connected_count(ell)
        if total == 0:
            raise ValueError('connected identity fiber is empty')
        q = partition = self.identity
        word = []
        for r in range(ell, 0, -1):
            children = [marked_step(q, partition, edge) for edge in self.edges]
            weights = [self.count(r - 1, *child) for child in children]
            assert sum(weights) == self.count(r, q, partition)
            index = g01.weighted_choice(rng, range(len(self.edges)), weights)
            word.append(self.edges[index])
            q, partition = children[index]
        assert q == self.identity and len(set(partition)) == 1
        return tuple(word)

    def word_probability(self, word: tuple) -> Fraction:
        """Exact transition-product audit for a specific connected word."""
        q = partition = self.identity
        denominator = self.connected_count(len(word))
        if not denominator:
            return Fraction(0)
        result = Fraction(1)
        for j, edge in enumerate(word):
            child = marked_step(q, partition, edge)
            child_count = self.count(len(word)-j-1, *child)
            result *= Fraction(child_count, self.count(len(word)-j, q, partition))
            if child_count == 0:
                return Fraction(0)
            q, partition = child
        return result


@dataclass(frozen=True)
class RestrictedSample:
    word: tuple
    n: int
    m: int
    cutoff: int
    candidate: str
    total_count: int
    allowed_count: int

    @property
    def covered_mass(self) -> Fraction:
        return Fraction(self.allowed_count, self.total_count)

    @property
    def global_tv(self) -> Fraction:
        return Fraction(self.total_count - self.allowed_count, self.total_count)


class PreparedSampler:
    """Reusable exact conditional sampler with immutable cutoff semantics.

For research tests only, cutoff_override declares a DIFFERENT restricted
candidate. Such output is explicitly labeled test-cutoff, never H0.
H0 is defined for every N>=2 and even m, including outside target T0.
N=0/1,m=0 return the empty word; empty identity fibers raise ValueError.
"""
    def __init__(self, n: int, m: int, *, cutoff_override=None, policy='H0'):
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError('N and m must be nonnegative integers')
        if m % 2 or (n < 2 and m):
            raise ValueError('the identity fiber is empty')
        if policy not in ('H0', 'H1'):
            raise ValueError('policy must be H0 or H1')
        self.policy = policy
        self.n, self.m = n, m
        self.h0_cutoff = top_level_cutoff(n, m)
        if cutoff_override is not None:
            if not isinstance(cutoff_override, int) or not 0 <= cutoff_override <= n:
                raise ValueError('test cutoff must be an integer in [0,N]')
        self.cutoff = self.h0_cutoff if cutoff_override is None else cutoff_override
        self.candidate = f'{policy}-v1' if cutoff_override is None else f'{policy}-test-cutoff-{self.cutoff}'
        self.C = counts.connected_counts(n, m)
        self.Z = counts.assembly_counts(n, m, self.C)
        self.A = counts.assembly_counts(n, m, self.C, self.is_allowed)
        if self.A[n][m] == 0:
            raise ValueError('the specified restricted fiber is empty')
        assert 0 < self.A[n][m] <= self.Z[n][m]
        self.marked = {}

    def is_allowed(self, v: int, ell: int) -> bool:
        """H1 keeps only isolates and small support; H0 also keeps all g0/1."""
        return allowed(v, ell, self.cutoff) and (self.policy == 'H0' or v == 1 or v <= self.cutoff)

    @property
    def global_tv(self):
        return Fraction(self.Z[self.n][self.m] - self.A[self.n][self.m], self.Z[self.n][self.m])

    def branches(self, n: int, m: int):
        """Actual conditional assembly branches, with the TOP-LEVEL cutoff."""
        choices, weights = [], []
        for v in range(1, min(n, m // 2 + 1) + 1):
            for ell in range(0, m + 1, 2):
                c = self.C[v][ell]
                if c and self.is_allowed(v, ell):
                    weight = comb(n-1, v-1)*comb(m, ell)*c*self.A[n-v][m-ell]
                    if weight:
                        choices.append((v, ell))
                        weights.append(weight)
        assert sum(weights) == self.A[n][m]
        return choices, weights

    def connected_sample(self, v: int, ell: int, rng) -> tuple:
        assert self.is_allowed(v, ell)
        if v == 1:
            return ()
        genus = (ell - 2 * v + 2) // 2
        if self.policy == 'H0' and genus <= 1:
            assert g01.count((1,) * v, genus) == self.C[v][ell]
            return g01.sample(tuple(range(v)), genus, rng)
        assert v <= self.cutoff
        if v not in self.marked:
            self.marked[v] = MarkedCounter(v)
        oracle = self.marked[v]
        assert oracle.connected_count(ell) == self.C[v][ell]
        return oracle.sample(ell, rng)

    def sample(self, rng=None) -> RestrictedSample:
        rng = random.SystemRandom() if rng is None else rng
        labels, positions = list(range(self.n)), list(range(self.m))
        result = [None] * self.m
        while labels:
            n, m = len(labels), len(positions)
            choices, weights = self.branches(n, m)
            v, ell = g01.weighted_choice(rng, choices, weights)
            other = g01.unrank_subset(n-1, v-1, g01.randbelow(rng, comb(n-1, v-1)))
            selected_labels = [labels[0]] + [labels[i+1] for i in other]
            selected_positions = g01.unrank_subset(m, ell, g01.randbelow(rng, comb(m, ell)))
            local_word = self.connected_sample(v, ell, rng)
            assert len(local_word) == ell
            for i, (a, b) in zip(selected_positions, local_word):
                result[positions[i]] = (selected_labels[a], selected_labels[b])
            removed_labels, removed_positions = set(selected_labels), set(selected_positions)
            labels = [x for x in labels if x not in removed_labels]
            positions = [x for i, x in enumerate(positions) if i not in removed_positions]
        assert not positions and all(edge is not None for edge in result)
        return RestrictedSample(tuple(result), self.n, self.m, self.cutoff,
                                self.candidate, self.Z[self.n][self.m], self.A[self.n][self.m])


def sample_h0(n: int, m: int, rng=None) -> RestrictedSample:
    """Clean one-shot H0 API; use PreparedSampler for repeated fixed inputs."""
    return PreparedSampler(n, m).sample(rng)


def sample_h1(n: int, m: int, rng=None) -> RestrictedSample:
    """Separate H1 law: every nontrivial component has v<=top-level K.

All connected draws use the elementary marked DP. No g0/1 count or
sampler formula is called on this path; shared exact random-choice and
subset-unranking utilities are elementary and do not use those formulas.
"""
    return PreparedSampler(n, m, policy='H1').sample(rng)


def _decimal_safe(value: int) -> bool:
    """Respect the current interpreter's decimal limit without changing it."""
    limit = sys.get_int_max_str_digits() if hasattr(sys, 'get_int_max_str_digits') else 0
    return not limit or abs(value).bit_length() <= 3 * limit


def exact_integer_json(value: int):
    """Usual JSON integer, or a lossless hex object for very large integers."""
    return value if _decimal_safe(value) else {'encoding': 'hex', 'value': hex(value)}


def exact_fraction_json(value: Fraction):
    """Usual rational string, or lossless hexadecimal numerator/denominator."""
    if _decimal_safe(value.numerator) and _decimal_safe(value.denominator):
        return str(value)
    return {'encoding': 'hex-rational', 'numerator': hex(value.numerator),
            'denominator': hex(value.denominator)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, required=True)
    parser.add_argument('--m', type=int, required=True)
    parser.add_argument('--seed', type=int, help='diagnostic reproducibility only')
    parser.add_argument('--draws', type=int, default=1)
    parser.add_argument('--certificate-only', action='store_true')
    parser.add_argument('--test-cutoff', type=int, help='declares a different candidate, not H0')
    parser.add_argument('--policy', choices=('H0', 'H1'), default='H0')
    args = parser.parse_args()
    if args.draws < 0:
        parser.error('--draws must be nonnegative')
    try:
        prepared = PreparedSampler(args.n, args.m, cutoff_override=args.test_cutoff, policy=args.policy)
    except ValueError as error:
        parser.error(str(error))
    rng = random.SystemRandom() if args.seed is None else random.Random(args.seed)
    draws = [] if args.certificate_only else [prepared.sample(rng) for _ in range(args.draws)]
    print(json.dumps({
        'candidate': prepared.candidate,
        'target': 'Unif(A(N,m)); exact restriction with one fixed top-level cutoff',
        'N': args.n, 'm': args.m, 'cutoff': prepared.cutoff,
        'h0_cutoff': prepared.h0_cutoff,
        'T0_length_condition': args.n >= 2 and args.m % 2 == 0 and args.m ** 5 <= args.n ** 3,
        'Z': exact_integer_json(prepared.Z[args.n][args.m]),
        'Z_A': exact_integer_json(prepared.A[args.n][args.m]),
        'global_TV_exact': exact_fraction_json(prepared.global_tv),
        'negligible_error_theorem': 'not asserted by this implementation',
        'word_labels': '1 through N',
        'words': [[[a+1, b+1] for a, b in draw.word] for draw in draws],
        'composition': '(alpha beta)(x)=alpha(beta(x)); rightmost factor acts first',
        'diagnostic_seed': args.seed,
        'randomness_model': 'independent fair bits; seeded PRNG is diagnostic only',
        'source_sha256': {path: digest for path, digest in SOURCES.values()},
    }, indent=2))


if __name__ == '__main__':
    main()
