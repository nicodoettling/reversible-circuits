#!/usr/bin/env python3
"""Exact R1 nonauthor obstruction audit and own stronger incidence falsification."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,prod
import hashlib,importlib.util,json,platform,sys,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
INPUT='experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py'
EXPECTED=json.loads((HERE/'input_hashes.json').read_text())[INPUT]
SOURCE=ROOT/INPUT
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
spec=importlib.util.spec_from_file_location('r1_upper_frozen_old_counts',SOURCE)
old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)

def cutoff(n,m):
    return max(v for v in range(1,n+1) if v**(2*v)<=(n+m+2)**4)

def exp_coeff(s,kmax):
    out=[F(1)]+[F(0)]*kmax
    for k in range(1,kmax+1):
        out[k]=sum(j*s[j]*out[k-j] for j in range(1,k+1))/k
    return out

def main():
    t=time.monotonic();nmax=64;mmax=16;kmax=mmax//2
    C=old.connected_counts(nmax,mmax);Z=old.assembly_counts(nmax,mmax,C)
    ks={cutoff(n,m) for n in range(2,nmax+1) for m in range(0,mmax+1,2)}
    ZA={K:old.assembly_counts(nmax,mmax,C,lambda v,ell,K=K:v==1 or v<=K or (ell-2*v+2)//2<=1) for K in ks}
    checks={'profile_coefficient':0,'finite_SA_lt_8k':0,'subgroup_denominator':0,'rising_incidence':0,'j_integer_constants':0}
    instances=[]
    for n in range(2,nmax+1):
      for m in range(0,mmax+1,2):
        k=m//2;K=cutoff(n,m);S=[F(0)]*(kmax+1)
        for v in range(2,min(n,kmax+1)+1):
          for q in range(v-1,kmax+1):
            g=q-v+1
            if v<=K or g<=1:S[q]+=F(n**v*C[v][2*q],factorial(v)*factorial(2*q))
        ecoeff=exp_coeff(S,kmax)
        assert F(ZA[K][n][m],factorial(m))<=ecoeff[k],('profile',n,m,K)
        checks['profile_coefficient']+=1
        if not m:continue
        for r in range(2,n+1):
            assert Z[n][m]*factorial(r)>=2*comb(r,2)**m,('denominator',n,m,r)
            checks['subgroup_denominator']+=1
        x=F(k,n*n);qparam=3*n*x;bK=F(K**3-K,36)
        if qparam<=F(1,2) and x<=1 and bK*x<=1:
            sx=sum(S[q]*x**q for q in range(1,k+1))
            assert sx<8*k,('SA',n,m,K,sx)
            checks['finite_SA_lt_8k']+=1
        if m<=n:
          D=n-m+1
          for v in range(2,min(n,k+1)+1):
            b=F(v**3-v,36)
            for g in range(k-v+2):
              q=v-1+g
              lhs=F(comb(n,v)*comb(m,2*q)*C[v][2*q]*Z[n-v][m-2*q],Z[n][m])
              rhs=comb(n,v)*F(v)**(v-3)*b**g/factorial(g)*F(4**q*factorial(k),factorial(k-q)*prod(range(D,D+2*q)))
              assert lhs<=rhs,('rising',n,m,v,g,lhs,rhs)
              checks['rising_incidence']+=1
        if (n,m) in [(3,4),(4,4),(4,6),(42,12)]:
            instances.append({'N':n,'m':m,'K':K,'Z':Z[n][m],'ZA':ZA[K][n][m]})
    for j in range(1,1001):
        # All checked by exact integer powers, no logs or rounding.
        assert (16*j+2)**3<72*2**(10*j)
        assert 3*2**(6*j-1)*2<=2**(8*j)
        if j>=64:assert (2**18*j*j)**2<=2**j
        checks['j_integer_constants']+=1
    assert 2*64**4>65**4
    result={'claim':'R2-O1 nonauthor exact regression; R1 rising-incidence finite falsification',
            'checks':checks,'failures':[],'instances':instances,'N_max':nmax,'m_max':mmax,
            'j_checks':[1,1000],'python':platform.python_version(),'seconds':time.monotonic()-t,
            'source':INPUT,'source_sha256':EXPECTED,'command':sys.argv,'seed':None}
    (HERE/'audit_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
