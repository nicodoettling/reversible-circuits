# What a logarithmic transposition correction budget changes

Author status: **proved** statements below are self-contained derivations,
provisionally recorded pending independent review. General polynomial mixing
is **unresolved**. The finite checks are falsification attempts, not proofs
of asymptotic bounds. No external literature theorem is used.

## 1. Target, kernel and parameters

Let T_N contain all M=binom(N,2) transpositions, N>=2. Products act
rightmost first. Put ell(g)=N-c(g), counting fixed-point cycles. This is
the minimum number of transpositions needed to correct g to identity.
For even m and even k>=2, our CIRCUIT target pi_m is uniform on

    A(N,m,k) = {w in T_N^m : ell(eval(w))<=k}.

H_k holds with probability 1/2; otherwise it chooses one of the m
coordinates uniformly and replaces that gate uniformly among its legal
values, given all other gates. Old values are included. This is exact
conditional heat bath, hence reversible for pi_m. There is no boundary
window convention to supply: every position has the same selection rule.
The regime of interest is k=Theta(log N), with k=2ceil(log2 N) as one
concrete choice. Polynomial time means polynomial in N,m, not log N wires.

For a word A a B, deleting a and putting h=BA makes the new endpoint
A s B conjugate to s h. Since multiplication by a transposition changes
ell by exactly one, its legal set is all M gates if ell(h)<=k-1.
If ell(h)=k+1, precisely the transpositions splitting a cycle of h are
legal. Their number is

    s(h)=sum over cycles C of binom(|C|,2),
    k+1 <= s(h) <= binom(k+2,2).                         (1)

The inequalities follow by writing each cycle contribution as
binom(d_C+1,2), with d_C=|C|-1 and sum d_C=k+1. Thus a logarithmic
budget still permits conditional sets of size only O(log^2 N).
The uniform-proposal rejection kernel R_k has off-diagonal H_k/R_k=M/s
for a legal fiber of size s. Consequently

    gap(R_k) <= gap(H_k) <= M gap(R_k).                  (2)

This comparison alone does not establish a gap for either chain.

## 2. Hamming contraction fails even with both endpoints on the boundary

For neighboring words x,y differing at coordinate i, let L_j(x) be the
legal gate set at j. The exact optimal one-step Hamming transport cost is

    W_1(H_k(x,.),H_k(y,.))
      = 1 - 1/(2m) + (1/(2m)) sum_{j!=i} TV(U(L_j(x)),U(L_j(y))). (3)

For a lower bound, sum coordinate marginal total variations: the changed
coordinate contributes 1-1/(2m), and each other coordinate contributes its
conditional TV divided by 2m. A coupling that selects the same update
coordinate, then couples its legal values maximally, attains this bound.
The hold events are coupled together. Thus (3) is an optimal-cost identity,
not merely a failure of one particular coupling.

Choose pairwise disjoint transpositions a,b,c,d_1,...,d_{k-1}, possible
when N>=2(k+2). For even r>=2 set m=k+r and

    x=(a,d_1,...,d_{k-1},c,...,c),
    y=(b,d_1,...,d_{k-1},c,...,c),

with r copies of c. Both endpoints have defect exactly k and consist
of k disjoint transpositions. At coordinate i=1 the common legal set is
all T_N. At each d-coordinate both legal sets are all T_N. At each
c-coordinate the respective legal sets are

    {a,d_1,...,d_{k-1},c},  {b,d_1,...,d_{k-1},c}.

They have size k+1 and intersection size k, so their TV is 1/(k+1).
Substitution in (3) gives the **proved exact expansion**

    W_1 = 1 + (m-2k-1)/(2m(k+1)) > 1 if m>2k+1.       (4)

In particular even m=2k+2 works for every sufficiently large N with
k=Theta(log N). This refutes uniform one-step contraction in Hamming
distance, even among neighbors whose endpoints have the same boundary
cycle type. Any fixed positive coordinate weights also fail: place i
at a minimum-weight coordinate, and the r conditional disagreements have
weights at least that minimum; the same threshold proves expansion.

A second family has a stronger expansion but an interior endpoint.
Take disjoint a,b,c,d_1,...,d_{k-2}, N>=2(k+1), and

    x=(a,a,d_1,...,d_{k-2},c^r),
    y=(b,a,d_1,...,d_{k-2},c^r).

Their endpoint defects are k-2 and k. All x conditionals are full.
Only the r c-conditionals differ: y has the k+1 legal gates
{a,b,d_1,...,d_{k-2},c}. Therefore

    W_1 = 1 - 1/(2m) + (m-k)/(2m) * (1-(k+1)/M).       (5)

Already r=2 makes this exceed one when M>2(k+1).
Equations (4)-(5) refute this metric and time horizon, not rapid mixing.

## 3. Exact minimum correction multiplicity

Write Z_j(g) for the number of length-j transposition words with product g,
and a_k(g)=Z_k(g^-1) for the number of k-gate corrections to g.
Reversing words gives Z_k(g)=Z_k(g^-1). Define the parity-compatible ball

    B_k = {g : ell(g)<=k and ell(g)=k mod 2}.

**Proved:** for any integer k>=1 and N>=2k,

    min_{g in B_k} a_k(g) = k!.                         (6)

First, every permutation g of defect d has at least d! reduced
factorizations. For a cycle of length l, fix a root. For each nonroot
vertex v, put t=(v,g^-1(v)). The permutation g t fixes v and is a cycle
on the other l-1 labels. Recursing while keeping the root gives at least
(l-1)! factorizations, with distinct last factors distinguishing choices
when l>=3. The l=2 and l=1 bases are immediate. For disjoint cycles,
interleave these words; the multinomial coefficient cancels the per-cycle
factorials, giving at least d! words supported inside supp(g).

Now d<=k and k-d=2r. Since |supp(g)|<=2d and N>=2k, there are at least
4r unused labels. Partition 4r of them into r groups of four. In each
group select one of two fixed disjoint edges, independently (2^r choices).
Insert two copies of each selected edge into a reduced word for g,
retaining the order of its d original gates. This has
k!/(d! 2^r) interleavings. All inserted edges commute with g's factors
and with one another, and cancel in pairs. The resulting word recovers
the selected fresh edges and the original subsequence, so no overcount
occurs across choices. There are at least k! words of product g.

For equality, let g be a product of k disjoint transpositions. In a
length-k factorization of this defect-k endpoint, each step must merge
cycles, never split them. Merges cannot cross final cycles, since they
could not subsequently be separated. Thus the factors are precisely
the k specified disjoint edges in any order: exactly k! possibilities.
This proves (6). At k=0, B_0={id} and a_0(id)=1 separately.

For even k, adjacent cancellation pairs give

    a_k(id) >= M^(k/2).

Consequently the actual multiplicity ratio obeys

    max a_k / min a_k >= M^(k/2)/k!.                    (7)

For k=Theta(log N), (7) is exp(Theta((log N)^2)); the trivial upper bound
M^k gives the matching order in the exponent. Both the identity and a
k-edge matching are feasible prefix endpoints whenever even m>=k.
Hence this is also the density range between uniform relaxed prefixes
and prefixes weighted by exact k-gate completions. The old global
bounded-density comparison incurs a genuinely superpolynomial factor.
This is an obstruction to that comparison, not a mixing lower bound.

## 4. Positive result: the auxiliary endpoint laws are close

These laws concern PERMUTATIONS, not length-m circuit words. Let U_B
be uniform on B_k and let P_k be the product of k independent uniform
transpositions. Its mass at g is a_k(g)/M^k. From (6), setting

    alpha = k! |B_k| / M^k,

we have 0<alpha<=1 and pointwise P_k>=alpha U_B. Therefore

    TV(P_k,U_B) <= 1-alpha.                            (8)

Let A_j(N) count permutations of defect j. Inserting label N either as
a singleton or into one of N-1 positions in an existing cycle proves

    sum_j A_j(N) z^j = product_{r=1}^{N-1} (1+r z).

Thus k! A_k(N)/M^k is the probability that k independent draws from
{1,...,N-1}, with probabilities p_r=r/M, are all distinct. A union bound
on pairs of equal draws yields

    alpha >= k! A_k(N)/M^k >= 1-Delta,
    Delta = binom(k,2) sum_{r=1}^{N-1} r^2/M^2
          = binom(k,2) * 2(2N-1)/(3N(N-1)).             (9)

Combining (8)-(9), for N>=2k,

    TV(P_k,U_B) <= min(1,Delta) = O(k^2/N).             (10)

In particular this tends to zero for a logarithmic budget, despite the
superpolynomial worst-case multiplicity ratio in (7). The exponent there
and the total-variation conclusion here measure different properties.
This is a constant-accuracy asymptotic endpoint result, not negligible
error for every security parameter and not a circuit-mixing theorem.

There is a useful common subset. Let D_k be the permutations consisting
of k disjoint transpositions. Both P_k and U_B conditional on D_k are
uniform. If k independent transpositions use disjoint labels, their product
lies in D_k. Conversely a length-k word ending in D_k must be such a word.
A union bound over the first overlapping edge gives

    P_k(D_k) = (N)_(2k)/(2^k M^k)
              >= 1-2k(k-1)/(N-1).

Since |B_k|<=M^k/k! by (6), U_B(D_k)>=P_k(D_k) as well.
This observation supplies an endpoint typical set; it does not supply
its mass under an arbitrary length-m circuit law.

## 5. The remaining word-law obstruction and a conditional transfer

Let nu_m be the length-m prefix of a uniformly chosen exact identity
word of length m+k. This is an auxiliary law; obtaining such an exact
word efficiently is itself not assumed. For every w in A(N,m,k),

    pi_m(w) = 1/Z_A,           Z_A=sum_{g in B_k} Z_m(g),
    nu_m(w) = a_k(eval(w))/Z_L,
    Z_L = sum_{g in B_k} Z_m(g) a_k(g).

The endpoint law under pi_m is proportional to Z_m(g), not uniform on
B_k. This is why (10) cannot automatically be applied to circuit words.
Conditioning both circuit laws on endpoint in D_k makes them identical,
since a_k=k! there; neither target's concentration there is established
for arbitrary m by the endpoint-only result.

In fact a near-maximal discrepancy already occurs at m=k, where the
relaxed constraint is vacuous. Under pi_k, the gates are independent, so
pi_k(endpoint in D_k)>=1-2k(k-1)/(N-1). Under nu_k, the number of exact
length-2k identity words with a prefix endpoint in D_k is exactly
|D_k|(k!)^2: each half is a minimal factorization of the same matching.
There are at least |D_k|(2k)!/2^k identity words overall, obtained by
choosing a k-edge matching and ordering two copies of every edge.
Each resulting word determines its matching, so there is no overcount.
Consequently

    nu_k(endpoint in D_k) <= 2^k/binom(2k,k),
    TV(pi_k,nu_k) >= 1 - 2k(k-1)/(N-1) - 2^k/binom(2k,k). (11)

For k=Theta(log N), the right side tends to ONE: the first error is
O(log^2 N/N), and binom(2k,k)>=4^k/(2k+1) makes the second at most
(2k+1)/2^k. Thus (10)'s close ENDPOINT laws can coexist with almost
disjoint CIRCUIT laws. This refutes an approximate-uniform-prefix claim
for the unweighted exact correction lift, even in the easy m=k regime.
It does not refute rapid mixing of H_k; that regime's H_k is a product
heat bath. An inverse-multiplicity correction could change the lifted
target, but would require its own kernel and mixing analysis.

**Conditional static comparison.** Assume even m>=k and explicitly assume
there exist C>0 and 0<=epsilon<1 with

    C(1-epsilon) <= Z_m(g) <= C(1+epsilon)
    for EVERY g in B_k.                                 (FC)

Then Z_A>=C(1-epsilon)|B_k|, while Z_L<=C(1+epsilon)M^k.
Together with (6) this gives nu_m/pi_m >= alpha(1-epsilon)/(1+epsilon),
and hence

    TV(pi_m,nu_m) <= 1-alpha(1-epsilon)/(1+epsilon)
                  <= Delta+2epsilon.                  (12)

No all-length assertion of (FC) is made. For example at m=k the counts
Z_m themselves have the superpolynomial ratio (7), so that regime cannot
have uniformly small epsilon in (FC). A uniform short correction law is
not enough to wash out long-prefix multiplicities.

Even when (12) is small, it is not a spectral comparison. Worst-case
mixing can be sensitive to low-mass states and to transition flows.
No local kernel on the lifted words has been proved rapidly mixing here.

## 6. Dependencies, boundary checks and remaining lemma

Sections 1-5 use only elementary permutation arithmetic, conditional
probability, counting, and the marginal-coupling proof in (3). The earlier
experiment's all-budget connectivity theorem may be used as a separate
qualitative input, but none of the new inequalities needs it. Its fixed-k2
gap comparison is not extended by this report. No claim about the original
{3,4,5} exact bridge kernel follows without its own comparison.

Boundary cases: m=0 gives one empty word. For m>=1 with m<=k the constraint
is vacuous: independent-coordinate half-lazy refresh has gap 1/(2m),
unless the space is a singleton. Thus m=2,k>=2 is trivial. For N=2 the
gate library is a singleton; every feasible space is a singleton. For
odd m, feasible endpoints have odd defect: an even nominal budget must
be rounded down to its largest odd value, and k=0 is infeasible. Our
word witnesses use even m,k; the counting theorem (6) covers either k
parity with its corresponding ball. At even m, k=0 or 1 is the exact
identity constraint and single-coordinate replacement is frozen. Small
N with k beyond the maximum feasible defect also make the constraint
vacuous; the counting result is only claimed when N>=2k. The matching
witnesses are minimal-length endpoint factorizations padded by pairs;
no connected-support hypothesis is imposed.

**First unresolved quantitative step (standalone target).** For a fixed
constant c>0, k=2ceil(c log2 N), and even m>k, establish constants A,B,C
depending only on c such that, for every f on A(N,m,k),

    Var_pi_m(f) <= C N^A m^B E_{H_k}(f,f).              (P)

Here E is the Dirichlet form of the exact kernel in Section 1. Even a
restricted theorem proving (P) in a new growing-N,length regime would
be useful. A possible decomposition would separately bound dynamics within
the matching-endpoint subset, the complementary dynamics, and exchange
between them. None of these bounds is supplied by (10), and no
irreducibility of that restricted subset is assumed. One-step Hamming
contraction and worst-case bounded-density transfer have now been ruled
out as the straightforward routes to (P) for logarithmic budgets.

Stable manuscript insertion: none yet; retain these author derivations
and negative findings for independent review.
