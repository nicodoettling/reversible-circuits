# M319 exact obstruction: canonical PEBP is circular

Date: 2026-08-14 UTC

## 1. Qualitative involution

Represent each weighted token atom in `Omega_e^+` and `Omega_e^-` by a
half-open interval of its exact mass, concatenated in the frozen lexicographic
order.  On the initial interval of length

```text
min(L_e^+,L_e^-)
```

the equal-coordinate map between the two orientation intervals is a
measure-preserving involution after atom splitting.  It preserves the
unordered profile edge and reverses orientation.  Hence all paired pieces
cancel in `(4)` of `edge_coefficient_identity.md`.

The unpaired terminal interval has exact mass

```text
L_e^+ + L_e^- - 2 min(L_e^+,L_e^-)
 =|L_e^+-L_e^-|
 =|J_e|.                                             (5)
```

Thus the qualitative PEBP involution is proved for every finite edge table,
independently of Borel laws or owner geometry.

## 2. Exact circularity

Summing `(5)` over unordered profile edges gives

```text
sum_e mass(Boundary_e)=sum_e |J_e|=||J||_edge.       (6)
```

Therefore each quantitative boundary estimate in frozen PEBP is word-for-word
the corresponding MPCF estimate.  PEBP supplies no narrower lemma, conserved
grading, or localization.  Its unmatched interval is selected only by global
orientation surplus and the arbitrary atom order; changing that order moves
the alleged boundary while leaving its mass unchanged.

This is an exact obstruction to PEBP as proof progress.  It does **not**
refute MPCF or the numerical inequality asserted by PEBP; those remain the
same unresolved statement.

## 3. Why Borel data alone cannot repair it

The insufficiency is already exact on a two-profile abstract realization.
For every split take `g_s=delta_P` and `f_t=delta_Q`, with `P!=Q`.  The same
normalized `p,q`, quantile coupling, fixed mass `c_X`, and endpoint identity
then give `kappa_(s,t)(P,Q)=1` for every cell and

```text
|J_e|=c_X sum_(s,t)pi_(s,t)=c_X.
```

No `O(1/k)` scale follows from the Borel coupling axioms.  This example is not
an actual owner-profile counterexample; it proves that a successful argument
must use a literal raw-state localization absent from canonical PEBP.

## 4. First genuinely stronger obligation

The next non-circular statement must be a **source-local edge coboundary
certificate**.  Before consulting the aggregate signs `L_e^+-L_e^-`, it must
provide:

1. a fixed raw-state/source surgery `S` on the fully combined token labels;
2. an explicitly source-local exceptional predicate `Exc` (for example,
   marked-owner contact with a distinguished support head or seam);
3. exact preservation of the unordered profile edge and reversal of its
   orientation under `S` on `Exc^c`;
4. a weight coboundary identity on `Exc^c`, with no channel/type/cell norm;
5. the global exceptional-mass bounds

   ```text
   mass(Exc^H_d)<=C d b_d/k,
   mass(Exc^A_d)<=C d b_d/k,
   mass(Exc^C_(d,e))<=C max(d,e)b_d b_e/k.
   ```

Unlike canonical PEBP, `S` and `Exc` may not depend on the final edge
orientation totals or use arbitrary equal-mass matching.  Constructing such a
literal surgery is the first genuinely stronger, falsifiable localization
lemma.  No such surgery is supplied or claimed here.

## 5. Why no k=15 guard is run

Canonical PEBP exists identically and `(6)` holds at every rank.  A single
finite edge norm would only be another finite value of the still-unspecified
absolute constant; it could neither refute nor prove the all-rank boundary
scale and could not test a nonexistent source-local surgery.  Running the
authorized guard would therefore not discharge a named obligation.
