#!/usr/bin/env python3
"""Targeted nonauthor finite audit of frozen R1 proof v1."""
import collections
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import platform
import time

R=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r2_verify',R/'verify.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

def partitions(labels):
    if not labels:
        yield ()
        return
    first,*rest=labels
    for p in partitions(rest):
        yield ((first,),)+p
        for j in range(len(p)):
            yield p[:j]+((first,)+p[j],)+p[j+1:]

def compositions(total,n):
    if n==0:
        if total==0: yield ()
    elif n==1:
        yield (total,)
    else:
        for x in range(total+1):
            for tail in compositions(total-x,n-1): yield (x,)+tail

def macros(labels,k):
    for part in partitions(list(labels)):
        large=[b for b in part if len(b)>1]
        base=sum(len(b)-1 for b in large)
        if base>k: continue
        for gs in compositions(k-base,len(large)):
            gdict=dict(zip(large,gs))
            yield tuple(sorted((b,gdict.get(b,0)) for b in part))

def perfect_matchings(labels):
    if not labels:
        yield ()
        return
    a=labels[0]
    for j in range(1,len(labels)):
        b=labels[j]
        for tail in perfect_matchings(labels[1:j]+labels[j+1:]):
            yield ((a,b),)+tail

def main():
    t=time.monotonic(); h=v.connected_h(8,8)
    A=lambda b,g:h[len(b),g]*math.factorial(len(b))
    def weight(macro):
        out=Q(1)
        for b,g in macro: out*=A(b,g)
        return out
    cells=incidences=0; maxdeg=0
    for n in range(2,8):
        for k in range(n//2+1):
            for q in range(k+1):
                for removed in range(n+1):
                    # All fixed removed sets are equivalent under label bijections.
                    V=set(range(removed)); degrees=collections.Counter(); fwd=Q(0); bases=Q(0)
                    for sub in macros(range(removed,n),k-q):
                        base=tuple(sorted(sub+tuple(((x,),0) for x in V)))
                        bases+=weight(base)
                        isolates=tuple(b[0] for b,g in base if len(b)==1)
                        for chosen in itertools.combinations(isolates,2*q):
                            for matching in perfect_matchings(chosen):
                                chosen_set=set(chosen)
                                beta=tuple(sorted(tuple((b,g) for b,g in base if not(len(b)==1 and b[0] in chosen_set))+tuple((pair,0) for pair in matching)))
                                wb=weight(beta)
                                assert wb==weight(base)/2**q
                                degrees[beta]+=1; fwd+=wb; incidences+=1
                    reverse=Q(0)
                    for beta in macros(range(n),k):
                        pair_indices=[i for i,(b,g) in enumerate(beta) if len(b)==2 and g==0]
                        count=0
                        for deleted in itertools.combinations(pair_indices,q):
                            remain=[bg for i,bg in enumerate(beta) if i not in deleted]
                            used=set(x for b,g in remain if len(b)>1 for x in b)
                            if not(V & used): count+=1
                        assert count==degrees[beta],(n,k,q,removed,beta,count,degrees[beta])
                        assert count<=math.comb(k,q)
                        maxdeg=max(maxdeg,count)
                        reverse+=weight(beta)*count
                    assert fwd==reverse
                    assert fwd>=bases*Q((n-2*k+1)**(2*q),4**q*math.factorial(q))
                    cells+=1
    C=v.connected_counts(h,8,14)
    # Fresh finite tail checks, using a rational upper bound for exp(1+a).
    def short_assembly(nmax,mmax,cap):
        Z={(0,m):int(m==0) for m in range(mmax+1)}
        for n in range(1,nmax+1):
            for m in range(mmax+1):
                Z[n,m]=sum(math.comb(n-1,s-1)*math.comb(m,l)*C[s,l]*Z[n-s,m-l]
                    for s in range(1,min(n,m//2+1,cap)+1) for l in range(m+1))
        return Z
    allZ=short_assembly(1024,14,8)
    capZ={J:short_assembly(1024,14,J) for J in range(1,7)}
    tailrows=[]
    for n in [16,32,64,128,256,1024]:
        for k in range(1,8):
            D=n-2*k+1; a=Q(k*k*(k+2),9*D*D)
            if 1+a>=100: continue
            c=(Q(100)/(99-a))**100 # exp(1+a)<=c by -log(1-u)>=u
            rho=c*n*Q(4*k,D*D)
            if rho>=1: continue
            for J in range(1,min(k+1,7)):
                actual=1-Q(capZ[J][n,2*k],allZ[n,2*k])
                bound=Q(n)*c*rho**J/((J+1)**3*(1-rho))
                assert actual<=bound,(n,k,J,actual,bound)
                tailrows.append({'N':n,'m':2*k,'J':J,'actual_numerator':actual.numerator,'actual_denominator':actual.denominator,'bound_float':float(bound),'nontrivial':bound<1})
    out={'reviewed_claim':'R1 proof_v1.md','reviewed_sha256':hashlib.sha256((R/'r1_proof_v1_review_input.md').read_bytes()).hexdigest(),
         'own_verify_sha256':hashlib.sha256((R/'verify.py').read_bytes()).hexdigest(),'python':platform.python_version(),
         'command':'python3 -B experiments/20260922-sparse-global-sampler/roles/r2-analytic/audit_r1.py','seed':None,
         'method':'exact weighted macro incidence enumeration and rational finite tail comparison','incidence_cells':cells,
         'extension_incidences':incidences,'maximum_reverse_degree':maxdeg,'tail_rows':tailrows,
         'tail_nontrivial_rows':sum(r['nontrivial'] for r in tailrows),'elapsed_seconds':time.monotonic()-t,'passed':True}
    (R/'r1_audit_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ['incidence_cells','extension_incidences','maximum_reverse_degree','tail_nontrivial_rows','elapsed_seconds','passed']}))

if __name__=='__main__': main()
