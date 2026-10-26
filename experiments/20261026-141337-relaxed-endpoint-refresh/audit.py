#!/usr/bin/env python3
"""Independent finite audits of the formulas and quotient implementation."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import platform
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    c, q = load('check'), load('quotient')
    records = []
    finite = {(d['N'],d['m'],d['k']):d for d in map(json.loads,(HERE/'results.jsonl').read_text().splitlines())
              if d['kind']=='finite_graph'}
    quot = {(d['N'],d['m'],d['k']):d for d in map(json.loads,(HERE/'quotient.jsonl').read_text().splitlines())
            if d['kind']=='relabeling_quotient'}
    compared = 0
    for key in finite.keys() & quot.keys():
        a, b = finite[key], quot[key]
        for field in ('allowed_words','identity_words','distance_to_identity_histogram'):
            assert a[field] == b[field], (key,field)
        compared += 1
    records.append({'kind':'labeled_quotient_agreement','cases':compared})
    # A separate labeled count DP checks quotient orbit cardinalities without
    # generating the word graph or calling the canonical-labeling routine.
    count_cases = []
    for n in range(2,9):
        G = c.Group(n)
        counts = [0]*len(G.perms)
        counts[0] = 1
        inequalities = 0
        for m in range(9):
            if m % 2 == 0:
                assert all(z <= counts[0] for z in counts)
                inequalities += len(counts)
            key = (n,m,2)
            if key in quot:
                total = sum(z for z,d in zip(counts,G.defects) if d <= 2)
                assert total == quot[key]['allowed_words']
                assert counts[0] == quot[key]['identity_words']
                assert Fraction(counts[0],total) >= Fraction(1,1+2*math.comb(n,3)+3*math.comb(n,4))
            nxt = [0]*len(counts)
            for g,z in enumerate(counts):
                for h in G.next[g]:
                    nxt[h] += z
            counts = nxt
        count_cases.append({'N':n,'even_count_inequalities':inequalities})
    records.append({'kind':'count_bound_checks','lengths':list(range(0,9,2)), 'cases':count_cases})

    # Exact simulation of every adjacent Hurwitz and square refresh channel
    # on the three required identity fibers, using <=2 single-coordinate edits.
    channel_checks = []
    for n,m in [(3,4),(4,4),(4,6)]:
        G = c.Group(n)
        gates = [G.perms[G.next[0][a]] for a in range(G.M)]
        gate_index = {p:i for i,p in enumerate(gates)}
        ends = G.endpoints(m)
        count = 0
        for code,g in enumerate(ends):
            if g:
                continue
            word = G.decode(code,m)
            for i in range(m-1):
                a,b = word[i:i+2]
                bab = gate_index[c.compose(gates[b],c.compose(gates[a],gates[b]))]
                aba = gate_index[c.compose(gates[a],c.compose(gates[b],gates[a]))]
                choices = [(b,bab),(aba,a)]
                if a == b:
                    choices += [(s,s) for s in range(G.M)]
                for x,y in choices:
                    intermediate = word.copy()
                    intermediate[i] = x
                    p = 0
                    for t in intermediate:
                        p = G.next[p][t]
                    assert G.defects[p] <= 2
                    intermediate[i+1] = y
                    p = 0
                    for t in intermediate:
                        p = G.next[p][t]
                    assert p == 0
                    count += 1
        channel_checks.append({'N':n,'m':m,'channels':count})
    records.append({'kind':'two_edit_exact_move_simulation','cases':channel_checks})

    # Refute the tempting strict-descent argument with a smallest checked
    # example. Every possible one-gate replacement is inspected.
    G = c.Group(4)
    ends,codes,index,rows,_ = c.graph(G,4,2)
    witness = None
    for i,code in enumerate(codes):
        if ends[code] == 0 or any(ends[codes[j]] == 0 for j in rows[i]):
            continue
        for j in rows[i]:
            terminal = next((z for z in rows[j] if ends[codes[z]] == 0),None)
            if terminal is not None:
                path = [code,codes[j],codes[terminal]]
                witness = {'word_path':[[G.edges[t] for t in G.decode(z,4)] for z in path],
                           'endpoint_path':[G.perms[ends[z]] for z in path],
                           'defect_path':[G.defects[ends[z]] for z in path],
                           'checked_single_gate_replacements':4*(G.M-1),
                           'strict_descent_neighbor_count':0}
                break
        if witness:
            break
    assert witness is not None
    records.append({'kind':'strict_descent_refuted',**witness})

    # Exact first-equal-pair cut in the all-size length-four quotient.
    cut_records = []
    for n in [4,5,6,8,14,20,50,100]:
        words = q.states(n,4,2)
        attrs = [q.data(w) for w in words]
        weights = [math.prod(range(n-v+1,n+1))//2**b for v,_,_,b in attrs]
        allowed = set(words)
        total = sum(weights)
        mass_numerator = 0
        boundary = 0
        M = n*(n-1)//2
        for w,weight in zip(words,weights):
            if w[0] != w[1]:
                continue
            mass_numerator += weight
            for i in (0,1):
                for replacement,multiplicity in q.extensions(w,n):
                    new = q.canonical(w[:i]+(replacement,)+w[i+1:])
                    if new in allowed and new[0] != new[1]:
                        boundary += weight*multiplicity
        assert mass_numerator == M**3
        phi = Fraction(boundary,8*M*mass_numerator)
        rayleigh = Fraction(boundary*total,8*M*mass_numerator*(total-mass_numerator))
        assert phi <= Fraction(5,2*M)
        if n >= 14:
            assert 2*mass_numerator <= total
            assert rayleigh <= Fraction(5,M)
        cut_records.append({'N':n,'allowed_words':total,'cut_words':mass_numerator,
                            'boundary_channels':boundary,'conductance':str(phi),
                            'indicator_rayleigh':str(rayleigh),
                            'M_times_rayleigh':str(M*rayleigh)})
    records.append({'kind':'first_equal_pair_cut','cases':cut_records})

    manifest = {'kind':'manifest','commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                'python':platform.python_version(),'dependencies':'standard library only',
                'command':'python3 -B experiments/20261026-141337-relaxed-endpoint-refresh/audit.py',
                'seeds':[],'deterministic':True,
                'sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                          for name in ['audit.py','check.py','quotient.py','results.jsonl','quotient.jsonl']}}
    with (HERE/'audit.jsonl').open('w') as out:
        for record in [manifest]+records:
            out.write(json.dumps(record,sort_keys=True)+'\n')
    for record in records:
        print(json.dumps(record,sort_keys=True),flush=True)


if __name__ == '__main__':
    main()
