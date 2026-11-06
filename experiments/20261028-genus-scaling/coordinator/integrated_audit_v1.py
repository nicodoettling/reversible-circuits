"""Bounded finite audit of generated coefficients wired into the production parser."""
import argparse,datetime,hashlib,json,os,platform,random,subprocess,time
from fractions import Fraction
from itertools import product
from pathlib import Path
import integrated_sampler_v1 as I


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic();before=sorted(I.decoder.SPECS)
    assert before==[0,1]
    I.prepare(4)
    terms={str(h):len(I.decoder.SPECS[h]) for h in range(2,5)}
    checks=[]
    for g in range(5):
        for n in range(1,8):
            for alpha in I.coefficient.partitions(n):
                got=I.decoder.count(alpha,g)
                want=I.coefficient.connected(alpha,n+len(alpha)-2+2*g)
                assert got==want,(g,alpha,got,want)
                checks.append({'kind':'generated-count','g':g,'alpha':alpha,'count':got})
    # Production branch weights compared against an independent endpoint/support DP.
    for n in range(2,5):
        reference=I.coefficient.literal_connected_counts(n,2*n-2+8)
        for p,count in reference[2*n-2+8].items():
            if I.coefficient.cycle_type(p)!=(1,)*n:continue
            bs=I.decoder.branches(p,4)
            assert sum(b.weight for b in bs)==count
            checks.append({'kind':'g4-identity-branches','N':n,'count':count,'branches':len(bs)})
    # Full actual parser categorical law for N2 at new genus4; forced singleton fiber.
    for g in range(5):
        for seed in (103,211,307):
            word=I.sample_identity(2,g,random.Random(seed))
            assert word==((0,1),)*(2+2*g)
    samples=[]
    for seed in (103,211,307):
        rng=random.Random(seed)
        for n,g in ((3,3),(4,3),(3,4),(4,4)):
            word=I.sample_identity(n,g,rng)
            assert len(word)==2*n-2+2*g
            assert I.decoder.evaluate(n,word)==tuple(range(n))
            assert len(I.decoder.components(n,word))==1
            samples.append({'seed':seed,'N':n,'g':g,'word':word})
    sources=[Path(__file__),Path(I.__file__),Path(I.coefficient.__file__),Path(I.decoder.__file__)]
    result={'status':'passed','elapsed_seconds':time.monotonic()-start,'python':platform.python_version(),'dependencies':'standard library','commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'seeds':[103,211,307],'initial_installed_genera':before,'generated_term_counts':terms,'checks':checks,'samples':samples,'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'limitations':['finite reference only','g3/4 N3/4 samples test validity, not uniformity','whole N2 law is singleton','general proof separately reviewed']}
    out=Path(args.output);tmp=out.with_name(out.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,out)
    print(json.dumps({'status':result['status'],'checks':len(checks),'samples':len(samples),'seconds':result['elapsed_seconds'],'terms':terms}))
if __name__=='__main__':main()
