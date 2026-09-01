# M281 fresh immutable referee report for M278

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: ACCEPT M278 WITH ONE NONMATERIAL CONVENTION CORRECTION.
MATERIAL OBJECTIONS: NONE.
```

For every `d>=5`, frozen M278 correctly proves the three fixed local rooted
old-padded/new DPS routes

```text
i=2,4,...,2d-6 : identity;
i=2d-4         : (R_(2d-5)^(-1))^2;
i=2d-3         : R_(2d-2)^(-1).
```

Moves act chronologically by `R_j[x,y]=[y,yxy]` and
`R_j^(-1)[x,y]=[xyx,x]`.  This local theorem is not a synchronized or
every-color routing assembly and is not a gap or mixing theorem.

## 2. Frozen provenance

M278's top inventory digest is
`352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad`;
all eight payloads verify.  Every cited M225/M228, M231/M234, M236/M237,
M240/M242, M250/M254, M269/M271, and M273/M275 payload verifies.  Exact
digests are retained in `checkpoint.md` and `proof_audit.md`.  The locked DPS
source verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.

## 3. Canonical-slot and complete-interval proof

At old rank, root slot `1` is `(m-1,m)` and slot `h>=2` is
`(2h-3,2h-2)`.  At new rank child `d` occupies the old root slot and the
new root occupies `(m+1,m+2)`.  Marking the two edited slots partitions the
tree contour into nested/disjoint excursions.  RandomQuad LIFO erases each
leafmost complete excursion to one side; induction removes every unmarked
branch/path slot without changing a marked last distance-three endpoint.
The one-leaf extension is outside an internal skeleton and supplies the
accepted appended square.  This validates M278's arbitrary-rank locality;
the finite checks are not being promoted to induction.

## 4. Internal even window

With `e=(v-1,p(v)-1)` and `f=(v,p(v+1)-1)`, the four exhaustive incidence
windows are exactly

```text
[e,f,fef,f], [e,efe,e,f], [c,e,c,f] (c=fef=efe), [e,f,e,f].
```

The parent relations and every outside complete node are unchanged at the
two ranks, so each internal even row uses identity.

## 5. Cross-boundary and last seams

For `j=m-3`, `h=(d-2,p(d-1)-1)`, `g=(0,d-1)`, `k=(0,d)`,
`a=ghg`, and `b=aga`, every recorded/default endpoint in both
`p(d-1)=1` and `p(d-1)!=1` regimes gives

```text
N=[a,b,a,g,k,k],  A=[h,g,a,g,k,k].
```

For the last edit, the old root and new child/root endpoint table gives

```text
N=[g,g,k,k],      A=[g,gkg,g,k].
```

All unshown factors agree.

## 6. Routes, inverses, and minimal rank

The literal chronological calculations are

```text
[a,b,a] -> [g,a,a] -> [h,g,a],
[g,k]   -> [gkg,g].
```

They remain valid in the disjoint seam regime.  Reverse routes are
`R_j,R_j` and `R_m`.  At `d=5`, the fixed edits are `2,4,6,7` and use
identity, two `R_5^(-1)`, and `R_8^(-1)` as appropriate; all slots exist.

## 7. Formal ordinary/fixed composition

Accepted M269/M271 + M273/M275, then M250/M254, then M240/M242 give every
ordinary odd local route of length `4(d-v-1)+5<=4d-7`.  Adding fixed
lengths `0,2,1` covers every adjacent local rooted edit, still with maximum
`4d-7`.  No synchronized tuple, every-color, voltage, or congestion result
is inferred.

## 8. Independent check and numbered objection

The stdlib-only no-import/no-search checker passes all `141` trees, `407`
internal rows, `141` cross rows, and `141` last rows at exactly `d=5,6`.
Its normalized rank digest is
`f1cafde37bee35a4f2f0bbe116f45948f6b238efc5216332df52050398a00836`.
M278's frozen guard replay is byte-identical, SHA-256
`5ef2469e0b09be4d8efa4053e09ef9056097019866591caf77ec0392f4d8f064`.

1. **N-1, nonmaterial:** M278 Section 5 must declare a cyclic starting cut if
   it retains the particular last-seam closure order `alpha,gamma`.  Another
   allowed root-side cut gives `gamma,alpha`; pairings, endpoints, factors,
   and chronological Hurwitz routes are identical.

## 9. Exact stop and final action

```text
fixed local rooted edits                    proved by M278, accepted
complete local rooted adjacent-edit table  proved formally, max 4d-7
synchronized/every-color routes            unresolved
voltage correction/other routing           unresolved
recovery and congestion                    unresolved
spectral gap and polynomial mixing         unresolved
Terminal A/B                               not inferred
```

Final action: **accept frozen M278 with N-1 as a convention-only correction,
and use it only in the complete local rooted-row table pending a separate
assembly.**

