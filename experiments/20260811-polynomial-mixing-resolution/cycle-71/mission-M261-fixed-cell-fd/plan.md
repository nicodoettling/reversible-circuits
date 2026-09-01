# M261 plan: fixed-cell closure after PCS

## Objective

Resolve exactly the independent fixed-cell observable obligation left after the
accepted PCS route, for odd `k >= 3` and `n=3k`:

1. prove the fixed-difference estimate

   ```text
   k^2 sum_{y=1}^{n-4} |z_k(y+1)-z_k(y)| = O(1),
   ```

   or
2. prove the accepted M168 minority-sign substitute

   ```text
   k min(P_k,N_k)=O(1),
   ```

while retaining the exact phase law and both channels/kinds.

If neither route closes, freeze the strictest exact coefficient/observable
reduction and isolate the first unproved statement as a standalone lemma.

## Declared target and scope

The mathematical target is the fixed-cell observable under the exact
fixed-length bridge law used by the accepted predecessor chain.  This mission
does not alter or implement a Markov kernel.  It will not assume full DV,
infer FCL1 from PCS alone, or claim a spectral-gap, mixing-time, or Terminal
conclusion.

## Required dependency audit

Verify the immutable ledgers and freeze manifests for M161/M166, M168/M171,
M174/M178, and M256/M259 before relying on their claims.  Record exact digests
and any discrepancy in `dependency_audit.md`.

## Work order

1. Read the project source of truth and only the relevant fixed-cell sections.
2. Audit the cited immutable missions.
3. Reconstruct the exact phase law, both channels, and both kinds from frozen
   artifacts.
4. Derive an exact coefficient/observable reduction before any finite
   diagnostics.
5. Attempt FD-bound first where the reduction exposes a summable discrete
   derivative; in parallel mathematics, test whether the M168 minority-sign
   functional has a direct cancellation formula.
6. Check boundary cases `k=3`, odd parity, endpoint rows, and exact indexing.
7. Freeze a proof or the strictest reduction, then request a fresh audit.

## Claim labels and expected failure modes

- `proved`: exact algebra or a complete uniform estimate.
- `conditional`: only if an explicitly named predecessor hypothesis is used.
- `empirical`: finite arithmetic, never promoted to a uniform bound by itself.
- `unresolved`: the first missing standalone lemma.

Expected failure modes are loss of one channel/kind, replacing the exact phase
law by an averaged surrogate, hidden endpoint terms, and deriving FCL1 from PCS
without an independent fixed-cell estimate.

## Reproducibility

Any nontrivial finite diagnostic will be added only after the exact reduction,
with command, Python version, parameters, and machine-readable output recorded
in this directory.

