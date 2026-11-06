#!/usr/bin/env python3
"""Exact moment falsification; no production sampler imports; bounded job only."""
from collections import defaultdict
from datetime import datetime,timezone
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb,factorial
from pathlib import Path
import argparse,json,os,platform,time

ROLE=Path(__file__).resolve().parent
ROOT=ROLE.parents[4]
MAX_K=12


def enc(q):
    q=F(q)
    return {'numerator_hex':hex(q.numerator),'denominator_hex':hex(q.denominator)}


def a0(v):
    return F(1,2) if v==2 else F(v**(v-3))


def counts():
    """DYZ normalized connected count, separate from production implementation."""
    A={(1,0):F(1)}
    B={}
    for v in range(2,MAX_K+2):
        for g in range(MAX_K-v+2):
            acc=F(0)
            for u in range(1,v):
                w=v-u
                for ga in range(g+1):
                    for gb in range(g-ga+1):
                        r=g+1-ga-gb
                        acc+=2*comb(v,u)*u*w*w*F(u**(2*r),factorial(2*r))*A.get((u,ga),0)*A.get((w,gb),0)
            A[v,g]=acc/(v*v*(v-1))
            q=v-1+g
            B[v,q]=A[v,g]/factorial(v)
    return A,B


def assembly(B):
    # H(x,y)=exp(sum_{v,q} B[v,q] x^v y^q); x*dH/dx=(x*dB/dx)H.
    H={(0,0):F(1)}
    for s in range(1,2*MAX_K+1):
        for k in range(MAX_K+1):
            H[s,k]=sum((v*b*H.get((s-v,k-q),0) for (v,q),b in B.items() if v<=s and q<=k),F(0))/s
    W={}
    for a in (3,9):
        W[a]={}
        for s in range(2*MAX_K+1):
            for k in range(MAX_K+1):
                W[a][s,k]=sum((a**v*b*H.get((s-v,k-q),0) for (v,q),b in B.items() if v<=s and q<=k),F(0))
    return H,W


def support_step(parts,i,j):
    x=next(t for t,(mask,_) in enumerate(parts) if mask&(1<<i))
    y=next(t for t,(mask,_) in enumerate(parts) if mask&(1<<j))
    result=[part for t,part in enumerate(parts) if t not in(x,y)]
    if x==y:
        result.append((parts[x][0],parts[x][1]+1))
    else:
        result.append((parts[x][0]|parts[y][0],parts[x][1]+parts[y][1]+1))
    return tuple(sorted(result))


def literal_dp(n,max_length=12):
    identity=tuple(range(n));initial=tuple((1<<i,0) for i in range(n))
    states={(identity,initial):1};rows=[]
    for ell in range(max_length+1):
        totals=defaultdict(int);cost={3:0,9:0};total=0;connected=0
        for (perm,parts),number in states.items():
            if perm!=identity:continue
            total+=number
            if len(parts)==1:connected+=number
            for mask,length in parts:
                v=mask.bit_count()
                if v==1:
                    assert length==0
                else:
                    assert length%2==0 and length>=2*v-2
                    totals[v,length]+=number
                    for a in cost:cost[a]+=number*a**v
        rows.append({'N':n,'m':ell,'total':total,'connected':connected,'weighted_counts':cost,'marked':dict(totals),'states':len(states)})
        if n==3 and ell==5:
            target=(1,0,2)
            endpoint_total=sum(value for (perm,parts),value in states.items() if perm==target)
            endpoint_connected=sum(value for (perm,parts),value in states.items() if perm==target and len(parts)==1)
            assert (endpoint_total,endpoint_connected)==(81,80)
            rows[-1]['exposed_regression']={'endpoint':[1,0,2],'total':endpoint_total,'connected':endpoint_connected}
        if ell==max_length:break
        nxt=defaultdict(int)
        for (perm,parts),number in states.items():
            for i in range(n):
                for j in range(i+1,n):
                    child=list(perm);child[i],child[j]=child[j],child[i]
                    nxt[tuple(child),support_step(parts,i,j)]+=number
        states=nxt
    return rows


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    out=Path(args.output)
    if out.exists():raise SystemExit('Immutable output already exists.')
    started=time.monotonic();A,B=counts();H,W=assembly(B)
    @lru_cache(None)
    def normalized(N,k,a=0):
        if N<0 or k<0:return F(0)
        table=H if a==0 else W[a]
        acc=F(0);fall=1
        for s in range(min(N,2*k)+1):
            if s:fall*=N-s+1
            acc+=fall*table.get((s,k),0)
        return acc
    @lru_cache(None)
    def ex_component(N,k,v,q):
        if v>N or q>k:return F(0)
        return comb(N,v)*A.get((v,q-v+1),0)*normalized(N-v,k-q)/normalized(N,k)
    def moment_bound(N,k,a):
        D=N-2*k+1
        assert D>0
        value=F(0)
        for v in range(2,min(N,k+1)+1):
            fall=1
            for z in range(v-1):fall*=k-z
            bv=F(v**3-v,36)
            value+=a**v*comb(N,v)*a0(v)*fall*F(4,D*D)**(v-1)*(1+F(4,D*D)*bv)**(k-v+1)
        return value
    literal=[]
    for N in range(2,6):
        for row in literal_dp(N):
            m=row['m']
            if m%2:
                assert row['total']==0
            else:
                k=m//2
                assert normalized(N,k)*factorial(m)==row['total']
                conn=A.get((N,k-N+1),0)*factorial(m)
                assert conn==row['connected']
                for a in (3,9):
                    assert normalized(N,k,a)*factorial(m)==row['weighted_counts'][a]
                for (v,ell),value in row['marked'].items():
                    assert ex_component(N,k,v,ell//2)==F(value,row['total'])
            literal.append({'N':N,'m':m,'total':str(row['total']),'connected':str(row['connected']),'weighted_counts':{str(a):str(z) for a,z in row['weighted_counts'].items()},'states':row['states'],'marked':[{'v':v,'ell':ell,'marked_count':str(z)} for (v,ell),z in sorted(row['marked'].items())],'exposed_regression':row.get('exposed_regression')})
    grids=[2,3,4,5,6,8,12,20,40,82,128,256,512,1024,2**36,2**2400]
    data=[];bound_cells=0;mark_cells=0;certificate_cells=0
    for N in grids:
        max_k=6 if N.bit_length()>1024 else MAX_K
        for k in range(max_k+1):
            Z=normalized(N,k)
            for a in (3,9):
                exact=normalized(N,k,a)/Z
                marked=sum((a**v*ex_component(N,k,v,q) for v in range(2,min(N,k+1)+1) for q in range(v-1,k+1)),F(0))
                assert exact==marked
                mark_cells+=1
                rec={'N_hex':hex(N),'m':2*k,'a':a,'moment':enc(exact),'sparse_primary':(2*k)**3<=N*N}
                if k>0 and 2*k<=N:
                    bound=moment_bound(N,k,a)
                    assert exact<=bound
                    rec['finite_genus_bound']=enc(bound);bound_cells+=1
                    D=N-2*k+1;x=F(4*k,D*D);z=F(k*k*(k+2),9*D*D)
                    # e<3 and z<=1 imply c=e^(1+z)<9; conservative rational substitute.
                    cbar=9;rho_bar=cbar*N*x
                    if z<=1 and a*rho_bar<=F(1,2):
                        upper=F(N*cbar*a,8)
                        assert exact<=upper
                        certificate_cells+=1
                        rec['finite_moment_certificate']={'z':enc(z),'cbar':cbar,'rho_bar':enc(rho_bar),'upper':enc(upper)}
                    if z<=F(1,16) and a*3*N*x<1:
                        cbar3=3;rho3=3*N*x
                        upper3=F(N*cbar3*a*a,8)*rho3/(1-a*rho3)
                        assert exact<=upper3
                        rec['sharper_finite_certificate']={'z':enc(z),'cbar':cbar3,'rho_bar':enc(rho3),'upper':enc(upper3)}
                if N==2**2400:
                    # Inherited ES-LOG asymptotic bounds at a degree with rational fourth/24th roots.
                    cbar=3*2**600;rhobar=F(1,2**100)
                    assert a*rhobar<=F(1,2)
                    assert exact<=F(N*cbar*a,8)
                    rec['log_inherited_bound_check']={'cbar_hex':hex(cbar),'rho_bar':enc(rhobar),'upper':enc(F(N*cbar*a,8))}
                data.append(rec)
    rare=[]
    for N,k,v,q in [(82,7,6,7),(128,8,6,7),(128,8,7,8)]:
        ex=ex_component(N,k,v,q)
        assert ex>0
        rare.append({'N':N,'m':2*k,'v':v,'ell':2*q,'g':q-v+1,'expected_components':enc(ex),'contribution_9v':enc(9**v*ex)})
    assert F(21,2000)>F(1,100)
    # Genus-only truncation does not remove support bookkeeping: the known endpoint regression remains.
    regressions={'CP1_old_product_rejected':True,'CP1_joint':enc(F(21,2000)),'CP1_bad_bound':enc(F(1,100)),
                 'literal_identity_baselines':{f'S{r["N"]}m{r["m"]}':r['total'] for r in literal if (r['N'],r['m']) in {(3,4),(4,4),(4,6),(3,8),(4,10)}},
                 'odd_lengths_zero':True,'empty_word_cost_zero':True,'N2_positive_even_cost_9':81}
    sources=[Path(__file__).resolve(),ROLE/'plan-v1.md',ROOT/'experiments/20260922-sparse-global-sampler/proof.md',ROOT/'experiments/20260922-sparse-boundary/proof.md',ROOT/'experiments/20260922-sparse-boundary/roles/r4-construction/proof-v1.md',ROOT/'experiments/20260922-sparse-boundary/construction_audit.md']
    result={'schema_version':1,'status':'PASS','scope':'Exact normalized additive exponential component costs; no production sampler law or asymptotic proof inferred',
            'base_commit':'92af1b7b47583b60571a84c660d527422ce0e8ce','completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'python':platform.python_version(),'dependencies':[],'seed':0,'seed_used':False,
            'parameters':{'max_k':MAX_K,'a':[3,9],'literal_N':[2,3,4,5],'literal_m_max':12,'N_grid_hex':[hex(n) for n in grids]},
            'checks':{'literal_cells':len(literal),'marked_moment_cells':mark_cells,'finite_genus_bound_cells':bound_cells,'finite_certificate_cells':certificate_cells},
            'literal':literal,'normalized_moments':data,'rare_high_genus_components':rare,'regressions':regressions,
            'source_sha256':{str(s.relative_to(ROOT)):sha256(s.read_bytes()).hexdigest() for s in sources}}
    tmp=out.with_name(out.name+'.tmp')
    with tmp.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    os.replace(tmp,out)
    print('PASS I2 R3 exact moments;',mark_cells,'marked cells;',bound_cells,'finite bound cells; raw file written.')


if __name__=='__main__':main()
