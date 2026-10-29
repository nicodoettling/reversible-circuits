# Theory claim ledger v1

This role supplies proofs and finite falsification evidence; final coordinator acceptance is separate. “Proved” below means a complete authored proof is present, not human or statistically independent certification. All exact T0 proof dependencies remain subject to the campaign's final audit reconciliation.

| Claim | Status | Assumptions | Evidence/artifact | Independent-check scope | Action |
|---|---|---|---|---|---|
| D1 even-time maximum and return-ratio monotonicity | proved, audit provisional | finite symmetric transposition walk, even r,L, L>=2r | proof-T0.md D1 | exact N=2..7, times<=24; author-distinct T0 review requested | retain as self-contained lemma |
| D2 noisy-window null probability <=p_r(id)^2/p_2r(id) | proved, audit provisional | global literal bridge; word-independent exact Q_k; even r and L>=2r | proof-T0.md D2 | all local noise masks and all k for eight exact cases in results-T0-v1.json | retain; never replace reference by connected law |
| D3 exact c6 polynomial and c12 lower count | proved, audit provisional | N>=2 for c6; N>=12 for lower count | proof-T0.md D3 | c6 matched exact full-group DP N=2..7; c3 type counts also checked | retain combinatorial proofs |
| D4 beta6<1/40 for N>=1000 | proved, audit provisional | stated finite onset only | proof-T0.md D4 | exact rational inequalities in results-T0-v1.json | retain conservative onset |
| D5 >=M-1-2B-k surviving disjoint six-windows | proved, audit provisional | six-relator concatenation, conjugation/rotation, <=B adjacent moves, k replacements | proof-T0.md D5 | 6300 deterministic finite transforms; proof is pointwise | retain; arbitrary scrambling excluded |
| D6 one-query advantage>=7/10 when H>=M/2 | proved, audit provisional | D1–D5, N>=1000,L=6M>=12 | statement-T0.md; proof-T0.md D6 | no independence between windows assumed; repeated requests use actual conditional product law | apply to C1 within budget |
| D7 lambda schedule N=lambda²,L=6N,k=lambda,B=floor(N/8) | proved, audit provisional | integer lambda>=32 | proof-T0.md D7 | exact schedule substitutions lambda32,33,64,1000 | runtime polynomial in lambda, not log N |
| Unrestricted L>=r replacement of L>=2r in D2 | refuted | S3,L=r=6,k=0 | probability1 versus claimed1/3; results-T0-v1.json rejected_scope | direct full-word identity event | preserve regression |
| Marginal residual probabilities imply sequential product bound | refuted | CP-1 finite model | full inherited reference plus proof/checker CP1 | exact 21/2000>1/100 and 21/221<1/10 | forbid this proof step |
| C2 support attack and R<=lambda^(-lambda) at lambda>=1024 | proved, scope-reviewed | exact frozen C2 versions and N>=2m | review-C2-v1.md; input hashes JSON | author-distinct analytic review; same model; no new execution | retain pending coordinator reconciliation |
| Sparse noise hides some arbitrary structured sampler | unresolved | unspecified beyond attacked classes | no general impossibility claim | candidate failures cannot decide it | explicit open remainder |
