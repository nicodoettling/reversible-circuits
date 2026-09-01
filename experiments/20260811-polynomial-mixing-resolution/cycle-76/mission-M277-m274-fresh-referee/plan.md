# M277 plan: fresh immutable referee of M274

Date: 2026-08-14 UTC.

## Objective and target

Audit frozen M274 independently and issue an evidence-backed `ACCEPT` or
`REJECT` verdict.  The mathematical target is limited to the balanced
first fixed cell of the auxiliary uniform minimal-factorization law for the
long cycle under the nonlazy cyclic rank-two quotient kernel.  It is not the
global identity-word target and not the lazy exact `{3,4,5}` heat-bath
chain.

The audit will verify whether M274 correctly:

1. states and proves the exact equivalence between positive-column sums
   `(PCS)` and the minority-sign statement `(MS)`;
2. retains the raw per-lag, channel, triangle/double kind, topology, phase,
   and normalization formulas;
3. handles reflection, endpoint lags, and the caveat that the phase total is
   positive without promoting it to atomwise positivity;
4. reports the exact `k=9` one-switch-positive `(OS+)` result and the
   `MON/FOSD` counterexamples correctly;
5. refutes raw atomwise positivity for arbitrary odd rank by a genuine
   counterfamily rather than finite extrapolation; and
6. identifies channel-combined column positivity `(CP)` as the first
   plausible stronger lemma while keeping `OS+` and `MS` unresolved.

## Immutable source protocol

- Verify the supplied M274 `SHA256SUMS` digest
  `c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e`
  and every payload before reading mathematical claims.
- Verify every dependency named by M274 against its own checksum ledger.
- Do not edit M274 or any dependency.
- Reconstruct the formulas from the underlying completion-count and
  fixed-cell definitions before comparing them with M274.
- Build a compact, no-import checker only after the analytic derivation is
  fixed.  It must use standard-library exact arithmetic and must not import
  M274 code.

## Audit plan

1. Pass the M274/dependency hash gates and inventory the precise claim chain.
2. Re-derive PCS, MS, their equivalence, reflection, endpoints, and the
   positive phase-total caveat.
3. Re-derive raw conditional laws and the per-lag/channel/kind/topology
   coefficient formulas with every normalization explicit.
4. Inspect and independently rerun the smallest decisive checks for
   `k=9`, `MON/FOSD`, and arbitrary-odd-rank atomwise positivity.
5. Write a clean no-import compact checker encoding only the audited
   identities and counterexamples.
6. Record every objection as fatal, major, or minor; freeze an
   `ACCEPT/REJECT` verdict, report, manifest, checksum inventory, and fresh
   synthesis request.

## Proof and scope firewall

- Finite signs prove only the displayed finite ranks.
- A positive sum over phases does not imply each phase atom is positive.
- Generic total positivity, PF, stochastic ordering, or monotonicity cannot
  be imported without an exact premise.
- No PCS-to-FCL1, gap, mixing, or Terminal inference is allowed.
- `OS+`, `MS`, and `CP` remain open unless the audit independently
  supplies a uniform proof.

## Deliverables

- `checkpoint.md` and `halfway_checkpoint.md`;
- an independent reconstruction/audit note;
- a clean no-import checker and machine-readable exact results;
- `report.md`, `freeze_manifest.md`, `fresh_synthesis_request.md`, and
  `SHA256SUMS`.

## Completion status

All six audit steps completed.  The final verdict is `ACCEPT WITH
NONMATERIAL CORRECTIONS`; exact objections and scope firewalls are frozen in
`report.md`.
