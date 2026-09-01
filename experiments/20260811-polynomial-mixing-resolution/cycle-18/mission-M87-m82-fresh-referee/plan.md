# M87 plan: fresh referee of frozen M82

Date: 2026-08-12. This directory is owned only by M87.

## Objective and target

Independently referee frozen M82's reset-substochasticity report. The
background target is uniform on `Omega(N,m)` for the literal lazy exact
same-product `{3,4,5}` heat-bath kernel, but the audited operator is only the
full nonlazy stationary-flow parking-degree projection in the minimal
long-cycle sector. No result for the original heat-bath chain is presumed.

The frozen M82 report and manifest must first match the coordinator-supplied
SHA-256 digests, and every manifest entry must verify.

## Required checks

1. Reconstruct independently the root-composition law, contextual mean,
   negative-hypergeometric inheritance, canonical reset current/capacity,
   strict phase descent, and `K_reset=(I-D)^(-1)J_can` normalization.
2. Check the exact right-heavy reset property and reachable `(K,R)` closure.
3. Prove or find a flaw in the universal split-mass bound `q<=2/3`, including
   the excluded `(1,1)` case and the active-reset quantifier.
4. Reproduce the smallest decisive exact all-context eliminated-row witness,
   and distinguish it from the right-heavy conjecture.
5. Reproduce independently the raw constant, `d=0`, and `d=1` Bellman
   refutations. Audit the `d=2` downward-floor certificate exactly, including
   term counts and the comparison of the rational floor with the parent.
6. Compare grouped Cayley sums with direct composition enumeration on a fresh
   bounded grid, without importing any M82 or predecessor code.
7. Verify the conditional implication from `K_reset W<=W`, with
   `W=(1-q)K/(R+1)`, to reset-epoch mass at most `3` and separated occupation
   at most `3eP^3(1+log P)`.
8. Check that M82 claims neither the open weighted lemma nor a `Pbar` gap,
   original-chain gap, or Terminal A/B.

## Independent computation and expected failure modes

Use only the Python standard library, exact `fractions.Fraction` arithmetic,
and deterministic exhaustive enumeration. The independent script will import
no M82/M79 module. Floating conversions are presentation only. Likely failure
modes are a missing `q_parent` divisor, a grouped-tail multiplicity error,
confusing all reachable contexts with right-heavy seeds, or an invalid floor
direction/term count in the rank-120 certificate.

## Deliverables and freeze

Write `checkpoint.md`, an independent audit script, machine-readable JSON,
and a nine-field `report.md` ending in `ACCEPT` or `REJECT` with numbered
material objections. Record commit, exact commands, Python version, seed
status, dependencies, and all hashes in `SHA256SUMS`. Do not edit M82 or any
shared project file.
