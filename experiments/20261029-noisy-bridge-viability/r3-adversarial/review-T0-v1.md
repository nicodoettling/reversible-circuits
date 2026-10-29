# Exact-version referee report: T0

Reviewer: r3-adversarial. Date 2026-10-29. This report follows frozen blind reconstruction B1/BS1/BS2/BS3. No proposed T0 proof or claimed status was read before BS2. Same-model reviewers are correlated; neither agreement nor this report alone closes coordinator certification.

## Frozen inputs and hashes

All paths below are relative to `experiments/20261029-noisy-bridge-viability/`.

| Artifact | SHA256 |
|---|---|
| r1-theory/statement-T0.md | 6ce9be16da02a1e1ce85fe464035f2e8b3f985188fc9f585276eb357fdb5927b |
| r1-theory/proof-T0.md | 447ad895ad2eede2a5d428d657c79a6bc319f21b960663a9a22d3d948b242ed7 |
| r1-theory/check-T0-v1.py | 99e21554ece37b4824964bd6720a820e6d8cbd6cdf77cefcf7b3bde973a3df1c |
| r1-theory/results-T0-v1.json | 7354c9d9c0f96997b61ec468f8a545f7f057425f6044031914d7ed3002cd015e |

The complete proof, script and result JSON were read. The script SHA recorded in results matches the inspected script. Results record Python 3.12.3, standard library, no random sampling, commit `24649e0a2b4fa0d0ede444234bfedfc428453571`, and the exact command. I did not execute an additional mathematical job; coordinator owns the bounded-job record and decisive rerun requirement.

## Claim-by-claim assessment

| Claim | Assessment | Reason and limitations |
|---|---|---|
| D1 even return moments and maximum | proved in the finite symmetric walk model | The symmetric matrix spectral theorem yields a nonnegative moment sequence for squared eigenvalues. Log convexity has the stated direction, and the ratio indices n>=2d compare correctly. Cauchy-Schwarz gives the even-time maximum. No odd-time maximum or parity-free mixing is used. |
| D2 noisy local domination | proved | Consecutive-window cyclic rotation preserves global literal bridge uniformity. Completion density is exact. Applying any fixed-coordinate replacement kernel preserves the iid law and the pointwise measure bound. Independence of the whole replacement tape from the source justifies averaging the same inequality over hidden subsets. |
| D3 exact c6 and c12 lower count | proved | The four odd endpoint types at distance <=3 exhaust three-step outputs. Last-gate counts  A_N,16,9,6 and class sizes q,6 C(N,4),20 C(N,5),15 C(N,6) are correct. Squaring those counts gives c6. The c12 disjoint-edge family has a unique pair partition, so there is no overcount. |
| D4 beta_N<1/40 for N>=1000 | proved | Expanding the displayed upper bounds gives coefficients 15/8,57/4,513/8. The explicit rational inequalities and product lower bound have the correct directions and constants. This requires no imported mixing theorem. |
| D5 surviving witnesses | proved pointwise | A rotation loses at most one disjoint interval. Each adjacent move intersects at most two fixed witnesses and each noise coordinate at most one. Discarding all touched witnesses is conservative and survives adaptive move choices. |
| D6 advantage and reused-setup amplification | proved in M0 | Markov uses only a first moment. Structured acceptance is every-word/every-key one. Reference replies really are independent conditional on the public setup, so the product amplification is justified by their actual joint law. |
| D7 schedule and cost | proved in stated parameterization | lambda>=32 implies N>=1000 and H>=M/2. Six gates touch at most twelve labels, yielding the claimed scan complexity. Polynomiality is explicitly in lambda,N,L, and semantic error remains inverse polynomial. |

The proof's direct three-step endpoint count improves on my blind BS2 derivation: BS2 used the small F6(4) count to derive its polynomial, whereas D3 reconstructs all coefficients directly. Thus that finite count is a regression, not a load-bearing imported premise of the authored proof.

## Probability audit

The random variables are the original global bridge W, independent uniform subset I, and iid independent replacement gates. D2 conditions on I before applying a source-independent positive kernel. No posterior restriction of W occurs. The proof does not multiply untouched-window marginals; its count bound is pointwise and its reference estimate is linearity plus Markov. The only product of probabilities is across independent fresh reference replies conditional on public setup, where the conditional joint law is explicitly a product. This is not the invalid cached-prefix mechanism.

The checker explicitly reproduces CP1's 21/2000>1/100 and 21/221<1/10, rejecting the false marginal-product inference. It does not reimplement every original CP1 posterior mass, so the complete reference's finite model remains the explanatory source. T0's replacement argument avoids that inference on structural grounds.

## Finite falsification evidence and its scope

The inspected checker uses permutation tables with right multiplication by a transposition implemented by swapping the permutation's two entries, consistent with rightmost-first products. It checks return counts and c3 endpoint types for N=2,...,7 through length 24; even-time maxima and log-convex/ratio inequalities; eight local-window cases including literal full-word checks at S3L4/S4L4/S4L6; all local replacement masks and all global k in those cases; 6300 bounded rotated/Hurwitz/replacement survival cases; rational constants and several schedule values. It also asserts that S3,L=r=6,k=0 refutes a version lacking the L>=2r hypothesis.

For the local noisy-window tests, the script uses an exact marginal array built from completion counts. The smaller literal enumeration checks that array against all global bridge words. The replacement-mask transform sums old values then replicates to new values, with denominator q per replacement, and the hypergeometric weights count exactly the choices outside the window. This matches M0, including replacements equal to old values. It does not enumerate length-12 literal words; its exact finite-state/count argument suffices for those marginals.

Limitations: the survival search uses selected shifts and noise positions and one repeated relator template, not every adaptive construction. It is falsification evidence; the pointwise proof handles the general class. Finite N data do not establish an asymptotic statement; D1-D7 independently prove the universal result.

## Boundaries and attempted failures

I checked N=2, odd L, L=0,2,6, k=0,1,L, H<=0, and the threshold equality H=M/2. The theorem is vacuous or explicitly excluded exactly where the matched worlds coincide or the local-window bound would fail. In particular the full r=L window is always identity at k=0, so retaining L>=2r is necessary for the given universal constant; this counterexample is preserved in both BS2 and the checker. At k=L the structured witness threshold cannot be positive and both noisy laws are iid, preventing a false positive advantage claim.

Adaptive conjugation, rotation and move choices do not defeat D5 because the argument freezes the actual resulting witness intervals for each realized construction. An adversary does not need to recover those intervals. Nonlocal compilers and unbounded scrambling may destroy the budget, and remain outside the theorem. No global sampler hardness is claimed.

## Verdict

**Recommend acceptance of exact statement T0 as proved in its stated finite model**, after the coordinator confirms the current bounded-run provenance and performs its required smallest decisive recheck. No mathematical repair is requested for these hashed versions. This is a scoped referee recommendation, not independent cryptographic certification or acceptance of a generic sparse-noise impossibility. The candidate application must use each candidate's actual published parameters rather than silently replacing them with T0's example schedule.
