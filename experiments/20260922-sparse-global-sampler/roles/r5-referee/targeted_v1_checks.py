#!/usr/bin/env python3
"""Independent checks against copied exact current and historical versions."""
from collections import defaultdict
from itertools import product,combinations
from math import comb
from pathlib import Path
import datetime,hashlib,json,platform,subprocess,sys,time,types

HERE=Path(__file__).resolve().parent
source=HERE/'review-inputs-v1/g01-sampler.input.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d'
g=types.ModuleType('r5_frozen_g01');g.__file__=str(source);sys.modules[g.__name__]=g
exec(compile(source.read_bytes(),str(source),'exec'),g.__dict__)

def merge(part,a,b):
    x,y=part[a],part[b]
    q=tuple(x if c==y else c for c in part);ren={}
    return tuple(ren.setdefault(c,len(ren)) for c in q)

def swap(p,a,b):
    q=list(p);q[a],q[b]=q[b],q[a];return tuple(q)

def cycle_lengths(p):
    seen=set();ans=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;l=0
        while j not in seen:seen.add(j);j=p[j];l+=1
        ans.append(l)
    return tuple(ans)

start=time.monotonic();endpoints=[]
for n in range(1,6):
    identity=tuple(range(n));states={(identity,identity):1};checks=0
    maxstates=1
    for ell in range(2*n+1):
        for (p,part),value in states.items():
            if len(set(part))!=1:continue
            alpha=cycle_lengths(p)
            for genus in (0,1):
                if ell==n+len(alpha)-2+2*genus:
                    assert g.count(alpha,genus)==value,(n,ell,p,genus,value,g.count(alpha,genus))
                    if ell:
                        assert sum(x.weight for x in g.branches(p,genus))==value
                    checks+=1
        if ell==2*n:break
        nxt=defaultdict(int)
        for (p,part),value in states.items():
            for a,b in combinations(range(n),2):nxt[(swap(p,a,b),merge(part,a,b))]+=value
        states=nxt;maxstates=max(maxstates,len(states))
    endpoints.append({'n':n,'connected_endpoint_checks':checks,'max_states':maxstates})

allocation=[]
for lengths in [(1,)*7,(1,1,2,3),(2,2,2,2),(1,3,1,2),(4,1,1),(2,1,3,1,1)]:
    cases=0
    for assignment_status in product((-1,0,1),repeat=len(lengths)-2):
        forced={0:0,1:1}|{i+2:x for i,x in enumerate(assignment_status) if x!=-1}
        for ga,gb in [(0,0),(1,0),(0,1)]:
            expected=0
            for assignment in product((0,1),repeat=len(lengths)):
                if any(assignment[i]!=side for i,side in forced.items()):continue
                left=tuple(x for i,x in enumerate(lengths) if assignment[i]==0)
                right=tuple(x for i,x in enumerate(lengths) if assignment[i]==1)
                la=sum(left)+len(left)-2+2*ga;lb=sum(right)+len(right)-2+2*gb
                expected+=comb(la+lb,la)*g.count(left,ga)*g.count(right,gb)
            observed=g.allocation_mass(lengths,ga,gb,forced)
            assert expected==observed,(lengths,ga,gb,forced,expected,observed)
            cases+=1
    allocation.append({'lengths':lengths,'forced_allocation_checks':cases})

# Check the actual CLI's serialization operation independently of expensive
# preparation. (N,m)=(100000,1000) meets m^5=N^3. Adjacent repeated pairs
# give Z>=binom(N,2)^(m/2), so its integer certificate exceeds the runtime cap.
N,m=100000,1000;lower=comb(N,2)**(m//2)
assert m**5==N**3
cap=sys.get_int_max_str_digits()
try:json.dumps({'Z':lower});serialization={'status':'no failure','runtime_digit_limit':cap}
except ValueError as e:serialization={'status':'ValueError','message':str(e),'runtime_digit_limit':cap,'N':N,'m':m,'T0':True,'lower_bound_bits':lower.bit_length(),'reason':'Z >= choose(N,2)^(m/2) from adjacent repeated pairs; default CLI serializes Z as a decimal JSON integer'}

result={'status':'mathematical checks passed','endpoint_checks':endpoints,'allocation_checks':allocation,'CLI_serialization':serialization,'elapsed_seconds':time.monotonic()-start,'provenance':{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'seed':'none; exhaustive deterministic checks','command':'timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r5-referee/targeted_v1_checks.py','git_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'g01_input_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}}
(HERE/'targeted_v1_checks.results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
