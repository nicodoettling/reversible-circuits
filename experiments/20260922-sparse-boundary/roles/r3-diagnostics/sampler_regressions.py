#!/usr/bin/env python3
"""Preserve required exact sampler regressions on hash-frozen v4 inputs."""
from pathlib import Path
from fractions import Fraction
import json,platform,random,sys,time
import boundary_diagnostics as bd

def main():
    start=time.monotonic()
    s=bd.load('experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler-v4.py','r3_frozen_sampler_v4')
    r=bd.load('experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/review_forward.py','r3_frozen_forward_review')
    law=[r.forward_law(s,n,m,k) for n,m,k in [(3,4,None),(4,4,None),(4,6,None),(3,8,None),(3,8,2)]]
    fixed=[r.frozen_cutoff_path(s,policy) for policy in ['H0','H1']]
    boundary=[]
    for policy in ['H0','H1']:
      for n,m in [(1,0),(2,0),(2,2),(2,12)]:
        prepared=s.PreparedSampler(n,m,policy=policy)
        for seed in [1729,2718,31415]:
          draw=prepared.sample(random.Random(seed));assert len(draw.word)==m
          assert r.evaluate(n,draw.word)==tuple(range(n))
        boundary.append({'policy':policy,'N':n,'m':m,'count':prepared.A[n][m],'global_tv':str(prepared.global_tv),'seeds':[1729,2718,31415]})
    invalid=[]
    for n,m in [(1,2),(2,1),(3,3)]:
      try:s.PreparedSampler(n,m)
      except ValueError as e:invalid.append({'N':n,'m':m,'rejected':str(e)})
      else:raise AssertionError(('empty accepted',n,m))
    long=s.MarkedCounter(2);word=long.sample(1400,random.Random(1729))
    assert len(word)==1400 and set(word)=={(0,1)} and long.connected_count(1400)==1
    big=s.exact_integer_json(10**5000);assert isinstance(big,dict)
    # Independent signature of endpoint-only loss: at zero remaining steps,
    # identity endpoint is accepted only when exposed support is connected.
    support=s.MarkedCounter(3)
    initial=support.identity
    assert support.count(0,initial,(0,0,0))==1
    assert support.count(0,initial,(0,1,2))==0
    result={'version':'SB-R3-SAMPLER-REGRESSIONS.v1','input_version':'sampler-v4.py','input_hashes':bd.MANIFEST['source_hashes'],
            'forward_laws':law,'fixed_top_level_cutoff':fixed,'boundaries':boundary,'empty_targets':invalid,
            'arbitrary_genus_small_support':{'N':2,'m':1400,'genus':699,'count':1,'identity':True,'seed':1729},
            'large_integer_serialization':{'decimal_digits':5001,'encoding_keys':list(big),'passed':True},
            'support_history_zero_remaining':{'connected_identity_count':1,'disconnected_identity_count':0},
            'CP1':'not invoked: no sequential marginal-product claim in tested count inequalities',
            'seconds':time.monotonic()-start,'python':platform.python_version(),'command':sys.argv}
    (bd.HERE/'sampler-regression-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'seconds':result['seconds'],'law_cases':law,'fixed_cutoff_paths':len(fixed),'boundary_cases':len(boundary),'empty_cases':len(invalid)},indent=2))
if __name__=='__main__':main()
