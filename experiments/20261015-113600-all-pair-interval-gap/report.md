# Arbitrary-pair lifted walk: scoped gap theorem

Verdict: **promote** the same-author S3 gap and improved all-N comparison,
provisionally pending independent review. The growing-N full-cycle N+1
gap remains **unresolved**. Pure Hurwitz without square refresh is not
a global sampler for arbitrary endpoints.

The user asked whether applying the displayed lifted move to any two gates
gives fast mixing. This study fixes uniform arbitrary position pairs, not
state-dependent selection among graph wedges. It retains the earlier
Hurwitz/square branch probabilities and uniform ordered-word target.

## Results

For the actual K_G=I/2+H_G/4+R_G/4, every nontrivial feasible fiber obeys
(2/m) E_KA <= E_KG <= 4m^2 E_KA. The upper proof uses uniform marginals
at every stage of a lifted transition, including after the heat bath.
It removes the M=binom(N,2) factor from the earlier comparison without
claiming a general gap theorem.

In S3, all feasible endpoints admit independent ternary prefix coordinates.
The transported exact pair heat bath becomes a uniform interval translation.
Fourier diagonalization gives its gap exactly 1/m. Actual K_G channel
weights lie between 1/2 and 3/4 of that kernel's nontrivial weights, so
1/(2m) <= gap(K_G) <= 3/(4m). Consequently mixing takes at most
ceil(2m[(m-1)log(3)/2+log(1/epsilon)]) completed pair updates. A completed
update uses at most 2m-3 primitive moves; its simulation cost is polynomial
too. No replacement global-refresh algorithm is introduced.

## Reproduction and exact validation

Command: `python3 -B experiments/20261015-113600-all-pair-interval-gap/check.py`.
Start commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`.
Python 3.12.3, standard library only. No random seeds: every check is
deterministic and exhaustive over its declared finite domain. The raw JSON
record pins the imported previous move implementation by SHA256.

- All 3276 S3 words at lengths 2 through 7: prefix bijections for all
  feasible endpoints, interval identities, exact transition ratios;
  299340 labeled move channels checked.
- All 9832 nonconstant Fourier modes at m=2 through 9: interval-sum cut
  counts and exact auxiliary gap 1/m.
- Identity S3,m=4 (27 states), S4,m=4 (120), S4,m=6 (3936): 478890
  labeled channels checked against primitive lifts, endpoint preservation,
  inverse channels, exact integer detailed balance and connectivity.
- All 4950 slot/length combinations through m=100: weighted comparison
  occurrence formula and the 4m^2 constant. The general proof is algebraic.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Uniform arbitrary-pair Hurwitz plus transported square refresh | Uniform fixed-product ordered words | yes, every tested primitive stage | yes, complete identity fibers connected in the specified cases; prior constructive proof covers all feasible endpoints | exact moves, uniform stationarity, connectivity, ternary Fourier comparison | promote scoped proofs; general gap unresolved |

The checks validate formulas and normalizations, not extrapolated mixing.
The N>=4 obstruction to this proof is precise: internal prefixes cannot be
chosen independently from parity classes, since not every odd permutation
is a transposition. No assertion that another coordinate system cannot work.

## Workspace changes

New in this turn:

- experiments/20261015-113600-all-pair-interval-gap/plan.md
- experiments/20261015-113600-all-pair-interval-gap/proof.md
- experiments/20261015-113600-all-pair-interval-gap/check.py
- experiments/20261015-113600-all-pair-interval-gap/results.jsonl
- experiments/20261015-113600-all-pair-interval-gap/claim_ledger.md
- experiments/20261015-113600-all-pair-interval-gap/report.md
- notes/project-map/integration-2026-10-15-all-pair-interval-gap.md

Already-dirty map files updated further for the new provisional record:

- PROJECT_MAP.md
- notes/project-map/COVERAGE.md
- notes/project-map/RESULTS.md
- notes/project-map/catalogue.json
- notes/project-map/inventory.json

Pre-existing untracked research files preserved without editing:

- experiments/20261014-133815-cycle-excess-one/plan.md
- experiments/20261014-133815-cycle-excess-one/proof.md
- experiments/20261014-133815-cycle-excess-one/tree_jump_proof.md
- experiments/20261014-133815-cycle-excess-one/check.py
- experiments/20261014-133815-cycle-excess-one/results.json
- experiments/20261014-133815-cycle-excess-one/tree_jump_check.py
- experiments/20261014-133815-cycle-excess-one/tree_jump_results.json
- experiments/20261014-133815-cycle-excess-one/claim_ledger.md
- experiments/20261014-133815-cycle-excess-one/report.md
- experiments/20261015-adjacent-gap-proof/plan.md
- experiments/20261015-adjacent-gap-proof/proof.md
- experiments/20261015-adjacent-gap-proof/check.py
- experiments/20261015-adjacent-gap-proof/results.json
- experiments/20261015-adjacent-gap-proof/claim_ledger.md
- experiments/20261015-adjacent-gap-proof/report.md
- notes/project-map/integration-2026-10-14-cycle-excess-one.md
- notes/project-map/integration-2026-10-15-adjacent-gap-proof.md

No manuscript, HANDOFF, GOAL_SPEC, skill, or prior research source changed.
