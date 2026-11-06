"""Nonauthor exact checks of frozen R1-T2.v1. Standard library only.

Signed source terms and literal words are independent references. No candidate
file is modified. Source reading and universal proof review are separate.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, prod
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, platform, sys, time

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent.parent/'r1-recursive'
spec=importlib.util.spec_from_file_location('reviewed_r1_t2',AUTHOR/'sampler-v1.py')
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)
EXPECTED='8b44aa29010b2cb1cb62bf879c191a090f04e704ba622024c15214ace588b63b'
assert hashlib.sha256((AUTHOR/'sampler-v1.py').read_bytes()).hexdigest()==EXPECTED


def parts(n,minimum=1):
    if not n:
        yield ()
    for a in range(minimum,n+1):
        for rest in parts(n-a,a):
            yield (a,)+rest


def elementary(values):
    row=[1]
    for a in values:
        nxt=row+[0]
        for j in range(1,len(nxt)):
            nxt[j]+=a*row[j-1]
        row=nxt
    return row


@lru_cache(None)
def signed_count(alpha,g):
    """Direct ordered numerator injections from signed source expression A.

    This does not call the production marker specification or coefficient
    functions. Genus1 uses the subtractive elementary-symmetric formula.
    """
    n,k=sum(alpha),len(alpha)
    if g==0:
        b=Q(n)**(k-3)
    elif g==1:
        e=elementary(alpha)
        b=(Q(n)**k-Q(n)**(k-1)-sum(factorial(j-2)*e[j]*Q(n)**(k-j)
                                  for j in range(2,k+1)))/24
    else:
        terms=((5,(4,),2),(-12,(3,),2),(7,(2,),2),
               (29,(2,3),3),(-25,(2,2),3),(28,(2,2,2),4))
        total=0
        for coefficient,powers,denpower in terms:
            d=len(powers)
            for slots in permutations(range(k),d):
                multiplier=coefficient*prod(alpha[i]**p for i,p in zip(slots,powers))
                remaining=[a for i,a in enumerate(alpha) if i not in slots]
                es=elementary(remaining)
                for j,ej in enumerate(es):
                    rising=factorial(denpower+j-1)//factorial(denpower-1)
                    total+=multiplier*rising*n**(k-d-j)*ej
        b=Q(total,5760)
    ans=factorial(n+k-2+2*g)*prod(Q(a**a,factorial(a-1)) for a in alpha)*b
    assert ans.denominator==1 and ans>=0,(alpha,g,ans)
    return ans.numerator


def count_checks():
    rows=[]
    for n in range(1,15):
        checked=0
        for alpha in parts(n):
            for g in (0,1,2):
                actual=s.count(alpha,g);expected=signed_count(alpha,g)
                assert actual==expected,(alpha,g,actual,expected)
                checked+=1
        rows.append({'degree':n,'counts':checked})
    return rows


def allocation_checks():
    inventories=((1,1),(1,1,1,1,1,1),(2,1,3,1,2),(1,2,1,3,2,1,4))
    pairs=((0,0),(0,1),(1,0),(0,2),(1,1),(2,0))
    rows=[]
    for aa in inventories:
        assignments=[(0,1)+tail for tail in product((0,1),repeat=len(aa)-2)]
        values={}
        for ass in assignments:
            left=tuple(sorted(a for a,x in zip(aa,ass) if x==0))
            right=tuple(sorted(a for a,x in zip(aa,ass) if x==1))
            for ga,gb in pairs:
                la=sum(left)+len(left)-2+2*ga;lb=sum(right)+len(right)-2+2*gb
                values[ass,ga,gb]=comb(la+lb,la)*signed_count(left,ga)*signed_count(right,gb)
        checked=zeros=0
        for partial in product((-1,0,1),repeat=len(aa)-2):
            forced={0:0,1:1}|{i+2:x for i,x in enumerate(partial) if x!=-1}
            for ga,gb in pairs:
                expected=sum(w for (ass,a,b),w in values.items()
                             if (a,b)==(ga,gb) and all(ass[i]==x for i,x in forced.items()))
                actual=s.allocation_mass(aa,ga,gb,forced)
                assert actual==expected,(aa,forced,ga,gb,actual,expected)
                checked+=1;zeros+=actual==0
        rows.append({'lengths':aa,'partial_forcing_queries':checked,'zero_masses':zeros})
    return rows


class Fork(Exception):
    def __init__(self,probabilities):self.probabilities=probabilities


class Oracle:
    def __init__(self,tape):self.tape=tape;self.cursor=0;self.probability=Q(1)
    def choice(self,values,weights):
        options=[(v,w) for v,w in zip(values,weights) if w]
        assert options and all(w>0 for _,w in options)
        if len(options)==1:return options[0][0]
        total=sum(w for _,w in options)
        if self.cursor==len(self.tape):raise Fork(tuple(Q(w,total) for _,w in options))
        index=self.tape[self.cursor];self.cursor+=1
        value,weight=options[index];self.probability*=Q(weight,total);return value


def own_eval(word,n):
    p=list(range(n))
    for a,b in word:p[a],p[b]=p[b],p[a]
    return tuple(p)


def own_connected(word,n):
    seen={0}
    while True:
        nxt=set(seen)
        for a,b in word:
            if a in seen:nxt.add(b)
            if b in seen:nxt.add(a)
        if nxt==seen:return len(seen)==n
        seen=nxt


def full_forward_longcycle():
    endpoint=(1,2,3,0);g=2;n=4;length=7
    saved_choice,saved_randbelow=s.weighted_choice,s.randbelow
    stack=[((),Q(1))];law=defaultdict(Q);nodes=leaves=0
    try:
        while stack:
            tape,probability=stack.pop();oracle=Oracle(tape)
            s.weighted_choice=lambda rng,values,weights:oracle.choice(values,weights)
            s.randbelow=lambda rng,bound:oracle.choice(range(bound),(1,)*bound)
            nodes+=1
            try:word=s.sample(endpoint,g,object())
            except Fork as fork:
                assert oracle.probability==probability
                stack.extend((tape+(i,),probability*p) for i,p in enumerate(fork.probabilities))
            else:
                assert oracle.cursor==len(tape) and oracle.probability==probability
                law[word]+=probability;leaves+=1
                assert leaves<=100000
    finally:s.weighted_choice,s.randbelow=saved_choice,saved_randbelow
    expected={w for w in product(tuple(combinations(range(n),2)),repeat=length)
              if own_eval(w,n)==endpoint and own_connected(w,n)}
    assert set(law)==expected and sum(law.values())==1
    assert all(p==Q(1,len(expected)) for p in law.values())
    assert len(expected)==signed_count((4,),2)
    digest=hashlib.sha256(repr(sorted(law.items())).encode()).hexdigest()
    return {'endpoint':endpoint,'genus':g,'length':length,'words':len(expected),
            'leaves':leaves,'execution_nodes':nodes,'each_probability':str(Q(1,len(expected))),
            'full_law_equals_literal_enumeration':True,'digest':digest}


def regressions():
    a=(0,1);b=(1,2);w=(a,b)*3
    assert own_eval(w,3)==(0,1,2) and own_connected(w,3)
    assert all(w[i]!=w[i+1] for i in range(len(w)-1))
    total=sum(own_eval(w,3)==(1,0,2) for w in product(((0,1),(0,2),(1,2)),repeat=5))
    connected=sum(own_eval(w,3)==(1,0,2) and own_connected(w,3)
                  for w in product(((0,1),(0,2),(1,2)),repeat=5))
    assert (total,connected)==(81,80)
    assert Q(21,2000)>Q(1,100) and Q(21,221)<Q(1,10)
    zero=[]
    for g in (1,2):
        try:s.sample((0,),g)
        except ValueError:zero.append(g)
        else:raise AssertionError('singleton positive genus accepted')
    assert s.sample((0,),0)==()
    for p in ((0,1),(1,0)):
        for g in (0,1,2):
            length=2+len(s.cycles(p))-2+2*g
            assert s.sample(p,g)==((0,1),)*length
    return {'support_total':total,'support_connected':connected,'squareless_retained':True,
            'cp1_rejects_marginal_product':True,'singleton_zero_genera':zero,'degree2_both_endpoints_all_genera':True}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    started=time.perf_counter()
    result={'status':'complete','python':platform.python_version(),'nonstandard_dependencies':[],
            'seeds':None,'base_commit':'d8893491e04aff74ff3185f7054470ffa24a44a4',
            'reviewed_sampler_sha256':EXPECTED,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'counts':count_checks(),'allocations':allocation_checks(),
            'forward_law':full_forward_longcycle(),'regressions':regressions()}
    assert hashlib.sha256((AUTHOR/'sampler-v1.py').read_bytes()).hexdigest()==EXPECTED
    result['elapsed_seconds']=time.perf_counter()-started
    result['generated_utc']=datetime.now(timezone.utc).isoformat()
    temp=args.output.with_name(args.output.name+'.tmp');temp.write_text(json.dumps(result,indent=2)+'\n');os.replace(temp,args.output)
    print(json.dumps({'status':'complete','seconds':result['elapsed_seconds'],'counts':sum(x['counts'] for x in result['counts']),
                      'allocation_queries':sum(x['partial_forcing_queries'] for x in result['allocations']),
                      'full_forward_words':result['forward_law']['words']}))
if __name__=='__main__':main()
