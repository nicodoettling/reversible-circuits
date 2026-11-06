# R1 final author report v1 — positive genus-two recursion

Frozen2026-10-28 11:07 UTC. **Verdict: promote for independent review, PROVISIONAL.** This is an author candidate, not mathematical acceptance. Same-model reviews are correlated. The global campaign theorem remains OPEN.

The deliverable meets I1's constructive target at the proposed proof level: exact uniform connected words on any canonical v-set, any specified endpoint sigma and g∈{0,1,2}, length v+c(sigma)−2+2g, expected O(v^11 log³(v+1)) fair-bit time. In particular identity g2 has length2v+2 and TV error0 for every b>=1. The source normalization and all combinatorial/bit steps are explicit in proof-v1.md. Singleton positive genus is rejected. This is polynomial in degree v, not log(v), and is not an arbitrary-genus/global bridge theorem or a local-chain mixing theorem.

## New ingredient and exact dependencies

Goulden–Jackson's published1999 genus2 generating formula, after the residue form of Lagrange inversion and distinct-cycle polarization, reduces to three positive marker specifications. The apparently signed numerators regroup into weights A(a)=a²(a−1)(5a−7),B(a)=a²,D(a)=a²(29a−25). All are nonnegative for integer cycle sizes a>=1. At most three special marker slots occur. A table over A-size,A-cycle count,ordinary marks and constant-size masks sums every partially forced allocation exactly. The(1,1) split uses a tensor of the two genus1 marker transitions, retaining the required cross-moments. The algorithm never enumerates cycle subsets or endpoint profile inventories in production.

Full references and checked normalization are in source-verification-v1.md. The new formula input is [Goulden–Jackson Theorem1.1](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjjcta1999-2.pdf); its fixed-permutation conversion is explicit in [their predecessor Section2 and equation(2)](https://arxiv.org/pdf/math/9902009). S1.v2 and its scoped exact-version audits supply the genus0/1 counts and prior final-letter design. Published scalar counts are not being called a decoder: proof Sections4–6 give the disjoint word decomposition, conditional allocation oracle, actual stack algorithm and per-word probability cancellation.

## Claim ledger

| Claim | Author status | Assumptions/dependencies | Evidence | Check/action |
|---|---|---|---|---|
| R1-C2 positive fixed-endpoint g2 count | proved, provisional | Published GJ theorem; explicit class normalization; formal Lagrange inversion | proof-v1 Sections2–3 | Finite independent support counts pass; fresh source/proof review required |
| R1-D2 complete final-edge branches | proved, provisional | Elementary support/genus bound | proof-v1 Section4 | All finite branch totals pass; review multiplicities |
| R1-A20 forced(2,0)/(0,2) allocation | proved, provisional | R1-C2 + inherited g0 | proof-v1 Section5; sampler-v1.py | Exact partial-assignment comparisons pass |
| R1-A11 positive tensor(1,1) oracle | proved, provisional | Inherited positive g1 formula | proof-v1 Sections3,5 | Exact partial-assignment comparisons pass |
| R1-W2 exact word sampler | proved, provisional | D2,A20,A11; exact integer choices | proof-v1 Section6; sampler-v1.py | Full tiny forward law passes; fresh referee required |
| R1-B2 polynomial bit bound | proved, provisional | Constant marker slots; positive arithmetic; common denominator | proof-v1 Section7 | Explicit worst-case proof; timings are not its justification |
| Global all-length sampler | unresolved | Arbitrary larger genus remains missing | frozen campaign mission | No upgrade |

No internal missing lemma is presently identified within R1-T2.v1 under its published inputs. The first outstanding certification obligations are fresh blind and exact-version nonauthor reviews, clean coordinator reproduction and reconciliation. They are not replaced by this promote verdict.

## Computation and falsification

Coordinator-reserved bounded jobI1-J4 used current helperv0.3.2 and attempt000002 run.json with180s wall cap,1GiB address-space ceiling; command, code/helper hashes and runtime are in job-v1.json. It exited0. Python3.12.3, standard library only; exact seed null, diagnostic seeds1729,2718. Child elapsed1.187410812s. Actual RSS was not measured; the largest reference state layer had250 states, versus the preflight bound6240. Detailed machine-readable output is results-v1.json.

- 459 endpoint/genus count comparisons: every permutation of degrees1–5 and g0,1,2, against an independently implemented walk DP whose state includes the literal permutation and support partition. Every positive nonempty-length branch sum was also checked.
- 780 arbitrary partial-assignment queries on six individually labeled cycle lists of lengths2–6, covering all genus pairs with total<=2; 24 zero-mass queries. Reference assignments and marker slots were explicitly enumerated only in the finite audit.
- 19 complete forward laws of the actual production stack, covering every S3 endpoint at g0,1,2 and S4 identity g0: 8322 literal words, exactly one logical categorical tape per word, each with probability1/C. The S3 genus2 identity law contains2184 words each of probability1/2184. Whole-law equality covers every finite statistic, including prefixes, edges, repeats, support and windows, without relying on marginal histograms.
- Baselines S3,m4=27;S4,m4=120;S4,m6=3936. At m4 on four labels there is no full connected fiber; the global counts are reference regression values, not a claimed global use of this connected sampler.
- S3 length5 transposition endpoint remains81 total versus80 connected. The squareless(ab)^3 example remains a valid connected identity word, so insertion-fiber failure is retained. Singleton empty/zero cases,N2 unique words,odd identity lengths and seeded valid outputs through degree8 all passed.

No failed computational run or repaired candidate version occurred. The derivative form of Lagrange inversion was considered, then superseded before coding by the simpler residue-Jacobian formula; it would introduce an extra1/v and differentiated marker terms but is not needed. The initially allowed signed-arithmetic route is also unnecessary after positive regrouping. These are abandoned equivalent representations, not refuted theorems.

Historical negative findings remain: zero-square insertion, unweighted support-graph bias, insufficient scalar counts, partition-enumeration complexity, marked-cut forgetting multiplicity and CP-1/posterior normalization failures. The proof explains why the current disintegration avoids each applicable inference. The structural cut mechanism and global mass policy are separate workers' questions; this report does not override their findings.

## Delivery and next operations

Author payload is frozen by manifest-v1.json; no edits to frozen proof/code/report after publication. Any correction needs a new version and reopened downstream review. Coordinator should give a fresh blind referee only statement-v1.md plus permitted primary sources, then obtain a separate exact-version nonauthor audit of proof-v1.md,source-verification-v1.md,sampler-v1.py,audit-v1.py and results-v1.json. Reproduce the smallest decisive checks and integrate only the reviewed scope.

| candidate | claimed target | identity/product ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| R1-T2.v1 recursive marker sampler | Connected fixed-endpoint g<=2 uniform | All tested outputs valid; exact proof supplied | Not a global chain; component selection not claimed | Full small laws and independent support counts pass | promote for review, provisional |

Worker metadata: model/effort/tier inherited from the coordinator under requested Astra/ultra/default; server-returned service tier and actual allocation memory are not exposed. No descendants, separate CLI research sessions, local MCPs, installs, commits, central edits or permission changes. Work is confined to the owned role directory. Every file created here is enumerated in manifest-v1.json (except the manifest itself and mutable checkpoint); the preserved draft is explicitly labeled.
