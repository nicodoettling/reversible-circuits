"""Nonauthor integrated g4 suffix-cylinder audit. Only run with reservation."""
from __future__ import annotations
import argparse, datetime, hashlib, importlib.util, json, math, os, platform, sys, time
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
spec=importlib.util.spec_from_file_location('r2_integrated_reference',ROOT/'coordinator/integrated_sampler_v1.py')
I=importlib.util.module_from_spec(spec);sys.modules[spec.name]=I;spec.loader.exec_module(I)
S=I.decoder

def compose_right(p,edge):
    a,b=edge
    return tuple(p[b] if j==a else p[a] if j==b else p[j] for j in range(len(p)))

def merge_blocks(blocks,edge):
    a,b=blocks[edge[0]],blocks[edge[1]]
    merged=tuple(min(a,b) if x in (a,b) else x for x in blocks)
    labels={x:i for i,x in enumerate(sorted(set(merged)))}
    return tuple(labels[x] for x in merged)

def partition_dp(n,maximum):
    row={(tuple(range(n)),tuple(range(n))):1};result=[row]
    for ell in range(maximum):
        nxt=defaultdict(int)
        for (p,blocks),num in row.items():
            for e in combinations(range(n),2):
                nxt[compose_right(p,e),merge_blocks(blocks,e)]+=num
        row=dict(nxt);result.append(row)
    return result

def ctype(p):
    seen=set();sizes=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;size=0
        while j not in seen:seen.add(j);size+=1;j=p[j]
        sizes.append(size)
    return tuple(sorted(sizes))

@lru_cache(None)
def assignments(lengths,ga,gb):
    """Exact joint law of actual production forced-normalizer decisions."""
    row=[({0:0,1:1},Fraction(1))]
    for i in range(2,len(lengths)):
        nxt=[]
        for forced,prob in row:
            parent=S.allocation_mass(lengths,ga,gb,forced)
            weights=[S.allocation_mass(lengths,ga,gb,forced|{i:b}) for b in (0,1)]
            assert parent>0 and sum(weights)==parent
            for b,w in enumerate(weights):
                if w:nxt.append((forced|{i:b},prob*Fraction(w,parent)))
        row=nxt
    result=tuple((tuple(forced[i] for i in range(len(lengths))),prob) for forced,prob in row)
    assert sum(p for a,p in result)==1
    return result

@lru_cache(None)
def suffix_law(p,g,t):
    """Use production branch/assignment masses; derive only terminal cylinders."""
    r=len(p)+len(ctype(p))-2+2*g
    if t==0:return {():Fraction(1)}
    assert 0<t<=r
    total=S.count(ctype(p),g);out=defaultdict(Fraction)
    for branch in S.branches(p,g):
        bp=Fraction(branch.weight,total)
        if branch.kind=='connected':
            for word,prob in suffix_law(branch.endpoint,branch.child_genus,t-1).items():
                out[word+(branch.edge,)]+=bp*prob
            continue
        lengths=tuple(map(len,branch.cut_cycles))
        for assignment,ap in assignments(lengths,branch.ga,branch.gb):
            aa=tuple(sorted(x for cyc,b in zip(branch.cut_cycles,assignment) if b==0 for x in cyc))
            bb=tuple(sorted(x for cyc,b in zip(branch.cut_cycles,assignment) if b==1 for x in cyc))
            amap={x:i for i,x in enumerate(aa)};bmap={x:i for i,x in enumerate(bb)}
            pa=tuple(amap[branch.endpoint[x]] for x in aa)
            pb=tuple(bmap[branch.endpoint[x]] for x in bb)
            ra=len(aa)+len(ctype(pa))-2+2*branch.ga
            rb=len(bb)+len(ctype(pb))-2+2*branch.gb
            L=ra+rb;assert L==r-1
            for colors in product((0,1),repeat=t-1):
                ka=colors.count(0);kb=t-1-ka
                if ka>ra or kb>rb:continue
                shuffle=Fraction(math.comb(L-t+1,ra-ka),math.comb(L,ra))
                la=suffix_law(pa,branch.ga,ka);lb=suffix_law(pb,branch.gb,kb)
                for wa,qa in la.items():
                    labeled_a=tuple(tuple(sorted((aa[x],aa[y]))) for x,y in wa)
                    for wb,qb in lb.items():
                        labeled_b=tuple(tuple(sorted((bb[x],bb[y]))) for x,y in wb)
                        ia=ib=0;word=[]
                        for color in colors:
                            if color==0:word.append(labeled_a[ia]);ia+=1
                            else:word.append(labeled_b[ib]);ib+=1
                        out[tuple(word)+(branch.edge,)]+=bp*ap*shuffle*qa*qb
    answer=dict(out)
    assert sum(answer.values())==1
    return answer

def reference_suffixes(n,rows,m,t):
    """Append each fixed terminal word to every exact prefix quotient state."""
    answer=defaultdict(lambda:defaultdict(int));edges=tuple(combinations(range(n),2))
    for word in product(edges,repeat=t):
        for (p,blocks),num in rows[m-t].items():
            q=p;cs=blocks
            for edge in word:q=compose_right(q,edge);cs=merge_blocks(cs,edge)
            if cs==(0,)*n:answer[q][word]+=num
    return {p:dict(v) for p,v in answer.items()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic();assert sorted(S.SPECS)==[0,1]
    I.prepare(4)
    assert [len(S.SPECS[g]) for g in (2,3,4)]==[6,26,85]
    records=[];cylinder_count=0;peak=0;digests=[]
    for n,t in ((3,4),(4,3)):
        g=4;maximum=2*n-2+2*g;rows=partition_dp(n,maximum)
        peak=max(peak,max(map(len,rows)))
        references={m:reference_suffixes(n,rows,m,t) for m in sorted({n+len(ctype(p))-2+2*g for p in permutations(range(n))})}
        for p in permutations(range(n)):
            m=n+len(ctype(p))-2+2*g
            direct=references[m][p];total=rows[m][p,(0,)*n]
            law=suffix_law(p,g,t)
            assert set(law)==set(direct),(n,p,'support mismatch')
            assert all(prob==Fraction(direct[word],total) for word,prob in law.items()),(n,p,'law mismatch')
            assert sum(direct.values())==total
            cylinder_count+=len(direct)
            digest=hashlib.sha256(repr(sorted(direct.items())).encode()).hexdigest()
            digests.append(digest)
            records.append(dict(N=n,g=g,endpoint=list(p),length=m,suffix_length=t,
                connected_words=total,positive_cylinders=len(direct),reference_law_sha256=digest,
                all_exact_joint_probabilities_equal_reference=True))
    # Different repeated-length/non-prefix forcing profile at genus split(2,2).
    lengths=(1,1,1,1,2);ga=gb=2
    direct=[]
    for tail in product((0,1),repeat=3):
        assignment=(0,1)+tail
        aa=tuple(a for a,b in zip(lengths,assignment) if b==0)
        bb=tuple(a for a,b in zip(lengths,assignment) if b==1)
        la=sum(aa)+len(aa)-2+2*ga;lb=sum(bb)+len(bb)-2+2*gb
        # Independent connected counts by anchored source quotient, rather than marker code.
        ca=I.coefficient.connected(tuple(sorted(aa)),la)
        cb=I.coefficient.connected(tuple(sorted(bb)),lb)
        direct.append((assignment,math.comb(la+lb,la)*ca*cb))
    forcing=0;zero_forcing=0
    for tail in product((-1,0,1),repeat=3):
        forced={0:0,1:1}|{i+2:b for i,b in enumerate(tail) if b>=0}
        expected=sum(w for a,w in direct if all(a[i]==b for i,b in forced.items()))
        got=S.allocation_mass(lengths,ga,gb,forced)
        assert got==expected;forcing+=1;zero_forcing+=expected==0
    result=dict(status='passed',generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        python=platform.python_version(),nonstandard_dependencies=[],seeds=None,
        base_commit='b178daf320833e859dcdee0ce56eb16c6d2130b7',
        purpose='independent exact integrated g4 joint suffix laws, not full word enumeration',
        generated_term_counts={str(g):len(S.SPECS[g]) for g in (2,3,4)},
        endpoint_cases=len(records),positive_suffix_cylinders=cylinder_count,records=records,
        joint_reference_sha256=hashlib.sha256(''.join(digests).encode()).hexdigest(),
        new_forcing_profile=list(lengths),new_forcing_genus_pair=[ga,gb],forced_cases=forcing,zero_forced_cases=zero_forcing,
        peak_reference_states=peak,elapsed_seconds=time.monotonic()-start,
        sources_sha256={str(Path(p)):hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in (__file__,I.__file__,S.__file__,I.coefficient.__file__)},
        limitations=['finite joint marginal law, not every full N4 word','same-model nonblind review','universal source and complexity proved separately'])
    out=Path(args.output);tmp=out.with_name(out.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,out)
    print(json.dumps({k:result[k] for k in ('status','endpoint_cases','positive_suffix_cylinders','forced_cases','elapsed_seconds')}))

if __name__=='__main__':main()
