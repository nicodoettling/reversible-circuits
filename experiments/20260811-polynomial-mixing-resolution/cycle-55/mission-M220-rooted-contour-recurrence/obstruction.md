# M220 obstruction: M214's finite key does not determine the next-rank schedule

Date: 2026-08-13 UTC.

## 1. Refuted statement

`symbolic_transport.md` declares the explicit recurrence

```text
ordinary odd edit i=2v-3:
  late(v) or forward_exception(v) -> identity;
  otherwise -> Q_(d,v,run) B_d Q_(d,v,run)^-1,
```

with internal even edits assigned identity and the two boundary edits assigned
the formal one-/two-generator schedules. The tree key retains only

```text
(v, late ancestor, initial consecutive larger-child run,
 forward-chain exception).
```

This recurrence is exact on all 112 M214 rows and false at `d=6 -> 7`.

## 2. Complete finite test

Deleting root leaf 6 and edge `{1,6}` identifies the declared rank-six tree
template with all Cayley trees on `[5]`; hence it has exactly

```text
5^(5-2)=125
```

members. `rooted_recurrence_audit.py` builds that set both directly and by a
filtered six-vertex Prüfer traversal and proves the sets equal. For each tree
it reconstructs the DPS closure and literally replays all edits `1,...,9`.
There is no quotient enumeration or route search.

The result is

```text
edit       1   2   3   4   5   6   7   8   9
failures  11   0   0   0   0   0  16   0   0
```

The normalized complete-row digest is

```text
f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
```

## 3. First exact same-key witness

Let old root 6 be a leaf at attachment 1 and take

```text
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}},
T_1={{1,2},{1,3},{1,4},{1,6},{2,5}}.
```

At edit 1, both have edited vertex `v=2`, stopped path `(2,1)`, no late
ancestor, consecutive direct-child run zero because vertex 3 is not a child
of 2, and no exception. The proposed key is therefore identical. It does not
record that 5 is a nonconsecutive larger child of 2 in `T_1`.

The common route assigned to both rows is

```text
C=R2 R3 R4^- R5^- R6 R7
  R8^- R9 R10^- R9^- R8^-
  R7^- R6^- R5 R4 R3^- R2^- .                       (3.1)
```

Using zero-based physical labels, the star row is

```text
N_0=(01),(15),(02)^2,(03)^2,(04)^2,(01),(05),(06)^2,
A_0=(01),(16),(02)^2,(03)^2,(04)^2,(05)^2,(01),(06),
C N_0=A_0.                                            (3.2)
```

For `T_1`, the row is

```text
N_1=(01),(15),(02)^2,(03)^2,(45)^2,(01),(05),(06)^2,
A_1=(01),(16),(02)^2,(03)^2,(46)^2,(05)^2,(01),(06),

C N_1=(01),(16),(02)^2,(03)^2,(45)^2,(05)^2,(01),(06)
     != A_1.                                          (3.3)
```

The literal mismatches are exactly positions 7 and 8. Every displayed word
evaluates to the identity. Equations (3.2)--(3.3) are an exact obstruction to
the proposed key-to-schedule map: the same key and same declared word succeed
on one row and fail on the other.

## 4. What geometry the key misses

The difference is off the stopped path. In `T_1`, the nonconsecutive larger
label 5 is a direct child of edited vertex 2, yet `run=0` because the initial
candidate label 3 is not such a child. Under extension, the actual edit
transports the square `(45)^2` to `(46)^2`; the alternating-sign conjugator
in (3.1) does not. Thus a viable recurrence must retain more of the full
larger-child/contour incidence than the initial consecutive run.

There is a second warning at edit 7. The proposed carrier fails on 16 rows,
all of which have `N=A`; their stopped paths include several patterns beyond
the one forward-chain exception. This independently shows that the single
exception flag is not stable at the next rank.

## 5. Surviving exact statements

- **PROVED formal:** the four-factor carrier and the single-/double-inverse
  Hurwitz identities in `symbolic_transport.md`.
- **PROVED exact finite:** the closed formula reproduces all 112 `d=5 -> 6`
  rows.
- **PROVED exact finite:** at `d=6 -> 7`, it succeeds on all rows for edits
  `2,3,4,5,6,8,9`; in particular both newly included edits 8 and 9 pass all
  125 trees.
- **REFUTED:** the explicit recurrence (5.2) of `symbolic_transport.md` and
  the claim that its displayed schedule is determined by the proposed finite
  key.
- **UNRESOLVED:** whether a richer full-contour descriptor yields a bounded
  all-rank correction family.

## 6. First unresolved lemma and strict scope

> **FULL CHILD-CONTOUR SIGN LEMMA (UNRESOLVED).** For a one-leaf extension,
> identify the finite ordered incidence data of all larger children and the
> stopped contour path that determine the signs and exceptional identity
> cases in a conjugate-of-carrier correction; then prove the resulting formula
> by local DPS boundary identities with an explicit length bound.

The witness does not prove that no alternative common braid exists for
`(N_0,N_1)` and `(A_0,A_1)`. It rejects only the declared key-to-word formula
and any proof that treats the initial consecutive run as sufficient for that
formula. No every-color, arbitrary-representative, voltage-length, polynomial
route, spectral-gap, mixing, or Terminal conclusion follows.

