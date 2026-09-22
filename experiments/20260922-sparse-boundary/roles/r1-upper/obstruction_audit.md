# Nonauthor audit of R2-O1

Reviewer: R1-upper, gpt-6-astra / ultra, same-model correlated internal review. R1 authored the separate positive upper-bound theorem and did not author R2-O1. This is not a blind review. R1 received the frozen task and old literature/project context, then the complete obstruction after freezing its own proof.

Input: `../r2-obstruction/obstruction-v1.md`, SHA256 `a6716e623768ded49b5ba1a2441abdddc8cb18c61be52d8a96b79387fe68b33f`. The input hash was saved before the audit in `proof-freeze.json`. Disposition: **ACCEPT for the mathematical obstruction, conditional only on the explicitly imported factorial genus majorant being source-verified by the coordinator**. The majorant's elementary induction was re-read in the hash-frozen previous proof and no issue was found. This role does not substitute its acceptance for coordinator certification.

## Checked statement

For every integer j>=64, N=2^(8j), m=2^(6j), with the unchanged top-level cutoff and full H0 predicate g<=1 OR v<=K, the proof gives

Z_A/Z <= 2^(-1-jm/2).

Here m is even and m^4=N^3 exactly, hence equals m_*(N). The exact H0 total variation error is 1-Z_A/Z, and tends to one. H1 error is no smaller because B is a subset of A. Thus P0 and P1 fail on the proposed benchmark. T0, existence of some other sampler, is not refuted.

## Claim-addressed audit

1. **Exact labels and interleavings: pass.** For a component-type profile the factor (N)_s product[(A_g(v)/v!)^a/a!] exactly restores disjoint labeled sets. Isolates are uniquely determined after choosing the active supports. Multiplying by m! restores distinguished position interleavings. The bound (N)_s<=N^s and allowing additional profiles only increase the numerator. Positive exponential coefficient extraction is therefore valid.
2. **All-genus small components: pass.** The v<=K term includes every g>=0. The bound by exp(b_K x), and the v>K bound by 1+b_v x, cover both overlapping branches of H0. No excluded-support shortcut or genus truncation weakens the numerator. Finite N and factorial coefficients make the evaluated functions convergent; no divergent unbounded-v all-genus generating series is used.
3. **Series constants: pass.** S_0<=9k/[8(1-q)] and S_1<=kx/[4(1-q)] follow from v!>(v/3)^v and b_v=(v³-v)/36. Under q<=1/2,x<=1,b_K x<=1, S_A<=29k/4<8k. The chosen x=k/N² gives the claimed coefficient bound.
4. **Top-level cutoff: pass.** P<=2N on the exact subsequence. K>=2 and log2 K>=1 imply K<=16j+2. The displayed b_K x bound is less than one at j1 and decreases thereafter. K is never recomputed on residual inputs.
5. **Exact denominator: pass.** For the symmetric transposition walk, convolution at even time yields sum of squared midpoint masses. Midpoint support is one parity class of size r!/2, giving return at least2/r!, valid also r2. This is a bound on the actual identity bridge count, not a guessed unconditioned normalizer.
6. **Integer subsequence and constants: pass.** r=floor(m/(6j))>=m/(12j)>=2, binom(r,2)>=m²/(576j²), r!<=2^m. The numerator denominator ratio simplifies to (1/2)[1152sqrt(2)e^4 j²2^(-j)]^m. The constant is <2^18. For j>=64, 2^18j²<=2^(j/2), proving the stated exponent. Exact finite integer checks below supplement the monotonic proof.
7. **Boundaries and scope: pass.** Empty/length-two/single-edge words are included; odd length and positive lengths at N1 have empty targets. These do not touch the asymptotic sequence. No new algorithm or hardness claim follows.

## Falsification checks

Command from repository root:

`timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r1-upper/audit_checks.py`

Existing Python3.12.3, standard library only, no stochastic seed. Run took approximately0.19 seconds. Before import the script checks the old positive-count implementation hash `a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2` against the saved manifest. No old files are written; `-B` suppresses bytecode caches.

Exact rational/integer checks, N2..64 and even m0..16:

- 567 allowed-count versus positive exponential coefficient comparisons;
- 304 truncated S_A(x)<8k comparisons under the finite hypotheses;
- 16128 exact subgroup denominator comparisons;
- all displayed integer j inequalities for j1..1000;
- 6300 checks of R1's sharper rising-factorial incidence variant, not needed by R2-O1.

All passed. Raw output: `audit_results.json`. Complete literals at S3m4, S4m4, S4m6 match the known counts27,120,3936. Fixed top-level(42,12,K5) retains all its allowed words. Finite tests cannot establish asymptotics; the elementary proof closes those steps.

No mathematical repair was requested. First unproved internal step: none identified after accepting the explicit genus-majorant dependency. The existence target T0 remains open. This acceptance is limited to the exact input hash above.
