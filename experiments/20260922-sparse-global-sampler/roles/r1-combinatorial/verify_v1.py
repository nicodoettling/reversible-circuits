#!/usr/bin/env python3
"""Deterministic exact falsification checks for R1 proof v1, no old imports."""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, platform, subprocess, time

ROOT=Path(__file__).resolve().parent

def connected_table(nmax,lmax):
    c=[[0]*(lmax+1) for _ in range(nmax+1)]
    c[1][0]=1
    for v in range(2,nmax+1):
        for ell in range(2*v-2,lmax+1,2):
            num=0
            for a in range(1,v):
                b=v-a
                for r in range(2,ell+1,2):
                    s=ell-r
                    conv=sum(comb(s,j)*c[a][j]*c[b][s-j] for j in range(0,s+1,2))
                    num+=2*comb(v,a)*b*b*comb(ell,r)*a**(r+1)*conv
            divisor=v*v*(v-1)
            assert num%divisor==0
            c[v][ell]=num//divisor
    return c

def total_table(c,nmax,lmax,predicate=lambda v,ell:True):
    z=[[0]*(lmax+1) for _ in range(nmax+1)]
    z[0][0]=1
    vmax=len(c)-1
    for n in range(1,nmax+1):
        for ell in range(0,lmax+1,2):
            z[n][ell]=sum(comb(n-1,v-1)*comb(ell,r)*c[v][r]*z[n-v][ell-r]
                for v in range(1,min(n,vmax)+1)
                for r in range(0,ell+1,2) if c[v][r] and predicate(v,r))
    return z

def canonical_partition(p):
    ren={}
    return tuple(ren.setdefault(x,len(ren)) for x in p)

def step(state,edge):
    perm,part=state; a,b=edge
    p=list(perm); p[a],p[b]=p[b],p[a]
    aa,bb=part[a],part[b]
    q=canonical_partition(tuple(aa if x==bb else x for x in part))
    return tuple(p),q

def support_dp(n,lmax):
    ident=tuple(range(n)); dp={(ident,ident):1}; rows=[]
    edges=list(combinations(range(n),2))
    for ell in range(lmax+1):
        total=sum(c for (p,q),c in dp.items() if p==ident)
        connected=sum(c for (p,q),c in dp.items() if p==ident and len(set(q))==1)
        rows.append((total,connected))
        nxt=defaultdict(int)
        for state,c in dp.items():
            for e in edges: nxt[step(state,e)]+=c
        dp=nxt
    return rows

def enumerate_marks(n,m):
    edges=list(combinations(range(n),2)); ident=tuple(range(n))
    total=0; marks=Counter(); macros=Counter()
    for w in product(edges,repeat=m):
        state=(ident,ident)
        for e in w: state=step(state,e)
        perm,part=state
        if perm!=ident: continue
        total+=1
        sizes=Counter(part); lengths=Counter(part[a] for a,b in w)
        signature=tuple(sorted((sizes[b],lengths[b]) for b in lengths))
        macros[signature]+=1
        for v,ell in signature: marks[(v,ell//2)]+=1
    return total,marks,macros

def rat(x): return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
def cutoff(n,m):
    return max(v for v in range(1,n+1) if v**(2*v)<=(n+m+2)**4)

def main():
    start=time.monotonic(); c=connected_table(13,24); z=total_table(c,128,24)
    out={'proof_sha256':hashlib.sha256((ROOT/'proof_v1.md').read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
         'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
         'command':'python3 -B experiments/20260922-sparse-global-sampler/roles/r1-combinatorial/verify_v1.py',
         'randomness':'none; exact deterministic tests','dependencies':'Python standard library',
         'domains':{},'counts':{},'examples':[]}
    # Independent endpoint plus support-partition transition DP.
    cells=0
    for n in range(1,5):
        for ell,(zt,ct) in enumerate(support_dp(n,12)):
            assert z[n][ell]==zt,(n,ell,'total')
            assert c[n][ell]==ct,(n,ell,'connected')
            cells+=1
    out['counts']['independent_support_dp_cells']=cells
    out['domains']['support_dp']='1<=N<=4, 0<=m<=12'
    # Convex recurrence weights and coefficient majorant.
    checked=0
    for v in range(2,14):
        weights=[F(comb(v,a)*a**a*(v-a)**(v-a-1),(v-1)*v**(v-1)) for a in range(1,v)]
        assert sum(weights)==1 and all(p>0 for p in weights)
        av0=F(v**max(v-3,0),v**max(3-v,0)); b=F(v**3-v,36)
        for ell in range(2*v-2,25,2):
            g=(ell-2*v+2)//2
            lhs=F(c[v][ell],factorial(ell)); rhs=av0*b**g/factorial(g)
            assert lhs<=rhs,(v,g,lhs,rhs)
            checked+=1
    for j in range(101):
        assert F(2,factorial(2*j+2))<=F(1,12**j*factorial(j))
    out['counts']['genus_majorant_cells']=checked
    out['counts']['elementary_series_coefficients']=101
    out['domains']['majorant']='2<=v<=13, 2v-2<=ell<=24; 0<=j<=100 for L coefficient'
    # Every available conditioned normalizer ratio in a bounded grid.
    checked=0; mark_checks=0; union_checks=0
    for n in range(2,21):
        for m in range(0,min(n,24)+1,2):
            k=m//2; d=n-m+1; sk=F(z[n][m],factorial(m))
            for v in range(0,n+1):
                for q in range(0,k+1):
                    residual=F(z[n-v][m-2*q],factorial(m-2*q))/sk
                    rhs=F(comb(k,q)*4**q*factorial(q),d**(2*q))
                    assert residual<=rhs,(n,m,v,q,residual,rhs)
                    checked+=1
            if k:
                x=F(4*k,d*d)
                for v in range(2,min(n,k+1)+1):
                    b=F(v**3-v,36); av0=F(v**max(v-3,0),v**max(3-v,0))
                    for q in range(v-1,k+1):
                        exact=F(comb(n,v)*comb(m,2*q)*c[v][2*q]*z[n-v][m-2*q],z[n][m])
                        bound=comb(n,v)*av0*b**(q-v+1)/factorial(q-v+1)*x**q
                        assert exact<=bound,(n,m,v,q)
                        mark_checks+=1
                for j in range(1,min(n,k+1)+1):
                    allowed=total_table(c,n,m,lambda v,ell: v<=j or (v==1 and ell==0))[n][m]
                    error=F(z[n][m]-allowed,z[n][m])
                    expected=sum(F(comb(n,v)*comb(m,2*q)*c[v][2*q]*z[n-v][m-2*q],z[n][m])
                        for v in range(j+1,min(n,k+1)+1) for q in range(v-1,k+1))
                    assert error<=expected,(n,m,j,error,expected)
                    union_checks+=1
    out['counts'].update(normalizer_ratios=checked,marked_majorants=mark_checks,union_bounds=union_checks)
    out['domains']['ratio_and_marks']='2<=N<=20, even 0<=m<=N; all v,q,J as feasible'
    # Literal enumeration gives mark identities without using the recurrence.
    enum=[]
    for n,m in [(3,4),(4,4),(4,6),(3,6),(3,8)]:
        total,marks,macros=enumerate_marks(n,m)
        assert total==z[n][m]
        for (v,q),count in marks.items():
            numerator=comb(n,v)*comb(m,2*q)*c[v][2*q]*z[n-v][m-2*q]
            assert count==numerator,(n,m,v,q,count,numerator)
        j=2
        bad=sum(count for sig,count in macros.items() if any(v>j and ell//2-v+1>=2 for v,ell in sig))
        enum.append({'N':n,'m':m,'Z':total,'marked_counts':{f'{v},{q}':n for (v,q),n in marks.items()},'K_test':j,'H0_bad_count_at_test_cutoff':bad})
    out['literal_enumeration']=enum
    # Nonzero true-H0 tail at a point in T0, plus high-genus included support.
    for n,m in [(128,16),(20,20),(3,8),(2,24)]:
        j=cutoff(n,m)
        allowed=total_table(c,n,m,lambda v,ell: v==1 or v<=j or ell<=2*v)[n][m]
        error=F(z[n][m]-allowed,z[n][m])
        expected=sum(F(comb(n,v)*comb(m,2*q)*c[v][2*q]*z[n-v][m-2*q],z[n][m])
            for v in range(j+1,min(n,m//2-1)+1) for q in range(v+1,m//2+1))
        assert error<=expected
        row={'N':n,'m':m,'K':j,'T0':m**5<=n**3,'T1':m**3<=n**2,'Z':str(z[n][m]),'ZA':str(allowed),'error':rat(error),'expected_excluded':rat(expected)}
        if n==128: assert error>0
        if n in (2,3): assert error==0
        out['examples'].append(row)
    out['elapsed_seconds']=time.monotonic()-start; out['all_assertions_passed']=True
    (ROOT/'results_v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_assertions_passed':True,'counts':out['counts'],'elapsed_seconds':out['elapsed_seconds'],'output':str(ROOT/'results_v1.json')}))

if __name__=='__main__': main()
