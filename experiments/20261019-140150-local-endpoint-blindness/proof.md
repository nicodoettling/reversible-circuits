# Local endpoint blindness: hidden prefix information and a block theorem

Author status: **proved** for the numbered statements below, subject to
independent review. **Unresolved:** whether identity-fiber polynomial mixing
implies polynomial mixing of the same local chain on every endpoint, even
under the proposed initialization restriction. No counterexample to that
specific implication is claimed here.

## 1. Target, conventions, kernels, and the precise hypothesis

Let T_N be all M=binom(N,2) transpositions, N>=2. Products act rightmost
first: (pq)(x)=p(q(x)). Write

    Omega_g(N,m)={w in T_N^m: product(w)=g},
    Z_m(g)=|Omega_g(N,m)|,  p_m(g)=Z_m(g)/M^m,
    pi_(g,m)=Uniform(Omega_g(N,m)).

Only nonempty fibers are considered: m>=N-cycles(g) and sign(g)=(-1)^m.
The input model explicitly supplies g on N labels and m gates; polynomial
means polynomial in N,m, not automatically in log N.

For m>=2, the actual adjacent kernel is K_A=I/2+H/4+R/4. H chooses one
of m-1 linear adjacent slots and a uniform sign, applying
(a,b)->(b,bab) or (aba,a). R chooses a uniform slot; equal (a,a) is
replaced by uniform (s,s), otherwise it holds. There is no wraparound.
Q_r is half-lazy uniform-scan exact same-product length-r heat bath.
Q_345 is half-lazy with equal weights on available lengths from {3,4,5}.
Unavailable kernels on m<2, or Q_345 on m<3, are the identity kernel.
All preserve pi_(g,m). Statements about a mixture apply, for example, to
K_mix=(K_A+Q_345)/2, retaining half-laziness. No new claim of mixing on
short lengths where this heat bath cannot move is implicit.

The initializer is a probability law nu_g, not a single deterministic word.
Use the strong, useful formulation of the user's condition:

    (LB(k,delta))  sup_{contiguous I, |I|<=k}
                  TV((nu_g)_I, Uniform(T_N)^I) <= delta.             (1)

This is stronger than merely requiring the same short marginals across g.
The examples below even hide information from arbitrary subsets of <=k
positions. Thus failure of a conclusion for these examples cannot be
blamed on using a weak meaning of local endpoint blindness.

## 2. Exact marginal identity and dense endpoint hiding

**Proposition 1 (proved).** For any fixed set of r positions, observed gates
u=(u_1,...,u_r) in their original order, and h=u_1...u_r,

    pi_(g,m)(w_I=u) = M^(-r) p_(m-r)(h^(-1)g)/p_m(g).               (2)

Proof. In the group algebra, the uniform transposition measure mu is
central. Inserting the fixed gates into the unobserved independent factors
gives a convolution of powers of mu with point masses at u_j. Commute all
mu powers to one side. The endpoint law is delta_h * mu^(m-r), so there
are precisely Z_(m-r)(h^(-1)g) completions. Division by Z_m(g) proves (2).
This argument covers scattered positions as well as consecutive windows.

For N>=3 and k>=1 define

    eta_k=((N!-2)/2) (1-2/(N-1))^k.

On the reachable parity class,

    |(N!/2) p_k(x)-1| <= eta_k.                                    (3)

The complete-graph interchange gap is N/M=2/(N-1), by
[Caputo--Liggett--Richthammer, Theorem 1.1](https://arxiv.org/pdf/0906.1238).
Twisting by sign pairs the positive and negative eigenvalues. After removing
the constant and sign vectors, the absolute spectral radius is at most
1-2/(N-1). The two point-mass projections have squared norm 1-2/N!;
Cauchy--Schwarz followed by division by 2/N! proves (3). This is the
manuscript's RR.10 parity estimate specialized to the complete graph,
not a bridge-dynamics mixing theorem.

If eta_(m-r)<1, the density in (2) relative to iid lies between
(1-eta_(m-r))/(1+eta_(m-r)) and its reciprocal. Therefore

    TV((pi_(g,m))_I, iid) <= eta_(m-r)/(1-eta_(m-r)).                (4)

This holds uniformly in g and in the specified positions. In particular,
if m>=N^3 and r<=C N for a fixed C, the error is exp(-Omega(N^2)) as
N grows. The user's endpoint-hiding observation is correct for a uniformly
sampled long bridge. Length alone does not give (1) for an arbitrary start.

## 3. A locally blind initializer with hidden prefix constraints

Choose even L and feasible g with both L and m-L large, and sample
independently

    A ~ pi_(e,L), B ~ pi_(g,m-L), W=A B.                            (5)

Let X_j=t_1...t_j. This law is exactly pi_(g,m) conditioned on X_L=e.
Every short window, including one crossing the join, is close to iid:
split its observed gates between A and B and use (4) and product coupling.
For windows of length <=k a sufficient bound is

    delta <= eta_(L-k)/(1-eta_(L-k))
             +eta_(m-L-k)/(1-eta_(m-L-k)),                         (6)

when the indicated lengths are positive and errors below one. A window
lying entirely in one half needs only its one term. Yet

    a_g := pi_(g,m)(X_L=e)=p_L(e)p_(m-L)(g)/p_m(g),
    TV(nu_g,pi_(g,m))=1-a_g.                                      (7)

For dense halves, a_g=(2/N!)(1+o(1)). Thus almost complete global bias
coexists with exponentially accurate local endpoint blindness.

**Proposition 2 (proved, exact S3 witness).** In S3, p_k is exactly uniform
on its parity class for every k>=1: multiplying any permutation by a
uniform transposition gives the uniform opposite parity class. Hence (5)
is exactly k-wise iid for every k<min(L,m-L), for any feasible endpoint g,
while its global TV distance is exactly 2/3.

This proves that local blindness does not imply global equilibrium or
eliminate hidden prefix modes. It does NOT prove superpolynomial mixing.
Even the factorial density ratio 1/a_g is not by itself a slow-mixing
obstruction: its logarithm is only O(N log N).

One can pin many cuts: concatenate independent long identity bridges and
one final g bridge. A short consecutive window meets at most two pieces
when k is below their lengths, so its local error stays bounded by twice
the one-piece error, regardless of the number of pieces. All intermediate
prefixes are nevertheless pinned.

## 4. What bounded-range dynamics does to this information

**Proposition 3 (proved, local propagation bound).** Consider a state-
independent random-scan product-preserving kernel. A branch of span s<=R
has probability alpha_s and chooses uniformly among m-s+1 linear slots;
combine different branches of the same span. Remaining probability is hold.
Each local branch preserves iid gates as a law on the full word space,
as do the kernels in Section 1. Put

    b=min(1, 2 sum_s alpha_s (s-1)/(m-s+1)).

If nu satisfies LB(k,delta), then for a window I of length r<=k,

    TV((nu K^t)_I, iid)
      <= delta + Pr{Binomial(t,b)>floor((k-r)/(R-1))}.              (8)

Proof. Reveal the random update schedule backwards from I. Its dependency
set is contained in an interval. An update extends this interval only when
it intersects and crosses a boundary. At most 2(s-1) span-s slots do so,
and each extension increases length by at most s-1<=R-1. The number of
extensions is stochastically dominated by the stated binomial, using
independent schedule choices and conditional probability at most b. On
the event that the initial dependency interval has length <=k, its nu
and iid laws differ by at most delta. Apply the same local random seeds
and data processing. The iid reference law is stationary. This proves (8).

For fixed R and fixed branch weights, b=O(1/m). Local blindness therefore
persists for order m*k updates with a suitably small constant, with an
exponentially small binomial tail when k-r is proportional to k. This is
a useful local-observation guarantee, not a global-TV mixing guarantee.

**Proposition 4 (proved, hidden-cut lower bound).** Pin q even interior
cuts as above, separated by >=R, and at distance >=R-1 from the boundaries.
Let

    p=sum_s alpha_s (s-1)/(m-s+1),
    theta_j=pi_(g,m)(X_(c_j)=e),  u=q(1-p)^t.

Then

    TV(nu_g K^t,pi_(g,m)) >= u/(1+u)-sum_j theta_j.                (9)

Proof. Only an update crossing a cut can change its prefix product.
Each cut is selected with probability p per step and no step can cross
two chosen cuts. If U counts untouched cuts, E U=u and
E U^2=u+q(q-1)(1-2p)^t <=u+u^2. Cauchy--Schwarz gives
Pr(U>0)>=u/(1+u). An untouched cut remains pinned. The stationary
probability of at least one pinned cut is at most sum_j theta_j. Use
that event in the variational formula for TV.

For polynomial q in N and long segments, sum theta_j~2q/N! is negligible.
The bound forces order m log q updates for fixed-range random scan.
This is a polynomial coupon-collection obstruction. It does not refute
polynomial mixing or the desired identity-to-endpoint implication.

### Exact relaxation under the actual small heat baths in S3

Every sequence of S3 prefixes x_1,...,x_(m-1) of the appropriate alternating
parities is valid, since x_(i-1)^(-1)x_i is an odd permutation and thus a
transposition. This is a bijection. Under pi_(g,m) the internal prefixes
are independent uniform three-valued coordinates, for every endpoint.
A length-r heat bath refreshes exactly its r-1 internal coordinates.

For even L, let f=3 1_{X_L=e}-1. For a half-lazy heat-bath mixture with
active length probabilities alpha_r,

    K f=lambda_L f,
    lambda_L=1-sum_r alpha_r
                   #{j: j<L<j+r, 0<=j<=m-r}/(m-r+1).             (10)

As nu/pi=1+f and the kernel is reversible,

    TV(nu K^t,pi)=(2/3) lambda_L^t.                               (11)

For Q_2, lambda_L=1-1/[2(m-1)], a slowest nonconstant eigenvalue. At
every time the law is a convex combination of the pinned initializer
and pi, so all the small gate marginals remain exactly iid throughout.
For Q_345 the same statement holds with (10). The exact formula does
not assert f is an eigenfunction of K_A; its conditional rates depend
on neighboring prefixes. K_A is treated by (8),(9) and Section 6.

Thus local gate statistics can be completely unchanged while a genuine
relaxation mode of a local heat bath is still decaying.

## 5. Positive theorem: sufficiently long overlapping refreshes mix

This section makes the user's floating-window idea precise. It is a
different, explicitly declared ideal block kernel. The general smoothing
and overlap strategy already appears in the archived M10 proof/referee;
this is a direct multi-block coupling, not a claim that the strategy is new.

**Theorem 5 (proved).** Choose L>=1 such that eta_L<=1/16. Partition m>=2L
gates into q=floor(m/L)>=2 consecutive blocks of lengths L_i in [L,2L-1].
Let d=q-1 and let I_i be the union of blocks i and i+1. Set

    B=I/2 + (1/(2d)) sum_(i=1)^d E_(I_i),

where E is exact same-product heat bath on that entire interval. For
every feasible g and every starting word,

    t_mix(B,epsilon)
      <=ceil(4d log(2d/epsilon))+ceil(2d log(2q/epsilon)),          (12)
    gap(B)>=1/(16d).                                             (13)

No polynomial-time implementation of an exact E_(I_i) is assumed.
The bound counts completed ideal block updates.

Proof. The coarse coordinates x_i are prefix products at the q-1 cuts;
x_0=e and x_q=g. Their joint law is proportional to

    product_(i=1)^q p_(L_i)(x_(i-1)^(-1)x_i).

Conditional on them, block interiors are independent uniform bridges.
Updating I_i is exactly a heat bath for x_i, followed by drawing both
block interiors conditional on the new coarse coordinates.

For any possible neighbors, the conditional law of x_i is proportional
to the product of two factors each within 1+/-eta_L of parity uniform.
It therefore dominates a times parity uniform, where

    a=((1-eta_L)/(1+eta_L))^2,
    beta=1-a<=64/289,   1-2 beta>=1/2.

Consequently any two such conditional laws can be coupled to agree with
probability >=1-beta, independently of the endpoints. Couple coarse
states differing only at coordinate j in Hamming distance. Updating j
heals the difference, and only updates j-1,j+1 can introduce a new one,
with probability <=beta each. Including half-laziness gives expected
distance at most 1-(1-2 beta)/(2d)<=1-1/(4d).
Telescoping along Hamming paths extends this Wasserstein bound to any
two states; iterated couplings give coarse mismatch probability at most
d exp(-t/(4d)). All parity-compatible coarse states exist by (3).

After the coarse coordinates agree, use identical future coarse updates
and identical conditional interior draws. Each block is refreshed with
probability at least 1/(2d) per step. A further t steps leave any block
uncoupled with probability at most q exp(-t/(2d)). The two stages give
(12), even if the initial words are adversarial.

Taking equal phases of length floor(t/2) bounds TV by a constant times
(d+q) exp(-t/(8d)). Since B is finite, reversible and half-lazy, applying
this convergence bound to any nonconstant eigenfunction and taking
t-th roots gives every such eigenvalue <=exp(-1/(8d)). Therefore
gap(B)>=1-exp(-1/(8d))>=1/(16d), proving (13).

For N>=4, a self-contained sufficient scale is

    L=ceil(log(8(N!-2))/[-log(1-2/(N-1))])=O(N^2 log N).           (14)

For N=3 take L=1. The archived M10 character estimate gives the sharper
O(N log N) scale; using that sharpening is conditional on its cited
Diaconis--Shahshahani import and parity translation, not needed for (14).
For fixed C and m>=N^3, (14) fits well inside the circuit for large N.

## 6. The actual comparison, and the first unproved lemma

For a nontrivial fiber write gamma_A(N,ell,h)=gap(K_A on Omega_h(N,ell)).
Use value one for singleton fibers in the minimum below, which is harmless
for their zero conditional variances. Suppose

    gamma_* = min_{2L<=ell<=4L-2, feasible h} gamma_A(N,ell,h)>0.   (15)

**Proposition 6 (proved conditional comparison).** Under (15), for m>=2L,

    gap(K_A on Omega_g(N,m))
       >= [(2L-1)/(16(m-1))] gamma_*,                            (16)

uniformly over endpoints g. For K_mix the right side may be divided by
two, because E_(K_mix)>=E_(K_A)/2.

Proof. Let E_K(f)=<f,(I-K)f>_pi. Conditional on the complement of I_i,
the local K_A has precisely some endpoint h and length ell_i in (15).
Thus E Var(f|outside I_i)<=gamma_*^(-1) E_(K_A,I_i)(f).
An adjacent slot occurs in at most two I_i, and ell_i-1>=2L-1.
The local slot coefficient is 1/[4(ell_i-1)] for each H and R form,
versus 1/[4(m-1)] globally. Therefore

    sum_i E_(K_A,I_i)(f)
       <= [2(m-1)/(2L-1)] E_(K_A)(f),
    E_B(f) <= [(m-1)/(d(2L-1)gamma_*)] E_(K_A)(f).

Combine with (13). No canonical paths, unbounded congestion, or
unmentioned holding-rate normalization is hidden in this comparison.

**First unproved standalone lemma (unresolved).** At the scale L in
(14), prove gamma_* >= (N L)^(-C) for a universal C; alternatively prove
a suitable comparison on the states visited from the proposed initializers
that avoids this worst-endpoint minimum.

An identity-only gap assumption supplies only h=e in (15). Under the
uniform long bridge, a long block product is approximately uniform on a
parity class. Its endpoint is generally not the identity. Local endpoint
blindness concerns marginals of observed gates; it supplies no Poincare
bound for a conditional block law with an arbitrary fixed product h.
This is the specific missing inference. It is not a proof that no other
identity-to-endpoint reduction exists.

The archive's M10/M10-referee already reduces a related aligned four-gate
Hamiltonian to all-endpoint base lengths O(N log N), with a polynomial
loss over scales. The present result does not close or supersede that
base-gap problem. It shows explicitly why a long buffer solves coupling
between blocks but leaves their local equilibration as a separate question.

## 7. Spectral formulation of the initializer-specific question

Let V_k be the span of all functions of <=k consecutive gates, including
constants, in L2(pi). If nu and pi have exactly the same such marginals,
then f=dnu/dpi-1 is orthogonal to V_k. This statement is **proved** by
the definition of conditional expectation. For reversible K,

    TV(nu K^t,pi)<= (1/2)||K^t f||_2.

Thus the relevant additional estimate is decay of K^t on locally
invisible initial densities. It does not follow from orthogonality alone:
Section 4 places a slowest Q_2 eigenfunction in V_k^perp.

A sufficient, **conditional** criterion is that every eigenfunction with
eigenvalue greater than 1-gamma lies in V_k. Then exact local matching
gives TV<=||f||_2 exp(-gamma t)/2. Approximate marginal matching needs
quantitative coefficient/control estimates; it cannot be substituted into
this criterion without them. This is a precise possible target for the
user's restricted-initialization conjecture, not an established premise.

## 8. Boundary checks, dependencies, and falsification scope

- N=2: each feasible fiber is a singleton. N=1 has no transposition gates
  and only the empty identity word, if that degenerate case is admitted.
- m=0: identity has the singleton empty word; other fibers are empty.
  m=1: feasible endpoints are transpositions, with singleton fibers.
- m=2: identity words are (t,t); K_A square refresh is nontrivial unless
  N=2. No dense or multi-block premise is asserted at this length unless
  the stated L permits it. The explicit feasibility condition handles odd m.
- Near-minimal connected factorizations generally do not satisfy the dense
  smoothing assumptions. No theorem here claims they do.
- Algebraic proofs: centrality, conditional bridge factorization, influence
  intervals, coupon second moments, S3 prefix bijection, coupling and the
  displayed Dirichlet comparison. External input for the conservative
  large-N scale: CLR Theorem 1.1, with its normalization shown above.
- Archived dependencies checked: M10 Section 2 and M10-referee Sections
  2.6--5; HB-BASE and HB-DECOMP map scopes. The sharper smoothing scale is
  inherited, not a fresh external-source audit. No M340 transport claim is
  used or promoted. Historical classification/irreducibility disagreement
  is irrelevant to these proofs; no classification input is needed here.
- Deterministic exact checks are in check.py/results.jsonl. They test all
  relevant finite identities, not a claim inferred from observed spectra.
  There is no independent reviewer in this run, no manuscript promotion,
  and no completed all-endpoint small-move gap theorem.
