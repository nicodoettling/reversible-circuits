# M223 proof audit of frozen M220

## 1. Immutable source and audited object

Every M220 payload passed its frozen checksum inventory. Its top inventory
digest is

```text
0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316
```

and the inventory exactly matches the directory contents. M220 was not edited.

There is no distribution or Markov kernel in this audit. The object is a
finite deterministic physical endpoint transformation under chronological
signed right-Hurwitz moves.

## 2. Formal identity audit

The clean-room checker independently implements transposition conjugation and

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

It verifies M220's carrier on every ordered injection of `(x,y,z,n)` into
`[7]`, totaling `7*6*5*4=840` cases. It verifies the double-inverse identity
on all `7*6*5=210` ordered distinct triples and the single-inverse identity on
all `21^2=441` ordered pairs of transpositions. Every literal tuple identity
passes. These are unconditional formal identities, independent of the failed
DPS recurrence.

## 3. Independent DPS and finite-template reconstruction

`fresh_recurrence_referee.py` reimplements the plus-mirror hairy-tree boundary
trace and distance-one/distance-three closure without predecessor code. For
each old rank `d`, it constructs the root-leaf tree set in two ways:

1. generate every tree on `[d-1]` and attach `{1,d}`;
2. generate every tree on `[d]` and filter for root `d` a leaf at 1.

The sets agree exactly. Counts are 16 at `d=5` and 125 at `d=6`, matching
Cayley's formula. For every unedited row the direct closure also verifies the
literal appended-leaf source identity, and all endpoint words evaluate to the
identity.

## 4. Rank-five specialization

The checker independently reconstructs the displayed finite key and formula:
odd edits use the late flag, consecutive larger-child run, forward-chain
exception, and `Q B Q^-1`; internal evens use identity; the final two edits
use double-/single-inverse words.

On the complete 16-tree `d=5 -> 6` template all `16*7=112` literal endpoint
replays pass. Thus M220 correctly says its candidate reproduces the accepted
M214 table before failing at the next rank.

## 5. Complete rank-six replay and digest

On the complete 125-tree `d=6 -> 7` template, all nine edits give

```text
edit       1   2   3   4   5   6   7   8   9
passes   114 125 125 125 125 125 109 125 125
failures  11   0   0   0   0   0  16   0   0
```

This is 1,098 passes and 27 failures among 1,125 rows. The clean-room
normalization gives

```text
f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
```

exactly M220's complete-row digest. Edits 8 and 9 pass all 125 rows here, but
this remains an exact finite statement only.

## 6. First same-key obstruction

The independent lexicographic scan returns

```text
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}},
T_1={{1,2},{1,3},{1,4},{1,6},{2,5}}.
```

At edit 1 their full proposed descriptors are identical:

```text
kind=ordinary_odd; vertex=2; path=(2,1);
late=false; run=0; forward_exception=false.
```

They receive the same 17-move word. It reaches the exact endpoint for `T_0`.
On `T_1`, its only literal mismatches are positions 7 and 8: replay has
`(45)^2`, whereas the actual endpoint requires `(46)^2`. All source, replay,
and target words evaluate to identity. The proposed key therefore does not
determine whether this displayed word works.

## 7. Objections and verdict

Material objections:

1. None.

Nonmaterial objections:

1. None. M220 labels the candidate conjectural before testing and states the
   refutation boundary correctly.

Verdict: **ACCEPT M220 AS FROZEN**.

## 8. Strict accepted boundary

Accepted: formal tuple identities; exact rank-five reproduction; complete
rank-six counts and digest; and the first same-key pass/failure obstruction.

Refuted only: M220's displayed key-to-word recurrence. Not refuted: another
common braid, a richer contour descriptor, or another all-rank construction.
No every-color, arbitrary-representative, voltage/total-length, gap, mixing,
or Terminal conclusion follows.

