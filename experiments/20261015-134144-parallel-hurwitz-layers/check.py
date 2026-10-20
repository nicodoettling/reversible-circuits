"""Exact validation of cyclic parallel Hurwitz layers and their endpoint seam."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'20261014-133815-cycle-excess-one/check.py'
spec=importlib.util.spec_from_file_location('old',SOURCE)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def conjugate(t,p):
    return tuple(sorted(p[x] for x in t))


def seam(w,g,sign):
    if sign==0:return w
    a,b=w[0],w[-1]
    gi=old.inverse(g)
    if sign==1:
        first=old.core.conj(conjugate(b,g),a)
        last=conjugate(a,gi)
    else:
        first=conjugate(b,g)
        last=old.core.conj(conjugate(a,gi),b)
    return (first,)+w[1:-1]+(last,)


def naive_seam(w,sign):
    b,a=old.core.hurwitz((w[-1],w[0]),0,sign)
    return (a,)+w[1:-1]+(b,)


def move(w,g,k,sign):
    if not sign:return w
    return seam(w,g,sign) if k==len(w)-1 else old.core.hurwitz(w,k,sign)


def seam_lift(w,sign):
    states=[w]
    for k in range(len(w)-2):
        states.append(old.core.hurwitz(states[-1],k,1))
    states.append(old.core.hurwitz(states[-1],len(w)-2,sign))
    for k in range(len(w)-3,-1,-1):
        states.append(old.core.hurwitz(states[-1],k,-1))
    return states


def matching(m,parity):
    return tuple(range(parity,m,2))


def layer(w,g,parity,vector,reverse=False):
    steps=list(zip(matching(len(w),parity),vector))
    if reverse:steps.reverse()
    for k,sign in steps:w=move(w,g,k,sign)
    return w


def components(words,neighbors):
    unseen=set(words);sizes=[]
    while unseen:
        start=unseen.pop();todo=[start];count=1
        while todo:
            w=todo.pop()
            for z in neighbors(w):
                if z in unseen:
                    unseen.remove(z);todo.append(z);count+=1
        sizes.append(count)
    return sorted(sizes)


def audit(n,m,g,words=None):
    if words is None:words=sorted(old.bridge_words(n,m,g))
    words=list(words);wordset=set(words)
    vectors=tuple(product((-1,0,1),repeat=m//2))
    channels=0;naive_failures=0;orders=Counter()
    # Store only support of each layer row; exact detailed balance is checked
    # channelwise by its same-matching inverse vector.
    adjacency={}
    for w in words:
        assert old.evaluate(w,n)==g
        for sign in (-1,1):
            z=seam(w,g,sign);path=seam_lift(w,sign)
            assert z==path[-1]
            assert all(old.evaluate(x,n)==g for x in path)
            assert seam(z,g,-sign)==w
            naive_failures+=old.evaluate(naive_seam(w,sign),n)!=g
        for k in range(m):
            z=move(w,g,k,1);length=1
            while z!=w:
                z=move(z,g,k,1);length+=1
                assert length<=3
            orders[length]+=1
        row=Counter()
        for parity in (0,1):
            for vector in vectors:
                z=layer(w,g,parity,vector)
                assert z in wordset and old.evaluate(z,n)==g
                assert layer(w,g,parity,vector,reverse=True)==z
                assert layer(z,g,parity,tuple(-x for x in vector))==w
                row[z]+=1;channels+=1
        assert sum(row.values())==2*3**(m//2)
        adjacency[w]=set(row)
    layer_components=components(words,lambda w:adjacency[w])
    ordinary_components=components(words,lambda w:(old.core.hurwitz(w,k,s)
                                   for k in range(m-1) for s in (-1,1)))
    assert layer_components==ordinary_components
    if g==tuple(range(n)):assert naive_failures==0
    return dict(N=n,m=m,endpoint=g,states=len(words),layer_channels=channels,
        local_cycle_histogram=dict(sorted(orders.items())),naive_seam_endpoint_failures=naive_failures,
        layer_component_sizes=layer_components,ordinary_component_sizes=ordinary_components,
        product_and_inverse_layer_balance=True,matching_commutation=True,seam_lift=True)


def scalar_certificates():
    tested=0
    for k in range(1,21):
        # Only counts of local eigenvalues matter; cover every combination.
        for zeros in range(k+1):
            for negatives in range(k-zeros+1):
                eigen=F(0) if zeros else F(-1,3)**negatives
                layer_energy=1-eigen
                local_sum=zeros+F(4,3)*negatives
                assert F(2,3*k)*local_sum<=layer_energy<=local_sum
                projection_energy=int(zeros+negatives>0)
                assert F(8,9)*projection_energy<=layer_energy<=F(4,3)*projection_energy
                assert eigen>=F(-1,3)
                tested+=1
    return dict(matching_sizes_through=20,complete_eigenvalue_count_types=tested,
                scalar_form_and_projection_bounds=True)


def heat_bath_boundary(n,m,g):
    gates=tuple(combinations(range(n),2));gi=old.inverse(g)
    count=0;active=0
    for w in old.bridge_words(n,m,g):
        a,b=w[0],w[-1]
        eligible=a==conjugate(b,g)
        active+=eligible
        for s in gates:
            expected=(conjugate(s,g),)+w[1:-1]+(s,) if eligible else w
            u=w
            for k in range(m-2):u=old.core.hurwitz(u,k,1)
            if u[-2]==u[-1]:u=u[:-2]+(s,s)
            for k in range(m-3,-1,-1):u=old.core.hurwitz(u,k,-1)
            assert u==expected and old.evaluate(u,n)==g
            if eligible:
                assert u[0]==conjugate(u[-1],g)
                reverse=(conjugate(b,g),)+u[1:-1]+(b,)
                assert reverse==w
            count+=1
    return dict(N=n,m=m,endpoint=g,channels=count,eligible_words=active,
                twisted_square_and_lift=True)


if __name__=='__main__':
    cases=[(2,2,tuple(range(2))),(3,2,old.cycle(3)),
           (4,2,(1,0,3,2)),(3,4,tuple(range(3))),(4,4,tuple(range(4))),
           (4,6,tuple(range(4))),(3,4,old.cycle(3)),
           (5,4,old.cycle(5)),(5,6,old.cycle(5))]
    commuting=tuple((2*i,2*i+1) for i in range(4))
    result=dict(metadata=dict(commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        python=platform.python_version(),dependencies='standard library only',
        random_seeds='none: exhaustive deterministic checks',
        command='python3 -B experiments/20261015-134144-parallel-hurwitz-layers/check.py',
        imported_sources={str(p.relative_to(HERE.parents[1])):hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (SOURCE,old.CORE)}),
        cases=[audit(*case) for case in cases],
        commuting=audit(8,4,old.evaluate(commuting,8),permutations(commuting)),
        scalar_certificates=scalar_certificates(),
        heat_bath_boundary=[heat_bath_boundary(n,m,g) for n,m,g in
                           [(3,4,tuple(range(3))),(4,4,tuple(range(4))),
                            (4,6,tuple(range(4))),(3,4,old.cycle(3))]])
    w=((0,1),(1,2),(2,3),(3,4));g=old.evaluate(w,5)
    result['naive_seam_witness']=dict(word=w,endpoint=g,
        naive_output=naive_seam(w,1),naive_endpoint=old.evaluate(naive_seam(w,1),5),
        corrected_output=seam(w,g,1),corrected_endpoint=old.evaluate(seam(w,g,1),5))
    assert result['naive_seam_witness']['naive_endpoint']!=g
    (HERE/'results.jsonl').write_text(json.dumps(result,sort_keys=True)+'\n')
    print(json.dumps(dict(states=sum(c['states'] for c in result['cases'])+result['commuting']['states'],
        layer_channels=sum(c['layer_channels'] for c in result['cases'])+result['commuting']['layer_channels'],
        cases=[{k:c[k] for k in ('N','m','states','layer_component_sizes','naive_seam_endpoint_failures')}
               for c in result['cases']],verdict='all exact checks passed'),indent=2))
