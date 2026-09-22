#!/usr/bin/env python3
"""Bounded exact H0 full-law checks. Not an asymptotic-tail experiment."""
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
import platform
import random
import subprocess
import sys
import time
from types import ModuleType

import sampler as s

OLD_AUDIT = 'experiments/20260907-genus-one-sampler/roles/r1-recursive/audit.py'
OLD_HASH = 'eb2aeffb1e4c4c2efd95245e407257461c8e2f79cb4e541646f6a72d10899930'
source = (s.ROOT / OLD_AUDIT).read_bytes()
assert hashlib.sha256(source).hexdigest() == OLD_HASH
old_audit = ModuleType('h0_checked_g01_word_audit')
old_audit.__file__ = str(s.ROOT / OLD_AUDIT)
sys.modules[old_audit.__name__] = old_audit
saved_sampler = sys.modules['sampler']
sys.modules['sampler'] = s.g01
try:
    exec(compile(source, old_audit.__file__, 'exec'), old_audit.__dict__)
finally:
    sys.modules['sampler'] = saved_sampler


def macro(n, word):
    """Independent bitset union-find support decomposition."""
    blocks = {1 << x for x in range(n)}
    for a, b in word:
        aa = next(B for B in blocks if B & (1 << a))
        bb = next(B for B in blocks if B & (1 << b))
        blocks.difference_update((aa, bb))
        blocks.add(aa | bb)
    answer = []
    for B in blocks:
        labels = tuple(x for x in range(n) if B & (1 << x))
        subsequence = tuple(edge for edge in word if B & (1 << edge[0]))
        answer.append((labels, subsequence))
    return tuple(sorted(answer))


def full_word_probability(prepared, word):
    components = macro(prepared.n, word)
    by_label = {x: (B, subword) for B, subword in components for x in B}
    if any(not s.allowed(len(B), len(local), prepared.cutoff) for B, local in components):
        return Fraction(0)
    remaining, length = list(range(prepared.n)), len(word)
    probability = Fraction(1)
    while remaining:
        B, local = by_label[remaining[0]]
        v, ell, n = len(B), len(local), len(remaining)
        choices, weights = prepared.branches(n, length)
        branch = choices.index((v, ell))
        probability *= Fraction(weights[branch], sum(weights))
        probability /= comb(n-1, v-1) * comb(length, ell)
        relabel = {x: i for i, x in enumerate(B)}
        local = tuple((relabel[a], relabel[b]) for a, b in local)
        if v == 1:
            assert not local
            local_probability = Fraction(1)
        else:
            genus = (ell - 2*v + 2) // 2
            if genus <= 1:
                local_probability = old_audit.word_probability(v, tuple(range(v)), genus, local)
            else:
                oracle = prepared.marked.setdefault(v, s.MarkedCounter(v))
                local_probability = oracle.word_probability(local)
        assert local_probability == Fraction(1, prepared.C[v][ell])
        probability *= local_probability
        remaining = [x for x in remaining if x not in B]
        length -= ell
    assert length == 0
    return probability


def diagnostics(n, word):
    edges = tuple(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    multiplicities = Counter(word)
    p, prefixes = tuple(range(n)), []
    for edge in word:
        p = s.g01.right_swap(p, edge)
        prefixes.append(tuple(sorted(len(c) for c in s.g01.cycles(p))))
    windows = []
    for j in range(max(0, len(word)-2)):
        p3 = s.g01.evaluate(n, word[j:j+3])
        windows.append(tuple(sorted(len(c) for c in s.g01.cycles(p3))))
    return {
        'prefix_cycle_types': tuple(prefixes),
        'per_position_edges': tuple(edge_index[e] for e in word),
        'edge_multiplicity': tuple(sorted(multiplicities.values())),
        'adjacent_repeats': sum(a == b for a, b in zip(word, word[1:])),
        'weighted_support_components': tuple((B, len(local)) for B, local in macro(n, word)),
        'three_window_product_types': tuple(windows),
    }


def law_case(n, m, cutoff=None):
    start = time.monotonic()
    prepared = s.PreparedSampler(n, m, cutoff_override=cutoff)
    probability_histogram, macro_counts, digest = Counter(), Counter(), hashlib.sha256()
    total = kept = 0
    summaries = {k: Counter() for k in diagnostics(n, ()).keys()}
    for word in old_audit.identity_words(n, m):
        total += 1
        assert s.g01.evaluate(n, word) == tuple(range(n))
        prob = full_word_probability(prepared, word)
        good = all(s.allowed(len(B), len(local), prepared.cutoff) for B, local in macro(n, word))
        assert (prob > 0) == good
        if good:
            kept += 1
            probability_histogram[str(prob)] += 1
            macro_counts[tuple((B, len(local)) for B, local in macro(n, word))] += 1
            for key, value in diagnostics(n, word).items():
                summaries[key][value] += 1
        digest.update(repr((word, str(prob))).encode())
    assert total == prepared.Z[n][m]
    assert kept == prepared.A[n][m]
    assert probability_histogram == {str(Fraction(1, kept)): kept}
    assert prepared.global_tv == Fraction(total-kept, total)
    for components, observed in macro_counts.items():
        expected = Fraction(factorial(m))
        for B, ell in components:
            expected *= Fraction(prepared.C[len(B)][ell], factorial(ell))
        assert expected == observed
    # Since every literal-word probability was checked, every deterministic
    # diagnostic pushforward is exact; retain compact histogram digests.
    return {'N': n, 'm': m, 'candidate': prepared.candidate, 'cutoff': prepared.cutoff,
            'total_words': total, 'allowed_words': kept, 'omitted_words': total-kept,
            'global_tv_exact': str(prepared.global_tv), 'per_word_probability': str(Fraction(1, kept)),
            'labeled_macro_count': len(macro_counts), 'word_probability_digest': digest.hexdigest(),
            'diagnostic_histograms': {k: {'distinct': len(v), 'sha256': hashlib.sha256(repr(sorted(v.items())).encode()).hexdigest()} for k, v in summaries.items()},
            'seconds': time.monotonic()-start, 'passed': True}


def boundary_checks():
    rows = []
    for n, m in ((0,0),(1,0),(2,0),(2,2),(2,4),(2,6),(3,0),(3,2)):
        p = s.PreparedSampler(n, m)
        result = p.sample(random.Random(1729))
        assert s.g01.evaluate(n, result.word) == tuple(range(n))
        assert len(result.word) == m and result.global_tv == 0
        rows.append({'N':n,'m':m,'Z':result.total_count,'K':result.cutoff,'status':'accepted'})
    for n, m in ((0,2),(1,2),(1,1),(2,1),(3,3),(-1,0),(2,-2)):
        try:
            s.PreparedSampler(n, m)
        except ValueError:
            rows.append({'N':n,'m':m,'status':'rejected empty/invalid'})
        else:
            raise AssertionError((n,m,'must reject'))
    cutoff_rows = []
    for n in range(0,61):
        for m in range(0,81):
            expected = max([0] + [v for v in range(1,n+1) if v**(2*v) <= (n+m+2)**4])
            assert s.top_level_cutoff(n,m) == expected
            cutoff_rows.append((n,m,expected))
    assert s.top_level_cutoff(4,9) == 3
    assert s.top_level_cutoff(4,10) == 4  # exact equality 4^8=16^4
    # At top-level (42,12), K=5; after isolating labels a remaining (5,12)
    # subproblem has K=4. Recomputing would incorrectly exclude genus2 v5.
    top = s.PreparedSampler(42,12)
    assert top.cutoff == 5 and s.top_level_cutoff(5,12) == 4
    assert (5,12) in top.branches(5,12)[0]
    assert top.A[5][12] == top.Z[5][12]
    # Beyond Python's default recursion depth: actual DP and actual sampler.
    long = s.MarkedCounter(2)
    word = long.sample(1200, random.Random(2718))
    assert len(word) == 1200 and set(word) == {(0,1)}
    assert long.connected_count(1200) == 1
    return {'boundaries':rows,'cutoff_integer_grid_cells':len(cutoff_rows),
            'cutoff_grid_digest':hashlib.sha256(repr(cutoff_rows).encode()).hexdigest(),
            'exact_cutoff_equality_case':[4,10,4],
            'frozen_cutoff_regression':{'top':[42,12,5],'remaining':[5,12,4],
                                      'length12_size5_branch_retained':True},
            'unbounded_length_stack_regression':{'v':2,'ell':1200,'cache_states':len(long.cache),'count':1,'passed':True}}


def marked_count_checks():
    rows = []
    table = s.counts.connected_counts(5,14)
    for v in range(1,6):
        oracle = s.MarkedCounter(v)
        for ell in range(15):
            actual = oracle.connected_count(ell)
            assert actual == table[v][ell], (v,ell,actual,table[v][ell])
            rows.append({'v':v,'ell':ell,'connected_count':actual,'states':len(oracle.cache)})
    return rows


def seeded_checks():
    rows = []
    cases = ((3,8,None),(4,8,None),(5,12,None),(6,12,None),(8,16,None),(3,8,2))
    for n,m,k in cases:
        prepared = s.PreparedSampler(n,m,cutoff_override=k)
        for seed in (1729,2718,31415):
            rng, digest = random.Random(seed), hashlib.sha256()
            for _ in range(10):
                draw = prepared.sample(rng)
                assert len(draw.word) == m
                assert s.g01.evaluate(n,draw.word) == tuple(range(n))
                assert all(s.allowed(len(B),len(local),prepared.cutoff) for B,local in macro(n,draw.word))
                assert draw.global_tv == prepared.global_tv
                digest.update(repr(draw.word).encode())
            rows.append({'N':n,'m':m,'candidate':prepared.candidate,'K':prepared.cutoff,
                         'seed':seed,'draws':10,'global_tv_exact':str(prepared.global_tv),
                         'valid':True,'sha256':digest.hexdigest()})
    return rows


def main():
    start = time.monotonic()
    result = {'version':'R3-audit-v1','claim':'exact finite laws and implementation validity; no asymptotic inference',
              'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=s.ROOT,text=True).strip(),
              'python':platform.python_version(),'dependencies':{},'command':' '.join(sys.argv),
              'source_hashes':{p:d for p,d in s.SOURCES.values()}|{OLD_AUDIT:OLD_HASH},
              'sampler_sha256':hashlib.sha256(Path(s.__file__).read_bytes()).hexdigest(),
              'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'law_cases':[]}
    output = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('results.json')
    for n,m,k in ((3,4,None),(4,4,None),(4,6,None),(3,6,None),(3,8,None),(3,8,2),(4,8,None)):
        row=law_case(n,m,k)
        result['law_cases'].append(row)
        output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(row),flush=True)
    result['boundary_checks']=boundary_checks()
    result['marked_count_checks']=marked_count_checks()
    result['seeded_checks']=seeded_checks()
    result['seconds']=time.monotonic()-start
    result['passed']=True
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'seconds':result['seconds'],'output':str(output)}))

if __name__ == '__main__':
    main()
