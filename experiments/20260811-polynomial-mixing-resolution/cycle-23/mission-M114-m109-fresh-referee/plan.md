# M114 plan: fresh referee audit of M109

## Objective

Independently referee the frozen M109 full-reset-excursion reduction.  The
declared object is the exact parking-projection reset excursion arising in the
accepted M90/M96 framework; this mission does not claim a spectral gap for the
original heat-bath chain.

## Claims under test

1. The all-`j` Schur recurrences for the unweighted and basin-weighted reset
   excursions are exact on the stated reachable state space, and suffix excess
   `L=s-B` strictly descends along live deep transitions.
2. The exceptional predecessor basin satisfies `beta_e <= k`.
3. The contraction `H(x) <= q(x)(1-q(x))` is proved on the boundary sectors
   `L=0,1,2`, including the `s=2` inactivity exception.
4. For `L=2`, the four compositions, masses, means, exceptional-basin term,
   live-group aggregation, quartic reduction, endpoint inequalities, and exact
   Bernstein certificates are correct.

## Method

- Verify the frozen M109 SHA-256 manifest before reading the argument.
- Read the accepted recurrence scope from M90/M96 and the subsequent
  refutations M98/M99 and M103/M106.
- Re-derive each recurrence and boundary formula independently.
- Build a compact no-import exact checker for a small set of decisive `L<=2`
  cases and certificate identities; do not perform a broad numerical scan.
- Give an `ACCEPT` or `REJECT` verdict with numbered objections and the required
  nine-field claim accounting.

## Parameters and reproducibility

- Exact arithmetic only (Python standard library is not imported by the
  checker).
- Boundary parameters follow M109: integer `s>=2`, `K>=1`, `0<=R<=K`,
  `0<=B<=s`, with active states restricted exactly as in the frozen proof.
- Repository date context: 2026-08-12 UTC.

## Expected failure modes

- A killed target is accidentally included as a live child.
- The contextual/all-`j` reset average is replaced by a favorable fixed `j`.
- Exceptional-basin mass is omitted or double counted.
- A derivative or denominator clearing changes sign.
- A finite Bernstein check is silently promoted to an all-parameter proof.
- The boundary-sector result is overstated as a global all-`L` contraction or
  as a polynomial-gap result.
