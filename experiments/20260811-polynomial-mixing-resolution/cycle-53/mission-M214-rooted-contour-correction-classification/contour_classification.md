# M214 exact rooted-contour correction classification at d5-to-d6

Date: 2026-08-13 UTC.

## 1. Declared finite template and convention

Let `F_d(T,pi)` be the accepted plus-mirror rooted DPS closure. Factors are
displayed left to right, and chronological signed right-Hurwitz generators are

```text
R_j(...,a,b,...)    =(...,b,bab,...),
R_j^-1(...,a,b,...)=(...,aba,a,...).
```

Let `mathcal T` be the set of Cayley trees `T` on `[5]` such that white root
5 is a leaf adjacent to the attachment vertex 1. Put

```text
pi_5=(7,8 | 1,2 | 3,4 | 5,6),
E(T)=T union {{1,6}},
pi_6=(9,10 | 1,2 | 3,4 | 5,6 | 7,8),
```

where `E(T)` is rooted at 6. For each inherited edit `1<=i<=7`, define

```text
N_(T,i)=F_5(T,s_i pi_5)(05)(05),
A_(T,i)=F_6(E(T),s_i pi_6).                           (1.1)
```

Deleting the fixed leaf 5 and its edge `{1,5}` is a bijection from
`mathcal T` to all Cayley trees on `[4]`. Cayley's formula therefore gives

```text
|mathcal T|=4^(4-2)=16.                              (1.2)
```

This is the complete template classified below, not a sample of d=5 trees.

## 2. Intrinsic rooted-contour key

Root `T` at 5 and let `p_T` be its parent map. Since 5 is a leaf at 1, vertex
1 lies on the path from every `v in {2,3,4}` to the root. For an odd edit

```text
i=2v-3,
```

the edited adjacent values are the two labels in the black slot belonging to
white vertex `v`. Define the stopped rooted path

```text
P_T(v)=(v,p_T(v),p_T^2(v),...,1).                    (2.1)
```

The following data are intrinsic to `(T,i)` and the declared attachment 1:

```text
late_T(v)=1 iff an internal vertex of P_T(v) has label greater than v;

run_T(v)=max{r>=0: p_T(v+k)=v for every 1<=k<=r},    (2.2)
```

where `v+k<=4`. Thus `run` is the initial consecutive run of larger labels
attached directly below the edited vertex in the rooted tree. It is not fit
from target words or route-search output.

For edit 5, where `v=4` and no larger old label exists, one additional
intrinsic path case is used: whether

```text
P_T(4)=(4,2,3,1).                                    (2.3)
```

## 3. Correction words

All words below are chronological. Define

```text
C_(1,0)=R2 R3 R4^- R5^- R6^- R7 R8^- R7^- R6^- R5 R4 R3^- R2^-

C_(1,1)=R2^- R3^- R4 R5 R6^- R7 R8^- R7^- R6^- R5^- R4^- R3 R2

C_(1,2)=R2^- R3^- R4^- R5^- R6^- R7 R8^- R7^- R6 R5 R4 R3 R2

C_(3,0)=R4 R5 R6^- R7 R8^- R7^- R6^- R5^- R4^-

C_(3,1)=R4^- R5^- R6^- R7 R8^- R7^- R6 R5 R4

C_5=R6^- R7 R8^- R7^- R6^-,
C_6=(R5^-)^2,
C_7=R8^-.                                            (3.1)
```

Together with the empty word, these are nine distinct correction words. The
maximum correction length is 13.

## 4. Exact finite classification theorem

### Theorem 4.1 (complete 16-tree correction classification; **PROVED**)

For every `T in mathcal T` and `1<=i<=7`, the following word maps the naive
endpoint to the actual endpoint:

```text
i=1:
  late_T(2)=1                       -> identity;
  late_T(2)=0, run_T(2)=r in 0,1,2 -> C_(1,r).

i=2 or i=4                          -> identity.

i=3:
  late_T(3)=1                       -> identity;
  late_T(3)=0, run_T(3)=r in 0,1   -> C_(3,r).

i=5:
  P_T(4)=(4,2,3,1)                 -> identity;
  otherwise                         -> C_5.

i=6                                -> C_6.
i=7                                -> C_7.            (4.1)
```

The 13 nonempty descriptor cases have exact sizes

```text
edit 1: direct runs 0/1/2 = 5/2/1; late ancestor = 8;
edit 2: universal identity = 16;
edit 3: direct runs 0/1 = 7/4; late ancestor = 5;
edit 4: universal identity = 16;
edit 5: exceptional path / standard = 1/15;
edit 6: universal double inverse = 16;
edit 7: universal inverse = 16.                       (4.2)
```

**Proof.** Prüfer generation exhausts all `4^2=16` trees in `mathcal T` by
(1.2). For each tree, `contour_classification_audit.py` computes the parent
map, path, late-ancestor flag, and consecutive-child run directly from the
tree. It independently executes the DPS boundary closure to form both words
in (1.1), selects the word in (4.1), and applies every Hurwitz generator in
the convention of Section 1. All `16*7=112` literal equalities

```text
C_(T,i) N_(T,i)=A_(T,i)
```

hold. The class sizes in (4.2) sum to 112 and the Prüfer traversal is complete,
so this is a proof for the full declared finite template. No bounded miss or
quotient-state inference is used. QED.

The normalized complete-row and class-summary digests are respectively

```text
96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b,
0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0.
```

## 5. What the classification repairs

M208/M212's original seven-word table corresponds to the direct-run-zero
cases for edits 1 and 3, the standard edit-5 case, and the universal even/edit-7
cases. Its 21 failures are exactly repaired by:

- identity on the late-ancestor classes;
- two further edit-1 run words;
- one further edit-3 run word; and
- identity on the exceptional edit-5 path.

The key is local in the rooted-DPS tree: it uses the edited black-slot vertex,
its stopped path to the declared leaf-attachment point, and direct larger-label
children. It is not merely a tree-ID lookup. The proof of sufficiency here is
nevertheless finite exhaustive, not a symbolic all-d recurrence.

## 6. Discovery versus proof

`discover_schedule_cover.py` used bounded endpoint balls only to discover
positive candidate words. Its archived radius misses, if any, have no negative
interpretation. The theorem depends only on the separate deterministic
`contour_classification_audit.py`, which performs no route search and imports
no predecessor code.

## 7. Scope and first unresolved step

Theorem 4.1 covers exactly the 16-tree d5-to-d6 template with old root 5 a
leaf at attachment 1, the fixed orders `pi_5,pi_6`, and inherited edits 1
through 7. It does not prove that the key is sufficient at larger d, for a
different old-root degree/attachment, for edits introduced by extension, or
under arbitrary H-orbit representatives and matching colors.

The next standalone obligation is:

> **GENERAL ROOTED-CONTOUR RECURRENCE (UNRESOLVED).** Extend (2.1)--(2.3) to
> arbitrary d and prove by local DPS closure identities that a bounded family
> of signed braids realizes every one-leaf endpoint transformation, with a
> proved length bound and synchronized compatibility.

Ordinary quotient-route corrections remain distinct from M175's later
fixed-physical-endpoint voltage correction. No voltage-corrected length,
polynomial total length, spectral gap, mixing, or Terminal conclusion follows.

