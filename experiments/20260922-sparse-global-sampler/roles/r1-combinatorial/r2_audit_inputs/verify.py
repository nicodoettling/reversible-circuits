#!/usr/bin/env python3
"""Small independent exact checks of R2-A.v1. Standard library, no old imports."""
import collections
from fractions import Fraction as Q
import itertools
import json
import math
import pathlib
import platform
import subprocess
import time

ROOT=pathlib.Path(__file__).resolve().parent

def connected_h(vmax,gmax):
    h={(1,g):Q(g==0) for g in range(gmax+1)}
    for v in range(2,vmax+1):
        for g in range(gmax+1):
            t=Q(0)
            for a in range(1,v):
                b=v-a
                for r in range(g+1):
                    for i in range(g-r+1):
                        j=g-r-i
                        t+=Q(a**(2*r+3)*b*b,math.factorial(2*r+2))*h[a,i]*h[b,j]
            h[v,g]=Q(2,v*v*(v-1))*t
    return h

def connected_counts(h,nmax,mmax):
    C={(1,0):1}
    for n in range(1,nmax+1):
        for m in range(mmax+1):
            if (n,m)==(1,0): continue
            g=(m-2*n+2)//2
            value=Q(0)
            if n>=2 and m%2==0 and g>=0 and (n,g) in h:
                value=h[n,g]*math.factorial(n)*math.factorial(m)
            assert value.denominator==1
            C[n,m]=int(value)
    return C

def assembly(C,nmax,mmax):
    Z={(0,m):int(m==0) for m in range(mmax+1)}
    for n in range(1,nmax+1):
        for m in range(mmax+1):
            Z[n,m]=sum(math.comb(n-1,v-1)*math.comb(m,l)*C[v,l]*Z[n-v,m-l]
                for v in range(1,n+1) for l in range(m+1))
    return Z

def classify(word,n):
    perm=list(range(n)); parent=list(range(n))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for a,b in word:
        perm[a],perm[b]=perm[b],perm[a] # right multiplication
        ra,rb=find(a),find(b)
        parent[ra]=rb
    if perm!=list(range(n)): return None
    blocks=collections.defaultdict(list)
    for a in range(n): blocks[find(a)].append(a)
    lens=collections.Counter(find(a) for a,b in word)
    return tuple(sorted((len(B),lens[r]) for r,B in blocks.items()))

def main():
    t0=time.monotonic(); rows=[]
    h=connected_h(12,12)
    majorant_cells=0
    for v in range(1,13):
        B=Q(sum(j*j for j in range(1,v)),12)
        if v>=2: assert h[v,0]*math.factorial(v)==Q(v**max(v-3,0),v**max(3-v,0))
        for g in range(13):
            assert h[v,g]<=h[v,0]*B**g/math.factorial(g),(v,g)
            majorant_cells+=1
    rows.append({'check':'factorial_majorant','v':[1,12],'g':[0,12],'cells':majorant_cells,'passed':True})
    C=connected_counts(h,12,16); Z=assembly(C,12,16)
    incidence_cells=0
    for n in range(2,13):
        for k in range(n//2+1):
            for p in range(k+1):
                lhs=Q(Z[n,2*(k-p)],math.factorial(2*(k-p))) / Q(Z[n,2*k],math.factorial(2*k))
                ff=lambda a,b:math.factorial(a)//math.factorial(a-b)
                rhs=Q(4**p*ff(k,p),ff(n-2*k+2*p,2*p))
                assert lhs<=rhs,(n,k,p,lhs,rhs)
                incidence_cells+=1
    rows.append({'check':'matching_incidence_ratio','N':[2,12],'k':'0..floor(N/2)','p':'0..k','cells':incidence_cells,'passed':True})
    for n,m in [(3,4),(4,4),(4,6),(2,0),(2,2),(2,12),(1,0),(3,6)]:
        edges=list(itertools.combinations(range(n),2)); profiles=collections.Counter()
        for word in itertools.product(edges,repeat=m):
            profile=classify(word,n)
            if profile is not None: profiles[profile]+=1
        actual=sum(profiles.values())
        assert actual==Z[n,m],(n,m,actual,Z[n,m])
        marked=collections.Counter()
        for profile,count in profiles.items():
            for typ in profile: marked[typ]+=count
        for v in range(1,n+1):
            for ell in range(m+1):
                expected=math.comb(n,v)*math.comb(m,ell)*C[v,ell]*Z[n-v,m-ell]
                assert marked[v,ell]==expected,(n,m,v,ell,marked[v,ell],expected)
        rows.append({'check':'raw_word_marked_identity','N':n,'m':m,'words':actual,'profiles':len(profiles),'passed':True,
            'marked_counts':{f'{v},{ell}':z for (v,ell),z in sorted(marked.items())}})
    # Independent exact kernel factor inequality and superadditivity.
    for r in range(101): assert math.factorial(2*r+2)>=2*12**r*math.factorial(r)
    for a in range(1,101):
        for b in range(1,101):
            S=lambda v:(v-1)*v*(2*v-1)//6
            assert S(a+b)>=S(a)+S(b)+a*a
    rows.append({'check':'coefficient_and_B_inequalities','r':[0,100],'a':[1,100],'b':[1,100],'passed':True})
    data={'claim_version':'R2-A.v1','status':'exact_finite_checks_only','commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
          'python':platform.python_version(),'dependencies':'standard library','seed':None,'method':'deterministic exact rational/integer checks',
          'command':'python3 -B experiments/20260922-sparse-global-sampler/roles/r2-analytic/verify.py',
          'elapsed_seconds':time.monotonic()-t0,'checks':rows}
    (ROOT/'results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'passed':len(rows),'elapsed_seconds':data['elapsed_seconds'],'output':str(ROOT/'results.json')}))

if __name__=='__main__': main()
