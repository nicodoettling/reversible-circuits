# Parallel Hurwitz layers: a proved layer-gap comparison

Verdict: **promote** the scoped author proofs, pending independent review.
For the user's independent ternary matching updates, a completed layer
has gap at least (1/48) min(m gamma,1) and at most (m/2) gamma, where gamma
is the one-cyclic-pair gap on the same Hurwitz orbit. The rare probability
of any one vector is absent from the comparison. The all-N full-cycle
mixing conjecture remains **unresolved**.

The exact convention, boundary correction, proof, dependency audits and
exceptional cases are in [proof.md](proof.md); individual statuses are in
[claim_ledger.md](claim_ledger.md). This record is new author work, not an
independent proof certification or a replacement for prior frozen results.

## Kernel and scope

Fix even m>=2 and a feasible product g. Products act rightmost first.
Choose one of the two cyclic perfect matchings uniformly. At each of its
m/2 pairs independently choose hold, positive Hurwitz or negative Hurwitz
with probability 1/3 each. There is no additional global hold. The target
is uniform on one ordinary Hurwitz orbit, not arbitrary global Omega_g.
A step is one completed layer, costing Theta(m) local updates.

For g=id the literal wraparound rule works. For arbitrary g it generally
changes the endpoint; the explicitly derived twisted boundary fixes this
while changing only the first and last gates. The main theorem applies to
that corrected fixed-endpoint walk. A separate section analyzes the earlier
square-heat-bath extension; it is not silently substituted for the pure
ternary proposal.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Pure ternary cyclic layers | uniform on one Hurwitz orbit | yes | no | products, inverse vectors, disjoint commutation, components, boundary lift, local eigenvalue types | promote comparison, no all-N gap |
| Naive seam on general g | uniform fixed-product words | identity only; general g fails | not applicable | 250/250 signed seam channels fail for minimal S5 cycle | reject arbitrary-endpoint formulation |
| Twisted seam on general g | uniform on one orbit | yes | no | all checked channels preserve endpoint and match the adjacent lift | promote formula |
| Explicit square-bath layer extension | global uniform Omega_g | yes | yes by inherited adjacent connectivity | boundary bath formulas and lifts; no new stochastic sampling estimate | keep separate; S3 gap >=1/256 proved from inherited bound |

## Proof obligations discharged

Local Hurwitz periods are 1,2,3, so each ternary local kernel has spectrum
in {1,0,-1/3}. Simultaneous diagonalization within a matching gives a
self-contained constant-factor comparison and bounds the negative
spectrum away from -1. Projection onto each local orbit and a checked
bounded-noncommutation lemma strengthen the gap improvement to order m
until saturation. Only adjacent constraints can fail to commute.

The primary dependency is Anshu-Arad-Vidick, arXiv:1602.01210v3,
Lemma 2 and Corollary 3. Its arbitrary-projector hypothesis, degree
parameter and unnormalized gap were checked against this application.
The special commuting-endpoint benchmark additionally uses
Caputo-Liggett-Richthammer, arXiv:0906.1238v4, Theorem 1.1, with unit-rate
cycle edges and discrete-time factor 2/(3m). Exact source links and
normalization translations are in the proof. Neither source supplies a
general transposition-bridge gap.

For even m>=4 and g a product of m disjoint transpositions, N>=2m, the
actual pure layer walk has gap Theta(m^-2), hence polynomial TV mixing.
Its support graph is fixed, so this is an order-mixing benchmark. With
square baths explicitly added, S3 has a constant gap per completed layer
and O(m+log(1/epsilon)) layer mixing, by the earlier adjacent gap.

The first missing lemma for growing full-cycle m=N+1 remains a polynomial
gap for the ordinary orbit walk. The layer/linear comparison shows that
parallelization does not change whether that gap is inverse polynomial.
Pure moves also cannot resolve global orbit weights. Faster marginal
mixing is not refuted by the unresolved full-chain gap.

## Exact validation and reproduction

Command:

```sh
python3 -B experiments/20261015-134144-parallel-hurwitz-layers/check.py
```

Repository commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`.
Python 3.12.3; standard library only; deterministic exhaustive enumeration,
so no random seeds. [results.jsonl](results.jsonl) records the command,
commit, Python version and hashes of both imported project scripts.

The run passed on **19,890 words and 1,062,144 complete layer channels**.
Cases include identity S3,m4 and S4,m4,m6; full-cycle S3,m2,m4 and
S5,m4,m6; N2,m2; a disjoint endpoint at N4,m2; and the 24 commuting
benchmark words at N8,m4. Every vector for each matching was checked.
All products, reverse-vector inverse maps, matching commutation and
ordinary/layer connected-component partitions agree. Every tested cyclic
move agrees with its ordinary Hurwitz sequence, whose intermediate
products also remain fixed.

All 1,770 scalar eigenvalue-count types for matching sizes 1 through 20
passed the comparison inequalities. There were also 24,498 twisted
square-boundary channels checked on the four declared identity/nonidentity
cases. The naive-seam counterexample is retained in raw output. These
are exact finite checks of formulas, not estimates of asymptotic gaps.

Boundary audit: odd identity m is infeasible; odd general m is outside
this perfect-matching schedule. The m0,m1,N2 cases are empty or singleton
as specified in the proof. At m2 the two cyclic slots coincide as local
kernels. Full-cycle m=N+1 fits the current schedule only when N is odd.

## Integration and changed-file inventory

The new six-file experiment is registered provisionally in the project map;
the integration receipt records exact fingerprints and validation. No
manuscript, HANDOFF, GOAL_SPEC, skill or prior research artifact was edited.
The inventory below distinguishes this turn's work from preserved dirty
files already present at the start of this turn.

Changed in this turn (new research and receipt):

- `experiments/20261015-134144-parallel-hurwitz-layers/check.py`
- `experiments/20261015-134144-parallel-hurwitz-layers/claim_ledger.md`
- `experiments/20261015-134144-parallel-hurwitz-layers/plan.md`
- `experiments/20261015-134144-parallel-hurwitz-layers/proof.md`
- `experiments/20261015-134144-parallel-hurwitz-layers/report.md`
- `experiments/20261015-134144-parallel-hurwitz-layers/results.jsonl`
- `notes/project-map/integration-2026-10-15-parallel-hurwitz-layers.md`

Map files updated in this turn, preserving earlier integrations:

- `PROJECT_MAP.md`
- `notes/project-map/COVERAGE.md`
- `notes/project-map/RESULTS.md`
- `notes/project-map/catalogue.json`
- `notes/project-map/inventory.json`

Pre-existing untracked research and receipts preserved unchanged:

- `experiments/20261014-133815-cycle-excess-one/check.py`
- `experiments/20261014-133815-cycle-excess-one/claim_ledger.md`
- `experiments/20261014-133815-cycle-excess-one/plan.md`
- `experiments/20261014-133815-cycle-excess-one/proof.md`
- `experiments/20261014-133815-cycle-excess-one/report.md`
- `experiments/20261014-133815-cycle-excess-one/results.json`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_check.py`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_proof.md`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_results.json`
- `experiments/20261015-113600-all-pair-interval-gap/check.py`
- `experiments/20261015-113600-all-pair-interval-gap/claim_ledger.md`
- `experiments/20261015-113600-all-pair-interval-gap/plan.md`
- `experiments/20261015-113600-all-pair-interval-gap/proof.md`
- `experiments/20261015-113600-all-pair-interval-gap/report.md`
- `experiments/20261015-113600-all-pair-interval-gap/results.jsonl`
- `experiments/20261015-122824-support-marginal-audit/check.py`
- `experiments/20261015-122824-support-marginal-audit/claim_ledger.md`
- `experiments/20261015-122824-support-marginal-audit/plan.md`
- `experiments/20261015-122824-support-marginal-audit/proof.md`
- `experiments/20261015-122824-support-marginal-audit/report.md`
- `experiments/20261015-122824-support-marginal-audit/results.jsonl`
- `experiments/20261015-adjacent-gap-proof/check.py`
- `experiments/20261015-adjacent-gap-proof/claim_ledger.md`
- `experiments/20261015-adjacent-gap-proof/plan.md`
- `experiments/20261015-adjacent-gap-proof/proof.md`
- `experiments/20261015-adjacent-gap-proof/report.md`
- `experiments/20261015-adjacent-gap-proof/results.json`
- `notes/project-map/integration-2026-10-14-cycle-excess-one.md`
- `notes/project-map/integration-2026-10-15-adjacent-gap-proof.md`
- `notes/project-map/integration-2026-10-15-all-pair-interval-gap.md`
- `notes/project-map/integration-2026-10-15-support-marginal-audit.md`
