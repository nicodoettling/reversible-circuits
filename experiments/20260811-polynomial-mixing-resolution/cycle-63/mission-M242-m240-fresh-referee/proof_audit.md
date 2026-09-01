# M242 proof audit of frozen M240

Date: 2026-08-13 UTC.

## Immutability and source lock

`sha256sum -c SHA256SUMS` returns `OK` for all nine payloads in frozen M240
and every frozen payload of all ten cited missions M214, M218, M220, M223,
M225, M228, M231, M234, M236, and M237. Their ledger dispositions L-0278,
L-0281, L-0283, L-0286, and L-0287 agree with M240's use: only exact finite
results and formal local identities are accepted. None supplies IDL.

## IDL positions and equivalence

IDL is not proved. It exactly supplies the remaining ordinary-edit DPS
comparison: initial cursor, every doubled slot, terminal boundary, literal
agreement elsewhere, and closed equality. The positions partition correctly.
For `r=v+1`, `I_r` starts after the cursor; for `r=d-1`, it ends at position
`2d-4`; the boundary starts at `2d-3`. When `v=d-1`, the slot range is empty
and the cursor is already at `2d-4`. The path is strictly decreasing exactly
when neither a later-labeled internal vertex nor an internal ascent occurs.

## Scan, carrier, inverse, and length

At stage `t` the moves act on the cursor at `2(v+t)-2` and exactly slot
`I_(v+t+1)`. For a direct child, epsilon is `-1` and both differing squares
conjugate to `(u,x)^2`. For a nonchild, IDL makes the common edge disjoint
from `{x,y,n}`; either signed pair transports it unchanged. After
`L=d-v-1` stages the cursor is at `2d-4`. The five carrier moves send
`(xy,zx,zy,zn)` to `(xn,zy,zy,zx)`. The inverse of a chronological route is
the reversed, sign-negated route, so the final `Q^-1` returns `act(A,Q)` to
`A`. The exact length is `4(d-v-1)+5`, including `L=0`.

## Nonmaterial correction

M240 (5.1) overstates `(R_j^-1)^2[a,b,a]=[b,aba,a]` as generic. For
`a=(01),b=(23)`, the two inverse moves fix `(a,b,a)`, so the claim fails.
It is true in the intended boundary instance `a=(xy),b=(zx)` for distinct
`x,y,z`, exactly the 210-case domain checked by M240 and accepted in
M220/M223. Theorem 4.1 does not use (5.1), and arbitrary-rank fixed-edit DPS
shapes remain explicitly unresolved.

## Verdict and objections

**ACCEPT M240's strict conditional ordinary-edit IDL-to-`Z_2` reduction. Do
not accept IDL, unconditional closure, or generic (5.1).**

Material objections: none.

1. **N-1 (nonmaterial):** equation (5.1) needs its overlapping boundary
   hypothesis. The valid intended instance and Theorem 4.1 are unaffected.

The clean-room checker imports no M240 code/data. It checks local identities,
all synthetic IDL child patterns for `5<=d<=11`, induction boundaries,
inverse chronology, exact length, the valid overlap case, and the disjoint
counterexample. Synthetic IDL words do not prove IDL.
