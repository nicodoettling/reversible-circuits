#!/usr/bin/env python3
"""Exhaust actual sampler choice paths with exact rational weights.

Replays the production H0 v3 implementation, replacing ONLY exact discrete
random choices by exhaustive branches. This validates forward reconstruction,
labels/positions, and internal component decoding together. Fair-bit rejection
correctness is proved separately; fixed PRNG seeds are not used here.
"""
from collections import defaultdict
from fractions import Fraction
import hashlib, json, platform, sys, time
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT/'roles/r3-sampler/sampler-v3.py'
EXPECTED = '56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06'
payload=SOURCE.read_bytes()
assert hashlib.sha256(payload).hexdigest()==EXPECTED
s=ModuleType('coordinator_h0_forward'); s.__file__=str(SOURCE)
sys.modules[s.__name__]=s
exec(compile(payload,str(SOURCE),'exec'),s.__dict__)

class Branch(Exception):
    def __init__(self, weights): self.weights=weights

class Tape:
    def __init__(self,tape): self.tape=tape; self.pos=0
    def choose(self,weights):
        weights=tuple(weights)
        positive=[i for i,w in enumerate(weights) if w]
        assert positive and all(w>=0 for w in weights)
        if len(positive)==1:return positive[0]
        if self.pos==len(self.tape):raise Branch(weights)
        i=self.tape[self.pos]; self.pos+=1
        assert weights[i]>0
        return i

def case(n,m,cutoff=None):
    start=time.monotonic(); prepared=s.PreparedSampler(n,m,cutoff_override=cutoff)
    frontier=[((),Fraction(1))]; law=defaultdict(Fraction); paths=0
    while frontier:
        history,probability=frontier.pop(); tape=Tape(history)
        def weighted(rng,values,weights):
            values=tuple(values); return values[tape.choose(weights)]
        def below(rng,bound):
            assert bound>0; return tape.choose((1,)*bound)
        s.g01.weighted_choice=weighted; s.g01.randbelow=below
        try:result=prepared.sample(object())
        except Branch as event:
            total=sum(event.weights)
            for i,w in enumerate(event.weights):
                if w:frontier.append((history+(i,),probability*Fraction(w,total)))
        else:
            assert tape.pos==len(history)
            assert s.g01.evaluate(n,result.word)==tuple(range(n))
            assert len(result.word)==m
            law[result.word]+=probability; paths+=1
    count=prepared.A[n][m]
    assert len(law)==count
    assert set(law.values())=={Fraction(1,count)}
    assert sum(law.values())==1
    return dict(N=n,m=m,cutoff=prepared.cutoff,candidate=prepared.candidate,paths=paths,words=len(law),total=prepared.Z[n][m],
                allowed=count,probability=str(Fraction(1,count)),passed=True,
                law_sha256=hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest(),
                seconds=time.monotonic()-start)

def main():
    cases=[(3,4,None),(4,4,None),(4,6,None),(3,6,None),(3,8,None),(4,8,None),(3,8,2)]
    rows=[]
    for n,m,cutoff in cases:
        row=case(n,m,cutoff); rows.append(row);print(json.dumps(row),flush=True)
    output=ROOT/'coordinator_forward_results.json'
    output.write_text(json.dumps(dict(source_sha256=EXPECTED,python=platform.python_version(),
                      seed=None,command=sys.argv,cases=rows),indent=2)+'\n')

if __name__=='__main__':main()
