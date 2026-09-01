# Mission M235 plan: signed two-run coefficient moment

Date: 2026-08-13 UTC

## Objective

Attack exactly the signed two-run coefficient moment `(TCM)` left open by the
accepted M226/M229 reduction.  Either prove the universal coefficient-moment
bound analytically, preserving the literal channel-two law, or freeze the
first rigorous exact/asymptotic counterexample or a strictly narrower
standalone obstruction.

## Project target and scope

The ambient target is the global fixed-length uniform law on

```text
Omega(N,m) = {(t_1,...,t_m): t_i is a transposition in S_N,
                              t_1...t_m=id}.
```

The project kernel is the lazy exact same-product `{3,4,5}` block heat-bath
kernel in `GOAL_SPEC.md`.  M235 studies only the algebraic `(TCM)` obligation
inside the accepted M226/M229 reduction.  It will not infer `(YCM)`, `(WBE)`,
`(DE)`, conditional `J2`, `PCR/WPCR`, a spectral gap, mixing, or a terminal.

## Source lock

- Repository commit at initialization:
  `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Durable coordinator ledger through accepted entry `L-0284`.
- Required frozen dependencies to verify: M192/M195, M199/M207, M211/M215,
  M217/M222, and M226/M229.
- Exact primary statement will be transcribed from frozen M226 and qualified
  by M229, including both channel-two kinds, seams, collisions, signed
  first-split weights, and the corrected used domain
  `1 <= x <= (3k-3)/2` for `G_k(x)`.

## Method

1. Reconstruct the exact literal coefficient formula and admissible integer
   domains from M226/M229 and its frozen ancestors.
2. Derive a paired two-run generating-function or discrete moment identity,
   keeping kind-1/kind-2, seam atoms, complementary orientations, collisions,
   and first-split signs separate until cancellation is certified.
3. Use exact rational diagnostics only to discover or falsify identities.
4. If a universal estimate survives, prove it with explicit constants and
   all boundary cases.  If it fails, give an exact family and rigorous
   asymptotics or a finite exact witness that directly violates the stated
   inequality.
5. Freeze a theorem/obstruction/reduction, checker, machine-readable results,
   report, manifest, and `SHA256SUMS`; then request a fresh independent audit.

## Expected failure modes

- silently replacing signed first-split weights by absolute values;
- dropping the second channel-two kind or a seam/collision stratum;
- confusing a finite diagnostic with a universal proof;
- using the overbroad pre-audit domain `x>=1` for `G_k`;
- proving only a one-run estimate or importing `(YCM)`;
- treating `(TCM)` as sufficient for downstream conclusions by itself.

