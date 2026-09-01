# M258 fresh immutable audit request

Audit the frozen M258 inventory without importing its checker code.

## Required proof checks

1. Reconstruct the cyclic-start seam-pattern counts
   `D-2t+j,t-j,t-j,j` and the signed overlap spikes at exactly
   `t=ell,ell-k`.
2. Check the tuple domain, both parent orientations, simultaneous hits,
   placements/kinds, collision multiplicity, and `H_s` normalization.
3. Treat `Wtilde_r(f)=sum(t-1)K(r,t)f(t)` as a reflected operator. Do not
   identify it with M251's forward `W_r`. Verify the coefficient ratio,
   head unimodality, total variation `2u/R`, and constant annihilation.
4. Check every endpoint in the piecewise `Q_ell` profile and its weighted
   cutoff variation constant 4, including `k=3` and maximal `ell`.
5. Reconstruct the exact short/long ambient pair list, the support
   `J_(k+c,t)=0` for `t<=c`, and the universal bound `J<=t(t-1)`.
6. Audit the Stirling ratio sum in (4.4)--(4.6), especially the conversion
   to `16sqrt(t/k)` for all `t<3k/2`.
7. Check that positivity is applied only after exact short/long pairing and
   that the quotient constants yield 26, 104, 160, and finally 500.
8. Run an import-free exact falsifier only at `k=3,5,7`; finite results are
   not a universal proof.

## Verdict scope

Return numbered material and nonmaterial objections. Accept or reject only
TAV. Do not infer full DV, J2, WPCR, SCBR, response, gap, mixing, or a
Terminal.
