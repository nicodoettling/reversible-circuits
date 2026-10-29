# Retained regression and failed-route registry v1

Each entry is preserved even where a stronger proof supersedes it. “Finite” is not an asymptotic security claim. Exact command receipts are in coordinator/job-registry.json.

ID | Claim tested / failed temptation | Expected outcome | Evidence
---|---|---|---
R-global | Global bridge counts distinct from connected counts | S3L4=27, S4L4=120, S4L6=3936; connected counterparts not substituted | J001,J002,J003,J005 and frozen projection input
R-boundaries | Odd L, empty word, N2, L2, k0,k1,kL | Odd infeasible; empty/N2 singleton; doubled L2 reference; full replacement iid | all checker outputs and T0/C2 boundary sections
R-subsequence | Raw selected tuple formula under global U only | Exact fixed-position completion law; connected conditioning cannot reuse it | frozen inputs/projection report and J001
R-conjugated | Replace raw selected product by conjugated old-gate product without invariance | Reject substitution for arbitrary word laws; old B tuple not iid | frozen projection proof, M0, J001
R-pair | Pair equality under exact-k replacement | Exact attenuation alpha=(L-k)(L-k-1)/(L(L-1)) | J001 exhaustive rational checks; only a smoke control
R-endpoint | Endpoint agreement implies whole-word hiding | Reject; N3L4 repeated-edge control has endpoint p2 at k1 but fixed-pair bias1/3; C1 N4L6k1 endpoint types agree while word TV323/328 | derivation below; J004; frozen mandatory inputs
R-full-window | Omit L>=2r in T0 local bound | Reject at N3,L=r=6,k0: true probability1 versus proposed1/3 | J003 and full proofs/reviews
R-channel-null | Extend LC1 inversion when k>L-s | Reject positive universal inverse: top s-coordinate component annihilated | J001 finite basis checks; q2,L=s=1,k1 is smallest example
R-LC1-denominator | Per-value rational bit bound survives q^s sums unchanged | Reject wording; s6 fixture has 9-bit individual denominators and 497-bit mean denominator | J005, v1 repair and full reviews
R-LC1-access | Any rational local f automatically yields efficient public test | Reject missing premise: f=1/2^(2^lambda) has exponential explicit denominator; hidden-key lookup is not public | v2 repair; exact v3 fresh recheck
R-C1-runtime | O((L+s)log N) fair bits for arbitrary unrelated N,L | Reject off schedule; add s log L | immutable C1 runtime erratum and reviews
R-checker-cost | factorial(N)/factorial(N-2m) at N=lambda^6 | Reject before executing; use a length2m falling product | check_candidates_v1.py, checker-v1-rejection.md, v2 passing result
R-dense-noise | Candidate rejection extends to near-total replacement | Reject: uniform one-coordinate marginals imply exact iid at k=L-1; all sources iid at k=L | J004 complete laws and conditional proof in report
R-support | Arbitrary Hurwitz steps erase planted support | Reject; generated subgroup/support is invariant | C2 proof, full r1 review, J002
R-key-reuse | One-sample average-setup match implies reused-key security | Reject; sample K~U once and repeat K: k0 marginal exactlyU, two full replies equal with probability1 versus1/|Omega| | r3 blind-report-v1.md B1.4
R-CP1 | Marginal lightness or fresh local independence justifies sequential product | Reject: 21/2000>1/100 despite second incidence21/221<1/10 | complete fixture below, J001, J003, probability audits
R-mixing-route | Need dense pointwise mixing to get T0 | Superseded, not refuted: even-return moment ratio removes import | proof-T0.md failed-route discussion
R-BS3 | Independent stronger-onset C2 derivation is automatically accepted | No; retain provisional alternative, not load-bearing | blind-supplement-v3-C2.md and coordinator ledger

## Exact repeated-edge endpoint/control counterexample

Choose one uniform transposition T and repeat it at even L. For k=1 the noisy product is either ST or TS up to the displayed repeated T factors, with independent uniform S,T; both give p2. The global bridge also has endpoint p2 by its verified replacement projection. Yet for N3,L4, a fixed original pair is equal with probability1 under the repeated-edge source and1/3 under global U. At k1 the exact pair attenuation is1/2, so the observable equality advantage is(1/2)(1-1/3)=1/3. This is a historical control, not the new contribution. Doubled adjacent iid pairs and mirrored inverse words remain explicitly excluded as purported novel successes.

## CP-1 complete finite fixture and failure mechanism

Let H be independent uniform bits at x,e0,e1,f0,f1. Put gamma=1/10. Before conditioning, trace A_b={e_b,f_b} has mass21/2200 and trace C_b={e_b,x} has mass1/11 for each b=0,1; empty trace D has mass879/1100. A_b,D always output vk=1; C_b does so iff H(x)=b. Therefore Pr[vk=1]=10/11. Conditioning gives each A_b mass21/2000, each C_b mass1/20, D mass879/1000; C_b retains latent answer H(x)=b.

A verifier reads x, sets b=H(x), then reads e_b,f_b. Initial query incidences are p(x)=1/10, p(e_b)=121/2000=.0605 and p(f_b)=21/2000=.0105, all nonheavy under strict p>gamma. The selected matching of verifier positions(2,3) to the two A_b addresses has probability sum_b(21/2000)/2=21/2000>.01=gamma^2. Transferring the cached x value after the first selected hit changes the relevant mass from .0605 to .1105; the second residual incidence is(.0105)/(.1105)=21/221<gamma. Thus local fresh-value independence and successive residual lightness do not give the false product bound. Support restriction and Bayes renormalization remove compensating sibling cylinders. Latent hit status is not freely observable to the algorithm.

The current proofs avoid this mechanism: deterministic witness counting, a positive source-independent channel inequality, or a single explicitly paid change of measure supplies the needed invariant. T0 repetition uses truly independent fresh reference replies conditional on public setup. No cache-transfer or selected-branch product assertion is imported.
