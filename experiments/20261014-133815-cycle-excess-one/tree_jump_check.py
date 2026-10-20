"""Exact preimage audit for tree-plus-extra-edge uniform refresh proposals."""
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess
from fractions import Fraction

HERE=Path(__file__).resolve().parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check=load('excess_checks',HERE/'check.py')
codec_path=HERE.parent/'20261013-single-cycle-walk/check.py'
codec=load('minimal_codec',codec_path)


def tree_count(word,n):
    """Parallel edge occurrences remain distinguishable by their positions."""
    count=0
    for positions in combinations(range(len(word)),n-1):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        for i in positions:
            a,b=word[i]
            a,b=find(a),find(b)
            if a==b:break
            parent[a]=b
        else:
            count+=1
    return count


def relabel_full_cycle(word,n):
    g=check.evaluate(word,n)
    label=[-1]*n
    v=0
    for j in range(n):
        if label[v]!=-1:return None
        label[v]=j
        v=g[v]
    if v!=0:return None
    return tuple(tuple(sorted((label[a],label[b]))) for a,b in word)


def check_proposals(n,h):
    m=n-1+2*h
    gates=tuple(combinations(range(n),2))
    minimal=[codec.tree_to_word(n,codec.code_to_tree(n,code))
             for code in product(range(n),repeat=n-2)]
    preimages=Counter()
    total=valid=0
    for u in minimal:
        for inserted in combinations(range(m),2*h):
            inserted=set(inserted)
            for extras in product(gates,repeat=2*h):
                ui=iter(u); ei=iter(extras)
                v=tuple(next(ei) if i in inserted else next(ui) for i in range(m))
                w=relabel_full_cycle(v,n)
                total+=1
                if w is not None:
                    assert check.evaluate(w,n)==check.cycle(n)
                    preimages[w]+=1
                    valid+=1
    words=set(check.bridge_words(n,m,check.cycle(n)))
    assert set(preimages)==words
    taus=Counter()
    for w,count in preimages.items():
        tau=tree_count(w,n)
        assert count==tau,(n,h,w,count,tau)
        assert 1<=tau<=comb(m,2*h)
        taus[tau]+=1
    accepted=Fraction(len(words),total)
    if h==1:
        assert accepted==Fraction(1,3*(n-1))
    if h==2:
        assert accepted==Fraction(5*n-7,15*(n-1)**3)
    assert accepted>=Fraction(1,comb(m,2*h)*len(gates)**h)
    return dict(N=n,h=h,m=m,states=len(words),proposal_tuples=total,
                valid_proposals=valid,acceptance_probability=str(accepted),
                tau_histogram=dict(sorted(taus.items())),
                exact_h1_or_h2_acceptance_formula_pass=True,
                every_output_preimage_count_equals_tau=True,
                rejection_corrected_per_word_weight='1 / proposal_tuples')


def main():
    result=dict(python=platform.python_version(),dependencies='standard library only',
                commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                command='python3 -B '+str(HERE.relative_to(Path.cwd())/'tree_jump_check.py'),
                seeds='none: exhaustive deterministic enumeration',
                imports={str(p.relative_to(Path.cwd())):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (HERE/'check.py',codec_path)})
    result['cases']=[]
    for n,h in [(2,1),(3,1),(4,1),(5,1),(3,2),(4,2)]:
        row=check_proposals(n,h)
        result['cases'].append(row)
        print(n,h,row['states'],row['acceptance_probability'],flush=True)
    result['status']='all exact preimage and uniform-law checks passed'
    (HERE/'tree_jump_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])


if __name__=='__main__':main()
