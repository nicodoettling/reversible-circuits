# One-cycle factorization investigation

Date: 2026-10-13. Local-mixing verdict: **inconclusive**.
Structural reduction and explicit coded benchmark: **keep**.
No polynomial bound for the requested adjacent Hurwitz kernel is claimed.

## Scope and strongest conclusions

Target: global uniform ordered transposition factorizations of the fixed
full cycle (0 1 ... N-1), initially at minimal length N-1. This is not the
identity-word target. Products act rightmost first. K=I/2+H/4+R/4 uses
linear adjacent slots, signed Hurwitz H, and uniform square refresh R.

The support of every minimal factorization is a tree with distinct edges.
Consequently R is the identity kernel and K=(3/4)I+(1/4)H. This removes
the multiple-support-component obstruction of the identity-word problem,
but also removes the square-refresh mechanism at minimal length.

Section 2 of `proof.md` establishes, for lazy exact two-factor heat bath Q,

    (3/4) E_Q <= E_K <= E_Q.

Thus their spectral gaps are equivalent within a factor 4/3. In prefix
coordinates Q is single-rank resampling on uniform maximal chains of the
noncrossing partition lattice. This identifies an exact narrower gap
problem, rather than inferring mixing from graph diameter or connectivity.

An explicit root/time-edge relabeling gives a bijection to ordinary labeled
trees, and then to N-2 independent Prüfer coordinates. The separate lazy
code-coordinate-refresh chain C has gap 1/[2(N-2)] and

    t_mix,C(epsilon) <= ceil(2(N-2) log((N-2)/epsilon)).

It also supplies an elementary exact direct sampler, a regime already
covered by S-MINIMAL. These facts do not close the local mixing problem.

## Negative transfer findings

Ordinary support-tree forgetting is not injective: (in one-based labels)
((13),(12),(34)) and ((13),(34),(12)) are distinct factorizations of
(1234) with the same support tree. The true codec relabels vertices using
the factor positions of incoming rooted edges.

Even under that genuine bijection, a code refresh is not in general a
single local move. At N=4, the codes (0,0) and (3,0) decode to, in
zero-based labels,

    ((0,3),(0,2),(0,1)),
    ((1,2),(0,3),(0,2)),

which differ at every factor. Both evaluate to (0 1 2 3). This refutes
the proposed immediate transfer of the product-chain gap to K, not the
possibility of a polynomial-congestion multi-step comparison.

The first missing lemma is stated precisely in `proof.md`, Section 5:
route the stationary flow of code refresh through adjacent Hurwitz paths
with polynomial length-weighted edge congestion. Equivalently, obtain a
polynomial gap for the single-rank maximal-chain heat bath.

## Validation and reproducibility

Command: `python3 -B experiments/20261013-single-cycle-walk/check.py`.
Start commit: `9a7ca2119172f87b15e9f85e28cee6dc91af188f`.
Python 3.12.3, standard library only. Seed 20261013 recorded; no randomness
used. `results.json` pins both the new script and the reused baseline script.

| N | minimal length | exact states | independent word enumeration |
|---:|---:|---:|---|
| 2 | 1 | 1 | yes |
| 3 | 2 | 3 | yes |
| 4 | 3 | 16 | yes |
| 5 | 4 | 125 | yes |
| 6 | 5 | 1296 | yes |
| 7 | 6 | 16807 | no; every Prüfer code tested |

Both codec inverse identities, endpoint evaluation, absence of repeated
edges, local detailed balance, connectivity and the exact off-diagonal
K/Q ratios passed. Prefix cycle types, per-position edge frequencies,
window product types, and the fixed weighted-support signature are recorded.
At N<=6 independent transposition-word enumeration agrees with every coded
state. At N=7 exhaustive code generation verifies the codec and local graph;
completeness at arbitrary N comes from the written inverse proof.

All 27522 nontrivial directed code-coordinate changes through N=6 were
checked. Of these, 23678 are not single K transitions; at N=6 a code change
can alter all five factors. This is a finite obstruction to a one-step
identification, not an asymptotic slow-mixing result. No numerical spectrum
or Monte Carlo convergence claim is used.

The existing exact identity-kernel harness also passed S3,m4 (27 states),
S4,m4 (120), and S4,m6 (3936). These are regression checks only: identity
preservation is replaced by preservation of the cycle endpoint in this task.
N=1 and N=2 singleton exceptions were checked explicitly.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| adjacent Hurwitz + square refresh K | uniform minimal factorizations of fixed full cycle | not an identity target; endpoint checks pass | target is one orbit by cited connectivity result; finite checks agree | exact kernel and Q comparison through N=7 | inconclusive for polynomial mixing |
| lazy Prüfer-coordinate refresh C | same endpoint target | not an identity target; endpoint checks pass | same target | bijection checked exhaustively, code transitions through N=6 | keep as proved nonlocal benchmark |

## Literature and evidence limits

Adin--Roichman arXiv:1201.4669v3 Definitions 2.1--2.3, Observation 2.5
and Remark 2.6 match the minimal model; their signed shifts are our inverse
Hurwitz pair. This source supplies structural context and a cited
connectivity input, not a checked mixing theorem. Lewis's FPSAC 2021
Theorem 2.2 quotes the stronger Kluitmann transitivity theorem; the original
source was not re-audited, so no additional all-length result is promoted.
No assertion about the absence of a theorem in the entire literature is made.

All proof writing and checks are from the same author session. The project
map records the reduction provisionally and leaves the local gap unresolved.
No changes to HANDOFF, manuscript, existing sampler code or project skill.
