#!/usr/bin/env python3
"""Hash-frozen exact finite H0/H1 certificates. Run with python3 -B."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, math, platform, sys, time
from fractions import Fraction
from collections import Counter
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
MANIFEST=json.loads((HERE/'source_hashes.json').read_text())

def load(relative,name):
    path=ROOT/relative
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest==MANIFEST['source_hashes'][relative], ('source changed',relative)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

d=load('experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/diagnostics.py','r3_frozen_diagnostics')

def star(n):
    lo,hi=0,n+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**4<=n**3:lo=mid
        else:hi=mid
    return lo-lo%2

def finite_bounds(n,m,k,c,total):
    if not 0<m<=n:return None
    x=Fraction(2*m,(n-m+1)**2)
    union_a=union_b=bound_a=bound_b=Fraction(0)
    rows=[]
    for v in range(k+1,min(n,m//2+1)+1):
        for g in range(m//2-v+2):
            ell=2*v-2+2*g
            exact=Fraction(d.marked_numerator(n,m,v,ell,c,total),total(n,m))
            upper=math.comb(n,v)*Fraction(v)**(v-3)*Fraction(v**3-v,36)**g/math.factorial(g)*x**(v-1+g)
            assert exact<=upper,('finite-count-incidence',n,m,v,g)
            union_b+=exact;bound_b+=upper
            if g>=2:union_a+=exact;bound_a+=upper
    return {'finite_genus_H0_upper':d.rational(bound_a),'finite_genus_H1_upper':d.rational(bound_b),
            'marked_H0_union':d.rational(union_a),'marked_H1_union':d.rational(union_b)}

def run(args):
    started=time.monotonic()
    c=d.connected_counts(args.m_max)
    timing={'connected_seconds':time.monotonic()-started}
    f=d.active_counts(c,args.m_max)
    total=d.evaluator(f)
    checks=d.exact_checks(c,f,args.m_max) if args.checks else {}
    g01=d.active_counts(c,args.m_max,lambda v,ell:d.genus(v,ell)<=1)
    instances=[(1,0),(1,2),(2,0),(2,1),(2,2),(2,12),(3,4),(4,4),(4,6),
               (27,10),(28,12),(34,14),(43,16)]
    if args.m_max>=32:instances +=[(64,22),(81,26),(100,30),(104,32),(82,14),(42,12)]
    if args.m_max>=64:instances +=[(128,38),(181,48),(256,64)]
    if args.m_max>=128:instances +=[(400,88),(512,106),(645,128)]
    if args.cases:instances=[tuple(map(int,item.split(':'))) for item in args.cases.split(',')]
    policies={};rows=[]
    for n,m in instances:
        assert m<=args.m_max
        k=d.cutoff(n,m)
        if k not in policies:
            policies[k]=(d.active_counts(c,args.m_max,lambda v,ell:d.h0_allowed(v,ell,k)),
                         d.active_counts(c,args.m_max,lambda v,ell:v<=k))
        af,bf=policies[k]
        row=d.certificate(n,m,c,f,af,g01,bf)
        # Old helper's T0 label refers to m^5<=N^3; version explicitly here.
        row['historical_m5_range']=row.pop('T0_range',None)
        row['T0_m4_range']=m%2==0 and m**4<=n**3
        row['old_m3_range']=m%2==0 and m**3<=n**2
        row['m_star']=star(n)
        row['Z_A']=d.evaluator(af)(n,m);row['Z_B']=d.evaluator(bf)(n,m)
        z=row['Z']
        assert 0<=row['Z_B']<=row['Z_A']<=z
        if z:
            row['H0_retained']=d.rational(Fraction(row['Z_A'],z))
            row['H1_retained']=d.rational(Fraction(row['Z_B'],z))
            row['H0_error']=d.rational(Fraction(z-row['Z_A'],z))
            row['H1_error']=d.rational(Fraction(z-row['Z_B'],z))
            row['finite_bounds']=finite_bounds(n,m,k,c,total)
        rows.append(row)
    first=None
    for n in range(2,129):
        m=star(n);k=d.cutoff(n,m)
        if k<n and m>=2*k+4:
            first={'N':n,'m':m,'K':k,'required_component':[k+1,2*k+4,2]};break
    result={'version':'SB-R3-DIAG.v1','target':'global U_(N,m), exact H0=A and H1=B counts',
            'status':'exact finite checks; no asymptotic consequence',
            'command':sys.argv,'python':platform.python_version(),'commit':MANIFEST['commit'],
            'source_hashes':MANIFEST['source_hashes'],'m_max':args.m_max,'seeds':None,
            'timings':timing,'seconds':time.monotonic()-started,'checks':checks,
            'first_nonzero_H0_in_boundary_scan':first,'rows':rows,'connected_counts':c}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'seconds':result['seconds'],'first':first,'checks':len(checks.get('cases',[])),
      'rows':[{'N':r['N'],'m':r['m'],'K':r['K'],'T0':r['T0_m4_range'],
        'H0_error':r.get('H0_error',{}).get('decimal'),'H1_error':r.get('H1_error',{}).get('decimal')} for r in rows]},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m-max',type=int,default=16)
    p.add_argument('--checks',action='store_true');p.add_argument('--cases')
    p.add_argument('--output',type=Path,required=True);run(p.parse_args())
