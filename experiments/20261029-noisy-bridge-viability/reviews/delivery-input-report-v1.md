# Sparse-noise identity words: bounded viability result

**Verdict: reject both specified sparse-noise hiding candidates; retain two proved efficient attack routes.** The six-relator family leaks surviving short relations. The path/star family leaks planted support even after arbitrarily many Hurwitz steps. These are scoped results in frozen M0, accepted through the campaign's internal proof-review gates. They do not refute sparse-noise hiding for arbitrary structured identity samplers, prove general sampling hardness, or supply a secure construction. Same-model reviews are correlated, not human or statistically independent certification.

The meaningful outcome requested by this study is delivered: a quantified efficient attack beyond the known pair controls, two fully specified constructions with negative outcomes, complete proofs and exact-version reviews, and reproducible finite diagnostics. Operator review of this scoped delivery remains separate from mathematical or campaign acceptance. The broader existence question stays **unresolved**.

## Frozen game and representation

[Model M0](model-v1.md): N>=2, even L, 0<=k<=L, q=binom(N,2), all transpositions on [N], products rightmost first. U(N,L) is uniform on ALL labeled ordered identity words, not a connected law or Hurwitz orbit. Q_k independently selects a uniform k-subset without replacement and replaces those gates with iid uniform transpositions; locations/tapes are hidden and a replacement may equal the old gate. Both worlds expose the same public A and compare complete observed words. All replies use fresh word/noise tapes under reused setup; no decoder oracle is provided.

Both candidates below have public parameters only and no secret setup key. Their exact mathematical sampling laws use independent uniform finite draws; unbiased-bit rejection gives expected polynomial time. The supplied Python Random tapes serve reproducible implementation tests, not cryptographic randomness. [Implementation scope and sparse injection pseudocode](r2-construction/implementation-scope-v1.md) handle the distinction between the mathematical family and machine-size validation code. No near-uniform sampler or assumed secure compiler supplies the hiding mechanism.

Runtime is polynomial in explicit N,L and each declared security index lambda, not automatically in log2(N) wires. Semantic correctness is disagreement with identity on uniform x in [N], bounded above by min(1,4k/N). The schedules give inverse-polynomial upper bounds, not negligible correctness. No PRC decoder/soundness property is imported.

## The main finite theorem: short relations survive

[Exact T0 statement](r1-theory/statement-T0.md), [full proof](r1-theory/proof-T0.md). Let L=6M, M>=2. Start with M arbitrary six-transposition identity blocks; permit arbitrary simultaneous relabeling and cyclic rotation, followed by at most b adjacent Hurwitz moves in either direction. Choices may be adaptive and depend on hidden setup. Set H=M-1-2b-k. If H>0, count all L-5 nonwrapping consecutive six-gate identity windows and accept when the count is at least H.

Structured acceptance is one, for every word, key and noise tape. Reference acceptance is at most

    min(1, (L-5) beta_N/H),    beta_N = p_6(id)^2 / p_12(id),

where p_r is the r-step all-transposition walk. For N>=1000, beta_N<1/40. Thus H>=M/2 implies one-query distinguishing advantage at least 7/10. The deterministic scan uses O(L) label operations. With t independent fresh reference replies, accepting only if all t pass gives reference acceptance at most (3/10)^t; this product uses the actual conditional independence of the reference replies. A single reply already breaks reused-setup security.

An explicit schedule is lambda>=32, N=lambda^2, M=N, L=6N, b=floor(N/8), k=lambda. It has H>=M/2, k/L=1/(6lambda), and semantic error bound 4/lambda. This is a finite theorem with an explicit polynomial schedule, not an extrapolation from spectra or finite experiments.

The proof uses only elementary inputs. Even-time return probabilities are nonnegative spectral moments, hence log convex, giving p_(L-r)(id)/p_L(id)<=p_r(id)/p_(2r)(id) for even L>=2r. Completion counts bound the r-window bridge density relative to iid gates. Every fixed-coordinate replacement preserves that iid reference and the density inequality. Therefore, for every k,

    Pr_Qk(U)[a fixed r-window has identity product] <= p_r(id)^2/p_(2r)(id).

An exact c6 count and a disjoint-doubled-edge c12 lower count prove the numerical constant. The candidate retains H disjoint witness windows pointwise; the reference needs only linearity and Markov, not independence of overlapping windows. No mixing theorem or historical irreducibility claim is used.

## Candidate outcomes

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| [C1-v1](r2-construction/candidate-1-v1.md), [runtime erratum](r2-construction/candidate-1-runtime-erratum-v1.md) | Its explicit structured law, compared with global U under matched Q_k | Yes: six distinct-edge relator; all signed moves preserve product | Generation varies labels; its Hurwitz stage preserves orbit data and has no global-weight guarantee | Complete N4,L6 noisy laws for s=0,1,2 and all k; mandatory global baselines; all signed moves on small bridges | **Reject** frozen sparse-noise schedule |
| [C2-v1](r2-construction/candidate-2-v1.md) | Its path/star structured law, compared with global U under matched Q_k | Yes: two different factorizations of inverse long cycles | Every draw has planted support m+1, preserved by any number of Hurwitz moves | Exact candidate identities/marginals at S3L4/S4L4/S4L6; disjoint-pair count check at S6L4; finite support and schedule checks | **Reject** frozen sparse-noise schedule |

C1 samples each ordered distinct quadruple (a,b,c,d) uniformly and emits `(ac),(cd),(ab),(ad),(bc),(bd)`. All six edges are distinct, so the relation witness extends beyond doubled-pair and mirrored controls. Concatenate B blocks and apply s uniform signed adjacent Hurwitz moves. Its frozen schedule is N=lambda^2, B=lambda^6, L=6B, s=floor(B/10), k=lambda, lambda>=2. The original general random-bit estimate omitted s log L; the preserved erratum corrects it without changing the law. Its schedule and every attack below remain unchanged.

C2 was selected only after C1's rejection. With m>=2, choose an ordered injection a_1,...,a_(m+1), concatenate the path `(a1 a2),...,(am a_(m+1))` and the ascending star `(a1 a2),...,(a1 a_(m+1))`, then apply s signed adjacent Hurwitz moves. It creates one full-length relation, not many constant-size null blocks. Its frozen schedule is N=lambda^6, m=lambda, L=2lambda, s=L^3, k=floor(sqrt(lambda)), lambda>=9. This removes the bounded-move premise as a useful design defense, but leaves support exactly m+1 before noise. No third candidate was started.

## Quantitative attacks and query costs

Advantage means the difference of acceptance probabilities; equal-prior success is (1+advantage)/2.

| Attack | One sample / reused setup | Rigorous effect | Samples and time | Evidence/status |
|---|---|---|---|---|
| T0 unaligned six-window scan | Every-key one-query attack; also reused setup | >=7/10 when N>=1000 and H>=M/2; reference false acceptance <=(3/10)^t for all-t repetition | One query, O(L) label operations | **proved**, scoped internal acceptance; T0 proof and two full reviews |
| C1 aligned null-window threshold | One query; no hidden key | Advantage >=1-min(1,N! binom(B,a) q^(-a)), a=ceil(B/2), provided B-2s-k>=a; frozen schedule deficit exp(-Omega(lambda^6 log lambda)) | One query, O(L) label operations | [Full proof](r2-construction/candidate-1-rejection-v1.md), [coordinator review](reviews/coordinator-C1-review-v1.md); **proved** |
| C2 word-support threshold h=m+1+2k | One query, arbitrary number of Hurwitz moves; also reused setup | Advantage >=1-min(1,binom(N,h)binom(h,2)^(2m)/D(N,m)), D=(N)_(2m)(2m)!/(4^m m!); requires N>=2m,h<=N | One query; O(L) expected dictionary operations, or deterministic sorting in O(L log L) comparisons | [Full proof](r2-construction/candidate-2-rejection-v1.md), [author-distinct review](r1-theory/review-C2-v1.md); **proved** |
| C2 frozen schedule | Same test | False acceptance <=lambda^(-lambda) for lambda>=1024, hence advantage >=1-lambda^(-lambda) | Same one-query cost | Exact onset audited and integer inequality checked |
| C1 all-six-distinct, finite case | One query at N4,L6,s0,k1 | Advantage exactly 149/984; probabilities 1/6 versus 5/328 | Six-gate inspection | **exact finite fact**, predeclared statistic; no asymptotic extrapolation |
| LC1-v3 local-observable transfer | One-query transfer only; general reused-key amplification not asserted | An available signed s-coordinate bias delta becomes alpha_s delta/(2*3^s), alpha_s=binom(L-s,k)/binom(L,k), for k<=L-s | O(4^s q^s) f evaluations plus explicit rational costs; expected polynomial time for fixed s under public evaluation/bit-size assumptions | [Statement](coordinator/local-channel-statement-v3.md), [proof](coordinator/local-channel-proof-v3.md), fresh r2 and r3 reviews; **proved** |

The C1/C2 reference bounds are exact change-of-measure arguments: for iid V and F={product V=id}, Q_k(V) is still iid, while U=V conditioned on F. Charge Pr[F] once, before applying independent-window or support counting under iid V. C1 uses p_L(id)>=1/N! and p6(id)<=1/q. C2 lower-bounds the actual literal global bridge count by D, counting disjoint doubled edges in every order. The doubled edges are a counting subset of the reference, not a proposed security candidate. There is no silent replacement of U by iid or connected words.

The blind adversarial role also derived a separate C2 bound 1-2(18/lambda)^lambda at lambda>=81. Its complete argument is retained in [BS3](r3-adversarial/blind-supplement-v3-C2.md), labelled **provisional** and not used to strengthen the accepted canonical claim. It is unnecessary for either rejection, and has not received a fresh author-distinct audit of that exact alternative proof.

## Exact checks and boundary findings

All jobs used the current sealed attempt and v0.4.4 bounded helper; one mathematical job at a time, 1 GiB address-space limit, 60 or 120 seconds, no dependencies beyond Python 3.12.3 stdlib. The initial inert smoke also passed. Commands, estimates, exits and output paths are in the [job registry](coordinator/job-registry.json). Every job completed; no output truncation, resource failure, partial mathematical journal or active job remains. Each invocation used a fresh Python process with bytecode caching disabled. The tests establish exact finite facts and implementation regressions, not an asymptotic theorem.

| Job | Check | Result/artifact |
|---|---|---|
| J001 | Inherited projection/replacement identities; global counts 27/120/3936; N2/empty/odd cases; pair attenuation smoke; CP1; 108 exact local-channel cases | [Raw results](coordinator/regressions-v1.json), [interpretation](coordinator/regressions-report-v1.md), passed |
| J002 | C1/C2 identity, injectivity, uniform coordinate marginals; all signed moves on small bridges; support/count checks; seeds 17,29,43 for implementation regression only | [Raw results](r2-construction/results-candidates-v2.json), [code](r2-construction/candidates_v1.py), passed |
| J003 | Return DP for N2..7; exact c3/c6 counts; moment ratios/maxima; all k and local masks in eight window cases; 6300 witness-survival cases; constants/boundaries | [Raw results](r1-theory/results-T0-v1.json), [checker](r1-theory/check-T0-v1.py), passed |
| J004 | Every literal N4,L6 word, all k0..6 and C1 s0/1/2; exact integer channel; independent brute Q1 check | [Raw results](r3-adversarial/exact-c1-results-v1.json), [checker](r3-adversarial/exact_c1.py), passed |
| J005 | Independent pointwise word evaluation recovers S4L6=3936 and S6L4=765, with D(6,2)=270; new LC1 distinct-denominator fixtures | [Raw results](coordinator/final-decisive-v1.json), [checker](coordinator/final-decisive-v1.py), passed |

J004 stores exact summary probabilities and complete feature histograms, reproducible from the literal-word script. It covers gate multiplicities, adjacent repeats, support/components including weighted component profiles, prefix/window/endpoint cycle types, and per-position edge frequencies. Endpoint cycle type determines sign, fixed points and the standard character, so those endpoint diagnostics are included. Sign and endpoint distance/support bounds shared by both worlds are not presented as attacks. No secret subset-product interface or persistent secret key was posited; meet-in-the-middle key recovery is unnecessary and no recovery-hardness assumption is claimed.

Selected exact full-word TV distances (these are descriptive optimum finite tests, not held-out security estimates):

| C1 scrambling steps s | k=0 | k=1 | k=2 | k=5 | k=6 |
|---|---|---|---|---|---|
| 0 | 163/164 | 323/328 | 12011/14760 | 0 | 0 |
| 1 | 157/164 | 73/82 | 17657/36900 | 0 | 0 |
| 2 | 63/82 | 93437/147600 | 716081/2214000 | 0 | 0 |

All one-coordinate marginals are uniform. At k=1 all endpoint cycle-type histograms agree, despite the large complete-word gaps. At k=L both laws are always iid. At k=L-1, any source with uniform coordinate marginals also becomes exactly iid: conditional on the sole retained position, that gate is uniform and independent of all fresh gates. This holds for both frozen candidates and U, and is retained as a genuine boundary limiting any broad impossibility interpretation. It does not assert hiding at their sparse k/L schedules.

Odd L has no identity words. L=0,k=0 and N=2 are singleton laws with zero advantage. L=2 has the doubled-gate reference and does not support these beyond-pair conclusions. The T0 local bound requires L>=2r: at N3,L=r=6,k=0 the full window is identity with probability one, whereas p6^2/p12=1/3, explicitly refuting its omission. C2's D-count requires N>=2m and is not applied at the small validation cases violating that premise. Nonpositive witness budgets, insufficient support separation and near-total replacement give no claimed sparse-noise attack.

## Audit, repairs, and retained negative evidence

The [claim ledger](claim-ledger-v1.md), [reconciliation](reconciliation-v1.md), and machine-readable [campaign claims](../../research-campaigns/noisy-bridge-20261029/claims.json) close only the exact versions cited. Full worker reports: [theory](r1-theory/report.md), [construction](r2-construction/report-v1.md), [adversarial](r3-adversarial/report.md). Blind B1/BS1/BS2 preceded the proposed proofs; C2's algorithm disclosed its support motivation, so BS3's limited blindness is recorded. The coordinator read full proofs and reports and reran the smallest decisive counts with an independently written evaluator. No review verdict alone was treated as proof acceptance.

Two LC1 repairs remain visible: v1 omitted possible q^s rational denominator growth; v2 omitted explicit public f evaluation and value-bit bounds from the efficient corollary. The probability identity did not change. [V3](coordinator/local-channel-statement-v3.md) includes both premises and received a [fresh r2 full-proof recheck](r2-construction/review-LC1-v3-v1.md), [r3 recheck](r3-adversarial/review-LC1-v3.md), and targeted exact fixtures. C1's runtime erratum is preserved. The first C2 checker used an infeasible factorial(N) implementation; it was rejected before execution, replaced by a short falling product, and retained as source/history. The dense-mixing route was superseded, not refuted. CP1, one-sample-versus-reused-key counterexample, exact high-noise equality and all scope failures remain in the [regression registry](regression-registry-v1.md).

Historical AGENTS/HANDOFF and PROJECT_MAP disagree on inherited irreducibility status; no result here uses that input. The historical mixing-only GOAL_SPEC is explicitly superseded for this authorized M0 study. No central maps, manuscripts, skills, primary worktree, continuous-prc project or supervisor configuration were edited. No external theorem, app/local MCP, installed package, additional research session or worker descendant was used.

## Recommendation and remaining obligation

**Deprioritize C1 and C2 as sparse-noise hiding constructions.** Their failures survive the precisely stated noise and, for C2, arbitrary Hurwitz scrambling. A later redesign must first derive and compare its labeled weighted support-component law with global U, and quantify its public short-relation surplus after its actual transformations. Those are necessary design checks, not a sufficient security criterion or an assumed relator compiler. Whether a genuinely different structured construction can hide under sparse M0 noise remains unresolved. No third candidate, new campaign, sampler programme or automatic continuation is authorized by this report.
