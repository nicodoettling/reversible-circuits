from pathlib import Path
import subprocess,json,os,time
out=Path(__file__).parent/'map-gates-v1.json'
commands=[['python3','-B','notes/project-map/manage.py','validate'],['python3','-B','notes/project-map/manage.py','check-freshness'],['python3','-B','notes/project-map/manage.py','render','--check'],['python3','-B','-m','unittest','discover','-s','notes/project-map','-p','test_*.py']]
rows=[]
for cmd in commands:
 start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True)
 rows.append(dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,elapsed_seconds=time.monotonic()-start))
t=out.with_suffix('.json.tmp');t.write_text(json.dumps(rows,indent=2)+'\n');os.replace(t,out)
print(json.dumps([dict(command=x['command'],exit_code=x['exit_code']) for x in rows]))
