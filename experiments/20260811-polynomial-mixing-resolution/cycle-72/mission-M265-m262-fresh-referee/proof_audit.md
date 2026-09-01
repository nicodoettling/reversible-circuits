# M265 Fresh Audit of M262

Date: 2026-08-14 UTC.

## 1. Verdict

**ACCEPT** M262's arbitrary-rank counterfamily as a refutation of the stated
CPR first-ascent/first-above-`v` `O -> C` transition.

Material objections: **none**.

The accepted conclusion is narrow.  The family preserves the M257/M260 raw
contexts CP-1--CP-6 and leaves open a refined path transducer, literal root
tables, and IDL.  It gives no fixed-edit, routing, congestion, spectral-gap,
mixing-time, or Terminal conclusion.

## 2. Immutable gates

Before any mathematical payload was opened, the SHA-256 digest of M262's
`SHA256SUMS` was independently computed as

```text
eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a.
```

Every listed M262 payload then verified:

```text
plan.md                         20021a8538cb01088edb8b2c1d51a2da580fe596d448f8da58894d36a2df9eb3
checkpoint.md                   e438608bff0caed2072012b7ca9331d8c7945d96b2e238ddbcfa1e7d9bf19bbe
halfway_checkpoint.md           34f4af35b85d0b7e356429dad2398db55aa3678dff2cc1b82d184e622cfc066d
cyclic_path_row_refutation.md    a3db72cf75880ebd696ce71ddc4e8c42e93ca249c64abfad0581d35f06559bd9
literal_row_check.py             d6b71a4c8ae5021013fa1daa9ab55ad4f668e2daa04c6e2212afdaa30faef844
literal_row_results.json         751e1baf153a53c88182c29d9a5adccb18de023a1d8e74830ba19cf97eae8f04
report.md                        c58927dd104ddfbacb069e22a238df43d4f2098f34ea99f05f3486d6630d963e
audit_request.md                 19b88ab99b53f5636a5f81d52be078e6d19587fea6dfbfd68cbf9f3fc08a9aab
freeze_manifest.md               f0a628d72cbbcf1021dde2ed699222b6e165b94213c197157a94ee54934705bc
```

Every M257 and M260 payload verifies, with inventory-file digests

```text
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144.
```

The relevant M250/M254 inventories likewise verify at

```text
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04.
```

Only M257's M260-accepted literal CP contexts and M250's exact statement of
the unresolved RSPT table are used below.

## 3. Arbitrary-rank admissibility

Fix an integer `rho>=8`.  The family has edges

```text
{1,rho}, {1,6}, {6,4},
{1,r}: 2<=r<=rho-1 and r not in {4,6}.
```

There are `rho-1` edges.  Every vertex is joined to `1`, either directly or
through `4--6--1`, so the graph is connected and hence a tree.  Vertex
`rho` has degree one and is the declared root leaf.  Orienting toward it gives

```text
p(4)=6,  p(6)=1,  p(1)=rho,
```

and all other nonroot vertices attach to `1`.  Therefore the stopped path
before the rank-dependent root row begins `4 -> 6 -> 1`; `6` is a strict
internal nonroot vertex.  Vertex `4` has no rooted child at all.  In
particular, no `r` with `4<r<rho` satisfies `p(r)=4`, and M250 `(4.1)` gives

```text
E_4={R_4}={6}.
```

The paired rank-`rho+1` tree is the same family with new root `rho+1`; the
old root `rho` is then one of the canonical children of `1`.  Thus it is
exactly the CP-6 rank extension and leaves the strict path row at `6`
unchanged except for the larger cyclic modulus.

## 4. Exact CP-5 and CP-2 words

Put `M=2rho-2`.  At the edited leaf-side vertex `v=4`,
`(L_4,R_4)=(5,6)`, and the child product in CP-5 is empty.  The literal base
is consequently

```text
B_4^4 B_4^3 B_4^2 B_4^1 B_4^M ... B_4^7
S^6
W_4^7 W_4^8 ... W_4^M W_4^1 ... W_4^5
S^6 S^5.                                             (A-1)
```

At `a=6`, `(L_6,R_6)=(9,10)`.  The only rooted child is the edited `4`, so
CP-1 requires its actual incidence to be `kappa(4)=L_4=5`, not `R_4=6`.
Substitution of (A-1) into CP-2 therefore gives exactly

```text
S^9
W_6^10 ... W_6^M W_6^1 ... W_6^4
S^5
[A-1]
W_6^6 W_6^7 W_6^8
S^9
B_6^8 B_6^7 B_6^6 B_6^5 B_6^4 ... B_6^1 B_6^M ... B_6^11
S^10.                                                (A-2)
```

All intervals are strict cyclic intervals from M257 CP-2/CP-5.  Since
`M>=14`, every displayed fixed low label exists and the ellipses have the
stated monotone order.

## 5. Complete-node deletion audit

In (A-2), the half-edges for label `4` nearest the child cut are
`W_6^4` and `B_4^4`, separated by the single side `S^5`.  Deleting that
complete node makes labels

```text
4,3,2,1,M,M-1,...,10
```

successively adjacent with exactly one side.  This is an arbitrary-length
interval induction, and it leaves

```text
S^9 S_A B_4^9 B_4^8 B_4^7
```

on the left of the retained base middle.

At the right boundary, `W_6^8` and `B_6^8` have only `S^9` between them.
After its deletion, the rows for labels `7` and `6` become complete in that
order, each again with one side.  In particular, the sole exposed label has
the literal unique internal row

```text
W_6^6 S B_6^6 -> S.                                 (A-3)
```

After (A-3), `W_4^5` sees exactly the two base-return sides plus the closure
side produced by label `6` before `B_6^5`.  Hence label `5`, not label `6`,
has the distance-three row.  The remaining labels

```text
4,3,2,1,M,M-1,...,11
```

then delete by a second distance-one interval induction.  Every deleted pair
is consecutive among the remaining half-edges, so the M250/M254
complete-node commutation result licenses this order.  The exact residual is

```text
S^9 S_A
B_4^9 B_4^8 B_4^7
S^6
W_4^7 W_4^8 W_4^9 W_4^10
S_C S^10.                                            (A-4)
```

This is not the claimed sealed canonical residual.  It also contains no
second distance-three endpoint for exposed label `6`.

## 6. Rank coupling and independent finite guard

Replacing `rho` by `rho+1` sends `M` to `M+2`.  The two newly available
labels `M+1,M+2` appear in each of the two long distance-one chains.  They
are deleted before the fixed terminal rows `10` and `11`, respectively.
Consequently the named closure sides and every inherited token in (A-4) are
unchanged.  This is the arbitrary-rank coupling proof; it is not inferred
from finite cases.

The independent script `independent_guard.py` reconstructs the tree, parent
map, exposed set, CP words, and prescribed complete-node order without
importing M262 code or data.  At `rho=8,9` it confirms (A-3), (A-4), and that
the extension adds labels `15,16` only inside the two distance-one chains.
The raw output is `independent_guard_results.json`.  This is solely a guard
against transcription and boundary mistakes.

Reproduction:

```text
repository commit        502a6f031c6d5a4bc0064ee5b370a4fa3914f993
command                  python3 -B independent_guard.py
Python                   3.12.3
nonstandard dependencies none
seed                     none (deterministic)
```

## 7. Effect on CPR, RST, and IDL

M250 `(4.2)` requires the initial open state at `v=4` to become `C` when the
next path value is `a=6>v`.  M257's separated CPR says equivalently that the
first `c<a`/first-above-`v` internal row gives every exposed label a
rank-stable distance-three endpoint before the root seam.  Here `c=4<a=6`,
but (A-3) has distance one for the sole member of `E_4`.  The next vertex is
`a=1`, reserved for CP-6/RST, so there is no later strict internal ancestor
that could satisfy CPR before the seam.  The stated CPR transition is
therefore **REFUTED**.

The raw contexts CP-1--CP-6 are inputs to the calculation and remain
**PROVED/ACCEPTED**.  The old one-bit `O/C` abstraction is not a proved
sufficient quotient for the separated root-table problem: the actual input
reaching the seam is (A-4), not the hypothetical sealed word.  A valid RST
statement must consume that literal frontier, quantify over a precisely
defined class of literal frontiers, or rely on a newly proved sufficient
refinement.

This conclusion does **not** show that root endpoint equations M250
`(4.4)--(4.5)` fail on (A-4), and it does not show that the proposed
`O^- / O^+` refinement is sufficient.  The `a=1` row was not evaluated.
Thus literal RST, a repaired path transducer, RSPT, repaired RSMI+, and IDL
remain unresolved; IDL may still hold after the root row.

## 8. Numbered objections and qualifications

### Material objections

None.

### Nonmaterial qualifications

1. **N-1 (RST status).**  M262's phrase that the old `O/C` RST is
   under-specified is accepted only as a statement that an abstract one-bit
   tag is not currently a justified sufficient input description.  The
   counterfamily does not refute the numerical root endpoint tables
   `(4.4)--(4.5)` themselves.
2. **N-2 (repair status).**  Distinguishing directional frontiers `O^-` and
   `O^+` is a necessary first repair to the refuted transition table, but
   M262 correctly does not prove that those two tags alone are sufficient;
   literal token data may still be needed.

## 9. Status ledger

```text
PROVED AND ACCEPTED:
  the all-rank admissible tree and rank coupling;
  exact CP-5/CP-2 substitution at v=4, a=6;
  complete-node deletion order and residual (A-4);
  the exposed-label row W_6^6 S B_6^6 -> S has distance one.

REFUTED:
  stated CPR / M250 (4.2) first-above-v O -> C transition;
  use of an unproved one-bit O/C tag as a sufficient RST input abstraction.

UNRESOLVED:
  a sufficient refined path transducer;
  literal root-seam tables on the actual frontier;
  RSPT, repaired RSMI+, and IDL.

NOT CLAIMED:
  fixed edits; routing or congestion; a gap; mixing; Terminal A or B.
```
