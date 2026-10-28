from collections import Counter
from fractions import Fraction as F
from itertools import combinations,product
from math import factorial,comb
from pathlib import Path
import datetime,hashlib,json,os,platform,time

ROOT=Path(__file__).resolve().parent

def evaluate(n,w):
 p=list(range(n))
 for a,b in w:p[a],p[b]=p[b],p[a]
 return tuple(p)

def cycles(p):
 seen=set();out=[]
 for x in range(len(p)):
  if x in seen:continue
  cyc=[];y=x
  while y not in seen:seen.add(y);cyc.append(y);y=p[y]
  out.append(tuple(cyc))
 return tuple(out)

def components(n,w):
 part=[{x} for x in range(n)]
 for a,b in w:
  A=next(x for x in part if a in x);B=next(x for x in part if b in x)
  if A is not B:A.update(B);part.remove(B)
 return tuple(sorted(tuple(sorted(x)) for x in part))

def side(n,w,p=None):
 if p is None:p=evaluate(n,w)
 cyc=cycles(p);out=[]
 for block in components(n,w):
  bs=set(block);alpha=tuple(len(c) for c in cyc if c[0] in bs)
  ell=sum(a in bs for a,b in w)
  twice=ell-len(block)-len(alpha)+2
  assert twice>=0 and twice%2==0
  out.append((block,twice//2,alpha,ell))
 return tuple(out)

def normalized_count(alpha,g):
 v=sum(alpha);k=len(alpha);q=F(1)
 for a in alpha:q*=F(a**a,factorial(a-1))
 if g==0:return q*F(v)**(k-3)
 assert g==1
 e=[1]+[0]*k
 for a in alpha:
  for j in range(k,0,-1):e[j]+=a*e[j-1]
 bracket=F(v)**k-F(v)**(k-1)
 for j in range(2,k+1):bracket-=factorial(j-2)*F(v)**(k-j)*e[j]
 return q*bracket/24

def macros_case(n,m):
 edges=tuple(combinations(range(n),2));direct=Counter();weight={};dist=Counter();coverage=0;words=0;zero_squares=0;triangle=0
 for w in product(edges,repeat=m):
  if evaluate(n,w)!=tuple(range(n)) or len(components(n,w))!=1:continue
  words+=1;valid=0
  for j in range(1,m):
   p=evaluate(n,w[:j]);left=side(n,w[:j],p);gl=sum(x[1] for x in left)
   if gl!=1:continue
   right=side(n,w[j:]);gr=sum(x[1] for x in right)
   E=len(cycles(p));V=len(left)+len(right);beta=E-V+1
   assert gr in (0,1) and beta in (0,1) and 2==gl+gr+beta
   key=(j,p,tuple((b,g) for b,g,_,_ in left),tuple((b,g) for b,g,_,_ in right))
   wgt=F(factorial(j)*factorial(m-j))
   for _,g,alpha,ell in left+right:
    assert ell==sum(alpha)+len(alpha)-2+2*g
    wgt*=normalized_count(alpha,g)
   assert wgt.denominator==1
   if key in weight:assert weight[key]==wgt
   weight[key]=wgt.numerator;direct[key]+=1;dist[(gr,beta)]+=1;valid+=1
  assert valid>0
  coverage+=valid
 assert all(direct[k]==weight[k] for k in direct)
 return dict(N=n,m=m,connected_words=words,cut_incidences=coverage,labeled_macros=len(direct),all_covered=True,all_macro_weights_equal=True,types=[dict(suffix_genus=k[0],cycle_rank=k[1],incidences=v) for k,v in sorted(dist.items())],macro_data=[dict(key=repr(k),literal_count=direct[k],formula_count=weight[k]) for k in sorted(direct)])

def identity_count(n,m):
 e=tuple(combinations(range(n),2));return sum(evaluate(n,w)==tuple(range(n)) for w in product(e,repeat=m))

def regressions():
 cases=[(2,0,1),(2,1,0),(2,2,1),(2,6,1),(3,4,27),(4,4,120),(4,6,3936)]
 totals=[]
 for n,m,expected in cases:
  c=identity_count(n,m);assert c==expected;totals.append(dict(N=n,m=m,count=c))
 w=((0,1),(1,2))*3
 assert evaluate(3,w)==(0,1,2) and all(a!=b for a,b in zip(w,w[1:]))
 e=tuple(combinations(range(3),2));all_count=conn_count=0;tri=connected=0
 for w in product(e,repeat=5):
  if evaluate(3,w)==(1,0,2):
   all_count+=1;conn_count+=len(components(3,w))==1
 assert (all_count,conn_count)==(81,80)
 for w in product(e,repeat=6):
  if evaluate(3,w)==(0,1,2) and len(components(3,w))==1:
   connected+=1;tri+=len(set(w))==3
 assert F(tri,connected)==F(3,4)
 a=F(21,2000);c=F(1,20);d=F(879,1000);gamma=F(1,10)
 assert 2*a+2*c+d==1 and a>gamma**2 and F(21,221)<gamma
 return dict(identity_totals=totals,square_zero_witness='((01),(12))^3',endpoint_total=all_count,endpoint_connected=conn_count,triangle_word_fraction=str(F(tri,connected)),unweighted_triangle_fraction='1/4',cp1=dict(joint=str(a),false_product=str(gamma**2),later_residual='21/221',passes_rejection=True))

start=time.monotonic()
result=dict(status='complete',base_commit='d8893491e04aff74ff3185f7054470ffa24a44a4',python=platform.python_version(),nonstandard_dependencies=[],seeds=None,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),regressions=regressions(),cases=[macros_case(2,6),macros_case(3,8)])
result['elapsed_seconds']=time.monotonic()-start
out=ROOT/'cut-reference-results-v1.json';tmp=out.with_name(out.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,out)
print(json.dumps(dict(status=result['status'],elapsed_seconds=result['elapsed_seconds'],cases=[{k:v for k,v in c.items() if k!='macro_data'} for c in result['cases']])) )
