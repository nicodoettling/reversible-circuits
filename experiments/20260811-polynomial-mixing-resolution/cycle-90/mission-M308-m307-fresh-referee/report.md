# M308 Fresh Immutable Referee Report

Date: 2026-08-14 UTC

## Verdict

**ACCEPT frozen M307 at its exact stated scope.**

## Numbered objections

0. **None.**  No provenance, algebraic, exact-enumeration, or scope defect was
   found.

## Non-objection metadata observation

M300's checksum inventory has 15 rows, not the 14 stated in one frozen M303
sentence.  M307 identifies this correctly.  Every M300 row passes, its top
digest matches, and the typo has no mathematical effect.  It must not be
confused with the separate `k=9` fact that the canonical quantile transport
has 15 supported cells.

## Accepted exact scope

1. For odd `k>=3` in the accepted auxiliary channel-one all-middle model,
   the canonical interval coupling has row marginals `x_c`, column marginals
   `y_d`, and proves QTI_1 exactly.
2. `R_c=A_c-B_c` has M307's stated support orientation: negative `R_c`
   forces `i>c>=j`, while positive `R_c` forces `i<=c<j`; mixed signs retain
   both crossing directions.
3. At the sole finite rank `k=9`, universal cellwise QCP_1 is exactly refuted
   first at `(u,ell,c,d)=(1,2,2,2)`.  Exactly 778 of 1440 supported cells are
   negative, and every one of the 96 rows has a negative cell.
4. Also only at `k=9`, all 96 complete MCLP aggregates are positive.  Their
   exact minimum occurs at `(u,ell)=(2,8),(2,19)` and reflection is exact.

The replay and proof audit support these conclusions independently of M307's
prose.  The first two items are exact analytic identities; the last two are
finite exact data only.

## Explicit non-inference

This ACCEPT does **not** infer MCLP, GOCI, OCI, CP, MS, FCL1, any spectral
gap, any mixing bound, or either Terminal.  It says nothing about the global
fixed-length identity-word law or the lazy exact same-product `{3,4,5}`
heat-bath chain.
