#!/usr/bin/env python3
"""Focused CLI metadata regression; unchanged sampling kernels checked by AST."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
source=HERE/'sampler.py'
old=HERE/'sampler-v3.py'

def kernel(path):
    tree=ast.parse(path.read_text())
    return {node.name:ast.dump(node,include_attributes=False) for node in tree.body
            if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name!='main'}

assert kernel(source)==kernel(old), 'a sampler/API/serialization kernel changed'
rows=[]
for policy,n,m,override,expected in [('H0',4,6,None,3936),('H1',4,6,None,1056),
                                    ('H0',3,8,2,3),('H1',4,6,2,96)]:
    command=[sys.executable,'-B',str(source),'--n',str(n),'--m',str(m),'--policy',policy,'--certificate-only']
    if override is not None:
        command += ['--test-cutoff',str(override)]
    data=json.loads(subprocess.check_output(command,text=True,timeout=30))
    predicate='v <= cutoff or g in {0,1}' if policy=='H0' else 'v <= cutoff'
    assert data['implementation_version']=='R3-implementation-v4'
    assert data['allowed_nontrivial_component_predicate']==predicate
    assert predicate in data['target']
    assert 'A(N,m)' not in data['target'] and 'B(N,m)' not in data['target']
    assert 'g=(ell-2*v+2)/2' in data['target'] and 'Isolated labels are allowed' in data['target']
    assert data['allowed_count']==data['Z_A']==expected
    assert data['top_level_cutoff']==data['h0_cutoff']==3
    assert data['diagnostic_cutoff_override']==override
    assert data['cutoff_source']==('top-level K(N,m)' if override is None else 'diagnostic override')
    assert data['cutoff']==(3 if override is None else override)
    assert data['candidate']==(f'{policy}-v1' if override is None else f'{policy}-test-cutoff-{override}')
    rows.append({'command':command,'output':data,'passed':True})
result={'version':'R3-CLI-audit-v4','sampler_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'historical_sampler_v3_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
        'unchanged_kernel_AST':True,'cases':rows,'passed':True}
(HERE/'cli-results-v4.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'cases':len(rows),'unchanged_kernel_AST':True,
                  'sampler_sha256':result['sampler_sha256']}))
