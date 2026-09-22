# Claim ledger (append version changes; do not erase rejections)

`proved` is internal mathematical acceptance, not external certification.
Provisional and repaired-pending-recheck qualifiers prevent promotion before
the exact current proof and dependencies are checked by a nonauthor.

| claim | status | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|
| T0.v1: uniform connected length-2N sampling in expected poly(N,b) bit time | unresolved | positive constructive route and full audit | plan.md | frozen user target | BOUND, COUNT, FIBER, BIAS | construct/audit |
| COUNT.v1: polynomial positive scalar C(v,k) and global Z(N,m) | conditional, pending source recheck | DYZ Prop.1 eq.(13), cover-to-word normalization | Sep 5 R3 eq.(3)-(4) | inherited input only | COUNT, BOUND | primary and independent exact check |
| ASSEMBLY.v1: macro weights m! product C/ell! and uniform interleaving | provisional | disjoint supports; connected primitives | Sep 5 R3 eq.(1)-(4) | coordinator intake | FIBER, COUNT | reprove per-word cancellation |
| CUT.v1: nonempty interval J(w) with both sides componentwise genus zero | provisional | elementary prefix genus/incidence graph proof | M97 sections 3-4 | inherited proof to be checked | CUT, BOUND | r2 structural route |
| SQUARE.v1: literal adjacent-square insertion covers every genus-one word | refuted (historical, recheck pending) | no extra transformations | M97 section 6; (ab)^3 | historical M92/M95 dependencies | SQUARE | retain and independently reproduce |
| GLOBAL.v1: g<=1 assembly gives global TV equal omitted mass (exact primitives) | conditional | COUNT, ASSEMBLY, T0 and minimal sampler | planned global certificate | pending | BOUND, COUNT, FIBER | compute exact mass; no extrapolation |

Dependency graph: DYZ normalization -> COUNT -> global mass certificate.
Exact decomposition -> ASSEMBLY; ASSEMBLY + component primitives -> GLOBAL.
The two construction routes may discharge T0; scalar counts alone do not.

## Update 2026-09-07 approximately 21:19 UTC

| claim | status | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|
| COUNT.v2: positive recurrence and assembly count | proved, coordinator check; nonauthor recheck pending | DYZ Prop.1 eq.(13), Sec.1.2 eq.(19)-(20) primary normalization | global_consequence.md; global_mass_results.json, 91 independent count cells | coordinator v2 | COUNT,BOUND | retain, request global audit |
| R1-T1: exact connected endpoint genus0/1 sampler | provisional | Vakil positive formula; disjoint final-letter split; cycle-subset DP | roles/r1-recursive/proof.md | coordinator read; tests and nonauthor audit pending | all construction regressions | freeze and audit |
| G1-SAT.v1: m=2N and component genus<=1 implies full support and each genus=1 | provisional | length identity, 0<=g<=1 | global_consequence.md | coordinator v1 | GLOBAL,BOUND | nonauthor audit |
| G1-OMIT.v1: g<=1-only global TV tends to one at m=2N | provisional | Vakil identity bound; G1-SAT; subgroup return CS | global_consequence.md | coordinator v1 | GLOBAL; finite certificate separate | nonauthor audit; no hardness inference |
| G1-CERT.v1: 369 exact covered mass certificates N<=64,m<=128 | proved finite computation | checked integer C/Z code | global_mass.py, global_mass_results.json | independent DP/enumeration within script | COUNT,FIBER | retain as per-instance certificates |

## Update 2026-09-07 approximately 21:33 UTC

| claim | status | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|
| R1-T1.1 / S1.v1: exact connected g0/1 sampler, O(N^10 log^3(N+1)) expected bits | provisional, current proof frozen | primary Vakil formula; R1-C2..C6 | proof.md; frozen R1 report/code/results | coordinator reading; r2 and r3 reviewing exact hashes | full X4 laws; 112698 forced queries; 1745 endpoint comparisons | await nonauthor decisions |
| R1 implementation v1: recursive Python sample runs for every N without interpreter-limit issue | refuted as literal implementation claim; mathematical recursion unaffected | finite interpreter stack | coordinator_review.md | coordinator implementation observation | explicit stack / relabeling test | superseded by stack implementation |
| R1 explicit-stack implementation | repaired-pending-recheck | same mathematical sampler, task/value stacks | sampler.py hash d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d | author full rerun; nonauthors assigned | new stack/reconstruction checks | do not inherit old implementation review |
| R2-C1: exact cut sampler | provisional, independent report final | genus0 source count; M97 elementary cut; weighted unicycle grammar | R2 proof/report/code/results and SHA256SUMS | r1 fresh review assigned | parallel core; all macros through N4; square-zero fibers | retain secondary route pending audit |
| R3-B1..B7: independently derived signed-coefficient recursive sampler | provisional, blind report frozen | primary Vakil count | R3 blind_report.md hash e638cecd1c337a8d740be59f09aa7d9b895778616419dbcf85b3c9befde2250c | coordinator read after freeze | exact S3 laws; independent endpoint/support DP | preserve independent derivation, not automatic acceptance |
| Integration entry points implement declared targets | provisional; seeded validity passes | frozen R1 and exact assembly | sample.py, integration_results.json | r2/r3 review assigned | 15 connected,51 restricted draws;7 invalid inputs | exact law depends on proof, not smoke histograms |

## Update 2026-09-07 approximately 21:38 UTC

| claim | status | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|
| G1-COUNT.v1 / COUNT and ASSEMBLY | proved / accepted | checked DYZ Prop.1 eq.(13), Sec.1.2 normalization | global_consequence.md; complete R3 global_audit.md | R3 v1; source and different total-count recurrence | all369 certificates independently matched,91 coordinator small cells | promote |
| G1-SAT.v1 | proved / accepted | exact connected length identity | global_consequence.md | R3 global audit | A(0)=1,A(1)=0; saturated recurrence | promote |
| G1-OMIT.v1 | proved / accepted | checked Vakil bound; factorial/composition upper bound; subgroup CS lower bound | global_consequence.md | R3 global audit | 2016 subgroup bounds and all finite upper bounds; asymptotic proof separate | promote named restricted-method obstruction only |
| G1-SAMPLE.v1 | conditional theorem accepted | connected primitive pending certification | global_consequence.md; sample.py | R3 global audit | exact conditional coupling; actual integration boundaries | discharge primitive before unconditional claim |
| G1.v1.1 wording clarification | proved claims unchanged; editorial recheck pending | v1 mathematics unchanged | clarified size-two support and separate N0 case | coordinator, responding to R3 | preserve v1 snapshot and both observations | include in final delivery review |
| Frozen R1 fresh-process rerun | proved finite verification | exact frozen code | coordinator_r1_results.json; coordinator_r1_rerun.log | coordinator rerun | all exact digests match worker output | evidence only; nonauthor proof audit still required |

## Accepted synthesis — 2026-09-07 21:57 UTC

Rows below supersede earlier provisional statuses, which are retained as the
audit history. An original worker report saying provisional is intentionally
frozen; it is not a disagreement with the later, version-matched review.

| claim | status | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|
| S1.v2 / R1-T1.1: exact connected endpoint genus0/1 sampler; T0 for every N>=2,b>=1 | proved / accepted | checked Vakil fixed-permutation formulas; disjoint deletion; positive allocation DP; exact conditional reconstruction | proof.md; frozen roles/r1-recursive/proof.md and sampler.py | complete R2 recursive_audit.md and R3 candidate_audit.md; coordinator reconciliation | BOUND,COUNT,FIBER,SUBSETS,SQUARE; complete X4 probability law | promote sampler-theorem |
| S1 complexity: expected O(N^10 log^3(N+1)) bit time, polynomial space | proved / accepted | O(N^7) exact operations; O(N log(N+1)) bit operands; fair-bit integer rejection | proof.md R1-C6 | R2 and R3 complete audits | rational denominator; asymmetric cycle lists; no subset enumeration | promote in degree N, not wire count log N |
| Repaired R1 explicit-stack implementation | proved / accepted | frozen sampler.py d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d | R2 full forward execution; R3 prescribed tapes and deep mechanical fixture | current-version R2/R3; coordinator rerun | STACK: 5068 full forward words; degree600 fixture uses stub oracles | close repair gate; retain initial recursion-limit failure |
| R2-C1: exact cut-incidence sampler with reciprocal-mark rejection | proved / accepted | checked genus0 formula; elementary nonempty M97 cut; weighted unicyclic grammar and parser | roles/r2-structural/proof.md; roles/r1-recursive/structural_audit.md | R1 nonauthor; coordinator full reading and parser rerun | CUT,BIAS,parallel core,child-order multiplicity; all336 cut pairs at N3 | retain second complete route |
| G1-SAMPLE / G1.v1.2: exact Unif(A_01) and TV=1-Z_01/Z | proved / accepted | G1-COUNT/ASSEMBLY and now-accepted g0/1 primitives | global_consequence.md; sample.py | R3 global_audit.md plus candidate_audit.md; R2 recursive_audit.md | all369 certificates; full forward integration small cases; conditional coupling | close primitive gate; keep global target separate |
| G1-SAT and G1-OMIT: genus<=1-only mass tends to zero at m=2N | proved / accepted | length identity; checked count upper bound; subgroup Cauchy-Schwarz lower bound | global_consequence.md | R3 global audit and R2 recursive audit | exact finite bounds; asymptotic proof independent of plot | promote restricted-method obstruction, not hardness |
| SQUARE.v2: literal adjacent-square insertion is not surjective | refuted construction / checked witness | literal insertion into connected minimal words | all three role reports; (ab)^3 and tree extensions | independent rechecks; current samplers give correct positive word mass | SQUARE,SQUARE-TREE | preserve negative result |
| FIBER-S3: unconstrained endpoint counts may replace connected ones | refuted | transposition endpoint, degree3,length5 | R3 blind_report.md: 81 total versus80 connected | blind finite exact check | FIBER | retain witness; final deletion proof accounts for support |
| GRAPH-S3: uniform simple connected support graph gives uniform words | refuted | unweighted support-graph choice | R3 blind_report.md: triangle1/4 versus required3/4 | blind finite exact check | GRAPH | retain witness; weighted code route accounts for multiplicity |
| General arbitrary-genus connected sampler / all-length global sampler | unresolved, outside achieved T0 | higher-genus connected decoding or another global method | exact limitation in global_consequence.md | coordinator scope reconciliation | GLOBAL | no general closure or hardness claim |

Accepted dependency graph: checked Vakil count theorem -> S1 count formula ->
disjoint final-letter decomposition + positive moment DP -> exact per-word
law + bit bound -> T0. Independently, checked genus0 counts + elementary M97
cut + weighted parser + reciprocal rejection -> R2-C1 -> T0. Checked DYZ
normalization -> positive C/Z and exact selector; selector + S1 -> G1-SAMPLE.
The length identity + checked identity-count bound + subgroup return bound
prove G1-SAT/OMIT. No accepted edge uses local-chain mixing, Hurwitz
transitivity, DPS decoding, an exposed-prefix completion oracle, empirical
convergence, or the blind report's agreement alone. A future change to any
load-bearing source normalization, DP, parser, or reconstruction reopens its
downstream theorem and implementation claims.
