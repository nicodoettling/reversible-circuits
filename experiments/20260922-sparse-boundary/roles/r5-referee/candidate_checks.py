#!/usr/bin/env python3
"""Fresh exact checks for finite component bounds, independent of R3 artifacts."""
from collections import defaultdict
from fractions import Fraction as F
from math import comb,factorial,prod
from pathlib import Path
import json,platform,subprocess

def counts(n,M):
    e=tuple(range(n)); states={(e,e):1}; conn={}; totals={}
    for ell in range(M+1):
        conn[ell]=states.get((e,(0,)*n),0)
        totals[ell]=sum(c for (p,s),c in states.items() if p==e)
        if ell==M:break
        nxt=defaultdict(int)
        for (p,s),c in states.items():
            for i in range(n):
                for j in range(i+1,n):
                    a=list(p);a[i],a[j]=a[j],a[i]
                    lo,hi=sorted((s[i],s[j])); z=tuple(lo if b==hi else b for b in s)
                    labels={}; z=tuple(labels.setdefault(b,len(labels)) for b in z)
                    nxt[(tuple(a),z)]+=c
        states=nxt
    return conn,totals
M=8; maxN=24
C={}; totals={}
for v in range(2,M//2+2): C[v],totals[v]=counts(v,M)
Z={}
for n in range(maxN+1):
    for ell in range(0,M+1,2):
        if n<=1: Z[n,ell]=int(ell==0);continue
        val=Z[n-1,ell]
        for v in range(2,min(n,ell//2+1)+1):
            for q in range(v-1,ell//2+1):
                val+=comb(n-1,v-1)*comb(ell,2*q)*C[v][2*q]*Z[n-v,ell-2*q]
        Z[n,ell]=val
for n,table in totals.items():
    for ell in range(0,M+1,2): assert Z[n,ell]==table[ell]
S=lambda n,k:F(Z[n,2*k],factorial(2*k))
cells=0;fgcells=0;majorants=0
for v in C:
    for q in range(v-1,M//2+1):
        g=q-v+1;b=F(v**3-v,36)
        assert F(C[v][2*q],factorial(2*q))<=F(v)**(v-3)*b**g/factorial(g)
        majorants+=1
for n in range(2,maxN+1):
    for k in range(1,min(M//2,n//2)+1):
        D=n-2*k+1
        for v in range(2,min(n,k+1)+1):
            h=k-v+1;b=F(v**3-v,36)
            ex=sum(F(comb(n,v)*C[v][2*q],factorial(2*q))*S(n-v,k-q)/S(n,k) for q in range(v-1,k+1))
            pref=F(comb(n,v))*F(v)**(v-3)*prod(range(k-v+2,k+1))*F(4,D*D)**(v-1)
            bound=pref*(1+4*b/(D*D))**h
            assert ex<=bound
            fgcells+=1
            for q in range(v-1,k+1):
                ratio=S(n-v,k-q)/S(n,k)
                weak=F(4**q*prod(range(k-q+1,k+1)),D**(2*q))
                strong=F(4**q*prod(range(k-q+1,k+1)),prod(range(D,D+2*q)))
                assert ratio<=strong<=weak
                cells+=1
# R2 monotonic threshold, checked without floating point.
assert 2**18*64**2<=2**32
assert 2*64**4>65**4
assert (16+2)**3<72*2**10
# Independent coefficient tests for normalized DYZ comparison L(z)<=exp(z²/12).
for j in range(31):assert F(2,factorial(2*j+2))<=F(1,12**j*factorial(j))
result={'status':'passed','kind':'exact finite checks; not asymptotic evidence','N_range':[2,maxN],'maximum_m':M,'component_genus_majorant_cells':majorants,'ratio_cells':cells,'finite_genus_sum_cells':fgcells,'normalization_crosscheck':'component recurrence agrees with permutation/support DP through N=5,m=8','python':platform.python_version(),'dependencies':'standard library only','seeds':'none: deterministic exact fractions','git_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'command':'timeout 90s python3 experiments/20260922-sparse-boundary/roles/r5-referee/candidate_checks.py','Z_rows':[{'N':n,'m':ell,'Z':Z[n,ell]} for n in range(maxN+1) for ell in range(0,M+1,2)]}
Path(__file__).with_name('candidate_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='Z_rows'}))
