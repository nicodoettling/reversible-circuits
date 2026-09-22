# R5 final nonauthor audit

Status: **promote the reviewed mathematical and sampler claims**, with the dependency and scope qualifications below. No unresolved mathematical gap was found in the reviewed versions. The v1 CLI defect is retained as a genuine counterexample and is repaired in the reviewed v3. This is same-model internal review, not independent human certification.

## Exact reviewed objects and isolation

The blind report was frozen at 2026-09-22T05:55:11.341362+00:00, before any candidate proof or sampler was read. Its SHA256 is `22f49d8084f9e94e564cae6c6912d74788ebb70b766914ff13877ee36a9bce64`. It independently proves a weaker real-variable majorant sufficient for T0, the same essential fresh-pair comparison, a stronger all-large-component tail, and an exact small-component sampler construction. The exact initial brief is preserved in `blind-brief.input.md` with hash `601bf5519d98531f848778a8207aeab5bba264d126c0feadd93f8a6204a8427c`.

Blind isolation was achieved from current candidate proofs, other workers, and historical verdicts. It was not isolation from all project knowledge: repository-wide AGENTS framing and the parent operational task were inherited in context. Only the brief and its permitted primary sources supplied task-specific mathematical input before freezing. Runtime model identity/effort are not separately exposed; the run manifest requests gpt-6-astra/ultra.

After freezing, the following snapshots and their load-bearing historical dependencies were copied into this role directory and audited:

| Object | SHA256 |
|---|---|
| R1 `proof_v1.md` | `43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0` |
| R3 `sampler-v1.py` | `c8fc1bc78dc2c187c3f3cf7b71b58833aba3b1b4a10e19776717d5032591f40b` |
| R3 `sampler-v3.py` | `56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06` |
| R3 `proof-v3.md` | `f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868` |
| September 7 g0/1 sampler | `d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d` |
| September 7 primitive proof | `c779902224eaab4ebe2837fbb0d4aaaf9850aa4aede5443cd86259a746f6b9ba` |
| Positive connected-count implementation | `a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2` |

Copies and complete manifests are in `review-inputs-v1/` and `review-inputs-v3/`. The R1 header used an estimated freeze time; its separate manifest corrects that timestamp. This has no mathematical consequence and is not silently treated as an exact timestamp.

## Mathematical audit

Target: global fixed-length uniform ordered transposition identity words, with labels and positions distinguished and rightmost factor acting first. The new samplers draw exact uniform restrictions; total variation from the global target is precisely omitted mass. No local-chain, mixing, transitivity classification, or hardness hypothesis enters.

**R1-C1, source normalization: proved established input.** The DYZ primary source was opened independently during the blind phase. Proposition 1, equations (13)/(17), and equations (19)–(20) give the positive recurrence with `C(v,ell)=v! ell! h_(g,v)`. The fixed-permutation convention is also independently checked in Vakil Section 1.2 and Corollary 1.5 for the g0/1 primitive. The source documents and coefficient tests agree; no extra conjugacy-class, cycle-multiplicity, position, or component divisor is missing. Word reversal supplies the harmless convention translation for identity products. The sources are:

- https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- https://math.stanford.edu/~vakil/files/g01hurwitz.pdf

The DYZ article is published in Moscow Mathematical Journal 17(4), 2017, 601–633; publication information was checked against the author/institutional sources. Downloading PDF bytes through the local shell failed because network name resolution is restricted; web primary-source access succeeded. The lack of a local PDF byte hash is recorded in `DYZ-source-manifest.json`. The mathematical input equations and citations are preserved in the frozen report.

**R1-C2, factorial genus majorant: proved.** In the author's normalization the genus-zero recurrence yields a genuine probability vector `p_(a,b)`. Its sum is one, including singleton children. The coefficient inequality `2/(2j+2)! <= 1/(12^j j!)` holds for j=0,1 with equality and then decreases by the stated ratio. The potential difference `(v^3-v-a^3+a-b^3+b)/36=abv/12` dominates `a^2/12`. Thus the induction controls every genus simultaneously. This is stronger than the blind report's pointwise exponential majorant and does not appeal to fixed-genus asymptotics.

**R1-C3, fresh-pair comparison: proved.** The normalized weight of each newly inserted size-two/length-two component is 1/2. Matching choices contribute the second power of two and q!, giving exactly the author's `4^q q!`. A cost-k output has at most k such components; marking q of them gives at most `binom(k,q)` preimages. Requiring a prescribed removed label set to be isolated only decreases that preimage count. The same estimate at q=0 is ordinary label-set inclusion. This correctly pays for bridge conditioning.

**R1-C4 and finite tail: proved.** Component marking counts literal label sets and position sets exactly. The feasible degree restriction `v<=k+1` remains in force while bounding `B_v x<=v a`; only the resulting geometric majorant is extended beyond that degree. This avoids illegally evaluating the divergent two-variable Hurwitz series. The sum over genus is an entire exponential from the coefficientwise bound. The fixed top-level cutoff is preserved.

**T0 and separately named T1: proved in the reviewed argument.** The same error function

`eta(N)=1` below `2^160`, and `exp[-(log N)^2/(10 log log N)]` at or above `2^160`,

bounds both H0 and the stronger small-component-only H1 restriction uniformly for every feasible even `m` with `m^3<=N^2`. In particular it gives the original T0 range `m^5<=N^3`. All constants in the displayed finite-threshold calculation check: `a<=5/18`, `rho<=64 N^(-1/3)<=N^(-1/6)`, `K>=log N/log log N`, and the final exponent comparison. The same algorithm and eta work for every inverse-polynomial accuracy exponent; no accuracy parameter is silently changed. Finite exceptions have the explicit universal error bound one.

The boundaries m=0, m=2, N=2, N=1, and odd lengths are handled correctly. Odd lengths have no target law. This is polynomial time in N,m, not in log N wires. The first unproved mathematical step is **none identified after the explicitly checked published count inputs are accepted**.

## Decoder and implementation audit

**H0 and H1 are distinct exact laws.** In v3 the policy is applied consistently to the assembly table, branch weights, local sampler dispatch, and candidate label. H1 imposes component size<=K for every nontrivial component; H0 additionally retains all genus-zero/one components. Both use the original input's K in every residual subproblem.

**Marked decoder: proved.** Its full state contains the actual prefix permutation, actual exposed support partition, and remaining length. Every transition joins the partition and right-multiplies the permutation by the literal next edge. The terminal state tests both identity and full connectivity. The pruning condition can only remove impossible support connections. The explicit stack follows a strict remaining-length DAG and avoids interpreter recursion limits. Continuation probabilities telescope exactly. The retained factor `(m+1)` in the state count is essential and present.

**Assembly: proved.** The component containing the smallest remaining label makes the decomposition unique. Uniform subset unranking chooses its other labels and literal positions; local edges are relabeled consistently and remain in order. Equal component sizes do not create an additional quotient. Inspection of the actual loops agrees with the telescoping per-word proof.

**H0 g0/1 primitive: proved using the checked Vakil count input.** I read the full historical proof and code, rather than accepting its old status. Deleting the final transposition gives the stated disjoint connected/two-component cases. The endpoints distinguish the two split components, so there is no missing 1/2. Cycle objects with equal lengths remain individually assigned. The positive allocation DP aggregates the correct elementary symmetric and marked sums, including the forced opposite sides. The iterative decoder relabels children back to the correct support sets and appends the correct last transposition. Fresh endpoint and allocation checks below support this audit.

**Resource bounds: proved polynomial; displayed v3 exponents are conservative.** With M=N+m+2, Q<=(m+1)K M^4<=M^6 and count/key bit lengths O(M^2), the marked-state storage fits O(M^8), hence the stated O(M^10). The overall dictionary lookup/transition bound is O(M^16) before the additional bookkeeping allowance. Dictionary resize operations should be understood in aggregate: a single resize can reinsert many keys, but across geometrically growing tables its worst collision cost is O(Q^2) and is already dominated by the displayed total lookup bound. Thus this wording nuance does not invalidate O(M^20). Count-table arithmetic, binomial construction, fixed-capacity primitive caches, and g0/1 exact-rational arithmetic remain within that loose exponent. These are complexity bounds, not practical performance claims.

**v1 CLI counterexample: refuted, repaired in v3.** At valid T0 `(N,m)=(100000,1000)`, adjacent repeated pairs already give `Z>=binom(N,2)^500`, exceeding Python's default 4300-digit decimal conversion cap. The old CLI's `json.dumps` therefore raises ValueError. The witness and exact serialization operation are retained in `targeted_v1_checks.results.json`; no expensive sampler preparation was needed. The core API law was unaffected.

In v3, `_decimal_safe` uses a conservative bit threshold below the current decimal limit. Exact integer/hex and fraction/hex-rational encodings preserve every bit, including negative values, zero, and large numerator/denominator cases. Limit zero is correctly treated as unlimited. Independent tests under actual caps 4300, 640, and 0 pass, and the sampler never changes the interpreter setting. No floating-point conversion occurs. The CLI issue is closed for the reviewed scope.

## Independent computational evidence

All computations were supervised, standard-library-only, deterministic where stated, and bounded by 120-second commands. No heavy grid, installation, detached session, or outside-role write was used. Exact script hashes, Python version, git commit, commands, seeds, and raw results are recorded with each result.

| Artifact | Independent evidence | Result |
|---|---|---|
| `exact_checks.py` / `.results.json` | full permutation DP, connected assembly inversion; n<=7,m<=12; 78 recurrence coefficients, 20 insertion ratios, minimal connected counts | passed |
| `restricted_sampler_check.py` / `.results.json` | independently constructed connected unranking and rooted assembly; exhaustive equality with complete allowed word sets | passed |
| `targeted_v1_checks.py` / `.results.json` | 305 connected fixed-endpoint g0/1 count and branch comparisons through n=5; 900 forced labeled-cycle allocation checks | passed |
| same targeted artifact | valid-T0 decimal serialization counterexample | v1 fails as recorded |
| `v3_regression_checks.py` / `.cap4300.json`, `.cap640.json`, `.cap0.json` | exact integer/rational JSON roundtrips under three actual interpreter limits | passed |
| same v3 artifacts | eight H1 cases, three fixed seeds, with `g01.count`, `normalized_count`, and `sample` replaced by raising functions | passed; no hidden formula/decoder call |

The independent unranking sets include S3,m4 (27 words), S4,m4 (120), S4,m6 at K3 (1056) and K4 (3936), and N2 at m0,2,8. Complete word-set equality certifies all deterministic word diagnostics in these finite cases. The H1 isolation cases additionally include S3,m8, S4,m8 and S5,m12. Seeded checks establish implementation validity only; exact uniformity rests on the disintegration proof and exact finite law checks. No finite experiment is used to infer asymptotic negligibility.

## Claim ledger and coordinator action

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| DYZ/Vakil normalizations | proved established inputs | cited primary theorems | blind/source records; copied primitive proof | direct primary-source reading, exact counts | retain explicit citations |
| R1 factorial genus majorant | proved | positive DYZ recurrence | frozen proof_v1 | independent algebraic audit | promote |
| Bridge-conditioning comparison | proved | N>=m even | fresh-pair incidence argument | blind independent argument, finite ratios | promote |
| Uniform negligible tail in T0 and T1 | proved | source input and displayed parameter regimes | proof_v1 sections5–6 | constants, quantifiers, fixed cutoff audited | promote both, separately named |
| H0 exact restricted law | proved | DYZ and Vakil primitive | sampler-v3, proof-v3 | code/proof audit, fresh endpoint/allocation checks | promote |
| H1 exact restricted law | proved | DYZ count input and elementary marked DP | sampler-v3, proof-v3 | independent construction, dependency-disabling tests | promote |
| Expected polynomial bit/storage bounds | proved | standard exact arithmetic/fair bits | proof-v3 accounting | retained m, integer/rational and dictionary analysis | promote as conservative bounds |
| v1 CLI handles all declared certificates | refuted | default decimal limit | valid-T0 witness | actual serialization operation | retain regression |
| v3 repairs the identified CLI failure | proved for audited serialization behavior | ordinary Python JSON/base16 operations | v3 cap tests | actual cap0/640/4300 roundtrips | close defect |
| Human/external certification or novelty priority | unresolved / not claimed | outside this run | none | none | do not imply |

Recommended synthesis: accept T0 as achieved by either reviewed policy with the cited dependencies, state T1 as a separately labeled stronger result, and preserve the explicit finite exception/error function. H1 offers a simpler mathematical dependency set; H0 remains the requested broader restriction and is also supported. Keep the v1 failure and repair provenance. Do not turn these results into a claim about local-chain mixing, all-length global sampling, or wire-efficient complexity.
