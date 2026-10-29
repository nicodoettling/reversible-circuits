"""Independent tiny decisive reruns and LC1-v2 denominator regression; bounded only."""
import argparse,itertools as it,math,json,os,platform,subprocess,time,importlib.util
from fractions import Fraction as F
from collections import Counter
from pathlib import Path

def prime_list_after(n,count):
    values=[];v=n+1
    while len(values)<count:
        if all(v%d for d in range(2,math.isqrt(v)+1)):values.append(v)
        v+=1
    return values

def average(f,x,indices,q):
    total=F()
    for values in it.product(range(q),repeat=len(indices)):
        z=list(x)
        for i,a in zip(indices,values):z[i]=a
        total+=f[tuple(z)]
    return total/q**len(indices)

def denominator_checks():
    rows=[]
    for s in range(1,7):
        q=2;domain=list(it.product(range(q),repeat=s));M=len(domain)
        primes=prime_list_after(M,M);f={x:F(1,p) for x,p in zip(domain,primes)}
        mean=sum(f.values(),F())/M
        # No denominator prime cancels: modulo that prime only one summand survives.
        assert all(mean.denominator%p==0 for p in primes)
        b=max(p.bit_length() for p in primes)
        row=dict(q=q,s=s,distinct_values=M,max_value_denominator_bits=b,mean_denominator_bits=mean.denominator.bit_length(),all_distinct_primes_retained=True)
        if s<=4:
            L=s+2;k=2;alphas=[F(math.comb(L-j,k),math.comb(L,k)) for j in range(s+1)]
            g={}
            for x in domain:
                value=F()
                for mask in range(1<<s):
                    S=tuple(i for i in range(s) if mask>>i&1);outside=tuple(i for i in range(s) if not mask>>i&1)
                    component=F()
                    for sub in range(1<<len(S)):
                        extra=tuple(S[i] for i in range(len(S)) if sub>>i&1)
                        component+=(-1)**len(extra)*average(f,x,outside+extra,q)
                    value+=component/alphas[len(S)]
                g[x]=value
            h={x:F(1,2)+alphas[s]*g[x]/(2*3**s) for x in domain}
            common=math.prod(primes)*q**s*math.prod(a.numerator for a in alphas)*alphas[s].denominator*2*3**s
            for x in domain:
                assert 0<=h[x]<=1 and common%h[x].denominator==0
                Tg=sum((average(g,x,tuple(i for i in I if i<s),q) for I in it.combinations(range(L),k)),F())/math.comb(L,k)
                assert Tg==f[x]
            row.update(L=L,k=k,inverse_identity_passed=True,h_common_denominator_bits=common.bit_length(),max_h_denominator_bits=max(a.denominator.bit_length() for a in h.values()))
        rows.append(row)
    return rows

def evaluate_independent(n,word):
    # Apply rightmost gate first to each point; independent of array-right-multiply code.
    out=[]
    for x in range(n):
        y=x
        for a,b in reversed(word):
            if y==a:y=b
            elif y==b:y=a
        out.append(y)
    return tuple(out)

def decisive_counts(n,L):
    edges=list(it.combinations(range(n),2));identity=tuple(range(n));count=paired=small_support=0
    m=L//2
    for word in it.product(edges,repeat=L):
        if evaluate_independent(n,word)!=identity:continue
        count+=1;hist=Counter(word);support={x for edge in word for x in edge}
        paired+=len(hist)==m and len(support)==2*m and all(v==2 for v in hist.values())
        small_support+=len(support)<=m+1
    if (n,L)==(4,6):assert count==3936
    if (n,L)==(6,4):
        assert count==765 and paired==270 and F(small_support,count)==F(11,17)
        assert paired==math.prod(range(n-2*m+1,n+1))*math.factorial(2*m)//(4**m*math.factorial(m))
    return dict(N=n,L=L,identity_words=count,distinct_disjoint_doubled_words=paired,reference_support_threshold=m+1,reference_support_acceptance=str(F(small_support,count)))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();p=Path(args.output)
    if p.exists():raise SystemExit('immutable output already exists')
    start=time.monotonic();result=dict(status='passed',python=platform.python_version(),dependencies='stdlib',randomness='none; exact integer/rational enumeration',commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),denominator_checks=denominator_checks(),independent_decisive_counts=[decisive_counts(4,6),decisive_counts(6,4)])
    result['elapsed_seconds']=time.monotonic()-start;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(result,indent=2)+'\n');os.replace(t,p)
    print(json.dumps(dict(status='passed',elapsed_seconds=result['elapsed_seconds'],output=str(p))))
if __name__=='__main__':main()
