# support-marginal-audit

- Created UTC: 2026-10-15T12:28:24.786665+00:00
- Objective: Test support lumpability of the actual all-pair circuit walk and isolate a graph-only mixing criterion
- Target distribution: Support multigraph pushforward of uniform ordered fixed-product transposition words
- Parameters: K_G=I/2+H_G/4+R_G/4 with uniform unordered position pairs, signed transported Hurwitz moves and uniform transported square refresh. Products act rightmost first. Graphs retain vertex labels and edge multiplicities, forget gate order.
- Tested claim: support forgetting is strongly lumpable for this precise all-pair walk. Test separately from stationary weighted-graph correctness and from polynomial marginal mixing.
- Exact cases: full-cycle N3,m4 and N4,m3,m5; identity N3,m4 and N4,m4,m6. Compare full weighted graph rows from distinct words in the same support fiber. Preserve both positive and negative outcomes.
- Commands: `python3 -B experiments/20261015-122824-support-marginal-audit/check.py`.
- Raw data: results.jsonl, deterministic exact rational checks; no random seeds or stochastic mixing claims.
- Expected failure modes: gate order changes conjugations of middle edges; an averaged stationary-flow graph kernel is mistaken for the observed process; a fast cycle-partition cut-and-join theorem is applied to fixed-endpoint support graphs; fast projected Poincare is mistaken for graph marginal convergence.
- Proof deliverables: exact target weights, a concrete same-support transition witness if one exists, correct observable-only criterion, and a general counterexample to the stationary-flow-gap shortcut. Identify the first missing growing-N lemma without replacing the actual walk.
- Literature scope: Blumberg, arXiv:1109.3915v1, Definition 2 and Definition 5, only to identify the object and kernel in standard split-merge results. No imported mixing theorem is applied to circuit supports.
- Interpretation: finite obstruction can refute lumpability; failure of that method cannot refute fast marginal mixing.
