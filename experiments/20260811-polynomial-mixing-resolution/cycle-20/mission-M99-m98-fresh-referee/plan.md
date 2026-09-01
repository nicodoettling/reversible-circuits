# M99 plan: fresh referee of M98

Date: 2026-08-12. Frozen M98 report SHA-256:
`fcf92cf8222aec8f4675b56fc86fda0cb676a37aac79320571eb7a8856e34476`.
Frozen M98 manifest SHA-256:
`2a8772686dfcfdc4d16103c4ff2b32ff5a0f610da5988184eb7410e69f81521e`.

## Objective and scope

Freshly audit M98's claimed infinite counterfamily to the one-step
nonfresh reset-defect sign for the auxiliary full nonlazy stationary-flow
parking-degree projection.  This is not an audit of a result for the
original lazy exact same-product `{3,4,5}` heat-bath chain.  Permutations
compose as `(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.

## Independent checks

1. Verify the frozen hashes and complete manifest without altering M98.
2. Reconstruct the root-composition and all-attachment-rank normalization,
   the contextual formula, and its right-heavy specialization.
3. Build the cleared defect polynomial directly in `Q[K]`, rather than
   inferring its degree from sampled values.  Check degree at most `32`,
   exact signs at `K=709,710`, and every Newton coefficient at base `710`.
4. Reconstruct the limiting mass/variance and canonical-basin energy
   decomposition.  Check the Cayley/Borel coefficient both by literal
   compositions and by the beta-integral finite sum.
5. Verify reachability of `(16,K,K-1,4)` from a fresh state and independently
   recurse through the finite DAG at `K=710` for weighted and unweighted
   full-resolvent survival.
6. Freeze exact machine-readable output, a halfway checkpoint, a nine-field
   referee report with numbered objections, a manifest, and hygiene checks.

All calculations are deterministic (`seed=null`) and use only Python's
standard library with exact `fractions.Fraction` arithmetic.  Bounded checks
are labeled finite; algebraic polynomial and Newton certificates carry the
infinite-tail conclusion.
