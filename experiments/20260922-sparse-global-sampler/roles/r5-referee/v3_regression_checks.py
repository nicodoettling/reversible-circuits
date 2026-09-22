#!/usr/bin/env python3
"""Version-locked independent CLI and H1 dependency regression checks."""
from pathlib import Path
from fractions import Fraction
import argparse,datetime,hashlib,json,platform,random,sys,types
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'review-inputs-v3/sampler-v3.py'
ROOT=HERE.parents[3]
ORIGINAL=ROOT/'experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler-v3.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06'
s=types.ModuleType('r5_v3');s.__file__=str(ORIGINAL);sys.modules[s.__name__]=s
exec(compile(SOURCE.read_bytes(),str(SOURCE),'exec'),s.__dict__)

def decode_int(x):
    if isinstance(x,int):return x
    assert x['encoding']=='hex';return int(x['value'],16)

def decode_fraction(x):
    if isinstance(x,str):return Fraction(x)
    assert x['encoding']=='hex-rational'
    return Fraction(int(x['numerator'],16),int(x['denominator'],16))

cap=sys.get_int_max_str_digits()
levels=sorted(set([0,1,2,20001]+([3*cap-1,3*cap,3*cap+1] if cap else [12900,12901])))
rows=[]
for bits in levels:
    for sign in (-1,1):
        v=sign*((1<<bits)-1)
        encoded=s.exact_integer_json(v)
        payload=json.dumps(encoded)
        assert decode_int(json.loads(payload))==v
        rows.append({'bits':bits,'sign':sign,'encoding':'integer' if isinstance(encoded,int) else encoded['encoding'],'json_length':len(payload)})
fractions=[]
for value in [Fraction(0),Fraction(1),Fraction(-3,7),Fraction((1<<20001)+1,(1<<20000)+3),Fraction(3,(1<<20001)+1),Fraction((1<<20001)+1,3)]:
    encoded=s.exact_fraction_json(value);payload=json.dumps(encoded)
    assert decode_fraction(json.loads(payload))==value
    fractions.append({'numerator_bits':abs(value.numerator).bit_length(),'denominator_bits':value.denominator.bit_length(),'encoding':'rational-string' if isinstance(encoded,str) else encoded['encoding'],'json_length':len(payload)})
assert sys.get_int_max_str_digits()==cap

# The core H1 claim is specifically independence from genus-0/1 formulas.
def forbidden(*args,**kwargs):raise AssertionError('H1 called forbidden g0/1 formula or decoder')
s.g01.count=forbidden;s.g01.normalized_count=forbidden;s.g01.sample=forbidden
h1=[]
for n,m in [(0,0),(1,0),(2,2),(3,4),(3,8),(4,6),(4,8),(5,12)]:
    prepared=s.PreparedSampler(n,m,policy='H1')
    for seed in (1729,2718,31415):
        w=prepared.sample(random.Random(seed)).word
        assert s.g01.evaluate(n,w)==tuple(range(n)) and len(w)==m
        assert all(len(block)<=prepared.cutoff for block in s.g01.components(n,w))
    h1.append({'N':n,'m':m,'K':prepared.cutoff,'Z':prepared.Z[n][m],'Z_H1':prepared.A[n][m],'seeds':[1729,2718,31415],'no_g01_calls':True})
result={'status':'passed','runtime_decimal_cap':cap,'integer_roundtrips':rows,'fraction_roundtrips':fractions,'cap_unchanged':True,'H1_dependency_isolation':h1,'provenance':{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'command':'PYTHONINTMAXSTRDIGITS='+str(cap)+' timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r5-referee/v3_regression_checks.py'}}
(HERE/('v3_regression_checks.cap'+str(cap)+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'passed','cap':cap,'integer_cases':len(rows),'fraction_cases':len(fractions),'H1_cases':len(h1)}))
