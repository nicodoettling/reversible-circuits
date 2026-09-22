#!/usr/bin/env python3
"""Exact g<=1 coverage certificate, using the September 5 positive count code.

The independent checks use labeled permutation DP and direct support-word
enumeration, never the DYZ recurrence as their reference. All arithmetic is
integer/Fraction and all tests are deterministic. Run with python3 -B.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
COUNT_SOURCE = ROOT / 'experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py'
SPEC = importlib.util.spec_from_file_location('genus_one_historical_counts', COUNT_SOURCE)
counts = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = counts
SPEC.loader.exec_module(counts)


def allowed(v, ell):
    return (v == 1 and ell == 0) or (v >= 2 and ell in (2*v-2, 2*v))


def permutation_totals(n, m_max):
    """Independent exact ordinary permutation walk, right composition."""
    identity = tuple(range(n))
    layer = {identity: 1}
    result = [1]
    edges = list(combinations(range(n), 2))
    for _ in range(m_max):
        nxt = Counter()
        for p, weight in layer.items():
            for a, b in edges:
                q = list(p)
                q[a], q[b] = q[b], q[a]
                nxt[tuple(q)] += weight
        layer = nxt
        result.append(layer.get(identity, 0))
    return result


def recover_connected(totals, m_max):
    """Subtract proper least-label components from independent totals."""
    c = [[0]*(m_max+1) for _ in totals]
    for n in range(1, len(totals)):
        for m in range(m_max+1):
            proper = sum(comb(n-1,v-1)*comb(m,k)*c[v][k]*totals[n-v][m-k]
                         for v in range(1,n) for k in range(m+1))
            c[n][m] = totals[n][m] - proper
    return c


def exact_checks(c, z, z01):
    m_max = min(12, len(c[0])-1)
    n_max = min(6, len(c)-1)
    totals = [permutation_totals(n,m_max) for n in range(n_max+1)]
    recovered = recover_connected(totals,m_max)
    cells = 0
    for n in range(n_max+1):
        for m in range(m_max+1):
            assert z[n][m] == totals[n][m], (n,m,'total')
            assert c[n][m] == recovered[n][m], (n,m,'connected')
            cells += 1
    cases = [(0,0),(1,0),(1,2),(2,0),(2,2),(2,3),(2,4),
             (3,4),(3,6),(4,4),(4,6),(4,8)]
    rows = []
    for n,m in cases:
        if n >= len(c) or m >= len(c[0]):
            continue
        total = good = connected = 0
        probs = Counter()
        good_macros = Counter()
        for w in counts.identity_words(n,m):
            total += 1
            macro = counts.support_macro(n,w)
            connected += int(n >= 1 and len(macro) == 1)
            is_good = all(allowed(len(b),ell) for b,ell in macro)
            if is_good:
                good += 1
                good_macros[macro] += 1
                p = counts.assembly_word_probability(n,w,c,z01)
                probs[p] += 1
        assert total == z[n][m]
        assert good == z01[n][m]
        assert connected == c[n][m]
        if good:
            assert probs == Counter({Fraction(1,good):good})
        for macro,multiplicity in good_macros.items():
            weight = Fraction(factorial(m))
            for b,ell in macro:
                weight *= Fraction(c[len(b)][ell],factorial(ell))
            assert weight.denominator == 1 and int(weight) == multiplicity
        rows.append({'N':n,'m':m,'all':total,'connected':connected,
                     'g_le_1':good,'macro_types':len(good_macros),
                     'per_word_probability':str(Fraction(1,good)) if good else None})
    return {'independent_count_cells':cells,'cases':rows,
            'word_law':'every allowed literal word has probability exactly 1/Z_g_le_1'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n-max', type=int, default=48)
    parser.add_argument('--m-max', type=int, default=96)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert 4 <= args.n_max <= 80 and 8 <= args.m_max <= 160
    t = time.monotonic()
    c = counts.connected_counts(args.n_max,args.m_max)
    z = counts.assembly_counts(args.n_max,args.m_max,c)
    z01 = counts.assembly_counts(args.n_max,args.m_max,c,allowed)
    checks = exact_checks(c,z,z01)
    rows = []
    for n in range(2,args.n_max+1):
        for m in sorted({0,2,2*(n//4),2*(n//2),2*n-2,2*n}):
            if m > args.m_max:
                continue
            ratio = Fraction(z01[n][m],z[n][m])
            rows.append({'N':n,'m':m,'Z':z[n][m],'Z_g_le_1':z01[n][m],
                         'covered_numerator':ratio.numerator,'covered_denominator':ratio.denominator,
                         'covered_decimal':float(ratio),'omitted_decimal':float(1-ratio)})
    # At m=2N the g<=1 support condition forces all N labels active and
    # every component to have genus exactly one. Check a separate recurrence.
    saturated = [0]*(args.n_max+1)
    saturated[0] = 1
    for n in range(1,min(args.n_max,args.m_max//2)+1):
        saturated[n] = sum(comb(n-1,v-1)*comb(2*n,2*v)*c[v][2*v]*saturated[n-v]
                           for v in range(2,n+1))
        assert saturated[n] == z01[n][2*n]
        if n >= 2:
            assert 24*c[n][2*n] <= factorial(2*n)*n**n
            assert z01[n][2*n] <= factorial(2*n)*factorial(n)*6**n
    # The finite subgroup lower bound is a consequence of exact Cauchy-
    # Schwarz, not a fit to the table. Validate every available r,N pair.
    subgroup_checks = 0
    for n in range(2,min(args.n_max,args.m_max//2)+1):
        for r in range(2,n+1):
            assert z[n][2*n]*factorial(r) >= 2*comb(r,2)**(2*n)
            subgroup_checks += 1
    data = {'target':'global uniform Omega(N,m); covered subset every component genus <=1',
            'sampling_theorem_status':'conditional on accepted connected primitives',
            'python':platform.python_version(),'dependencies':{},'seed':None,
            'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'command':' '.join(sys.argv),'n_max':args.n_max,'m_max':args.m_max,
            'count_source':str(COUNT_SOURCE.relative_to(ROOT)),
            'count_source_sha256':hashlib.sha256(COUNT_SOURCE.read_bytes()).hexdigest(),
            'checks':checks,'saturated_m_2N_recurrence_checked':True,
            'omission_inequalities_checked':True,'subgroup_bound_checks':subgroup_checks,
            'rows':rows,'seconds':time.monotonic()-t}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'seconds':data['seconds'],'rows':len(rows),'checks':checks,
                      'm_2N_rows':[r for r in rows if r['m']==2*r['N'] and r['N'] in (2,3,4,8,16,32,48,64)]},indent=2))


if __name__ == '__main__':
    main()
