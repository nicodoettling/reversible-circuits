"""Exact finite coefficient reconstruction for connected Hurwitz words.
Coordinator author, 2026-10-28. Provisional implementation of COEFF-EXP.v1.
Standard library only. No random sampling. Run experiments only via bounded helper.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, prod
import argparse, datetime, hashlib, json, os, platform, subprocess, time
from pathlib import Path


def partitions(n, lo=1):
    if n == 0:
        yield ()
    for a in range(lo, n + 1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def permutation(alpha):
    ans=[]; start=0
    for a in alpha:
        ans.extend(list(range(start+1,start+a))+[start]); start+=a
    return tuple(ans)


def cycle_type(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; a=0
        while j not in seen:
            seen.add(j); a+=1; j=p[j]
        out.append(a)
    return tuple(sorted(out))


@lru_cache(None)
def transitions(alpha):
    p=permutation(alpha); ans=Counter()
    for x,y in combinations(range(len(p)),2):
        q=list(p); q[x],q[y]=q[y],q[x]
        ans[cycle_type(q)]+=1
    return tuple(ans.items())


@lru_cache(None)
def ordinary(alpha, length):
    if length<0: return 0
    n=sum(alpha); distance=n-len(alpha)
    if length<distance or (length-distance)%2: return 0
    if length==0: return int(distance==0)
    if n<2: return 0
    return sum(m*ordinary(mu,length-1) for mu,m in transitions(alpha))


def proper_anchored_subprofiles(alpha):
    """All actual indexed subsets containing first cycle, grouped by lengths."""
    rest=Counter(alpha[1:]); keys=tuple(sorted(rest)); first=alpha[0]
    for counts in product(*(range(rest[a]+1) for a in keys)):
        picked=tuple(a for a,c in zip(keys,counts) for _ in range(c))
        u=tuple(sorted((first,)+picked))
        if len(u)==len(alpha): continue
        v=tuple(a for a,c in zip(keys,counts) for _ in range(rest[a]-c))
        multiplicity=prod(comb(rest[a],c) for a,c in zip(keys,counts))
        yield u,v,multiplicity


@lru_cache(None)
def connected(alpha,length):
    if not alpha: return 0
    n=sum(alpha); k=len(alpha)
    if n==1: return int(length==0)
    minimum=n+k-2
    if length<minimum or (length-minimum)%2: return 0
    answer=ordinary(alpha,length)
    for u,v,multiplicity in proper_anchored_subprofiles(alpha):
        min_u=sum(u)+len(u)-2
        min_v=sum(v)-len(v)
        if sum(u)==1: lengths=(0,)
        else: lengths=range(min_u,length-min_v+1,2)
        for s in lengths:
            answer-=multiplicity*comb(length,s)*connected(u,s)*ordinary(v,length-s)
    assert answer>=0, (alpha,length,answer)
    return answer


@lru_cache(None)
def normalized(genus,alpha):
    n=sum(alpha); length=n+len(alpha)-2+2*genus
    return Fraction(connected(alpha,length)*prod(factorial(a-1) for a in alpha),
                    factorial(length)*prod(a**a for a in alpha))


@lru_cache(None)
def difference(genus,beta):
    # Symmetry makes sorting beta safe; variables remain labeled in expansion.
    total=Fraction(0)
    for gamma in product(*(range(b+1) for b in beta)):
        weight=prod(comb(b,c) for b,c in zip(beta,gamma))
        if (sum(beta)-sum(gamma))%2: weight=-weight
        alpha=tuple(sorted(c+1 for c in gamma))
        total+=weight*normalized(genus,alpha)
    return total


@lru_cache(None)
def shifted_binomial_coeff(n,k):
    """Coefficient of a**k in binom(a-1,n)."""
    p=[1]
    for j in range(1,n+1):
        q=[0]*(len(p)+1)
        for i,c in enumerate(p): q[i]-=j*c; q[i+1]+=c
        p=q
    return Fraction(p[k] if k<len(p) else 0,factorial(n))


def simplex(d,total):
    if d==0:
        yield ()
    else:
        for a in range(total+1):
            for tail in simplex(d-1,total-a): yield (a,)+tail


def hodge_coefficient(genus,theta):
    d=len(theta); degree=3*genus-3+d
    slack=degree-sum(theta); result=Fraction(0)
    for eta in simplex(d,slack):
        beta=tuple(t+e for t,e in zip(theta,eta))
        coefficient=prod(shifted_binomial_coeff(b,t) for b,t in zip(beta,theta))
        result+=coefficient*difference(genus,tuple(sorted(beta)))
    return result


def recover(genus):
    assert genus>=2
    out=[]
    for weight in range(2*genus-3,3*genus-2):
        for lam in partitions(weight):
            theta=tuple(a+1 for a in lam)
            kappa=hodge_coefficient(genus,theta)
            aut=prod(factorial(c) for c in Counter(theta).values())
            out.append({'theta':list(theta),'denominator_power':2*genus-2+len(theta),
                        'K':[kappa.numerator,kappa.denominator],
                        'coefficient':[(kappa/aut).numerator,(kappa/aut).denominator]})
    return out


def marker_count(genus,alpha,terms):
    """Direct subset marker DP, independent of interpolation recurrence."""
    n=sum(alpha); k=len(alpha); answer=Fraction(0)
    for term in terms:
        theta=term['theta']; d=len(theta)
        if d>k: continue
        table={(0,0):1}
        for a in alpha:
            nxt=defaultdict(int)
            for (j,mask),v in table.items():
                nxt[j,mask]+=v
                nxt[j+1,mask]+=a*v
                for t,power in enumerate(theta):
                    if not(mask>>t&1): nxt[j,mask|(1<<t)]+=a**power*v
            table=nxt
        e=term['denominator_power']-1
        raw=0
        for j in range(k-d+1):
            rising=prod(range(e,e+j))
            raw+=rising*n**(k-d-j)*table.get((j,(1<<d)-1),0)
        answer+=Fraction(*term['coefficient'])*raw
    length=n+k-2+2*genus
    answer*=factorial(length)*prod(Fraction(a**a,factorial(a-1)) for a in alpha)
    assert answer.denominator==1,(genus,alpha,answer)
    return answer.numerator


def literal_connected_counts(n,max_length):
    """Tiny independent DP over endpoint and label support partition."""
    identity=tuple(range(n)); start=(identity,tuple(range(n)))
    states={start:1}; out=[]
    edges=list(combinations(range(n),2))
    for length in range(max_length+1):
        counts=defaultdict(int)
        for (p,blocks),v in states.items():
            if len(set(blocks))==1: counts[p]+=v
        out.append(dict(counts))
        if length==max_length: break
        nxt=defaultdict(int)
        for (p,blocks),v in states.items():
            for x,y in edges:
                q=list(p);q[x],q[y]=q[y],q[x]
                bx,by=blocks[x],blocks[y]; small=min(bx,by);large=max(bx,by)
                b=tuple(small if a==large else a for a in blocks)
                nxt[tuple(q),b]+=v
        states=nxt
    return out


def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp');tmp.write_text(json.dumps(obj,indent=2)+'\n');os.replace(tmp,path)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    parser.add_argument('--genera',nargs='+',type=int,default=[2,3]);args=parser.parse_args()
    start=time.monotonic(); result={'status':'running','genera':args.genera,'seed':None,'python':platform.python_version(),'dependencies':'standard library','commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'command':__import__('sys').argv,'coefficients':{},'checks':[]}
    # Primitive quotient/connected counts checked against disjoint endpoint/support DP.
    for n in (2,3,4):
        dp=literal_connected_counts(n,12 if n<4 else 12)
        for length,counts in enumerate(dp):
            for alpha in partitions(n):
                got=connected(alpha,length); want=counts.get(permutation(alpha),0)
                assert got==want,(n,length,alpha,got,want)
                result['checks'].append({'kind':'connected-DP','N':n,'length':length,'alpha':alpha,'count':got})
    assert ordinary((1,1,1),4)==27
    assert ordinary((1,1,1,1),4)==120
    assert ordinary((1,1,1,1),6)==3936
    assert ordinary((1,2),5)==81 and connected((1,2),5)==80
    for g in args.genera:
        terms=recover(g); result['coefficients'][str(g)]=terms
        if g==2:
            expected={(2,):[7,5760],(3,):[-12,5760],(4,):[5,5760],(2,2):[-25,5760],(2,3):[29,5760],(2,2,2):[28,5760]}
            assert {tuple(t['theta']):Fraction(*t['coefficient']) for t in terms}=={k:Fraction(*v) for k,v in expected.items()}
        for n in range(1,9):
            for alpha in partitions(n):
                got=marker_count(g,alpha,terms);want=connected(alpha,n+len(alpha)-2+2*g)
                assert got==want,(g,alpha,got,want)
                result['checks'].append({'kind':'recovered-marker','g':g,'alpha':alpha,'count':got})
    result.update(status='passed',elapsed_seconds=time.monotonic()-start,cache_sizes={f.__name__:f.cache_info().currsize for f in (ordinary,connected,normalized,difference)},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    atomic_json(args.output,result)
    print(json.dumps({'status':result['status'],'checks':len(result['checks']),'genera':args.genera,'seconds':result['elapsed_seconds'],'output':args.output}))

if __name__=='__main__':main()
