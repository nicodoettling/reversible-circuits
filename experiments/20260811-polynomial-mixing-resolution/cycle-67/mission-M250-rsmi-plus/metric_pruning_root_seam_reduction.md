# M250 metric pruning and exact root-seam reduction

Date: 2026-08-14 UTC. Status: **metric canonical pruning and the open
common-nonchild clause proved; repaired RSMI+ reduced to one exact unresolved
root-seam path transducer**.

## 1. Immutable gate, source, and scope

The frozen inventories verify at:

~~~text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
~~~

The locked author PDF of E. Duchi, D. Poulalhon, and G. Schaeffer,
*Uniform random sampling of simple branched coverings of the sphere by
itself*, SODA 2014, 294--304, DOI
'10.1137/1.9781611973402.21', has SHA-256

~~~text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
~~~

DPS Proposition 3 supplies the hairy tree, Lemma 2 supplies legal
distance-one/distance-three local closure, and RandomQuad/Theorem 5 supplies
the LIFO closure. The only accepted M244 theorem used below is Theorem 3.1,
canonical unedited one-open **colored** pruning. M244's frozen RSMI was
rejected by M247 and is not a premise here.

There is no distribution or Markov kernel in this note. The target is a
deterministic comparison of two DPS stack closures. No fixed edit,
every-color, voltage, route length, gap, mixing, or Terminal claim is made.

## 2. Exact setting and literal side-token rewrite

Fix 'd>=5'. Let 'T' be a tree on one-based white labels '[d]', rooted at the
leaf 'd', with '{1,d}' an edge. Let 'p' be the parent map. Put

~~~text
m=2d-2,
pi_d=(m-1,m,1,2,...,m-2).
~~~

For an ordinary odd edit choose '2<=v<=d-1' and swap the values
'2v-3,2v-2'. At a canonical unedited black slot 'x_a', write

~~~text
L_a=2a-3,       R_a=2a-2=L_a+1                      (2.1)
~~~

cyclically. At the edited slot these two incidences are reversed. White
rotations increase and black rotations decrease, as in the accepted
plus-mirror display.

Write 'W_u^q' and 'B_a^q' for white and black half-edges of label 'q', and
write 'S' for an actual tree side or a side created by a previous local
closure. The DPS recurrence is literally

~~~text
W_u^q S^e B_a^q  ->  S_q,             e in {1,3},   (2.2)
~~~

whenever the two half-edges are consecutive among the remaining half-edges.
If 'e=3', record 'x_a' as the second black endpoint of factor 'q'; if 'e=1',
record no factor endpoint. If label 'q' never has a distance-three closure,
its second black endpoint is the final root black vertex. Lemma 2 proves
that every LIFO row has exactly one of the two displayed side counts.

For a label 'q', let

~~~text
b_d(q) = the one-based recorded second black endpoint at rank d,
         or d if no distance-three row for q occurs.                (2.3)
~~~

The physical factor is the unordered pair consisting of the slot black
endpoint and 'b_d(q)', shifted to zero-based labels.

## 3. Metric canonical pruning

### Theorem 3.1+ (exact metric one-open pruning; **PROVED**)

Let 'E_a' be M244's bridge-delimited contour excursion of a nonroot white
vertex 'a'. Assume every inserted black slot in the descendant component of
'a', including 'x_a', is canonical and unedited. There is a bottom-up legal
DPS rewrite wholly inside 'E_a' with all of the following properties.

1. Its literal residual token word is

   ~~~text
   E_a  ->  S^(L_a) W^(R_a) S^(*) S^(R_a).          (3.1)
   ~~~

   Thus the side profile, not only the color profile, is 'S W S S'.
2. For every strict descendant 'c' of 'a', each of its two slot labels
   'L_c,R_c' has a distance-three row whose black half-edge lies at
   'x_(p(c))'. Hence both factors have second endpoint 'x_(p(c))'.
3. Apart from these two rows for each strict descendant slot, every internal
   row used by this reduction has distance one.
4. Every deleted interval is a complete node of M244's noncrossing rewrite
   dependency forest, so the reduction commutes with every outside rewrite.

#### Proof

Induct on the number of white descendants of 'a'. M244 equation (2.2) gives
the literal bridge-contour factorization, and accepted M244 Theorem 3.1
permits the same postorder deletion of complete child nodes.

For a leaf, 'R_a=L_a+1' makes the leading black gap empty. The token word is

~~~text
S^(L_a)
W^(R_a) W^(R_a+1) ... W^(L_a-1)
S^(L_a)
B^(L_a-1) ... B^(R_a+1)
S^(R_a),                                               (3.2)
~~~

with cyclic intervals and empty ranges omitted. Starting at the right,
every displayed white/black pair except 'W^(R_a)' has one surviving side
between it and therefore uses (2.2) with 'e=1'. The entire middle suffix
reduces to one side, leaving exactly (3.1).

For the induction step, first reduce each child excursion. Let 'c' be one
child and put 'q=R_c=L_c+1'. Immediately before crossing from 'y_a' to
'x_c', the increasing white gap ends in 'W^(q-1)'. The crossing side and
the first side in the child residual precede its survivor; its other two
residual sides follow the survivor. Thus, after the already processed
suffix to the right has reduced to one side, the two literal rows are

~~~text
W^q     S S S B_a^q     -> S,                       (3.3)
W^(q-1) S S S B_a^(q-1) -> S.                       (3.4)
~~~

Both have distance three and both record 'x_a'. The two sides before
'W^q' in (3.4) are respectively the parent-to-child crossing and the first
side of (3.1); the third is the side created by (3.3). The two sides after
'W^q' in (3.3) are the last two sides of (3.1); the third is the already
reduced suffix.

Every white label strictly between adjacent child blocks has only that one
suffix side before the oppositely ordered black token, hence uses

~~~text
W^t S B_a^t -> S.                                   (3.5)
~~~

Process children in reverse increasing 'R_c' order. Equations
(3.3)--(3.5) leave one suffix side after every block. At the end the only
white token without a black partner in the trailing gap is 'W^(R_a)';
the initial parent side, reduced suffix side, and final parent side give
(3.1). The inductive distance-three records are retained, and (3.3)--(3.4)
add exactly the two records for each immediate child.

Legality follows from DPS Lemma 2. Completeness and commutation follow from
the accepted M244 dependency-forest argument, because child nodes are
deleted before parent nodes and neither bridge cut is crossed. QED.

### Corollary 3.2 (absolute common nonchild endpoint; **PROVED**)

Assume 'P(v)=(v,p(v),...,1)' is strictly decreasing. For every

~~~text
v<r<d,       p(r)!=v,
~~~

both edited closures, at ranks 'd' and 'd+1', have

~~~text
b_d(2r-3)=b_d(2r-2)=p(r),
b_(d+1)(2r-3)=b_(d+1)(2r-2)=p(r).                  (3.6)
~~~

Consequently the two coordinates in slot 'I_r=(2r-3,2r-2)' are literally

~~~text
h_r^2,       h_r=(r-1,p(r)-1),                     (3.7)
~~~

and 'h_r' is disjoint from '{v-1,d-1,d}'.

#### Proof

If 'p(r)' lies off 'P(v)', slot 'r' is a strict descendant inside one
canonical off-path excursion and Theorem 3.1+ gives (3.6).

Otherwise 'p(r)=a' is on 'P(v)'. Since the path is strictly decreasing and
'p(r)!=v', one has 'a<v<r'. Put 'q=R_r=2r-2'. The retained path-child label
at 'y_a' is at most '2v-2<q'. In the increasing white order, the 'r' block
therefore lies in the high suffix after every path-defect label. LIFO
processes that suffix from high to low. Ordinary high labels use (3.5), and
larger canonical child blocks use (3.3)--(3.4), so the suffix immediately
after the 'r' block is one side at both ranks. Equations (3.3)--(3.4) then
record 'x_a' for both slot labels before the retained path interface is
reached. This proves (3.6).

Finally 'r>v', 'p(r)!=v', and 'r<d'. The old root 'd' is a leaf whose only
child is '1', so 'p(r)!=d'; the extension does not change 'p(r)'. Thus
neither endpoint in (3.7) belongs to '{v-1,d-1,d}'. QED.

This proves exactly the common nonchild 'h_r^2' and disjointness clause
missing in M247 objection M-3. It does not prove the edited, direct-child,
sealed, or root rows.

## 4. Exact first remaining lemma: root-seam path transducer

Theorem 3.1+ deletes all off-path interiors with their actual metric records,
and Corollary 3.2 deletes every high nonchild block needed by IDL-c. What
remains is a one-dimensional stopped-path/root rewrite. The first unproved
step is the following exact lemma.

> **ROOT-SEAM PATH TRANSDUCER (RSPT; UNRESOLVED).**
> With the setting of Section 2, put
>
> ~~~text
> alpha=m-1, beta=m, gamma=m+1, delta=m+2,
> D_v={r:v<r<d and p(r)=v},
> E_v={2v-2} union union_(r in D_v){2r-3,2r-2}.       (4.1)
> ~~~
>
> Apply Theorem 3.1+ to every canonical off-path excursion, then apply
> (3.3)--(3.5) to every high nonchild suffix licensed by Corollary 3.2.
> Couple the remaining rank-'d' and rank-'d+1' token words by inherited
> labels. Their exact state transition is:
>
> ~~~text
> reversed x_v                                      -> O(E_v)
> O(E_v), next path value a>v                       -> C
> O(E_v), descending step current a>next b          -> O(E_v)
> O(E_v), internal ascent current a<next b           -> C
> C, any remaining path step                         -> C.             (4.2)
> ~~~
>
> In an 'O(E_v)->O(E_v)' row, every 'e in E_v' is transported only through
> literal distance-one rows 'W^e S B^e->S'; it receives no
> distance-three record. Every other inherited low label has the same
> distance-three black endpoint at the two ranks. In an 'O(E_v)->C' row,
> every still exposed 'e in E_v' receives a distance-three endpoint before
> the root seam, and that endpoint is the same at the two ranks. No exposed
> label remains in state 'C'.
>
> Equivalently, for all low labels '1<=q<=m-2', the endpoint output is:
>
> ~~~text
> P(v) not decreasing:
>     b_(d+1)(q)=b_d(q) for every q;
>
> P(v) decreasing:
>     q in E_v      => b_d(q)=d and b_(d+1)(q)=d+1,
>     q not in E_v  => b_(d+1)(q)=b_d(q).             (4.3)
> ~~~
>
> The sealed root transition is
>
> ~~~text
> b_d(alpha)=b_d(beta)=d,
> b_(d+1)(alpha)=b_(d+1)(beta)=1,
> b_(d+1)(gamma)=b_(d+1)(delta)=d+1.                 (4.4)
> ~~~
>
> The open root transition is
>
> ~~~text
> b_d(alpha)=v,       b_d(beta)=d,
> b_(d+1)(alpha)=1,   b_(d+1)(beta)=1,
> b_(d+1)(gamma)=v,   b_(d+1)(delta)=d+1.            (4.5)
> ~~~

All quantities in RSPT are literal token-rewrite outputs. The set 'E_v' is
explicit; no phrase such as “absorbs the defect” is left without a metric
meaning. In particular, 'O->C' means that every exposed label acquires a
common distance-three endpoint before the rank-dependent root, while
'O->O' means that every exposed label uses distance-one transport only.

RSPT is strictly narrower than the rejected RSMI:

- arbitrary off-path colored and metric interiors are already eliminated;
- the absolute common-nonchild endpoint and disjointness are proved;
- only the parent sequence 'P(v)', the explicit exposed set 'E_v', and the
  four root-seam labels remain;
- the old false unqualified larger-child row is absent: 'D_v' is exposed
  only in state 'O', never in a sealed row.

RSPT is directly falsifiable by the first label whose distance changes
between one and three, the first differing black endpoint in (4.3), or any
failure of the endpoint identities (4.4)--(4.5).

## 5. Explicit conditional coordinate exhaustion

### Proposition 5.1 (**PROVED CONDITIONAL ON RSPT**)

Theorem 3.1+ together with RSPT implies all repaired RSMI+ clauses and hence
all of M240 IDL for ordinary odd edits.

#### Proof

First suppose 'P(v)' is not decreasing. Equation (4.3) makes every inherited
low physical factor equal at the two ranks. In (4.4), old labels
'alpha,beta' have first black 'x_1' and second black 'x_d'; at the new rank
those same labels have first black 'x_d' and second black 'x_1'. Thus their
unordered physical factors agree. New labels 'gamma,delta' have first black
'x_1' and final-root endpoint 'x_(d+1)', exactly the padded pair. Hence every
coordinate agrees and 'N=A'.

Now suppose 'P(v)' is strictly decreasing. At low label '2v-2', the first
black endpoint is 'x_v'; membership in 'E_v' and (4.3) give second endpoints
'x_d,x_(d+1)', exactly IDL-a. For 'r in D_v', both slot labels lie in 'E_v',
giving IDL-b. Corollary 3.2 gives IDL-c, including its absolute endpoint and
disjointness.

For the root positions, old labels 'alpha,beta' have first endpoint 'x_1';
new labels 'alpha,beta' have first endpoint 'x_d'; and new labels
'gamma,delta' have first endpoint 'x_1'. Substituting (4.5) gives, in
zero-based physical labels,

~~~text
position             2d-3       2d-2       2d-1       2d
old plus padding     (0,v-1)     (0,d-1)    (0,d)      (0,d)
new rank             (0,d-1)     (0,d-1)    (0,v-1)    (0,d),
~~~

which is IDL-d.

Every remaining low coordinate is covered by the equality row of (4.3);
every high coordinate is in (4.5). These ranges are disjoint and exhaust
'1,...,2d'. Thus every unnamed coordinate agrees literally. QED.

This proposition is a conditional coordinate exhaustion only. RSPT remains
unproved, so IDL and M240's all-rank ordinary-edit route remain conditional.

## 6. Predeclared four-row falsifier

Only after (2.2), (3.1)--(3.5), and the exact transition table (4.1)--(4.5)
were recorded in 'checkpoint.md', a clean no-input script tested exactly four
hand-picked rank-seven rows:

~~~text
open  : 4>3>2>1, direct child 5->4, nonchild 6->3
open  : 6>1, empty intermediate scan
closed: 4->6->1, with direct child 5->4
closed: 5->3->4->2->1, with direct child 6->5
~~~

All applicable initial, direct-child, common-nonchild, sealed, root, and
unnamed-coordinate checks passed: four rows, zero failures. The normalized
row digest is

~~~text
d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59.
~~~

Run:

~~~text
python3 -B targeted_rsmi_plus_falsifier.py
~~~

Python is 3.12.3; nonstandard dependencies are empty; no seed is used. This
is exact finite calibration only. It proves neither RSPT, RSMI+, nor IDL.

## 7. Verdict

~~~text
PROVED:
  exact metric canonical pruning E_a -> S W^(R_a) S S;
  both descendant slot labels close at distance three to the parent black;
  the open common-nonchild h_r^2 endpoint and disjointness clause;
  RSPT plus those results exhausts every RSMI+/IDL coordinate.

UNRESOLVED:
  the exact root-seam path transducer (4.1)--(4.5);
  therefore repaired RSMI+, IDL, and unconditional all-rank ordinary-edit Z2.

NOT CLAIMED:
  fixed edits; every-color or voltage closure; route length or congestion;
  a physical spectral gap; polynomial mixing; Terminal A or B.
~~~

