#!/usr/bin/env python3
"""Independent tiny-state DP; deterministic checks, not asymptotic evidence."""
from collections import defaultdict
from fractions import Fraction
from math import factorial,comb,log,exp
from pathlib import Path
import json,platform,subprocess

def connected_counts(n,max_m):
    ident=tuple(range(n)); states={(ident,ident):1}; out=[]
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    for m in range(max_m+1):
        total=sum(c for (p,part),c in states.items() if p==ident)
        connected=states.get((ident,(0,)*n),0)
        out.append((m,total,connected))
        if m==max_m:break
        nxt=defaultdict(int)
        for (p,part),c in states.items():
            for i,j in edges:
                q=list(p);q[i],q[j]=q[j],q[i]
                lo,hi=sorted((part[i],part[j])); z=tuple(lo if a==hi else a for a in part)
                ren={}; z=tuple(ren.setdefault(a,len(ren)) for a in z)
                nxt[(tuple(q),z)]+=c
        states=nxt
    return out

def genus0(n): return Fraction(factorial(2*n-2))*Fraction(n)**(n-3)
def genus1(n):
    bracket=Fraction(n*n-n)-sum(Fraction(factorial(j-2)*comb(n,j))*Fraction(n)**(2-j) for j in range(2,n+1))
    return Fraction(factorial(2*n)*n**(n-2),24)*bracket

rows=[]
for n in range(2,6):
    for m,total,conn in connected_counts(n,2*n):
        row=dict(N=n,m=m,all_identity=total,connected_identity=conn)
        if m==2*n-2:
            assert conn==genus0(n); row['checked_formula']='Vakil 1.5 genus zero'
        if m==2*n:
            assert conn==genus1(n); row['checked_formula']='Vakil 1.5 genus one'
        if m%2: assert total==0
        else:
            assert total*factorial(n)>=comb(n,2)**m
            row['cauchy_schwarz_lower_bound_verified']=True
        rows.append(row)
# Explicit threshold inequalities in the proof, using conservative margins.
L=1024.0
assert 4*log(L)+31<=L/16
assert 2*exp(1)+2*exp(2)+1<22
assert 22+log(16)+1+1.5*log(2)+2*log(6)<31
result=dict(status='passed',classification='finite formula checks only',python=platform.python_version(),git_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),command='timeout 90s python3 experiments/20260922-sparse-boundary/roles/r5-referee/finite_checks.py',seeds='none: deterministic exhaustive state aggregation',dependencies='Python standard library only',rows=rows,threshold_checks={'L':L,'lhs':4*log(L)+31,'rhs':L/16})
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'passed','rows':len(rows),'largest_N':5,'largest_m':10}))
