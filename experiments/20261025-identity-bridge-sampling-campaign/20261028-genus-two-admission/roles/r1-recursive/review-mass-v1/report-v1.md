# Nonauthor exact-version audit of M-GROW.v1

Frozen2026-10-28 11:20UTC. **Verdict: ACCEPT the exact M-GROW.v1 proof and its stated FG.v1/M2 corollaries, under the explicitly checked published DYZ counting theorem. Material numbered objections: zero.** Coordinator reconciliation, the separately commissioned blind review and campaign acceptance remain separate. This is a same-model correlated nonauthor review, not external certification or statistical independence.

I authored the separate recursive genus-two construction, not this mass argument. I received the full frozen mass proof and its stated claims, so this review is not blind. The current blind review was neither read nor contacted. The complete assignment is input.md; all seven specified input hashes matched and are retained in intake-hashes-v1.json. In particular the accepted proof bytes have SHA256cdfcc097d50a8ed070c27fcc5b8ae700e0472769578f7ccd6ab7e5ac85178aef. No author artifact was changed.

## 1. Exact scope accepted

For each integer j>=64, N=2^(8j), m=2^(6j), and every integer0<=G<=2^j, define L=max{1<=v<=N:3^v<=(N+m+2)^4} once at the original input. E consists of literal ordered identity transposition words whose every nontrivial support component has genus g<=G or size v<=L. Rightmost-first products, canonical vertex labels and ordered positions are retained. The proof establishes

    Unif(Omega(N,m))(E)<=2^(-1-jm/2).

Thus any probability law supported on E has TV distance at least1−2^(-1-jm/2) from the global uniform bridge law. The conclusion needs no word decoder or distributional property within E. It includes fixed G, with j>=max{64,ceil(log2(max{1,G}))}, and G2 specifically.

This is a support-policy obstruction on the explicit sequence. It neither proves general sampling hardness nor refutes a uniform global sampler. It does not establish any all-N statement about m=N^(3/4), a local-chain gap, or efficient decoding for the growing genus range. The older provisional all-N blind claim is not used or upgraded by this verdict.

## 2. Published dependency and factorial majorant

I read the exact September22 source audit and the DYZ section of the earlier nonauthor reconstruction, then reopened the [primary DYZ PDF](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf). Proposition1 equation(13), Section1.2 equations(19)–(20) and the following ordered-transposition interpretation fix the normalization. The genus-zero expression following equation(28) gives h(0,v)=v^(v−3)/v!. Hence C(v,ell)=v!ell!h(g,v) for connected literal identity words, ell=2v−2+2g. Reversal changes product convention without changing identity or support. I import this published theorem; I do not reprove its underlying geometric input.

Multiplying the source recurrence by v! yields precisely

    v²(v−1)F_v=2 Σ_(a+b=v) binom(v,a) a b²(cosh(at)−1)F_aF_b.

The split is ordered. Substituting F_a=a^(a−3)t^(2a−2)H_a, including the singleton convention, gives numerator a^a b^(b−1) after extracting the a²t² in2(cosh(at)−1). The resulting nonnegative weights divide by v^(v−1)(v−1); their sum is1 by the genus-zero coefficient. Thus there is no hidden factor2, factorial or degree-label loss.

The coefficient inequality2/(2r+2)!<=1/(12^r r!) holds from r0 by its displayed successive ratio. The exponent identity

    b_v−b_a−b_b=abv/12>=a²/12

holds also when a or b is1; bv>=a here means the product b·v, not the indexed b_v. Since both children have strictly smaller degree, induction closes coefficientwise for all genus coefficients. The singleton H1=1 and b1=0 are valid bases. Therefore

    A_g(v)<=v^(v−3)b_v^g/g!

is uniform over all integer g>=0, not a fixed-genus asymptotic. This uniformity is essential for growing G and is actually present in the proof.

## 3. Component assembly and exact target normalization

A connected support component of an identity word itself has identity product because disjoint components commute and each component's action is confined to its own labels. The full word uniquely determines its support sets, internal ordered subsequences and position interleaving. For a type profile the factor(N)_s/∏(v!)^a a! chooses the unlabeled collection of labeled components, while m!/∏ell! interleaves internal words. Multiplying the C(v,ell) counts therefore gives exactly the normalized expression in the proof.

Unused singleton labels are determined by the chosen support and require no extra multiplicity. Replacing(N)_s by N^s and admitting impossible profiles with s>N only increases a series with nonnegative coefficients. A component contributes y^(v−1+g), precisely half its identity length. Every nontrivial component has positive half-length, so each fixed coefficient has finitely many contributing profiles. At positive evaluation x, the all-genus sums at each of finitely many v are dominated by exp(b_v x). The proof never substitutes a divergent all-degree, all-genus series into a probability calculation.

For the union condition(g<=G or v<=J), the bound exp(b_Jx)+Σ_(g=1..G)(b_vx)^g/g! is valid on both cases: on small v the first term already covers all genus, while on large v it covers the genus-zero term and the displayed sum covers the allowed positive genera. It intentionally double-counts some permitted weights, which is harmless for an upper bound. J1 and G0 are included: b1=0, and the positive-genus sum is empty at G0. This correctly bounds the enlarged event directly; failure of the smaller historical event is not used as an implication.

## 4. New finite numerator estimate and growing-genus uniformity

The factorial inequality gives exactly3Nq^(v−1)/v³ for the genus-zero term, q=3Nx. Summing1/v³<=1/8 from v2 gives S0<=9k/[8(1−q)]<=9k/4. There is no missing initial q term or index shift.

For g>=1, d=3g−3 is nonnegative, including d0 at g1. The inequality

    v^d <= v(v+1)…(v+d−1)=d!binom(v+d−1,d)

is valid with empty product1 when d0. Summing from v2 subtracts exactly the v1 term1. The derivative integral of(1−q)^(-d−1) gives the next inequality, and q<=1/2 gives the stated2^(d+2). Both inequalities remain valid at q=1/2 itself. Substitution yields the displayed

    c_g=(3g−2)!2^(3g−1)/(36^g g!).

Its upper bound(6g³)^g follows by separately replacing the factorial by(3g)^(3g), dropping g! from the denominator and bounding the power ratio by(2/9)^g. These are pointwise inequalities for every integer g>=1; no hidden constant depends on a fixed G.

For1<=g<=G, x^g c_g<=(6G³x)^g. Thus the entire sum is bounded by a geometric series whenever a=6G³x<=1/16, giving9k·a/(1−a)<=3k/5. Adding3S0 yields147k/20<8k exactly. At G0 the argument takes an empty sum instead of invoking a nonexistent positive genus. I find no lost term, sign, truncation or quantifier in this step.

## 5. Sequence, subgroup denominator and TV conclusion

For the declared sequence, x=2^(-10j−1) and q=3·2^(-2j−1). The finite conditions hold already at j1. The bound P<=2N and3^L>=2^L gives L<=32j+4; substituting into b_Lx gives the exact base ratio46656/73728<1. Its consecutive ratio is bounded strictly by8/1024. The separate genus condition follows uniformly for G<=2^j from6G³x<=3·2^(-7j)<=3/128<1/16. The cutoff is never recomputed after conditioning on a selected component.

For the denominator, the midpoint law of the transposition walk on S_r has p_k(sigma)=p_k(sigma^(-1)): reverse the sequence of involutive generators. Therefore its2k-step return probability isΣp_k². At fixed k the support lies in exactly one ambient parity class of size r!/2; Cauchy–Schwarz gives at least2/r!, even if the actual support is smaller. The r2 case is valid and needs no aperiodicity or mixing assertion. Embedding the words in S_N preserves identity and injects the word set.

With r=floor(m/(6j)), the estimates r>=m/(12j), binom(r,2)>=m²/(576j²), and r!<=2^m all hold. In the last estimate log2(m)=6j exactly. Combining the numerator with the denominator gives

    (1/2)[1152 sqrt(2) exp(4) j² 2^(−j)]^m.

The replacement of the constant by2^18 is safe because1152·2·81=186624<262144. At j64,2^18j²=2^30<=2^32; the ratio increases thereafter since sqrt(2)>(65/64)². This proves the exponent−1−jm/2 without rounding or an unproved asymptotic threshold. Finally the event complement has Q-mass0 and target mass at least the claimed amount, so the TV lower bound follows for every Q supported on E, whether or not Q is uniform.

## 6. Independent finite falsification

I wrote check-v1.py without importing an author module. The weighted-support walk uses explicit label tuples and edge counts. Component assembly uses the bivariate exponential coefficient identity sH[s,k]=ΣvB[v,l]H[s−v,k−l], unlike the author's least-label recursion. Moment checks use Eulerian-polynomial differentiation, unlike the author's Stirling-number expansion. These differences help expose implementation errors but do not create statistically independent model evidence.

Coordinator reservationI1-J6 ran via the current v0.3.2 helper and sealed attempt000002 run with60s timeout and1GiB address-space ceiling. Exit0; child0.322411692s, tool wall0.344031642s. Python3.12.3, standard library, no random seed because every check is exact. Actual RSS was not measured. Largest weighted-support layer:615 states. Command and hashes are in job-v1.json; raw results are results-v1.json.

All checks passed:

-490 exact event-count comparisons for N2..5, even m0..12, G0..4, J1..N, including singleton/zero-length, minimum length, and J1/G0 cases.
-28 DYZ recurrence cells and18 factorial-majorant cells against independently computed literal word counts.
-256 complete rational moment-chain checks through g64, q∈{1/2048,3/8,511/1024,1/2}, plus64 c_g envelope checks.
-129 coefficients of the L-series majorant and63 convex-weight degree checks through v64, including every ordered degree split in those cases.
-60 subgroup return lower-bound comparisons.
-All sequence finite conditions for every j1..256, with exact integer cutoff L; the final constant inequality for j64..256. For example exactL at j64 is1292, beneath the proof's2052 upper bound.

The checks failed to falsify the proof on this finite scope. The analytical derivation in Sections2–5, not those tests, supports the universal claim. Author finite tests were inspected but not treated as independent proof or simply rerun as the new evidence.

## 7. Reconciliation, boundaries and remaining limitations

I read the canonical September22 obstruction and the exact enlarged-cutoff corollary to check scope. They cover genus0/1 plus smaller/unrestricted support policies on the same explicit sequence. M-GROW's positive-genus sum is a new direct estimate for a genuinely larger event. Their older source-scoped statuses remain unchanged. I did not use the stronger all-N blind claim, and this report supplies no verdict on it.

Odd identity length has no target law. At m0 the empty word has retained mass1; at m2 every bridge is a doubled transposition and is retained. At N2 the top-level L equals2 and every even bridge is retained. None lies on the stated large-j sequence. In the finite numerator lemma these cases merely make the loose upper bound uninformative; they do not falsify it. Isolates have only length0 and no fabricated positive genus. Negative genus is excluded by the elementary connected-length bound.

Historical insertion, support-conditioning81-versus80, uniform-graph bias, marked-cut multiplicity and CP-1 failures remain intact. This proof uses no insertion or cut decoder, no unweighted support-graph transfer and no product of marginal probabilities. Its sole probability calculation is an exact global cardinality ratio plus the midpoint return identity.

The accepted current claim has no identified unproved internal step under the published DYZ recurrence and genus-zero formula. External theorem acceptance remains explicit. Campaign integration must retain the exact source hashes, this full report, the withheld blind report once frozen, and coordinator reproduction. The all-length polynomial sampler question remains unresolved; a successful general method must cover mass outside E or use another architecture. No change to the generating set or mathematical mission is warranted by this obstruction alone.

## 8. Files and operational provenance

Only this review subdirectory was written: input.md,intake-hashes-v1.json,checkpoint.md,check-v1.py,results-v1.json,job-v1.json,report-v1.md,manifest-v1.json. Frozen recursive construction files and all mass-author files remain unchanged. No descendants, CLI research sessions, packages, central edits, Git writes or permission changes. Astra/ultra/default was inherited/requested; server-returned tier was not observable. Git status was inspected; unrelated coordinator changes were preserved.
