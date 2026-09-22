#!/usr/bin/env python3
"""Verify and inventory this run without modifying prior research or launcher files."""
from pathlib import Path
import datetime, hashlib, json, platform, subprocess
R=Path(__file__).resolve().parent
ROOT=R.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
source=json.loads((R/'source_hashes.json').read_text())
verification={p:{'expected':h,'actual':digest(ROOT/p)} for p,h in source.items()}
assert all(v['expected']==v['actual'] for v in verification.values())
(R/'source_hashes_final.json').write_text(json.dumps(verification,indent=2)+'\n')
cap_path=ROOT/'notes/sparse-boundary-run.log.sparse-boundary-20260922.cap-status.json'
cap=json.loads(cap_path.read_text())
expected={'started_at':'2026-09-22T09:25:28.937730+00:00','wrapup_at':'2026-09-22T10:15:28.937730+00:00','graceful_shutdown_at':'2026-09-22T10:24:23.937730+00:00','hard_deadline_at':'2026-09-22T10:25:28.937730+00:00'}
assert all(cap[k]==v for k,v in expected.items())
(R/'cap_final_snapshot.json').write_text(json.dumps(cap,indent=2)+'\n')
required=['plan.md','run_manifest.md','initial_git_status.txt','source_hashes.json','checkpoint.md','claim_ledger.md','proof.md','obstruction.md','coordinator_report.md','regression_registry.md','resume.md','coordinator-checks.json','coordinator-qc-checks.json','construction_audit.md']
for name in required:assert (R/name).is_file(),name
for role in ['r1-upper','r2-obstruction','r3-diagnostics','r4-construction','r5-referee']:
 base=R/'roles'/role
 assert (base/'plan.md').is_file() and (base/'report.md').is_file(),role
 assert list(base.glob('checkpoint*.md')),role
accepted=json.loads((R/'roles/r5-referee/integration_verification.json').read_text())
for path,h in accepted['hashes'].items():assert digest(ROOT/path)==h,path
scripts=[];jsons=[]
for path in R.rglob('*'):
 if path.is_file() and path.suffix=='.py':
  compile(path.read_bytes(),str(path),'exec');scripts.append(str(path.relative_to(R)))
 if path.is_file() and path.suffix=='.json':
  json.loads(path.read_text());jsons.append(str(path.relative_to(R)))
assert json.loads((R/'coordinator-qc-checks.json').read_text())['all_passed']
assert json.loads((R/'coordinator-checks.json').read_text())['status'].startswith('all assertions passed')
tracked=subprocess.check_output(['git','diff','--name-only'],cwd=ROOT,text=True)
assert not tracked,('unexpected tracked changes',tracked)
status=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True)
(R/'git_status_final.txt').write_text(status)
launch=json.loads((R/'tmux-run.json').read_text())
launcher={'tmux-run.json','tmux-status.json'}
future={'changed_files.txt','artifact_manifest.json','delivery_checks.json'}
files=sorted({str(p.relative_to(R)) for p in R.rglob('*') if p.is_file()}|future)
owned=[x for x in files if x not in launcher]
lines=['Attributable research files (all under experiments/20260922-sparse-boundary):']
lines += ['experiments/20260922-sparse-boundary/'+x for x in owned]
lines += ['','Launcher-owned files excluded from research attribution:']
lines += ['experiments/20260922-sparse-boundary/'+x for x in sorted(launcher)]
lines += ['notes/sparse-boundary-run.log','notes/sparse-boundary-run.log.sparse-boundary-20260922.cap-status.json']
lines += ['','Pre-existing untracked entries recorded by launcher before activation (not attributed to this research):',launch['git_before']['status_short'].rstrip(),'','Final git status:',status.rstrip(),'','Tracked diff: empty. Frozen old inputs: all unchanged.']
(R/'changed_files.txt').write_text('\n'.join(lines)+'\n')
checks={'utc':now,'status':'passed','python':platform.python_version(),'old_sources_unchanged':len(source),'accepted_hashes_verified':accepted['hashes'],'scripts_compiled_without_bytecode':scripts,'json_files_parsed':len(jsons),'required_root_files':required,'all_five_role_reports_present':True,'cap_times_unchanged':expected,'tracked_diff_empty':True,'research_files':len(owned),'native_completion_record_present':(R/'completion_record.json').exists(),'math_tests':'Previously completed exact tests and current result flags; no unnecessary repeated broad computation.'}
(R/'delivery_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
manifest={'utc':now,'hash':'sha256','excluded_mutable_launcher':sorted(launcher),'self_hash_omitted':True,'files':{str(p.relative_to(R)):{'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p!=R/'artifact_manifest.json' and str(p.relative_to(R)) not in launcher}}
(R/'artifact_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:checks[k] for k in ['utc','status','old_sources_unchanged','json_files_parsed','all_five_role_reports_present','tracked_diff_empty','research_files','native_completion_record_present']},indent=2))
