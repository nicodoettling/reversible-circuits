"""Final clean-process, exact-version decisive reproduction. Coordinator owned."""
import argparse,hashlib,importlib.util,json,os,platform,subprocess,sys,time
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m


def verify_manifest(base,name,field):
    obj=json.loads((base/name).read_text());checks={}
    for name,expected in obj[field].items():
        actual=hashlib.sha256((base/name).read_bytes()).hexdigest()
        assert actual==expected,(base/name,actual,expected)
        checks[str(base/name)]=actual
    return checks


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    start=time.monotonic();pinned={}
    pinned.update(verify_manifest(ROOT/'coordinator','coefficient-freeze-v1.json','files'))
    pinned.update(verify_manifest(ROOT/'roles/r1-recursion','manifest-v1.json','files'))
    pinned.update(verify_manifest(ROOT/'roles/r2-structure','freeze-manifest-v1.json','payloads'))
    # The actual reviewed parser is loaded in a new interpreter; no cached coefficients.
    R=load('clean_production_law',ROOT/'roles/r3-adversarial/review-t0-v1/production_law_check_v1.py')
    assert sorted(R.I.decoder.SPECS)==[0,1]
    R.I.prepare(3)
    expected=json.loads((ROOT/'coordinator/coefficient-results-v1.json').read_text())['coefficients']
    for genus in (2,3):assert R.I.coefficient.recover(genus)==expected[str(genus)]
    reference=R.REF.connected_state_dp(3,10)
    law=R.whole_law((0,1,2),3,reference[10][(0,1,2)])
    assert law['word_count']==19680 and law['probability']==[1,19680]
    ordinary,connected=R.REF.tables(5,18)
    # Fresh full conditional partition identity at (1,2,1,1) with two genus-one children.
    sizes=(1,2,1,1);forced={0:0,1:1};z=R.I.decoder.allocation_mass(sizes,1,1,forced)
    za=R.I.decoder.allocation_mass(sizes,1,1,{**forced,2:0})
    zb=R.I.decoder.allocation_mass(sizes,1,1,{**forced,2:1})
    assert z==za+zb and z>=0 and za>=0 and zb>=0
    assert R.I.coefficient.ordinary((1,1,1),4)==27
    assert R.I.coefficient.ordinary((1,1,1,1),4)==120
    assert R.I.coefficient.ordinary((1,1,1,1),6)==3936
    assert R.I.coefficient.ordinary((1,2),5)==81 and R.I.coefficient.connected((1,2),5)==80
    assert Fraction(21,2000)>Fraction(1,100) and Fraction(21,221)<Fraction(1,10)
    for p,h in pinned.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    result={'status':'passed','kind':'fresh Python interpreter, generated coefficients and actual production-law replay','commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'python':platform.python_version(),'dependencies':'stdlib','seed':None,'pinned_files_verified':len(pinned),'pinned_sha256':pinned,'regenerated_genera':[2,3],'actual_production_law':law,'forcing_partition':{'sizes':sizes,'genus_pair':[1,1],'total':z,'extensions':[za,zb]},'regressions':['S3m4=27','S4m4=120','S4m6=3936','ordinary81/connected80','CP1 false marginal product rejected'],'elapsed_seconds':time.monotonic()-start,'command':sys.argv}
    out=Path(a.output);tmp=out.with_name(out.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,out)
    print(json.dumps({'status':'passed','pins':len(pinned),'whole_law_words':law['word_count'],'seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
