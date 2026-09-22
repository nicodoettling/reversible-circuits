#!/usr/bin/env python3
"""Inventory only this run's research outputs; leave launcher files untouched."""
from datetime import datetime, timezone
import hashlib, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
EXTERNAL={'tmux-run.json','tmux-status.json'}
(ROOT/'git_status_final.txt').write_text(subprocess.check_output(['git','status','--short'],cwd=REPO,text=True))
# Create placeholders before listing, avoiding a self-referential hash.
for name in ('changed_files.txt','artifact_manifest.json'):
    if not (ROOT/name).exists(): (ROOT/name).write_text('')
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.relative_to(ROOT).as_posix() not in EXTERNAL)
(ROOT/'changed_files.txt').write_text(''.join(str(p.relative_to(REPO))+'\n' for p in paths))
rows=[]
for p in paths:
    rel=p.relative_to(ROOT).as_posix()
    if rel=='artifact_manifest.json': continue
    payload=p.read_bytes()
    rows.append(dict(path=rel,bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest()))
manifest=dict(schema_version=1,generated_at=datetime.now(timezone.utc).isoformat(),
              session_id='01a0c7a4-3ed2-7372-914a-19f0ed2228c6',
              commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
              scope='Only research files in experiments/20260922-sparse-global-sampler',
              excluded_launcher_owned=sorted(EXTERNAL),
              excluded_external='All notes and pre-existing September7 work; never attributed to this run',
              self_hash_note='artifact_manifest.json inventories itself by name only to avoid recursion',
              attributable_file_count=len(paths),files=rows)
(ROOT/'artifact_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(attributable_file_count=len(paths),hashed_files=len(rows),
                     bytes=sum(row['bytes'] for row in rows),manifest='artifact_manifest.json')))
