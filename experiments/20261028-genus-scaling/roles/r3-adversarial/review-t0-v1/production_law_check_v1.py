#!/usr/bin/env python3
"""NONBLIND fresh check: intercept actual production categorical execution."""
import argparse, collections, hashlib, importlib.util, itertools, json, math, platform, sys, time
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module

I=load('r3_integrated_under_review',ROOT/'coordinator/integrated_sampler_v1.py')
REF=load('r3_frozen_blind_reference',HERE.parent/'check_blind_v1.py')

class NextChoice(Exception):
    def __init__(self,kind,weights): self.kind=kind; self.weights=tuple(weights)

class Replay:
    def __init__(self,tape): self.tape=tape; self.cursor=0; self.calls=0
    def choose(self,kind,weights):
        self.calls+=1
        assert all(isinstance(w,int) and w>=0 for w in weights) and sum(weights)>0
        positive=[i for i,w in enumerate(weights) if w]
        if len(positive)==1:return positive[0]
        if self.cursor==len(self.tape):raise NextChoice(kind,weights)
        old_kind,old_weights,chosen=self.tape[self.cursor];self.cursor+=1
        assert old_kind==kind and old_weights==tuple(weights) and weights[chosen]>0
        return chosen


def whole_law(endpoint,genus,reference_count):
    decoder=I.decoder; oldwc=decoder.weighted_choice; oldrb=decoder.randbelow
    pending=[((),Fraction(1))]; law=collections.defaultdict(Fraction)
    runs=0; branchpoints=0; call_count=0; max_frontier=1
    try:
        while pending:
            tape,mass=pending.pop(); replay=Replay(tape);runs+=1
            def wc(rng,values,weights):return values[replay.choose('weighted',tuple(weights))]
            def rb(rng,bound):return replay.choose('interleaving', (1,)*bound)
            decoder.weighted_choice=wc;decoder.randbelow=rb
            try:
                word=I.sample_endpoint(endpoint,genus,object())
                assert replay.cursor==len(tape)
                law[word]+=mass
            except NextChoice as node:
                branchpoints+=1; total=sum(node.weights)
                for i,w in enumerate(node.weights):
                    if w:pending.append((tape+((node.kind,node.weights,i),),mass*Fraction(w,total)))
                max_frontier=max(max_frontier,len(pending))
            call_count+=replay.calls
    finally:
        decoder.weighted_choice=oldwc;decoder.randbelow=oldrb
    assert len(law)==reference_count,(endpoint,genus,len(law),reference_count)
    target=Fraction(1,reference_count)
    for word,mass in law.items():
        assert mass==target,(endpoint,genus,word,mass,target)
        assert len(word)==len(endpoint)+len(REF.cycle_type(endpoint))-2+2*genus
        p=list(range(len(endpoint)));blocks=list(range(len(endpoint)))
        for x,y in word:
            p[x],p[y]=p[y],p[x]
            small=min(blocks[x],blocks[y]);large=max(blocks[x],blocks[y]);blocks=[small if z==large else z for z in blocks]
        assert tuple(p)==endpoint and len(set(blocks))==1
    return {'endpoint':endpoint,'genus':genus,'word_count':len(law),'probability':[target.numerator,target.denominator],'replayed_runs':runs,'categorical_branchpoints':branchpoints,'intercepted_calls':call_count,'maximum_DFS_frontier':max_frontier,'exact_uniform':True}


def allocation_checks(connected):
    results=[]
    cases=[(1,1,2,2),(1,2,1,3),(2,2,1,1,1)]
    pairs=[(1,2),(2,1),(1,3),(3,1),(2,2)]
    for sizes in cases:
        k=len(sizes)
        for ga,gb in pairs:
            weights={}
            for assignment in itertools.product((0,1),repeat=k-2):
                assignment=(0,1)+assignment
                A=tuple(sorted(a for a,s in zip(sizes,assignment) if s==0));B=tuple(sorted(a for a,s in zip(sizes,assignment) if s==1))
                la=sum(A)+len(A)-2+2*ga;lb=sum(B)+len(B)-2+2*gb
                weights[assignment]=math.comb(la+lb,la)*connected[sum(A)][A][la]*connected[sum(B)][B][lb]
            for forcing in itertools.product((-1,0,1),repeat=k-2):
                H={0:0,1:1}|{i+2:v for i,v in enumerate(forcing) if v>=0}
                expected=sum(w for a,w in weights.items() if all(a[i]==side for i,side in H.items()))
                actual=I.decoder.allocation_mass(sizes,ga,gb,H)
                assert actual==expected,(sizes,ga,gb,H,actual,expected)
                results.append({'sizes':sizes,'ga':ga,'gb':gb,'forcing':sorted(H.items()),'count':actual})
    return results


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic(); assert sorted(I.decoder.SPECS)==[0,1]
    I.prepare(3)
    states={n:REF.connected_state_dp(n,12) for n in (2,3,4)}
    cases=[((0,1),3),((0,1,2),0),((0,1,2),1),((0,1,2),2),((0,1,2),3),((1,0,2),2),((1,2,0),3),((1,0,3,2),1),((1,2,3,0),2)]
    laws=[]
    for endpoint,g in cases:
        length=len(endpoint)+len(REF.cycle_type(endpoint))-2+2*g
        laws.append(whole_law(endpoint,g,states[len(endpoint)][length][endpoint]))
    _,connected=REF.tables(8,26)
    allocations=allocation_checks(connected)
    sources=[Path(I.__file__),Path(I.coefficient.__file__),Path(I.decoder.__file__),Path(REF.__file__),Path(__file__)]
    result={'status':'pass','phase':'NONBLIND exact-version review','python':platform.python_version(),'dependencies':'stdlib only','seed':0,'deterministic':True,'source_commit_at_blind_intake':'b178daf320833e859dcdee0ce56eb16c6d2130b7','source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'law_method':'Replay actual sample_endpoint/sample/sample_assignment/stack/relabel/unrank/interleave; intercept only exact categorical primitive and interleaving randbelow, contracting fair-bit rejection by its proved uniform law. No alternate word decoder.','laws':laws,'allocation_checks':allocations,'limits':['finite checks do not prove asymptotic theorem','no all-N4g3 word enumeration','actual fair-bit retry loops contracted, not enumerated'],'elapsed_seconds':time.monotonic()-start}
    out=Path(args.output);tmp=out.with_suffix(out.suffix+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
    print(json.dumps({'status':'pass','laws':len(laws),'words':sum(x['word_count'] for x in laws),'forcing_cases':len(allocations),'seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
