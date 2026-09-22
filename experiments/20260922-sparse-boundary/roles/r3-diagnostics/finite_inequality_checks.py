#!/usr/bin/env python3
"""Exact finite tests of R1's falling-factorial finite-genus bound."""
import argparse,json,math,platform,sys,time
from fractions import Fraction
from pathlib import Path
import boundary_diagnostics as bd

def run(args):
    start=time.monotonic();d=bd.d
    c=d.connected_counts(args.m_max);f=d.active_counts(c,args.m_max);total=d.evaluator(f)
    ns=list(range(2,49))+[64,82,100,128,181,256,512,1000]
    counts={'component_terms':0,'size_sums':0,'binomial_identity':0};failures=[];worst={}
    def check(kind,lhs,rhs,params):
        counts[kind]+=1
        ratio=lhs/rhs if rhs else Fraction(0)
        if kind not in worst or ratio>worst[kind][0]:worst[kind]=(ratio,params)
        if lhs>rhs:failures.append({'kind':kind,'params':params,'lhs':d.rational(lhs),'rhs':d.rational(rhs)})
    for n in ns:
      for m in range(2,min(n,args.m_max)+1,2):
        k=m//2;D=n-m+1;z=total(n,m)
        for v in range(2,min(n,k+1)+1):
          b=Fraction(v**3-v,36)
          base=math.comb(n,v)*Fraction(v)**(v-3)*Fraction(math.factorial(k),math.factorial(k-v+1))*Fraction(4,D*D)**(v-1)
          rhs_sum=base*(1+4*b/(D*D))**(k-v+1)
          lhs_sum=term_sum=Fraction(0)
          for g in range(k-v+2):
            q=v-1+g;ell=2*q
            lhs=Fraction(d.marked_numerator(n,m,v,ell,c,total),z)
            rhs=math.comb(n,v)*Fraction(v)**(v-3)*b**g/math.factorial(g)*Fraction(4,D*D)**q*Fraction(math.factorial(k),math.factorial(k-q))
            check('component_terms',lhs,rhs,[n,m,v,g]);lhs_sum+=lhs;term_sum+=rhs
          check('size_sums',lhs_sum,rhs_sum,[n,m,v])
          counts['binomial_identity']+=1
          if term_sum!=rhs_sum:failures.append({'kind':'binomial_identity','params':[n,m,v]})
    result={'version':'SB-R3-FINITE-INEQ.v1','claim_source':'R1 message 2026-09-22 before09:36UTC','statement':'E X_(v,g)<=binomNv v^(v-3)b_v^g/g! (4/D²)^(v-1+g)(k)_(v-1+g); sum equals base*(1+4b_v/D²)^(k-v+1)',
            'domain':{'N':ns,'even_m_max':args.m_max,'m_le_N':True,'all_feasible_v_g':True},'counts':counts,'failures':failures,
            'worst':{kind:{'ratio':d.rational(value[0]),'params':value[1]} for kind,value in worst.items()},
            'seconds':time.monotonic()-start,'command':sys.argv,'python':platform.python_version(),'source_hashes':bd.MANIFEST['source_hashes'],'seed':None}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['counts','failures','worst','seconds']},indent=2));assert not failures
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m-max',type=int,default=48);p.add_argument('--output',type=Path,required=True);run(p.parse_args())
