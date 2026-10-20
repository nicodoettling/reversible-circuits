# Excess-one circuit walks: proof attempt and separate fast refresh

Verdict: **keep** the scoped proofs and explicit obstruction. **Inconclusive**
for the requested growing-N pair-slide hybrid at m=N+1. No result is
independently certified. The stronger alternate-kernel theorem is kept
separate and registered provisionally.

## Outcome

The original hybrid P=(K_A+K_G)/2 is polynomially mixing on S_3 for every
feasible endpoint and length; an explicit prefix-coordinate coupling gives
O(m log(m/epsilon)) for K_A and a spectral comparison gives O(m^2+
m log(1/epsilon)) for P. For growing N at m=N+1, selecting available
equal-edge pairs with the exact Metropolis correction accelerates only
the square branch by Theta(N^2). The full-chain Poincare inequality is
still missing. Exact support-multigraph restrictions can be frozen, so
that particular projection/restriction proof route fails.

A different completed-macro kernel has a full proof for growing N. Draw
a uniform minimal word, insert 2h arbitrary gates, normalize the endpoint
to the desired full cycle when possible, and accept with probability
1/tau, where tau counts occurrence-distinguished support spanning trees.
The preimage lemma proves exactly uniform accepted outputs. One attempt
is Q_h=(1-p_h)I+p_h Pi. For any stationary local kernel L, the hybrid
(L+Q_h)/2 mixes within ceil((2/p_h) log(1/epsilon)) attempts. At h=1,
p_h=1/[3(N-1)]; at h=2, p_h=(5N-7)/[15(N-1)^3]. For every fixed h,
the bound is O_h(N^h log(1/epsilon)). This regenerates a whole tree;
it does not prove mixing for the original pair-slide proposal.

Exact genus-one sampling already exists in the repository. The contribution
here is an explicit tree-proposal correction and its macro-kernel bound,
plus limited results and an obstruction for the requested pair kernel.
No extension of the all-length identity-sampling frontier is claimed.

## Reproduction and finite results

Baseline commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`.
Python 3.12.3, standard library only. All runs are deterministic and
exhaustive, so no stochastic seeds or convergence estimates apply.

```sh
python3 -B experiments/20261014-133815-cycle-excess-one/check.py
python3 -B experiments/20261014-133815-cycle-excess-one/tree_jump_check.py
```

The first output is `results.json`; the second is `tree_jump_results.json`.
Both record command, commit, Python version and imported-source hashes.
Both commands passed all assertions. Main checks:

| N | m=N+1 | Number of words | Count with Y=0 | Equal count at each position pair |
| --- | --- | --- | --- | --- |
| 2 | 3 | 1 | 0 | 1 |
| 3 | 4 | 27 | 0 | 9 |
| 4 | 5 | 640 | 60 | 96 |
| 5 | 6 | 15625 | 3000 | 1250 |

For the alternate jump, every output's preimage count equals its separately
enumerated spanning-tree count, and every target word is covered. The six
(N,h) cases (2,1),(3,1),(4,1),(5,1),(3,2),(4,2) exhaust 922830 proposal
tuples. Acceptance probabilities are respectively 1/3,1/6,1/9,1/12,1/15,
13/405. The last target has 23296 words. This checks the implementation;
the bijection in tree_jump_proof.md is the general proof.

The fixed-multigraph obstruction was checked for N=3,...,12, using every
macro channel on both witnesses. S_3 prefix formulas were checked for
all feasible endpoints at m=2,...,7, and the neighboring-state coupling
for d=1,...,5. Identity regression state counts are 27 at S_3,m=4,
120 at S_4,m=4, and 3936 at S_4,m=6. Exact rational row sums, reverse
transition probabilities, endpoints, repeats and support multisets passed.
The identity cases have refresh acceptance below 1/3 in some channels;
that lower bound is intentionally restricted to genus-one full cycles.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
| --- | --- | --- | --- | --- | --- |
| P, original nonlocal/local hybrid | uniform fixed-endpoint words | inherited endpoint-preserving formulas; new identity regressions pass | square refresh permits it; inherited connectivity proof | S_3 coordinates and star-fiber tests | keep partial proof; growing-N mixing inconclusive |
| P_* with balanced equal-pair choice | same uniform law | exact endpoint tests pass | square branch may change generated support | rational detailed balance and branch comparison | keep branch improvement; full gap unresolved |
| P_tree=(L+Q_h)/2 | uniform full-cycle words at m=N-1+2h | target here is a full cycle, not identity | not a required assertion for this endpoint family | all proposal preimages and accepted weights checked | keep separate macro theorem |

## Dependencies and first missing lemma

The minimal codec and all-endpoint connectivity come from the earlier
cycle/nonlocal experiments. Count constants are checked against the primary
Goulden-Jackson-Vakil Proposition 1.1 and Theorem 3.1, equation (21), with
the normalization fully recorded in tree_jump_proof.md. No classification
theorem or finite spectral extrapolation is needed for the new proofs.

To prove the original conjecture, it would suffice to establish
E_(Q_1)<=N^{O(1)} E_P by polynomial-congestion routing. Short paths alone
do not establish it. Freezing exact multigraphs supplies disconnected
restrictions and cannot complete that comparison. No general lower gap
bound is inferred from apparent graph coverage.

## Workspace changes

The workspace was clean on entry. Added these nine research files:

- `experiments/20261014-133815-cycle-excess-one/plan.md`
- `experiments/20261014-133815-cycle-excess-one/proof.md`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_proof.md`
- `experiments/20261014-133815-cycle-excess-one/check.py`
- `experiments/20261014-133815-cycle-excess-one/results.json`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_check.py`
- `experiments/20261014-133815-cycle-excess-one/tree_jump_results.json`
- `experiments/20261014-133815-cycle-excess-one/claim_ledger.md`
- `experiments/20261014-133815-cycle-excess-one/report.md`

Navigation changes: `notes/project-map/catalogue.json`,
`notes/project-map/inventory.json`, generated `PROJECT_MAP.md`,
`notes/project-map/RESULTS.md`, `notes/project-map/COVERAGE.md`, and new
`notes/project-map/integration-2026-10-14-cycle-excess-one.md`.
No existing proof, manuscript, HANDOFF, skill, or user file was changed.
The reusable distinction between fast direct sampling, completed macros,
and unproved local mixing already exists in the project workflow; no
new workflow rule is introduced. No commit or push was made.
