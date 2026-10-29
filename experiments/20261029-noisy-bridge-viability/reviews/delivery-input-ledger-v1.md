# Coordinator claim ledger v1

Statuses below refer only to the exact frozen model/versions. “Proved / accepted internally” means full arguments passed this campaign's stated same-model audit and finite regressions; it is not external certification. The broader question remains open. No restart or Git checkpoint changed a mathematical status.

claim | status | assumptions | evidence/artifact | independent check | action
---|---|---|---|---|---
M0 | frozen definition | exact uniform k-subset, fresh iid replacement, global U, same public A, rightmost-first | model-v1.md | coordinator/three roles checked conventions | use unchanged
T0 D1 | proved / accepted internally | finite symmetric transposition walk, even times | r1-theory/proof-T0.md D1 | blind BS2, r2 and r3 full reviews; N2..7 exact return DP | close exact claim
T0 D2 | proved / accepted internally | even r>=2, even L>=2r, word-independent Q_k | proof-T0.md D2 | density-kernel proof and alternative blind derivation; exact masks/all k | close; never remove length hypothesis
T0 D3-D4 | proved / accepted internally | c6 all N>=2; c12 lower count N>=12; numerical bound N>=1000 | proof-T0.md D3-D4 | r2/r3 endpoint-class and rational arithmetic checks; independent S4L6 rerun | close exact onset
T0 D5-D7 | proved / accepted internally | six-relator source, rotation/conjugation then <=b adjacent moves; H>0; .7 bound needs H>=M/2 | statement-T0.md and proof-T0.md | two full reviews, blind reconstruction, 6300 survival cases | accept scoped O(L) one-query attack
C1 identity/law | proved / accepted internally | N>=4,L=6B, exact ordered quadruples and signed moves | candidate-1-v1.md + runtime erratum; candidates_v1.py | blind convention check, exhaustive labels/moves, J002/J004 | freeze no security claim
C1 attack | proved / accepted internally | a=ceil(B/2), B-2s-k>=a; published lambda schedule | candidate-1-rejection-v1.md | coordinator full rederivation; T0 independently covers class; exact matched finite laws | reject C1 schedule
C2 identity/support/law | proved / accepted internally | m>=2,N>=m+1; exact injection, path/star, arbitrary finite s | candidate-2-v1.md; implementation-scope-v1.md | blind construction check, r1 full review, J002 exact states | freeze no security claim
C2 finite attack and schedule | proved / accepted internally | N>=2m,h=m+1+2k<=N; R truncated at1; lambda>=1024 explicit bound | candidate-2-rejection-v1.md | full r1 review; coordinator normalization/constants check; D(6,2)=270 independent rerun | reject C2 schedule
C2 BS3 alternative onset81 | provisional, not promoted | a=m+1+4k and exact BS3 schedule | r3-adversarial/blind-supplement-v3-C2.md | independently authored from algorithm but no fresh exact-proof audit | retain; not load-bearing
LC1-v1 arithmetic clause | refuted/superseded wording | variable s, unrelated rational denominators | reviews/LC1-v1-arithmetic-repair.md | r3 objection and exact prime-denominator fixtures | preserve; probability identity unchanged
LC1-v2 efficient-corollary clause | incomplete/superseded wording | no free evaluator/advice and no implicit polynomial value size | reviews/LC1-v2-efficiency-repair.md | independently raised by r2/r3 | preserve; use exact v3
LC1-v3 | proved / accepted internally | k<=L-s; finite rational f; efficient part also public polynomial f/I and polynomial b, fixed s | coordinator/local-channel-statement-v3.md and proof-v3.md | blind algebra reconstruction; fresh r2 v3 review, r3 v3 review, J001/J005 | close scoped transfer only
Finite complete-word C1 laws | exact finite facts | N4,L6,s0/1/2,k0..6 | r3-adversarial/exact-c1-results-v1.json | literal enumeration, independent Q1 transform, exact normalizations | retain without asymptotic inference
k=L and uniform-marginal k=L-1 equality | proved | fresh independent replacements; uniform coordinate marginals for L-1 | r3-adversarial/report-v1.md and report.md | conditional-on-retained-position proof, J004 | preserve limiting case
C1 general random-bit bound v1 | refuted off schedule; repaired | log L need not be O(log N) | candidate-1-runtime-erratum-v1.md | coordinator and r3 fresh review | link erratum; no law change
Checker factorial(N) route | rejected before execution | N=lambda^6 too large to materialize factorial(N) | r2-construction/checker-v1-rejection.md | source review; v2 short falling product passed | retain failed source; no failed mathematical job
General sparse-noise hiding / general hardness | unresolved | no construction/reduction established beyond this scoped study | report.md final paragraph | explicit exclusions across all reports | no completion claim for this question
