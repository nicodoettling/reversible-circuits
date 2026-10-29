"""Exact deterministic regressions; run ONLY through the authorized bounded helper."""
import argparse
import importlib.util
import itertools as it
import json
import math
import os
import platform
import subprocess
import time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research-campaigns/noisy-bridge-20261029/inputs/experiments/20261028-bridge-projections/check.py'

def average(f, x, averaged, q):
    total = F()
    for z in it.product(range(q), repeat=len(averaged)):
        y = list(x)
        for i, a in zip(averaged, z): y[i] = a
        total += f[tuple(y)]
    return total / q**len(averaged)

def local_channel_checks():
    rows=[]
    for q in (1,2,3):
        for s in (1,2,3):
            domain=list(it.product(range(q),repeat=s))
            # Point-mass indicators span every function, proving only this finite case.
            for L in (s,s+1,s+2):
                for k in range(L+1):
                    if k>L-s:
                        # Highest-order centered tensor is killed when fewer than s survive.
                        f={x:math.prod((q-1 if a==0 else -1) for a in x) for x in domain}
                        for x in domain:
                            value=F()
                            for J in it.combinations(range(L), k):
                                value+=average(f,x,tuple(i for i in J if i<s),q)
                            assert value==0
                        rows.append(dict(q=q,s=s,L=L,k=k,invertible=False,top_component_killed=True))
                        continue
                    alphas=[F(math.comb(L-j,k),math.comb(L,k)) for j in range(s+1)]
                    C=F(3**s)/alphas[s]
                    for target in domain:
                        f={x:F(x==target) for x in domain}
                        g={}
                        for x in domain:
                            val=F()
                            for mask in range(1<<s):
                                S=tuple(j for j in range(s) if mask>>j&1)
                                complement=tuple(j for j in range(s) if not mask>>j&1)
                                comp=F()
                                for sub in range(1<<len(S)):
                                    extra=tuple(S[j] for j in range(len(S)) if sub>>j&1)
                                    comp+=(-1)**len(extra)*average(f,x,complement+extra,q)
                                val+=comp/alphas[len(S)]
                            g[x]=val
                            assert abs(val)<=C
                        for x in domain:
                            Tg=sum((average(g,x,tuple(i for i in J if i<s),q) for J in it.combinations(range(L),k)),F())/math.comb(L,k)
                            assert Tg==f[x]
                    rows.append(dict(q=q,s=s,L=L,k=k,invertible=True,basis_size=len(domain),alpha_s=str(alphas[s])))
    return rows

def pair_checks():
    rows=[]
    for q,L in ((1,2),(1,4),(2,2),(2,4),(3,4)):
        for k in range(L+1):
            alpha=F((L-k)*(L-k-1),L*(L-1))
            for w in it.product(range(q),repeat=L):
                yes=total=0
                for positions in it.combinations(range(L),k):
                    for values in it.product(range(q),repeat=k):
                        y=list(w)
                        for i,a in zip(positions,values):y[i]=a
                        yes+=y[0]==y[1];total+=1
                assert F(yes,total)==alpha*int(w[0]==w[1])+(1-alpha)/q
            rows.append(dict(q=q,L=L,k=k,alpha=str(alpha)))
    return rows

def cp1():
    prior_A=F(21,2200); prior_C=F(1,11); prior_D=F(879,1100)
    normalizer=2*prior_A+prior_C+prior_D
    assert normalizer==F(10,11)
    A=prior_A/normalizer; C=prior_C/2/normalizer; D=prior_D/normalizer
    assert (A,C,D)==(F(21,2000),F(1,20),F(879,1000))
    px=2*C; pe=A+C; pf=A; gamma=F(1,10)
    assert max(px,pe,pf)<=gamma
    joint=2*A/2
    assert joint==F(21,2000)>gamma**2
    conditional=F(21,221)
    assert conditional<gamma
    return dict(prior_normalizer=str(normalizer),posterior_per_A=str(A),posterior_per_C=str(C),posterior_D=str(D),initial_incidence=list(map(str,(px,pe,pf))),joint=str(joint),invalid_product=str(gamma**2),old_product_bound_rejected=True,post_transfer_second_incidence=str(conditional),mechanism='support restriction and Bayes normalization; local fresh-value independence is insufficient')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    output=Path(args.output)
    if output.exists():raise SystemExit('refuse overwrite immutable result')
    start=time.monotonic()
    spec=importlib.util.spec_from_file_location('frozen_projection_check',SOURCE)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    cases=[mod.check(n,L) for n,L in ((2,0),(2,2),(2,4),(3,0),(3,2),(3,4),(3,6),(4,0),(4,4),(4,6))]
    counts={(row['N'],row['L']):row['bridge_words'] for row in cases}
    assert counts[3,4]==27 and counts[4,4]==120 and counts[4,6]==3936
    # Odd-length emptiness checked by exhaustive checker independently of rejection in APIs.
    odd=[mod.check(n,L) for n,L in ((2,1),(3,1),(3,3),(4,3))]
    assert all(row['bridge_words']==0 for row in odd)
    result=dict(status='passed',commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),python=platform.python_version(),dependencies='stdlib',randomness='none; exact finite exhaustive integer/rational checks',projection_cases=cases,odd_cases=odd,pair_cases=pair_checks(),local_channel_cases=local_channel_checks(),cached_prefix=cp1())
    result['elapsed_seconds']=time.monotonic()-start
    tmp=output.with_suffix(output.suffix+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,output)
    print(json.dumps(dict(status=result['status'],elapsed_seconds=result['elapsed_seconds'],output=str(output),projection_cases=len(cases),local_channel_cases=len(result['local_channel_cases']))))
if __name__=='__main__':main()
