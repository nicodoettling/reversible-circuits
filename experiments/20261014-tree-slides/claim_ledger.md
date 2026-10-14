# Claim ledger

All new proofs and computational checks below are same-author work.
Independent review is pending; map registration is provisional.

| claim | status | assumptions | evidence/artifact | independent check | action |
|---|---|---|---|---|---|
| P has target proportional to W(T) | proved | half-lazy, uniform incident pair and direction; all vertex-labeled trees | proof.md Section 1; results.json stationary sums | analytic detailed balance; exact all-state sums through N=6; no independent referee | keep |
| P is uniform for general N | refuted | same kernel | proof.md Section 6; N=4 stars/paths | exact counts 4 stars with W=3 and 12 paths with W=2 | retain negative finding |
| U and M have uniform target | proved | kernels exactly as stated | proof.md Section 1 | exact stationary sums and holding checks through N=6 | keep |
| Reference B gap >=1/(N-1) | proved literature input | graphic matroid of K_N, rank N-1, unit weights, drop-one/complete normalization | proof.md Section 3; arXiv:1811.01816v3 Theorems 1.1 and 5.2 | theorem statements and normalization checked in primary source; not independently reproved | import at stated scope |
| Each exchange has a <=N-2 slide simulation with uniquely recoverable fixed forest | proved | complete labeled-tree state space | proof.md Section 4; check.py route | all 36894 nontrivial exchanges through N=6 checked; independent edge-subset state enumeration | keep |
| Comparison congestion <=binom(N-1,2)(N-2) | proved | same fixed-component-order routes and B probabilities | proof.md (6)--(7) | exact rational load accumulation, maxima 1,4,12,24 at N=3,4,5,6 | keep |
| All three gaps >=2/[(N-1)^2(N-2)^2] and polynomial TV mixing | proved | preceding checked theorem and analytic comparison; N>=3 | proof.md Sections 2,4,5 | N=3 exact spectrum by direct row formula; finite checks audit only ingredients | provisional author result pending independent review |
| Ordinary support forgetting is a bijection or gives the proposed Markov projection | refuted | fixed (1234) endpoint, rightmost-first products | proof.md Section 6; results.json circuit_forgetting_witness | explicit same-support words have different projected transition rows | preserve obstruction |
| This proves fast adjacent Hurwitz circuit mixing | unresolved | would require a valid lift and order control | proof.md Section 6 | no such comparison established | do not upgrade HB-CYCLE-MINIMAL or G-HEATBATH |
