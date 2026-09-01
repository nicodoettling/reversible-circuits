# M295 plan: GOCI signed composition

## Objective

Independently reconstruct the accepted M285/M287 positive-composition formula
for the two gapped owner-correlation inequalities, then seek one genuine
all-rank signed coefficient pairing.  The target is a standalone analytic
lemma proving `GOCI_j >= 0` (channelwise if possible, otherwise through an
explicit cross-channel/minority-mass comparison).

## Frozen inputs to verify

- M266/M268: full decorated-variable/positive-composition assembly.
- M274/M277: minority-sign closure and its audited scope.
- M280/M283: channel-combined positivity conventions and failed routes.
- M285/M287: exact GOCI reduction, owner-autocorrelation repair, coefficient
  normalizations, and admissible lag range.

## Scope and safeguards

- Target distribution: uniform fixed-length transposition identity bridge,
  only through the already-reduced algebraic GOCI obligation.
- Preserve the accepted `beta_j`, triangle factor `1/3`, square/negative
  factor `1/4`, absence of an extra factor of `n`, repaired nonnegative owner
  autocorrelations, and admissible lags.
- Do not reuse signed-PSD, MON, FOSD, or raw atomwise positivity.
- Name exactly one candidate coefficient inequality before computation.
- If a finite check is useful, use at most one compact new exact rank (`k=5`
  or `k=7`) and treat it only as a falsifier.
- Make no CP/OS+/MS/FCL1, spectral-gap, mixing, or Terminal inference without
  an all-rank implication and fresh independent audit.

## Deliverables

- `checkpoint.md`: frozen reconstruction and the single named candidate.
- `proof.md`: analytic proof or the first standalone failed coefficient lemma,
  with exact counterexample if found.
- optional compact exact script and machine-readable output for one rank.
- `report.md`: status-labelled verdict, dependency list, exceptional cases,
  and next lemma.

## Expected failure modes

- confusing product coefficients with normalized probabilities;
- introducing a spurious channel-two `1/2` or global `n` factor;
- extending lag-zero autocorrelation repair to inadmissible interior lags;
- mistaking positive entries or finite-rank positivity for PSD/all-rank GOCI;
- proving a pairing that silently assumes monotonicity already refuted.

