"""Bounded candidate and support-count regression. Never run outside reservation."""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, log, prod
from pathlib import Path
import hashlib
import json
import os
import platform
import random
import subprocess
import time
from candidates_v1 import (c1, c1_block, c2, c2_word, evaluate, hurwitz_at,
                           null_six_count, replacement, support)


def count_d(n,m):
    return prod(range(n-2*m+1,n+1))*factorial(2*m)//(4**m*factorial(m))


def check_case(n,length):
    edges=list(combinations(range(n),2)); identity=tuple(range(n))
    words=[w for w in product(edges,repeat=length) if evaluate(n,w)==identity]
    expected={(3,4):27,(4,4):120,(4,6):3936,(6,4):765}
    assert len(words)==expected[n,length]
    move_checks=0
    for w in words:
        for i in range(length-1):
            for inv in (False,True):
                v=hurwitz_at(w,i,inv)
                assert evaluate(n,v)==identity
                assert support(v)==support(w)
                assert hurwitz_at(v,i,not inv)==list(w)
                move_checks+=1
    m=length//2
    injections=list(permutations(range(n),m+1))
    base=[tuple(c2_word(t)) for t in injections]
    assert len(set(base))==len(injections)
    assert all(evaluate(n,w)==identity and len(support(w))==m+1 for w in base)
    for i in range(length):
        hist=Counter(w[i] for w in base)
        assert set(hist)==set(edges) and len(set(hist.values()))==1
    support_hist=Counter(len(support(w)) for w in words)
    disjoint_count=None
    if n>=2*m:
        disjoint_count=sum(len(set(w))==m and len(support(w))==2*m and
                           all(c==2 for c in Counter(w).values()) for w in words)
        assert disjoint_count==count_d(n,m)
    return {"N":n,"L":length,"global_count":len(words),
            "all_signed_move_checks":move_checks,
            "C2_injections":len(injections),"C2_injective":True,
            "C2_uniform_position_marginals":True,
            "global_support_histogram":dict(sorted(support_hist.items())),
            "disjoint_paired_count":disjoint_count,
            "C2_k0_support_acceptance_reference":str(Fraction(sum(c for size,c in support_hist.items() if size<=m+1),len(words)))}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args();out=Path(args.output)
    if out.exists():
        raise SystemExit('refusing to overwrite immutable output')
    started=time.time()
    cases=[check_case(*case) for case in [(3,4),(4,4),(4,6),(6,4)]]
    for n in (4,5):
        blocks=[tuple(c1_block(t)) for t in permutations(range(n),4)]
        assert len(set(blocks))==len(blocks)
        assert all(evaluate(n,w)==tuple(range(n)) and len(set(w))==6 for w in blocks)
        for i in range(6):
            assert len(set(Counter(w[i] for w in blocks).values()))==1
    sample_checks=0;seeds=[17,29,43]
    for seed in seeds:
        rng=random.Random(seed)
        for n,m in [(3,2),(4,2),(4,3),(12,8)]:
            for _ in range(40):
                w=c2(n,m,(2*m)**3,rng)
                assert evaluate(n,w)==tuple(range(n)) and len(support(w))==m+1
                for k in sorted({0,1,2*m}):
                    noisy=replacement(n,w,k,rng)
                    assert len(support(noisy))<=min(n,m+1+2*k)
                    assert sum(a!=b for a,b in zip(evaluate(n,noisy),range(n)))<=4*k
                    sample_checks+=1
        for _ in range(100):
            n,blocks,steps,k=12,30,3,5
            w=c1(n,blocks,steps,rng);noisy=replacement(n,w,k,rng)
            assert evaluate(n,w)==tuple(range(n))
            assert null_six_count(n,noisy)>=blocks-2*steps-k
            sample_checks+=1
    rng=random.Random(7)
    assert replacement(2,[],0,rng)==[]
    for length in (0,2,4,6):
        w=[(0,1)]*length
        for k in range(length+1):
            assert replacement(2,w,k,rng)==w
    for n in (2,3,4):
        for length in (1,3):
            assert not any(evaluate(n,w)==tuple(range(n)) for w in product(combinations(range(n),2),repeat=length))
    schedule=[]
    for m in (64,128,256,512,1024):
        n=m**6;h=m+1+2*int(m**0.5)
        numerator=comb(n,h)*comb(h,2)**(2*m)
        denominator=count_d(n,m)
        log_bound=log(numerator)-log(denominator)
        if m>=1024:
            assert numerator*m**m<=denominator
        schedule.append({"lambda":m,"h":h,"log_exact_C2_bound":log_bound,
                         "bound_le_lambda_minus_lambda":numerator*m**m<=denominator})
    result={"status":"passed","python":platform.python_version(),
      "dependencies":"stdlib only","commit":subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
      "command":"python3 -B experiments/20261029-noisy-bridge-viability/r2-construction/check_candidates_v2.py --output "+str(out),
      "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "implementation_sha256":hashlib.sha256(Path(__file__).with_name('candidates_v1.py').read_bytes()).hexdigest(),
      "cases":cases,"seeds":seeds,"stochastic_regression_checks":sample_checks,
      "sample_claim":"Implementation checks only, not empirical security estimates",
      "boundary_checks":["N2 singleton even words","empty word k0","odd length infeasible","k0 k1 kL samples"],
      "C2_schedule_checks":schedule,"elapsed_seconds":time.time()-started}
    temp=out.with_suffix(out.suffix+'.tmp');temp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');os.replace(temp,out)
    print(json.dumps({"status":"passed","output":str(out),"cases":len(cases),"elapsed_seconds":result['elapsed_seconds']}))

if __name__=='__main__':main()
