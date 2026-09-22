#!/usr/bin/env python3
"""Nonauthor actual-forward H1 and fixed-cutoff audit on hash-frozen code.

This executes the sampler and explores each positive abstract random choice.
It checks exact probabilities rather than estimating a distribution by draws.
The tiny reference enumerates literal words independently.
"""
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations,product
import json
from pathlib import Path
import sys
from types import ModuleType
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]


VERSION=3


def load_snapshot():
    manifest=json.loads((HERE/f'review-input-v{VERSION}-manifest.json').read_text())
    snapshot=HERE/f'review-input-v{VERSION}/sampler-v{VERSION}.py'
    source=snapshot.read_bytes()
    assert hashlib.sha256(source).hexdigest()==manifest['files'][f'sampler-v{VERSION}.py']
    module=ModuleType(f'r4_review_frozen_sampler_v{VERSION}')
    # Its fixed repository-root calculation intentionally sees the ORIGINAL
    # filename. The code bytes always come from the preserved review snapshot.
    module.__file__=str(ROOT/f'experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler-v{VERSION}.py')
    sys.modules[module.__name__]=module
    exec(compile(source,module.__file__,'exec'),module.__dict__)
    return module,manifest['files'][f'sampler-v{VERSION}.py']


class NeedChoice(Exception):
    def __init__(self,options):
        self.options=options


class Tape:
    def __init__(self,indices):
        self.indices=indices
        self.position=0

    def choose(self,options):
        options=[(item,Fraction(p)) for item,p in options if p]
        assert sum(p for _,p in options)==1
        if len(options)==1:
            return options[0][0]
        if self.position==len(self.indices):
            raise NeedChoice(options)
        index=self.indices[self.position]
        self.position+=1
        return options[index][0]

    def weighted(self,rng,values,weights):
        values=list(values)
        weights=list(weights)
        return self.choose([(v,Fraction(w,sum(weights))) for v,w in zip(values,weights)])

    def uniform(self,rng,bound):
        return self.choose([(i,Fraction(1,bound)) for i in range(bound)])


def evaluate(n,word):
    p=list(range(n))
    for a,b in word:
        p[a],p[b]=p[b],p[a]
    return tuple(p)


def components(n,word):
    sets=[{i} for i in range(n)]
    for a,b in word:
        hit=[block for block in sets if a in block or b in block]
        sets=[block for block in sets if block not in hit]+[set.union(*hit)]
    return sorted((tuple(sorted(block)),sum(a in block for a,b in word)) for block in sets)


def forward_law(s,n,m,cutoff=None):
    p=s.PreparedSampler(n,m,policy='H1',cutoff_override=cutoff)
    original_weighted,original_uniform=s.g01.weighted_choice,s.g01.randbelow
    original_count,original_sample=s.g01.count,s.g01.sample
    def forbidden(*args,**kwargs):
        raise AssertionError('H1 called an imported g01 formula or sampler')
    s.g01.count=s.g01.sample=forbidden
    todo=[((),Fraction(1))]
    law=Counter()
    paths=0
    try:
        while todo:
            indices,prob=todo.pop()
            tape=Tape(indices)
            s.g01.weighted_choice=tape.weighted
            s.g01.randbelow=tape.uniform
            try:
                draw=p.sample(object())
            except NeedChoice as branch:
                todo.extend((indices+(i,),prob*weight) for i,(_,weight) in enumerate(branch.options))
                continue
            assert tape.position==len(indices)
            law[draw.word]+=prob
            paths+=1
    finally:
        s.g01.weighted_choice,s.g01.randbelow=original_weighted,original_uniform
        s.g01.count,s.g01.sample=original_count,original_sample
    expected=set()
    all_count=0
    for word in product(tuple(combinations(range(n),2)),repeat=m):
        if evaluate(n,word)!=tuple(range(n)):
            continue
        all_count+=1
        if all(len(block)<=p.cutoff for block,ell in components(n,word)):
            expected.add(word)
    assert set(law)==expected
    assert len(expected)==p.A[n][m]
    assert all_count==p.Z[n][m]
    assert set(law.values())=={Fraction(1,len(expected))}
    assert sum(law.values())==1
    return {'policy':'H1','N':n,'m':m,'cutoff':p.cutoff,'override':cutoff,
            'actual_forward_paths':paths,'words':len(law),'total_words':all_count,
            'probability':str(Fraction(1,len(law))),
            'global_tv':str(p.global_tv),'g01_formula_calls_forbidden':True,
            'law_digest':hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest(),'passed':True}


def frozen_cutoff_path(s,policy):
    p=s.PreparedSampler(42,12,policy=policy)
    assert p.cutoff==5 and s.top_level_cutoff(5,12)==4
    probability=Fraction(1)
    assembly=[]
    original_weighted,original_uniform=s.g01.weighted_choice,s.g01.randbelow
    def weighted(rng,values,weights):
        nonlocal probability
        values,weights=list(values),list(weights)
        # Assembly values are pairs, marked transition values are integers.
        if values and isinstance(values[0],tuple):
            wanted=(1,0) if len(assembly)<37 else (5,12)
            i=values.index(wanted)
            assembly.append(wanted)
        else:
            i=next(i for i,w in enumerate(weights) if w)
        probability*=Fraction(weights[i],sum(weights))
        return values[i]
    def uniform(rng,bound):
        nonlocal probability
        probability/=bound
        return 0
    s.g01.weighted_choice,s.g01.randbelow=weighted,uniform
    try:
        draw=p.sample(object())
    finally:
        s.g01.weighted_choice,s.g01.randbelow=original_weighted,original_uniform
    assert assembly==[(1,0)]*37+[(5,12)]
    assert evaluate(42,draw.word)==tuple(range(42))
    assert components(42,draw.word)[-1]==((37,38,39,40,41),12)
    assert probability==Fraction(1,p.A[42][12])
    return {'policy':policy,'top':[42,12,5],'residual':[5,12,4],
            'actual_assembly':assembly,'word':draw.word,'per_word_probability':str(probability),
            'A':p.A[42][12],'passed':True}


def main():
    start=time.monotonic()
    s,digest=load_snapshot()
    rows=[forward_law(s,n,m,k) for n,m,k in [(4,6,None),(4,4,2),(4,6,2),(3,8,None)]]
    fixed=[frozen_cutoff_path(s,policy) for policy in ['H0','H1']]
    long=s.MarkedCounter(2)
    word=long.sample(1400)
    assert len(word)==1400 and set(word)=={(0,1)}
    result={'version':'R4-FORWARD.v1','reviewed_sampler_version':VERSION,'sampler_sha256':digest,
            'target':'exact restricted H0/H1 laws; no asymptotic assertion',
            'law_cases':rows,'frozen_cutoff_actual_paths':fixed,
            'long_stack':{'v':2,'ell':1400,'count':long.connected_count(1400),
                          'cache_states':len(long.cache),'passed':True},
            'seconds':time.monotonic()-start,'passed':True}
    (HERE/'review-forward-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
