#!/usr/bin/env python3
"""Exact bounded tests of provisional count/incidence inequalities.

Finite successful checks do not prove the estimates or their asymptotics.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from math import factorial,comb
from pathlib import Path
import platform
import subprocess
import sys
import time

import diagnostics as d


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--m-max',type=int,default=64)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    start=time.monotonic()
    c=d.connected_counts(args.m_max)
    f=d.active_counts(c,args.m_max)
    z=d.evaluator(f)
    count_tests=[]
    count_failures=[]
    for v in range(2,len(c)):
        a0=Fraction(c[v][2*v-2],factorial(2*v-2))
        assert a0 == Fraction(v)**(v-3)
        b1=Fraction(v**3-v,36)
        b2=sum(Fraction(i*i,12) for i in range(1,v))
        for ell in range(2*v,args.m_max+1,2):
            g=(ell-2*v+2)//2
            a=Fraction(c[v][ell],factorial(ell))
            for name,b in [('cubic36',b1),('sum_squares12',b2)]:
                bound=a0*b**g/factorial(g)
                row={'name':name,'v':v,'g':g,'ell':ell,'actual':d.rational(a),
                     'bound':d.rational(bound),'ratio':d.rational(a/bound),'pass':a<=bound}
                count_tests.append(row)
                if a>bound:
                    count_failures.append(row)
    incidence_tests=0
    incidence_failures=[]
    worst=None
    ns=list(range(2,129))+[256,512,1024,2048,10_000,1_000_000]
    # Cancel common positive binom(N,v)C(v,2q) before comparison.
    for n in ns:
        for m in range(2,min(n,args.m_max)+1,2):
            k=m//2
            denominator=n-m+1
            total=z(n,m)
            for v in range(2,min(n,len(c)-1)+1):
                for ell in range(2*v-2,m+1,2):
                    if not c[v][ell]:
                        continue
                    q=ell//2
                    lhs=factorial(m)//factorial(m-ell)*z(n-v,m-ell)*denominator**(2*q)
                    rhs=total*(4*k)**q
                    incidence_tests+=1
                    ratio=Fraction(lhs,rhs)
                    if worst is None or ratio>worst[0]:
                        worst=(ratio,n,m,v,ell)
                    if lhs>rhs:
                        incidence_failures.append({'N':n,'m':m,'v':v,'ell':ell,'lhs':lhs,'rhs':rhs})
    g01=d.active_counts(c,args.m_max,lambda v,ell:d.genus(v,ell)<=1)
    cases=[(82,14),(128,16),(128,18),(512,32),(2048,64),(8,12),(16,32),(32,64)]
    cases.extend((n,m) for n,m in [(16,12),(32,12),(64,14)] if m<=args.m_max)
    coefficients={}
    rows=[]
    for n,m in cases:
        if m>args.m_max:
            continue
        for cutoff in sorted({2,d.cutoff(n,m)}):
            if cutoff not in coefficients:
                coefficients[cutoff]=(d.active_counts(c,args.m_max,lambda v,ell:d.h0_allowed(v,ell,cutoff)),
                                      d.active_counts(c,args.m_max,lambda v,ell:v<=cutoff))
            a,size=coefficients[cutoff]
            row=d.certificate(n,m,c,f,a,g01,size,cutoff)
            # Aggregate exact marked large-support union bound separately.
            marks=row['marked_category_expectations']
            mark=Fraction(0)
            for name,value in marks.items():
                if name.startswith('large_'):
                    mark+=Fraction(value['numerator'],value['denominator'])
            event=row['large_support_event']
            assert Fraction(event['numerator'],event['denominator'])<=mark
            row['large_support_marked_union_bound']=d.rational(mark)
            # The finite proposed incidence+count bound, no exponential rounding.
            if m<=n:
                finite_bound=Fraction(0)
                for v in range(cutoff+1,min(n,m//2+1)+1):
                    for g in range(m//2-v+2):
                        q=v-1+g
                        upper_a=Fraction(v)**(v-3)*Fraction(v**3-v,36)**g/factorial(g)
                        finite_bound+=comb(n,v)*upper_a*Fraction(4*(m//2),(n-m+1)**2)**q
                row['proposed_large_support_finite_bound']=d.rational(finite_bound)
                assert mark<=finite_bound
            rows.append(row)
    first=None
    for n in range(2,129):
        for m in range(0,n+1,2):
            if m**5>n**3:
                break
            if m>=2*d.cutoff(n,m)+4 and d.cutoff(n,m)<n:
                first={'N':n,'m':m,'K':d.cutoff(n,m)}
                break
        if first:
            break
    data={'version':'R4-INEQ.v1','status':'exact bounded checks; no asymptotic certification',
          'normalization':'A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!',
          'statements':{'cubic36':'A_g(v)<=A_0(v)*((v^3-v)/36)^g/g!',
                        'sum_squares12':'A_g(v)<=A_0(v)*(sum_{i=1}^{v-1}i^2/12)^g/g!',
                        'incidence':'E X_(v,2q)<=binom(N,v)*A(v,q)*(4k/(N-2k+1)^2)^q; m=2k<=N'},
          'python':platform.python_version(),'dependencies':{},'seed':None,
          'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
          'command':sys.argv,'diagnostics_sha256':hashlib.sha256(Path(d.__file__).read_bytes()).hexdigest(),
          'm_max':args.m_max,'incidence_N_domain':ns,'count_tests':len(count_tests),
          'count_failures':count_failures,'count_worst_by_bound':{
              name:max((r for r in count_tests if r['name']==name),
                       key=lambda r:Fraction(r['ratio']['numerator'],r['ratio']['denominator']))
              for name in ['cubic36','sum_squares12']},
          'count_rows':count_tests,'incidence_tests':incidence_tests,'incidence_failures':incidence_failures,
          'incidence_worst':{'ratio':d.rational(worst[0]),'N':worst[1],'m':worst[2],'v':worst[3],'ell':worst[4]},
          'first_feasible_nonzero_H0_in_T0_search':first,'rows':rows,'seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({key:data[key] for key in ['seconds','count_tests','count_failures','count_worst_by_bound',
          'incidence_tests','incidence_failures','incidence_worst','first_feasible_nonzero_H0_in_T0_search']},indent=2))
    print(json.dumps([{key:r[key] for key in ['N','m','K','actual_K','T0_range','omitted_mass',
                      'large_support_event','large_support_marked_union_bound']}
                     for r in rows if r['N']==82],indent=2))


if __name__=='__main__':
    main()
