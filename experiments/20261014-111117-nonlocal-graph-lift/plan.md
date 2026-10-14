# nonlocal-graph-lift

- Created UTC: 2026-10-14T11:11:17.921713+00:00
- Objective: Prove connectivity for nonlocal Hurwitz and transported square refresh; audit reversible lifts and polynomial comparison with the adjacent chain.
- Target distribution: Uniform length-m transposition factorizations of a fixed endpoint g in S_N.
- Parameters: exhaustive normalization for N=2,3,4 and m=0,...,6, plus N=5,m=4; exact kernels for S3,m=4 and S4,m=4 at all endpoints, and S4,m=6 at identity.
- Commands: `python3 -B experiments/20261014-111117-nonlocal-graph-lift/check.py`
- Raw data: results.json, including initial Git commit and Python version.
- Interpretation: test connectivity, product preservation, detailed balance, and exact macro/primitive-path agreement. No spectral extrapolation.
- Next changes: report proof and remaining quantitative obligation.

Products act rightmost first. The target has no connected-support restriction.
The precise half-lazy kernel is in proof.md. Positions are chosen uniformly
among all unordered pairs, including disjoint transpositions. Intermediate
gates may change, as explicitly authorized by the user. Incident-only proposals
define a different kernel, whose obstruction will be recorded.

Expected failure modes: incorrect composition convention; noninverse macro
moves; missing middle-block conjugation; failed square extraction; input-
dependent purported canonical form; unjustified polynomial congestion.
All computations are deterministic and exhaustive; no seeds or dependencies
beyond the Python standard library. Finite checks can refute universal claims
but cannot replace the general proof.

Extension after the constructive proof: implement a separate minimal-cycle
macro chain by decoding the existing uniform-target tree-slide walk. This
tests whether the user-authorized long Hurwitz implementation can realize
every proposed decoded tree move. Command:
`python3 -B experiments/20261014-111117-nonlocal-graph-lift/tree_check.py`.
Check all trees/slides through N=6, every intermediate endpoint and the
2N(N-1) primitive path bound. Record tree_results.json. Do not conflate this
kernel with the pair-selected lift or claim primitive-time uniformity.
