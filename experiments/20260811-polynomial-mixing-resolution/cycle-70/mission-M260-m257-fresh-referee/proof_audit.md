# M260 Fresh Proof Audit of M257

Date: 2026-08-14 UTC.

## 1. Split verdict

**ACCEPT** M257's proved raw cyclic path-context reduction CP-1--CP-6.
Material objections: none.

This acceptance covers only the actual incidence rule, canonical cyclic
context, accepted off-path substitution, reversed edited base context,
nesting along the unique stopped path, and explicit old/new rooted-tree seam
data. It does **not** accept CPR, RST, their conjunction RSPT, repaired
RSMI+, IDL, or any downstream ordinary/fixed-edit, routing, gap, mixing, or
Terminal claim. CPR and RST are separate unresolved obligations.

## 2. Immutable and source gates

Every one of the six entries in M257's frozen SHA256SUMS verifies:

~~~text
plan.md                           93444afb43f61aef0c2349462afb3d0e0373f3685e9ea3d4384986c070a6915f
checkpoint.md                     edc5d632b46cc78a6a8b96248466166086c793ee6a95b8dcf57a790382dd1818
cyclic_path_context_reduction.md  6e9f8e5f7c5a415b564c1d40f362a9c4e3e74b7c04a9c1600e0fe984076dd6f9
report.md                         a96a627a5e685a45e8bdd15634ba4647858e9cbc191188da08294e7c9d824d61
audit_request.md                  f9ef46336aa87fe64e9c57e3b35836830e8e425acaf67dcf9154240a93ba69f4
freeze_manifest.md                399b4aa2d3490232b434eac5f1a1da0d0734c9037b13d0b258293b47fbae7bd8
~~~

The SHA-256 digest of M257's SHA256SUMS is exactly

~~~text
9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1.
~~~

Every inventoried payload of M240, M242, M244, M247, M250, and M254 also
verifies. Their inventory-file digests are:

~~~text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
~~~

The locked DPS PDF verifies at

~~~text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
~~~

Direct source reading gives precisely the permitted inputs. DPS Proposition 3
roots the Cayley tree and inserts black x_a in the first edge from y_a toward
the root. The hairy-tree definition completes labels increasingly around
white vertices and oppositely around black vertices. Lemma 2 gives a legal
same-label distance-one or distance-three closure for consecutive white/black
half-edges, and RandomQuad/Theorem 5 gives LIFO closure. The source contains
no two-rank endpoint comparison, CPR, RST, RSPT, or IDL.

M247 accepts only M244 Theorem 3.1 and rejects M244's RSMI. M254 accepts
M250's metric canonical pruning, complete-node commutation, and open
common-nonchild result while keeping RSPT unresolved. M257 respects those
gates.

## 3. Actual incidence of the reversed child

For a canonical nonroot slot x_c,

~~~text
L_c = label on x_c--y_c,
R_c = label on x_c--y_(p(c)).
~~~

Therefore the incidence of child c seen at its parent white vertex is R_c.
The ordinary odd edit reverses only the two incidences at x_v, so the
incidence seen at y_(p(v)) becomes L_v, while the incidence seen at y_v
becomes R_v. Hence the actual child-incidence map is exactly

~~~text
kappa(c)=L_v  if c=v,
         R_c  otherwise.
~~~

Replacing kappa(v) by R_v would cross the edited edge on its wrong side and
alter both the cyclic position of the retained hole and its surrounding
white interval. CP-1 is necessary, not cosmetic.

## 4. Canonical cyclic context CP-2

Cut the contour just after it crosses from y_(p(a)) to canonical x_a on the
R_a side. At a black vertex the rotation is decreasing. Since
R_a=L_a+1 cyclically, the strict interval B_a(R_a down_M L_a) is empty, and
the contour immediately crosses S^(L_a) to y_a.

At y_a, increasing white rotation encounters all actual child incidences in
increasing cyclic order after L_a. If these are q_j=kappa(c_j), with
q_0=L_a, then the part through child c_j is

~~~text
W_a(q_(j-1) up_M q_j) S^(q_j) I_j.
~~~

After the last child, the contour traverses

~~~text
W_a(q_t up_M L_a) S^(L_a)
~~~

back to x_a. Decreasing black rotation then traverses
B_a(L_a down_M R_a) and returns to the parent on S^(R_a). Concatenating
these literal segments is exactly CP-2/M257 (3.1).

This derivation orders children by cyclic incidence labels, not by numerical
vertex names. A smaller-index post-wrap child is therefore included in its
unique correct interval. Empty intervals and an empty child list reduce by
the same formula.

## 5. Reversed base context CP-5

The contour cut for x_v follows the actual parent-side crossing, now labelled
L_v. From that incidence, decreasing black rotation traverses the entire
strict interval B_v(L_v down_M R_v) before reaching the actual child side
R_v; it then crosses S^(R_v) to y_v. Every rooted child of v is canonical
and has parent incidence R_c, so increasing white rotation begins after R_v
and gives the product in CP-5.

On returning from y_v across S^(R_v), the decreasing interval from R_v to
L_v is empty because R_v=L_v+1. The final crossing to the parent is S^(L_v).
Thus the complete literal base is

~~~text
B_v(L_v down_M R_v) S^(R_v)
product_j[W_v(q_(j-1) up_M q_j) S^(q_j) I_j]
W_v(q_t up_M R_v) S^(R_v) S^(L_v),
~~~

which is CP-5/M257 (3.4). It includes larger children before wrap and
lower-index children after wrap.

## 6. Off-path substitution, commutation, and nesting

Every child subtree off the unique rooted path from v excludes the sole
reversed slot x_v; all its slots are canonical. Accepted M250 metric pruning
therefore replaces its bridge-delimited excursion by

~~~text
I_h -> S^(L_h) W^(R_h) S^(*) S^(R_h).
~~~

The parent context already contains the crossing S^(R_h) into x_h.
Consequently the complete parent block is exactly

~~~text
S^(R_h) S^(L_h) W^(R_h) S^(*) S^(R_h),
~~~

which is CP-4/M257 (3.3), with all five side/half-edge tokens accounted for.

M250's accepted theorem says each deleted interval is a complete node of the
noncrossing rewrite-dependency forest and commutes with every outside rewrite.
Thus pruning an off-path child cannot cross or modify the retained path-child
hole. After all off-path substitutions, leaving that one hole defines the
context operator P_(a,c). Inserting CP-5 at the bottom and successively
inserting the result into the unique parent hole reconstructs the full
stopped-path contour. No colored projection or finite-rank pattern is used.

## 7. Root seam CP-6

Put

~~~text
m=2d-2, alpha=m-1, beta=m, gamma=m+1, delta=m+2.
~~~

At rank d, white d is the root and the edge 1--d contains x_1; the canonical
cyclic representatives are (L_1,R_1)=(alpha,beta), with R_1 on the parent
side. After adjoining the new root leaf d+1, white d+1 becomes the root. The
edge 1--(d+1) now contains x_1 with
(L_1,R_1)=(gamma,delta).

The old root leaf d becomes a child of 1, its edge contains the new canonical
x_d, and the incidence at y_1 is

~~~text
kappa(d)=R_d=2d-2=beta.
~~~

All inherited low child incidences are unchanged except the already explicit
edited child rule CP-1. Applying CP-2 at a=1 with modulus m in the old row
and modulus m+2 in the new row includes the new child, both new labels, all
post-wrap children, and every half-edge in the exhausted label set. It
requires no unused fresh label. This is exactly CP-6/M257 (4.1).

## 8. Boundary and falsification audit

- At a=1 use cyclic representatives L_1=M-1 and R_1=M; CP-6 supplies the
  rank-specific values.
- If v=d-1, the larger-direct-child range is empty, but CP-1, CP-5, and the
  seam remain literal.
- A post-wrap child's numerical index is irrelevant because the product is
  ordered by kappa in cyclic order after the current incidence.
- For an empty child set or adjacent incidences, the product or open interval
  is empty, with no phantom token.
- CP-2 lists the complete cyclic interval at the rank-specific modulus and
  therefore assumes no supply of unnamed labels.

The first symbolic falsifiers would have been a nonempty canonical leading
black interval, an edited parent incidence R_v, a missing parent crossing in
CP-4, or a new child incidence other than R_d=beta. Direct contour parsing
rules out all four. No finite replay or census was performed.

## 9. Exact unresolved split

The only nonoverlapping interpretation consistent with M257's checkpoint,
Section 5, and report is:

1. **CPR** starts with CP-5 and simplifies the rank-coupled contexts at strict
   internal ancestors between v and 1. It must output the actual root input
   word, tagged O(E_v) or C, while proving its metric side counts and inherited
   low-endpoint stability.
2. **RST** alone consumes the two rank-specific a=1 contexts from CP-6 and
   performs final root completion. Conditional on the actual open/sealed words
   output by CPR, it must prove endpoint tables (5.2)--(5.3).
3. Only CPR plus RST, together with accepted M250 gates, would establish RSPT.

M257 explicitly labels both lemmas unresolved and says neither RSPT nor IDL
follows. There is no hidden RSPT claim.

### Nonmaterial clarifications

1. **N-1 (domain wording).** Theorem 3.1 says “canonical vertex” although its
   formula uses a parent slot and therefore applies to a canonical nonroot
   vertex. The stopped path uses only such contexts, and root completion is
   separately assigned to RST.
2. **N-2 (CPR/RST boundary wording).** Section 5's CPR list says “a path
   step” without repeating the checkpoint's restriction to ancestors strictly
   between v and 1. Read literally without that restriction it could overlap
   the rank-dependent a=1 row assigned to RST. The checkpoint, CP-6 paragraph,
   “internal path induction” sentence, and report make the intended partition
   unambiguous. This is a scope clarification, not a proof gap in CP-1--CP-6
   and not an acceptance of either unresolved lemma.
3. **N-3 (RST input).** “Open input” and “sealed input” must mean the actual
   side-token words produced by CPR, not merely an abstract one-bit tag.
   Otherwise the root endpoint table would be underspecified. M257's command
   to apply CP-2 to those inputs supports this reading.

## 10. Status ledger

~~~text
PROVED AND ACCEPTED:
  raw cyclic incidence and path contexts CP-1--CP-6;
  off-path metric substitution under accepted M250;
  complete-node commutation and stopped-path nesting;
  explicit root-seam rooted-tree data.

UNRESOLVED:
  CPR metric O/C row lemma;
  RST root endpoint tables;
  hence RSPT, repaired RSMI+, IDL, and all-rank ordinary-edit Z2.

NOT CLAIMED:
  fixed edits; every-color synchronization; voltage-corrected length;
  routing or congestion; a spectral gap; polynomial mixing;
  Terminal A or Terminal B.
~~~
