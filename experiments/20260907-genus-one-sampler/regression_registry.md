# Regression registry

| ID | fixture / previous failure | expected outcome | affected claims |
|---|---|---|---|
| BOUND | N=1/2; m=0, odd m,m=2; connected minimal and genus-one lengths | classify feasibility exactly; no division by zero | all |
| COUNT | (N,m)=(2,4),(3,6),(4,8) connected counts 1,240,131040; shared total counts 27,120,3936 at (3,4),(4,4),(4,6) | independently enumerate, not inherit archive as oracle | COUNT,T0,ASSEMBLY |
| SQUARE | a=(12),b=(23), w=(ab)^3 | identity, connected, length 6, no adjacent square; literal insertion has zero fiber | any insertion/coverage route |
| SQUARE-TREE | (ab)^3 followed by e^2 for remaining tree edges | deleting any adjacent square loses connectivity; no literal connected-deletable mark | structural variants |
| CUT | M97 J(w)={b(w),...,h(w)-1} and prefix genus | nonempty; sum side genera and incidence Euler relation exact | CUT |
| BIAS | uniform (w,j) on decorated cuts | forgetting weights w by |J(w)|; 1/|J(w)| correction must be included | cut sampling |
| FIBER | scalar connected endpoint counts vs exposed-prefix support constraints | do not substitute C(v,k) or ordinary endpoint bridge counts without decomposition proof | recursive sampling |
| SUBSETS | arbitrary subset partitions at fixed genus | fixed genus alone does not bound inventory polynomially in N | complexity |
| GLOBAL | connected X_N vs unrestricted Omega(N,2N) | retain excluded component mass and exact interleaving/component factorials | GLOBAL |
| SOURCE | long-cycle endpoint arxiv:2105.03284; cover weights; DPS roots | reject wrong endpoint/accuracy substitution; normalize labeled words explicitly | source imports |
| HANDLE | M97 x=(01)^4(02)^2 and y=(01)^3(02)(01)(12), same forward handle but different transitions | reject strong lump/pointwise birth-death assumption; no mixing inference | only if handle-chain proposal used |
| CP-1 | audit skill cached-prefix branch inflation | run if multiplying sequential marginal bounds or claiming independence survives conditioning; reject .0105<=.01 | probabilistic arguments when relevant |

Sources: M97 complete report, September 5 component/phase-diagram reports,
and mathematical-proof-audit probability-regressions.md. Exact reproductions
and new witnesses will be added with candidate versions. No failed method
implies computational hardness.

## Completed disposition — S1.v2, R2-C1, G1.v1.2

| ID | checked domain / artifact | disposition |
|---|---|---|
| BOUND | all role audits; integration_results.json; R3 candidate/global checks | N2 length4 singleton; N1 target infeasible; connected singleton g0 empty and g1 infeasible; global m0/odd/m2 and zero restricted mass handled |
| COUNT | coordinator_r1_results.json; global_mass_results.json; R3 independent counts | exact connected1,240,131040 and required shared cases pass; 1745 endpoint checks and91 global/connected cells agree |
| SQUARE / SQUARE-TREE | R1 complete word-law checks; R2 regression family through N12; R3 blind check | historical zero fiber reproduced; accepted samplers cover witnesses, including probability1/240 for the base word |
| CUT / BIAS | R2 proof/results; R1 structural_audit.md and structural_parser_results.json | nonempty cut proved; decorated totals1,336,234720 at N2/3/4; full N3 cut probabilities1/336 and accepted word probabilities1/240; expected rejection trials<=2N-1 |
| PARSER (new) | R1 structural_audit.md; coordinator_structural_parser_results.json | all 58 numerical codes at N5 (78 across N2..5);1420 labeled macros at N5;4431 partial coefficients; parallel core and repeated child orders agree |
| FIBER / SUBSETS | R1 and both nonauthor candidate audits | actual partial-assignment masses compared to independent subset sums; positive DP loops over polynomially many indices; ordinary bridge substitution rejected |
| FIBER-S3 (new) | R3 blind_report.md and blind exact results | degree3 transposition endpoint at length5 has81 ordinary words versus80 connected; retained as a checked counterexample |
| GRAPH (new) | R3 blind_report.md | uniform connected simple graph has triangle probability1/4; uniform X3 words require180/240=3/4; retained as a checked counterexample |
| GLOBAL | global_mass_results.json; R3 global_audit.md; R2 recursive_audit.md | every one of369 rational certificates independently reproduced; exact TV accounts for omitted support; at m2N covered mass tends to zero by proof |
| SOURCE | primary PDFs; all construction proof/audit source sections | fixed-permutation and cover normalization checked; long-cycle sampler not imported; DPS/mobile bijection not a hidden decoder assumption |
| HANDLE | historical M97 Sections3-7; coordinator_report.md | historical strong-lumping/pointwise failure retained; no handle Markov chain is used, so no unrelated diagnostic rerun |
| CP-1 | exact inequality21/2000>1/100 retained in role checks; proof.md conditional telescoping; R3 global finite coupling tests | cached-prefix marginal argument remains invalid; accepted proofs recompute actual conditional masses or use conditional coupling, never multiply marginal error bounds |
| STACK (new) | R2 recursive_audit.md; R3 candidate_audit.md | original recursive implementation failure repaired with explicit task/value stacks; fresh full forward law and1488 prescribed tapes pass;1200-step mechanical fixture uses stub oracles and is not a degree600 sampler benchmark |

Probability tests are exact rational checks of finite supports or actual
production execution. Seeded draws are validity smoke tests only. Complete
reports preserve precise domains, command lines, seeds, and limitations;
the universal claims rely on their proofs, not finite-test extrapolation.
