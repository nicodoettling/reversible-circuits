# M272 plan: signed endpoint transport

## Objective

Resolve the remaining phase-sensitive endpoint estimate (`SET`) in the
first-cell reduction.  The intended target is the literal two-channel signed
quantity

```text
sum_{ell=2}^{(n-3)/2} | sum_K <w, T_{K,ell}> | = O(n^-2),
```

with every normalization, range, and exceptional case recovered from the
accepted source lock before the statement is promoted.  By the accepted
M91/M94 and M261/M264 reductions this is intended to be equivalent to the
phase-boundary-variation / fixed-cell derivative estimate (`PBV`/`FD`), not a
claim about the full sampler by itself.

## Source lock and claim discipline

- Required project sources: `HANDOFF.md`, `GOAL_SPEC.md`, the
  `reversible-circuit-sampler` skill, and its sampling/experiment references.
- Mathematical source lock: frozen M91, M94, M261, M264, and frozen M267
  (while M267 is under M270 audit).
- Every M267 identity used will be independently rederived.  An audited M267
  claim may be cited only with its exact hypotheses and normalization.
- Preserve the two Abel channels, `T/D` endpoint kinds, endpoint phase,
  owner-pair weights `kappa`, and the exterior factor of `n`.  Do not
  triangle-bound channels or kinds and do not replace endpoint data by only
  size/run profiles.
- The uniform statewise lag-`l1` envelope may be used only after the signed
  `D_u/q_u` cancellation has been made explicit.
- No inference from finite signs, generic total positivity/PF heuristics, or a
  single small case.  No FCL1, gap, mixing, or terminal claim unless SET is
  rigorously closed and all subsequent accepted implications are stated.

## Work plan

1. Recover the exact M91/M94 coefficient arrays and M261/M264 endpoint
   response formula, including parity, half-range, and all powers of `n`.
2. Reconstruct M267's endpoint-signature representation independently.
3. Define literal adjacent couplings for
   `Phi_{j,u}`/`Phi_{j,u+1}` and `Phi`/`Psi`, retaining channel, kind, phase,
   owner-pair, and residual-cycle labels.
4. Perform summation by parts or transport only after combining the signed
   channels and `T/D` kinds.  Track the exterior `n` factor explicitly.
5. Attempt a uniform `O(n^-2)` SET estimate.  Separately test an `SR/TPR`
   route only if it has a self-contained exact premise.
6. Falsify boundary/minimal cases and any proposed coefficient inequality by
   exact rational computation where useful.  Computation will test named
   identities only and will not substitute for an asymptotic proof.
7. If SET does not close, freeze the narrowest explicit coefficient/transport
   lemma or obstruction, with exact normalizations and the first unproved
   step.

## Deliverables

- `checkpoint.md` and a halfway update;
- a theorem/reduction/obstruction note;
- any exact checker plus machine-readable output and its command/environment;
- `report.md`, `fresh_audit_request.md`, `freeze_manifest.md`, and
  `SHA256SUMS`.

## Expected failure modes

- losing the cancellation by taking absolute values before summing channels;
- confusing cyclic phase with a linear boundary coordinate;
- suppressing owner-pair weights whose variation is the target signal;
- proving only an `O(n^-1)` estimate before the exterior factor of `n`;
- relying on a statewise lag envelope whose aggregate cost is too large;
- importing an unaudited M267 identity or an unproved sign-regularity claim.
