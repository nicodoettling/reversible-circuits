# M258 Plan: two-run total-averaged variation (TAV)

## Objective

Prove or refute, uniformly for odd `k >= 3`, `2 <= ell <= (3k-1)/2`,

```text
Theta_s(ell) = Phi_s^D(X_ell) - Phi_s^D(Y_ell),
sum_{s=1}^{k-2} sqrt(s) |Theta_{s+1}(ell)-Theta_s(ell)|
    <= C sqrt(ell).
```

The target is exactly the two-run TAV statement above.  No conclusion about
full DV, J2, WPCR, SCBR, response, spectral gap, mixing, or either terminal is
in scope.

## Immutable dependencies to verify

- M199/M207: literal-B disjoint-double profiles.
- M235/M238: exact two-seam two-run geometry.
- M251/M255: accepted paired identities and Y-DV.

Every dependency manifest and SHA will be checked before use.  Any mismatch is
a blocker, not an invitation to repair another mission's artifacts.

## Method

1. Reconstruct the exact conventions and definitions for `Phi_s^D`, `X_ell`,
   `Y_ell`, `H_s`, the two parent orientations, both seams, simultaneous seam
   hits, and all placements/kinds/collisions.
2. Starting from the M235 identity
   `y_B = t + k 1_beta + 1_sigma`, derive an exact cyclic-start averaged
   coefficient formula for `Theta_s(ell)` with no `q/qhat` averaging.
3. Decompose the formula into cutoff/head responses and pair the short/long
   Borel increments before absolute values, following the accepted M251 paired
   identity architecture.
4. Prove near/far placement-moment estimates sufficient for TAV.  If closure
   fails, freeze the first exact standalone two-run head-response or
   placement-moment lemma, including its unresolved residue.
5. Only after the formula is fixed, run exact falsification checks for
   `k in {3,5,7}`.
6. Freeze a dependency inventory, theorem/proof report, hashes, and request a
   fresh independent audit.

## Expected failure modes

- Losing one parent orientation or one of the two seams.
- Treating simultaneous seam hits as disjoint events.
- Suppressing a placement, kind, or collision case.
- Replacing exact `H_s` normalization by an asymptotic surrogate.
- Taking absolute values before the short/long pairing cancellation.
- Smuggling in forbidden `q/qhat` averaging.
- Mistaking a finite check for a uniform proof.

## Status labels

All statements will be labeled `proved`, `conditional`, `empirical`,
`refuted`, or `unresolved` according to the repository standard.
