#!/usr/bin/env python3
"""Bounded exact rank-bijection audit for the blind small-component sampler."""
from functools import lru_cache
from itertools import combinations,product
from math import comb
from pathlib import Path
from collections import Counter
import datetime, hashlib,json,platform,subprocess,time

OUT=Path(__file__).resolve().parent

def merge(part,a,b):
    x,y=part[a],part[b]
    q=tuple(x if c==y else c for c in part)
    canonical={}
    return tuple(canonical.setdefault(c,len(canonical)) for c in q)

def edges(v): return tuple(combinations(range(v),2))

def trans(p,e):
    a,b=e; q=list(p);q[a],q[b]=q[b],q[a]
    return tuple(q)

@lru_cache(None)
def completions(v,r,p,part):
    if r==0: return int(p==tuple(range(v)) and len(set(part))==1)
    return sum(completions(v,r-1,trans(p,e),merge(part,*e)) for e in edges(v))

def connected(v,ell): return completions(v,ell,tuple(range(v)),tuple(range(v)))

def local_unrank(v,ell,rank):
    p=part=tuple(range(v));word=[]
    for r in range(ell,0,-1):
        for e in edges(v):
            q,pp=trans(p,e),merge(part,*e)
            weight=completions(v,r-1,q,pp)
            if rank<weight:
                word.append(e);p,part=q,pp;break
            rank-=weight
        else: raise AssertionError('no local branch')
    assert rank==0 and p==tuple(range(v)) and len(set(part))==1
    return tuple(word)

@lru_cache(None)
def restricted_count(n,t,K):
    if n==0:return int(t==0)
    total=restricted_count(n-1,t,K)
    for v in range(2,min(K,n)+1):
        for ell in range(2*v-2,t+1,2):
            total+=comb(n-1,v-1)*comb(t,ell)*connected(v,ell)*restricted_count(n-v,t-ell,K)
    return total

def unrank(labels,t,K,rank):
    n=len(labels)
    if n==0:
        assert t==rank==0
        return ()
    iso=restricted_count(n-1,t,K)
    if rank<iso:return unrank(labels[1:],t,K,rank)
    rank-=iso
    for v in range(2,min(K,n)+1):
        for ell in range(2*v-2,t+1,2):
            lc=connected(v,ell); rc=restricted_count(n-v,t-ell,K)
            nlabels=comb(n-1,v-1);npositions=comb(t,ell)
            weight=nlabels*npositions*lc*rc
            if rank>=weight:
                rank-=weight;continue
            rank,rr=divmod(rank,rc)
            rank,lr=divmod(rank,lc)
            labelrank,posrank=divmod(rank,npositions)
            restlabels=tuple(combinations(labels[1:],v-1))[labelrank]
            chosen=(labels[0],)+restlabels
            other=tuple(z for z in labels if z not in chosen)
            local=tuple(tuple(chosen[a] for a in e) for e in local_unrank(v,ell,lr))
            remainder=unrank(other,t-ell,K,rr)
            positions=set(tuple(combinations(range(t),ell))[posrank])
            li=iter(local);ri=iter(remainder)
            return tuple(next(li) if j in positions else next(ri) for j in range(t))
    raise AssertionError('no assembly branch')

def evaluate(N,w):
    p=part=tuple(range(N));prefix=[]
    for e in w:
        p=trans(p,e);part=merge(part,*e)
        seen=set();cyc=[]
        for a in range(N):
            if a not in seen:
                l=0;b=a
                while b not in seen:seen.add(b);l+=1;b=p[b]
                cyc.append(l)
        prefix.append(tuple(sorted(cyc)))
    return p,part,tuple(prefix)

def diagnostic(N,words):
    out=Counter()
    for w in words:
        p,part,prefix=evaluate(N,w)
        out['identity_ok']+=int(p==tuple(range(N)))
        out['adjacent_repeats']+=sum(a==b for a,b in zip(w,w[1:]))
        for j,e in enumerate(w):out['edge_at_'+str(j)+'_'+str(e)]+=1
        out['component_sizes_'+str(tuple(sorted(Counter(part).values())))]+=1
        out['edge_multiplicities_'+str(tuple(sorted(Counter(w).values())))]+=1
        out['prefix_cycle_types_'+str(prefix)]+=1
    return dict(out)

start=time.monotonic();results=[]
for N,m,K in [(3,4,3),(4,4,4),(4,6,3),(4,6,4),(2,0,2),(2,2,2),(2,8,2)]:
    count=restricted_count(N,m,K)
    generated={unrank(tuple(range(N)),m,K,r) for r in range(count)}
    assert len(generated)==count
    oracle=set()
    for w in product(edges(N),repeat=m):
        p,part,_=evaluate(N,w)
        if p==tuple(range(N)) and max(Counter(part).values())<=K:oracle.add(w)
    assert generated==oracle,(N,m,K,len(generated),len(oracle))
    d=diagnostic(N,generated)
    assert d['identity_ok']==count
    results.append({'N':N,'m':m,'fixed_K':K,'count':count,'exact_set_equality':True,'diagnostics':d})
r={'status':'all exact unrank bijections match exhaustive word sets','results':results,'elapsed_seconds':time.monotonic()-start,'provenance':{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'dependencies':'standard library only','seed':'none: deterministic exhaustive check','command':'timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r5-referee/restricted_sampler_check.py','git_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
(OUT/'restricted_sampler_check.results.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':r['status'],'cases':[{k:x[k] for k in ('N','m','fixed_K','count')} for x in results],'elapsed_seconds':r['elapsed_seconds']}))
