#!/usr/bin/env python3
"""Independent bounded exact checks for blind R5 review; no dependencies."""
from collections import defaultdict
from fractions import Fraction
from math import factorial, comb
from pathlib import Path
import datetime, hashlib, json, platform, subprocess, time

MAX_N=7
MAX_M=12
OUT=Path(__file__).resolve().parent

def all_bridge_counts(n,max_m):
    identity=tuple(range(n)); states={identity:1}; result=[1]
    edges=[(a,b) for a in range(n) for b in range(a+1,n)]
    for ell in range(1,max_m+1):
        nxt=defaultdict(int)
        for p,c in states.items():
            for a,b in edges:
                q=list(p); q[a],q[b]=q[b],q[a]
                nxt[tuple(q)]+=c
        states=nxt
        result.append(states.get(identity,0))
    return result

start=time.monotonic()
B={0:[1]+[0]*MAX_M}
for n in range(1,MAX_N+1): B[n]=all_bridge_counts(n,MAX_M)
C={}
for n in range(1,MAX_N+1):
    C[n]=[]
    for ell in range(MAX_M+1):
        excluded=sum(comb(n-1,v-1)*comb(ell,j)*C[v][j]*B[n-v][ell-j]
            for v in range(1,n) for j in range(ell+1))
        C[n].append(B[n][ell]-excluded)
        assert C[n][-1]>=0

recurrence=[]
for n in range(2,MAX_N+1):
    for ell in range(MAX_M+1):
        rhs=Fraction(0)
        for k in range(1,n):
            for j in range(2,ell+1,2):
                for a in range(ell-j+1):
                    b=ell-j-a
                    rhs+=Fraction(k*(n-k)**2*2*k**j*C[k][a]*C[n-k][b],factorial(j)*factorial(k)*factorial(a)*factorial(n-k)*factorial(b))
        rhs/=n*n*(n-1)
        lhs=Fraction(C[n][ell],factorial(n)*factorial(ell))
        assert lhs==rhs,(n,ell,lhs,rhs)
        recurrence.append({'n':n,'m':ell,'connected':C[n][ell],'normalized':str(lhs)})

insertions=[]
for n in range(2,MAX_N+1):
    for m in range(2,min(n,MAX_M)+1,2):
        k=m//2
        for r in range(1,k+1):
            actual=Fraction(B[n][m-2*r]*factorial(m),B[n][m]*factorial(m-2*r))
            bound=Fraction(4*k,(n-2*k+1)**2)**r
            sharper=Fraction(4**r*factorial(k)//factorial(k-r),factorial(n-2*k+2*r)//factorial(n-2*k))
            assert actual<=sharper<=bound,(n,m,r,actual,sharper,bound)
            insertions.append({'N':n,'m':m,'r':r,'actual':str(actual),'sharp_bound':str(sharper),'bound':str(bound)})

for n in range(2,MAX_N+1):
    ell=2*n-2
    expected=Fraction(factorial(ell)*n**max(0,n-3),n if n==2 else 1)
    assert C[n][ell]==expected

result={'status':'all checks passed','parameters':{'max_n':MAX_N,'max_m':MAX_M},'composition':'rightmost first; append transposition by swapping permutation image entries','bridge_counts':B,'connected_counts':C,'recurrence_checks':recurrence,'insertion_checks':insertions,'elapsed_seconds':time.monotonic()-start,'provenance':{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'dependencies':'standard library only','seed':'none: exhaustive deterministic computation','command':'timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r5-referee/exact_checks.py','git_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
(OUT/'exact_checks.results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'recurrence_checks':len(recurrence),'insertion_checks':len(insertions),'elapsed_seconds':result['elapsed_seconds']}))
