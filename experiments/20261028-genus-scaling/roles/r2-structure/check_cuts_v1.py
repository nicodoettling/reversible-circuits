"""Exact bounded-state checks for penultimate genus cuts. No word enumeration."""
from __future__ import annotations
import argparse, datetime, hashlib, json, math, os, platform, time
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path

BASE_COMMIT = 'b178daf320833e859dcdee0ce56eb16c6d2130b7'

def step_perm(p, edge):
    q = list(p); a,b=edge; q[a],q[b]=q[b],q[a]; return tuple(q)

def inverse(p):
    q=[0]*len(p)
    for i,a in enumerate(p): q[a]=i
    return tuple(q)

@lru_cache(None)
def cycles(p):
    seen=set(); answer=[]
    for i in range(len(p)):
        if i in seen: continue
        cyc=[]; j=i
        while j not in seen:
            cyc.append(j); seen.add(j); j=p[j]
        answer.append(tuple(cyc))
    return tuple(answer)

def weighted_step(blocks, edge):
    a,b=edge; ia=next(i for i,(s,k) in enumerate(blocks) if (s>>a)&1)
    ib=next(i for i,(s,k) in enumerate(blocks) if (s>>b)&1)
    out=list(blocks)
    if ia==ib:
        mask,length=out[ia];out[ia]=(mask,length+1)
    else:
        mask=out[ia][0]|out[ib][0]; length=out[ia][1]+out[ib][1]+1
        out=[x for i,x in enumerate(out) if i not in (ia,ib)];out.append((mask,length))
    return tuple(sorted(out))

def genus(n,length,p,blocks):
    z=length-n-len(cycles(p))+2*len(blocks)
    assert z>=0 and z%2==0
    return z//2

def partitions(n):
    out=[()]
    for a in range(n):
        nxt=[]
        for bs in out:
            nxt.append(bs+(1<<a,))
            for i in range(len(bs)):
                nxt.append(bs[:i]+(bs[i]|(1<<a),)+bs[i+1:])
        out=nxt
    return out

def connected_reference(n,maxlen):
    """Partition-lattice inversion of unrestricted subgroup endpoint walks."""
    ident=tuple(range(n)); result=[Counter() for _ in range(maxlen+1)]
    ordinary=None
    for bs in partitions(n):
        coefficient=(-1)**(len(bs)-1)*math.factorial(len(bs)-1)
        edges=[(a,b) for a,b in combinations(range(n),2)
               if any((s>>a)&1 and (s>>b)&1 for s in bs)]
        row=Counter({ident:1})
        for ell in range(maxlen+1):
            for p,num in row.items():result[ell][p]+=coefficient*num
            if len(bs)==1 and ell==maxlen: pass
            nxt=Counter()
            for p,num in row.items():
                for e in edges:nxt[step_perm(p,e)]+=num
            row=nxt
    row=Counter({ident:1});ordinary=[]
    for ell in range(maxlen+1):
        ordinary.append(row)
        nxt=Counter()
        for p,num in row.items():
            for e in combinations(range(n),2):nxt[step_perm(p,e)]+=num
        row=nxt
    assert all(v>=0 for row in result for v in row.values())
    return result,ordinary

def weighted_tables(n,maxlen):
    ident=tuple(range(n)); blocks=tuple((1<<i,0) for i in range(n))
    rows=[Counter({(ident,blocks):1})]; edges=list(combinations(range(n),2))
    for ell in range(maxlen):
        nxt=Counter()
        for (p,bs),num in rows[-1].items():
            oldg=genus(n,ell,p,bs)
            for e in edges:
                q=step_perm(p,e);cs=weighted_step(bs,e)
                assert genus(n,ell+1,q,cs)-oldg in (0,1)
                nxt[q,cs]+=num
        rows.append(nxt)
    return rows

def local_spec(p,block):
    mask,ell=block; labels=[i for i in range(len(p)) if (mask>>i)&1]
    pos={a:i for i,a in enumerate(labels)}
    q=tuple(pos[p[a]] for a in labels)
    h=(ell-len(labels)-len(cycles(q))+2)//2
    assert ell==len(labels)+len(cycles(q))-2+2*h and h>=0
    return len(labels),ell,q,h

def macro_graph(p,left,right):
    edges=[]
    for cyc in cycles(p):
        a=cyc[0]
        li=next(i for i,(s,k) in enumerate(left) if (s>>a)&1)
        ri=next(i for i,(s,k) in enumerate(right) if (s>>a)&1)
        edges.append((li,len(left)+ri,len(cyc)))
    vertices=len(left)+len(right);neighbors=[[] for _ in range(vertices)]
    for i,(a,b,c) in enumerate(edges):neighbors[a].append((b,i));neighbors[b].append((a,i))
    seen={0};todo=[0]
    while todo:
        for v,e in neighbors[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==vertices,edges,neighbors

def core_stats(edges,neighbors):
    alive=set(range(len(edges))); degree=[len(x) for x in neighbors]
    queue=[i for i,d in enumerate(degree) if d<=1]
    while queue:
        v=queue.pop()
        for u,e in neighbors[v]:
            if e not in alive:continue
            alive.remove(e);degree[v]-=1;degree[u]-=1
            if degree[u]==1:queue.append(u)
    verts={v for e in alive for v in edges[e][:2]}
    return alive,verts,degree

def plateau_histogram(n,g,m):
    ident=tuple(range(n));initial=tuple((1<<i,0) for i in range(n))
    row=Counter({(ident,initial,0):1});edges=list(combinations(range(n),2))
    peaks=[]
    for ell in range(1,m+1):
        nxt=Counter()
        for (p,bs,d),num in row.items():
            for e in edges:
                q=step_perm(p,e);cs=weighted_step(bs,e)
                add=int(ell<m and genus(n,ell,q,cs)==g-1)
                nxt[q,cs,d+add]+=num
        row=nxt;peaks.append(len(row))
    hist=Counter()
    for (p,bs,d),num in row.items():
        if p==ident and len(bs)==1:hist[d]+=num
    assert hist and min(hist)>=1 and max(hist)<=2*n-2
    return hist,max(peaks)

def check_case(n,g,tables,reference):
    m=2*n-2+2*g;ident=tuple(range(n));target=reference[n][0][m][ident]
    out=dict(N=n,g=g,m=m,connected_words=target)
    if g<2:return out
    rows=tables[n];marked=0;macro_count=0;types=Counter();by_j=Counter();parallel_macros=0
    for j in range(1,m):
        lgroup=defaultdict(list);rgroup=defaultdict(list)
        for (p,bs),num in rows[j].items():
            if genus(n,j,p,bs)==g-1:lgroup[p].append((bs,num))
        for (p,bs),num in rows[m-j].items():rgroup[p].append((bs,num))
        for p,litems in lgroup.items():
            for left,lnum in litems:
                for right,rnum in rgroup[inverse(p)]:
                    connected,edges,neighbors=macro_graph(p,left,right)
                    if not connected:continue
                    beta=len(edges)-len(left)-len(right)+1
                    gl=genus(n,j,p,left);gr=genus(n,m-j,inverse(p),right)
                    assert g==gl+gr+beta and (gr,beta) in ((1,0),(0,1))
                    assert j==n+len(right)-len(left)+beta+2*g-3
                    # Independent connected endpoint reference -> full literal macro mass.
                    expected=math.factorial(j)*math.factorial(m-j)
                    denominator=1;left_h=[]
                    for endpoint,bs in ((p,left),(inverse(p),right)):
                        for block in bs:
                            v,ell,q,h=local_spec(endpoint,block)
                            expected*=reference[v][0][ell][q];denominator*=math.factorial(ell)
                            if endpoint is p:left_h.append(h)
                    assert expected%denominator==0
                    expected//=denominator
                    assert expected==lnum*rnum
                    assert sum(local_spec(p,b)[3] for b in left)==g-1
                    root_total=sum((Fraction(local_spec(p,b)[3],g-1) for b in left),Fraction())
                    assert root_total==1
                    if beta==1:
                        alive,verts,degrees=core_stats(edges,neighbors)
                        assert len(alive)==len(verts) and len(alive)%2==0
                        assert all(degrees[v]==2 for v in verts)
                        # Core start/direction codes are incidence-distinct, also in the digon.
                        code_count=sum(degrees[v] for v in verts if v<len(left))
                        assert code_count==len(alive)
                        if len(alive)==2:parallel_macros+=1
                    count=lnum*rnum;marked+=count;macro_count+=1;types[gr,beta]+=count;by_j[j]+=count
    hist,peak=plateau_histogram(n,g,m)
    assert sum(hist.values())==target
    assert sum(d*num for d,num in hist.items())==marked
    assert Fraction(target,marked)>=Fraction(1,2*n-2)
    out.update(marked_pairs=marked,macros=macro_count,parallel_core_macros=parallel_macros,
        plateau_histogram={str(k):v for k,v in sorted(hist.items())},
        cut_totals={str(k):v for k,v in sorted(by_j.items())},
        types=[dict(right_genus=r,beta=b,count=c) for (r,b),c in sorted(types.items())],
        acceptance=str(Fraction(target,marked)),peak_plateau_states=peak,
        full_macro_factorization=True,root_genus_weights_sum_one=True)
    return out

def regressions(reference):
    baseline=[]
    for n,m,want in ((2,0,1),(2,1,0),(2,2,1),(3,4,27),(4,4,120),(4,6,3936)):
        got=reference[n][1][m][tuple(range(n))];assert got==want
        baseline.append(dict(N=n,m=m,ordinary_identity_words=got))
    p=(1,0,2);ordinary=reference[3][1][5][p];connected=reference[3][0][5][p]
    assert (ordinary,connected)==(81,80)
    word=((0,1),(1,2))*3;p=tuple(range(3))
    for e in word:p=step_perm(p,e)
    assert p==tuple(range(3)) and all(a!=b for a,b in zip(word,word[1:]))
    edges=list(combinations(range(3),2)); row=Counter({(tuple(range(3)),0):1})
    for _ in range(6):
        nxt=Counter()
        for (p,mask),num in row.items():
            for i,e in enumerate(edges):nxt[step_perm(p,e),mask|(1<<i)]+=num
        row=nxt
    triangle=row[(tuple(range(3)),7)];connected6=reference[3][0][6][tuple(range(3))]
    assert Fraction(triangle,connected6)==Fraction(3,4)
    a=Fraction(21,2000);c=Fraction(1,20);d=Fraction(879,1000);gamma=Fraction(1,10)
    assert 2*a+2*c+d==1 and a>gamma**2 and Fraction(21,221)<gamma
    # Exactly the support-restriction/renormalization witness, not a product bound.
    return dict(baselines=baseline,endpoint81_80=[ordinary,connected],zero_square_witness=list(word),
        triangle_target_fraction='3/4',unweighted_graph_fraction='1/4',
        cp1=dict(initial_x='1/10',initial_e='121/2000',initial_f='21/2000',
                 joint=str(a),false_marginal_product=str(gamma**2),posterior_f='21/221',
                 support_restriction_failure_retained=True),
        low_genus_mass_obstruction='M-GROW retained as source-scoped input; no policy claim tested here')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic();maxlen=12
    reference={n:connected_reference(n,maxlen) for n in range(1,5)}
    tables={n:weighted_tables(n,maxlen) for n in range(2,5)}
    states_checked=0
    for n,rows in tables.items():
        ident=tuple(range(n));full=(1<<n)-1
        for ell,row in enumerate(rows):
            for p in reference[n][1][ell]:
                assert row[(p,((full,ell),))]==reference[n][0][ell][p]
                states_checked+=1
    cases=[check_case(n,g,tables,reference) for n in range(2,5) for g in range(4)]
    result=dict(status='complete',base_commit=BASE_COMMIT,python=platform.python_version(),
        nonstandard_dependencies=[],deterministic_seeds=None,method='exact quotient/weighted-support DP and independent partition inversion',
        no_literal_word_enumeration=True,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        reference_cells_checked=states_checked,weighted_state_peaks={str(n):max(map(len,rs)) for n,rs in tables.items()},
        regressions=regressions(reference),cases=cases,elapsed_seconds=time.monotonic()-start)
    out=Path(args.output);tmp=out.with_name(out.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,out)
    print(json.dumps(dict(status=result['status'],cases=len(cases),elapsed_seconds=result['elapsed_seconds'],output=str(out))))

if __name__=='__main__':main()
