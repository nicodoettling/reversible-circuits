# Weighted support marginal: correct limit, unresolved growing-N rate

Verdict: **promote** the scoped lumpability obstruction and exact projection
identities, provisionally pending independent review. **Inconclusive** for
the actual graph-marginal polynomial-mixing conjecture. The correct limiting
law is known; an inverse-polynomial rate in growing N is not proved here.

The user explicitly weakened the target from circuit mixing to support
mixing. This study preserves vertex labels as previously requested, retains
edge multiplicities, and also checks the simple-support projection. The
kernel remains the actual half-lazy uniform arbitrary-pair lifted Hurwitz
and square-refresh walk. No fiber resampling stage is added.

## Findings

The correct graph law is A_g(G)/|Omega_g|, where A_g counts distinct ordered
words realizing G and endpoint g. The usual raw support map is not the
tree/factorization bijection: at minimal N4 there are 16 words, 12 graphs,
and nonconstant weights. Arbitrary-pair selection does not remove the
gate-order dependence of the next graph.

An explicit minimal N4 witness has equal support and probabilities 0 and
1/24 of reaching a specified star in one step. A second witness lies in
the requested N4,m5 cycle family and gives 1/80 versus 0 for a specified
weighted graph. Both also yield a failure for simple labeled graphs.
These are complete finite counterexamples to strong lumpability, not
counterexamples to rapid marginal mixing.

The averaged stationary-flow graph kernel is reversible for the desired
weights. However, its two-step return differs from the actual process
even from a uniform fiber lift. The exact positive difference is a
within-fiber variance; for the minimal star it is 1/288. A general
four-state construction proves that a constant stationary-projection gap
can coexist with exponentially slow observed-marginal convergence.

A sufficient condition that can be weaker than the full circuit gap is a
Poincare inequality on the K-invariant span of graph observables. The
proof yields d_graph(t)<=sqrt(|Omega_g|) exp(-t/p)/2. Establishing a
polynomial p at growing N remains the named missing lemma. Graph-only
one-step distance contraction cannot hold for every pair because the
same-support witnesses have zero initial graph distance and different
next-graph laws.

The standard cut-and-join source was inspected only to verify its model:
Blumberg arXiv:1109.3915v1, Definitions 2 and 5. It projects a changing
permutation onto its cycle lengths. Here g stays fixed, and that theorem
does not give the required support marginal. No broad literature search
or claim of novelty/absence is made.

## Exact checks and reproduction

Command: `python3 -B experiments/20261015-122824-support-marginal-audit/check.py`.
Commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`. Python 3.12.3;
standard library only; deterministic exact enumeration, no random seeds.
Raw output is results.jsonl and pins both imported source hashes.

| Endpoint | N,m | Words | Weighted support graphs | Fibers with differing graph rows |
|---|---|---|---|---|
| Full cycle | 3,4 | 27 | 12 | 9 |
| Full cycle | 4,3 | 16 | 12 | 4 |
| Full cycle | 4,5 | 640 | 142 | 122 |
| Identity | 3,4 | 27 | 9 | 6 |
| Identity | 4,4 | 120 | 33 | 27 |
| Identity | 4,6 | 3936 | 189 | 171 |

All 4766 words passed endpoint and exact integer detailed balance checks.
All stationary-flow graph weights and the two-step variance identities
passed. No floating-point spectra or asymptotic extrapolations are used.
A trial S3 triangle-presence event did not distinguish the selected
same-support pair (both 1/9); that negative trial is retained in the raw
output. Full graph rows nevertheless distinguish other events.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Actual uniform all-pair lifted Hurwitz/square walk, observed only through support | Compatible-order-weighted support marginal | yes on all listed identity cases | prior constructive full-chain proof; square branch retained | exact endpoint, uniform balance, support weights, failure of lumpability and two-step closure | correct limit; general polynomial marginal rate unresolved |

Positive scope retained: S3 all lengths inherits the previous polynomial
full-chain bound; arbitrary-N identity at m2 is an exact quarter-refresh
graph chain; singleton and parity exceptions are stated in the proof.

## Workspace changes

The complete changed-file inventory is appended below. Existing research
artifacts are preserved; only the five already-dirty map files are updated
further. No manuscript, HANDOFF, GOAL_SPEC, skill, or previous proof changes.

New in this turn:

- experiments/20261015-122824-support-marginal-audit/check.py
- experiments/20261015-122824-support-marginal-audit/claim_ledger.md
- experiments/20261015-122824-support-marginal-audit/plan.md
- experiments/20261015-122824-support-marginal-audit/proof.md
- experiments/20261015-122824-support-marginal-audit/report.md
- experiments/20261015-122824-support-marginal-audit/results.jsonl
- notes/project-map/integration-2026-10-15-support-marginal-audit.md

Already-dirty tracked map files updated further:

- PROJECT_MAP.md
- notes/project-map/COVERAGE.md
- notes/project-map/RESULTS.md
- notes/project-map/catalogue.json
- notes/project-map/inventory.json

Pre-existing untracked files preserved without editing:

- experiments/20261014-133815-cycle-excess-one/check.py
- experiments/20261014-133815-cycle-excess-one/claim_ledger.md
- experiments/20261014-133815-cycle-excess-one/plan.md
- experiments/20261014-133815-cycle-excess-one/proof.md
- experiments/20261014-133815-cycle-excess-one/report.md
- experiments/20261014-133815-cycle-excess-one/results.json
- experiments/20261014-133815-cycle-excess-one/tree_jump_check.py
- experiments/20261014-133815-cycle-excess-one/tree_jump_proof.md
- experiments/20261014-133815-cycle-excess-one/tree_jump_results.json
- experiments/20261015-113600-all-pair-interval-gap/check.py
- experiments/20261015-113600-all-pair-interval-gap/claim_ledger.md
- experiments/20261015-113600-all-pair-interval-gap/plan.md
- experiments/20261015-113600-all-pair-interval-gap/proof.md
- experiments/20261015-113600-all-pair-interval-gap/report.md
- experiments/20261015-113600-all-pair-interval-gap/results.jsonl
- experiments/20261015-adjacent-gap-proof/check.py
- experiments/20261015-adjacent-gap-proof/claim_ledger.md
- experiments/20261015-adjacent-gap-proof/plan.md
- experiments/20261015-adjacent-gap-proof/proof.md
- experiments/20261015-adjacent-gap-proof/report.md
- experiments/20261015-adjacent-gap-proof/results.json
- notes/project-map/integration-2026-10-14-cycle-excess-one.md
- notes/project-map/integration-2026-10-15-adjacent-gap-proof.md
- notes/project-map/integration-2026-10-15-all-pair-interval-gap.md
