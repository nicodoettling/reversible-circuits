# Mission M173 plan: aggregated modal-vector recursion

Date: 2026-08-13 (UTC)

## Single target

In the exact actual-history reset recursion frozen by M162/M165, derive the
parent recursion for every retained beta-binomial observation after writing

```text
Phi = M + (u-p) C / sigma^2 + Z,
```

including all Hilbert-space cross terms and the killed `a=d` atom. Then prove
or refute one uniform terminal/exterior aggregate inequality controlling the
re-emergent high-Jacobi tail after exact Cayley weighting.

If the global aggregate statement cannot be closed, the mission will instead
close the terminal `h=1` sector as a standalone lemma or exhibit an exact
reachable/operator obstruction. Unrestricted operator examples will be
distinguished from actual-history states.

## Source lock

Read the repository source of truth and the frozen M147/M151, M157/M160,
M162/M165, and M167/M170 artifacts. Verify their manifests and preserve their
normalizations. Any disagreement will be reported rather than silently
resolved.

## Method

1. Reconstruct the actual-history state, Jacobi conventions, reset/retained
   branches, killed atom, and exterior Cayley weights.
2. Derive the exact retained-child-to-parent update for `(M,C,Z)` and expand
   all norm/cross terms without scalarizing the vector geometry.
3. Sum the resulting high-tail charge with the exact terminal/exterior
   weights. Use M167's factorial bound only as a summability input, not as a
   sign or budget inequality.
4. Test one precisely stated aggregate inequality algebraically; use a compact
   exact checker only where it materially audits the identities.
5. Check `L=0`, absent first mode, killed branch, terminal `h=1`, and minimal
   admissible degrees. Do not enumerate `L=7` or run a broad scan.

## Claim discipline

- Target distribution: the same actual-history beta-binomial conditional law
  used in the accepted reset-frontier artifacts; this mission does not alter
  the Markov kernel.
- No weighted/root-mean claim, spectral-gap claim, Terminal claim, or
  polynomial-mixing inference.
- Every example is labeled `actual-history`, `reachable`, or `unrestricted
  operator`.

## Deliverables

- `checkpoint.md`, initialized now and extended at halfway.
- A theorem/proof note with exact formulas, dependencies, status, boundary
  checks, and the first unresolved lemma.
- A compact exact checker and machine-readable output only if useful.
- A nine-field `report.md`, freeze manifest, SHA-256 ledger, and hygiene check.
