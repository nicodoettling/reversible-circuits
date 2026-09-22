#!/usr/bin/env python3
"""Independent global audit checks, standard-library only, deterministic."""
from collections import Counter
from fractions import Fraction
import importlib.util
from itertools import combinations, product
import json
from math import comb, factorial
from pathlib import Path
import platform
import random
import sys
import time

from check import connected_count, finite_reference, right_t, union

ROLE = Path(__file__).resolve().parent
RUN = ROLE.parents[1]


def independent_global_counts(nmax, mmax):
    """Derive total counts directly from DYZ eq. (22), not connected counts.

    If A_d(x)=sum_k Z(d,k)x^k/(d!k!), ZH D^2 ZH-(D ZH)^2
    =y ZH(x,ye^x) ZH(x,ye^-x) gives
    2*d^2*Z(d,k)=2*H(d,k)-F(d,k), with F and H below.
    Only even k are needed; odd return counts are zero by sign.
    """
    z = [[0]*(mmax+1) for _ in range(nmax+1)]
    z[0][0] = 1
    choose = [[comb(k,j) for j in range(k+1)] for k in range(mmax+1)]
    powers = [[q**k for k in range(mmax+1)] for q in range(nmax+1)]

    def convolution(a,b):
        out = [0]*(mmax+1)
        for k in range(0,mmax+1,2):
            out[k] = sum(choose[k][j]*z[a][j]*z[b][k-j] for j in range(0,k+1,2))
        return out

    for d in range(1,nmax+1):
        f,h = [0]*(mmax+1),[0]*(mmax+1)
        for a in range(1,d):
            b=d-a
            coef=comb(d,a)*(a-b)**2
            if not coef:
                continue
            conv=convolution(a,b)
            for k in range(0,mmax+1,2):
                f[k] += coef*conv[k]
        for a in range(d):
            b=d-1-a
            conv=convolution(a,b)
            coef=d*comb(d-1,a)
            pw=powers[abs(a-b)]
            for k in range(0,mmax+1,2):
                h[k] += coef*sum(choose[k][s]*conv[s]*pw[k-s] for s in range(0,k+1,2))
        for k in range(0,mmax+1,2):
            value,remainder=divmod(2*h[k]-f[k],2*d*d)
            assert remainder==0 and value>=0
            z[d][k]=value
    return z


def independent_restricted_counts(nmax,mmax):
    c=[[0]*(mmax+1) for _ in range(nmax+1)]
    if nmax:
        c[1][0]=1
    for v in range(2,nmax+1):
        for g in (0,1):
            k=2*v-2+2*g
            if k<=mmax:
                c[v][k]=connected_count((1,)*v,g)
    z=[[0]*(mmax+1) for _ in range(nmax+1)]
    z[0][0]=1
    for n in range(1,nmax+1):
        for k in range(0,mmax+1,2):
            z[n][k]=sum(comb(n-1,v-1)*comb(k,j)*c[v][j]*z[n-v][k-j]
                        for v in range(1,n+1) for j in range(0,k+1,2) if c[v][j])
    return c,z


def coupling_regression():
    grid=tuple(Fraction(i,4) for i in range(5))
    results=[]
    for delta in (Fraction(0),Fraction(1,4),Fraction(1,2)):
        tested=0; maximum=Fraction(0); witness=None
        for p,q in product(grid,repeat=2):
            if abs(p-q)>delta:
                continue
            for p0,p1,q0,q1 in product(grid,repeat=4):
                if abs(p0-q0)>delta or abs(p1-q1)>delta:
                    continue
                lawp=((1-p)*(1-p0),(1-p)*p0,p*(1-p1),p*p1)
                lawq=((1-q)*(1-q0),(1-q)*q0,q*(1-q1),q*q1)
                tv=sum(abs(a-b) for a,b in zip(lawp,lawq))/2
                assert tv<=2*delta
                tested+=1
                if tv>maximum:
                    maximum=tv; witness=list(map(str,(p,q,p0,p1,q0,q1)))
        results.append({'per_history_delta':str(delta),'models_checked':tested,'maximum_joint_tv':str(maximum),'witness':witness})
    return results


def main():
    t=time.monotonic()
    nmax,mmax=64,128
    total=independent_global_counts(nmax,mmax)
    c,restricted=independent_restricted_counts(nmax,mmax)
    saved=json.loads(ROLE.joinpath('global-review-input/global_mass_results.json').read_text())
    table_checks=0
    for row in saved['rows']:
        n,m=row['N'],row['m']
        assert total[n][m]==row['Z']
        assert restricted[n][m]==row['Z_g_le_1']
        ratio=Fraction(restricted[n][m],total[n][m])
        assert ratio==Fraction(row['covered_numerator'],row['covered_denominator'])
        assert float(ratio)==row['covered_decimal']
        table_checks+=1
    finite_cells=0
    for n in range(1,7):
        for m,level in enumerate(finite_reference(n)):
            exact=sum(w for (p,partition),w in level.items() if p==tuple(range(n)))
            assert exact==total[n][m]
            finite_cells+=1
    bound_checks=0
    for n in range(2,nmax+1):
        assert 24*c[n][2*n] <= factorial(2*n)*n**n
        assert restricted[n][2*n] <= factorial(2*n)*factorial(n)*6**n
        for r in range(2,n+1):
            assert total[n][2*n]*factorial(r)>=2*comb(r,2)**(2*n)
            bound_checks+=1
    # Exercise the actual integration code under its frozen imports. This only
    # checks support, exclusions and exact certificates; primitive law is a
    # separate frozen-code audit.
    spec=importlib.util.spec_from_file_location('r3_global_integration',RUN/'sample.py')
    integrated=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=integrated
    spec.loader.exec_module(integrated)
    sample_cases=0; rejected_cases=0
    for seed in (17,101,20260907):
        rng=random.Random(seed)
        for n in range(9):
            for m in range(2*n+5):
                good=restricted[n][m]>0
                try:
                    draw=integrated.sample_restricted_components(n,m,rng)
                except ValueError:
                    assert not good,(n,m)
                    rejected_cases+=1
                    continue
                assert good
                assert draw.covered_mass==Fraction(restricted[n][m],total[n][m])
                p,part=tuple(range(n)),tuple(range(n))
                for e in draw.word:
                    p,part=right_t(p,e),union(part,*e)
                assert p==tuple(range(n)) and len(draw.word)==m
                for component in set(part):
                    v=part.count(component)
                    ell=sum(part[e[0]]==component for e in draw.word)
                    assert (v==1 and ell==0) or (v>=2 and ell in (2*v-2,2*v))
                sample_cases+=1
    out={'python':platform.python_version(),'nonstandard_dependencies':[],
         'method':'total counts from independently derived DYZ eq22 coefficient recurrence; restricted counts from blind Vakil oracle and least-label recurrence',
         'nmax':nmax,'mmax':mmax,'saved_exact_rows_verified':table_checks,
         'independent_endpoint_support_dp_cells':finite_cells,'subgroup_bounds_verified':bound_checks,
         'integration_valid_smoke_cases':sample_cases,'integration_rejected_boundary_cases':rejected_cases,
         'diagnostic_seeds':[17,101,20260907],'conditional_coupling_regression':coupling_regression(),
         'seconds':time.monotonic()-t,'result':'pass'}
    ROLE.joinpath('global-check-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
