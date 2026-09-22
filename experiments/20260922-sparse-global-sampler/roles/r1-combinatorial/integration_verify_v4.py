#!/usr/bin/env python3
"""Reproduce the final integration delta and CLI checks; role-local output only."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, subprocess

ROLE=Path(__file__).resolve().parent
BASE=ROLE.parents[1]
OLD=ROLE/'integration_audit_inputs'
NEW=ROLE/'integration_audit_v4_inputs'

manifest=json.loads((NEW/'manifest.json').read_text())['files']
for item in manifest:
    path=Path(item['source'])
    assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256']
    assert Path(item['snapshot']).read_bytes()==path.read_bytes()

v3=OLD/'roles/r3-sampler/sampler-v3.py'
v4=NEW/'roles/r3-sampler/sampler-v4.py'
def invariant_ast(path):
    tree=ast.parse(path.read_text())
    return [ast.dump(node,include_attributes=False) for node in tree.body
            if not (isinstance(node,ast.Expr) and isinstance(node.value,ast.Constant) and isinstance(node.value.value,str))
            and not (isinstance(node,ast.FunctionDef) and node.name=='main')]
assert invariant_ast(v3)==invariant_ast(v4)
oldmain=next(node for node in ast.parse(v3.read_text()).body if isinstance(node,ast.FunctionDef) and node.name=='main')
newmain=next(node for node in ast.parse(v4.read_text()).body if isinstance(node,ast.FunctionDef) and node.name=='main')
assert [ast.dump(x) for x in oldmain.body[:-1]]==[ast.dump(x) for x in newmain.body[:-2]]
assert isinstance(newmain.body[-2],ast.Assign)
assert ast.unparse(newmain.body[-2].targets[0])=='predicate'
assert (OLD/'proof.md').read_text().replace('`roles/r3-sampler/sampler-v3.py`','`roles/r3-sampler/sampler-v4.py`')==(NEW/'proof.md').read_text()
assert (OLD/'sample.py').read_text().replace('sampler-v3.py','sampler-v4.py').replace('56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06','cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002')==(NEW/'sample.py').read_text()

rows=[]
for policy,n,m,override,expected_count in [('H0',4,6,None,3936),('H1',4,6,None,1056),('H0',3,6,0,240),('H1',4,0,0,1)]:
    cmd=['python3','-B',str(BASE/'sample.py'),'--n',str(n),'--m',str(m),'--policy',policy,'--certificate-only']
    if override is not None:cmd+=['--test-cutoff',str(override)]
    run=subprocess.run(cmd,text=True,capture_output=True,timeout=120)
    assert run.returncode==0,run.stderr
    obj=json.loads(run.stdout)
    predicate='v <= cutoff or g in {0,1}' if policy=='H0' else 'v <= cutoff'
    assert obj['implementation_version']=='R3-implementation-v4'
    assert obj['allowed_nontrivial_component_predicate']==predicate and predicate in obj['target']
    assert 'A(N,m)' not in obj['target'] and 'B(N,m)' not in obj['target']
    assert obj['allowed_count']==obj['Z_A']==expected_count
    assert obj['diagnostic_cutoff_override']==override
    assert obj['cutoff_source']==('top-level K(N,m)' if override is None else 'diagnostic override')
    assert obj['cutoff']==(obj['top_level_cutoff'] if override is None else override)
    rows.append({'command':cmd,'returncode':run.returncode,'output':obj,'passed':True})
result={'recorded_at':datetime.now(timezone.utc).isoformat(),'reviewed_hashes':manifest,
        'command':'python3 -B experiments/20260922-sparse-global-sampler/roles/r1-combinatorial/integration_verify_v4.py',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_nonmain_nondoc_AST_unchanged':True,'main_preprint_choice_AST_unchanged':True,
        'canonical_proof_only_executable_reference_changed':True,'root_wrapper_only_version_and_digest_changed':True,
        'CLI_cases':rows,'INT_L1':'CLOSED','passed':True}
(ROLE/'integration_v4_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'CLI_cases':len(rows),'INT_L1':'CLOSED'}))
