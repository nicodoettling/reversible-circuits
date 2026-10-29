# Full proof for frozen statement T0

Authored version T0, 2026-10-29. Author status: PROVISIONAL, pending exact-version adversarial review and finite regressions. This full file is immutable. The authoritative statement is statement-T0.md. No literature theorem is imported. A source claim used below is reproved from finite counting.

## Probability space and notation

Fix N>=2, q=binom(N,2), the finite group G=S_N, and mu uniform on all transpositions. The word product acts rightmost first. For independent mu gates X_1,...,X_s, let p_s(g)=Pr[X_1...X_s=g] and c_s(g)=q^s p_s(g). Write p_s=p_s(id), c_s=c_s(id) when the endpoint is omitted. For even L, p_L>0 because doubled transpositions give identity words. The global bridge U(N,L) is the iid gate law conditioned on product=id; every ordered literal identity word therefore has probability 1/c_L. This statement is not a claim about connected bridges.

The Q_k tape is independent of the entire original word and setup. Its position set I is uniform among k-subsets of [L], and selected replacements are independent mu. The word, I and replacements together form the original sample space. All local probability arguments condition only on a fixed I, then average over I. No local identity events are asserted independent.

## D1: even-time maximum and return moments

Let P be the transition matrix on G with P(x,y)=mu(x^{-1}y). Since every transposition is its own inverse, P is a real symmetric stochastic matrix. In the standard Euclidean inner product, the spectral theorem gives real eigenvalues theta_j in [-1,1]. Its diagonal entries are translation invariant, so

    p_(2s) = (1/|G|) trace(P^(2s))
           = (1/|G|) sum_j (theta_j^2)^s.

This applies at s=0 with 0^0 interpreted as 1 for the trace formula. The sequence a_s=p_(2s) is positive for s>=0 and log convex:

    a_s^2 <= a_(s-1) a_(s+1),  s>=1,

by Cauchy–Schwarz on the finite nonnegative moment sum. Therefore b_s=a_(s+1)/a_s is nondecreasing for s>=0. If d>=1 and n>=2d,

    a_(n-d)/a_n = product_(j=n-d)^(n-1) b_j^(-1)
                 <= product_(j=d)^(2d-1) b_j^(-1)
                 = a_d/a_(2d).

Set r=2d and L=2n. For even L>=2r,

    p_(L-r)/p_L <= p_r/p_(2r).                         (D1.1)

Also, by symmetry p_s(g)=p_s(g^{-1}), and convolution followed by Cauchy–Schwarz gives for every g

    p_(2s)(g) = sum_x p_s(x) p_s(x^{-1}g)
               <= sum_x p_s(x)^2 = p_(2s)(id).         (D1.2)

The equality of the two squared norms follows because x -> x^{-1}g is a bijection. This even-time maximum is not asserted at odd times. In particular, parity is preserved throughout the proof.

## D2: bridge window density, then replacement domination

Fix a nonwrapping consecutive window of length r. Cyclic rotation is a bijection on global identity words: if a word is uv with product uv=id, then vu=id. It preserves literal ordered uniformity. Thus its r-window has the first-r tuple law. For a fixed tuple a=(a_1,...,a_r) with product h,

    nu(a) = q^(-r) p_(L-r)(h^{-1})/p_L.               (D2.1)

Indeed there are c_(L-r)(h^{-1}) completions, out of c_L full identity words. The iid tuple law rho=mu^tensor r assigns every a the mass q^(-r). For even r and even L>=2r, D1 yields the pointwise finite measure inequality

    nu <= R rho,  R=p_r/p_(2r).                        (D2.2)

For any fixed intersection J=I intersect window, let K_J be the channel replacing precisely the coordinates in J by fresh independent mu, with the other coordinates retained. It preserves rho exactly, since rho already has iid mu coordinates. Applying the positive Markov kernel to (D2.2),

    nu K_J <= R rho K_J = R rho.                       (D2.3)

This argument includes J empty and J the full window. The original word law conditional on I is still U, because I was sampled independently. Replacements outside the window have no effect on its literal gates. Averaging D2.3 over the hypergeometric law of J proves the same domination for the noisy window. Under rho, the event that its product is identity has probability p_r; hence

    Pr_Qk(U)[window product=id] <= R p_r
                                = p_r^2/p_(2r).       (D2.4)

No information about hidden I is used by the test. There is no approximation, no conditioning on a window surviving, no independence claim for different windows, and no product of marginal bounds. The exact cardinality-k noise is used throughout, although this upper bound in fact holds for any word-independent random subset.

## D3: elementary length-six return count

Count length-three factorizations of each possible odd endpoint. An endpoint reached in three transpositions has transposition distance at most three and odd sign. Its nontrivial cycle type is therefore exactly one of 2, 4, 3+2, or 2+2+2. This can also be seen by multiplying from identity: each transposition changes the number of permutation cycles by one, so distance equals N minus the number of cycles.

Length-two products have exactly q factorizations for identity, three for a specified 3-cycle, and two for a specified pair of disjoint transpositions. There are no other length-two endpoints. These counts follow by listing the last transposition: for a 3-cycle its three transpositions each leave a transposition; for disjoint transpositions either of the two may be last.

For a fixed transposition t, append the last transposition c. If c=t, the first two factors multiply to identity, giving q choices. There are 2(N-2) last c sharing one label with t, each leaving a 3-cycle, giving 6(N-2) choices. There are binom(N-2,2) disjoint last c, each leaving two disjoint transpositions, giving 2 binom(N-2,2) choices. Thus

    A_N = c_3(t) = q+6(N-2)+2 binom(N-2,2)
                = (3N^2+N-12)/2.

For a specified 4-cycle, a last transposition splitting adjacent positions in its cycle has four choices and leaves a 3-cycle (three factorizations each). A last transposition joining opposite positions has two choices and leaves two disjoint transpositions (two each). Hence c_3=4*3+2*2=16.

For a specified disjoint 3-cycle and transposition, the last transposition can be one of the three splitting the 3-cycle, leaving two transpositions (two factorizations), or the sole transposition component, leaving the 3-cycle (three factorizations). Hence c_3=3*2+1*3=9.

For three disjoint transpositions, the last gate can be any of those three and leaves two disjoint transpositions. Hence c_3=3*2=6. A transposition merging distinct cycles cannot occur in these minimal-length factorizations, because it would increase the remaining distance to four.

There are q transpositions, 6 binom(N,4) specified 4-cycles, 20 binom(N,5) specified 3+2 endpoints, and 15 binom(N,6) specified triples of disjoint transpositions. Since reversing a word inverts its product, c_3(g)=c_3(g^{-1}). Concatenating two triples therefore gives

    c_6 = sum_g c_3(g)c_3(g^{-1})
        = q A_N^2 +1536 binom(N,4)
          +1620 binom(N,5)+540 binom(N,6).             (D3.1)

The formula uses binom(N,j)=0 for j>N and holds for all N>=2. In particular it gives c_6=1,243,3936 for N=2,3,4. The N=3,L=4 and N=4,L=4 bridge counts 27 and 120 are separate regression inputs, not c_6 values.

For c_12, retain only words made from six distinct vertex-disjoint transpositions, each appearing exactly twice. Such transpositions commute and square to identity, so every such word evaluates to identity. There are 11!!=10395 partitions of the twelve positions into six unordered position pairs. Order the pairs canonically by their smaller positions. Assign an ordered list of six vertex-disjoint unordered edges to these pairs: (N)_12/2^6 choices, where (N)_12=N(N-1)...(N-11). The resulting literal word determines its unique equal-edge pair partition and all assigned edges, so there is no overcounting. Therefore for N>=12,

    c_12 >= (10395/64) (N)_12.                         (D3.2)

The omitted return words make this a lower bound, not an exact c_12 formula.

## D4: explicit numerical constant

Use q<=N^2/2, A_N<=(3N^2+N)/2 and binom(N,j)<=N^j/j! in D3.1. This gives

    c_6 <= (15/8)N^6+(57/4)N^5+(513/8)N^4.

For N>=1000, dividing by N^6 gives at most

    15/8 +57/4000 +513/8000000 <19/10.

For numbers x_j in [0,1], product_j(1-x_j)>=1-sum_j x_j, by induction; this is a deterministic algebraic inequality, not independence. Consequently

    (N)_12/N^12 >=1-(0+1+...+11)/N
                =1-66/N >=467/500.

Since q^12 cancels between p_6^2 and p_12,

    beta_N = c_6^2/c_12
      <= (19/10)^2 / ((10395/64)*(467/500)) <1/40.

The final comparison is the integer/rational inequality

    40*(19/10)^2 =722/5
       < 4854465/32000 = (10395/64)*(467/500).

All inequalities have explicit finite onset N>=1000; no asymptotic counting approximation is used.

## D5: deterministic surviving-window count

The original concatenation has M pairwise disjoint contiguous length-six intervals, each with product identity. Simultaneous label conjugation preserves every such product. After a cyclic rotation, at most one of these intervals wraps the new cut. Discard it. At least M-1 disjoint nonwrapping six-position witness intervals remain. Their index sets are retained in the proof; the adversary need not know them.

A single adjacent Hurwitz move changes only its two positions. Therefore at most two of the retained disjoint witness intervals intersect those positions. All other retained witnesses have exactly the same gates and remain identity. Removing every witness touched by any of at most B moves discards at most 2B witnesses. This upper bound remains valid for adaptive moves and arbitrary correlations. In fact moves wholly inside a witness preserve that witness too, but this improvement is not needed.

Now fix any noise position set I of size k and any replacement values. Each selected position lies in at most one of the disjoint remaining intervals. Discard at most k further witnesses. Every remaining interval was unchanged by scrambling and noise, so at least

    H=M-1-2B-k

nonwrapping identity six-windows occur in the observed word. If H>0, the scan test always accepts. This is pointwise, not merely a high-probability survival statement. Replacement equal to the old gate can only improve survival relative to this lower bound.

Hurwitz moves preserve the total product because b(bab)=ab and (aba)a=ab for involutory a,b. Cyclic rotation and conjugation preserve total identity. Thus every candidate output is an exact pre-noise identity word as required by M0.

## D6: matched reference, advantage and quantifiers

Let X be the number of nonwrapping identity six-windows in the observed reference word. There are L-5 windows. D2 gives each marginal probability at most beta_N; linearity of expectation, which does not require independence, yields

    E[X] <= (L-5) beta_N.

For H>0, the pointwise inequality 1[X>=H]<=X/H proves

    Pr[X>=H] <= min(1,(L-5) beta_N/H).

The structured acceptance is exactly one by D5. Hence the difference of acceptance probabilities, which is the specified distinguishing advantage, is at least one minus this upper bound. For N>=1000 and H>=M/2,

    Pr_reference[accept] <= (6M-5)/(M/2) * beta_N
                          <12/40=3/10.

Thus advantage is at least 7/10. The structured proof is valid separately for every word, setup and key. The reference is independent global U with the same exposed public setup. Therefore the result is every-key and also holds after averaging setup. It is statistical and computationally achieved by a deterministic polynomial-time test, not a hardness reduction.

For t requests, define the fixed test that accepts iff every reply separately passes. Conditional on any fixed exposed setup, the reference replies are independent with fresh word/noise tapes; their individual acceptance probability is the same number p<=3/10. Thus the joint reference acceptance equals p^t<= (3/10)^t. This uses the actual conditional product law, not marginal estimates under adaptive conditioning. Structured acceptance is pointwise one on every reply. An adversary needs only one request for constant advantage; amplification is optional.

## D7: explicit schedule and cost

Let lambda>=32 be an integer, N=lambda^2, M=N, L=6N, k=lambda and B=floor(N/8). Then N>=1024. Since 2B<=N/4,

    H>=3N/4-lambda-1 >=N/2,

because lambda^2/4-lambda-1>=0 for lambda>=32. Candidate generation, if one samples fresh relator blocks and performs B local moves, uses polynomially many operations; uniform bounded choices can be generated exactly by rejection from independent unbiased random bits with expected polynomial cost. The theorem itself does not make a generation claim for every arbitrary source in its class.

For the literal scan, a window has six transpositions on at most twelve labels. Collect those labels, apply the six transpositions in the rightmost-first convention, and test if all collected labels return. Labels outside this set are automatically fixed. At most a fixed number of comparisons and updates are needed per window. The test is O(L) operations on O(log N)-bit labels, or O(L log N) bit operations with direct binary comparisons. A streaming implementation stores six gates and a counter, using O(log N+log L) auxiliary bits.

The common semantic error bound is 4k/N=4/lambda. This tends to zero but is inverse polynomial, not negligible. The noise attack does not imply better correctness. Runtime is polynomial in lambda, N and L and is not claimed polynomial in the wire count log2 N.

## Boundaries, failed routes and exact exclusions

* N=2: one transposition exists, so every length-even word, structured or reference and before or after any replacement, is identical. beta_N=1 and the finite upper bound is vacuous; the N>=1000 corollary does not apply.
* Odd L: there are no identity words because sign is (-1)^L. M0 excludes this case.
* L=0: only the empty word with k=0 exists; it contains no windows and has no distinguishing advantage.
* L=2: all exact identity words are doubled transpositions; the theorem's length-six construction hypothesis fails.
* L=6: the local bridge bound needs L>=12 for r=6. Indeed at k=0 the sole full-length window is always identity under global U, so a general r-window upper bound below one would be false here. T0 explicitly excludes it.
* k=0 and k=1 are covered when H>0; no noise-survival approximation is used.
* k=L: both Q_L worlds are exactly iid mu^tensor L, so advantage is zero. H<=0, so the attack theorem gives no contradiction and its nontrivial condition fails.
* H<=0: the particular threshold is not used as an attack; T0 makes no advantage claim.
* Large B, nonlocal rewriting, hidden shuffling not realizable within the stated adjacent-move budget, or variable/long relator lengths may invalidate the witness count. Failure to prove leakage in those regimes is unresolved, not evidence of security.
* An earlier loose approach would have imported or reproved dense pointwise mixing at polynomially large L. It is unnecessary after D1. No such mixing theorem is a dependency.
* A naive union bound on the existence of any identity window is poor for large L. The test instead compares their count to a linear deterministic witness budget. It uses only first moments; false independence of overlapping windows is expressly excluded.
* Pair-equality attenuation alone is not this theorem. It applies to six-distinct-gate relators, whose within-block equal-gate count is zero, and uses their ordered product relation. Other pair statistics may still reject the same candidate; no exclusivity is claimed.

## Claim graph and certification gap

D1 -> D2; D3 -> D4; D2,D4,D5 -> D6; D6 -> schedule/application D7. All seven are author-proved candidates in this file but remain PROVISIONAL until the coordinator's exact-version audit gates close. The first remaining obligation is external to the written mathematics: author-distinct review plus finite regressions of D1–D6 and the frozen candidate's membership in the structural class. The theorem says that this class is attacked; it does not refute the main possibility of sparse-noise hiding for a different structured identity sampler.
