#!/usr/bin/env python3
"""Fresh R2 nonauthor checks of R1, independent labeled reference tables."""
from collections import Counter, defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt
from pathlib import Path
import json
import platform
import subprocess
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
AUTHOR=HERE.parent/'r1-short-exact'/'short_exact.py'
spec=spec_from_file_location('author_short_exact', AUTHOR)
author=module_from_spec(spec)
spec.loader.exec_module(author)


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def ts(n):
    ans=[]
    for a,b in combinations(range(n),2):
        p=list(range(n));p[a],p[b]=p[b],p[a]
        ans.append(((a,b),tuple(p)))
    return ans


def typ(p):
    marked=[False]*len(p);out=[]
    for i in range(len(p)):
        if marked[i]:continue
        start=i;size=0
        while not marked[start]:
            marked[start]=True;size+=1;start=p[start]
        if size>1:out.append(size-1)
    return tuple(sorted(out))


def label_tables(n,m):
    ps=list(permutations(range(n)));ix={p:i for i,p in enumerate(ps)}
    moves=ts(n)
    dest=[[ix[compose(p,t)] for _,t in moves] for p in ps]
    rows=[[0]*len(ps)];rows[0][0]=1
    for _ in range(m):
        row=[0]*len(ps)
        for i,c in enumerate(rows[-1]):
            if c:
                for j in dest[i]:row[j]+=c
        rows.append(row)
    return ps,ix,rows


def reference_canonical(word):
    # Independent first-appearance times; ties are ordered by actual label.
    first={}
    for i,edge in enumerate(word):
        for x in edge:first.setdefault(x,i)
    labels=sorted(first,key=lambda x:(first[x],x))
    number={x:i for i,x in enumerate(labels)}
    b=sum(1 for i in range(len(word)) if sum(v==i for v in first.values())==2)
    return tuple(tuple(sorted(number[x] for x in edge)) for edge in word),len(labels),b


def main():
    started=time.monotonic()
    result={'schema':'fresh-r1-short-audit-v1','python':platform.python_version(),'standard_library_only':True,'deterministic':True,'random_seed':None,'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'author_file':str(AUTHOR.relative_to(ROOT))}
    transition_cases=0;endpoint_cases=0;layer_cases=0;minimal_cases=0
    for n in range(1,7):
        ps,ix,rows=label_tables(n,10)
        representatives={}
        for p in ps:
            mu=typ(p);representatives.setdefault(mu,p)
            expected=Counter(typ(compose(t,p)) for _,t in ts(n))
            assert author.transition_counts(n,mu)==expected
            assert sum(expected.values())==comb(n,2)
            transition_cases+=1
        for g in ps:
            h=sum(typ(g))
            mincounts=author.minimal_cycle_counts(n)
            assert author.minimal_completion_count(g,mincounts)==rows[h][ix[g]]
            minimal_cases+=1
            for m in range(11):
                count=rows[m][ix[g]]
                assert author.feasible(n,m,g)==bool(count)
                if not count:continue
                dp=author.BridgeDP(n,m,g)
                assert dp.count==count
                # Check ALL included cone layers against untruncated labeled
                # completion counts, including types not reachable from g.
                for i,table in enumerate(dp.tables):
                    cap=min(h+i,m-i,n-1)
                    for mu,p in representatives.items():
                        if sum(mu)<=cap and (sum(mu)-h-i)%2==0:
                            assert table.get(mu,0)==rows[m-i][ix[p]]
                            layer_cases+=1
                endpoint_cases+=1
    result['transition_checks']=transition_cases
    result['endpoint_count_checks']=endpoint_cases
    result['every_cone_layer_count_checks']=layer_cases
    result['minimal_endpoint_count_checks']=minimal_cases
    word_cases=[]
    for n,m in [(3,4),(4,4),(4,6)]:
        ps,ix,rows=label_tables(n,m)
        dps={p:author.BridgeDP(n,m,p) for p in ps if rows[m][ix[p]]}
        hist=Counter();patterns=Counter()
        for word in product([e for e,_ in ts(n)],repeat=m):
            p=tuple(range(n))
            for edge in word:
                t=dict(ts(n))[edge]
                p=compose(p,t)
            hist[p]+=1
            assert dps[p].word_probability(word)==Fraction(1,rows[m][ix[p]])
            if p==tuple(range(n)):
                key,k,b=reference_canonical(word)
                patterns[(key,k,b)]+=1
                assert k<=m
                actual_key,actual_k,actual_pairs=author.canonical_pattern(word)
                assert (key,k,b)==(actual_key,actual_k,len(actual_pairs))
        for (key,k,b),observed in patterns.items():
            expected=factorial(n)//factorial(n-k)//(2**b)
            assert observed==expected
        generated={(key,k,len(pairs)):author.pattern_weight(n,k,pairs) for key,k,pairs in author.pattern_words(m) if k<=n}
        assert generated==patterns
        word_cases.append({'N':n,'m':m,'all_endpoint_words':sum(hist.values()),'identity_words':hist[tuple(range(n))],'canonical_patterns':len(patterns)})
    result['per_word_and_pattern_checks']=word_cases
    # Enumerate every finite bit tape for the bounded rejection sampler. At
    # S3,m2 only its first draw is random: W=3, two bits per trial.
    bit_tape_results=[]
    class Tape:
        def __init__(self,bits):self.bits=bits;self.pos=0
        def getrandbits(self,k):
            assert self.pos+k<=len(self.bits)
            out=0
            for bit in self.bits[self.pos:self.pos+k]:out=2*out+bit
            self.pos+=k
            return out
    dp=author.BridgeDP(3,2)
    fallback=tuple(author.valid_word(3,2,tuple(range(3))))
    for b in [0,1,2]:
        R=b+2;law=Counter()
        for tape in product([0,1],repeat=2*R):
            word=tuple(dp.sample(Tape(tape),accuracy_bits=b))
            law[word]+=1
            assert author.evaluate(3,word)==tuple(range(3))
        law={w:Fraction(c,2**(2*R)) for w,c in law.items()}
        fail=Fraction(1,4)**R
        for edge,_ in ts(3):
            word=(edge,edge)
            assert law[word]==(1-fail)/3+(fail if word==fallback else 0)
        tv=sum(abs(p-Fraction(1,3)) for p in law.values())/2
        assert tv<=Fraction(1,2**b)
        bit_tape_results.append({'accuracy_bits':b,'trials_per_call':R,'tapes':2**(2*R),'exact_TV':str(tv),'cap_failure_probability':str(fail)})
    result['bounded_random_tapes']=bit_tape_results
    # Verify the counting injection used to charge raw partition generation
    # and the positive midpoint inventory obstruction in small complete cases.
    inventory=[]
    for n in range(2,31):
        for D in range(n):
            S=len(tuple(author.type_universe(n,D)))
            raw=sum(1 for d in range(D+1) for _ in author.partitions(d))
            pnext=sum(1 for _ in author.partitions(D+1))
            assert raw<=(D+1)*pnext<=(D+1)*S
            if 2*D<=n:
                assert all(sum(mu)+len(mu)<=n for mu in author.partitions(D))
            if n in (2,10,30) and D in (0,n//2,n-1):
                inventory.append({'N':n,'D':D,'S':S,'unfiltered_partition_count':raw})
    result['partition_inventory_selected']=inventory
    result['elapsed_seconds']=round(time.monotonic()-started,3)
    result['failures']=0
    HERE.joinpath('fresh_short_audit_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)

if __name__=='__main__':main()
