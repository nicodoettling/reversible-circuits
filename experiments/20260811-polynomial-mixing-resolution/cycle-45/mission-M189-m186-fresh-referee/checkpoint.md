# M189 Checkpoint

## Start checkpoint

- The owned M189 directory and plan were initialized before substantive audit.
- The reversible-circuit-sampler skill and current source-of-truth files were
  reread for this assignment.
- M186 is immutable. Its complete checksum gate is the next mandatory step;
  no conclusion has yet been adopted.
- `(PCR)`, `(SCBR)`, `(BIR)`, `(BR)`, PCS-bound, and all downstream claims
  remain unresolved at start.

## Halfway checkpoint

### Immutable gate

M186's complete eight-entry `SHA256SUMS` passed before conclusions. Fresh
top-level hashes match its frozen report, proof, manifest, and checksum file.
No M186 file has been edited.

### Independent analytic findings

- From `F_r(R)=r! product_i tau(d_i)`, the first-prefix and ordered-pair
  denominators are exactly `r` and `r(r-1)`. This independently recovers all
  displayed `lambda_L,lambda_F,lambda_M,Lambda_L,Lambda_F` constants.
- With `eta=P_B-P_A`, the signs in `(CB)` are `+L-F` in both channels. Adding
  and subtracting `sum q_s phi_s`, then using `D_0=D_(k-1)=0`, gives `(BA-C)`
  with the displayed plus signs and no endpoint term.
- Same-run counts are `(k-1-a)_+ +(k-a)_+`. Solving the cross-run endpoint
  equation gives `a-1` for `2<=a<=k` and `2k-a` above `k`; its source split
  is `a-1`. Thus `rho_A,rho_B` and
  `rho_B(2k-c)=c nu_(2k-1)(c)` are exact.
- The two weighted `J=1` estimates are `O(1/k)`. In the tail one can sharpen
  M186's last estimate to the exact identity
  `sum_(c<k)nu_(2k-1)(c)=1/(2k-1)`.
- The pointwise lift identity is
  `N_1(1)=W+(1/2)W 1_T`. Together with
  `eta(W)=2[U_2(2k-1)-2U_1(k)]/(n-3)` and `O(1/k)` triangle probability, it
  gives the full combined `M_1(1)=O(1/n)`.
- Ordinary finite Abel summation gives `(SBP)` exactly. The derivative bounds
  `u_2,r=O(1/d)` and first differences `O(1/d^2)` make either `(PCR)` or
  `(WPCR)` sufficient for `(SCBR)`; neither prefix condition is proved.

### Exact reconstruction and provisional verdict

The self-contained checker imports no M186 code or data and is restricted to
`k=3,5`. It reconstructs literal completion rows and separate prefix laws.
All normalization, combined-sign, Abel, face/tail, singleton, triangle, and
formal `(SBP)` assertions pass on 64 and 810 source-accessible states.

Provisional verdict: **ACCEPT with zero material objections and two
nonmaterial exposition qualifications**. In M186 (4.10), `a=1` should be
handled separately rather than invoking undefined `b_0`; the low-face sum
should explicitly cite `sum b_a<infinity` (indeed `sum b_a=1`). These do not
alter any estimate. `(PCR)` and every downstream claim remain open.

## Final checkpoint

- The coordinator cap was honored: no `(PCR)` attempt or broader computation
  followed the exact `k=3,5` reconstruction.
- Final verdict is `ACCEPT`, with zero material objections and the two
  nonmaterial qualifications recorded in the proof and nine-field report.
- The clean-room checker reran successfully; Python AST, both JSON files,
  report-field count, whitespace, and cache hygiene passed.
- M186 remains immutable. `(PCR)`, `(WPCR)`, `(SCBR)`, `(BIR)`, `(BR)`,
  PCS-bound, and every downstream claim remain unresolved.
