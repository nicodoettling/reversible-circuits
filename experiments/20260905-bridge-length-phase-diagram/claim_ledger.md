# Audited Claim Ledger

Status: final; classification `quantified-phase-diagram`. "Proved" means the mathematical argument survived
this run's internal audit; it is not a claim of external human certification.
Every sampler below always returns its requested endpoint and length.

| claim | status | parameter regime | assumptions | artifact | independent check | action |
|---|---|---|---|---|---|---|
| A bridge is feasible iff endpoint parity matches m and m≥N−cycles(g) | proved | N≥2; N=1 only m=0 | elementary cycle splitting and pair padding | R1 report boundaries | all endpoints through S6; coordinator domain audit | retain explicit N≥2 exception |
| At most m active labels in an identity word | proved | even m≥0 | any active label occurs at least twice | R1 report | R2 fresh short audit | promote |
| Exact first-appearance sampler, m^(O(m)) poly(N) | proved | identity bridges; m parameterized | correct embedding factor (N)_k/2^b | R1 report and short_exact.py | R2 independent canonical enumeration | retain elementary FPT baseline |
| Blind pattern embedding weight (N)_k | refuted | simultaneous introduction of two labels | ignores ordering symmetry | R1 report eq4 | already fails at m2; exact observed masses checked | retain negative correction |
| Exact defect-type DP, exp(O(sqrt(min(m,N)))) poly(N,m) expected bit time | proved | every feasible endpoint; m is input/output length | positive per-permutation cut/join recurrence; fair bits | R1 report eq1–3 | R2 fresh_short_audit.md; 90,743 cone-layer checks; coordinator rerun | promote exact m=O(log² N) regime |
| Bounded-time short sampler with TV≤epsilon and valid fallback | proved | same state inventory; overhead poly(log1/epsilon) | finite random-bit rejection cap and coupling | R1 report | R2 explicit 336 random-tape enumeration | retain exact expected vs bounded approximate distinction |
| Polynomial exact minimal arbitrary-endpoint sampling | proved | m=N−cycles(g) | positive cycle split/interleaving recurrence | R1 report eq5–6 | all endpoints through S6; fresh audit | retain internal primitive; public identity only m0 |
| Literal full midpoint type inventory has exp(Omega(sqrt(m))) states | proved | even m≤N; superpoly when m=omega(log²N) | explicit enumeration architecture | R1 report | R2 independent midpoint inclusion checks | named-method obstruction only |
| Old-long discarded bridge mass ≤3r exp(−q/144) | proved | retained rank r≥6; q≥4ceil(log2N) | old completion pointwise bound, exact star token projection, full endpoint denominator | R2 Lemma S, D12–D17 | R1 fresh_dense_audit.md, every feasible S6 endpoint at L380/381; coordinator line derivation/rerun | strongest new dense proof step; promote |
| Dense TV≤min(1,3N² exp(−floor(m/[2N(N−1)])/144)) | proved | N≥5; q≥4ceil(log2N); arbitrary feasible endpoint | audited stable sort, Féray star sampler, CLR endpoint spectra, retained floors | R2 Theorem D, D1–D19 | R1 fresh audit, 25,228 floors and 173,520 rank5 branches; coordinator primary-source check | promote quantified dense regime |
| m≥2N(N−1)ceil(144 ln(3N²/epsilon)) suffices for epsilon-close sampling | proved | feasible m; N≥5; 0<epsilon<1 | preceding theorem; exact rank≤4 base | R2 Corollary D2 | R1 fresh audit including ceilings, all ranks, bits and epsilon quantifiers | replace fixed m2N³ schedule in proposed patch only |
| Smaller epsilon at fixed dense (N,m) follows just by more computation | unresolved | below the dense output-law bound | no tunable fixed-length connection primitive supplied | R2 scope | auditor preserves limitation | do not claim arbitrary accuracy at fixed length |
| Exact component, labeling, surplus and interleaving law | proved | all feasible identity bridges | disjoint support decomposition | R3 eq1–2 | M02 §1; fresh per-word enumeration; coordinator reconciliation | promote |
| All connected scalar counts C(v,k), and Z(N,m), are polynomial-time computable | proved | v,k and N,m variable | DYZ Prop1 eq13, C=d!k!h; positive assembly DP | R3 eq3–4 and component_audit.py | coordinator original rational recurrence vs independent labeled DP: 78 cells N≤6,m≤12 | counting is discharged, separate from sampling |
| DPS exact connected minimal sampler | proved | v≥2,k=2v−2 | Props1,3; Thms4–5; v-to-one root quotient | R3 eq5, M112/M119 | primary PDF; all 11,520 v4 rooted inputs | retain conditional target only |
| All-minimal global sampler has exact TV 1−Z0/Z | proved | even 0≤m≤2N−2; Z0 positive | restricted exact macro law and DPS | R3 eq6 | exact required TVs 1/9,1/20,11/41; coordinator check | promote polynomial per-instance mass certificate |
| Sparse global TV≤min(1,m⁴/[48(N−m+1)²]) | proved | even 0≤m≤N | DYZ genus ratio; fresh-matching incidence; DPS | coordinator derivation; R3 eq7, sparse_bound_audit.md | fresh nonauthor R3 proof audit, coordinator independent count checks | promote sparse approximate regime |
| Minimal-only TV tends to one at m=Theta(N^alpha), 2/3<alpha≤1 | proved | fixed alpha and positive scale constants; even m | forest identity and embedded-subgroup return lower bound | R3 eq8–10 | R3 audited coordinator base proof; coordinator checked stronger exponent | retain named-method obstruction and vacuous finite bounds |
| Dense-to-connected rejection costs constant expected calls | proved | exact alpha=C/Z≥1/2; global dense TVδ≤1/4 | endpoint-valid proposals; support test | R3 eq11–12 | coordinator conditioning/return-bound audit | allow with explicit connected error≤4δ |
| Support-marked connected DP is exact | proved | all feasible connected inputs; poly for v^(2v) under a fixed polynomial cap | state (permutation,support partition), positive recurrence | R3 eq14 | exact small per-word checks; coordinator state/bit audit | retain correct short connected primitive |
| Certified hybrid TV≤1−Z_allowed/Z+epsilon/2 | proved | allowed exact/approx connected primitives under explicit polynomial work/acceptance caps | exact macro counts; component error≤epsilon/(2N) | R3 eq13–14 | coordinator coupling and eligibility audit | promote per-instance reduction/certificate; no global overlap claim |
| DYZ recursive term sampling already decodes to uniform words | unresolved | positive genus | no bijection/multiplicity proof | R3 first open step | scalar-count vs marked-prefix distinction checked | do not infer sampler from counts |
| Connected genus-one identity sampling in poly(v,log1/epsilon) | unresolved | k=2v; v unbounded | no required primitive supplied | R3 standalone lemma | focused primary search found only different endpoint/accuracy or coherence primitive | first concrete open family; no novelty claim |
| All-length polynomial sampler | unresolved | every feasible (N,m,epsilon) | regimes/certificates do not cover all inputs | phase_diagram.md | synthesis of all role bounds | classification is quantified-phase-diagram |
| Computational hardness in uncovered band | unresolved | remaining length/accuracy pairs | no computational reduction | none | all negative results scoped to named methods | no hardness claim |

Artifacts named R1/R2/R3 are the corresponding `roles/*/report.md` files.
Fresh audits are written by nonauthors in the other role's directory.
The final cross-document consistency audit by R3 accepted the synthesis at
15:56 UTC; all three numbered observations were resolved. Its reviewed
snapshot hashes are in `roles/r3-intermediate-hybrid/synthesis_audit.md`.
No minority or negative finding was discarded: the pattern symmetry error,
the conditioning cost, the minimal-only asymptotic failure, the type-table
blowup, and the scalar-count/sampling distinction all remain recorded.
