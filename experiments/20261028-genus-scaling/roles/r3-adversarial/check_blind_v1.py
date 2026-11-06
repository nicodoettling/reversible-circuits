#!/usr/bin/env python3
"""Finite falsification only. Run solely under coordinator bounded reservation."""
import argparse, collections, itertools, json, math, platform, time
from fractions import Fraction as F
from pathlib import Path


def partitions(n,lo=1):
    if n==0:
        yield ()
    else:
        for a in range(lo,n+1):
            for rest in partitions(n-a,a): yield (a,)+rest


def representative(alpha):
    p=[]; off=0
    for a in alpha:
        p.extend(list(range(off+1,off+a))+[off]); off+=a
    return p


def cycle_type(p):
    seen=set(); out=[]
    for a in range(len(p)):
        if a in seen: continue
        j=a; k=0
        while j not in seen: seen.add(j); k+=1; j=p[j]
        out.append(k)
    return tuple(sorted(out))


def tables(nmax,rmax):
    pts={n:list(partitions(n)) for n in range(nmax+1)}
    ordinary={}; connected={}
    for n in range(1,nmax+1):
        trans={}
        for alpha in pts[n]:
            p=representative(alpha); out=collections.Counter()
            for x in range(n):
                for y in range(x+1,n):
                    q=p.copy(); q[x],q[y]=q[y],q[x]
                    out[cycle_type(q)]+=1
            trans[alpha]=out
        ordinary[n]={a:[int(a==(1,)*n)]+[0]*rmax for a in pts[n]}
        for r in range(1,rmax+1):
            for a in pts[n]:
                ordinary[n][a][r]=sum(m*ordinary[n][b][r-1] for b,m in trans[a].items())
        connected[n]={}
        for a in pts[n]:
            values=ordinary[n][a].copy(); mult=collections.Counter(a); anchor=a[0]
            keys=sorted(mult); caps=[mult[k]-int(k==anchor) for k in keys]
            for counts in itertools.product(*(range(c+1) for c in caps)):
                bcounts=dict(zip(keys,counts)); bcounts[anchor]+=1
                b=tuple(k for k in keys for _ in range(bcounts[k])); nb=sum(b)
                if nb==n: continue
                rest=tuple(k for k in keys for _ in range(mult[k]-bcounts[k]))
                ways=math.prod(math.comb(mult[k]-int(k==anchor),bcounts[k]-int(k==anchor)) for k in keys)
                cb=connected[nb][b]; ar=ordinary[n-nb][rest]
                for r in range(rmax+1):
                    values[r]-=ways*sum(math.comb(r,s)*cb[s]*ar[r-s] for s in range(r+1) if cb[s] and ar[r-s])
            assert min(values)>=0
            connected[n][a]=values
    return ordinary,connected


def add(A,B,scale=F(1)):
    C=A.copy()
    for k,v in B.items():
        C[k]=C.get(k,F(0))+scale*v
        if not C[k]: del C[k]
    return C


def mul(A,B,K):
    C={}
    for a,av in A.items():
        for b,bv in B.items():
            c=tuple(x+y for x,y in zip(a,b))
            if sum(c)<=K: C[c]=C.get(c,F(0))+av*bv
    return {k:v for k,v in C.items() if v}


def power(A,j,K):
    D=len(next(iter(A))) if A else 4
    B={(0,)*D:F(1)}
    for _ in range(j): B=mul(B,A,K)
    return B


def inverse(A):
    d=len(A); B=[list(row)+[F(i==j) for j in range(d)] for i,row in enumerate(A)]
    for j in range(d):
        pivot=next(i for i in range(j,d) if B[i][j]); B[pivot],B[j]=B[j],B[pivot]
        q=B[j][j]; B[j]=[x/q for x in B[j]]
        for i in range(d):
            if i!=j:
                q=B[i][j]; B[i]=[a-q*b for a,b in zip(B[i],B[j])]
    return [r[d:] for r in B]


def linear(weights):
    d=len(weights); out={}
    for i,v in enumerate(weights):
        if v: e=[0]*d; e[i]=1; out[tuple(e)]=v
    return out


def subst(A,forms,K):
    d=len(forms); out={}; cached={}
    for a,v in A.items():
        term={(0,)*d:v}
        for i,e in enumerate(a):
            if (i,e) not in cached: cached[i,e]=power(forms[i],e,K)
            term=mul(term,cached[i,e],K)
        out=add(out,term)
    return out


def recover_two(connected):
    d=4; K=3; E=5; zero=(0,)*d
    phi=[linear([F(a**(a+j),math.factorial(a)) for a in range(1,d+1)]) for j in range(d+1)]
    out={}
    for n,typs in connected.items():
        for alpha,counts in typs.items():
            if len(alpha)>K or max(alpha)>d: continue
            r=n+len(alpha)+2
            z=math.prod(a for a in alpha)*math.prod(math.factorial(m) for m in collections.Counter(alpha).values())
            h=F(counts[r],math.factorial(r)*z)
            if not h: continue
            e=tuple(alpha.count(a) for a in range(1,d+1))
            for j in range(K-len(alpha)+1):
                out=add(out,mul({e:h*F((-n)**j,math.factorial(j))},power(phi[0],j,K),K))
    denominator=add({zero:F(1)},phi[1],F(-1))
    Pp=mul(out,power(denominator,E,K),K)
    V=[[F(a**(a+j),math.factorial(a)) for a in range(1,d+1)] for j in range(1,d+1)]
    inv=inverse(V); Py=subst(Pp,[linear(row) for row in inv],K)
    Y=[linear([F(i==j) for i in range(d)]) for j in range(d)]
    Q3=add(add({},Y[3],F(5)),Y[2],F(-12)); Q3=add(Q3,Y[1],F(7))
    Q4=add(mul(Y[1],Y[2],K),{},F(0)); Q4={a:29*v for a,v in Q4.items()}; Q4=add(Q4,power(Y[1],2,K),F(-25))
    Q5={a:28*v for a,v in power(Y[1],3,K).items()}
    den=add({zero:F(1)},Y[0],F(-1))
    expected=add(add(mul(Q3,power(den,2,K),K),mul(Q4,den,K)),Q5)
    expected={a:v/F(5760) for a,v in expected.items()}
    assert Py==expected,(Py,expected)
    return Py


def rises(e,q):
    if e==0: return int(q==0)
    return math.factorial(e+q-1)//math.factorial(e-1)


def descriptor_value(sizes,slots,e):
    """Independent direct injection/subset definition of one normalized term."""
    n=sum(sizes); k=len(sizes); out=0
    for inject in itertools.permutations(range(k),len(slots)):
        marked=set(inject); fixed=math.prod(sizes[i]**j for i,j in zip(inject,slots))
        rest=[i for i in range(k) if i not in marked]
        for q in range(len(rest)+1):
            for ordinary in itertools.combinations(rest,q):
                out+=fixed*rises(e,q)*math.prod(sizes[i] for i in ordinary)*n**(len(rest)-q)
    return out


def forced_mask(sizes,slotsA,eA,slotsB,eB,forced):
    """New subset-mask DP, looping target child degree; no slot injections."""
    total=sum(sizes); da=len(slotsA); db=len(slotsB); out=0
    for target in range(1,total):
        tab={(0,0,0,0):1} # A degree, qA, qB, combined mask
        for i,a in enumerate(sizes):
            nxt=collections.defaultdict(int)
            for (s,qa,qb,mask),v in tab.items():
                for side in (0,1):
                    if i in forced and forced[i]!=side: continue
                    ns=s+a if side==0 else s
                    if ns>target: continue
                    nside=target if side==0 else total-target
                    nxt[ns,qa,qb,mask]+=v*nside
                    if side==0: nxt[ns,qa+1,qb,mask]+=v*a
                    else: nxt[ns,qa,qb+1,mask]+=v*a
                    start=0 if side==0 else da; slots=slotsA if side==0 else slotsB
                    for j,expo in enumerate(slots):
                        bit=1<<(start+j)
                        if not mask&bit: nxt[ns,qa,qb,mask|bit]+=v*a**expo
            tab=nxt
        full=(1<<(da+db))-1
        out+=sum(v*rises(eA,qa)*rises(eB,qb) for (s,qa,qb,mask),v in tab.items() if s==target and mask==full)
    return out


def check_masks():
    cases=0
    data=[(1,1),(1,1,1),(1,2,1),(1,1,2,2),(1,2,1,3,1),(1,1,1,1,1,1)]
    specs=[((),0,(),0),((2,),1,(),0),((1,),0,(2,),1),((2,2),3,(3,),2),((1,2,3),4,(2,2,2),5)]
    for sizes in data:
        k=len(sizes)
        for sa,ea,sb,eb in specs:
            for extra in [None,0,1]:
                forced={0:0,1:1}
                if k>2 and extra is not None: forced[k-1]=extra
                exact=0
                for assign in itertools.product((0,1),repeat=k):
                    if any(assign[i]!=side for i,side in forced.items()): continue
                    A=[a for a,s in zip(sizes,assign) if s==0]; B=[a for a,s in zip(sizes,assign) if s==1]
                    exact+=descriptor_value(A,sa,ea)*descriptor_value(B,sb,eb)
                actual=forced_mask(sizes,sa,ea,sb,eb,forced)
                assert actual==exact,(sizes,sa,sb,forced,actual,exact)
                cases+=1
    return cases


def connected_state_dp(n,rmax):
    """Independent literal state DP (endpoint permutation, support partition)."""
    start=(tuple(range(n)),tuple(range(n))); tab={start:1}; bylen=[]
    edges=list(itertools.combinations(range(n),2))
    for r in range(rmax+1):
        counts=collections.Counter()
        for (p,blocks),v in tab.items():
            if len(set(blocks))==1: counts[p]+=v
        bylen.append(counts)
        if r==rmax: break
        nxt=collections.defaultdict(int)
        for (p,blocks),v in tab.items():
            for x,y in edges:
                q=list(p); q[x],q[y]=q[y],q[x]
                b=list(blocks); lo=min(b[x],b[y]); hi=max(b[x],b[y]); b=[lo if z==hi else z for z in b]
                nxt[tuple(q),tuple(b)]+=v
        tab=nxt
    return bylen


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    started=time.monotonic(); ordinary,connected=tables(12,28)
    P=recover_two(connected); finite=0; ids=[]
    for n in (2,3,4):
        literal=connected_state_dp(n,2*n+4)
        for g in range(4):
            r=2*n-2+2*g
            ids.append({'n':n,'g':g,'count':connected[n][(1,)*n][r]})
        for r,counts in enumerate(literal):
            for p in itertools.permutations(range(n)):
                assert counts[p]==connected[n][cycle_type(p)][r]
                finite+=1
    assert ordinary[3][(1,1,1)][4]==27
    assert ordinary[4][(1,1,1,1)][4]==120
    assert ordinary[4][(1,1,1,1)][6]==3936
    assert ordinary[3][(1,2)][5]==81 and connected[3][(1,2)][5]==80
    assert F(21,2000)>F(1,100)
    mask_cases=check_masks()
    result={'status':'pass','purpose':'finite falsification; no asymptotic certification','source_commit':'b178daf320833e859dcdee0ce56eb16c6d2130b7','python':platform.python_version(),'dependencies':'stdlib only','seed':0,'deterministic':True,'ordinary_connected_table':{'nmax':12,'rmax':28},'recovered_genus_two_numerator':[{'powers':list(a),'numerator':v.numerator,'denominator':v.denominator} for a,v in sorted(P.items())],'independent_literal_state_comparisons':finite,'forced_mask_cases':mask_cases,'identity_counts':ids,'retained_regressions':{'S3m4':27,'S4m4':120,'S4m6':3936,'ordinary_vs_connected_endpoint':[81,80],'CP1':[str(F(21,2000)),str(F(1,100))]},'elapsed_seconds':time.monotonic()-started}
    dest=Path(args.output); tmp=dest.with_suffix(dest.suffix+'.tmp'); tmp.write_text(json.dumps(result,indent=2)+'\n'); tmp.replace(dest)
    print(json.dumps({'status':'pass','literal_comparisons':finite,'mask_cases':mask_cases,'elapsed_seconds':result['elapsed_seconds']}))
if __name__=='__main__': main()
