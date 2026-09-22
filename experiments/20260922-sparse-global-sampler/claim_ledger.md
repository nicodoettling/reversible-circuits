# Append-only claim ledger

| ID/version | statement | status/audit | assumptions/dependencies | evidence | reviewer/version | regressions | action |
|---|---|---|---|---|---|---|---|
| T0.v1 | One poly(N,m) sampler, negligible TV uniformly even m^5<=N^3 | unresolved | exact H0 primitives plus uniform omitted-mass lemma, or alternate algorithm | plan.md | pending | all boundaries | investigate |
| H0.v1 | Exact conditional sampler on fixed-top-level allowed subset | conditional/provisional | g0/1 exact primitive; support-marked DP; assembly counts | user candidate; old Sept7 inputs | pending current review | fixed cutoff, high-genus small supports | implement/check |
| MASS.v1 | Excluded v>K and g>=2 mass negligible uniformly T0 | unresolved | exact bridge-conditioned component law | no proof yet | R1/R2 assigned | distinguish old g<=1 obstruction | primary obligation |

| MAJ.v1 | A_g(v)<=v^(v-3)[(v³-v)/36]^g/g! for all v>=2,g>=0 | proved-by-author/provisional | checked DYZ Eq13 and genus0 count | R1 proof_v1.md Sections2–3; independent R2 derivation pending freeze | root preliminary read; nonauthor pending | factorial kernel and small exact counts | cross-audit |
| INC.v1 | S(N-v,k-q)/S(N,k)<=(4k/(N-2k+1)²)^q for 2k<=N | proved-by-author/provisional | weighted fresh-pair incidence, no independence | R1 proof_v1.md Section4 | root preliminary read; nonauthor pending | label sets, q0,k, pair multiplicity | cross-audit |
| T1.v1 | Same H0 negligible sampler for every even m³<=N², eta1 below2^160 and exp[-log²N/(10loglogN)] above | conditional/provisional | MAJ,INC,tail,exact sampler/bit proof | R1 proof_v1.md Sections5–7 | nonauthor pending | T0 retained, boundaries, uniformity | audit as stronger version |

| MAJ.v1 / INC.v1 / T1-tail.v1 | Frozen R1 Sections2–6, same eta for T0 and T1 | proved/accepted analytic dependency | checked DYZ, exact weighted incidences | R2 r1_audit.md, r1_audit_results.json; root complete read | R2 current hash43fc4b84...; R5 preliminary scrutiny |237 macro cells8107 extensions,45 nontrivial rational tail comparisons | integrate only after sampler audit |
| CLI.v1 | H0 CLI emits exact certificates for arbitrary supported input size | refuted/repair pending | CPython default decimal-int conversion cap | R5 targeted_v1_checks.results.json; root separately identified | R5 frozen v1 | N100000,m1000 inT0; count lower bound already exceeds4300digits | R3 hex serialization repair, fresh R5 recheck |

| SRC.v1 | DYZ and Vakil exact normalizations, connected feasibility | proved/accepted | published count statements checked against canonical words | source_checks.md; R2 r1_audit; R5 report | root/R2/R5 direct primary reading | independent recurrence/endpoint counts | closed |
| DECODER.v3 | H0/H1 exact restricted sampling with fixed top-level K and explicit-stack connected DP | proved/accepted | SRC; H0 checked September7 decoder, H1 no nontrivial g01 dependency | R3 proof-v3.md; sampler-v3.py hash56b27019... | R4 sampler_review-v3.md hashd673444c...; R5 report hashf01600cf... | actualforward H0/H1, highgenus, fixedK, longstacks | closed |
| COST.v3 | ExpectedO(P20) bit time,O(P10) bit storage, one fixed algorithm | proved/accepted | exact arithmetic/fairbits; polynomial integer/map costs | R3 proof-v3.md hashf941c5e1... | R4 and R5 current-v3 review | m+1 cachefactor, dictionaryresizes, cutoffpow, g01storage | closed |
| CLI.v3 | Lossless big-integer/rational serialization fixes v1 decimalcap failure | proved/accepted repair | hex fallback, currentcap read without modification | R3 sampler-v3.py; R5 v3_regression_checks.cap*.json | R5 fresh cap0/640/4300 tests | CLI-DIGITS retained | close repaired dependency |
| T0.v1 / T1.v1 | Both H0/H1 global negligible sampling throughm³<=N², hence originalm⁵<=N³ | proved/current component audits accepted; canonical delivery pending | MAJ,INC,SRC,DECODER,COST | canonical proof.md and complete R1/R3 frozen proofs | R2/R5 full mathematical acceptance; R4 implementation | all registered relevant cases pass | final canonical synthesis review |

| LABEL.v3 | CLI target description unambiguously distinguishes H0 and H1 laws | refuted/presentation repair pending | policy field was correct but target text reused A(N,m) | R1 integration_cli_results.json; root proof usesAforH0,BforH1 | R1 final integration review | H0/H1 N4,m6 have distinct allowed counts yet same targetlabel | R3 minimalv4predicate-label repair; mathematical law unchanged |

| LABEL.v4 | CLI reports exact H0/H1 predicates, actual/original cutoff and generic allowed_count | proved/accepted repair | v4 changes only output metadata; all choice code unchanged | R3 sampler-v4.py hash cdb91799...; R1 integration_v4_results.json | R1 fresh AST and actual root-wrapper CLI recheck | H0/H1 distinct laws, diagnostic K0 and empty word | close INT-L1 |
| SG-T1.v1 | Canonical proof and fixed default H0 achieve T0 and stronger m³<=N² with stated eta and bit bounds; optional H1 also works | proved/accepted | all source, tail, decoder, assembly and cost dependencies accepted | proof.md hash f788eaec...; sample.py hash 2d74da26... | R1 integration audit; independent analytic R2/R5 and code R4/R5 audits retained | every relevant registered regression has expected outcome | mathematical objective achieved; final artifact/accounting closure |

## Final closed disposition

This is an append-only chronological ledger. The final statuses below supersede earlier provisional/open rows, which remain as the audit history. No unresolved dependency remains in T0/T1; out-of-scope questions and lack of external human certification are not hidden assumptions of these claims.

| Claim | Final status | Accepted assumptions and evidence | Independent check | Action |
|---|---|---|---|---|
| T0.v1 | proved / accepted | Exact original m^5<=N^3 target, achieved by stronger SG-T1.v1 | R2/R5 analytic audits; R4/R5 decoder audits; current canonical integration | complete |
| T1.v1 / SG-T1.v1 | proved / accepted | All even m^3<=N^2, one eta and one polynomial algorithm | R1 integration_audit_v4.md plus independent underlying audits | complete |
| MASS.v1 / MAJ.v1 / INC.v1 | proved / accepted | Checked DYZ recurrence, factorial majorant, exact weighted fresh-pair incidence | R2 literal reverse-incidence audit and R5 full proof review | closed |
| H0.v1 / DECODER.v3 | proved / accepted | Fixed cutoff, exact marked DP, checked g0/1 primitive, exact assembly | R4/R5 proof/code reviews; root complete forward laws | closed; v4 choice AST unchanged |
| H1.v1 | proved / accepted | Same size-tail theorem, elementary marked decoder; no nontrivial g0/1 call | R4/R5 primitive-disabling and forward tests | closed |
| COST.v3 | proved / accepted | Exact arithmetic/fair bits; expected O(P^20), storage O(P^10) | R4/R5 and canonical integration accounting | closed |
| CLI.v1 and LABEL.v3 | refuted historical versions | Digit-cap failure and ambiguous target name preserved | Exact witnesses in R5/R1 artifacts | retain regressions |
| CLI.v3 and LABEL.v4 | proved / accepted repairs | Hex output and explicit policy/cutoff metadata | Fresh R5 cap tests and R1 v4 AST/CLI recheck | closed |
| Delivery | verified | delivery_checks.json matches accepted proof/wrapper/source hashes and current CLI | Coordinator fresh bounded checks; full inventories/provenance | record native completion |
