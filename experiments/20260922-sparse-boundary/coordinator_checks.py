#!/usr/bin/env python3
"""Decisive independent exact audits of frozen component proofs; no asymptotic inference."""
import argparse, hashlib, importlib.util, json, math, platform, sys, time
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parent
ROOT=R.parents[1]
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
start=time.monotonic()
old='experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/diagnostics.py'
manifest=json.loads((R/'source_hashes.json').read_text())
assert hashlib.sha256((ROOT/old).read_bytes()).hexdigest()==manifest[old]
spec=importlib.util.spec_from_file_location('frozen_root_counts',ROOT/old)
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
M=20;c=d.connected_counts(M);total=d.evaluator(d.active_counts(c,M))
checks={'majorant':0,'profile_coefficient':0,'subgroup_denominator':0,'finite_binomial':0,'sequence':0}
for v in range(2,len(c)):
 for ell in range(2*v-2,M+1,2):
  g=(ell-2*v+2)//2
  assert F(c[v][ell],math.factorial(ell))<=F(v)**(v-3)*F(v**3-v,36)**g/math.factorial(g)
  checks['majorant']+=1
for n in [2,3,4,6,12,28,42,64]:
 for m in range(2,M+1,2):
  k=m//2;K=d.cutoff(n,m)
  za=d.evaluator(d.active_counts(c,M,lambda v,e:d.h0_allowed(v,e,K)))(n,m)
  s=[F(0)]*(k+1)
  for i in range(1,k+1):
   for v in range(2,min(n,i+1)+1):
    if d.h0_allowed(v,2*i,K):s[i]+=F(n**v*c[v][2*i],math.factorial(v)*math.factorial(2*i))
  exp=[F(1)]+[F(0)]*k
  for a in range(1,k+1):exp[a]=sum(i*s[i]*exp[a-i] for i in range(1,a+1))/a
  assert F(za,math.factorial(m))<=exp[k]
  checks['profile_coefficient']+=1
  for rank in range(2,min(n,8)+1):
   assert total(n,m)*math.factorial(rank)>=2*math.comb(rank,2)**m
   checks['subgroup_denominator']+=1
  if m<=n:
   D=n-m+1
   for v in range(2,min(n,k+1)+1):
    base=math.comb(n,v)*F(v)**(v-3)*F(math.factorial(k),math.factorial(k-v+1))*F(4,D*D)**(v-1)
    rhs=base*(1+F(v**3-v,9*D*D))**(k-v+1)
    lhs=sum(F(d.marked_numerator(n,m,v,ell,c,total),total(n,m)) for ell in range(2*v-2,m+1,2))
    assert lhs<=rhs
    checks['finite_binomial']+=1
sequence=[]
for j in range(1,513):
 n=1<<(8*j);m=1<<(6*j);k=m//2;K=d.cutoff(n,m)
 assert m**4==n**3 and (m+2)**4>n**3 and K<=16*j+2
 assert 6*n*k<=n*n and (K**3-K)*k<=36*n*n
 rank=m//(6*j)
 assert 2<=rank<=n and 12*j*rank>=m
 assert math.comb(rank,2)*576*j*j>=m*m
 if j>=64:
  assert (1<<36)*j**4<=1<<j
  assert (j+1)**4<=2*j**4
 checks['sequence']+=1
 if j in [1,63,64,65,128,256,512]:sequence.append({'j':j,'log2N':8*j,'log2m':6*j,'K':K,'proved_threshold':j>=64})
assert 1152*2*81 < 1<<18
result={'version':'ROOT-EXACT.v1','command':sys.argv,'python':platform.python_version(),'old_source_sha256':manifest[old],'checks':checks,'sequence_checkpoints':sequence,'seconds':time.monotonic()-start,'seeds':None,'status':'all assertions passed; finite falsification only'}
args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
