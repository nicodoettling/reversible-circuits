# Nonlocal graph lift: connectivity and mixing conclusions

Verdict: **keep** the self-contained connectivity proof, reversible pair
lift and polynomial comparison. **Keep** the derived fast decoded-tree
macro sampler for a minimal full-cycle endpoint. General polynomial mixing
of the direct pair lift remains **unresolved**. Same-author proofs and
exact checks; independent review is pending.

The user authorized an entire Hurwitz sequence for each graph-selected
move, including changes to other support edges. This permits a precise
nonlocal implementation, but does not select one unique transition kernel.
We distinguish two kernels explicitly.

| candidate | claimed target | endpoint ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| K_G: uniformly selected position pairs, transported Hurwitz and square moves | uniform Omega_g(N,m) | proved and checked at every primitive stage | yes with square refresh; general connectivity proved | exact integer detailed balance, fiber connectivity and every macro path | keep; general gap open |
| K_T: decoded uniform tree-slide walk, completed Hurwitz paths | uniform minimal words of one full N-cycle | proved and checked at every primitive stage | not needed; one minimal Hurwitz orbit | all decoded slide transitions through N=6 | keep; polynomial macro mixing proved from earlier tree theorem |
| incident-only moves with no disjoint commutation | proposed global endpoint uniformity | endpoint preservation alone insufficient | not globally connected for all endpoints | two disjoint transpositions are frozen | reject the universal connectivity claim |
| replace a nonadjacent square without changing intermediate gates | proposed Omega_g law | fails | not applicable | explicit S3 counterexample | reject |

## Mathematical results

The exact formulas, kernels, boundary cases and proofs are in [proof.md](proof.md).

1. **Proved:** adjacent Hurwitz plus square refresh connects every feasible
   fixed-endpoint transposition fiber. A vertex sweep exposes a square in
   every nonreduced word, and gives a unique reduced word otherwise. Each
   input reaches a common padded reduced word within (N+3)m^2 moves.
   Diameter is at most 2(N+3)m^2. No Hurwitz classification theorem is used.
2. **Proved:** the direct nonlocal lift K_G is uniform-reversible. For
   M=binom(N,2), its gap satisfies
   `(2/m) gap(K_A) <= gap(K_G) <= 8M(M+1)m^3 gap(K_A)`.
   The upper comparison has an explicit recoverable-source congestion
   proof, not a hub argument. Thus these two gap questions are equivalent
   up to polynomial factors. General polynomial mixing is not established.
3. **Proved:** a conservative exponential mixing bound is given in Section 5,
   using the exact state count S, diameter and minimum edge probability.
4. **Proved from earlier scoped inputs:** for a full cycle with m=N-1,
   the bijective time-labeled tree encoding transfers the earlier uniform
   tree-slide kernel to K_T, with gap at least
   `2/[(N-1)^2(N-2)^2]`. Mixing takes
   `O(N^4 [N log N + log(1/epsilon)])` completed macro updates. Each update
   has a constructive implementation with at most 2N(N-1) Hurwitz moves.
   Circuit outputs are observed at completed macros. The actual permutation
   labels can change globally; this is not one slide in those original labels.

The last result uses the existing same-author tree-slide comparison and its
checked external spanning-tree down-up theorem (Anari--Liu--Oveis Gharan--
Vinzant, arXiv:1811.01816v3, Theorems 1.1 and 5.2). It also uses the earlier
proved codec, restated here with its inverse argument. No local adjacent
mixing theorem is inferred. Intermediate execution states may pass through
a canonical word and are not the stationary macro output law.

For uniform circuits, the resulting support distribution remains weighted
by the number of realizing circuits. No uniform unlabeled-support claim
or ordinary-support Markov projection is made.

## Exact checks

`check.py` verified normal forms for 67,087 words: N=2,3,4 with m=0,...,6,
and N=5,m=4. Every normal form matched the independently computed canonical
endpoint word and satisfied the length bound.

Exact kernels checked all 81 S3 length-four words (three endpoint fibers),
all 1,296 S4 length-four words (12 endpoint fibers), and all 3,936 S4
length-six identity words. Every fiber was connected. All 536,958 labeled
macro channels agreed with their primitive paths and preserved their
endpoint at every stage. Integer symmetry and row sums certify uniform
stationarity of every observable, including prefix cycle types, gate
frequencies, multiplicities, adjacent repeats and support components.

`tree_check.py` checked 13,938 directed tree slides through N=6 and their
complete decoded Hurwitz paths. At N=6 there were 1,296 trees and 12,960
directed slides; maximum observed primitive path length was 20, below
the general bound 60. Both codec inverse identities and reverse-slide
symmetry passed. These finite checks corroborate, rather than prove, the
asymptotic statements.

Commands:

```text
python3 -B experiments/20261014-111117-nonlocal-graph-lift/check.py
python3 -B experiments/20261014-111117-nonlocal-graph-lift/tree_check.py
```

Python 3.12.3, standard library only, deterministic exhaustive runs (no
random seeds). Starting commit and imported source hashes are in
[results.json](results.json) and [tree_results.json](tree_results.json).
No existing sampler implementation was changed.

## Remaining obligation

For K_G the next substantive claim is an inverse-polynomial Poincare
bound, equivalently for K_A up to the proved comparison. Graph-space
mixing and short Hurwitz paths alone do not discharge this obligation.
For K_T the theorem already bounds completed macro mixing in the minimal
full-cycle regime; extending the codec/graph law to nonminimal words or
arbitrary endpoints is a separate problem.

## Workspace changes

This turn added the eight files in this research directory: `plan.md`,
`proof.md`, `check.py`, `results.json`, `tree_check.py`, `tree_results.json`,
`report.md`, and `claim_ledger.md`. It also added
`notes/project-map/integration-2026-10-14-nonlocal-graph-lift.md`.

This turn updated five already-dirty map files: `PROJECT_MAP.md`,
`notes/project-map/COVERAGE.md`, `notes/project-map/RESULTS.md`,
`notes/project-map/catalogue.json`, and `notes/project-map/inventory.json`.

The following pre-existing untracked files were preserved unchanged:

- `experiments/20261013-single-cycle-walk/plan.md`
- `experiments/20261013-single-cycle-walk/proof.md`
- `experiments/20261013-single-cycle-walk/check.py`
- `experiments/20261013-single-cycle-walk/results.json`
- `experiments/20261013-single-cycle-walk/report.md`
- `experiments/20261013-single-cycle-walk/claim_ledger.md`
- `experiments/20261014-tree-slides/plan.md`
- `experiments/20261014-tree-slides/proof.md`
- `experiments/20261014-tree-slides/check.py`
- `experiments/20261014-tree-slides/results.json`
- `experiments/20261014-tree-slides/report.md`
- `experiments/20261014-tree-slides/claim_ledger.md`
- `notes/project-map/integration-2026-10-13-single-cycle.md`
- `notes/project-map/integration-2026-10-14-tree-slides.md`

No HANDOFF, GOAL_SPEC, manuscript, AGENTS or skill changes; no commits,
pushes, installations or sub-agents. Map entries are provisional navigation,
not independent mathematical certification.
