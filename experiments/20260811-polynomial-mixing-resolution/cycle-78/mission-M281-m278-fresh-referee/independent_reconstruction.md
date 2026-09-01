# M281 independent fixed-edit reconstruction

Date: 2026-08-14 UTC.

This reconstruction was fixed after the immutable gate and after reading the
locked DPS source and accepted predecessor definitions, but before opening
M278's `fixed_edit_boundary_theorem.md`, `guard.py`, `guard_results.json`, or
`report.md`.  It imports no M278 claim or computation.

## 1. Exact deterministic setting

Fix `d>=5`.  Let `T` be a tree on one-based white vertices `[d]`, rooted at
the leaf `d`, with edge `{1,d}`.  Rooting gives `p(1)=d`.  Put

```text
m=2d-2,
pi_d=(m-1,m,1,2,...,m-2),
T^+=T union {{1,d+1}}.
```

For the plus-mirror DPS closure `F`, an adjacent value edit `s_i` has source
and target

```text
N_i=F_d(T,s_i pi_d) (0,d)(0,d),
A_i=F_(d+1)(T^+,s_i pi_(d+1)).                    (1.1)
```

The displayed transposition labels are zero-based.  Right Hurwitz moves act
chronologically by

```text
R_j[x,y]=[y,yxy],       R_j^(-1)[x,y]=[xyx,x].     (1.2)
```

This is a deterministic endpoint comparison.  Its ambient sampler target is
the global fixed-length uniform law on `Omega(N,m)` for the lazy exact
same-product `{3,4,5}` heat-bath chain, but no stochastic claim is made here.

## 2. Canonical-slot lemma

DPS Proposition 3 inserts black vertex `x_h` in the edge from white `h` to
white `p(h)`.  The first label of slot `h` meets white `h`; the second meets
white `p(h)`.  Thus at rank `d`, with

```text
L_1=m-1, R_1=m,
L_h=2h-3, R_h=2h-2       (2<=h<=d-1),              (2.1)
```

the first black endpoint of both labels in slot `h` is physical vertex
`h-1`.  The actual sides are

```text
L_h : W_h -- B_h,
R_h : B_h -- W_(p(h)).                              (2.2)
```

At rank `d+1`, the inherited slots `2,...,d-1` remain literal, while

```text
new child d : (L_d,R_d)=(m-1,m),
new root 1  : (L_1,R_1)=(m+1,m+2).                 (2.3)
```

Indeed `p^+(d)=1` and `p^+(1)=d+1`.  Hence the new child occupies exactly
the old root slot and the new root is the appended slot.  This is also the
literal source of the accepted unedited extension identity

```text
F_(d+1)(T^+,pi_(d+1))=F_d(T,pi_d)(0,d)^2.          (2.4)
```

An adjacent value edit changes which black slot supplies the first endpoint
of a boundary label; it does not change the output coordinate bearing that
label.

## 3. Complete-interval locality

The locked DPS RandomQuad Step 3 is a LIFO closure.  A contiguous boundary
excursion which enters and leaves a component of the underlying tree without
using another marked side is a complete interval: its white half-edges are
matched to black half-edges from the same interval, from the inside out.
Every closure replaces the matched pair and its one or three intervening
sides by one side.  Induction on the number of tree sides in the excursion
therefore erases the whole interval to one complete node.  Because the
underlying graph is a tree, excursions cut out by distinct marked sides are
nested or disjoint and cannot interlace.  Complete-node commutation permits
their bottom-up deletion in either order.

For two adjacent canonical slots, mark their four actual sides and delete
every maximal intervening excursion.  What remains is a finite skeleton
depending only on how the two underlying tree edges meet.  No off-skeleton
vertex or label can change a marked label's last distance-three row.  Under
the one-leaf extension, an internal pair of slots is unchanged.  The added
child/root interval lies in the outside root component; by `(2.4)` it only
adds the final `(0,d)^2` after the inherited closure.  Thus the internal
skeleton and every outside complete node are identical at the two ranks.

At the cyclic old-root seam the same statement holds after cutting the
cyclic trace immediately after the marked root excursion.  RandomQuad may
start from any boundary half-edge, and the cycle-lemma rotation changes no
LIFO pairing.  The marked seam skeleton is therefore literal even though
the edit moves label `m` away from the particular root side used as a
convenient start in unedited implementations.

This locality is an all-rank tree/stack statement.  A finite guard may test
its transcription but cannot replace it.

## 4. Internal even edits

Let

```text
i=2v-2<=m-4,       2<=v<=d-2,
q=i,
e=(v-1,p(v)-1),
f=(v,p(v+1)-1).                                      (4.1)
```

The edit swaps `R_v=q` and `L_(v+1)=q+1`.  Therefore the first black
endpoints at coordinates `(q-1,q,q+1,q+2)` are, respectively,

```text
v-1, v, v-1, v.                                     (4.2)
```

Two distinct edges in a tree have exactly four possible incidences.  Direct
deletion of the complete intervals in Section 3 gives the following
distance-three endpoint/factor table; every one of the four displayed labels
has a distance-three row, and every unshown factor is unchanged:

| incidence | four factors at `q-1,...,q+2` |
| --- | --- |
| `p(v)=p(v+1)` | `[e,f,fef,f]` |
| `p(v+1)=v` | `[e,efe,e,f]` |
| `p(v)=v+1` | `[c,e,c,f]`, `c=fef=efe` |
| otherwise | `[e,f,e,f]`, with `e,f` disjoint |

For clarity, the corresponding one-based second-black endpoints are

```text
same parent r:          [r,r,v+1,r];
p(v+1)=v, p(v)=r:      [r,r,r,v];
p(v)=v+1, p(v+1)=r:    [r,v,r,r];
disjoint parents r,s:  [r,s,r,s].                   (4.3)
```

The four cases are exhaustive: sharing can occur through a common parent,
because `v+1` is the parent of `v`, because `v` is the parent of `v+1`, or
not at all.  A second simultaneous incidence would make a cycle.  The
conjugates in the table are just the third edges of the relevant triangle;
in the disjoint case conjugation is trivial.

The parent relations are unchanged in `T^+`, so the old and new skeletons
give the same literal four factors.  Section 3 gives equality at every other
inherited coordinate, and `(2.4)` gives the appended square.  Consequently

```text
N_i=A_i                                                        (4.4)
```

for every internal even edit.  The route is the empty word, in both
directions.

## 5. Cross-boundary edit `i=m-2`

Put

```text
lambda=m-3, mu=m-2, alpha=m-1, beta=m,
gamma=m+1, delta=m+2,
g=(0,d-1),
h=(d-2,p(d-1)-1),
a=ghg,
b=aga.                                               (5.1)
```

The old edit crosses the physical cyclic wrap between slot `d-1` and the
old root slot `1`.  The new edit is between slot `d-1` and new child `d`;
the new root is the untouched `(gamma,delta)` slot.  Since root `d` is a
leaf adjacent only to `1`, `h` meets `g` exactly when `p(d-1)=1`; otherwise
they are disjoint.

Complete-interval erasure gives the literal factor table

```text
coordinates       lambda  mu  alpha  beta  gamma delta
N_(m-2)              a     b     a      g      k     k
A_(m-2)              h     g     a      g      k     k,
k=(0,d).                                             (5.2)
```

Here is the full endpoint audit.  `D(x_r)` means a distance-three row whose
second black endpoint is `x_r`; `F(x_r)` means there is no distance-three
row for that label and RandomQuad Step 4 supplies final root `x_r`.

Old rank, `p(d-1)=1`:

| label | first black | second black |
| --- | --- | --- |
| `lambda` | `x_(d-1)` | `F(x_d)` |
| `mu` | `x_1` | `D(x_(d-1))` |
| `alpha` | `x_(d-1)` | `F(x_d)` |
| `beta` | `x_1` | `F(x_d)` |

Old rank, `p(d-1)=r!=1`:

| label | first black | second black |
| --- | --- | --- |
| `lambda` | `x_(d-1)` | `D(x_r)` |
| `mu` | `x_1` | `F(x_d)` |
| `alpha` | `x_(d-1)` | `D(x_r)` |
| `beta` | `x_1` | `F(x_d)` |

New rank, `p(d-1)=1`:

| label | first black | second black |
| --- | --- | --- |
| `lambda` | `x_(d-1)` | `D(x_1)` |
| `mu` | `x_d` | `D(x_1)` |
| `alpha` | `x_(d-1)` | `D(x_d)` |
| `beta` | `x_d` | `D(x_1)` |
| `gamma` | `x_1` | `F(x_(d+1))` |
| `delta` | `x_1` | `F(x_(d+1))` |

New rank, `p(d-1)=r!=1`:

| label | first black | second black |
| --- | --- | --- |
| `lambda` | `x_(d-1)` | `D(x_r)` |
| `mu` | `x_d` | `D(x_1)` |
| `alpha` | `x_(d-1)` | `D(x_r)` |
| `beta` | `x_d` | `D(x_1)` |
| `gamma` | `x_1` | `F(x_(d+1))` |
| `delta` | `x_1` | `F(x_(d+1))` |

These endpoint tables multiply to `(5.2)`.  In the meeting case,
`a=(d-2,d-1)` and `b=h`; in the disjoint case `a=h,b=g`.

Let `j=m-3`.  Two chronological inverse moves at the same position give

```text
[a,b,a]
 --R_j^(-1)--> [aba,a,a]=[g,a,a]
 --R_j^(-1)--> [gag,g,a]=[h,g,a].                  (5.3)
```

The equalities use only `b=aga`, `a=ghg`, and involutivity; they are valid in
both regimes.  Positions `j+2` and every outside position are unchanged.
The reverse route is the chronological word `R_j R_j`.

## 6. Last edit `i=m-1`

The old edit swaps the two labels of the old root slot.  Neither label has a
distance-three row: both have first black `x_1` and default to old root
`x_d`.  After padding, its final four factors are

```text
N_(alpha,beta,gamma,delta)=[g,g,k,k].               (6.1)
```

At the new rank the edit is inside child slot `d`.  The endpoint rows are

| label | first black | second black |
| --- | --- | --- |
| `alpha` | `x_d` | `D(x_1)` |
| `beta` | `x_d` | `F(x_(d+1))` |
| `gamma` | `x_1` | `D(x_d)` |
| `delta` | `x_1` | `F(x_(d+1))` |

Thus

```text
A_(alpha,beta,gamma,delta)=[g,gkg,g,k].             (6.2)
```

The sole forward correction acts at `beta=m`:

```text
[g,k] --R_beta^(-1)--> [gkg,g].                     (6.3)
```

It changes only `beta,gamma`.  The reverse route is `R_beta`.

## 7. Minimal boundary and formal composition

For `d=5`, `m=8`.  Internal even edits are `i=2,4`, the cross-boundary edit
is `i=6` with `j=5`, and the last edit is `i=7` with generator `R_8` on the
length-ten endpoint.  Every four-factor window and every generator above is
present; empty outside intervals are allowed by the interval induction.

All adjacent edits `1<=i<=m-1` partition exactly as follows:

```text
ordinary odd:       i=2v-3, 2<=v<=d-1;
internal even:      i=2v-2, 2<=v<=d-2;
cross boundary:     i=m-2;
last edit:          i=m-1.                           (7.1)
```

Accepted M269/M271 plus M273/M275 give ordinary IDL, and accepted M240/M242
then give an ordinary route of length

```text
4(d-v-1)+5 <= 4d-7                                  (7.2)
```

in every open ordinary row; sealed ordinary rows use identity.  Sections
4--6 add fixed-edit lengths `0,2,1`.  Since `d>=5`, all are at most `4d-7`.
Reversing chronology and signs gives every inverse route at the same length.
Therefore the complete local rooted-row adjacent-edit table has routes of
maximum length `4d-7`.

This conclusion is deliberately local.  It does not assert a synchronized
tuple route, every-color coverage, voltage correction, route recovery or
congestion, a spectral gap, polynomial mixing, or Terminal A/B.

