"""Exact conditional-gap certificates and K_A comparison; no spectral extrapolation."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE=Path(__file__).resolve().parent
IMPORTED=HERE.parent/'20261014-133815-cycle-excess-one/check.py'
spec=importlib.util.spec_from_file_location('previous_check',IMPORTED)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def endpoint(parts,n=None):
    n=sum(parts) if n is None else n
    g=list(range(n));start=0
    for size in parts:
        for i in range(start,start+size):g[i]=start+(i-start+1)%size
        start+=size
    return tuple(g)


def pair_table(n):
    gates=tuple(combinations(range(n),2))
    tab=defaultdict(list)
    for a in gates:
        for b in gates:tab[old.evaluate((a,b),n)].append((a,b))
    return tab


def comparison(n,m,g):
    tab=pair_table(n)
    words=list(old.bridge_words(n,m,g))
    ratios=set();channels=0;normalization_max=0
    for w in words:
        if g==old.cycle(n) and m==n+1:
            steps=old.core.normalize(w,n)
            assert steps<=2*(n+1)*m
            normalization_max=max(normalization_max,steps)
        p=old.local_row(w,n)
        q=defaultdict(F);q[w]=F(1,2)
        for i in range(m-1):
            choices=tab[old.evaluate(w[i:i+2],n)]
            for a,b in choices:
                z=w[:i]+(a,b)+w[i+2:]
                q[z]+=F(1,2*(m-1)*len(choices))
        assert sum(p.values())==sum(q.values())==1
        assert set(p)==set(q)
        for z,prob in q.items():
            assert old.evaluate(z,n)==g
            if z!=w:
                ratio=p[z]/prob
                assert F(1,2)<=ratio<=1
                ratios.add(ratio);channels+=1
    return dict(N=n,m=m,endpoint=g,states=len(words),
                directed_channels=channels,ratios=sorted(map(str,ratios)),
                exact_endpoint_and_comparison_pass=True,
                genus_one_normalization_max=normalization_max)


def length_two_checks(n):
    table=pair_table(n);checked=0
    for g,words in table.items():
        if len(words)==1:continue
        if g==tuple(range(n)):gap=F(1,4)
        elif len(words)==3:gap=F(3,8)
        else:
            assert len(words)==2
            gap=F(1,2)
        for w in words:
            row=old.local_row(w,n)
            for z in words:
                assert row.get(z,0)==(1-gap)*(w==z)+gap/len(words)
            checked+=1
    return dict(N=n,words_checked=checked,exact_gap_formula_pass=True)


def outer_matrix(n,g):
    gates=tuple(combinations(range(n),2))
    perms={t:old.core.perm(t,n) for t in gates}
    tset=set(perms.values())
    A=[[int(old.core.compose(old.core.compose(perms[a],g),perms[b]) in tset)
        for b in gates] for a in gates]
    rows=[i for i,row in enumerate(A) if sum(row)]
    cols=[j for j in range(len(gates)) if sum(row[j] for row in A)]
    return ([gates[i] for i in rows],[gates[j] for j in cols],
            [[A[i][j] for j in cols] for i in rows])


def ldl_certificate(M):
    """Exact no-pivot LDL; a zero pivot requires a zero remaining row."""
    A=[list(map(F,row)) for row in M];pivots=[]
    for k in range(len(A)):
        p=A[k][k];assert p>=0,(k,p,A)
        pivots.append(p)
        if not p:
            assert all(A[k][j]==0 for j in range(k+1,len(A)))
            continue
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                A[i][j]-=A[i][k]*A[k][j]/p
    return list(map(str,pivots))


def correlation_certificate(parts):
    n=sum(parts);g=endpoint(parts)
    rows,cols,A=outer_matrix(n,g)
    r=list(map(sum,A));c=[sum(row[j] for row in A) for j in range(len(cols))]
    # f_last=-sum r_i f_i / r_last parametrizes weighted mean-zero functions.
    d=len(r);V=[[F(i==j) for j in range(d-1)] for i in range(d-1)]
    V.append([-F(r[j],r[-1]) for j in range(d-1)])
    # B certifies squared maximal correlation <=4/9, without square roots.
    G=[[F(4,9)*r[i]*(i==k)-sum(F(A[i][j]*A[k][j],c[j]) for j in range(len(c)))
        for k in range(d)] for i in range(d)]
    B=[[sum(V[i][j]*G[i][k]*V[k][l] for i in range(d) for k in range(d))
        for l in range(d-1)] for j in range(d-1)]
    pivots=ldl_certificate(B)
    return dict(endpoint_cycle_parts=parts,rows=rows,columns=cols,
                outer_adjacency=A,row_degrees=r,column_degrees=c,
                mean_zero_matrix=[[str(x) for x in row] for row in B],
                exact_ldl_pivots=pivots,squared_correlation_bound='4/9',
                certificate_pass=True)


def transposition_window(n):
    g=endpoint((2,),n);rows,cols,A=outer_matrix(n,g)
    assert rows==cols
    for i,a in enumerate(rows):
        for j,b in enumerate(cols):
            expected=(a==(0,1) or b==(0,1) or a==b or
                      (len(set(a)&{0,1})==1 and len(set(b)&{0,1})==1
                       and (set(a)-{0,1})==(set(b)-{0,1})))
            assert A[i][j]==expected
    result=dict(N=n,states=sum(map(sum,A)),outer_matrix_formula_pass=True)
    if n>=4:
        def f(a):
            if a in ((0,2),(1,2)):return 1
            if a in ((0,3),(1,3)):return -1
            return 0
        for i,a in enumerate(rows):
            assert F(sum(A[i][j]*f(b) for j,b in enumerate(cols)),sum(A[i]))==F(2,3)*f(a)
        words=list(old.bridge_words(n,3,g));values={w:f(w[0])+f(w[2]) for w in words}
        assert sum(values.values())==0 and any(values.values())
        tab=pair_table(n)
        for w in words:
            hf=F(0)
            for i in range(2):
                choices=tab[old.evaluate(w[i:i+2],n)]
                avg=sum(values[w[:i]+(a,b)+w[i+2:]] for a,b in choices)/F(len(choices))
                hf+=values[w]-avg
            assert hf==F(1,3)*values[w]
        # Every such triple is a conditional fiber in a full-cycle N+1 word.
        tail=tuple((i,i+1) for i in range(1,n-1))
        for w in words:assert old.evaluate(w+tail,n)==old.cycle(n)
        result.update(exact_overlap_generator_eigenvalue='1/3',
                      conditional_correlation='2/3',
                      embedded_full_cycle_length=n+1,
                      every_conditional_word_embeds=True)
    return result


def main():
    result=dict(command='python3 -B '+str(HERE.relative_to(Path.cwd())/'check.py'),
                commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                python=platform.python_version(),dependencies='standard library only',
                seeds='none: exact deterministic enumeration and rational certificates',
                imported_source=str(IMPORTED.relative_to(Path.cwd())),
                imported_sha256=hashlib.sha256(IMPORTED.read_bytes()).hexdigest(),
                imported_core_sha256=hashlib.sha256(old.CORE.read_bytes()).hexdigest())
    result['length_two']=[length_two_checks(n) for n in range(2,9)]
    result['length_three_minimal_types']=[correlation_certificate(parts)
                                         for parts in [(4,),(3,2),(2,2,2)]]
    result['transposition_windows']=[transposition_window(n) for n in range(2,13)]
    print('Exact local correlation certificates and embedding witnesses passed',flush=True)
    result['comparison_cases']=[]
    cases=[(3,4,old.cycle(3)),(4,5,old.cycle(4)),(5,6,old.cycle(5)),
           (3,4,tuple(range(3))),(4,4,tuple(range(4))),(4,6,tuple(range(4)))]
    for n,m,g in cases:
        row=comparison(n,m,g);result['comparison_cases'].append(row)
        print(n,m,row['states'],row['ratios'],flush=True)
    result['status']='all exact checks passed; growing-N polynomial K_A gap not proved'
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
