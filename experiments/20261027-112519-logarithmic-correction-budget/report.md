# A logarithmic budget: endpoint balance does not give circuit balance

Verdict: **keep** the counting results and explicit obstructions; **reject**
one-step Hamming contraction and the unweighted exact correction lift as
general routes to a uniform relaxed sampler. Growing-N polynomial mixing
remains **unresolved**. Author proofs are provisional pending independent
review. No simulation, spectral computation, new dependency or subagent
was used.

The requested target is uniform on length-m transposition words with
endpoint defect at most k=Theta(log N), centered at identity. Products
act rightmost first; the tested kernel holds with probability 1/2 and
otherwise refreshes a uniformly selected coordinate from its exact legal
gate set. Main word statements use even m,k. Examples set k=2ceil(log2 N).

## Findings

**Proved obstruction to contraction.** For explicit neighboring words
whose endpoints both consist of k disjoint transpositions, the optimal
one-step Hamming transport cost is

    1 + (m-2k-1)/(2m(k+1)).

It exceeds one for m>2k+1, including logarithmic k. Fixed positive
coordinate weights do not fix this. This refutes a coupling proof
criterion, not rapid mixing. Boundary conditionals still have only
O(k^2) legal gates, despite M=binom(N,2) available gates globally.

**Proved counting lemma and comparison limitation.** When N>=2k,
every feasible endpoint has at least k! length-k corrections; a product
of k disjoint transpositions has exactly k!. For even k the identity
has at least M^(k/2) corrections. Hence the worst-case completion-weight
ratio is exp(Theta((log N)^2)) at logarithmic k. The constant-budget
comparison cannot simply be extended using a polynomial density ratio.

**Proved positive endpoint result.** The product of k iid uniform
transpositions is within

    Delta = binom(k,2) * 2(2N-1)/(3N(N-1))

in TV of the uniform permutation law on the parity-compatible correction
ball, with the bound capped at one. This is O(log^2 N/N), despite the
large pointwise density range. It concerns endpoint permutations.

**Proved failure of the corresponding circuit lift.** At m=k, compare
uniform length-k words pi_k with the prefix nu_k of a uniform exact
identity word of length 2k. Counting the event that the prefix endpoint
is a k-edge matching gives

    TV(pi_k,nu_k) >= 1-2k(k-1)/(N-1)-2^k/binom(2k,k).

This tends to one for logarithmic k. Thus near-uniform correction
endpoints do not make prefixes of uniform exact extensions nearly
uniform. This example is especially useful because the relaxed heat
bath itself is EASY at m=k: independent coordinate refresh with gap
1/(2m). A failure of this lift is not a failure of the relaxed dynamics.

For illustration, evaluating the proved bounds at N=2^20,k=40 gives
endpoint-law TV at most 0.000992, but circuit-law TV at least 0.997024.
The multiplicity ratio is at least 2^620.84. These are formula
evaluations, not measurements of a large chain.

**Conditional transfer.** If all length-m endpoint counts in the ball
lie within a multiplicative 1±epsilon of a common value, the lifted and
uniform relaxed word laws have TV at most Delta+2epsilon. The count
hypothesis is explicit and unproved at arbitrary m; it fails with small
epsilon at m=k. Even a close static law supplies no mixing bound.

## What remains

The missing result is a polynomial Poincare bound for the actual H_k
kernel at m>k. A possible route must control dynamics within endpoint
classes and transitions between them, including atypical states.
The matching-endpoint subset has constant correction multiplicity, but
its stationary mass and restricted dynamics for arbitrary m are not
established here. Neither its connectivity nor a gap is assumed.

The earlier all-budget connectivity result remains a separate qualitative
input. No new proof of general rapid or torpid mixing, and no transfer to
the original exact {3,4,5} kernel, is claimed.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| H_k single-coordinate heat bath | uniform relaxed length-m words | intentionally relaxed; defect<=k | may change endpoint, so exact-orbit label is not its state partition | explicit conditionals and optimal Hamming witnesses | keep; rate unresolved |
| Prefix of uniform exact length-m+k word | proposed uniform relaxed prefix | suffix restores identity | no local walk specified | exact correction weights; asymptotic TV counterexample | reject proposed uniformity |
| k iid transpositions | approximate uniform correction-ball permutation | defect<=k | not a circuit-fiber sampler | minimum counts, elementary-symmetric coefficient DP | keep endpoint-only theorem |

## Reproducibility and scope of checks

Run:

    python3 -B experiments/20261027-112519-logarithmic-correction-budget/check.py

The 73 JSONL records include a manifest and 72 deterministic records:
45 permutation-state DP cases at N=2,...,6 and lengths 0,...,8;
nine prefix-lift bias checks; four conditional transfers; six Hamming
witnesses with 21 representative coordinate classes; six coefficient
DP cases through N=4096; and two evaluations of proved bounds.
Largest permutation-state space: 720. The run took under one second
in this workspace, using Python 3.12.3 and only its standard library.
No random seed applies. Commit and current script hash are in the manifest.

Checks include the standard identity counts S3,m4=27, S4,m4=120 and
S4,m6=3936, parity and correction support, minimal matching counts,
exact TV computations and conditional gate sets. No production sampler
logic changed, so trajectory marginals or stochastic diagnostics would
not test an additional implementation claim. General conclusions rest
on proof.md, not these finite checks. Boundaries m0,m2,N2, odd length
and minimal-length matching endpoints are discussed in proof.md §6.

Map registration is provisional. HANDOFF, GOAL_SPEC and the manuscript
are unchanged. The procedural skill reference now distinguishes endpoint
and word laws, and pointwise density from TV and spectral comparison.

## Complete changed-file inventory

Files created for this investigation:

- experiments/20261027-112519-logarithmic-correction-budget/plan.md
- experiments/20261027-112519-logarithmic-correction-budget/proof.md
- experiments/20261027-112519-logarithmic-correction-budget/check.py
- experiments/20261027-112519-logarithmic-correction-budget/results.jsonl
- experiments/20261027-112519-logarithmic-correction-budget/claim_ledger.md
- experiments/20261027-112519-logarithmic-correction-budget/report.md
- notes/project-map/integration-2026-10-27-logarithmic-correction-budget.md

Shared files already dirty at turn start, extended for this investigation:

- .codex/skills/reversible-circuit-sampler/references/experiments.md
- notes/project-map/catalogue.json
- notes/project-map/inventory.json
- notes/project-map/RESULTS.md
- notes/project-map/COVERAGE.md

Pre-existing uncommitted artifacts preserved without edits:

- experiments/20261027-104714-relaxed-heatbath-comparison/plan.md
- experiments/20261027-104714-relaxed-heatbath-comparison/proof.md
- experiments/20261027-104714-relaxed-heatbath-comparison/check.py
- experiments/20261027-104714-relaxed-heatbath-comparison/results.jsonl
- experiments/20261027-104714-relaxed-heatbath-comparison/claim_ledger.md
- experiments/20261027-104714-relaxed-heatbath-comparison/report.md
- notes/project-map/integration-2026-10-27-relaxed-heatbath-comparison.md

These 19 changed/untracked files are not committed in this turn.
