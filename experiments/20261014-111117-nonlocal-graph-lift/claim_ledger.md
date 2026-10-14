# Claim ledger: nonlocal graph lifts

All proofs and checks are same-author work, pending independent review.

| claim | status | assumptions | evidence/artifact | independent check | action |
|---|---|---|---|---|---|
| Explicit nonlocal pair formulas preserve endpoint and have Hurwitz/square lifts | proved | fixed N,m; middle conjugation retained | proof.md Section 2 | none; exact macro/path check in check.py | keep |
| K_G is uniform-reversible | proved | exact state-independent pair/sign/square proposal | proof.md Section 2; results.json | none; exact integer detailed balance | keep |
| All feasible endpoint fibers are connected under adjacent H plus refresh | proved | all transpositions allowed; disjoint commutations included | proof.md Section 3 | none; 67,087 exhaustive normal-form checks | keep |
| Diameter <=2(N+3)m^2 | proved | m>=2; same move set | proof.md Section 3 | none; exhaustive finite bounds | keep for connectivity only |
| Gap comparison (2/m) gap(K_A)<=gap(K_G)<=8M(M+1)m^3 gap(K_A) | proved | precisely defined lazy kernels on identical uniform fibers | proof.md Section 4, explicit path reconstruction | none; algebraic audit by author | keep |
| General polynomial mixing of K_G | unresolved | would need inverse-polynomial Poincare inequality | proof.md Sections 4--5 | none | do not promote |
| Explicit exponential mixing upper bound | proved | nontrivial feasible fiber of size S | proof.md Section 5 | none | retain without fast-mixing claim |
| Every graph-incident-only kernel connects every endpoint fiber | refuted | no commuting disjoint branch | proof.md Section 6; results.json | explicit two-word counterexample | retain negative finding |
| Literal nonadjacent square replacement preserves g | refuted | intervening gates unchanged | proof.md Section 6; results.json | explicit S3 calculation | retain negative finding |
| K_T has gap >=2/[(N-1)^2(N-2)^2] | proved from listed inputs | full N-cycle, m=N-1; time-label tree bijection; earlier uniform tree-slide gap | proof.md Section 8; tree_results.json | no independent reviewer; all slides through N=6 checked | keep as separate macro kernel |
| K_T steps can execute in <=2N(N-1) adjacent H moves | proved | output only after completed macro; other edges and labels may change | proof.md Sections 3,8; tree_check.py | none; 13,938 explicit complete paths | keep |
| Fast K_T mixing proves adjacent-H mixing or uniform intermediate states | refuted as an inference | no polynomial flow congestion established | proof.md Section 8 | canonical-hub intermediate obstruction | retain distinction |

Decision: proof-progress on connectivity and a permitted minimal-cycle
macro sampler; general pair-chain gap remains open. No global sampler
frontier or historical accepted result is replaced by this ledger.
