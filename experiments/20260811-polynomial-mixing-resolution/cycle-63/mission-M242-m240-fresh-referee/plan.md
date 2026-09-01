# Mission M242 plan: fresh audit of M240

## Objective

Freshly and immutably referee frozen mission M240's claimed strict conditional
all-rank `Z_2` reduction.  The only permissible positive verdict is acceptance
of the stated conditional reduction.  This mission will not claim an
all-rank closure, an every-color comparison, a congestion or spectral-gap
bound, polynomial mixing, or a terminal resolution.

## Source lock

- Repository operating guide and project skill.
- `HANDOFF.md`, `GOAL_SPEC.md`, and the sampling-problem reference.
- Frozen M240 directory
  `cycle-62/mission-M240-all-rank-z2-closure/`, verified against its full
  `SHA256SUMS` inventory before substantive audit.
- Only the accepted predecessor artifacts cited by frozen M240, with their
  frozen hashes checked before use.
- Relevant manuscript sections only if M240 makes a manuscript-dependent
  claim (none assumed at initialization).

## Audit obligations

1. Check M240's full frozen inventory and cited-predecessor provenance.
2. Reconstruct the exact IDL statement at every position and decide whether
   it is equivalent to the remaining DPS comparison.
3. Check chronological Hurwitz conventions, square-transport identities and
   signs, direct-child equalization, and the disjoint-nonchild case.
4. Check the `Q` induction indices and epsilon requirement.
5. Check the terminal `B_d` four-block carrier, the application of `Q^{-1}`,
   the conditional length `4(d-v-1)+5`, and all closed/fixed-edit boundary
   cases.
6. Write and run a clean-room symbolic checker that imports neither M240 code
   nor M240 data.
7. Issue an explicit `ACCEPT` or `REJECT` verdict with numbered objections;
   then freeze proof/audit, checker, results, report, manifest, and hashes.

## Falsification policy

Search first for convention, index, sign, support, and boundary failures.
Any material gap in the strict conditional reduction forces `REJECT`.
Finite or symbolic agreement alone cannot establish the all-rank statement.

