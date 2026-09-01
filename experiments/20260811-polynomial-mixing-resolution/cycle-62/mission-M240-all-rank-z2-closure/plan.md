# M240 plan: all-rank route-normal Z2 closure

## Objective

Decide the precise all-rank endpoint statement suggested by the accepted
finite M231/M234 and M236/M237 route-normal formula.  The intended output is
either a symbolic proof, for every admissible rank and ordinary odd edit, that
the chronological signed-Hurwitz word prescribed by `Z_2` carries the exact
rooted-DPS source to its exact target, or the first exact symbolic obstruction
or counterfamily.

## Source lock and accepted inputs

Read and treat as controlling:

- `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, and its sampling/experiment
  references;
- ledger L-0278 (M214/M218), L-0281 (M220/M223), L-0283 (M225/M228),
  L-0286 (M231/M234), and L-0287 (M236/M237);
- the frozen proof/checker artifacts in those missions.

Only their ledgered conclusions are inputs.  In particular, the two finite
passes do not supply induction, an all-rank route, an every-color statement,
or a length/gap/mixing theorem.

## Exact theorem target

Fix arbitrary admissible rank `d`, the accepted rooted one-leaf extension
template, and an ordinary odd edit `i=2v-3`.  Define the rooted-DPS source and
target words under the repository's literal factor order and chronological
right-Hurwitz convention.  Define the late-ancestor bit, path-ascent bit,
larger-child sign vector `epsilon`, the route-normal quotient

```text
Z_2=("closed",)                    if late OR ascent,
    ("open",v,epsilon)            otherwise,
```

and its word `1` in the closed case and
`Q(v,epsilon) B_d Q(v,epsilon)^-1` in the open case.  Prove endpoint equality
by literal local carrier identities and an algebraic contour invariant, not by
finite enumeration.  Treat the minimal ranks `d=5,6,7`, new-versus-inherited
edits, and fixed boundary/internal edits separately where they lie outside the
ordinary theorem.

## Method

1. Reconstruct the exact DPS source/target maps and signed-Hurwitz action from
   the frozen code and proof artifacts.
2. Extract the symbolic carrier, double-inverse, and single-inverse identities
   and state their support/chronology precisely.
3. Track the entire rooted contour along the stopped path.  Derive a local
   recurrence for the endpoint defect and show that each larger-child bit
   contributes exactly the corresponding signed transport pair in `Q`.
4. Prove the closed cancellation and open terminal carrier cases uniformly in
   `d`; if any identity fails, isolate the first symbolic missing identity and
   construct a parameterized exact witness.
5. Use a small independent symbolic checker only to validate literal identities
   and boundary substitutions.  Do not use another broad finite-rank census as
   a substitute for proof.

## Deliverables and claim discipline

- `checkpoint.md` and a halfway update;
- `all_rank_z2_closure.md` or `symbolic_obstruction.md`;
- optional symbolic identity checker plus machine-readable results;
- `report.md`, `freeze_manifest.md`, `SHA256SUMS`, and an audit request.

Any successful statement is only an all-rank ordinary-edit endpoint theorem
for the declared one-leaf template.  It does not imply every-color coverage,
polynomial route length or congestion, an original-chain gap, polynomial
mixing, or either Terminal.

