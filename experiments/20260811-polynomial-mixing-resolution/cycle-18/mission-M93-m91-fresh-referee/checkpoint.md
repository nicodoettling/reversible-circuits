# M93 halfway checkpoint

Date: 2026-08-12.

## Frozen provenance

- observed `report.md` SHA-256:
  `df2983ca83c8fd92dec6406eb6341b4f07655304c491a7c74687649ceaa609ea`;
- observed `SHA256SUMS` SHA-256:
  `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703`;
- `sha256sum -c SHA256SUMS` passes all thirteen frozen entries;
- no cache was present in frozen M91 and no frozen file was changed.

## Independent mathematical audit so far

1. The quotient posterior identity retains both the orbit size and raw
   ordered-pair multiplicity.  Replacing an orbit sum by all `n` phases gives
   the factor `1/n`, even when `|O_A|=k`; the three repetitions are exactly
   the stabilizer correction.
2. Sampling two residual colors without replacement from ranks `(2m,m)`
   gives
   `alpha_0=m(m-1)/D`, `alpha_1=4m^2/D`, and
   `alpha_2=2m(2m-1)/D`, `D=3m(3m-1)`.  The `J=0` conditional law is the
   same literal middle-cycle pair law on both sides.
3. Direct ordered-factor enumeration shows all conditioned laws normalize
   after quotienting and retains exactly three lifts per oriented triangle
   and two per double.
4. The conditioned-Borel ratio proof has the right sign: the sequence
   `r_j=b_(j-1)/b_j` is strictly decreasing, the extra prefactor is also
   below one, hence `p_s<q_s` on common support.  Abel summation uses
   `D_0=D_(k-1)=0`, so no endpoint term is missing.
5. With `q_g=1_g/pi(g)`, one has `f=K(q_B-q_A)` and
   `||Kf||_pi^2=<q_B-q_A,K^4(q_B-q_A)>_pi`.  Expanding gives precisely the
   four denominators printed in M91.

## Exact audit

The fresh standard-library-only checker imports no M91 or predecessor code.
At `k=3,5` it reconstructs the raw kernel and quotient from ordered
transposition pairs, all conditional channels, the Abel measures, posterior
phase formula, second row, stationary norm, and four-step contrast over
`Fraction`.  It matches the frozen exact values for one-step TV, two-step TV,
scaled BA2 energy, source orbit sizes, color probabilities, and the channel
cross inner product.  The cross inner product is strictly positive at both
values, so universal channel orthogonality is exactly refuted.

## Provisional decision

`ACCEPT`, with no numbered material objection found.  The accepted scope is
only the balanced-family exact reduction.  `(BA2)`, its desired `O(k^-2)`
consequence, the general strict-edge estimate, H0, every sampler gap, and both
Terminals remain unresolved.

