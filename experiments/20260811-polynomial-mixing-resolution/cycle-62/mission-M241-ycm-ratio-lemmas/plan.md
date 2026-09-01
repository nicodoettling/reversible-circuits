# M241 plan: YCM ratio and strip lemmas

Date: 2026-08-13 UTC.

## Objective

Independently prove or refute only the three scalar lemmas isolated by M239
from the interrupted M232 YCM attempt:

1. **R1 (GG2 bracket):** a uniform explicit bound, on the exact GG2 domain,
   for

       b_x b_(k-s) / (b_k b_(D-s)),   D=2k-1.

2. **R2 (smooth shifted fragmentation):** outside `x<s<2x`, compare the
   shifted fragmentation contribution with the no-shift term with an explicit
   `O((x+1)/k)` constant on the exact SG domain.
3. **R3 (nonsmooth strip):** for `x<s<2x`, bound both actual and comparison
   masses by an explicit multiple of `sqrt(x)/R`, `R=2k-3`.

The deliverable is a rigorous factorial/log-ratio proof, a counterexample, or
a precise frozen obstruction. No implication to YCM is allowed unless the
exact sufficiency of all three lemmas is separately checked.

## Immutable gate and source lock

- Read `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, and its sampling and
  experiment references.
- Verify frozen M226 and M229 from within their mission directories and record
  their checksum-file digests.
- Record hashes of interrupted M232 and active-unaccepted M239 inputs used.
- Treat M226/M229 as immutable accepted inputs and M232/M239 only as candidate
  reductions. Never edit any predecessor.
- Use only M229's corrected `G_k` domain `1<=x<=(3k-3)/2`.

## Method

1. Recover the exact algebraic meanings and domains of R1--R3 from the
   accepted coefficient interface and candidate skeletons.
2. Express Borel ratios through exact factorial products or the recurrence
   `rho_n=b_(n-1)/b_n`; prove explicit one-sided log-ratio bounds.
3. Derive constants analytically before running diagnostics.
4. Use a compact deterministic exact-rational or certified-interval checker
   only to falsify proposed inequalities and test boundary cases.
5. Check whether R1--R3, exactly as proved, actually discharge every named
   constant gap in the proposed SG/GG2 argument. If not, freeze the first
   missing step rather than infer YCM.

## Exclusions

No TCM, WBE, DE, J2, PCR, downstream gap/mixing result, or Terminal claim.
No broad numerical scan and no inference from finite data.

## Deliverables

`checkpoint.md`, `ratio_strip_lemmas.md` (proof or obstruction), compact
checker and machine-readable results, `report.md`, `freeze_manifest.md`, and
`SHA256SUMS`, followed by a request for fresh immutable audit.
