#!/usr/bin/env python3
"""Fresh exact tests of sharper R2 constants/normalizer inequality."""
from fractions import Fraction as F
from math import factorial,comb,prod
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import hashlib,json,time
import verify_v1 as own

r=Path(__file__).resolve().parent; start=time.monotonic()
c=own.connected_table(13,24); z=own.total_table(c,40,24)
majorants=[]; ratios=0; zero_residual=0
for v in range(2,14):
 b=F((v-1)*v*(2*v-1),72); a0=F(v**max(v-3,0),v**max(3-v,0))
 for ell in range(2*v-2,25,2):
  g=(ell-2*v+2)//2; lhs=F(c[v][ell],factorial(ell)); rhs=a0*b**g/factorial(g)
  assert lhs<=rhs
  majorants.append({'v':v,'g':g,'actual_over_bound':own.rat(lhs/rhs)})
for n in range(2,41):
 for m in range(0,min(n,24)+1,2):
  k=m//2; total=F(z[n][m],factorial(m))
  for p in range(k+1):
   lhs=F(z[n][m-2*p],factorial(m-2*p))/total
   den=prod(range(n-2*k+1,n-2*k+2*p+1))
   rhs=F(4**p*prod(range(k-p+1,k+1)),den)
   assert lhs<=rhs,(n,m,p,lhs,rhs)
   ratios+=1
   for v in range(1,n+1):
    residual=F(z[n-v][m-2*p],factorial(m-2*p))/total
    assert residual<=lhs
    if residual==0: zero_residual+=1
# Genus bound on size2: exact C(2,2+2g)=1, much beyond inherited length tests.
for g in range(0,201):
 assert F(1,factorial(2+2*g))<=F(1,2)*F(1,12)**g/factorial(g)
# R2 B is exactly tight for the most unbalanced ordered split (a,b)=(v-1,1).
for v in range(2,1001):
 b=lambda s:F((s-1)*s*(2*s-1),72)
 assert b(v)-b(v-1)-b(1)==F((v-1)**2,12)
# Numerical boundary regression only; analytic inequalities are separately reviewed.
constants=[]
with localcontext() as ctx:
 ctx.prec=100
 for exponent in (145,160,256,1024):
  L=Decimal(exponent)*Decimal(2).ln(); logL=L.ln()
  assert L>100
  assert L+Decimal(8).ln()<=L*L/(16*logL)
  assert Decimal(32).ln()<=L/15
  assert Decimal(32).ln()<=L/12
  constants.append({'N':'2^'+str(exponent),'L':str(L),'prefactor_slack':str(L*L/(16*logL)-L-Decimal(8).ln())})
output={'claim_version':'R2-A.v1','reviewed_proof_sha256':hashlib.sha256((r/'r2_audit_inputs/proof_v1.md').read_bytes()).hexdigest(),
 'utc':datetime.now(timezone.utc).isoformat(),'command':'python3 -B experiments/20260922-sparse-global-sampler/roles/r1-combinatorial/audit_r2_check.py',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'imported_own_checker_sha256':hashlib.sha256((r/'verify_v1.py').read_bytes()).hexdigest(),
 'methods':'independently written DYZ integer recurrence and exact fractions; decimal checks are boundary regressions only',
 'domains':{'sharper_majorant':'2<=v<=13, all feasible ell<=24','falling_factorial_ratio':'2<=N<=40, even0<=m<=min(N,24), all p','size2_high_genus':'0<=g<=200','unbalanced_split_B_equality':'2<=v<=1000'},
 'counts':{'sharper_majorants':len(majorants),'falling_factorial_ratios':ratios,'zero_residual_branches':zero_residual,'size2_genus':201,'unbalanced_splits':999},
 'majorants':majorants,'constant_boundary_regressions':constants,'passed':True,'elapsed_seconds':time.monotonic()-start}
(r/'r2_audit_results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'passed':True,'counts':output['counts'],'elapsed_seconds':output['elapsed_seconds']}))
