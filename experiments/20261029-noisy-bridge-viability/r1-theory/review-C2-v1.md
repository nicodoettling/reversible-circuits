# C2 exact-version review v1

Reviewer: /root/r1_theory. Author: /root/r2_construction. This is a nonblind, author-distinct review with the same model and shared campaign lineage; it is not statistically independent or human certification. The exact inputs and complete coordinator task are recorded in review-C2-inputs-v1.json. The reviewed mathematical versions are candidate-2-v1.md and candidate-2-rejection-v1.md, as hashed there.

## Verdict and scope

**KEEP the authored finite support attack and its explicit asymptotic schedule as mathematically supported by this review.** No mathematical counterexample or missing hypothesis was found in those statements. Candidate C2 is rejected on the stated schedule. Final campaign proof acceptance still requires the coordinator's other review and exact implementation/regression gates. This report does not certify a general hardness or impossibility statement. No independent mathematical computation was launched for this review; the checks below are analytic. The construction code was inspected, not executed here.

## A1: exact identity and support invariant

For distinct a_1,...,a_(m+1), rightmost-first path multiplication (a_1 a_2)...(a_m a_(m+1)) sends a_i to a_(i+1) for i<=m and a_(m+1) to a_1. Thus it is c=(a_1 ... a_(m+1)). The ascending-star product sends a_1 to a_(m+1) and a_i to a_(i-1) for i>=2, hence is c^{-1}. Their concatenation is identity at literal length 2m.

At m=2, the base word is (a_1 a_2),(a_2 a_3),(a_1 a_2),(a_1 a_3); evaluating its action on the three labels gives identity. This minimum allowed instance confirms the convention and shows the base is not a literal mirrored inverse word. Only (a_1 a_2) repeats, as claimed.

The path contains every planted vertex. Under (u,v)->(v,vuv), the new gates lie in <u,v>, while u=v(vuv)v lies in the new generated subgroup. The inverse move has the same equality of generated subgroups. The support of a transposition-generated subgroup is exactly the union of labels in its gates: a label absent from every gate is fixed by the whole subgroup, while a label occurring in a gate is moved by that subgroup element. Therefore the full planted support remains exactly m+1 after any finite number s of moves, even adaptively selected moves. The frozen random-tape sampler is a special case.

A k-replacement channel changes only k gates, each adding at most two labels. It may remove old labels or redraw old edges, but this cannot violate the upper bound m+1+2k. Candidate test acceptance is pointwise one. No survival-independence assumption is present.

## A2: the literal global-bridge lower count

Choose 2m labels, match them into m unordered disjoint edges, then order a multiset with two copies of each edge. These choices are uniquely recoverable from the literal word because all m edges are distinct. The count is

    binom(N,2m) * (2m)!/(2^m m!) * (2m)!/2^m
    = (N)_(2m) (2m)!/(4^m m!).

The inverse factorials do not quotient away ordered-word multiplicity: the first matching factor removes edge orientations and edge-list order, whereas the final division removes only the indistinguishability of the two copies of each fixed edge. All retained words evaluate to identity because their gates commute and square to identity. N>=2m is required and stated. This is a valid lower bound on the GLOBAL bridge count, with no connected-law substitution.

The checker-v1-rejection.md correctly preserves a separate computational failure: factorial(N)/factorial(N-2m) is a poor way to implement the falling product at N=lambda^6. That resource-planning rejection does not invalidate the count; a 2m-factor product is exact. I did not run the superseded checker.

## A3: change of measure and exact noise

Let V be a length-2m iid uniform transposition word, F={product(V)=id}, and use a noise tape independent of V. Conditioning V on F gives the global literal bridge. For any observable event E,

    Pr[Q_k(U) in E] = Pr[E(Q_k(V)) and F]/Pr[F]
                    <= Pr[E(Q_k(V))]/Pr[F].

The exact hidden uniform-k-subset replacement preserves the iid gate product law. This follows by conditioning on its chosen subset: all retained original gates and fresh replacement gates are still independent mu, with the same product law for every subset. Thus no Bernoulli-noise substitution is used.

For support<=h, union over every h-label set S. The event that all 2m gates lie inside one fixed S has exactly binom(h,2)^(2m) literal words. The union bound may overcount words whose support is smaller than h, which only enlarges the numerator. It is valid for the fixed integer h<=N. Cancelling q^(2m) from the iid probability and Pr[F] produces exactly (C2.1). The denominator replacement by D enlarges the upper bound. All normalizations and inequalities have the correct direction.

This proof is insensitive to the CP-1 cached-prefix regression because it multiplies no conditional stage probabilities and exposes no latent cache/selected support branch. In particular, the containing support set is union-bounded over all possible S, rather than chosen for free after observing the word.

## A4: schedule and explicit negligible bound

Write m=lambda>=9, N=m^6, k=floor(sqrt(m)), h=m+1+2k. The claimed h<=2m is valid: at m>=9, 1+2sqrt(m)<=m. Also N>=2m. Starting with the raw untruncated union bound, use

    binom(N,h)<=N^h,
    binom(h,2)^(2m)<=h^(4m)/4^m,
    (N)_(2m)>=(N-2m)^(2m),
    m!/(2m)! <= m^(-m).

The factors 4^m cancel, yielding the displayed finite upper bound. With h<=m+1+2sqrt(m) and h<=2m, its logarithm is bounded by

    (-3m+6+12sqrt(m)) log m +4m log2
      -2m log(1-2/m^5).

At m>=1024, 6/m+12/sqrt(m)<=6/1024+12/32<1/2, proving the first numeric inequality. The second follows from m>=256. For the third, x=2/m^5<=1/2 and -log(1-x)<=2x imply -2m log(1-2/m^5)<=8/m^4<=1. Therefore the exponent is at most -2m log m+1<=-m log m. This establishes the explicit bound R<=m^(-m) at m>=1024. It is negligible in lambda, hence the attack advantage is at least 1-lambda^(-lambda) there. The statement only promises asymptotic decay, with a conservative onset; no unsupported assertion at lambda=9 is made.

## A5: security quantifiers, complexity and boundaries

The candidate has no secret key; public A consists of the parameters, identical in both worlds. All sampling/noise tapes are fresh per request. The one-sample attack is already sufficient, so no repetition or reused-setup independence amplification is required. Statistical rejection by this explicit efficient statistic refutes computational indistinguishability for this candidate schedule without importing an assumption.

The support counter needs only O(L) dictionary operations on O(log N)-bit labels and O(min(N,L)) labels of storage. A deterministic sorting variant gives O(L log L) label comparisons if one wishes to avoid expected dictionary-time assumptions. Both are polynomial in lambda on the frozen schedule. The output word has L=2lambda gates, while generating s=L^3 moves is also polynomial. Materializing all N=lambda^6 labels would remain polynomial, though the inspected candidates_v1.py actually calls rng.sample(range(n),m+1), so the prose's phrase that it materializes [N] is stronger than what this code necessarily does; the conservative O(N+L+s) upper bound remains safe. This is a documentary precision issue, not a theorem or security failure.

The exact mathematical law uses ideal independent uniform draws; the implementation explicitly labels random.Random as a finite-test tape, not a cryptographic RNG. Its transposition replacement routine samples an ordered distinct endpoint pair and canonicalizes it; each unordered edge has exactly two preimages, hence is uniform. Its subset sampler is uniform without replacement. Its evaluate function swaps p[a],p[b], which is right multiplication of the current permutation by the transposition, matching the frozen rightmost-first product convention.

At k=0 and k=1 the same finite bound applies. At k=L=2m, h=5m+1 exceeds the maximum possible support 4m of any length-2m word, so the event is universal. If h<=N, the untruncated count numerator is then at least the total number q^(2m) of iid words, hence at least D, forcing R=1; if h>N, the statement already uses R=1. Thus this boundary cannot falsely distinguish the two identical iid noisy worlds. N=2,L=0,L=2 and odd L are explicitly outside the C2 construction or impossible as stated. S3,L4 and S4,L6 do not satisfy N>=2m, so their implementation checks must not be presented as checks of the asymptotic counting hypothesis.

## Failed assertions searched and retained

No counterexample to the reviewed theorem was found. The following tempting strengthenings are invalid or unsupported and are excluded: equality of the noisy support with m+1+2k; any support advantage at k=L; using D when N<2m; using a connected bridge reference; treating correct entropy or arbitrary Hurwitz scrambling as global-uniformity evidence; and upgrading this candidate rejection to an impossibility theorem for all noise-hiding samplers.

The limited scope of this review is exact authored statements, elementary proof, parameter arithmetic, and inspected code conventions. Coordinator-owned bounded tests and the second referee remain separate evidence. The highest-value remaining check is literal-word implementation validation and finite exact comparison under the matched noise law, not a new asymptotic lemma.
