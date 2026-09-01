# Exact finite full child-contour correction theorem

Date: 2026-08-13 UTC.  Status: **proved on the complete `d=6 -> 7`
template only**.

## Statement

Let `T` range over all trees on `[6]` for which root 6 is a leaf adjacent to
1.  There are exactly `5^3=125` such trees.  For the canonical rooted order
`pi_d=(2d-3,2d-2,1,...,2d-4)` and every adjacent-label edit `1<=i<=9`, set

```text
N_(T,i)=F_6(T,s_i pi_6)(06)^2,
A_(T,i)=F_7(T+{{1,7}},s_i pi_7).
```

Use chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

For an ordinary odd edit `i=2v-3`, form the stopped parent path
`P(v)=(v,p(v),...,1)`, the full ordered larger-child vector

```text
c_t = 1 iff p(v+t+1)=v,       0<=t<6-v-1,
```

and signs

```text
epsilon_0=-1 if c_0=1 else +1,
epsilon_t=-1 if c_t=1 else -epsilon_(t-1).
```

For each vertex of `P(v)`, also record its increasing list of off-path
children.  These data, together with the late-ancestor flag and M214 forward
exception flag, form the full Candidate-B descriptor `D_B` fixed in
`candidate_descriptors.md`.  Let `ascent(v)` mean that two consecutive
internal entries of `P(v)` increase.

Define

```text
Q = product_(t=0)^(6-v-2)
      R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t,

B_6 = R_8^- R_9 R_10^- R_9^- R_8^-.
```

The Candidate-B correction is

```text
odd i:     identity                         if late(v) or ascent(v),
           Q B_6 Q^-1                      otherwise;
even i<=6: identity;
i=8:       (R_7^-)^2;
i=9:       R_10^-.
```

Then, for every one of the `125*9=1,125` pairs `(T,i)`, the assigned word
sends `N_(T,i)` exactly to `A_(T,i)`.  Consequently all 407 Candidate-B
descriptor classes admit a common displayed correction word on this finite
template.  There are 14 distinct assigned words and their maximum length is
17.

## Proof certificate

For distinct `x,y,z,n`, literal chronological action gives

```text
R_p^- R_(p+1) R_(p+2)^- R_(p+1)^- R_p^-
  [(xy),(zx),(zy),(zn)]
= [(xn),(zy),(zy),(zx)].
```

The six intermediate tuples are written in `symbolic_transport.md`; the
checker verifies this identity independently for all 840 ordered choices of
four distinct symbols from seven.

`child_contour_audit.py` then supplies an exhaustive finite certificate:

1. Prüfer codes reconstruct every tree on `[5]`, append `{1,6}`, and cross-check
   this set against direct Prüfer generation of all six-vertex trees having
   root 6 as a degree-one neighbor of 1.  Both constructions give the same
   125 trees.
2. The checker independently implements DPS boundary tracing and closure,
   constructs all nine naive/actual endpoint pairs per tree, and checks their
   products are identity.
3. It transcribes the two candidate formulae fixed before replay, groups rows
   by descriptor, asserts that each class receives exactly one route, and
   literally applies every chronological signed-Hurwitz generator.
4. Candidate B passes all 1,125 comparisons.  Per-edit pass counts are
   `(125,125,125,125,125,125,125,125,125)`.  Its class count is 407, distinct
   route count 14, and route-length histogram is
   `{0:568,1:125,2:125,5:108,9:84,13:65,17:50}`.
5. A second run reproduces the result file byte-for-byte.  The normalized
   digest of the complete internal Candidate-B row table is
   `80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e`.

This proves the displayed statement because the Prüfer construction is
complete for the declared finite template and every declared row is replayed.
No search for a correction word occurs.

## Candidate-A obstruction retained

The predeclared Candidate A, which records the full larger-child vector but
keeps only M220's forward-path exception, passes 1,109 rows and fails 16,
all at edit 7.  Its first exact collision has common descriptor

```text
("odd_A",5,false,[],false)
```

and common five-move word `R_8^- R_9 R_10^- R_9^- R_8^-`:

```text
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}}       passes,
T_1={{1,3},{1,4},{1,6},{2,3},{2,5}}       fails at factors 8 and 11.
```

For `T_1`, `P(5)=(5,2,3,1)` and `N=A`, so Candidate B's predeclared ascent
rule assigns identity and repairs the row.  Candidate A's complete internal
row digest is
`85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6`.
This refutes only Candidate A's displayed map, not existence of other words.

## Dependencies and first unproved step

Proved inputs used here are elementary Prüfer completeness, the explicit DPS
implementation, and direct Hurwitz tuple algebra.  No classification theorem,
mixing hypothesis, or predecessor implementation is imported.  M214/M218 and
M220/M223 are provenance and falsification targets only and passed their
immutable source lock.

The first unproved step toward a genuine recurrence is an all-rank local DPS
closure lemma showing that, under one-leaf extension, the late/ascent decision
and the full child-sign automaton always expose the carrier factor shape.  It
would also need an induction controlling how much contour information is
necessary.  The present descriptor nearly records an entire rooted contour,
and this finite test supplies neither that induction nor an all-rank length
bound.

## Strict scope

This theorem is only the complete `d=6 -> 7`, 125-tree, nine-edit template.
The 407 rich descriptor classes map to only 14 words, but that finite collapse
must not be read as intrinsic descriptor completeness.  It proves no all-`d`
locality, every-color or arbitrary-representative routing, voltage-corrected
or total route-length bound, polynomial gap or mixing statement, or Terminal
claim.
