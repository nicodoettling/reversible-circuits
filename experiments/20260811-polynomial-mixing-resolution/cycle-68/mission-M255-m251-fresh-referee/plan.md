# M255 fresh referee plan

## Objective

Independently audit the frozen M251 claimed proof of the `Y`-profile denominator-variation estimate (`Y-DV`) without editing M251 artifacts or attempting the remaining `X-Y` tail-averaging obligation (`TAV`).

## Target and status discipline

- Target distribution/model: the exact prefix-profile quantities used in the fixed-length uniform transposition-identity bridge analysis, with odd `k >= 3` and `2 <= ell <= (3k-1)/2`.
- Audited claim: `sum_{s=1}^{k-2} sqrt(s) |Phi^D_{s+1}(Y_ell)-Phi^D_s(Y_ell)| <= 18400 sqrt(ell)`.
- A finite checker is falsification evidence only; it cannot promote a universal claim without the algebraic proof.
- The sole remaining `X-Y` obligation must be identified exactly and left unresolved.

## Immutable source

Audit `cycle-67/mission-M251-dv-restart` at its declared top-level `SHA256SUMS` digest. Verify every listed file before reading the mathematical claims. Do not modify that directory.

## Independent checks

1. Verify all 11 source hashes and the top-level digest.
2. Check the paired-domain identity, index ranges, and endpoints.
3. Check Lemma 1, including the global `3/R` increment bound and the boundary atom.
4. Re-derive the far-region `120 sqrt(t)/(Rr)` estimates from the exact `rho` derivatives.
5. Check Lemma 2 constants and the actual lower bound for `H_s`, including `k=3`.
6. Enumerate the exact three seam profiles and verify weighted variation at most `8 sqrt(ell)`.
7. Check constant annihilation, Abel expansion, and assembly of constant `18400`.
8. Audit the exact definition of `TAV` as the only unproved `X-Y` obligation.
9. Write a compact standard-library-only exact/algebra checker over bounded `k` as a falsification attempt.
10. Return `ACCEPT` or `REJECT` with numbered objections, then freeze report, manifest, and hashes.

## Expected failure modes

- Off-by-one errors at `s=1`, `s=k-2`, or the paired argument `q=D-s`.
- A missing boundary atom in the one-step profile increment.
- Use of an invalid uniform lower bound on `H_s`, especially at `k=3`.
- Seam-profile variation counted with the wrong weight or endpoint.
- Circular use of `TAV`, full `DV`, conditional `J2/WPCR`, or `SCBR`.
- Numerical evidence presented as proof.

