# M251 plan: restart the adjacent-split DV obligation

## Objective

Independently reconstruct and resolve the exact unweighted adjacent-split
variation estimate

\[
 \sum_{s=1}^{k-2}\sqrt{s}\,\left|\Phi^D_{s+1}(Z)-\Phi^D_s(Z)\right|
 \le C\sqrt{\ell},
 \qquad Z\in\{X_\ell,Y_\ell\},
\]

uniformly for odd `k >= 3` and `2 <= ell <= (3k-1)/2`, with a universal
explicit constant `C` if the bound is proved.

## Status discipline

- Target: the exact scalar profile `Phi_s^D` accepted in immutable missions
  M192/M195 and M199/M207.  This is an analytic profile estimate, not a new
  Markov kernel or stationary-law claim.
- M245 is interrupted read-only source reconstruction and is not accepted.
- Every result here is `unresolved` until frozen and independently audited.
- No inference to DE, J2, PCR, a spectral gap, mixing, or a Terminal is in
  scope.

## Method

1. Read the mandated project sources and immutable M192/M195, M199/M207
   artifacts; transcribe every domain, normalization, and endpoint exactly.
2. Put the `s` and `s+1` profiles on one common summation domain.  Pair the
   short- and long-fragmentation terms before taking absolute values, and
   derive an exact discrete-difference identity whose blocks are:
   survivor/cutoff jumps, common smooth kernel, strip/boundary, and
   normalization.
3. Estimate only after the exact identity is fixed.  Preserve cancellations
   between short and long kernels.
4. If a proof closes, state all constants and exceptional cases.  Otherwise
   freeze the first precise scalar lemma (or a genuine counterfamily) that is
   still needed.
5. A compact formula-only diagnostic is permitted only after Step 2; it is
   falsification evidence, never an asymptotic proof.
6. Freeze the complete artifact inventory and request a fresh immutable audit.

## Expected failure modes

- taking absolute values before the short/long leading derivatives cancel;
- confusing the unweighted DV target with a `q`- or `qhat`-weighted sum;
- omitting the reflected split `D-s`, the cutoff `d<r`, or the profile
  normalization `1-gamma_L(s)`;
- silently changing ordered/unordered domains or endpoint conventions;
- treating finite diagnostics as proof.

