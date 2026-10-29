# Exact-version referee report: LC1 versions 1 and 2

Reviewer r3-adversarial, 2026-10-29. The statement-only blind proof was frozen in BS1 before either proposed proof was read. This review preserves a correction instead of silently replacing the first version. Same-model review is correlated; a separate fresh reviewer is required for repaired-version certification.

## Inputs and SHA256

Paths are relative to `experiments/20261029-noisy-bridge-viability/coordinator/`.

| File | SHA256 |
|---|---|
| local-channel-statement-v1.md | bd0a5d3bbd88abd8c07fd32af9e16d51794022c7f3ee7cd2fa6ece569180ed6c |
| local-channel-proof-v1.md | ecaa79af7f661f27df560e700ab308efb7ee0c6e703725f0ba566aba049df274 |
| local-channel-statement-v2.md | d6221e67e61f96fcd9f83b9937cbf0fbf0acc517eb1c73db35af010bf2d24d42 |
| local-channel-proof-v2.md | 5f2218e69ab89b67fc34ef0d736ed80f77bd8ca9efbca13b80cb7183af5249b5 |
| regressions-v1.py | 037a43b42fbfefbb8f31049d571a1959eb16f9c07c0955338fbb8226aad9dc1a |
| regressions-v1.json | 92ed9ec146f4b7352b32ccdbb6d8b5b838b8b859353777255d578abaf6169fe4 |

I read the exact proofs and finite checker, and inspected the associated results. The regression script was executed by the coordinator under J001; I did not launch a duplicate mathematical process. The JSON records Python 3.12.3, standard-library exact arithmetic, commit `61cba521d833996a3232a5c2516bb6c213e6b6ce`, and a passed result. Its source and results are not a proof of the unrestricted identity.

## Probability identity: both versions pass

The proof correctly defines commuting coordinate-average projections E_j and the decomposition f=sum_S f_S. The restricted exact-k channel multiplies f_S by alpha_|S|, since a component survives exactly when no coordinate in S is selected. This is counted directly as a uniform-subset probability. It is not a product of single-coordinate marginals. Independence of the replacement tape from the whole source word ensures that the conditional channel depends only on the fixed observed tuple.

All eigenvalues used for inversion are positive under k<=L-s. The bound ||g||_infinity<=3^s/alpha_s is valid and places h=(g+C)/(2C) in [0,1]. The exact affine identity T h=1/2+alpha_s f/(2*3^s) yields the oriented acceptance difference. No source-coordinate independence, group invariance, endpoint mixing, secret-key information or global bridge assumption is required.

The public-setup application is correct pointwise for I and f fixed from public A. Selecting f from hidden K would be an invalid adversarial interface; both statements explicitly exclude this. General reused-key amplification is correctly not inferred from an averaged one-sample gap. The CP1 failure mechanism is absent because there is no sequential posterior restriction: the entire channel is conditioned on a fixed source tuple, with a directly computed joint subset probability.

Boundaries q=1, k=0, s=L, k=L-s, and s=0 are correct. When k>L-s, an s-coordinate mean-zero tensor is annihilated, so a universal positive-coefficient inverse theorem would fail. The explicit q=2,L=s=1,k=1 erased-bit example from BS1 is a regression. Odd word length matters only when instantiating M0, not for the alphabet-general identity.

## Finite checker assessment

The script checks q in {1,2,3}, s in {1,2,3}, L in {s,s+1,s+2}, and all k=0,...,L: 108 parameter rows. For invertible rows it checks all point-mass test functions, which span the finite function space, and all source tuples. It expands projections independently by subset sums, then explicitly averages over global k-subsets and replacement symbols to verify T g=f and the norm bound. For excluded k it checks a centered top tensor is killed. The q=1 tensor is zero, so its row is a degenerate boundary check, not evidence of noninvertibility of the singleton function space.

The separate pair checks and complete CP1 calculation serve mandatory regressions. The source projection checker is imported without changing its outputs and exercises S3L4/S4L4/S4L6, odd emptiness and trivial lengths. These are complementary finite checks, not extra premises of LC1.

## Version 1 arithmetic issue

The sentence claiming rational bit growth polynomial in L,s,log q and bounded descriptions of individual f outputs omits the number of distinct rational values. There can be q^s unrelated denominators; a common denominator for their sum may require the sum of those denominator bit lengths. The explicitly allowed q^s evaluation count does not by itself make the old operand-size wording true. I requested that the cost account for the number/total representation of evaluated values. This affects only the computational cost description, not the exact channel identity or its fixed-s use with ordinary polynomial-size data.

Status of v1: **probability identity proved; overbroad arithmetic wording rejected/superseded**. Preserve v1 and the correction record. No claim downstream of an unrestricted small operand-size bound should inherit acceptance.

## Version 2 arithmetic repair

The new bound

    O(q^s b+s^2 log(L+1)+s log(q+1)+s)

bits per operand is justified. At most q^s values of f occur. Their denominator product D has <=q^s b bits, and each coordinate average has denominator dividing D q^s. Writing alpha_j=(L-k)_j/(L)_j and multiplying the at most s numerator denominators contributes O(s^2 log(L+1)) further bits. The affine normalization adds only O(s log(L+1)+s); the norm bounds control numerator magnitudes by the same order. A common-denominator implementation realizes the claimed bound, rather than repeatedly multiplying unrelated unreduced denominators without control. Exact rational Bernoulli rejection has finite expected bit cost and no fixed worst-case finite tape requirement, as stated.

This repair is mathematically satisfactory. A targeted distinct-denominator regression and the fresh r2 review are still coordinator certification gates. My recheck after identifying the issue is not a replacement for that fresh review.

## One remaining corollary clarification

The M0 efficiency corollary must state that f is publicly evaluable in polynomial time with polynomial-bit rational outputs, or is provided as a polynomial-size explicit table. Fixed s, polynomial N,L, and an inverse-polynomial bias do not make an arbitrary rational-valued f efficient or even give the adversary its description. The v2 proof already says fixed-s efficiency holds when q,L,b are polynomial; put the f-evaluation and b hypothesis next to the efficient corollary in the statement. This is a narrow computational-access clarification; the finite probability identity is unchanged.

## Verdict

The exact mathematical survival identity is proved in both versions. V2 repairs the operand bound correctly. **Hold final acceptance of the efficient-corollary wording until the explicit f-computability/bit-size hypothesis is added and the exact repaired version receives the required fresh recheck.** No generic efficient distinguisher follows without a publicly implementable biased f, and no hardness conclusion follows from the transfer lemma.
