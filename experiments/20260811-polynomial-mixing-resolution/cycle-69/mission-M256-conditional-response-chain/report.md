# M256 report: conditional response-chain synthesis

Date: 2026-08-14 UTC.

## Verdict

```text
CONDITIONAL THEOREM THROUGH PCS-BOUND: PROVED.
FULL DV: EXPLICIT HYPOTHESIS.
FCL1 AND A_k(1,1): STILL REQUIRE THE INDEPENDENT FD-BOUND
  (OR M168'S MINORITY-SIGN SUBSTITUTE).
NO GAP, MIXING, OR TERMINAL CLAIM.
```

For odd `k>=3`, `n=3k`, full M192 `(DV)` together with accepted M248/M249
`(DE)` implies

```text
full WPCR => SCBR => BR <=> BIR => PCS-bound.
```

The proof and exact constants are in `chain_proof.md`.

## Decisive normalization audit

- `m=(n-1)/2=floor(n/2)` is the small-component endpoint because `n` is
  odd.
- M252's nonnegative channel masses sum to one and the common `J=0` law
  cancels. The channel-two prefixes are conditional expectations before the
  factor `alpha_2`; no normalization is missing.
- The M192 shared-endpoint and unequal-disjoint-mass endpoint contributions
  remain in `K_J=K_EK_V+7185`.
- M186's `WPCR` functional contains exactly the Abel endpoint
  `(|A_m|+|C_m|)/m` and the interior `D^-2` weights. Its separately proved
  singleton `M_1(1)=O(1/n)` closes the omitted `d=1` term.
- M180's `d>n/2` tail, bounded collision term, and bounded remainder are all
  retained before BR/BIR.
- M174's affine kind transfer `2n eta(T)` is explicit and already `O(1)`;
  it is not absorbed into the boundary coefficient.
- M168's temporary sequence length is `n-3=3k-3`, not the project ambient
  symmetric-group parameter `N`.

## Exact stopping point

M168's closure is

```text
sum_y|Z_k(y)|
 <=k|sum_y z_k(y)|+(n-3)k sum_y|Delta z_k(y)|.
```

Conditional full DV proves only the first term via PCS. The second term is
controlled by `(FD-bound)`, not by WPCR, SCBR, BR, BIR, or PCS. Therefore
the strongest correct theorem under full DV alone stops at PCS-bound.

With the additional FD hypothesis, FCL1 follows, and M161/M166's exact

```text
A_k(1,1)=k/(n-3)sum_y|Z_k(y)|
```

makes boundedness of the first fixed-cell scalar equivalent. Full PCR and
J1-PCR are not required for this weighted route.

## Dependency and checker status

Every declared file in the complete frozen inventories from M168/M171
through M252/M253, including the transitive DE inputs requested in the
mission, passes. The exact checksum-file digests are in
`dependency_audit.md`. The supplementary M161/M166 payload and freeze hashes
also pass for the cell/FCL1 equivalence.

`algebra_checker.py` is standard-library only, deterministic, and attempts
no DV, TAV, FD, or asymptotic computation. It checks exact Hardy coefficients,
the endpoint-bearing SBP identity, channel normalization, `n=3k` conversions,
the affine kind scale, target-mass identity, `TV-close`, and the first-cell
prefactor. All rows in `algebra_results.json` pass.

Retained command:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-69/mission-M256-conditional-response-chain/algebra_checker.py
```

Environment: repository base commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, deterministic, `seed=null`.

## First remaining lemmas and scope

The two independent first residues are `(TAV)` for the complementary two-run
profile (once `Y-DV` is accepted, this is exactly the rest of full DV) and
`(FD-bound)` for absolute phase L1. Solving one does not solve the other.

This auxiliary theorem concerns only the balanced first fixed cell of the
nonlazy long-cycle rank-two kernel. It proves no other cell, direct L1,
all-edge/H0 theorem, comparison bound, spectral gap, polynomial mixing of the
identity heat-bath chain, or Terminal.

Action: **freeze this conditional theorem and request a fresh immutable audit
of the WPCR-to-SCBR endpoint/singleton step and the mandatory stop at FD.**
