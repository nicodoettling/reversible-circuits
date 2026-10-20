"""Deterministic exact tests for the excess-one proof attempt."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE = Path(__file__).resolve().parent
CORE = HERE.parent / '20261014-111117-nonlocal-graph-lift/check.py'
spec = importlib.util.spec_from_file_location('nonlocal_core', CORE)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def evaluate(w, n):
    p = list(range(n))
    for a, b in w:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def inverse(p):
    q = [0]*len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def cycle(n):
    return tuple((i+1) % n for i in range(n))


def bridge_words(n, m, target):
    """Meet in the middle, exact ordered words at a specified endpoint."""
    gates = tuple(combinations(range(n), 2))
    left_len = m//2
    right = defaultdict(list)
    for v in product(gates, repeat=m-left_len):
        right[evaluate(v, n)].append(v)
    for u in product(gates, repeat=left_len):
        needed = core.compose(inverse(evaluate(u, n)), target)
        for v in right.get(needed, ()):
            yield u+v


def collisions(w):
    return sum(k*(k-1)//2 for k in Counter(w).values())


def graph(w):
    return tuple(sorted(w))


def square_rows(words, n, adjacent=False, balanced=False):
    gates = tuple(combinations(range(n), 2))
    M, m = len(gates), len(words[0])
    all_pairs = tuple(zip(range(m-1), range(1, m))) if adjacent else tuple(combinations(range(m), 2))
    rows = {}
    max_ratio = F(0)
    min_ratio = None
    min_acceptance = F(1)
    for w in words:
        eq = [ij for ij in all_pairs if w[ij[0]] == w[ij[1]]]
        row = defaultdict(F)
        if not eq:
            rows[w] = {w:F(1)}
            continue
        pairs = eq if balanced else all_pairs
        for i, j in pairs:
            for s in gates:
                z = core.macro(w, i, j, 'R', s)
                accept = min(F(1), F(collisions(w), collisions(z))) if balanced else F(1)
                weight = F(1, len(pairs)*M)
                row[z] += weight*accept
                row[w] += weight*(1-accept)
                if balanced and z != w:
                    min_acceptance = min(min_acceptance, accept)
                    ratio = F(len(all_pairs), max(collisions(w), collisions(z)))
                    min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
                    max_ratio = max(max_ratio, ratio)
        assert sum(row.values()) == 1
        assert all(evaluate(z, n) == evaluate(w, n) for z in row)
        rows[w] = dict(row)
    for w, row in rows.items():
        for z, q in row.items():
            assert rows[z].get(w, 0) == q
    action = sum(1-row.get(w, 0) for w, row in rows.items())/len(words)
    return rows, dict(action=str(action), min_acceptance=str(min_acceptance),
                      min_nontrivial_channel_ratio=str(min_ratio),
                      max_nontrivial_channel_ratio=str(max_ratio))


def genus_one(n):
    m = n+1
    words = list(bridge_words(n, m, cycle(n)))
    expected = n**(n+1)*(n*n-1)//24
    assert len(words) == expected
    Y = Counter(collisions(w) for w in words)
    X = Counter(sum(a == b for a,b in zip(w,w[1:])) for w in words)
    assert max(Y) <= 3 and max(X) <= 2
    assert F(sum(k*v for k,v in Y.items()),len(words)) == F(6,n)
    assert F(sum(k*v for k,v in X.items()),len(words)) == F(12,n*(n+1))
    assert F(len(words)-X.get(0,0), len(words)) == F(12*(n*n-2),n**3*(n+1))
    expected_pair = F(12,n*n*(n+1))
    pair_counts = []
    for i,j in combinations(range(m),2):
        c = sum(w[i] == w[j] for w in words)
        assert F(c,len(words)) == expected_pair
        pair_counts.append(c)
    result = dict(N=n,m=m,states=len(words),equal_pair_histogram=dict(Y),
                  adjacent_square_histogram=dict(X),equal_count_at_every_pair=pair_counts[0],
                  exact_formulas_pass=True)
    if n <= 4:
        old, old_stats = square_rows(words,n)
        new, new_stats = square_rows(words,n,balanced=True)
        C=m*(m-1)//2
        for w,row in old.items():
            for z,q in row.items():
                if z != w:
                    assert F(C,3)*q <= new[w].get(z,0) <= C*q
        result['uniform_pair_refresh'] = old_stats
        result['balanced_refresh'] = new_stats
    return result


def star_obstruction(n):
    reduced = tuple((0,k) for k in range(n-1,0,-1))
    a,b = reduced[:2]
    w1 = (a,a,a,b)+reduced[2:]
    w2 = (a,b,a,a)+reduced[2:]
    assert w1 != w2 and graph(w1) == graph(w2)
    assert evaluate(w1,n) == evaluate(w2,n) == cycle(n)
    gates = tuple(combinations(range(n),2))
    checked = 0
    for w in (w1,w2):
        for i,j in combinations(range(n+1),2):
            for kind,args in [('H',(1,-1)),('R',gates)]:
                for arg in args:
                    z=core.macro(w,i,j,kind,arg)
                    assert z == w or graph(z) != graph(w)
                    checked += 1
    return dict(N=n,distinct_same_graph_witnesses=[w1,w2],
                all_restricted_offdiagonal_moves_absent=True,checked_channels=checked)


def local_row(w,n):
    gates=tuple(combinations(range(n),2))
    d=len(w)-1
    row=defaultdict(F)
    row[w] += F(1,2)
    for i in range(d):
        for sign in (1,-1):
            row[core.hurwitz(w,i,sign)] += F(1,8*d)
        for s in gates:
            row[core.macro(w,i,i+1,'R',s)] += F(1,4*d*len(gates))
    return dict(row)


def s3_coordinates(w):
    # Prefix permutations of a fixed parity form an independent 3-element set.
    p=(0,1,2)
    return tuple(evaluate(w[:i],3) for i in range(1,len(w)))


def s3_checks(m):
    gates=tuple(combinations(range(3),2))
    fibers=defaultdict(list)
    for w in product(gates,repeat=m):
        fibers[evaluate(w,3)].append(w)
    checked=0
    for target,words in fibers.items():
        assert len(words)==3**(m-1)
        for w in words:
            old=s3_coordinates(w)
            qrow=defaultdict(F)
            qrow[w] += F(1,2)
            decomposition=defaultdict(F)
            decomposition[w] += F(5,8)
            for i in range(m-1):
                pairprod=evaluate(w[i:i+2],3)
                choices=[(a,b) for a in gates for b in gates if evaluate((a,b),3)==pairprod]
                assert len(choices)==3
                prefixes=[]
                for pair in choices:
                    z=w[:i]+pair+w[i+2:]
                    new=s3_coordinates(z)
                    assert all(old[k]==new[k] for k in range(m-1) if k!=i)
                    prefixes.append(new[i])
                    qrow[z] += F(1,6*(m-1))
                    decomposition[z] += F(1,12*(m-1))
                    if w[i]!=w[i+1]:
                        decomposition[z] += F(1,24*(m-1))
                if w[i]==w[i+1]:
                    decomposition[w] += F(1,8*(m-1))
                assert len(set(prefixes))==3
            row=local_row(w,3)
            assert row==dict(decomposition)
            for z,q in qrow.items():
                if z!=w:
                    assert F(1,2)*q <= row.get(z,0)
            checked+=1
    return dict(m=m,endpoint_fibers=len(fibers),words=checked,
                independent_prefix_heatbath_and_local_decomposition_pass=True)


def contraction_check(d):
    # Gauge prefix parity classes into Z3; endpoints can be arbitrary.
    worst=F(-10)
    checks=0
    for end in range(3):
        for x in product(range(3),repeat=d):
            xx=(0,)+x+(end,)
            for k in range(d):
                for val in range(3):
                    if val==x[k]:continue
                    y=x[:k]+(val,)+x[k+1:]
                    yy=(0,)+y+(end,)
                    delta=F(-1,4*d) # common heat bath at differing coordinate
                    for i in range(d):
                        ax=(xx[i]!=xx[i+2]); ay=(yy[i]!=yy[i+2])
                        if i==k:
                            assert ax==ay
                            if ax:delta -= F(1,8*d)
                        elif ax!=ay:
                            delta += F(1,12*d) # 1/(8d) times mismatch probability 2/3
                    assert delta<=-F(1,12*d)
                    worst=max(worst,delta)
                    checks+=1
    return dict(d=d,neighbor_pairs_checked=checks,worst_expected_distance_change=str(worst),
                claimed_upper_bound=str(-F(1,12*d)))


def regressions(n,m):
    words=list(bridge_words(n,m,tuple(range(n))))
    _,stats=square_rows(words,n,balanced=True)
    expected={(3,4):27,(4,4):120,(4,6):3936}[(n,m)]
    assert len(words)==expected
    return dict(N=n,m=m,identity_states=len(words),balanced_refresh_exact=stats)


def main():
    result=dict(python=platform.python_version(),dependencies='standard library only',
                commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                command='python3 -B '+str(HERE.relative_to(Path.cwd())/'check.py'),
                seeds='none: exhaustive deterministic checks',
                imported_core_sha256=hashlib.sha256(CORE.read_bytes()).hexdigest())
    result['genus_one']=[genus_one(n) for n in range(2,6)]
    print('genus-one counts and refresh checks passed',flush=True)
    result['star_obstructions']=[star_obstruction(n) for n in range(3,13)]
    result['s3']=[s3_checks(m) for m in range(2,8)]
    result['coupling']=[contraction_check(d) for d in range(1,6)]
    print('S3 and fixed-graph obstruction checks passed',flush=True)
    result['identity_regressions']=[regressions(n,m) for n,m in [(3,4),(4,4),(4,6)]]
    result['status']='all exact checks passed; no asymptotic inference from enumeration'
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])


if __name__=='__main__':main()
