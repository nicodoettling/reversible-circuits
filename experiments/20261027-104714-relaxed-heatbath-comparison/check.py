#!/usr/bin/env python3
"""Exact audits of correction-gate lift, pair routing and Hamming expansion."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIOR = ROOT/'experiments/20261026-141337-relaxed-endpoint-refresh/check.py'
spec = importlib.util.spec_from_file_location('prior', PRIOR)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


class Model(prior.Group):
    def __init__(self, n):
        super().__init__(n)
        self.gates = [self.perms[self.next[0][t]] for t in range(self.M)]
        self.gate_index = {g:i for i,g in enumerate(self.gates)}
        self.pairs = defaultdict(list)
        for a,b in product(range(self.M),repeat=2):
            self.pairs[self.eval((a,b))].append((a,b))

    def eval(self, word):
        p = 0
        for t in word:
            p = self.next[p][t]
        return p

    def inverse(self, p):
        ans = [0]*self.n
        for i,j in enumerate(p): ans[j] = i
        return tuple(ans)

    def conjugate(self, p, t):
        # p t p^-1 acts by swapping p(a),p(b).
        a,b = self.edges[t]
        return self.edges.index(tuple(sorted((p[a],p[b]))))

    def pair_fiber(self, w, i, j):
        B = self.perms[self.eval(w[i+1:j])]
        x = self.conjugate(self.inverse(B),w[i])
        end = self.eval((x,w[j]))
        return [(self.conjugate(B,a),b) for a,b in self.pairs[end]]

    def band(self, w, i, j, sign):
        B = self.perms[self.eval(w[i+1:j])]
        x,y = self.conjugate(self.inverse(B),w[i]),w[j]
        if sign == 1:
            a,b = y,self.conjugate(self.gates[y],x)
        else:
            a,b = self.conjugate(self.gates[x],y),x
        ans = list(w)
        ans[i],ans[j] = self.conjugate(B,a),b
        return tuple(ans)

    def replace_pair(self,w,i,j,pair):
        z = list(w)
        z[i],z[j] = pair
        return tuple(z)

    def adjacent_to_hub(self,w,i,pair):
        h = len(w)-1
        if i+1 == h:
            return [w,self.replace_pair(w,i,h,pair)]
        z = self.band(w,i+1,h,1)
        path = [w,z]
        if w[i] == w[i+1]:
            middle = next(p for p in self.pair_fiber(z,i,h) if p[0] == pair[0])
            z = self.replace_pair(z,i,h,middle)
        else:
            plus = self.band(w,i,i+1,1)
            sign = 1 if plus[i:i+2] == pair else -1
            z = self.band(z,i,h,sign)
        path.append(z)
        path.append(self.band(z,i+1,h,-1))
        return path

    def hub_to_adjacent(self,w,i,pair):
        h = len(w)-1
        dest = self.replace_pair(w,i,h,pair)
        path = [w]
        z,target = w,dest
        for j in range(i,h-1):
            z = self.band(z,j,j+1,1)
            target = self.band(target,j,j+1,1)
            path.append(z)
        z = self.replace_pair(z,h-1,h,target[h-1:h+1])
        path.append(z)
        for j in reversed(range(i,h-1)):
            z = self.band(z,j,j+1,-1)
            path.append(z)
        return path


def audit_routes(n,L):
    G = Model(n)
    counts = Counter()
    for code,end in enumerate(G.endpoints(L)):
        if end: continue
        w = tuple(G.decode(code,L))
        counts['states'] += 1
        for i in range(L-1):
            for pair in G.pair_fiber(w,i,i+1):
                if pair == w[i:i+2]: continue
                path = G.adjacent_to_hub(w,i,pair)
                assert path[-1] == G.replace_pair(w,i,i+1,pair)
                assert len(path)-1 <= 3
                for a,b in zip(path,path[1:]):
                    assert G.eval(b) == 0
                    changed = [j for j in range(L) if a[j] != b[j]]
                    assert not changed or (len(changed)==2 and changed[-1]==L-1)
                    if changed:
                        j = changed[0]
                        assert (b[j],b[-1]) in G.pair_fiber(a,j,L-1)
                    assert sum(a[j]!=b[j] for j in range(L-2)) <= 1
                    assert G.defects[G.eval(b[:-2])] <= 2
                counts['adjacent_to_hub_paths'] += 1
            for pair in G.pair_fiber(w,i,L-1):
                if pair == (w[i],w[-1]): continue
                path = G.hub_to_adjacent(w,i,pair)
                assert path[-1] == G.replace_pair(w,i,L-1,pair)
                assert len(path)-1 <= 2*L
                for a,b in zip(path,path[1:]):
                    assert G.eval(b) == 0
                    changed = [j for j in range(L) if a[j] != b[j]]
                    assert not changed or (len(changed)==2 and changed[1]==changed[0]+1)
                    if changed:
                        j = changed[0]
                        assert (b[j],b[j+1]) in G.pair_fiber(a,j,j+1)
                counts['hub_to_adjacent_paths'] += 1
    return {'kind':'route_audit','N':n,'L':L,**counts}


def local_fibers(n):
    G = Model(n)
    fibers = defaultdict(list)
    for w in product(range(G.M),repeat=3): fibers[G.eval(w)].append(w)
    stats = []
    for g,words in fibers.items():
        visited = {words[0]}
        todo = [words[0]]
        while todo:
            w = todo.pop()
            for i in (0,1):
                for pair in G.pair_fiber(w,i,2):
                    z = G.replace_pair(w,i,2,pair)
                    assert G.eval(z) == g
                    if z not in visited: visited.add(z);todo.append(z)
        assert len(visited)==len(words)
        stats.append({'endpoint':G.perms[g],'size':len(words)})
    return {'kind':'three_factor_hub_connectivity','N':n,'fibers':stats}


def conditional_audit(n,m):
    G = Model(n)
    ends = G.endpoints(m)
    records = []
    word_count = completion_count = fiber_checks = 0
    legal_hist = Counter()
    endpoint_hist = Counter()
    position = [Counter() for _ in range(m)]
    weights = {}
    # Group by the actual outside coordinates, independently of deletion formula.
    by_coordinate = [defaultdict(list) for _ in range(m)]
    for code,g in enumerate(ends):
        if G.defects[g] > 2: continue
        w = tuple(G.decode(code,m))
        a = len(G.pairs[G.index[G.inverse(G.perms[g])]])
        assert a in (2,3,G.M)
        word_count += 1
        completion_count += a
        weights[w] = a
        endpoint_hist[str(G.types[g])] += 1
        for i,t in enumerate(w):
            by_coordinate[i][w[:i]+w[i+1:]].append((t,a))
            position[i][t] += 1
    assert all(len(set(p.values()))==1 for p in position)
    assert completion_count == G.endpoints(m+2).count(0)
    for i,rows in enumerate(by_coordinate):
        for outside,values in rows.items():
            L = G.perms[G.eval(outside[:i])]
            R = G.perms[G.eval(outside[i:])]
            h = prior.compose(R,L)
            d = n-len(prior.cycles(h))
            assert d in (1,3)
            expected = set(range(G.M)) if d==1 else {
                t for t in range(G.M)
                if G.defects[G.index[prior.compose(G.gates[t],h)]] == 2}
            assert {t for t,a in values} == expected
            assert len(values) in (3,4,6,G.M)
            legal_hist[len(values)] += 1
            total = sum(a for _,a in values)
            # The unweighted exact lift gives conditional gate weights a(g),
            # rather than uniform weights. These sums enumerate all completions.
            assert sum((F(a,total) for _,a in values),F(0)) == 1
            if m==4 and n<=4:
                # Direct selected-triple enumeration checks the projected row
                # independently of the prefix/completion count construction.
                direct = Counter()
                for t,u,v in product(range(G.M),repeat=3):
                    w = outside[:i]+(t,)+outside[i:]+(u,v)
                    if G.eval(w)==0: direct[t] += 1
                assert direct == Counter(dict(values))
            # Uniform legal heat bath has exactly symmetric conditional rows;
            # the lifted conditional has detailed balance with weight a.
            for _,a in values:
                for _,b in values:
                    assert a*F(b,total) == b*F(a,total)
            fiber_checks += 1
    return {'kind':'conditional_lift_audit','N':n,'m':m,'relaxed_words':word_count,
            'exact_extended_words':completion_count,'coordinate_fibers':fiber_checks,
            'legal_set_sizes':dict(legal_hist),'endpoint_types':dict(endpoint_hist),
            'extension_multiplicities':dict(Counter(weights.values()))}


def evaluate_edges(n,w):
    p = list(range(n))
    for a,b in w: p[a],p[b] = p[b],p[a]
    return tuple(p)


def legal_edges(n,w,i):
    ans = []
    for edge in combinations(range(n),2):
        q = evaluate_edges(n,w[:i]+(edge,)+w[i+1:])
        if n-len(prior.cycles(q)) <= 2: ans.append(edge)
    return ans


def heatbath_row(n,w):
    row = Counter({w:F(1,2)})
    for i in range(len(w)):
        legal = legal_edges(n,w,i)
        for edge in legal: row[w[:i]+(edge,)+w[i+1:]] += F(1,2*len(w)*len(legal))
    assert sum(row.values()) == 1
    return row


def hamming_witness(n,m):
    a,b,c = ((0,1),(1,2),(3,4)) if n==5 else ((0,1),(4,5),(2,3))
    small_legal = 4 if n==5 else 3
    x = (a,a)+(c,)*(m-2)
    y = (b,)+x[1:]
    px,py = heatbath_row(n,x),heatbath_row(n,y)
    marginal_tvs = []
    for i in range(m):
        ax,ay = Counter(),Counter()
        for w,p in px.items(): ax[w[i]] += p
        for w,p in py.items(): ay[w[i]] += p
        marginal_tvs.append(sum((abs(ax[t]-ay[t]) for t in ax.keys()|ay.keys()),F(0))/2)
    lower = sum(marginal_tvs,F(0))
    M = n*(n-1)//2
    expected = 1-F(1,2*m)+F(m-2,2*m)*(1-F(small_legal,M))
    assert lower == expected and lower > 1
    return {'kind':'hamming_expansion','N':n,'m':m,
            'initial_distance':1,'marginal_tvs':list(map(str,marginal_tvs)),
            'optimal_one_step_W1':str(lower),
            'x':x,'y':y,'endpoint_defects':[n-len(prior.cycles(evaluate_edges(n,w))) for w in (x,y)]}


def main():
    manifest = {'kind':'manifest','commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                'python':platform.python_version(),'dependencies':'standard library only',
                'command':'python3 -B experiments/20261027-104714-relaxed-heatbath-comparison/check.py',
                'seeds':[],'deterministic':True,
                'sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),PRIOR]}}
    with (HERE/'results.jsonl').open('w') as out:
        def emit(d):
            out.write(json.dumps(d,sort_keys=True)+'\n');out.flush()
            print(json.dumps({k:v for k,v in d.items() if k not in ('fibers','sha256','x','y')},sort_keys=True),flush=True)
        emit(manifest)
        for n,m in [(3,4),(4,4),(4,6),(5,4)]: emit(conditional_audit(n,m))
        for n in (3,4,5): emit(local_fibers(n))
        for n,L in [(3,4),(4,4),(3,6),(4,6),(5,4),(5,6)]:
            start = time.monotonic()
            d = audit_routes(n,L);d['seconds']=time.monotonic()-start;emit(d)
        for n,m in [(5,4),(6,4),(6,6),(8,8),(12,16)]: emit(hamming_witness(n,m))


if __name__=='__main__': main()
