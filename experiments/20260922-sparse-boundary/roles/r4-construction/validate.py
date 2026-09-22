#!/usr/bin/env python3
"""Deterministic exact QC tests, with seeded smoke tests for validity only."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product, permutations
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import platform
import random
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
raw = (HERE/'quotient_sampler.py').read_bytes()
spec = importlib.util.spec_from_file_location('r4_quotient_sampler',HERE/'quotient_sampler.py')
qc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qc)

class NeedChoice(Exception):
    def __init__(self,weights):
        self.weights = weights

class Tape:
    def __init__(self,indices):
        self.indices,self.cursor = indices,0
        self.probability = Fraction(1)
    def exact_index(self,weights):
        if self.cursor == len(self.indices):
            raise NeedChoice(weights)
        i = self.indices[self.cursor]
        self.cursor += 1
        assert weights[i] > 0
        self.probability *= Fraction(weights[i],sum(weights))
        return i

def literal_words(n,m):
    edges = tuple(combinations(range(n),2))
    identity = tuple(range(n))
    words = []
    connected = 0
    for word in product(edges,repeat=m):
        p = pi = identity
        for edge in word:
            p,pi = qc.literal_step(p,pi,edge)
        if p == identity:
            words.append(word)
            connected += len(set(pi)) == 1
    return words,connected

def forward_law(prepared):
    pending = [()]
    law = defaultdict(Fraction)
    branches = 0
    while pending:
        prefix = pending.pop()
        tape = Tape(prefix)
        try:
            word = prepared.sample(tape)
        except NeedChoice as event:
            branches += 1
            pending.extend(prefix+(i,) for i,w in enumerate(event.weights) if w)
            continue
        assert tape.cursor == len(prefix)
        law[word] += tape.probability
    assert sum(law.values()) == 1
    return law,branches

def representative(state):
    p,pi = [],[]
    for block_id,block in enumerate(state):
        for length in block:
            start = len(p)
            p.extend(range(start+1,start+length))
            p.append(start)
            pi.extend([block_id]*length)
    return tuple(p),tuple(pi)

def quotient_states(v):
    states = set()
    # Direct ternary separators give every composition of compositions.
    for marks in product(range(3),repeat=v-1):
        blocks,block,part = [],[],1
        for marker in marks:
            if marker == 0:
                part += 1
            elif marker == 1:
                block.append(part)
                part = 1
            else:
                block.append(part)
                blocks.append(tuple(block))
                block,part = [],1
        block.append(part)
        blocks.append(tuple(block))
        states.add(qc.canon(blocks))
    return states

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    parser.add_argument('--skip-forward',action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    results = {'candidate':'H2-QC.v1','python':platform.python_version(),'seeded_validity_seeds':[1729,2718,31415],
        'source_sha256':hashlib.sha256(raw).hexdigest(),'count_source_sha256':qc.COUNT_HASH,
        'command':' '.join(sys.argv),'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}
    rows = []
    # Every quotient state through7, and every edge of its representative.
    for v in range(1,8):
        states = quotient_states(v)
        edge_checks = 0
        for state in states:
            p,pi = representative(state)
            assert qc.signature(p,pi) == state
            direct = Counter(qc.signature(*qc.literal_step(p,pi,e)) for e in combinations(range(v),2))
            assert dict(qc.transition_counts(state)) == direct
            edge_checks += len(tuple(combinations(range(v),2)))
        rows.append({'v':v,'quotient_states':len(states),'ternary_bound':3**(v-1),'literal_edges_checked':edge_checks})
    results['orbit_transitions'] = rows
    # Compare independently imported established positive counts.
    C = qc.counts.connected_counts(9,20)
    results['connected_counts'] = []
    for v in range(1,10):
        oracle = qc.QuotientCounter(v)
        for ell in range(21):
            actual = oracle.connected_count(ell)
            assert actual == C[v][ell], (v,ell,actual,C[v][ell])
        results['connected_counts'].append({'v':v,'lengths':list(range(21)),'cache_entries':len(oracle.cache),'transition_states':len(oracle.transitions)})
    rows = []
    for n,m in [(3,4),(4,4),(4,6),(3,8)]:
        words,connected = literal_words(n,m)
        prepared = qc.PreparedH2(n,m)
        oracle = qc.QuotientCounter(n)
        assert oracle.connected_count(m) == connected
        for word in words:
            p = pi = tuple(range(n))
            for e in word:
                p,pi = qc.literal_step(p,pi,e)
            expected = Fraction(1,connected) if len(set(pi)) == 1 else Fraction(0)
            assert oracle.word_probability(word) == expected
        if not args.skip_forward:
            law,branches = forward_law(prepared)
            assert set(law) == set(words)
            assert set(law.values()) == {Fraction(1,len(words))}
        else:
            branches = None
        for seed in (1729,2718,31415):
            rng = random.Random(seed)
            for _ in range(20):
                assert prepared.sample(rng) in set(words)
        rows.append({'N':n,'m':m,'total':len(words),'connected':connected,'forward_law_branches':branches,'cutoff':prepared.cutoff,'per_word_probability':str(Fraction(1,len(words)))})
    results['literal_laws'] = rows
    results['boundaries'] = []
    for n,m in [(0,0),(1,0),(2,0),(2,2),(2,8),(3,2)]:
        prepared = qc.PreparedH2(n,m)
        word = prepared.sample(random.Random(1729))
        assert len(word)==m and prepared.global_tv==0
        results['boundaries'].append({'N':n,'m':m,'word':word})
    for n,m in [(1,2),(2,1),(3,3)]:
        try:
            qc.PreparedH2(n,m)
        except ValueError:
            pass
        else:
            raise AssertionError('empty target accepted')
    # Same endpoint, different support history: not merged by quotient.
    oracle = qc.QuotientCounter(2)
    assert oracle.count(0,((1,1),)) == 1
    assert oracle.count(0,((1,),(1,))) == 0
    results['support_history_regression'] = {'connected_identity_zero_remaining':1,'disconnected_identity_zero_remaining':0}
    # Long arbitrary-genus length uses explicit stacks, not Python recursion.
    oracle = qc.QuotientCounter(2)
    word = oracle.sample(1400,random.Random(1729))
    assert word == ((0,1),)*1400
    results['long_stack'] = {'v':2,'length':1400,'cache_entries':len(oracle.cache)}
    # Fixed-cutoff test: top L must survive a smaller residual input.
    top = qc.PreparedH2(100,38)
    top_cutoff = top.cutoff
    small = qc.cutoff(17,38)
    assert top_cutoff >= 17 > small
    choices,weights = top.branches(17,38)
    assert (17,38) in choices
    assert top.allowed(17,38)
    results['fixed_cutoff'] = {'top':[100,38],'L_top':top_cutoff,'residual':[17,38],'L_if_recomputed':small,'branch_retained':[17,38]}
    results['seconds'] = time.monotonic()-started
    results['all_passed'] = True
    Path(args.output).write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'seconds':results['seconds'],'output':args.output}))

if __name__ == '__main__':
    main()
