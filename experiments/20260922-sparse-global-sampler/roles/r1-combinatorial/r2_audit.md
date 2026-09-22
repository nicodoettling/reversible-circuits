# Nonauthor audit of R2-A.v1

Completed 2026-09-22T05:58:46.975042+00:00; reviewer `/root/r1_combinatorial`. Verdict: **ACCEPT mathematical tail argument in the frozen reviewed version**, conditional only on the explicitly imported DYZ theorem. This does not independently certify the complete sampler implementation. Same-model role-separated review is correlated evidence, not external human certification.

## Exact review inputs

- Full proof snapshot: `r2_audit_inputs/proof_v1.md`, SHA256 518a5392f305aa7a7838a52ef8c28a2cacbb2e6bb52d285be7f0a8c01aa7a8d3.
- Full author results and verification script are preserved with hashes in `r2_audit_inputs/manifest.json`.
- R1's own proof/report were frozen before reading these inputs. Parent disclosed that related majorants existed, so this audit is not blind.
- Direct primary source checked: DYZ Proposition 1 Eq 13, Eqs19-20 and following ordered-word interpretation, plus genus-zero coefficient in Section 1.3 immediately after Eq 28.

## Claim-addressed conclusions

**R2-DYZ.v1: accepted.** Substitution r=ell-1 changes DYZ's index constraint i+j+ell=g+1 to i+j+r=g and gives a^(2r+3)/(2r+2)!. The h=C/(v!length!) normalization has exactly one sheet-label factorial and one ordered-position factorial. Connected support equals transitivity for transposition generators. Reversing all factors is a bijection preserving the identity target, support, component length, and genus. No fixed-genus asymptotic is imported.

**R2-MAJORANT.v1: accepted.** The pi weights sum to one by the exact genus-zero instance of the same positive recurrence; the coefficient inequality F(z)<=exp(z/12) holds at every order. The stated B_v difference is exactly a^2/12 plus a nonnegative sum. In the ordered extreme split (a,b)=(v-1,1) it is equality, a useful regression against swapped split parameters. Coefficientwise products and convex averaging are valid because all coefficients are nonnegative. The series argument is formal, and the later exponential evaluation is finite for all nonnegative arguments.

**R2-INCIDENCE.v1: accepted.** Every feasible nontrivial component has cost p>=v/2, so the base's isolated-label lower bound is correct. Unordered matching count includes 2^p p!; normalized pair weights contribute a further 2^p. Reverse deletion chooses p distinct minimal size-two components among at most k, giving exactly the claimed binomial upper bound. Each incidence is weighted by the final macro weight, not the original macro weight; R2 records this explicitly. The falling factorial lower bound remains positive at 2k=N, and p=0 is the identity ratio. Denominator F(N,k)>0 throughout N>=2 and even length because a repeated edge word exists. No removed support branch is treated as independent.

**R2-MARKED.v1: accepted.** The mark count has binom(N,v) label choices, binom(2k,2p) position choices, C(v,2p) internal words, and Z(N-v,2k-2p) complementary words. Cancelling factorials gives Eq R2.7 with no equal-component symmetry divisor. Inserting the specified removed labels as isolates proves the complementary-degree comparison. Summing genus to infinity is an upper bound between nonnegative terms. The bound B_v<=v^3/36, v<=k+1, and v!>=(v/e)^v yield exactly the displayed a,q. The final union bound is an expectation under the endpoint-conditioned law with normalizer Z(N,2k), not an unconditioned graph estimate. H0's omitted event is a subset of the larger event used here, so allowing arbitrary genus at small support is respected.

**T0 and T1 explicit constants: accepted.** For N>=2^145, L>100; under T1 the inequalities d>=N/2, k+1<=m, a<=2m^3/(9N^2)<=2/9 are valid forpositive even m. Then e^(1+a)<4 and q<=32m/N. The logarithmic comparisons yieldq<=N^(-1/3) under T0 and q<=N^(-1/4) under T1. The cutoff lower bound K>=floor(L/logL)>=L/(2logL) uses an actually eligible integer and does not recompute K during recursion. The absorption of 8N uses L+log8<=L^2/(16logL) for L>=100; this is stronger than needed for T0 and exact for the claimed T1 exponent. Both eta functions are fixed and negligible, uniformly over the length range, with no accuracy-power-dependent algorithm or runtime. T1 strengthens T0 separately rather than replacing the frozen target silently.

**Boundaries: accepted.** Empty length, odd parity, N=1/N=2, m=2, singleton support, and a cutoff beyond all feasible support sizes are classified correctly. The universal bound 1 below the effective threshold does not obstruct negligible asymptotics. H0 remains nonempty on feasible even lengths because it admits the size-two repeated-edge word.

## Fresh targeted falsification

Command: `python3 -B experiments/20260922-sparse-global-sampler/roles/r1-combinatorial/audit_r2_check.py`.

All assertions passed; raw data in `r2_audit_results.json`. This uses R1's independently written integer recurrence, not the author's script. Tested the **sharper R2 B_v**, not merely R1's weaker majorant: 78 exact cells through v=13, length=24. Tested 2273 exact falling-factorial incidence inequalities at N=2..40, even m<=min(N,24), all p, plus 3796 zero complementary branches. Independently checked size 2 exact connected words for genus 0..200 and the extreme-split B equality for v=2..1000. Decimal evaluations at N=2^145, 2^160, 2^256, 2^1024 serve only as boundary regressions; the constants were also checked symbolically above. Required word-enumeration and support-DP regressions were inherited from the independently run R1 suite, whose full input domains and results are preserved.

CP-1 is not a load-bearing test here: the proof never multiplies sequential marginal probabilities or claims independence after conditioning. It instead writes exact weighted incidences and a single union bound. The old cached-prefix product claim remains rejected; no step relies on it.

## Objections and limitations retained

- **R2-O1, bibliographic precision only:** the minimal formula A_0(v)=v^(v-3) is stated without its exact primary-source locus. Directly checked it at DYZ Section 1.3 after Eq 28 (PDF page 7). This discharges the issue without changing the mathematics; adding that locator is an optional exposition correction.
- **R2-O2, scope boundary:** the analytic statement alone does not certify exact component generation, expected random-bit runtime, or an implementation. Its global algorithm conclusion remains dependent on those separate audits, as the author explicitly says. No contradiction or mathematical repair is requested.
- No false lemma or finite counterexample was found. No claim of sharpness above exponent 2/3 or sampling hardness is licensed by this audit.

All inputs/reports are retained under this role. No other worker file was changed.
