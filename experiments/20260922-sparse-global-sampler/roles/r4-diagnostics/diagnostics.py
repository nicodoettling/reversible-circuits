#!/usr/bin/env python3
"""Independent exact H0 certificates and marked-component diagnostics.

Counts concern labeled ordered transposition words, rightmost factor first.
No old code is imported. The connected recurrence is the separately recorded
DYZ dependency; tiny independent labeled-walk checks audit normalization.
Run under python3 -B. All substantive arithmetic is integer or Fraction.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
from math import comb, factorial
from pathlib import Path
import platform
import subprocess
import sys
import time


def cutoff(n, m):
    if n < 1 or m < 0:
        raise ValueError('cutoff requires n >= 1, m >= 0')
    budget = (n + m + 2) ** 4
    k = 1
    while k < n and (k + 1) ** (2 * (k + 1)) <= budget:
        k += 1
    return k


def genus(v, ell):
    if v < 2 or ell < 2*v-2 or ell % 2:
        return None
    return (ell - 2*v + 2)//2


def h0_allowed(v, ell, k):
    g = genus(v, ell)
    return (v == 1 and ell == 0) or (g is not None and (v <= k or g <= 1))


def connected_counts(m_max):
    """Independent two-stage positive recurrence; C(1,0)=1.

    Degrees > m_max//2+1 have no connected nontrivial entries.
    """
    vmax = m_max//2 + 1
    c = [[0]*(m_max+1) for _ in range(vmax+1)]
    c[1][0] = 1
    choose = [[comb(n,k) for k in range(n+1)] for n in range(m_max+1)]
    for v in range(2, vmax+1):
        numerators = [0]*(m_max+1)
        for a in range(1,v):
            b = v-a
            conv = [0]*(m_max+1)
            for i in range(0,m_max+1,2):
                if not c[a][i]:
                    continue
                for j in range(0,m_max-i+1,2):
                    if c[b][j]:
                        conv[i+j] += choose[i+j][i]*c[a][i]*c[b][j]
            outer = 2*comb(v,a)*b*b
            for s in range(0,m_max+1,2):
                if not conv[s]:
                    continue
                for r in range(2,m_max-s+1,2):
                    numerators[s+r] += outer*choose[s+r][r]*a**(r+1)*conv[s]
        divisor = v*v*(v-1)
        for ell in range(0,m_max+1,2):
            c[v][ell], rem = divmod(numerators[ell],divisor)
            assert rem == 0, (v,ell,rem)
    return c


def active_counts(c, m_max, allowed=lambda v,ell: True):
    """F[s][m] counts identity words with every one of s labels active.

    Isolates are excluded here, hence s<=m. Recursion distinguishes the
    least active label. Arbitrary ambient N enters only via binom(N,s).
    """
    f = [[0]*(m_max+1) for _ in range(m_max+1)]
    f[0][0] = 1
    components = [(v,ell,c[v][ell]) for v in range(2,len(c))
                  for ell in range(2*v-2,m_max+1,2)
                  if c[v][ell] and allowed(v,ell)]
    choose = [[comb(n,k) for k in range(n+1)] for n in range(m_max+1)]
    for s in range(2,m_max+1):
        for v,ell,cv in components:
            if v > s:
                continue
            label_weight = choose[s-1][v-1]*cv
            for rest_len in range(0,m_max-ell+1,2):
                rest = f[s-v][rest_len]
                if rest:
                    f[s][rest_len+ell] += label_weight*choose[rest_len+ell][ell]*rest
    return f


def evaluator(f):
    @lru_cache(None)
    def total(n,m):
        if n < 0 or m < 0 or m >= len(f[0]):
            return 0
        if m == 0:
            return 1
        return sum(comb(n,s)*f[s][m] for s in range(2,min(n,m,len(f)-1)+1))
    return total


def permutation_totals(n,m_max):
    ident = tuple(range(n))
    layer = {ident:1}
    out = [1]
    edges = tuple(combinations(range(n),2))
    for _ in range(m_max):
        nxt = Counter()
        for p,w in layer.items():
            for a,b in edges:
                q = list(p)
                q[a],q[b] = q[b],q[a]
                nxt[tuple(q)] += w
        layer = nxt
        out.append(layer.get(ident,0))
    return out


def walk_macros(n,m):
    """Independent forward DP with literal labeled weighted support blocks."""
    ident = tuple(range(n))
    initial = tuple((1<<i,0) for i in range(n))
    layer = {(ident,initial):1}
    edges = tuple(combinations(range(n),2))
    for _ in range(m):
        nxt = Counter()
        for (p,blocks),w in layer.items():
            for a,b in edges:
                q = list(p)
                q[a],q[b] = q[b],q[a]
                hit = [(mask,ell) for mask,ell in blocks if mask & ((1<<a)|(1<<b))]
                mask = 0
                ell = 1
                for submask,length in hit:
                    mask |= submask
                    ell += length
                rest = [(submask,length) for submask,length in blocks if not submask & mask]
                new_blocks = tuple(sorted(rest+[(mask,ell)]))
                nxt[tuple(q),new_blocks] += w
        layer = nxt
    return {blocks:w for (p,blocks),w in layer.items() if p == ident}


def rational(value):
    value = Fraction(value)
    return {'numerator':value.numerator,'denominator':value.denominator,
            'decimal':float(value)}


def marked_numerator(n,m,v,ell,c,total):
    if v > n or ell > m:
        return 0
    return comb(n,v)*comb(m,ell)*c[v][ell]*total(n-v,m-ell)


def marked_pair_numerator(n,m,v,ell,w,j,c,total):
    """Ordered distinct components; same type gives X(X-1), not X^2."""
    if v+w > n or ell+j > m:
        return 0
    return (comb(n,v)*comb(n-v,w)*comb(m,ell)*comb(m-ell,j)
            *c[v][ell]*c[w][j]*total(n-v-w,m-ell-j))


def exact_checks(c,f,m_max):
    total = evaluator(f)
    tiny_m = min(m_max,12)
    tiny_n = min(6,len(c)-1)
    walk = [permutation_totals(n,tiny_m) for n in range(tiny_n+1)]
    recovered = [[0]*(tiny_m+1) for _ in range(tiny_n+1)]
    count_cells = 0
    for n in range(tiny_n+1):
        for m in range(tiny_m+1):
            assert total(n,m) == walk[n][m], ('total',n,m)
            full_support = sum((-1)**(n-s)*comb(n,s)*walk[s][m] for s in range(n+1))
            assert f[n][m] == full_support, ('active',n,m)
            if n:
                recovered[n][m] = walk[n][m] - sum(
                    comb(n-1,v-1)*comb(m,ell)*recovered[v][ell]*walk[n-v][m-ell]
                    for v in range(1,n) for ell in range(m+1))
                assert recovered[n][m] == c[n][m], ('connected',n,m)
            count_cells += 1
    cases = [(1,0),(1,2),(2,0),(2,2),(2,3),(2,6),(2,12),
             (3,4),(4,4),(4,6),(3,6),(3,8),(4,8),(4,10)]
    rows = []
    cached_f = {}
    for n,m in cases:
        if m > m_max:
            continue
        macros = walk_macros(n,m)
        z = total(n,m)
        assert sum(macros.values()) == z
        for k in sorted({2,cutoff(n,m)}):
            if k not in cached_f:
                cached_f[k] = active_counts(c,m_max,lambda v,ell:h0_allowed(v,ell,k))
            za = evaluator(cached_f[k])(n,m)
            kept = 0
            marked = Counter()
            bad_histogram = Counter()
            for macro,weight in macros.items():
                counts = Counter((mask.bit_count(),ell) for mask,ell in macro if ell)
                bad = sum(num for (v,ell),num in counts.items() if not h0_allowed(v,ell,k))
                bad_histogram[bad] += weight
                if bad == 0:
                    kept += weight
                for typ,num in counts.items():
                    marked[typ] += num*weight
                # Labeled macro multiplicity retains position interleavings.
                predicted = Fraction(factorial(m))
                for mask,ell in macro:
                    predicted *= Fraction(c[mask.bit_count()][ell],factorial(ell))
                assert predicted == weight, ('literal-macro',n,m,macro)
            assert za == kept and z-za == sum(w for j,w in bad_histogram.items() if j)
            for (v,ell),num in marked.items():
                assert num == marked_numerator(n,m,v,ell,c,total), ('marked',n,m,v,ell)
            bad_types = [(v,ell) for v,ell in marked if not h0_allowed(v,ell,k)]
            second = sum(marked_pair_numerator(n,m,v,ell,w,j,c,total)
                         for v,ell in bad_types for w,j in bad_types)
            assert second == sum(j*(j-1)*w for j,w in bad_histogram.items())
            rows.append({'N':n,'m':m,'K':k,'actual_K':cutoff(n,m),
                         'cutoff_kind':'H0' if k == cutoff(n,m) else 'diagnostic_override',
                         'Z':z,'Z_allowed':za,'Z_excluded':z-za,
                         'bad_component_histogram':dict(sorted(bad_histogram.items())),
                         'labeled_macro_count':len(macros)})
    boundaries=[]
    for n in range(1,25):
        for m in range(0,41):
            k=cutoff(n,m)
            assert k**(2*k) <= (n+m+2)**4
            assert k == n or (k+1)**(2*(k+1)) > (n+m+2)**4
    for k in range(2,9):
        # Perfect fourth-power budgets when k is even: at N+m+2=k^(k/2).
        if k%2 == 0:
            boundary=k**(k//2)
            n=max(k,boundary-2)
            if n+2 == boundary:
                boundaries.append({'K':k,'N':n,'m':0,'at':cutoff(n,0),
                                   'before':cutoff(n-1,0) if n>k else None})
    return {'count_cells':count_cells,'tiny_n_max':tiny_n,'tiny_m_max':tiny_m,
            'checks':['total permutation DP','connected proper-component subtraction',
                      'active-support binomial inversion','weighted support DP',
                      'labeled macro multiplicity','marked first factorial moments',
                      'marked second factorial moment','full minus allowed','integer cutoff'],
            'cases':rows,'cutoff_boundary_cases':boundaries}


def certificate(n,m,c,full_f,allowed_f,g01_f,size_f,k=None):
    actual_k=cutoff(n,m)
    k=actual_k if k is None else k
    total=evaluator(full_f)
    z=total(n,m)
    za=evaluator(allowed_f)(n,m)
    zg=evaluator(g01_f)(n,m)
    zs=evaluator(size_f)(n,m)
    if z == 0:
        return {'N':n,'m':m,'K':k,'actual_K':actual_k,'Z':z,'Z_allowed':za,'status':'empty'}
    marks=[]
    numerators=Counter()
    bad_types=[]
    for v in range(2,min(n,len(c)-1)+1):
        for ell in range(2*v-2,m+1,2):
            weight=marked_numerator(n,m,v,ell,c,total)
            if not weight:
                continue
            g=genus(v,ell)
            kind=('large' if v>k else 'small')+('_high_genus' if g>=2 else '_g01')
            numerators[kind]+=weight
            if v>k and g>=2:
                bad_types.append((v,ell))
                marks.append({'v':v,'ell':ell,'g':g,'expected_count':rational(Fraction(weight,z))})
    excluded_expected=numerators['large_high_genus']
    second=sum(marked_pair_numerator(n,m,v,ell,w,j,c,total)
               for v,ell in bad_types for w,j in bad_types)
    assert 0 <= z-za <= excluded_expected
    assert 2*(z-za) >= 2*excluded_expected-second
    return {'N':n,'m':m,'K':k,'actual_K':actual_k,
            'cutoff_kind':'H0' if k==actual_k else 'diagnostic_override',
            'T0_range':m%2==0 and m**5<=n**3,
            'Z':z,'Z_allowed':za,'Z_excluded':z-za,
            'omitted_mass':rational(Fraction(z-za,z)),
            'large_support_event':rational(Fraction(z-zs,z)),
            'high_genus_event':rational(Fraction(z-zg,z)),
            'marked_category_expectations':{name:rational(Fraction(num,z)) for name,num in sorted(numerators.items())},
            'excluded_second_factorial_moment':rational(Fraction(second,z)),
            'excluded_component_types':marks}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--m-max',type=int,default=48)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--skip-checks',action='store_true')
    args=parser.parse_args()
    assert 12 <= args.m_max <= 160
    start=time.monotonic()
    c=connected_counts(args.m_max)
    f=active_counts(c,args.m_max)
    checks={} if args.skip_checks else exact_checks(c,f,args.m_max)
    g01=active_counts(c,args.m_max,lambda v,ell:genus(v,ell)<=1)
    ns=[2,3,4,8,16,32,64,128,512,2048,10_000,1_000_000]
    instances=[]
    for n in ns:
        lengths={0,2,min(args.m_max,2*n),args.m_max}
        lengths.update(range(4,args.m_max+1,4))
        lengths.update(ell for ell in range(0,args.m_max+1,2) if ell**5<=n**3 and (ell+2)**5>n**3)
        instances.extend((n,m) for m in sorted(lengths))
    needed=sorted({cutoff(n,m) for n,m in instances}|{2})
    cached={}
    for k in needed:
        cached[k]=(active_counts(c,args.m_max,lambda v,ell:h0_allowed(v,ell,k)),
                   active_counts(c,args.m_max,lambda v,ell:v<=k))
    rows=[]
    for n,m in instances:
        k=cutoff(n,m)
        allowed,size=cached[k]
        rows.append(certificate(n,m,c,f,allowed,g01,size))
    for n,m in [(3,8),(4,10),(6,16),(10,20),(64,16),(128,16)]:
        if m<=args.m_max:
            allowed,size=cached[2]
            rows.append(certificate(n,m,c,f,allowed,g01,size,2))
    data={'version':'R4-DIAG.v1','target':'global Unif(Omega(N,m)); H0 exact retained subset',
          'convention':'(alpha beta)(x)=alpha(beta(x)); rightmost factor first',
          'status':'exact finite arithmetic; connected recurrence remains imported dependency',
          'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
          'python':platform.python_version(),'dependencies':{},'seed':None,
          'command':sys.argv,'m_max':args.m_max,'checks':checks,'rows':rows,
          'connected_counts':c,'seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'seconds':data['seconds'],'rows':len(rows),'check_cases':len(checks.get('cases',[])),
                      'nonzero_H0_in_range':[{key:r[key] for key in ['N','m','K','omitted_mass']}
                           for r in rows if r['cutoff_kind']=='H0' and r['T0_range'] and r['Z_excluded']],
                      'first_nonzero_H0':next(({key:r[key] for key in ['N','m','K','omitted_mass']}
                           for r in rows if r['cutoff_kind']=='H0' and r['Z_excluded']),None)},indent=2))


if __name__=='__main__':
    main()
