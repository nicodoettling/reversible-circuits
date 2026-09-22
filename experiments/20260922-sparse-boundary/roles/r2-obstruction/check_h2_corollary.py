#!/usr/bin/env python3
"""Exact parameter checks for the separately versioned H2 corollary."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROLE=Path(__file__).resolve().parent
ROOT=ROLE.parents[3]
source=ROOT/'experiments/20260922-sparse-boundary/roles/r4-construction/proof-v1.md'
rows=[]
for j in [1,2,4,8,16,32,63,64,65,128,256]:
    n,m=2**(8*j),2**(6*j)
    p=n+m+2
    value=1
    cap=0
    while cap<n and value*3<=p**4:
        value*=3
        cap+=1
    assert cap<=32*j+4
    x=Fraction(m//2,n*n)
    assert Fraction(cap**3-cap,36)*x<=1
    assert Fraction((32*j+4)**3,72*2**(10*j))<1
    assert 3*n*x<=Fraction(1,2) and x<=1
    if j>=64:
        assert 2**36*j**4<=2**j
    rows.append({'j':j,'L':cap,'L_bound':32*j+4,'numerator_conditions':True})
result={'status':'pass','scope':'finite exact parameter falsification; proof separate',
        'policy_source':str(source.relative_to(ROOT)),
        'policy_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'command':'python3 -B experiments/20260922-sparse-boundary/roles/r2-obstruction/check_h2_corollary.py',
        'rows':rows}
(ROLE/'h2-corollary-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
