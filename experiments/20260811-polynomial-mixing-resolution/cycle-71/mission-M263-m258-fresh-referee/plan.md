# M263 Plan — Fresh Referee Audit of M258 TAV

## Objective

Independently audit M258's frozen exact two-run adjacent-variation (TAV)
theorem on its stated full domain.  M258 is immutable.  This mission does not
claim full DV or any downstream polynomial-mixing consequence.

## Target and status discipline

The ambient project target is the global fixed-length uniform law on
`Omega(N,m)`, with the lazy exact same-product `{3,4,5}` heat-bath kernel fixed
in `GOAL_SPEC.md`.  The object under audit is only the finite combinatorial TAV
lemma used in a proposed proof of a two-run coefficient bound.  Any accepted
statement will be labeled `proved` only at that lemma's exact scope; all
downstream uses remain unaudited here.

## Audit obligations

1. Verify M258's complete frozen inventory and top digest
   `753ef6932c3e5e5d69df7f429e8740710d77269357749d505dca0cf31e109ef8`.
2. Re-derive the cyclic seam-pattern counts and placement-summed two-spike
   formula.
3. Audit the reflected `Wtilde` orientation, coefficient ratios,
   unimodality, and total variation without importing M251's `W` argument.
4. Check every cutoff endpoint, especially `k=3`, `ell>D-2`, and `ell=k`.
5. Check Borel ratio/Stirling constants in the spike-mass estimate.
6. Check raw paired variation, denominator normalization, and the exact
   support/pair list for `J`.
7. Check the declared parameter domain and all empty-spike cases.
8. Write a compact independent exact checker for falsification only; it may
   read no M258 code or output.
9. Freeze an `ACCEPT` or `REJECT` report with numbered objections (including
   explicit `none` if accepted), SHA-256 inventory, and a top digest.

## Expected failure modes

- cyclic wraparound gives a fifth seam pattern or changes a multiplicity;
- reflected orientation silently uses the wrong triangular kernel;
- a cutoff jump is omitted at `ell=k` or outside the active head range;
- the Borel comparison loses a constant or assumes a false monotonicity;
- normalized paired variation is inferred from an unnormalized estimate;
- a `J` spike survives outside the theorem's stated rank/domain;
- the frozen inventory or digest does not reproduce.

## Commands and reproducibility

Record exact commands in `checkpoint.md`/`report.md`.  The independent checker
will be deterministic and report the Python version, tested ranges, and raw
JSON output.  No random seed is needed because the check is exhaustive.

