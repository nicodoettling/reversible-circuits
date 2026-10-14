# Labeled-tree slide comparison

Date: 2026-10-14. Starting commit:
`9a7ca2119172f87b15e9f85e28cee6dc91af188f`.

User request: remove circuit edge order, retain vertex labels, and analyze
the walk choosing an adjacent edge pair and one of its two slides.
This is an auxiliary graph model; no permutation endpoint is imposed.

Targets declared before computation:

- P: lazy adjacent-pair slide walk, stationary mass proportional to
  W(T)=sum_v binom(deg_T(v),2).
- M: Metropolis correction of P, targeting uniform labeled trees.
- U: choose any unordered pair of tree edges, hold when disjoint, otherwise
  choose either slide. With half laziness this also targets uniform trees.

Claim to test: comparison with the spanning-tree down-up walk gives, for
all three kernels and N>=3, gap >=2/[(N-1)^2(N-2)^2].
The down-up gap >=1/(N-1) is the sole substantive external dependency:
Anari--Liu--Oveis Gharan--Vinzant, arXiv:1811.01816v3, Theorems 1.1 and 5.2.
Their chain definition, rank, weights, and normalization must be checked.

Exact checks: enumerate all labeled trees through N=6; verify slide
reversibility, all three target laws, holding probabilities, connectivity,
and all down-up transitions and bridge-slide paths. Accumulate exact
length-weighted directed-edge flow and check the proof's congestion bound.
Check the unique-forest reconstruction and the unweighted load-count
formula for each directed slide. Check singleton N=1,2 and the N=4
noninjectivity of forgetting circuit order. Deterministic run, seed 0
reserved but no random draws. Standard library Python only.

Expected failure modes: confusing graph adjacency with adjacent word slots;
assuming uniform stationarity for variable-degree proposals; duplicate
slide proposals; lost factors of two in Dirichlet forms; a path changing
the fixed forest; exponential congestion hidden by a normal-form route;
overinterpreting finite checks as an asymptotic proof.

Command: `python3 -B experiments/20261014-tree-slides/check.py`.
Raw output: `results.json`. Proof, report and claim ledger are separate
artifacts. Existing identity samplers are not changed; identity-word
regressions are inapplicable to a walk explicitly dropping functionality.
Record this result provisionally in the project map, without upgrading the
unresolved circuit Hurwitz gap. No installation, commit or push.
