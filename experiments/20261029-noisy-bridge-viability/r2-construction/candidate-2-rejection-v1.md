# C2 rejection v1: sparse planted support remains visible

Status: PROVISIONAL proof; candidate verdict reject on its frozen lambda schedule, pending author-distinct review. Exact M0 noise; no imported mixing, connected-factorization, or sparse-sampler theorem.

## Finite attack statement

Take C2-v1 with m>=2, N>=2m, L=2m, and ANY number s>=0 of the specified adjacent Hurwitz moves. Set h=m+1+2k. Assume h<=N. The support test accepts the structured world exactly when at most h distinct labels occur in the observed gates. It takes O(L) expected dictionary operations and one sample. Because pre-noise support is exactly m+1, and replacing k gates introduces at most 2k new labels, its acceptance probability under C2 is 1, pointwise for every tape.

Write

    D(N,m) = (N)_(2m) (2m)! / (4^m m!).

The same test on Q_k(U(N,2m)) has acceptance probability at most

    R(N,m,k) = min(1, binom(N,h) binom(h,2)^(2m) / D(N,m)).        (C2.1)

Thus distinguishing advantage is at least 1-R. If h>N, use the trivial bound R=1 and do not claim a separating test. Reused setup is already broken by one sample; there is no hidden key and no average-key/every-key distinction.

## Proof of the reference bound

There are D(N,m) literal ordered identity words consisting of m distinct pairwise disjoint edges, each appearing twice. Choose their 2m labels, then their perfect matching, then a permutation of the multiset containing two copies of each edge. These choices are uniquely recoverable from the final word. Their number is

    binom(N,2m) * (2m)!/(2^m m!) * (2m)!/2^m = D(N,m).

They all evaluate to identity because disjoint transpositions commute. Therefore the total global bridge count T(N,2m) is at least D(N,m). This is only a counting lower bound, not an assertion that all bridge words have this form or that an adjacent-pair control is a candidate.

Let V be an iid mu word and F its identity endpoint event. For any event E on the noisy full word,

    Pr[Q_k(U) in E] = Pr[Q_k(V) in E and F]/Pr[F]
                    <= Pr[Q_k(V) in E]/Pr[F].

The exact uniform-k-subset replacement channel preserves the iid mu product law. With E={support<=h}, at most binom(N,h) binom(h,2)^(2m) literal length-2m words satisfy E, by a union bound over containing h-label sets. Since Pr[F]=T/q^(2m), the q factors cancel and (C2.1) follows. This does not condition on a random set chosen after seeing the candidate; all possible h-label sets are charged by the union bound. No sequential probabilities are multiplied under bridge conditioning.

## Polynomial schedule and quantitative decay

For lambda>=9, set m=lambda, N=lambda^6, k=floor(sqrt(lambda)), h=lambda+1+2 floor(sqrt(lambda)). Then h<=2lambda<=N. Using binom(N,h)<=N^h, binom(h,2)<=h^2/2, (N)_(2m)>=(N-2m)^(2m), and m!/(2m)!<=m^(-m),

    R <= N^(h-2m) (1-2m/N)^(-2m) h^(4m) m^(-m).

Since h<=2m and N=m^6,

    log R <= (-3m+6+12sqrt(m)) log m + 4m log 2
             -2m log(1-2/m^5).

The right side is -Omega(m log m). In particular it is at most -m log m for all sufficiently large m; no claim is made that the crude bound is nontrivial already at lambda=9. Therefore R is negligible in lambda and this polynomial-time one-sample attack has advantage 1-exp(-Omega(lambda log lambda)). A more conservative fully explicit onset is m>=1024: then 6+12sqrt(m)<=m/2, 4log2<=log(m)/2, and -2m log(1-2/m^5)<=1, giving log R<=-2m log m+1<=-m log m.

## Checks and exclusions

The threshold is independent of hidden noise positions and secret tapes. At k=0 it detects planted support directly; at k=1 it remains valid if h<=N. At k=L the threshold exceeds the interesting support range and the result correctly becomes vacuous; both worlds are iid. N=2 and L=0 are outside C2 and retain their singleton/empty laws. Odd identity length remains infeasible. The lower-count D requires N>=2m; it is not used in the mandatory S3,L4 or S4,L6 small implementation checks, where that hypothesis fails.

The first unproved issue is not a hidden lemma in (C2.1), but external review and exact implementation verification. The construction supplies no surviving security candidate. Its failure does NOT establish impossibility of noise hiding arbitrary structured identity samplers, nor a general bridge-sampling hardness theorem. A next construction would need support statistics consistent with the global reference as well as long-range relation structure; no third candidate is started in this role.
