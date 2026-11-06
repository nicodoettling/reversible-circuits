"""Exact rational falsification for candidate R1-T2.v1, standard library only.
Production uses marker compression. References use support-partition walk DP,
literal subsets/words, and forward categorical decision tapes.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, factorial, prod
from pathlib import Path
import hashlib, importlib.util, json, platform, random, subprocess, sys, time
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r1_genus2',HERE/'sampler-v1.py')
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)

def canonical_partition(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))

def join_partition(part,a,b):
    aa=next(i for i,c in enumerate(part) if a in c)
    bb=next(i for i,c in enumerate(part) if b in c)
    if aa==bb:return part
    return canonical_partition([c for i,c in enumerate(part) if i not in (aa,bb)]+[part[aa]+part[bb]])

def support_reference(n,max_length):
    identity=tuple(range(n));initial=tuple((i,) for i in range(n))
    states={(identity,initial):1};layers=[];max_states=0
    for length in range(max_length+1):
        all_counts=defaultdict(int);connected=defaultdict(int)
        for (p,part),value in states.items():
            all_counts[p]+=value
            if len(part)==1:connected[p]+=value
        layers.append((dict(all_counts),dict(connected)))
        max_states=max(max_states,len(states))
        nxt=defaultdict(int)
        for (p,part),value in states.items():
            for a,b in combinations(range(n),2):
                q=list(p);q[a],q[b]=q[b],q[a]
                nxt[(tuple(q),join_partition(part,a,b))]+=value
        states=nxt
    return layers,max_states

def literal_marker(parts,spec):
    # Direct special-slot injections followed by ordinary subsets.
    d=len(spec[0]);ans=defaultdict(int)
    for slots in permutations(range(len(parts)),d):
        special=prod(s.special_weight(name,parts[i]) for name,i in zip(spec[0],slots))
        unused=[i for i in range(len(parts)) if i not in slots]
        jrange=range(len(unused)+1) if s.ordinary_allowed(spec) else (0,)
        for j in jrange:
            for ordinary in combinations(unused,j):
                ans[(j,(1<<d)-1)]+=special*prod(parts[i] for i in ordinary)
    return {k:v for k,v in ans.items() if v}

def ref_count_by_subsets(parts,g):
    n,k=sum(parts),len(parts)
    qprod=prod(Q(a**a,factorial(a-1)) for a in parts)
    total=Q(0)
    for spec in s.SPECS[g]:
        for (j,_),value in literal_marker(parts,spec).items():
            total+=value*s.coefficient(spec,n,k,j)
    ans=factorial(n+k-2+2*g)*qprod*total
    assert ans.denominator==1
    return ans.numerator

def allocation_audit():
    rows=[]
    inventories=((1,1),(1,1,1),(1,1,1,1),(2,1,2,1),(3,2,1,1,2),(1,4,2,1,3,1))
    genus_pairs=((0,0),(0,1),(1,0),(0,2),(1,1),(2,0))
    for lengths in inventories:
        assignments=[(0,1)+x for x in product((0,1),repeat=len(lengths)-2)]
        direct={}
        for ass in assignments:
            aa=tuple(a for a,side in zip(lengths,ass) if side==0)
            bb=tuple(a for a,side in zip(lengths,ass) if side==1)
            for ga,gb in genus_pairs:
                ra=sum(aa)+len(aa)-2+2*ga;rb=sum(bb)+len(bb)-2+2*gb
                direct[ass,ga,gb]=comb(ra+rb,ra)*ref_count_by_subsets(aa,ga)*ref_count_by_subsets(bb,gb)
        queries=zeros=0;digest=hashlib.sha256()
        for partial in product((-1,0,1),repeat=len(lengths)-2):
            forced={0:0,1:1}|{i+2:x for i,x in enumerate(partial) if x!=-1}
            kept=[a for a in assignments if all(a[i]==side for i,side in forced.items())]
            for ga,gb in genus_pairs:
                expected=sum(direct[ass,ga,gb] for ass in kept)
                actual=s.allocation_mass(lengths,ga,gb,forced)
                assert actual==expected,(lengths,forced,ga,gb,actual,expected)
                queries+=1;zeros+=actual==0
                digest.update(repr((partial,ga,gb,actual)).encode())
        rows.append(dict(lengths=lengths,queries=queries,zero_mass_queries=zeros,digest=digest.hexdigest()))
    return rows
class NeedDecision(Exception):
    def __init__(self, weights):
        self.weights = weights


class Oracle:
    def __init__(self, tape):
        self.tape, self.position = tape, 0

    def decide(self, values, weights):
        positive = [(v, w) for v, w in zip(values, weights) if w]
        assert positive and all(w > 0 for _, w in positive)
        if len(positive) == 1:
            return positive[0][0]
        if self.position == len(self.tape):
            raise NeedDecision(tuple(w for _, w in positive))
        index = self.tape[self.position]
        self.position += 1
        return positive[index][0]


def forward_law(call, module, leaf_cap=10000):
    original_choice, original_randbelow = module.weighted_choice, module.randbelow
    todo = [((), Q(1))]
    law = defaultdict(Q)
    leaves = trials = 0
    try:
        while todo:
            tape, probability = todo.pop()
            oracle = Oracle(tape)
            module.weighted_choice = lambda rng, values, weights: oracle.decide(values, weights)
            module.randbelow = lambda rng, bound: oracle.decide(range(bound), (1,) * bound)
            trials += 1
            try:
                word = call()
            except NeedDecision as decision:
                total = sum(decision.weights)
                for i, weight in enumerate(decision.weights):
                    todo.append((tape + (i,), probability * Q(weight, total)))
            else:
                assert oracle.position == len(tape)
                law[tuple(word)] += probability
                leaves += 1
                assert leaves <= leaf_cap
    finally:
        module.weighted_choice, module.randbelow = original_choice, original_randbelow
    assert sum(law.values()) == 1
    return law, dict(logical_leaf_tapes=leaves, implementation_replays=trials,
                     word_count=len(law), all_words_one_logical_tape=leaves == len(law))


def own_eval(word, n):
    p = list(range(n))
    for a, b in word:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def own_components(word, n):
    blocks = [{i} for i in range(n)]
    for a, b in word:
        aa = next(block for block in blocks if a in block)
        bb = next(block for block in blocks if b in block)
        if aa is not bb:
            blocks.remove(aa)
            blocks.remove(bb)
            blocks.append(aa | bb)
    return blocks


def direct_words(n, endpoint, length, connected=True, allowed=False):
    good = set()
    for word in product(tuple(combinations(range(n), 2)), repeat=length):
        if own_eval(word, n) != endpoint:
            continue
        blocks = own_components(word, n)
        if connected and len(blocks) != 1:
            continue
        if allowed:
            for block in blocks:
                ell = sum(a in block for a, _ in word)
                genus = (ell - 2 * len(block) + 2) // 2
                if genus > 1:
                    break
            else:
                good.add(word)
            continue
        good.add(word)
    return good


def run():
    out={"schema_version":1,"claim":"R1-T2.v1 exact counts, allocation and forward law","seed_exact":None,"diagnostic_seeds":[1729,2718],"python":platform.python_version(),"dependencies":"Python standard library only","commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"command":sys.argv,"code_sha256":hashlib.sha256((HERE/'sampler-v1.py').read_bytes()).hexdigest()}
    start=time.monotonic();count_rows=[];refs={}
    for n in range(1,6):
        ref,max_states=support_reference(n,2*n+2);refs[n]=ref;checks=0
        for p in permutations(range(n)):
            alpha=tuple(len(c) for c in s.cycles(p))
            for g in (0,1,2):
                length=n+len(alpha)-2+2*g
                expected=ref[length][1].get(p,0)
                actual=s.count(alpha,g)
                assert actual==expected,(p,g,actual,expected)
                if actual and length>0:
                    assert sum(b.weight for b in s.branches(p,g))==expected
                checks+=1
        count_rows.append(dict(n=n,maximum_support_states=max_states,endpoint_genus_checks=checks))
    out['counts']=count_rows
    out['allocation']=allocation_audit()
    rows=[]
    cases=[(p,g) for p in permutations(range(3)) for g in (0,1,2)]
    cases += [((0,1,2,3),0)]
    for p,g in cases:
        length=len(p)+len(s.cycles(p))-2+2*g
        law,row=forward_law(lambda:s.sample(p,g,object()),s,leaf_cap=10000)
        expected=direct_words(len(p),p,length)
        assert set(law)==expected
        assert all(x==Q(1,len(expected)) for x in law.values())
        row.update(endpoint=p,genus=g,length=length,each_probability=str(Q(1,len(expected))),digest=hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest())
        rows.append(row)
    out['forward_law']=rows
    baseline=[]
    for n,m,expected in ((3,4,27),(4,4,120),(4,6,3936)):
        actual=refs[n][m][0].get(tuple(range(n)),0)
        assert actual==expected;baseline.append(dict(n=n,m=m,global_count=actual))
    assert refs[3][5][0][(1,0,2)]==81 and s.count((2,1),1)==80
    a=(0,1);b=(1,2);squareless=(a,b)*3
    assert own_eval(squareless,3)==(0,1,2) and len(own_components(squareless,3))==1
    assert all(squareless[i]!=squareless[i+1] for i in range(5))
    for n in (1,2,3,4,5,6,8):
        for g in (0,1,2):
            for seed in (1729,2718):
                p=tuple(range(n))
                if n==1 and g:
                    try:s.sample(p,g,random.Random(seed))
                    except ValueError:pass
                    else:raise AssertionError('zero singleton sampled')
                else:
                    word=s.sample(p,g,random.Random(seed))
                    assert own_eval(word,n)==p and len(own_components(word,n))==1
                    assert len(word)==2*n-2+2*g
    for g in (0,1,2):
        assert s.sample((0,1),g,random.Random(1729))==((0,1),)*(2+2*g)
    out['regressions']={"baselines":baseline,"transposition_endpoint_total":81,"connected":80,"squareless_word":squareless,"singleton_zero":True,"N2_unique":True,"seeded_validity":True,"odd_identity_lengths":all(refs[4][m][0].get((0,1,2,3),0)==0 for m in (1,3,5,7,9))}
    out['elapsed_seconds']=time.monotonic()-start
    out['verdict']='all exact finite checks passed; asymptotic proof remains separately reviewable'
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    result=run();path=Path(args.output);temp=path.with_name(path.name+'.tmp');temp.write_text(json.dumps(result,indent=2)+'\n');temp.replace(path)
    print(json.dumps({"output":str(path),"elapsed_seconds":result['elapsed_seconds'],"verdict":result['verdict']}))
