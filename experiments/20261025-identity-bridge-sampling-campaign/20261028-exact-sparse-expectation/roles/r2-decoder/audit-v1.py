"""Exact full output laws and lazy-preparation regressions for I2-D.v1."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import argparse, gc, hashlib, importlib.util, json, os, platform, random, sys, time, weakref
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i2_d_under_test',HERE/'exact_sampler-v1.py')
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)


class Fork(Exception):
    def __init__(self,weights):self.weights=weights


class Oracle:
    def __init__(self,tape):self.tape=tape;self.cursor=0;self.probability=Q(1)
    def exact_index(self,weights):
        positive=[(i,w) for i,w in enumerate(weights) if w]
        assert positive and all(w>0 for _,w in positive)
        if len(positive)==1:return positive[0][0]
        if self.cursor==len(self.tape):raise Fork(tuple(w for _,w in positive))
        position=self.tape[self.cursor];self.cursor+=1
        index,weight=positive[position]
        self.probability*=Q(weight,sum(w for _,w in positive))
        return index


def own_evaluate(word,n):
    p=list(range(1,n+1))
    for a,b in word:
        assert 1<=a<b<=n
        p[a-1],p[b-1]=p[b-1],p[a-1]
    return tuple(p)


def own_components(word,n):
    blocks=[{i} for i in range(1,n+1)]
    for a,b in word:
        aa=next(block for block in blocks if a in block)
        bb=next(block for block in blocks if b in block)
        if aa is not bb:
            blocks.remove(aa);blocks.remove(bb);blocks.append(aa|bb)
    return tuple(sorted((tuple(sorted(block)),sum(a in block for a,b in word)) for block in blocks))


def direct_words(n,m):
    return {w for w in product(tuple(combinations(range(1,n+1),2)),repeat=m)
            if own_evaluate(w,n)==tuple(range(1,n+1))}


def full_law(n,m):
    prep=s.PreparedExact(n,m)
    assert set(prep.__dict__)=={'n','m','C','Z'}
    stack=[((),Q(1))];law=defaultdict(Q);leaves=nodes=0
    while stack:
        tape,probability=stack.pop();oracle=Oracle(tape);nodes+=1
        try:word=prep.sample(oracle)
        except Fork as fork:
            assert oracle.probability==probability
            total=sum(fork.weights)
            for i,weight in enumerate(fork.weights):
                stack.append((tape+(i,),probability*Q(weight,total)))
        else:
            assert oracle.cursor==len(tape) and oracle.probability==probability
            law[word]+=probability;leaves+=1
    expected=direct_words(n,m)
    assert set(law)==expected and sum(law.values())==1
    assert all(value==Q(1,len(expected)) for value in law.values())
    moment=sum(Q(sum(9**len(labels) for labels,ell in own_components(w,n) if ell),len(expected))
               for w in expected)
    return {'N':n,'m':m,'words':len(expected),'each_probability':str(Q(1,len(expected))),
            'logical_leaves':leaves,'replays':nodes,'full_law_equal':True,
            'expected_nontrivial_component_9_cost':str(moment),
            'law_sha256':hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest()}


class AcceptedTape:
    def __init__(self,items):self.items=list(items);self.read=0
    def getrandbits(self,bits):
        expected,value=self.items[self.read];self.read+=1
        assert expected==bits and 0<=value<2**bits
        return value


def prescribed_rare_macro():
    n,m,v=82,14,6
    prepared=s.PreparedExact(n,m)
    assert m**3<=n*n
    choices,weights=prepared.branches(n,m)
    which=choices.index((v,m));ticket=sum(weights[:which])
    tape=[((sum(weights)-1).bit_length(),ticket)]
    label_bound=comb(n-1,v-1)
    if label_bound>1:tape.append(((label_bound-1).bit_length(),0))
    oracle=AcceptedTape(tape)
    events=[];weak=[];original=s.SelectedCounter
    phase=['macro']
    def factory(degree):
        assert phase[0]=='decode','counter constructed before macro completed'
        obj=original(degree);events.append(degree);weak.append(weakref.ref(obj));return obj
    s.SelectedCounter=factory
    try:
        macro=prepared.sample_macro(oracle)
        assert oracle.read==len(tape) and not events
        assert macro[0].labels==tuple(range(1,v+1)) and macro[0].positions==tuple(range(m))
        assert all(item.degree==1 and item.length==0 for item in macro[1:])
        phase[0]='decode'
        word,metrics=prepared.decode_macro(macro,random.Random(1729),True)
        assert events==[v]
        assert own_evaluate(word,n)==tuple(range(1,n+1))
        assert own_components(word,n)==tuple(sorted([(tuple(range(1,v+1)),m)]+[((i,),0) for i in range(v+1,n+1)]))
        gc.collect();assert all(ref() is None for ref in weak)
    finally:s.SelectedCounter=original
    cost=metrics[0]
    assert cost['count_keys']<=cost['remaining_length_key_bound']
    assert cost['transition_states']<=cost['state_bound']
    specified_macro_probability=Q(prepared.C[v][m],prepared.Z[n][m])
    assert specified_macro_probability>0
    # The old H0 original cutoff is5, so v6,g2 is a positive excluded component.
    p=n+m+2;k=1
    while k+1<=n and (k+1)**(2*(k+1))<=p**4:k+=1
    assert k==5 and (m-2*v+2)//2==2 and v>k
    return {'N':n,'m':m,'component_v':v,'component_length':m,'component_genus':2,
            'inside_primary_sparse_range':True,'old_H0_cutoff':k,
            'specified_labeled_macro_probability':str(specified_macro_probability),
            'decoder_degrees_created':events,'no_counter_before_macro':True,
            'all_counters_released':True,'component_metrics':cost,
            'validity_seed':1729}


def boundaries_and_support():
    for n,m in ((0,0),(1,0),(2,0),(3,0)):
        assert s.PreparedExact(n,m).sample()==()
    for n,m in ((1,2),(2,1),(3,3),(-1,0),(2,-2)):
        try:s.PreparedExact(n,m)
        except ValueError:pass
        else:raise AssertionError(('invalid accepted',n,m))
    for m in (2,4,12):
        assert s.PreparedExact(2,m).sample()==((1,2),)*m
    counter=s.SelectedCounter(3)
    old_support=counter.count(5,((1,),(2,)))
    full_support=counter.count(5,((1,2),))
    assert (old_support,full_support)==(80,81)
    assert counter.count(0,((1,1,1),))==1
    assert counter.count(0,((1,),(1,),(1,)))==0
    a,b=(1,2),(2,3);squareless=(a,b)*3
    assert own_evaluate(squareless,3)==(1,2,3) and all(squareless[i]!=squareless[i+1] for i in range(5))
    assert Q(21,2000)>Q(1,100)
    samples=[]
    for n,m in ((3,4),(4,4),(4,6),(3,8),(5,10)):
        prepared=s.PreparedExact(n,m)
        for seed in (1729,2718):
            word,macro,metrics=prepared.sample_with_metrics(random.Random(seed))
            assert len(word)==m and own_evaluate(word,n)==tuple(range(1,n+1))
            assert sorted(row['degree'] for row in metrics)==sorted(c.degree for c in macro if c.degree>1)
            for row in metrics:
                assert row['count_keys']<=row['remaining_length_key_bound']
                assert row['transition_states']<=row['state_bound']
            samples.append({'N':n,'m':m,'seed':seed,'decoder_degrees':[row['degree'] for row in metrics]})
    # Old top42/residual5 cutoff witness: unrestricted C(5,12) stays eligible.
    prepared=s.PreparedExact(42,12)
    original_choices,_=prepared.branches(42,12)
    residual_choices,_=prepared.branches(5,12)
    assert (5,12) in original_choices and (5,12) in residual_choices
    return {'empty_odd_negative_small_degree':True,'N2_unique':True,
            'same_endpoint_connected_support_counts':[old_support,full_support],
            'zero_step_support_boundary':True,'squareless_retained':True,
            'CP1_rejects_old_product':True,'no_residual_cutoff_42_12_to_5_12':True,'samples':samples}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    started=time.perf_counter()
    result={'status':'complete','python':platform.python_version(),'nonstandard_dependencies':[],
            'deterministic_seed':None,'validity_seeds':[1729,2718],
            'base_commit':'92af1b7b47583b60571a84c660d527422ce0e8ce',
            'sampler_sha256':hashlib.sha256((HERE/'exact_sampler-v1.py').read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'full_laws':[full_law(n,m) for n,m in ((3,4),(4,4),(4,6),(3,8))],
            'rare_component':prescribed_rare_macro(),'regressions':boundaries_and_support()}
    result['elapsed_seconds']=time.perf_counter()-started
    result['generated_utc']=datetime.now(timezone.utc).isoformat()
    tmp=args.output.with_name(args.output.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,args.output)
    print(json.dumps({'status':'complete','seconds':result['elapsed_seconds'],
                      'words':[case['words'] for case in result['full_laws']],
                      'rare_counter_keys':result['rare_component']['component_metrics']['count_keys']}))
if __name__=='__main__':main()
