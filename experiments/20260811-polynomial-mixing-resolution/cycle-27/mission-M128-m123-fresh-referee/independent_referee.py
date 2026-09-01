#!/usr/bin/env python3
"""No-import exact referee reconstruction for frozen M123.

This independently rebuilds the root-composition law, canonical basins,
frame matrices, centered supplement, contextual-history recursion, and the
literal marked collision.  It imports no predecessor experiment module or
result.  Fractions are exact; floating eigenvalues are diagnostic only.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
import math
import platform
import subprocess
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path


Composition = tuple[int, ...]
State = tuple[int, int, int, int]
Perm = tuple[int, ...]
Edge = tuple[int, int]
Partition = tuple[tuple[int, ...], ...]


def rec(x: F) -> dict[str, str | float]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator), "decimal": float(x)}


def commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


@functools.cache
def weight(n: int) -> F:
    return F(n ** (n - 1), math.factorial(n))


@functools.cache
def compositions(n: int) -> tuple[Composition, ...]:
    if n == 0:
        return ((),)
    return tuple((a,) + tail for a in range(1, n + 1) for tail in compositions(n - a))


def rho(c: Composition) -> F:
    return math.prod(weight(a) for a in c) / (math.factorial(len(c)) * weight(sum(c) + 1))


def active(e: Composition) -> bool:
    return len(e) >= 2 and e[0] + e[1] - 1 >= 2


def in_basin(c: Composition, e: Composition) -> bool:
    return any(sum(c[:cut]) == e[0] and c[cut:] == e[1:] for cut in range(1, len(c) + 1))


def determinant(a: list[list[F]]) -> F:
    b = [row[:] for row in a]
    ans, sign = F(1), 1
    for j in range(len(b)):
        p = next((i for i in range(j, len(b)) if b[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            b[p], b[j] = b[j], b[p]
            sign *= -1
        pivot = b[j][j]
        ans *= pivot
        for i in range(j + 1, len(b)):
            q = b[i][j] / pivot
            for k in range(j + 1, len(b)):
                b[i][k] -= q * b[j][k]
    return sign * ans


def ldl_pivots(a: list[list[F]]) -> list[F]:
    n = len(a)
    lower = [[F(0) for _ in range(n)] for _ in range(n)]
    diag: list[F] = []
    for i in range(n):
        for j in range(i):
            numerator = a[i][j] - sum((lower[i][k] * diag[k] * lower[j][k] for k in range(j)), F(0))
            assert diag[j] != 0 or numerator == 0
            lower[i][j] = numerator / diag[j] if diag[j] else F(0)
        lower[i][i] = F(1)
        diag.append(a[i][i] - sum((lower[i][k] ** 2 * diag[k] for k in range(i)), F(0)))
    return diag


def frame(s: int):
    atoms = compositions(s)
    endpoints = tuple(c for c in atoms if active(c))
    masses = {c: rho(c) for c in atoms}
    assert sum(masses.values(), F(0)) == 1
    capacities = [len(e) * masses[e] for e in endpoints]
    basin_masses = [sum((masses[c] for c in atoms if in_basin(c, e)), F(0)) for e in endpoints]
    overlap = [
        [sum((masses[c] for c in atoms if in_basin(c, e) and in_basin(c, f)), F(0)) for f in endpoints]
        for e in endpoints
    ]
    defect = [[(capacities[i] if i == j else F(0)) - overlap[i][j] for j in range(len(endpoints))] for i in range(len(endpoints))]
    centered_defect = [
        [defect[i][j] + basin_masses[i] * basin_masses[j] for j in range(len(endpoints))]
        for i in range(len(endpoints))
    ]
    return atoms, endpoints, masses, capacities, basin_masses, overlap, defect, centered_defect


def quadratic(a: tuple[F, ...], matrix: list[list[F]]) -> F:
    return sum((a[i] * matrix[i][j] * a[j] for i in range(len(a)) for j in range(len(a))), F(0))


def check_frame() -> dict:
    _, endpoints, _, capacities, basin_masses, overlap, defect, _ = frame(5)
    selected = ((1, 3, 1), (2, 2, 1), (3, 1, 1), (4, 1))
    ix = [endpoints.index(e) for e in selected]
    local_d = [[defect[i][j] for j in ix] for i in ix]
    local_o = [[overlap[i][j] for j in ix] for i in ix]
    local_c = [capacities[i] for i in ix]
    local_b = [basin_masses[i] for i in ix]
    expected = [
        [F(5,108),F(0),F(0),F(-5,216)],
        [F(0),F(35,1296),F(0),F(-25,1296)],
        [F(0),F(0),F(49,1296),F(-41,1296)],
        [F(-5,216),F(-25,1296),F(-41,1296),F(4,81)],
    ]
    assert local_d == expected
    assert determinant(local_d) == F(-27125, 235092492288)
    a = (F(1,2), F(5,7), F(41,49), F(1))
    norm = sum((local_c[i] * a[i] ** 2 for i in range(4)), F(0))
    energy = quadratic(a, local_o)
    defect_energy = quadratic(a, local_d)
    mean = sum((a[i] * local_b[i] for i in range(4)), F(0))
    centered_energy = energy - mean ** 2
    assert defect_energy == F(-155,63504)
    assert norm == F(2094265,6223392)
    assert energy == F(2109455,6223392)
    assert energy / norm == F(421891,418853)
    assert centered_energy / norm == F(223235923,271416744) < 1

    unrestricted_rows=[]
    for s in range(2,6):
        *_, defect_s, _ = frame(s)
        max_size=len(defect_s) if s<=4 else min(3,len(defect_s))
        count=negative=zero=0
        for size in range(1,max_size+1):
            for indices in itertools.combinations(range(len(defect_s)),size):
                minor=determinant([[defect_s[i][j] for j in indices] for i in indices])
                count+=1;negative+=minor<0;zero+=minor==0
        assert negative==0
        unrestricted_rows.append({"s":s,"coordinate_count":len(defect_s),"maximum_minor_size":max_size,"principal_minors_checked":count,"negative_principal_minors":negative,"zero_principal_minors":zero})

    centered_rows = []
    for s in range(2, 6):
        *_, centered = frame(s)
        pivots = ldl_pivots(centered)
        assert all(x >= 0 for x in pivots)
        principal_count = 0
        negative_count = 0
        zero_count = 0
        for size in range(1, len(centered) + 1):
            for indices in itertools.combinations(range(len(centered)), size):
                minor = determinant([[centered[i][j] for j in indices] for i in indices])
                principal_count += 1
                negative_count += minor < 0
                zero_count += minor == 0
        assert negative_count == 0
        centered_rows.append({
            "s": s,
            "coordinate_count": len(centered),
            "ldl_pivots": [rec(x) for x in pivots],
            "principal_minors_checked": principal_count,
            "negative_principal_minors": negative_count,
            "zero_principal_minors": zero_count,
            "full_determinant": rec(determinant(centered)) if centered else rec(F(1)),
        })

    zraw = {
        "111111":-5,"11112":5,"11121":-3,"1113":1,"11211":-4,"1122":3,"1131":-2,
        "12111":-5,"1212":5,"1221":-3,"123":1,"1311":-3,"132":3,"141":-2,
        "21111":-5,"2112":5,"2121":-3,"213":1,"2211":-4,"222":3,"231":-2,
        "3111":-4,"312":4,"321":-2,"411":-3,"42":2,"51":-1,
    }
    z = {tuple(map(int, key)): value for key, value in zraw.items()}
    atoms6, endpoints6, masses6, capacities6, _, _, _, _ = frame(6)
    mean6 = sum((masses6[c] * z.get(c, 0) for c in atoms6), F(0))
    f6 = {c: F(z.get(c, 0)) - mean6 for c in atoms6}
    norm6 = sum((masses6[c] * f6[c] ** 2 for c in atoms6), F(0))
    currents6 = [sum((masses6[c] * f6[c] for c in atoms6 if in_basin(c, e)), F(0)) for e in endpoints6]
    energy6 = sum((currents6[i] ** 2 / capacities6[i] for i in range(len(endpoints6))), F(0))
    quotient6 = energy6 / norm6
    assert mean6 == F(-642,16807)
    assert quotient6 == F(18980340276465329,18038257962480000) > 1

    atoms8, endpoints8, masses8, capacities8, _, _, _, _ = frame(8)
    event_endpoint = (6,2)
    event_mass = sum((masses8[c] for c in atoms8 if in_basin(c,event_endpoint)),F(0))
    f8 = {c:F(in_basin(c,event_endpoint))-event_mass for c in atoms8}
    norm8 = sum((masses8[c]*f8[c]**2 for c in atoms8),F(0))
    currents8 = [sum((masses8[c]*f8[c] for c in atoms8 if in_basin(c,e)),F(0)) for e in endpoints8]
    energy8 = sum((currents8[i]**2/capacities8[i] for i in range(len(endpoints8))),F(0))
    quotient8 = energy8/norm8
    assert event_mass == F(512,6561)
    assert quotient8 == F(128297435442762499633,125986911480783360000)>1
    return {
        "s5_unrestricted": {
            "selected": [list(e) for e in selected], "determinant": rec(determinant(local_d)),
            "defect_energy": rec(defect_energy), "norm": rec(norm), "energy": rec(energy),
            "rayleigh": rec(energy / norm), "witness_mean": rec(mean),
            "same_witness_centered_energy": rec(centered_energy),
            "same_witness_centered_rayleigh": rec(centered_energy / norm),
        },
        "unrestricted_minor_scope":unrestricted_rows,
        "centered_psd_through_s5": centered_rows,
        "s6_centered": {"mean_z": rec(mean6), "norm": rec(norm6), "energy": rec(energy6), "rayleigh": rec(quotient6), "nonzero_z": zraw},
        "s8_centered_bounded_event": {"event_endpoint":list(event_endpoint),"event_mass":rec(event_mass),"norm":rec(norm8),"energy":rec(energy8),"rayleigh":rec(quotient8)},
    }


def choose(n: int, k: int) -> int:
    return math.comb(n,k) if 0 <= k <= n else 0


@functools.cache
def forest(total: int, parts: int) -> F:
    if total == 0 and parts == 0:
        return F(1)
    if not 1 <= parts <= total:
        return F(0)
    return F(parts * total ** (total-parts), total * math.factorial(total-parts))


def split(s: int, b: int) -> F:
    return weight(s+1-b)*weight(b)/weight(s+1)


def mean(k: int, t: int, K: int, R: int, B: int) -> F:
    if t < B:
        return F(0)
    if t == B:
        return F(K*choose(k+K-R-2,K-R-1), choose(k+K-1,K-1))
    return split(t-1,B)*(1-F(choose(K,R+1),choose(K+k,R+1)))


def attach(K: int, R: int, k: int, j: int) -> F:
    return F(choose(R+j,j)*choose(K-R-1+k-j,k-j),choose(K+k,k))


@functools.cache
def groups(s: int):
    out=[]
    for t in range(1,s+1):
        for k in range(1,s+1):
            p=weight(t)*forest(s-t,k-1)/(math.factorial(k)*weight(s+1))
            if p: out.append((k,t,p))
    assert sum((p for _,_,p in out),F(0))==1
    return tuple(out)


@functools.cache
def success(x: State) -> F:
    s,K,R,B=x; ans=F(0)
    for k,t,p in groups(s):
        if t<B: continue
        if t==B: ans += p*mean(k,t,K,R,B); continue
        for j in range(1,k+1):
            nu=attach(K,R,k,j)
            if nu: ans += p*nu*success((t-1,K+k,R+j,B))
    assert ans==split(s,B)
    return ans


def alpha(s: int) -> F:
    return F(1) if s<2 else F(2,3*s*(s-1))


@functools.cache
def wrong_success(x: State, direction: str) -> F:
    s,K,R,B=x; ans=F(0)
    for k,t,p in groups(s):
        if t<B: continue
        if t==B: ans += p*mean(k,t,K,R,B); continue
        for j in range(1,k+1):
            nu=attach(K,R,k,j)
            if not nu: continue
            child=(t-1,K+k,R+j,B)
            factor=F(1) if child[0]<2 else (alpha(child[0])/alpha(s) if direction=="child_over_parent" else alpha(s)/alpha(child[0]))
            ans += p*nu*factor*wrong_success(child,direction)
    return ans


def basin_energy(x: State):
    s,K,R,B=x; q=split(s,B); masses={c:rho(c) for c in compositions(s)}
    means={c:mean(len(c),c[-1],K,R,B) for c in compositions(s)}
    theta={}
    cap={}
    for e in compositions(s):
        if not active(e): continue
        theta[e]=sum((masses[c]*(means[c]-q) for c in compositions(s) if in_basin(c,e)),F(0))
        cap[e]=len(e)*masses[e]
    A0=sum((theta[e]**2/cap[e] for e in theta),F(0))
    assigned={e:F(0) for e in theta}
    for c in compositions(s):
        e=c
        while len(e)>=2 and not active(e): e=(e[0]+e[1],)+e[2:]
        if len(e)>=2: assigned[e]+=masses[c]*(means[c]-q)
    first=sum((assigned[e]**2/cap[e] for e in assigned),F(0))
    signed=sum((theta[e]*theta[e]/cap[e] for e in theta),F(0))
    assert signed==A0
    return q,means,theta,cap,A0,first,assigned


@functools.cache
def reset_energy(x: State) -> F:
    return basin_energy(x)[4]


@functools.cache
def signed_reset_energy(x: State) -> F:
    s,K,R,B=x; q=split(s,B); masses={c:rho(c) for c in compositions(s)}
    means={c:mean(len(c),c[-1],K,R,B) for c in compositions(s)}
    answer=F(0)
    for e in compositions(s):
        if not active(e): continue
        capacity=len(e)*masses[e]
        # This is the exact ordered two-copy sum, evaluated after independent
        # accumulation of its left and right copies rather than materializing
        # every pair.  Distributivity is the universal signed-frame identity.
        left=sum((masses[c]*(means[c]-q) for c in compositions(s) if in_basin(c,e)),F(0))
        right=sum((masses[d]*(means[d]-q) for d in compositions(s) if in_basin(d,e)),F(0))
        answer += left*right/capacity
    return answer


@functools.cache
def energy_children(x: State):
    s,K,R,B=x; phase=s+K-R; out=[]
    for k,t,p in groups(s):
        assert sum((attach(K,R,k,j) for j in range(k+1)),F(0))==1
        if t<=B or t-1<2: continue
        for j in range(1,k+1):
            nu=attach(K,R,k,j)
            if nu:
                child=(t-1,K+k,R+j,B)
                assert child[0]+child[1]-child[2]<phase
                out.append((p*nu,child,k,j))
    return tuple(out)


@functools.cache
def resolvent(x: State) -> F:
    return reset_energy(x)+sum((p*resolvent(y) for p,y,_,_ in energy_children(x)),F(0))


@functools.cache
def signed_resolvent(x: State) -> F:
    return signed_reset_energy(x)+sum((p*signed_resolvent(y) for p,y,_,_ in energy_children(x)),F(0))


def check_history() -> dict:
    mass_checks=0
    signed_checks=0
    right_heavy_failures=0
    right_heavy_worst=None
    attachment_labels=set()
    for s in range(2,11):
        for K in (1,2,5):
            for B in range(1,s+1):
                x=(s,K,K-1,B); qx=split(s,B); value=resolvent(x)
                assert success(x)==qx; mass_checks+=1
                assert signed_resolvent(x)==value; signed_checks+=1
                right_heavy_failures += value>qx*(1-qx)
                ratio=value/(qx*(1-qx))
                if right_heavy_worst is None or ratio>right_heavy_worst[0]: right_heavy_worst=(ratio,x)
                for _,_,k,j in energy_children(x): attachment_labels.add((k,j))
    assert right_heavy_failures==0
    multitype_checks=0
    multitype_failures=0
    multitype_worst=None
    for s in range(2,9):
        for K in range(1,7):
            for R in range(K):
                if R==0 and K!=1: continue
                for B in range(1,s+1):
                    x=(s,K,R,B);qx=split(s,B);value=resolvent(x);target=(K-R)*qx*(1-qx)
                    assert signed_resolvent(x)==value; signed_checks+=1; multitype_checks+=1
                    multitype_failures += value>target
                    ratio=value/target
                    if multitype_worst is None or ratio>multitype_worst[0]:multitype_worst=(ratio,x)
                    for _,_,k,j in energy_children(x): attachment_labels.add((k,j))
    assert multitype_failures==0
    x=(4,1,0,1); q,means,theta,cap,A0,first,assigned=basin_energy(x); source=(1,1,1,1)
    assert means[source]==1 and rho(source)==F(1,125)
    assert theta[(3,1)]==F(1647,15625)
    assert assigned[(3,1)]==F(1098,15625)
    assert A0==F(1351279,28125000)
    assert first==F(748477,28125000)
    assert wrong_success((3,1,0,1),"child_over_parent")==F(15,16)
    assert wrong_success((3,1,0,1),"parent_over_child")==F(7,16)
    return {"mass_states_checked":mass_checks,"signed_resolvent_checks":signed_checks,
            "right_heavy_failure_count":right_heavy_failures,"right_heavy_worst":{"state":list(right_heavy_worst[1]),"ratio":rec(right_heavy_worst[0])},
            "multitype_checks":multitype_checks,"multitype_failure_count":multitype_failures,"multitype_worst":{"state":list(multitype_worst[1]),"ratio":rec(multitype_worst[0])},
            "attachment_labels_seen":[list(x) for x in sorted(attachment_labels)],
            "collision_state":list(x),"source":list(source),"source_mass":rec(rho(source)),"q":rec(q),
            "active_endpoints":[[2,1,1],[3,1]],"later_current":rec(theta[(3,1)]),"first_edge_later_current":rec(assigned[(3,1)]),"A0":rec(A0),"first_edge_energy":rec(first),
            "extra_alpha_child_over_parent":rec(F(15,16)),"extra_alpha_parent_over_child":rec(F(7,16))}


def compose(p: Perm,q: Perm)->Perm: return tuple(p[q[x]] for x in range(len(p)))
def inverse(p: Perm)->Perm:
    out=[0]*len(p)
    for x,y in enumerate(p): out[y]=x
    return tuple(out)
def transposition(n:int,e:Edge)->Perm:
    p=list(range(n));p[e[0]],p[e[1]]=p[e[1]],p[e[0]];return tuple(p)
def normalize(blocks:list[set[int]])->Partition:return tuple(sorted(tuple(sorted(b)) for b in blocks))
def partition_perm(partition:Partition)->Perm:
    p=list(range(sum(map(len,partition))))
    for b in partition:
        if len(b)>1:
            for x,y in zip(b,b[1:]+b[:1]):p[x]=y
    return tuple(p)
def inverse_chain(labels:tuple[int,...])->tuple[Partition,...]:
    if not labels:return (((0,),),)
    largest=max(labels);pos=max(i for i,x in enumerate(labels) if x==largest);small=inverse_chain(labels[:pos]+labels[pos+1:]);new=largest+1;out=[]
    for rank in range(len(labels)+1):
        blocks=[{x if x<=largest else x+1 for x in b} for b in small[rank if rank<=pos else rank-1]]
        if rank<=pos:blocks.append({new})
        else:next(b for b in blocks if largest in b).add(new)
        out.append(normalize(blocks))
    return tuple(out)
def factor_word(chain:tuple[Partition,...])->tuple[Edge,...]:
    ans=[]
    for i in range(1,len(chain)):
        q=compose(inverse(partition_perm(chain[i-1])),partition_perm(chain[i]));m=[x for x,y in enumerate(q) if x!=y];assert len(m)==2;ans.append(tuple(m))
    return tuple(ans)
def root_comp(macro:tuple[int,...])->tuple[int,...]:
    deg=[macro.count(i) for i in range(len(macro))]+[0];children=[[] for _ in deg];stack=[[0,deg[0]]]
    for v in range(1,len(deg)):
        while stack and stack[-1][1]==0:stack.pop()
        children[stack[-1][0]].append(v);stack[-1][1]-=1;stack.append([v,deg[v]])
    def size(v):return 1+sum(size(u) for u in children[v])
    return tuple(size(u) for u in children[0])


def check_literal() -> dict:
    n=6;r=5;macro=(0,1,1,1,1);edges=tuple((a,b) for a in range(n) for b in range(a+1,n));ei={e:i for i,e in enumerate(edges)};perms=[transposition(n,e) for e in edges];fibers=defaultdict(list)
    for i,p in enumerate(perms):
        for j,q in enumerate(perms):fibers[compose(p,q)].append((i,j))
    words=[]
    for labels in itertools.product(range(r),repeat=r):
        if tuple(sorted(labels))!=macro or any(x>i for i,x in enumerate(sorted(labels))):continue
        ew=factor_word(inverse_chain(labels));words.append((labels,tuple(ei[e] for e in ew)))
    assert len(words)==5 and root_comp(macro)==(5,)
    marks=[];rate=F(0);fiber_sizes=set()
    for labels,word in words:
        for scan in range(r-1):
            fiber=fibers[compose(perms[word[scan]],perms[word[scan+1]])];fiber_sizes.add(len(fiber))
            for oi,(a,b) in enumerate(fiber):
                target=word[:scan]+(a,b)+word[scan+2:];tm=tuple(sorted(edges[i][0] for i in target))
                if root_comp(tm)==(4,1):
                    rate+=F(1,len(words)*(r-1)*len(fiber));marks.append({"labels":list(labels),"scan":scan,"outcome":oi,"target_macro":list(tm)})
    assert len(marks)==2 and rate==F(1,30) and fiber_sizes=={2,3}
    return {"source_word_count":len(words),"scan_count_per_word":4,"fiber_sizes":sorted(fiber_sizes),"favourable_mark_count":len(marks),"favourable_rate":rec(rate),"marks":marks}


def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True);args=ap.parse_args()
    payload={"status":"accept_with_scope_supplement","repository_commit":commit(),"python":platform.python_version(),"seed":None,"dependencies":{},"arithmetic":"fractions.Fraction exact","convention":"(pq)(x)=p(q(x)); factors displayed left-to-right","frame":check_frame(),"history":check_history(),"literal_collision":check_literal(),
             "pullback_audit":{"full_probability_marginal":"If kappa_*mu=rho, f->f composed kappa is isometric and preserves the O/c Gram matrix.","success_weighted":"The pushforward rho(C)h(C) instead gives O^succ and is not the same operator.","cross_prefix":"Requires joint prefix intersections; the aggregate recursion does not compute them."},
             "scope":"No all-L contraction, gap, mixing, Terminal A, or Terminal B inference."}
    encoded=json.dumps(payload,indent=2,sort_keys=True)+"\n";args.output.write_text(encoded);print(json.dumps({"output":str(args.output),"sha256":hashlib.sha256(encoded.encode()).hexdigest(),"status":payload["status"]},sort_keys=True))


if __name__=="__main__":main()
