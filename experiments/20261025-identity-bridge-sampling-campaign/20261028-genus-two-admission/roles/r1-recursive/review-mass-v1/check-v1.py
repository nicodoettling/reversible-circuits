"""Nonauthor independent finite checks for exact M-GROW.v1 proof.
No author module imported. Weighted support walk, exponential-profile assembly,
and Eulerian polynomial moments are separate implementations.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb,factorial
from pathlib import Path
import argparse,hashlib,json,platform,subprocess,time

def merge(blocks,a,b):
    ia=next(i for i,(labels,_) in enumerate(blocks) if a in labels)
    ib=next(i for i,(labels,_) in enumerate(blocks) if b in labels)
    if ia==ib:
        return tuple((lab,cost+int(i==ia)) for i,(lab,cost) in enumerate(blocks))
    labels=tuple(sorted(blocks[ia][0]+blocks[ib][0]));cost=blocks[ia][1]+blocks[ib][1]+1
    return tuple(sorted([x for i,x in enumerate(blocks) if i not in (ia,ib)]+[(labels,cost)]))

def words(n,mmax):
    identity=tuple(range(n));states={(identity,tuple(((i,),0) for i in range(n))):1}
    layers=[];peak=0
    for m in range(mmax+1):
        peak=max(peak,len(states));ids=defaultdict(int)
        for (p,blocks),number in states.items():
            if p==identity:ids[blocks]+=number
        layers.append(dict(ids));nxt=defaultdict(int)
        if m==mmax:break
        for (p,blocks),number in states.items():
            for a,b in combinations(range(n),2):
                q=tuple(p[b] if i==a else p[a] if i==b else p[i] for i in range(n))
                nxt[q,merge(blocks,a,b)]+=number
        states=nxt
    return layers,peak

def eligible(blocks,G,J):
    for labels,m in blocks:
        v=len(labels)
        if v==1:
            assert m==0;continue
        assert m%2==0 and m>=2*v-2
        if m//2-v+1>G and v>J:return False
    return True

def exponential_assembly(n,m,G,J,connected):
    # H=exp(sum C(v,2l)/(v!(2l)!) z^v y^l), no singleton terms.
    # Differentiate by z: sH[s,k]=sum v B[v,l]H[s-v,k-l].
    k=m//2;H={(0,0):F(1)}
    types=[]
    for v in range(2,n+1):
        for ell in range(2*v-2,m+1,2):
            g=ell//2-v+1
            if g<=G or v<=J:
                types.append((v,ell//2,F(connected[v,ell],factorial(v)*factorial(ell))))
    for s in range(1,n+1):
        for h in range(k+1):
            H[s,h]=sum((v*c*H.get((s-v,h-cost),0) for v,cost,c in types if v<=s and cost<=h),F(0))/s
    answer=factorial(m)*sum((F(factorial(n),factorial(n-s))*H.get((s,k),0) for s in range(n+1)),F(0))
    assert answer.denominator==1
    return answer.numerator

def eulerian_next(a,d):
    # P_(d+1)=(1+dq)P_d+q(1-q)P'_d.
    b=[0]*(len(a)+1)
    for i,c in enumerate(a):
        b[i]+=(i+1)*c
        b[i+1]+=(d-i)*c
    while len(b)>1 and b[-1]==0:b.pop()
    return b

def main(output):
    start=time.monotonic();connected={};references={};peak=0
    for n in range(1,6):
        rows,maxstates=words(n,12);references[n]=rows;peak=max(peak,maxstates)
        for m,blocks in enumerate(rows):
            connected[n,m]=sum(number for part,number in blocks.items() if len(part)==1)
    checks=[];digest=hashlib.sha256()
    for n in range(2,6):
        for m in range(0,13,2):
            for G in range(5):
                for J in range(1,n+1):
                    actual=sum(number for blocks,number in references[n][m].items() if eligible(blocks,G,J))
                    assembled=exponential_assembly(n,m,G,J,connected)
                    assert actual==assembled,(n,m,G,J,actual,assembled)
                    digest.update(repr((n,m,G,J,actual)).encode());checks.append((n,m,G,J))
    # Check the normalized source recurrence directly against word counts.
    recurrence_checks=0;majorant_checks=0
    for v in range(2,6):
        for m in range(0,13,2):
            lhs=F(v*v*(v-1)*connected[v,m],factorial(m));rhs=F(0)
            for a in range(1,v):
                b=v-a
                for ell in range(2,m+1,2):
                    for la in range(m-ell+1):
                        lb=m-ell-la
                        rhs+=2*comb(v,a)*a*b*b*F(a**ell,factorial(ell))*F(connected[a,la],factorial(la))*F(connected[b,lb],factorial(lb))
            assert lhs==rhs,(v,m,lhs,rhs);recurrence_checks+=1
            if m>=2*v-2:
                g=m//2-v+1
                assert F(connected[v,m],factorial(m))<=F(v)**(v-3)*F(v**3-v,36)**g/factorial(g)
                majorant_checks+=1
    # Independent rational power moments, including q immediately below1/2.
    poly=[1];moments=0;coefficient_checks=0;moment_digest=hashlib.sha256()
    qs=(F(1,2048),F(3,8),F(511,1024),F(1,2))
    for d in range(190):
        if d%3==0:
            g=d//3+1
            c=F(factorial(3*g-2)*2**(3*g-1),36**g*factorial(g))
            assert c<=(6*g**3)**g;coefficient_checks+=1
            for q in qs:
                p=sum((F(a)*q**i for i,a in enumerate(poly)),F(0))
                exact=p/(1-q)**(d+1)-1
                first=factorial(d)*((1-q)**(-d-1)-1)
                second=factorial(d+1)*q*(1-q)**(-d-2)
                last=factorial(d+1)*2**(d+2)*q
                assert exact<=first<=second<=last,(d,q)
                moment_digest.update(repr((d,q,exact)).encode());moments+=1
        poly=eulerian_next(poly,d)
    ratio_checks=0
    for r in range(129):
        assert F(2,factorial(2*r+2))<=F(1,12**r*factorial(r));ratio_checks+=1
    convex_checks=0
    for v in range(2,65):
        total=sum((F(comb(v,a)*a**a*(v-a)**(v-a-1),v**(v-1)*(v-1)) for a in range(1,v)),F(0))
        assert total==1
        for a in range(1,v):
            b=v-a
            assert F(v**3-v-a**3+a-b**3+b,36)==F(a*b*v,12)>=F(a*a,12)
        convex_checks+=1
    denominator_checks=0
    for n in range(2,6):
        for m in range(2,13,2):
            total=sum(references[n][m].values())
            for r in range(2,n+1):
                assert total>=F(2*comb(r,2)**m,factorial(r));denominator_checks+=1
    sequence=[]
    for j in range(1,257):
        N=2**(8*j);m=2**(6*j);P=N+m+2;k=m//2;x=F(k,N*N);q=3*N*x;G=2**j
        lo=1;hi=min(N,32*j+4)
        while lo<hi:
            mid=(lo+hi+1)//2
            if 3**mid<=P**4:lo=mid
            else:hi=mid-1
        L=lo
        assert 3**L<=P**4 and (L==N or 3**(L+1)>P**4)
        assert q<=F(1,2) and F(L**3-L,36)*x<=1 and 6*G**3*x<=F(1,16)
        r=m//(6*j)
        assert 2<=r<=N and r>=F(m,12*j) and comb(r,2)>=F(m*m,576*j*j)
        # r! not materialized: use the exact exponent implicationr<=m/(6j).
        assert r*6*j<=m
        if j>=64:assert (2**18*j*j)**2<=2**j
        if j in (1,2,63,64,65,256):sequence.append({'j':j,'exact_L':L,'max_G_bits':G.bit_length()})
    result={'schema_version':1,'status':'PASS','claim':'Independent exact finite checks for frozen M-GROW.v1; not asymptotic proof','seed':None,'python':platform.python_version(),'dependencies':'standard library only','base_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'peak_weighted_support_states':peak,'assembly_comparisons':len(checks),'assembly_digest':digest.hexdigest(),'DYZ_recurrence_cells':recurrence_checks,'majorant_cells':majorant_checks,'Eulerian_moment_checks':moments,'moment_gmax':64,'moment_digest':moment_digest.hexdigest(),'c_g_checks':coefficient_checks,'L_series_coefficients':ratio_checks,'convex_degree_checks':convex_checks,'subgroup_denominator_checks':denominator_checks,'sequence_j_range':[1,256],'selected_exact_cutoffs':sequence,'elapsed_seconds':time.monotonic()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    p=Path(output);assert not p.exists();t=p.with_name(p.name+'.tmp');t.write_text(json.dumps(result,indent=2)+'\n');t.replace(p)
    print(json.dumps({'status':'PASS','elapsed_seconds':result['elapsed_seconds'],'output':str(p)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();main(a.output)
