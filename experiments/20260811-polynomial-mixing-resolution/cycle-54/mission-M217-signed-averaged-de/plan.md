# M217 Plan — Signed Averaged DE

## Objective

Resolve the original signed averaged disjoint-embedding response

    |sum_(s<k/2) q_hat_s
       [Phi_s^D(Z)-Psi_s^D(Z)]|
      <= C sqrt(l)/k,                    Z=X_l,Y_l,

for odd k>=3 and 2<=l<=(3k-1)/2, or produce a rigorous asymptotic
obstruction/corrected statement. Pointwise IKBE-b is refuted and will not
be used.

## Target and convention

The target is the literal normalized disjoint ordered-double B/A law under
uniform minimal transposition factorizations in the fixed-cell coordinate
calculation, n=3k. Use (pq)(x)=p(q(x)), with displayed factors left-to-right.
Both B/A signs, seam and collision multiplicities, and the nonzero Abel
endpoint remain explicit.

## Immutable dependencies

M192/M195, M199/M207, and M211/M215 are immutable. Verify all checksum
entries before use and never edit those missions.

## Work plan

1. Complete source reading and immutable checksum gates.
2. Derive the exact q_hat_s weights and insert the literal B/A deletion-
   merge profiles into their signed sum.
3. Isolate the macroscopic surviving-face counterterm exposed by M211 and
   determine analytically whether its q_hat coefficient cancels or is small.
4. Bound the residual seam, Borel-kernel, normalization, collision, and
   endpoint contributions, or exhibit an exact asymptotic obstruction.
5. Only after the analytic decomposition, run compact formula diagnostics at
   odd k<=15.
6. Write halfway checkpoint, proof/obstruction, nine-field report, checker/
   results, frozen hashes/manifest, and fresh-audit request.

## Exclusions

No pointwise absolute bound, no attempt at IKBE-a/DV, no channel/kind or
collision deletion, no broad topology computation or finite-sign inference.
No conditional J=2, PCR/WPCR, SCBR/BIR/BR/PCS, gap, mixing, or Terminal
claim unless DE is actually proved and later audited.

## Outcome at the imposed cap

Steps 1--3 and the compact diagnostic part of step 5 are complete. Step 4
reduces exactly to WBE rather than closing DE: the normalizer block is
`O(k^-2)`, and the q_hat macroscopic tail is `O(k^-1/2)`, but the latter
matches the target only for `l` proportional to `k`, not for fixed `l`.
Step 6 is complete. WBE, DE, IKBE-a/DV, conditional J=2, and downstream
claims remain open.
