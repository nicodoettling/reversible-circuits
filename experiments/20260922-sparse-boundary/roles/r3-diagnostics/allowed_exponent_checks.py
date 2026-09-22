#!/usr/bin/env python3
"""Exact finite coefficient-relevant checks of R2's H0 exponent upper bound."""
import argparse,json,math,platform,sys,time
from fractions import Fraction
from pathlib import Path
import boundary_diagnostics as bd

def exp_interval(t,terms=20):
    assert 0<=t<=1
    low=sum((t**j/math.factorial(j) for j in range(terms+1)),Fraction(0))
    first=t**(terms+1)/math.factorial(terms+1)
    return low,low+first/(1-t/Fraction(terms+2))

def run(args):
    start=time.monotonic();d=bd.d
    c=d.connected_counts(args.m_max);f=d.active_counts(c,args.m_max);cache={};rows=[]
    ns=list(range(6,49))+[64,81,82,100,128,181,256,512,1000,1296,10_000,1_000_000]
    for n in ns:
      for m in sorted({2,4,2*(min(args.m_max,n//3)//2),min(args.m_max,bd.star(n))}):
        if not 0<m<=args.m_max:continue
        k=m//2;K=d.cutoff(n,m);x=Fraction(k,n*n);q=3*n*x;bK=Fraction(K**3-K,36)
        if q>Fraction(1,2) or x>1 or bK*x>1:continue
        S=Fraction(0);S_relaxed=Fraction(0)
        for v in range(2,min(n,k+1)+1):
          for ell in range(2*v-2,m+1,2):
            if d.h0_allowed(v,ell,K):
              component=Fraction(c[v][ell],math.factorial(ell))*x**(ell//2)
              S+=math.comb(n,v)*component
              S_relaxed+=Fraction(n**v,math.factorial(v))*component
        el,eu=exp_interval(bK*x)
        coeff=Fraction(9*k,8)/(1-q);remainder=Fraction(k,4)*x/(1-q)
        strong_lo=el*coeff+remainder;strong_hi=eu*coeff+remainder
        assert S<=S_relaxed<=8*k,('8k failure',n,m,S,S_relaxed)
        assert S_relaxed<=strong_lo,('strong comparison unresolved/fails',n,m,S_relaxed,strong_lo,strong_hi)
        if K not in cache:cache[K]=d.evaluator(d.active_counts(c,args.m_max,lambda v,ell:d.h0_allowed(v,ell,K)))
        za=cache[K](n,m)
        # e<3 gives an exact but coarser consequence of the claimed coefficient bound.
        assert za*k**k<=math.factorial(m)*n**(2*k)*3**(8*k)
        rows.append({'N':n,'m':m,'K':K,'x':d.rational(x),'q':d.rational(q),'bKx':d.rational(bK*x),
                    'truncated_S_binomial':d.rational(S),'truncated_S_relaxed':d.rational(S_relaxed),'S_over_8k':d.rational(S_relaxed/(8*k)),
                    'strong_rhs_lower':d.rational(strong_lo),'strong_rhs_upper':d.rational(strong_hi),
                    'S_over_strong_rhs_lower':d.rational(S_relaxed/strong_lo),'ZA':za,'passed':True})
    result={'version':'SB-R3-ALLOWED-EXPONENT.v2','status':'exact finite coefficient-relevant checks, not asymptotic proof',
            'S_definitions':{'binomial':'sum_{v>=2,ell<=m,H0allowed} binomNv C(v,ell)/ell! x^(ell/2)', 'relaxed':'replace binomNv by N^v/v!; this is R2 obstruction-v1 stated relaxed exponent', 'truncation':'terms ell>m cannot affect coefficient x^(m/2)'},
            'inequalities':['S<=8k','S<=exp(bKx)*9k/[8(1-q)]+kx/[4(1-q)]','ZA*k^k<=m!N^(2k)3^(8k)'],
            'strong_rhs_check':'Exact relaxed S<=20-term Taylor LOWER bound on RHS; tail interval also recorded',
            'm_max':args.m_max,'rows':rows,'seconds':time.monotonic()-start,'command':sys.argv,
            'python':platform.python_version(),'source_hashes':bd.MANIFEST['source_hashes'],'seeds':None}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'seconds':result['seconds'],'rows':len(rows),'max_S_over_8k':max((r['S_over_8k']['decimal'],r['N'],r['m']) for r in rows),
      'max_S_over_strong':max((r['S_over_strong_rhs_lower']['decimal'],r['N'],r['m']) for r in rows)},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m-max',type=int,default=64);p.add_argument('--output',type=Path,required=True);run(p.parse_args())
