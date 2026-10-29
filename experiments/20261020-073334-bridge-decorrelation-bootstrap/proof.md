# A static assumption that bootstraps local mixing

Status: the implications below are **proved conditional results** by the
author, pending independent review. The proposed uniform decorrelation
hypothesis is **conjectured/unresolved**. Finite checks do not prove it.
General polynomial mixing of the original walk remains unresolved.

## 1. Model and a meaningful new hypothesis

Let T_N be all transpositions in S_N, N>=3, M=binom(N,2). Products act
rightmost first. On every nonempty

    Omega_g(N,m)={w in T_N^m: product(w)=g},

let pi_(N,m,g) be uniform. Feasibility requires m>=N-cycles(g) and
sign(g)=(-1)^m. The local walk is

    K_A=I/2+H/4+R/4.

H chooses a uniform linear adjacent slot and a uniform signed Hurwitz move;
R chooses a uniform slot and replaces an equal pair (t,t) by uniform (s,s),
holding on an unequal pair. There is no wraparound. Its conditional
restriction to a window is the same kernel at that window's length and
product. No exact long-block oracle is added to the actual walk.

For m>=4 put a=floor(m/3), b=m-2a and split W=A B C into lengths a,b,a.
All laws in the following hypothesis are under pi_(N,m,g), with g fixed.
Define maximal correlation

    rho_(N,m,g) = sup |Cov(F(A),G(C))|
                        /sqrt(Var(F(A)) Var(G(C))),               (1)

where the supremum is over functions with positive variances; use zero
if either tail is deterministic. This is a property of the target measure,
not of an initialization law or of an MCMC trajectory.

**Balanced bridge decorrelation hypothesis H_delta (conjectured).** There
exists a UNIVERSAL constant delta>0 such that for every N,m>=4 and every
feasible g,

    rho_(N,m,g) <= 1-delta.                                       (2)

Interpretation: after conditioning on the total permutation, no observable
of the first third can be almost perfectly recovered from the last third.
The middle third absorbs a fixed proportion of this dependence. Individual
gates need not be independent, and rho need not be small or tend to zero.
The assertion is uniform over endpoints because subinterval conditionals
produce arbitrary endpoints during recursion.

This differs substantially from short-window endpoint blindness. That is a
statement about marginal laws across endpoints. Here the endpoint is fixed,
and ALL observables of two separated pieces have their conditional
correlation controlled. It is a stronger stationary-law hypothesis with an
explicit, falsifiable matrix formulation below.

## 2. A count-matrix test, independent of the local dynamics

Write Z_j(h)=|Omega_h(N,j)|. Put U=product(A), V=product(C). Their exact
joint-count matrix is

    J_(u,v)=Z_a(u) Z_b(u^(-1) g v^(-1)) Z_a(v).                   (3)

Its entries sum to Z_m(g). Its row and column sums are respectively

    r_u=Z_a(u)Z_(m-a)(u^(-1)g),
    c_v=Z_a(v)Z_(m-a)(g v^(-1)).                                 (4)

Conditional on U,V, A and C are independent uniform words of those
products. For arbitrary F(A),G(C), their covariance equals the covariance
of E[F|U], E[G|V]; conditional expectation does not increase variance.
Conversely U,V are functions of A,C. Therefore their maximal correlations
are equal. Remove zero rows and columns and set

    S=diag(r)^(-1/2) J diag(c)^(-1/2).

The constant vectors give singular value one. The norm after removing
this singular pair, equivalently the second singular value counting
multiplicity, is exactly rho_(N,m,g). This follows by writing covariance
and variance in the weighted Euclidean coordinates sqrt(r)F,sqrt(c)G.
Thus H_delta concerns completion counts; it is not stated by assuming
another Markov chain is rapidly mixing.

The formula does not require the transposition measure to be central.
It follows directly from concatenation and is valid for any finite group
and any fixed generator alphabet with its corresponding word counts.

## 3. The recursive variance bound

Let gamma_(N,m,g) be the gap of K_A and define the unnormalized gap

    Lambda_N(m)=min_(feasible g) (m-1) gamma_(N,m,g).               (5)

Singleton fibers contribute no variance; take their unnormalized gap
as infinity when forming this minimum. All-singleton cases are trivial.
Define delta_N(m)=1-max_g rho_(N,m,g).

**Theorem 1 (proved conditional recursion).** If delta_N(m)>0 and
ell=m-floor(m/3), then

    Lambda_N(m) >= [delta_N(m)/2] Lambda_N(ell).                   (6)

Proof. Refresh the overlapping intervals AB and BC by their exact
conditional laws. Let P_AB=E[.|C], P_BC=E[.|A] be the two projections,
as operators on functions of the full word. On centered functions,

    ||P_AB+P_BC|| <= 1+rho_(N,m,g).

For completeness, take F in the range of P_AB and G in the range of
P_BC, both centered. By definition |<F,G>|<=rho||F||||G||.
The map (F,G)->F+G has squared norm at most 1+rho, using
2||F||||G||<=||F||^2+||G||^2. Its adjoint is
f->(P_AB f,P_BC f), so their product is P_AB+P_BC and has the same
operator-norm bound. Consequently

    delta_N(m) Var(f)
      <= E Var(f|C)+E Var(f|A).                                 (7)

Conditional on C, AB is uniform on a length-ell fiber with prescribed
product g product(C)^(-1). Conditional on A, BC has product
product(A)^(-1)g. Both are covered by the minimum in (5).

Let D_m(f)=(m-1)<f,(I-K_A)f>. It is exactly the sum over adjacent slots
of (1/4) times the H and R Dirichlet contributions. Its coefficients do
not depend on m. Apply the conditional length-ell Poincare inequalities
to the right side of (7). Every adjacent slot belongs to at most two
of AB,BC. Hence

    E Var(f|C)+E Var(f|A) <= 2 D_m(f)/Lambda_N(ell).

This proves (6). Normalizing by m-1 only after the recursion is essential:
paying a random-scan factor at each level would give an erroneous loss.

## 4. Explicit global mixing consequences

Let k>=3, and suppose the local base gaps supply

    beta_N(k)=min_{2<=j<=k, feasible h} (j-1)gamma_(N,j,h)>0.       (8)

Again ignore singleton variances. Under H_delta for the lengths above k,
set m_0=m and m_(i+1)=m_i-floor(m_i/3), stopping once m_D<=k. Then

    gamma_(N,m,g) >= beta_N(k)/(m-1) (delta/2)^D.                 (9)

For m>k, the identity

    m_(i+1)-2 <= (2/3)(m_i-2)

gives D<=ceil(log_({3/2})((m-2)/(k-2))). Therefore a universal constant
delta and an inverse-polynomial beta_N(k) give an inverse-polynomial
gap for every endpoint and arbitrary larger m. No initialization
restriction is needed. A theorem for all endpoint complexities
d(h)<=k, uniform in starting word and relevant length, supplies (8),
because every j-gate word with j<=k has d(h)<=j<=k.

There is even a fixed small base already available for K_A. The prior
[adjacent-gap proof](../20261015-adjacent-gap-proof/proof.md), Sections
1--2, gives gamma_(N,3,h)>=1/24 for every nontrivial length-three fiber.
At length two the identity, 3-cycle and disjoint-transposition fibers
have gap at least 1/4 by their explicit pair transitions. Thus
beta_N(3)>=1/12. With

    alpha=log(2/delta)/log(3/2),

(9) implies, for m>=4,

    gamma_(N,m,g) >= delta/[24(m-1)(m-2)^alpha].                 (10)

This is a CONDITIONAL all-endpoint polynomial-gap theorem under H_delta,
using the same-author length-three result as a stated dependency. It
does not prove H_delta. For m=2,3 use the direct base bounds.

Since |Omega_g(N,m)|<=M^m and the chain is half-lazy, the elementary L2
contraction bound gives

    t_mix(epsilon) <= ceil(gamma^(-1)
                          [(m/2)log M+log(1/epsilon)]).           (11)

All polynomial statements are in N,m,log(1/epsilon). They are not
automatically polynomial in a wire count log_2 N. A fixed mixture
(K_A+Q_345)/2 inherits at least half the K_A gap. No claim for an
unspecified schedule or vanishing mixture weights is made.

## 5. A weaker version allows some poorly decorrelated scales

Uniform delta is sufficient, not necessary. The exact same proof gives

    gamma_(N,m,g) >= beta_N(k)/(m-1)
                       product_(i<D) [delta_N(m_i)/2].           (12)

Thus the more general STATIC assumption is

    sum_(i<D) log(2/delta_N(m_i)) <= C log(N+m)                   (13)

for a universal C. Together with a polynomial base gap it yields
gamma>=beta_N(k)/[(m-1)(N+m)^C]. A bounded number of inverse-polynomial
deficits is allowed. Requiring only delta_N(j)>=N^(-C) at every scale
does not suffice for a polynomial conclusion from this recursion: over
Theta(log m) levels that estimate gives N^(-O(log m)).

### A concrete weakening for the user's N/2 complexity cutoff

This corollary explicitly uses the sharper smoothing input from the
archived M10 report and its M10-referee: there is R_N=O(N log(N+1))
such that, for m>=R_N, the middle-third bridge kernel is pointwise
within 1/16 of parity uniform. Their endpoint-tilt bound then gives
rho_(N,m,g)<=22/75, uniformly in g. The archived estimate is for paired
transpositions; doubling the smoothing length and multiplying by three
for the middle third gives this R_N, and convolution handles later odd
lengths. This corollary is conditional on that named sharp input. The
previous note's conservative CLR-only O(N^2 log N) scale does not give
the same weakening.

The primary source was checked for this named input:
[Diaconis--Shahshahani (1981)](https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis,%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf),
Section 3, Lemma 14, equation (3.1), and the collection of partition-zone
bounds at the end of the proof of Theorem 1. Those bounds control the
Plancherel sum, not just the displayed total-variation conclusion. The
archive's translation pairs sign-conjugate representations of the pure
transposition measure, chooses the nonnegative character ratio r, and
uses r<=1/N+(N-1)r/N to dominate its even-time sum by the primary
source's lazy-walk Plancherel sum. This gives pointwise parity smoothing
at O(N log N) transposition steps. The external estimate is imported,
not reproved here; the weak-cutoff corollary keeps it as an explicit input.

For N>=6 put k=floor(N/2). Assume:

1. The user's low-complexity theorem gives a polynomial beta_N(k).
2. Only for k<m<R_N and all feasible g,

       1-rho_(N,m,g) >= c/[log(N+2)]^B,                          (14)

   where c>0 and B>=0 are universal constants.

Then the local walk mixes polynomially at all lengths and endpoints.
Proof: above R_N each level has constant loss. Between R_N and k
there are O(log log(N+2)) levels, each costing at most a power of
log(N+2). Their combined cost is exp(O((log log(N+2))^2)), which is
bounded by N^C for some universal C. Below k the base assumption
applies. Fixed N<6 may instead use the proved length-three base and
finitely many additional positive conditional gaps where needed; this
corollary's explicit stated regime is N>=6.

This is a meaningful generalization of the N/2 proposal: it replaces
the unknown global mixing assertion by a static, comparatively weak
separation-of-tails condition on a bounded interval of lengths.
For k=O(log N), the same polylogarithmic deficit alone yields a
quasipolynomial bound by this argument; a constant deficit or the
scale-product condition (13) supplies a polynomial bound.

## 6. What is already known, and what is actually new here

The archived M10 proof already uses maximal correlation of two tails
and a constant-loss overlap recursion above a smoothing scale. The
present target is its UNPROVED intermediate-scale analogue with
overlap proportional to the circuit length. The hypothesis must not
be described as a new proof of the archived theorem or as a resolved
local mixing problem.

The prior short-overlap obstruction does not falsify H_delta: it takes
overlap o(N) while both tails have length N^3. In H_delta the overlap
is at least a third of the TOTAL length. In S3, every nonempty middle
segment has parity-uniform product, and (3) factors, so rho=0 exactly.
This is an all-length proved example of the hypothesis, not merely
a numerical observation.

The proof mechanism extends to other finite groups or generator alphabets
provided the same fixed-endpoint conditional factorization, an additive
finite-range local Dirichlet form, and a small-length base gap are available.
For pair-local forms the constants above apply. For a different finite
interaction range the base must be large enough to cover boundary slots
under the chosen overlapping decomposition, and coefficients must be
recomputed. Group expansion alone does not imply H_delta.

## 7. Falsification, boundaries, and dependency ledger

The numerical search uses all feasible endpoint cycle types for S3,S4,S5
at lengths 4,...,12 and S6 at lengths 4,...,8. It builds (3) using exact
integer dynamic programming. Two seeded power iterations estimate the
largest centered singular value. These estimates are empirical LOWER
approximations, not upper certificates, even if they agree. For N<=4,
a separate exact rational PSD calculation certifies rho<99/100 on
the entire nonconstant subspace in each tested case.

The rational test uses

    G=(99/100)^2 diag(r)-J diag(c)^(-1)J^T.

Restrict to sum r_u f_u=0 by eliminating one coordinate. Strictly
positive rational LDL pivots certify the desired bound. This does not
extrapolate to untested N,m. The script also enumerates the required
identity S3,m4 and S4,m4,m6 cases to check (3) directly, and checks
recursion rounding and local slot multiplicities.

A stronger trial hypothesis rho<=1/2 is **refuted exactly**. In S5 take
m=4 and g=(12)(34), with label 0 fixed. For a tail's single transposition
set F=0 on (12),(34), F=9 on the four cross-pair transpositions within
{1,2,3,4}, and F=-16 on the four transpositions involving 0. Matrix (3)
gives E F=0, with covariance numerator 7336 and variance numerator 14400
under the unnormalized count law. Therefore

    Corr(F(A),F(C))=917/1800>1/2.

This falsifies that numerical constant, not existence of SOME universal
rho_0<1. The full matrix and exact witness are retained in results.jsonl.

Boundary cases: m0 is singleton identity or empty; m1 feasible fibers
are singleton; m2 is treated directly. Odd identity fibers are empty,
while feasible odd endpoints are included throughout. N2 fibers are
singleton and need no mixing. Empty support rows are removed, not
divided by zero. Near-minimal endpoints, including full cycles, are
included when feasible in the declared finite range; their large-N
behavior remains a central falsification target.

Dependencies: elementary conditional expectation and covariance for
Theorem 1; the explicit pair dynamics and the prior same-author
length-three gap for (10); the archived sharp parity-smoothing input
only for (14). New conjectural input: H_delta, or (13)/(14) in their
respective statements. No M340 transport claim, Hurwitz classification,
finite-spectrum extrapolation or unproved generic local-to-global rule
is used.
