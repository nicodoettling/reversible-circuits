# Claim ledger

| claim | status | assumptions | evidence/artifact | independent check | action |
|---|---|---|---|---|---|
| Minimal full-cycle factorization supports are trees; square refresh is inactive | proved | all transpositions, length N-1, full-cycle endpoint | proof.md Section 1 | exhaustive states N<=7; proof by connected support and edge count, self-reviewed | retain |
| (3/4) E_Q <= E_K <= E_Q | proved | exact lazy kernels and linear slots in proof.md | proof.md Section 2; results.json | exact off-diagonal comparisons N=3,...,7 by author | retain as strict local-gap reduction |
| Root/time-edge relabeling and Prüfer encoding give a uniform product code | proved | distinguished root 0, fixed endpoint c, minimal length | proof.md Section 3; check.py | both inverse identities for all codes through N=7; independent word enumeration through N=6 in same script | keep explicit benchmark; do not claim novelty |
| Lazy code-coordinate walk has gap 1/[2(N-2)] | proved | code-coordinate kernel C, N>=3 | proof.md Section 4 | standard product-chain proof; endpoint mapping tested | keep as a different walk |
| A code-coordinate refresh is one adjacent Hurwitz move | refuted | universal one-step identification | results.json N=4 witness; report.md | all three factors change in displayed pair | reject immediate transfer |
| Ordinary support-tree forgetting is a bijection | refuted | fixed-cycle endpoint, minimal length | proof.md Section 3; exact N=4 collision | products and unequal codec trees checked | preserve negative witness |
| Polynomial gap for the requested K | unresolved | requires polynomial-congestion comparison or maximal-chain gap | proof.md Section 5 | no inverse-polynomial estimate obtained; finite connectivity not sufficient | keep explicit open lemma |
| Minimal Hurwitz graph is connected | proved literature input | source conventions translated as in proof.md | Adin--Roichman arXiv:1201.4669v3 Remark 2.6, citing Bessis Prop. 1.6.1 | source statement and move definitions checked; original Bessis proof not independently re-proved | use qualitatively only |

No independent referee or subagent participated. This ledger does not
upgrade the local mixing claim or provide external certification.
