# M218 proof audit of frozen M214

## 1. Audited object and source lock

There is no probability distribution or Markov kernel in this mission. The
audited object is a deterministic finite signed-Hurwitz endpoint certificate
for one declared `d=5` to `d=6` rooted-tree template.

Frozen M214's complete `SHA256SUMS` inventory passed entry by entry. Its
inventory digest is

```text
cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
```

An independent filesystem listing contained exactly the eleven payload files
named by that inventory, besides `SHA256SUMS` itself. M214 remained immutable.

## 2. Independent finite-template completeness

The clean-room checker first generates all `4^(4-2)=16` Cayley trees on
`[4]` by Prüfer codes and attaches the fixed edge `{1,5}`. Separately it
generates all Cayley trees on `[5]` and filters for those in which 5 is a leaf
adjacent to 1. It proves the two resulting 16-element sets equal. This checks
both the claimed bijection and completeness of the finite template.

For every tree `T`, it roots at 5, extends to

```text
E(T)=T union {{1,6}},
pi_5=(7,8 | 1,2 | 3,4 | 5,6),
pi_6=(9,10 | 1,2 | 3,4 | 5,6 | 7,8),
```

and independently reconstructs the accepted plus-mirror DPS boundary closure.
For all 16 unedited rows it verifies the literal source-extension identity

```text
F_6(E(T),pi_6)=F_5(T,pi_5)(05)(05).
```

All reconstructed source and target words evaluate to the identity.

## 3. Descriptor reconstruction

For edits `i=2v-3` with `v=2,3,4`, the checker derives the stopped path from
`v` to attachment vertex 1 directly from the rooted parent map. It then
computes, before endpoint comparison,

```text
late = whether an internal stopped-path vertex has label greater than v,
run  = the initial consecutive larger-label direct-child run below v.
```

For edit 5 it separately tests the stated exceptional path `(4,2,3,1)`.
The exact independently recovered case sizes are

```text
edit 1: run 0/1/2 = 5/2/1; late = 8;
edit 2: universal identity = 16;
edit 3: run 0/1 = 7/4; late = 5;
edit 4: universal identity = 16;
edit 5: exceptional/standard = 1/15;
edit 6: universal double inverse = 16;
edit 7: universal inverse = 16.
```

Thus exactly 13 nonempty descriptor cases cover all 112 rows. The route table
contains eight nonempty words plus the empty word, hence nine distinct words;
the maximum correction length is 13.

## 4. Chronological signed-Hurwitz replay

`fresh_contour_referee.py` independently implements transposition conjugation
and acts in the declared chronological convention

```text
R_j(a,b)    = (b,bab),
R_j^-1(a,b) = (aba,a).
```

For every tree and edit `1<=i<=7`, it constructs

```text
N_(T,i)=F_5(T,s_i pi_5)(05)(05),
A_(T,i)=F_6(E(T),s_i pi_6),
```

chooses the word solely from the tree-derived descriptor, applies every signed
generator in display order, and checks literal factor-by-factor equality. All
`16*7=112` equalities pass. There is no route search, bounded negative
inference, or `Q_6` enumeration.

## 5. Published-digest replay

The mathematical replay was completed first with an independent verbose JSON
schema. A later serialization-only pass encoded the already computed rows in
the published normalized fields. It produced

```text
classification digest
96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b

13-class summary digest
0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0
```

Both equal the frozen values. A separate post-hoc read-only comparison reports
exact equality of M218's normalized 112 rows with M214's rows and exact
equality of the two 13-class summaries. The decisive checker itself imports
and reads no M214 code or result data.

## 6. Objections and verdict

Material objections:

1. None.

Nonmaterial objections:

1. None. M214 already states the finite-exhaustion and scope boundaries with
   sufficient precision.

Verdict: **ACCEPT M214 AS FROZEN**.

## 7. Accepted boundary

Accepted as **proved by exact finite exhaustive replay**: the 13-case,
nine-word correction classification for all 16 trees and seven inherited
edits in the declared `d=5` to `d=6` one-leaf template.

Not inferred: intrinsic completeness outside this template, a recurrence for
larger `d`, other roots or attachments, edits newly introduced by extension,
arbitrary matching colors or Hurwitz representatives, voltage-corrected route
length, total polynomial length, spectral gap, polynomial mixing, or Terminal.
