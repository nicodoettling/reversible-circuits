#!/usr/bin/env python3
"""Fresh nonauthor checks of the frozen positive-DP and explicit-stack code."""
from collections import defaultdict
import importlib.util
from itertools import combinations, permutations, product
import json
from math import comb, prod
from pathlib import Path
import platform
import random
import sys
import time

import check as independent

ROLE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r3_frozen_r1_sampler',ROLE/'candidate-review-input/sampler.py')
s=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=s
spec.loader.exec_module(s)


def literal_moments(alpha):
    e,ss=[0]*(len(alpha)+1),[0]*(len(alpha)+1)
    for mask in product((False,True),repeat=len(alpha)):
        chosen=tuple(a for a,on in zip(alpha,mask) if on)
        p=prod(chosen)
        e[len(chosen)]+=p
        ss[len(chosen)]+=p*sum(chosen)
    q=sum(a*(a-1) for a in alpha)
    return e,ss,q


def check_moments():
    profiles=table_cases=mass_cases=0
    for total in range(2,9):
        for first in range(1,total):
            for second in range(1,total-first+1):
                for rest in independent.partition_profiles(total-first-second):
                    lengths=(first,second)+rest
                    profiles+=1
                    allocations=[(0,1)+tail for tail in product((0,1),repeat=len(rest))]
                    prepared={}
                    for assignment in allocations:
                        for side in (0,1):
                            alpha=tuple(a for a,j in zip(lengths,assignment) if j==side)
                            prepared[assignment,side]=(sum(alpha),len(alpha),literal_moments(alpha))
                    for partial in product((-1,0,1),repeat=len(rest)):
                        forced={0:0,1:1}|{i+2:j for i,j in enumerate(partial) if j!=-1}
                        matching=[a for a in allocations if all(a[i]==j for i,j in forced.items())]
                        for side in (0,1):
                            expected={}
                            for assignment in matching:
                                size,number,(ee,ss,qq)=prepared[assignment,side]
                                e0,s0,q0=expected.setdefault((size,number),([0]*(number+1),[0]*(number+1),0))
                                for j in range(number+1):
                                    e0[j]+=ee[j];s0[j]+=ss[j]
                                expected[size,number]=(e0,s0,q0+qq)
                            actual=s.allocation_table(lengths,forced,side)
                            assert actual==expected,(lengths,forced,side,actual,expected)
                            table_cases+=1
                        left=tuple(a for i,a in enumerate(lengths) if forced.get(i)==0)
                        right=tuple(a for i,a in enumerate(lengths) if forced.get(i)==1)
                        free=tuple(a for i,a in enumerate(lengths) if i not in forced)
                        for ga,gb in ((0,0),(0,1),(1,0)):
                            actual=s.allocation_mass(lengths,ga,gb,forced)
                            expected=independent.allocation_mass(left,right,free,ga,gb)
                            assert actual==expected,(lengths,forced,ga,gb,actual,expected)
                            mass_cases+=1
    count_cases=0
    for n in range(1,19):
        for alpha in independent.partition_profiles(n):
            for g in (0,1):
                assert s.count(alpha,g)==independent.connected_count(alpha,g)
                count_cases+=1
    return {'maximum_moment_degree':8,'oriented_cycle_profiles':profiles,'exact_full_moment_tables':table_cases,'forced_mass_queries_vs_blind_oracle':mass_cases,'count_formula_profiles_through':18,'count_formula_queries':count_cases}


def subset_rank(n,k,positions):
    positions=set(positions)
    rank=0
    for i in range(n):
        if k==0:
            break
        if i in positions:
            k-=1
        else:
            rank+=comb(n-i-1,k-1)
    assert k==0
    return rank


def trace_for_word(p,g,word,upper):
    """Plan exact randbelow values by the target word's unique decomposition."""
    n=len(p)
    if not word:
        assert n==1 and g==0
        return []
    edge,prefix=word[-1],word[:-1]
    rho=independent.right_t(p,edge)
    part=tuple(range(n))
    for e in prefix:
        part=independent.union(part,*e)
    candidates=s.branches(p,g)
    if len(set(part))==1:
        childg=(len(prefix)-n-len(independent.cycles(rho))+2)//2
        branch=next(b for b in candidates if b.edge==edge and b.kind=='connected' and b.child_genus==childg)
    else:
        aa=tuple(i for i in range(n) if part[i]==part[edge[0]])
        bb=tuple(i for i in range(n) if part[i]==part[edge[1]])
        pa,ma=independent.restrict_permutation(rho,aa)
        pb,mb=independent.restrict_permutation(rho,bb)
        ia,ib={a:i for i,a in enumerate(ma)},{a:i for i,a in enumerate(mb)}
        wa=tuple(tuple(ia[a] for a in e) for e in prefix if e[0] in ia)
        wb=tuple(tuple(ib[a] for a in e) for e in prefix if e[0] in ib)
        ga=(len(wa)-len(aa)-len(independent.cycles(pa))+2)//2
        gb=(len(wb)-len(bb)-len(independent.cycles(pb))+2)//2
        branch=next(b for b in candidates if b.edge==edge and b.kind=='split' and b.ga==ga and b.gb==gb)
    offset=sum(b.weight for b in candidates[:candidates.index(branch)])
    total=sum(b.weight for b in candidates)
    tape=[(total,offset+(branch.weight-1 if upper else 0))]
    if branch.kind=='connected':
        return tape+trace_for_word(rho,childg,prefix,upper)
    lengths=tuple(map(len,branch.cut_cycles))
    forced={0:0,1:1}
    for i in range(2,len(lengths)):
        a=s.allocation_mass(lengths,ga,gb,forced|{i:0})
        b=s.allocation_mass(lengths,ga,gb,forced|{i:1})
        selected_side=int(branch.cut_cycles[i][0] not in ia)
        selected=(a,b)[selected_side]
        assert selected>0
        rank=(a if selected_side else 0)+(selected-1 if upper else 0)
        tape.append((a+b,rank))
        forced[i]=selected_side
    tape+=trace_for_word(pa,ga,wa,upper)
    tape+=trace_for_word(pb,gb,wb,upper)
    positions=tuple(i for i,e in enumerate(prefix) if e[0] in ia)
    tape.append((comb(len(prefix),len(wa)),subset_rank(len(prefix),len(wa),positions)))
    return tape


class ExactTape:
    def __init__(self,tape):
        self.tape=tape;self.position=0
    def getrandbits(self,width):
        bound,value=self.tape[self.position]
        self.position+=1
        assert width==(bound-1).bit_length()
        assert 0<=value<bound
        return value


def replay(p,g,word,upper):
    tape=ExactTape(trace_for_word(p,g,word,upper))
    got=s.sample(p,g,tape)
    assert got==word,(p,g,word,got)
    assert tape.position==len(tape.tape)
    return tape.position


def check_replays():
    literal=replays=draws=0
    n=3;edges=tuple(combinations(range(n),2))
    for length in range(1,7):
        for word in product(edges,repeat=length):
            p,part=tuple(range(n)),tuple(range(n))
            for e in word:
                p,part=independent.right_t(p,e),independent.union(part,*e)
            g2=length-n-len(independent.cycles(p))+2
            if len(set(part))!=1 or g2 not in (0,2):
                continue
            literal+=1
            for upper in (False,True):
                draws+=replay(p,g2//2,word,upper);replays+=1
    generated=0
    for seed in (17,101,20260907):
        rng=random.Random(seed)
        for p in permutations(range(4)):
            for genus in (0,1):
                word=independent.sampler(p,genus,rng)
                for upper in (False,True):
                    draws+=replay(p,genus,word,upper);replays+=1
                generated+=1
        for n in (5,6,8,12):
            p=list(range(n));rng.shuffle(p);p=tuple(p)
            for genus in (0,1):
                word=independent.sampler(p,genus,rng)
                draws+=replay(p,genus,word,False);replays+=1;generated+=1
    return {'all_s3_literal_family_words':literal,'generated_targets_from_blind_sampler':generated,'actual_sampler_replays':replays,'integer_draw_calls_replayed':draws,'branch_interval_endpoints':'both first and last for all S3 words and S4 generated targets','diagnostic_seeds':[17,101,20260907]}


def check_deep_stack():
    """Mechanical depth test with declared deterministic oracles, not a sampler benchmark."""
    original_count,original_branches,original_assignment=s.count,s.branches,s.sample_assignment
    statistics={'fake_branch_calls':0,'maximum_sample_frames':0,'maximum_pending_tasks':0}
    def fixture_branches(p,g):
        statistics['fake_branch_calls']+=1
        n=len(p);identity=tuple(range(n))
        if g==1:
            edge=(0,1);q=independent.right_t(p,edge)
            child=1 if p==identity else 0
            return (s.Branch(edge,q,'connected',child,-1,-1,(),1),)
        edge=(0,n-1)
        if p==identity:
            return (s.Branch(edge,independent.right_t(p,edge),'connected',0,-1,-1,(),1),)
        assert p==independent.right_t(identity,edge)
        cut=((0,),(n-1,))+tuple((i,) for i in range(1,n-1))
        return (s.Branch(edge,identity,'split',-1,0,0,cut,1),)
    class ZeroBits:
        def getrandbits(self,width):
            assert width==0
            f=sys._getframe();frames=0
            while f:
                if f.f_code is s.sample.__code__:
                    frames+=1
                    statistics['maximum_pending_tasks']=max(statistics['maximum_pending_tasks'],len(f.f_locals['tasks']))
                f=f.f_back
            statistics['maximum_sample_frames']=max(statistics['maximum_sample_frames'],frames)
            return 0
    try:
        s.count=lambda alpha,genus:1
        s.branches=fixture_branches
        s.sample_assignment=lambda lengths,ga,gb,rng:(0,1)+(0,)*(len(lengths)-2)
        n=600
        word=s.sample(tuple(range(n)),1,ZeroBits())
        expected=tuple(e for j in range(1,n) for e in ((0,j),(0,j)))+((0,1),(0,1))
        assert word==expected and len(word)==1200
        assert statistics['fake_branch_calls']==1200
        assert statistics['maximum_sample_frames']==1
    finally:
        s.count,s.branches,s.sample_assignment=original_count,original_branches,original_assignment
    return {'fixture_degree':600,'output_length':1200,'scope':'explicit-stack mechanics only; count, branch and assignment oracles stubbed deterministically',**statistics}


def main():
    start=time.monotonic()
    result={'python':platform.python_version(),'nonstandard_dependencies':[],'moments':check_moments(),'actual_stack_replays':check_replays(),'deep_stack':check_deep_stack(),'result':'pass','seconds':time.monotonic()-start}
    ROLE.joinpath('candidate-check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
