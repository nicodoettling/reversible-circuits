"""Independent full production C2 categorical law; no asymptotic assertion."""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import permutations, product, combinations
import importlib.util, json, os, hashlib, time, platform
HERE=Path(__file__).resolve().parent
TARGET=HERE.parent/'roles/r2-structural/cut_genus_two.py'
spec=importlib.util.spec_from_file_location('target_c2_full',TARGET);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
class Branch(Exception):
 def __init__(self,probs):self.probs=probs
class Trace:
 def __init__(self,tape):self.tape=tape;self.cursor=0;self.prob=F(1)
 def choose(self,items):
  a=[(v,F(w)) for v,w in items if w];assert a and all(w>0 for v,w in a)
  if len(a)==1:return a[0][0]
  total=sum(w for v,w in a)
  if self.cursor==len(self.tape):raise Branch(tuple(w/total for v,w in a))
  j=self.tape[self.cursor];self.cursor+=1;v,w=a[j];self.prob*=w/total;return v
 def randrange(self,n):return self.choose([(i,1) for i in range(n)])
 def shuffle(self,values):values[:]=self.choose([(x,1) for x in sorted(set(permutations(values)))])
def eval_parts(n,w):
 p=list(range(n));parent=list(range(n))
 def root(x):
  while parent[x]!=x:x=parent[x]
  return x
 for a,b in w:p[a],p[b]=p[b],p[a];parent[root(a)]=root(b)
 cycles=0;seen=set()
 for x in range(n):
  if x not in seen:
   cycles+=1;y=x
   while y not in seen:seen.add(y);y=p[y]
 q=len({root(x) for x in range(n)})
 return tuple(p),q,(len(w)-n-cycles+2*q)//2

def literal(n):
 out={};edges=list(combinations(range(n),2));m=2*n+2
 for w in product(edges,repeat=m):
  p,q,g=eval_parts(n,w)
  if p==tuple(range(n)) and q==1:
   js=tuple(j for j in range(1,m) if eval_parts(n,w[:j])[2]==1)
   assert js and g==2
   for j in js:out[w,j]=1
 return out

def law(n):
 started=time.perf_counter();grammar=c.CutGrammar(n)
 pending=[((),F(1))];out=defaultdict(F);nodes=leaves=0;max_depth=0
 saved=(c.choose,c.g01.weighted_choice,c.g01.randbelow)
 try:
  while pending:
   tape,prob=pending.pop();tr=Trace(tape);nodes+=1;max_depth=max(max_depth,len(tape))
   if nodes>500000:raise RuntimeError('explicit execution-node cap reached; incomplete finite check')
   c.choose=lambda items,rng:tr.choose(items)
   c.g01.weighted_choice=lambda rng,values,weights:tr.choose(zip(values,weights))
   c.g01.randbelow=lambda rng,bound:tr.randrange(bound)
   try:w,j=grammar.sample_cut(tr)
   except Branch as b:
    assert tr.prob==prob
    for k,p in enumerate(b.probs):pending.append((tape+(k,),prob*p))
   else:
    assert tr.cursor==len(tape) and tr.prob==prob
    out[tuple(w),j]+=prob;leaves+=1
 finally:c.choose,c.g01.weighted_choice,c.g01.randbelow=saved
 expected=literal(n);total=len(expected)
 assert set(out)==set(expected) and all(p==F(1,total) for p in out.values())
 counts=Counter(w for w,j in out);accepted=defaultdict(F)
 for (w,j),p in out.items():accepted[w]+=p/counts[w]
 acceptance=sum(accepted.values());assert all(p/acceptance==F(1,len(counts)) for p in accepted.values())
 assert acceptance>=F(1,2*n+1)
 law_payload='\n'.join(repr(k)+':'+str(v) for k,v in sorted(out.items()))
 return dict(N=n,words=len(counts),marked_pairs=total,execution_nodes=nodes,execution_leaves=leaves,maximum_decision_depth=max_depth,complete_production_marked_law_uniform=True,corrected_full_word_law_uniform=True,acceptance=str(acceptance),cut_multiplicities=dict(sorted(Counter(counts.values()).items())),law_sha256=hashlib.sha256(law_payload.encode()).hexdigest(),elapsed_seconds=time.perf_counter()-started)
if __name__=='__main__':
 result=dict(status='complete',base_commit='a4e2b9a9b7d68f33165ecc6f18b3f1532f344bec',seed=None,python=platform.python_version(),nonstandard_dependencies=[],sampler_sha256=hashlib.sha256(TARGET.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=[law(n) for n in (2,3)])
 p=HERE/'full-word-law-results-v1.json';tmp=p.with_name(p.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,p)
 print(json.dumps({"status":"complete","cases":[{k:x[k] for k in ('N','words','marked_pairs','execution_nodes','elapsed_seconds')} for x in result['cases']]}))
