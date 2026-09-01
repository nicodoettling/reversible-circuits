# M254 fresh proof audit of frozen M250

Date: 2026-08-14 UTC.

## 1. Verdict and immutable gate

**ACCEPT** M250's metric canonical-pruning theorem, its open
common-nonchild endpoint corollary, and its conditional implication from the
explicit RSPT tables to M240's ordinary-edit IDL.  Material objections: none.

This acceptance does **not** accept RSPT, repaired RSMI+, IDL, an all-rank
ordinary-edit route, or any downstream statement.  RSPT remains the first
unproved step.

Every entry in frozen M250's `SHA256SUMS` returns `OK`.  The SHA-256 of that
inventory is

```text
243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7.
```

The four cited dependency inventories were also checked entry by entry and
have the claimed top digests:

```text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
```

The locked DPS author PDF `/tmp/DuPoSc13.pdf` verifies at

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

## 2. What the primary source supplies

Direct reading of Duchi--Poulalhon--Schaeffer gives exactly the following
inputs.

1. Proposition 3 roots the Cayley tree at `y_d`, inserts `x_a` into the
   first edge from `y_a` toward the root, and assigns the two permutation
   labels to the two new edges.
2. Completing incident labels in increasing cyclic order at white vertices
   and the opposite cyclic order at black vertices gives the hairy tree.
3. Lemma 2 says that a consecutive white/black half-edge pair in a valid
   pre-map has the same label, has side distance one or three, and admits a
   legal closure.
4. RandomQuad/Theorem 5 supplies the LIFO order and replaces each complete
   nested interval by one closure side.

The source writes the transposition product in the opposite factor-list
order; M250 uses the already accepted plus-mirror convention.  The intrinsic
half-edge pairing and unordered physical transpositions are unchanged.  The
source states no two-rank endpoint comparison, RSMI, RSPT, or IDL.  M250 does
not attribute any such claim to it.

## 3. Metric canonical pruning

Fix `d>=5`, a canonical unedited excursion `E_a`, and use one-based cyclic
labels

```text
L_a=2a-3,       R_a=2a-2=L_a+1.
```

The accepted M244 contour factorization is literal and bridge-delimited.  The
following independent side count upgrades its colored pruning to M250's
metric statement.

### 3.1 Leaf row

For a leaf, the leading decreasing black gap is empty.  Suppressing only
irrelevant vertex subscripts, the actual token word is

```text
S^(L_a)
W^(R_a) W^(R_a+1) ... W^(L_a-1)
S^(L_a)
B^(L_a-1) ... B^(R_a+1)
S^(R_a).
```

Close from the right.  Each label other than `R_a` occurs in a row

```text
W^t S B^t -> S.
```

Thus every such row has distance one and the exact residual is

```text
S^(L_a) W^(R_a) S^(*) S^(R_a),
```

namely `S W^(R_a) S S` with the side identities retained.

### 3.2 Child rows

Let `c` be a canonical child of `a` and put
`q=R_c=L_c+1`.  After `E_c` has reduced to

```text
S^(L_c) W^q S^(*) S^(R_c)
```

and the cyclic suffix to its right has reduced to one side, the complete
local segment, up to names on sides, is

```text
W^(q-1) S S W^q S S S B_a^q B_a^(q-1).
```

The first two sides are the crossing into the child and the child's leading
side.  The three sides after `W^q` are the child's reduced suffix, the return
crossing, and the already reduced right suffix.  Therefore the first closure
is

```text
W^q S S S B_a^q -> S.
```

Its new side is the third side in the remaining row

```text
W^(q-1) S S S B_a^(q-1) -> S.
```

Both rows have distance three and both black half-edges are attached to the
parent black `x_a`.  Hence both slot factors record second endpoint `x_a`.
Every ordinary label between two child blocks has exactly the one reduced
suffix side and uses `W^t S B_a^t -> S`.

Processing child blocks in reverse cyclic `R_c` order preserves one suffix
side.  Induction then leaves precisely the leaf residual at `a`.  This proves
all four clauses of M250 Theorem 3.1+.

### 3.3 Completeness, boundaries, and edited-slot exclusion

At each displayed closure, the two half-edges have only side tokens between
them.  The interval is therefore a complete node of the noncrossing LIFO
dependency forest.  A child node is removed before any ancestor node, no row
crosses either bridge cut of `E_a`, and replacing a complete node by its one
closure side cannot alter a disjoint outside row.  This proves the claimed
commutation, not merely a colored cancellation.

The sole reversed slot is `x_v`.  It lies on the retained path `P(v)`.
Every excursion to which Theorem 3.1+ is applied is an off-path canonical
excursion and excludes `x_v`.  This remains true after adjoining the new root
leaf.  The cases `a=1` and a cyclic label seam use the same modular order;
no noncanonical slot is silently pruned.

Status: **proved**.  The independent symbolic checker confirms the three
schemas, but the proof above, not that finite check, establishes the theorem.

## 4. Open common-nonchild endpoint

Assume `P(v)` is strictly decreasing and take

```text
v<r<d,       p(r)!=v.
```

If `p(r)` is off `P(v)`, the slot `r` is strictly inside a canonical
off-path excursion.  The two child rows just audited record `x_(p(r))` at
both ranks.

Now suppose `p(r)=a` lies on `P(v)`.  Strict decrease and `p(r)!=v` give

```text
a<v<r.
```

The two slot labels of `r` are `q-1,q`, where `q=2r-2`.  The retained path
incidence at `y_a` is at most `2v-2<q`; hence the entire `r` block occurs
after every open-defect label in the increasing cyclic contour order.  LIFO
reduces the suffix after the block before reaching it.  Ordinary labels use
the distance-one row, and every canonical child block in that cyclic suffix
uses the two audited distance-three rows.  This includes:

- a child with index below `a` that occurs after the cyclic wrap; and
- when `a=1` at rank `d+1`, the new canonical child `d` at the root seam.

Thus the suffix is one side at both ranks.  The two `r` rows close at distance
three against `B_a^q,B_a^(q-1)`, so

```text
b_d(2r-3)=b_d(2r-2)=p(r),
b_(d+1)(2r-3)=b_(d+1)(2r-2)=p(r).
```

The physical slot is consequently

```text
h_r^2,       h_r=(r-1,p(r)-1),
```

at both ranks.  Since `r>v`, `p(r)!=v`, `r<d`, and the old root `d` is a
leaf whose sole neighbor is `1`, neither endpoint lies in
`{v-1,d-1,d}`.

Status: **proved**.  This supplies the absolute endpoint and disjointness
that M247 found missing from M244's rejected RSMI.

## 5. Conditional RSPT-to-IDL implication

RSPT equations (4.1)--(4.5) remain an explicit hypothesis.  Its transition
table covers every retained path event: the initial reversal opens the state;
a next path value above `v` or the first internal ascent seals it; a strict
descent preserves it; and a sealed state remains sealed.  Equality of path
labels cannot occur in a tree, so no transition case is missing.

The endpoint tables imply IDL as follows.  Put

```text
m=2d-2,
alpha=m-1, beta=m, gamma=m+1, delta=m+2.
```

At old rank, `alpha,beta` have first black `x_1`; at new rank those labels
have first black `x_d`, while `gamma,delta` have first black `x_1`.

### 5.1 Sealed case

Equation (4.3) gives equal second endpoints for every low label
`1<=q<=m-2`.  Equation (4.4) makes the old `alpha,beta` factors
`(x_1,x_d)^2` and the inherited new `alpha,beta` factors the same unordered
edge with endpoints reversed.  The new `gamma,delta` factors are
`(x_1,x_(d+1))^2`, exactly the padded pair.  Hence `N=A` coordinatewise.

### 5.2 Open case

For `q=2v-2`, membership in `E_v` and (4.3) give second endpoints
`x_d,x_(d+1)`; the fixed first endpoint is `x_v`.  This is IDL-a.
For each `r>v` with `p(r)=v`, both slot labels lie in `E_v`, giving IDL-b.
For `p(r)!=v`, Section 4 gives IDL-c including its absolute edge and
disjointness.  Every other low label has equal first endpoints and, by
(4.3), equal second endpoints.

Substitution of (4.5) gives the four zero-based physical factors

```text
position             2d-3       2d-2       2d-1       2d
old plus padding     (0,v-1)     (0,d-1)    (0,d)      (0,d)
new rank             (0,d-1)     (0,d-1)    (0,v-1)    (0,d),
```

which is IDL-d.

The low range is `1,...,2d-4`; the four root labels occupy
`2d-3,...,2d`.  IDL-a, the slots `r=v+1,...,d-1`, and unnamed low labels are
disjoint and exhaust the low range.  If `v=d-1`, the intermediate slot range
is empty, IDL-a is at `2d-4`, and the same partition remains valid.  Thus the
empty-scan boundary is covered.

This implication uses M247's five explicit repaired obligations, not any
clause of M244's refuted RSMI.  RSPT itself supplies the edited, direct-child,
sealed, root, and unnamed-coordinate assertions; Theorem 3.1+ and Corollary
3.2 supply the already eliminated metric interiors and common nonchildren.

Status: **proved conditional on RSPT**.  RSPT, repaired RSMI+, and IDL remain
**unresolved**.

## 6. Exact four-row replay

`cleanroom_referee.py` imports no predecessor code or data.  It reconstructs
the hairy contour and uses a cycle-lemma rotation followed by a linear LIFO
stack, an implementation different from M250's repeated cyclic-pair scan.
It runs exactly the four predeclared rank-seven rows and the three symbolic
token schemas; it performs no rank census.

Command:

```text
python3 -B cleanroom_referee.py
```

Environment:

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
```

Result: four rows, zero failures, all symbolic schemas hold, and the
independently normalized row digest is exactly

```text
d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59.
```

This is **exact finite calibration only** and proves none of RSPT, RSMI+, or
IDL.

## 7. Numbered objections and scope

Material objections: **none**.

Nonmaterial clarifications:

1. **N-1 (child-row wording).**  The sentence after M250 equations
   (3.3)--(3.4) says “the two sides before `W^q` in (3.4).”  Equation (3.4)
   starts at `W^(q-1)`; the intended and correct phrase is “the two sides
   between `W^(q-1)` and `W^q` before closing the `q` row.”  The displayed
   rows and proof use the correct count.
2. **N-2 (cyclic suffix wording).**  “Larger canonical child blocks” in the
   proof of Corollary 3.2 should mean blocks later in cyclic contour order,
   not only children with a numerically larger index.  Post-seam lower-index
   children and the `a=1` new-root child use the same already proved two-row
   identity.  This is a wording repair, not a new lemma.
3. **N-3 (`RSMI+` nomenclature).**  M250 does not give a separately boxed
   formal definition of RSMI+; its phrase “all repaired RSMI+ clauses” is
   correctly read as M247 Section 5's five enumerated obligations.  The
   direct RSPT-to-IDL coordinate proof is complete independently of that
   name.

No fixed-edit boundary, every-color synchronization, voltage correction,
route-length theorem, congestion estimate, physical or original-chain gap,
polynomial mixing theorem, or Terminal follows from the accepted claims.

