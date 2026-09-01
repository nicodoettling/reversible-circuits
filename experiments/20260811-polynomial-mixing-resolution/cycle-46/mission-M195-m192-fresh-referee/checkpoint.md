# M195 Checkpoint

## Start checkpoint

- The owned M195 directory and plan were initialized before substantive audit.
- The reversible-circuit-sampler workflow and current source-of-truth files
  were reread for this assignment.
- M192 is immutable. Its complete checksum gate is next; no conclusion has
  yet been adopted.
- `(DV)`, `(DE)`, conditional `J=2` prefix, `(PCR)/(WPCR)`, `(SCBR)`, and all
  downstream claims remain open at start.

## Halfway substantive checkpoint

- Immutable-input gate: `sha256sum -c SHA256SUMS` passed for all eight frozen
  M192 artifacts. The checksum-file digest is
  `4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60`.
- Clean-room algebra rederived
  `sum_(c=1)^(r-1) tau(c)tau(r-c)=2(r-1)tau(r)/r`. Applied to the two
  marked post-split components, this gives exactly M192's
  `gamma_L,gamma_F` with residual-rank denominator `2k-3`.
- The independently recomputed triangle masses are `3/(2k-1)` and
  `3(k-2)/[k(2k-3)]`. Therefore their complete signed prefix response is
  `O(1/k)` because each literal three-component prefix observable is in
  `[0,3]`; repeated sizes are still counted with multiplicity.
- The disjoint masses have unequal totals. Their cumulative endpoint is
  exactly
  `-6(k-1)/[k(2k-1)(2k-3)]`, so its sign is negative and its size is
  `O(k^-2)`. Finite summation by parts reproduces M192's endpoint-bearing
  Abel identity.
- A uniform Stirling-ratio audit gives, on `s<=k/2`,
  `p_s+q_s<=C b_s` and `|p_s-q_s|<=C(s/k)b_s`; the complementary long-cycle
  tail is `O(k^-1/2)`. Together with `gamma_L,gamma_F<=C/k`, this proves
  `|E_u|<=C sqrt(u)/k` uniformly, including the endpoint range.
- Algebraically `(DV)+(DE)` then control every term of the *conditional
  `J=2`* disjoint identity. This retains the literal profile laws, hence no
  double kind/color or size-collision stratum is discarded. It does not
  prove either lemma or license a separate-channel full `(PCR)` claim.

No material objection has appeared so far. The remaining audit work is the
independent exact `k=3,5` enumerator, artifact comparison, and frozen report.

## Final checkpoint

- The independent exact checker passed at `k=3,5`, reproducing both triangle
  masses, the negative endpoint, all tested Abel identities, and M192's 14
  and 132 disjoint collision-event counts.
- Frozen implementation inspection found no discrepancy from the clean-room
  law. Neither M192 code nor data was imported by the checker.
- Final verdict: **ACCEPT**, with zero material objections and zero
  nonmaterial qualifications.
- `(DV)`, `(DE)`, the conditional `J=2` prefix estimate, `(PCR)/(WPCR)`,
  `(SCBR)`, and every downstream claim remain open.
