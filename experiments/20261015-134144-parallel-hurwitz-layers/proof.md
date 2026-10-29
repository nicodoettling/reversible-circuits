# Parallel ternary Hurwitz layers

Author status: **proved** comparisons, boundary correction and scoped
benchmarks below, pending independent review. **Unresolved:** a growing-N
inverse-polynomial gap for the single-cycle family at m=N+1. Pure layers
remain within Hurwitz orbits. The square-heat-bath extension in Section 7
is explicitly a different kernel from the user's pure ternary proposal.

## 1. User kernel, target and conventions

Products act rightmost first. Fix a feasible endpoint g in S_N and an EVEN
word length m>=2. On a fixed ordinary Hurwitz orbit O in Omega_g(N,m),
the target is uniform. Let H_i^+ send (a,b) to (b,bab), and H_i^- be its
inverse (a,b)->(aba,a), at positions i,i+1 for 1<=i<m.

The two matchings have slots M_0={1,3,...,m-1} and M_1={2,4,...,m},
where slot m means the cyclic pair (m,1), interpreted as in Section 2.
Each step chooses a matching with probability 1/2 and independent uniform
coordinates v_i in {-1,0,1}. The corresponding disjoint updates are
applied simultaneously. Write the local ternary kernel and layer kernels

    L_i=(I+H_i^++H_i^-)/3,
    B_a=product_(i in M_a) L_i,
    P_parallel=(B_0+B_1)/2,
    P_seq=(1/m) sum_(i=1)^m L_i.                                (1)

P_seq updates ONE uniform cyclic pair. No extra global laziness is added.
Time for P_parallel counts completed layers, each containing m/2 gate-pair
updates. The coordinates of v are independent; another vector law defines
a different chain. The zero choice has probability 1/3 at each pair.

Disjoint updates commute and are bijections. Reversing all signs gives
the inverse layer with exactly the same probability. Hence P_parallel
is uniform-reversible on O. Its communicating classes equal ordinary
Hurwitz orbits: every layer is an ordinary Hurwitz sequence, and a vector
with just one nonzero coordinate realizes each ordinary adjacent move.
The latter event is used ONLY for connectivity, not to estimate the gap.

Pure Hurwitz moves do not give global uniformity on arbitrary endpoint
fibers. At g=id and even m, each all-equal word (a,...,a) is frozen, and
different a give different support graphs. A global graph-marginal claim
therefore also fails for the pure proposal from arbitrary initial words.

## 2. The cyclic boundary is valid literally at identity, but needs care otherwise

Write a word as a B b, with product g. Applying a naive Hurwitz move to
the ordered boundary pair (b,a), while leaving B unchanged, changes the
product to

    g'=(ab) g (ab)^(-1)   for the plus direction,
    g'=(ba) g (ba)^(-1)   for the minus direction.                (2)

Thus the literal rule works for identity circuits, but not for arbitrary
fixed g. For example ((12),(23),(34),(45)) computes (12345); the naive
boundary plus move gives ((45),(23),(34),(12)), with a different product.
This failure occurs on all 125 minimal five-cycle words and both boundary
signs, as checked exactly. The identity case is unaffected.

There is a natural fixed-endpoint cyclic move that STILL changes only
the first and last gates:

    H_m^+: a B b -> (a g b g^(-1) a) B (g^(-1) a g),
    H_m^-: a B b -> (g b g^(-1)) B (b g^(-1) a g b).              (3)

All displayed factors are transpositions. The two maps are inverses and
preserve g. Since g is fixed, they commute with every interior matching
update on slots 2,4,...,m-2. When g=id, (3) is exactly the literal cyclic
rule, not a change to the user's identity-circuit walk.

To derive (3), the Hurwitz rotation

    D(w)=(t_2,...,t_m,g^(-1)t_1 g)

is the sequence H_1^+,...,H_(m-1)^+. Conjugate the last adjacent move by
this rotation. Cancelling the repeated last generator gives the shorter
chronological lift

    H_1^+,...,H_(m-2)^+, H_(m-1)^sign,
    H_(m-2)^-,...,H_1^-,

of length 2m-3. This proves (3) stays in the SAME ordinary Hurwitz orbit.
For general g, the remainder of the proof uses (3), not the invalid naive
boundary. The naive rule is also valid in the commuting benchmark below.

## 3. A self-contained comparison without an exponentially rare event

Let gamma_seq and gamma_parallel be the Poincare spectral gaps of (1)
on the same nontrivial orbit. Then

    (2/3) E_seq <= E_parallel <= (m/2) E_seq,
    (2/3) gamma_seq <= gamma_parallel <= (m/2) gamma_seq.          (4)

Proof. A local Hurwitz orbit has length 1 (equal gates), 2 (disjoint
unequal gates), or 3 (incident unequal gates). Thus L_i is self-adjoint
with spectrum contained in {1,0,-1/3}. Section 2 makes this true also for
the cyclic slot, by conjugation through a permutation of word states.

The L_i in a matching commute, so diagonalize them simultaneously. Put
k=m/2. For their eigenvalues lambda_i,

    (2/(3k)) sum_i(1-lambda_i)
       <= 1-product_i lambda_i <= sum_i(1-lambda_i).             (5)

For the lower bound, if any eigenvalue is nontrivial, the product is at
most 1/9 unless it is zero or negative, so 1-product>=8/9, whereas the
sum is at most 4k/3. The all-ones case is equality. The upper bound follows
by telescoping the product, with every partial product at most one.
Average (5) over the two matchings to obtain (4).

Every layer spectrum lies in [-1/3,1]; their average does too. Thus the
negative spectrum cannot cause a slow nearly periodic mode. An additional
global hold would divide the gap by two, but is unnecessary here.

The probability of any prescribed v is 3^(-m/2), yet (4) has no such
loss: it aggregates all vectors through commuting operator products.
Likewise, the small probability of a specified sequential trajectory
does not by itself establish a slow mixing time.

## 4. Stronger theorem: one layer provides a sweep-scale gap

**Theorem (proved, using the checked projection lemma below).** For every
nontrivial orbit and even m>=2,

    (1/48) min{m gamma_seq,1}
       <= gamma_parallel <= (m/2) gamma_seq.                    (6)

The same lower bound controls the absolute spectral gap, since all
eigenvalues are at least -1/3. In particular, when m gamma_seq<=1,
the relaxation-time improvement per completed layer is Theta(m), with
absolute comparison constants. This is a parallel-time statement; a
layer uses Theta(m) elementary local updates.

Let E_i be the orthogonal projection onto H_i-invariant functions, i.e.
the average over the local orbit of length 1,2 or 3. Put Q_i=I-E_i,
mathcalH=sum_i Q_i, and let Delta be its gap above the common invariant
space. The local spectra give

    Q_i <= I-L_i <= (4/3) Q_i,
    Delta >= (3/4) m gamma_seq.                                 (7)

Write A_a=product_(i in M_a) E_i and D=(A_0+A_1)/2. The same joint
eigenvalue calculation as above gives the sharper projection comparison

    (8/9)(I-A_a) <= I-B_a <= (4/3)(I-A_a),
    gamma_parallel >= (8/9) gamma(D).                           (8)

Each Q_i commutes with all except at most its two neighboring constraints.
The common null space on O consists of constants. Anshu-Arad-Vidick,
arXiv:1602.01210v3, Lemma 2 and Corollary 3, apply to arbitrary finite
Hilbert-space projectors with this noncommutation bound; a tensor-product
state space is not required. Their bound, with degree parameter 2, yields

    ||A_1 A_0 f||^2 <= ||f||^2/(1+Delta/4)       for f perpendicular to 1.

Source and exact hypotheses checked: https://arxiv.org/pdf/1602.01210v3 .
Our degree-2 overlap, uniform L2 space, projectors, common kernel and
unnormalized Delta match that statement. No periodic-to-open or local-gap
extrapolation is being made; this is a comparison with the FULL Delta.

For two orthogonal projections with intersection projection Pi, put
s=||A_1 A_0-Pi||. The two-projection angle calculation gives
gamma(D)>=(1-s)/2. For completeness, an eigenvector of A_0+A_1 with
eigenvalue lambda>1 has an A_0 component which is an eigenvector of
A_0 A_1 A_0 with eigenvalue (lambda-1)^2, so lambda<=1+s on the
complement of the intersection. Eigenvalues <=1 satisfy the same bound.
Consequently (7),(8) give

    gamma_parallel >= (4/9)
        [1-(1+3m gamma_seq/16)^(-1/2)].                          (9)

For x=m gamma_seq<=1, use 1-(1+u)^(-1/2)>=u/4 for 0<=u<=1 with
u=3x/16. This gives x/48. For x>=1 use monotonicity at x=1. This proves
(6), with its upper bound already in (4).

The external projection theorem is an audited dependency, not a claim
that the Hurwitz gap Delta itself has been bounded independently.

## 5. Comparison with the ordinary LINEAR-position walk

Let P_line=(1/(m-1)) sum_(i=1)^(m-1) L_i, excluding the cyclic slot.
Then on the same orbit

    (1/3) E_line <= E_parallel <= 3m^2 E_line.                   (10)

The lower bound follows from (4) and E_seq>=(m-1)E_line/m. To bound
the boundary term, use the length-(2m-3) lift from Section 2, with the
middle move drawn from L_(m-1). Starting uniformly, every path marginal
is uniform. A deterministic Hurwitz step has energy (3/2) E_(L_i).
Cauchy-Schwarz therefore gives

    E_(L_m) <= (2m-3)[3 sum_(i=1)^(m-2) E_(L_i)+E_(L_(m-1))]
              <= 3(2m-3)(m-1) E_line.

It follows that E_seq<=6m E_line; (4) gives (10). Constants are loose.
All relevant spectra are bounded below by -1/3 and log|O|<=m log M,
M=binom(N,2). Thus polynomial mixing in N,m of the parallel and ordinary
linear orbit walks is equivalent. This proof controls stationary flow;
it never waits for a prescribed exponentially unlikely vector or path.

## 6. A growing-family positive theorem for the actual pure proposal

Take even m>=4, N>=2m, and

    g=(12)(34)...(2m-1,2m),        word length exactly m.

Every minimal word consists of these m disjoint transpositions in some
order. To see why, a transposition graph component containing v vertices
needs at least v-1 edges. If it contains q final cycles, that is at least
v-q+(q-1), exceeding the minimal sum when q>1. Thus a minimal component
contains exactly one final cycle, forcing one edge for each two-cycle and
no edges at fixed points. All m! orders are allowed and one Hurwitz orbit.

Every Hurwitz move now swaps its two commuting gates. Hence the user's
literal cyclic layer walk is parallel adjacent swapping, with swap
probability 2/3 on the selected matching. No boundary correction changes
it, since every gate commutes with g.

Caputo-Liggett-Richthammer, arXiv:0906.1238v4, Theorem 1.1, identifies the
continuous-time interchange gap with the one-particle gap on the same
weighted graph. Section 1.2 defines an edge swap at rate c_xy. On the
m-cycle with unit edge rates, the one-particle Fourier eigenvalues give
gap 4 sin^2(pi/m). Our discrete generator has the factor 2/(3m), so

    gamma_seq = [8/(3m)] sin^2(pi/m).

Source and normalization checked: https://arxiv.org/pdf/0906.1238v4 .
The position cycle is connected, uniform particle permutations are the
state space, and zero non-cycle edge weights are allowed by the theorem.

Combining with (6) proves

    gamma_parallel=Theta(m^(-2)),
    t_mix(epsilon)=O(m^3 log m + m^2 log(1/epsilon)) layers.      (11)

The TV estimate uses |O|=m! and the absolute-gap bound; it is a safe
polynomial bound, not an optimal TV mixing claim. This family has a fixed
support graph, so its nontrivial theorem concerns CIRCUIT order mixing.
It does not prove the full-cycle support or circuit conjecture.

## 7. If the earlier square heat bath is retained: a separate extension

Replace each local ternary L_i by

    J_i=I/2+H_i/4+R_i/4,

where H_i chooses the two signs equally, and R_i refreshes an equal pair
uniformly and otherwise holds. At the cyclic boundary eligibility is
a=g b g^(-1), and the refresh is

    a B b -> (g s g^(-1)) B s.

This is the same conjugated adjacent heat bath; for identity it is the
usual equal-boundary-pair refresh. It commutes with the other updates in
the matching. Let J_seq average the m cyclic J_i and J_parallel average
their products over the two matchings. The target is now global uniform
on every nonempty Omega_g, by the earlier adjacent-chain connectivity.

The local nonconstant eigenvalues of J_i are 3/4, 5/8, or 1/2, according
to whether the pair product is identity, a three-cycle, or two disjoint
transpositions. With E_i now the EXACT same-product pair projection,

    (1/4)(I-E_i) <= I-J_i <= (1/2)(I-E_i).

The matching product is between 1/4 and 1 times its matching projection
in Dirichlet form. Repeating Section 4 with these constants gives

    gap(J_parallel) >= (1/8)[1-(1+m gap(J_seq)/2)^(-1/2)]
                     >= (1/64) min{m gap(J_seq),1},
    gap(J_parallel) <= (m/2) gap(J_seq).                         (12)

In S3, the existing adjacent K_A bound gives gap(J_seq)>=1/(4m).
Therefore this explicitly augmented parallel chain has

    gap(J_parallel)>=1/256,
    t_mix(epsilon)<=ceil(256[(m-1)log(3)/2+log(1/epsilon)]).      (13)

These are global circuit and hence support-marginal bounds, for every
feasible endpoint in S3 and even m>=2. They are NOT bounds for the pure
{-1,0,1} proposal, which has no square refresh. Growing-N polynomial
mixing of the extension remains dependent on a corresponding sequential
gap. Parallelization alone does not establish it.

## 8. Boundaries, evidence and remaining obligation

The specified two perfect matchings require even m. At full-cycle length
m=N+1 this covers odd N; for even N the user must choose a different
schedule, for example open matchings with an unmatched site. That is not
silently included in (1). Odd identity lengths are empty. m=0 gives the
empty identity word; m=1 has no pair and every nonempty fiber is singleton.
N=2 has one feasible word per endpoint and length, so mixes in zero steps.
At m=2 the two slots represent the same local operator and the formulas
above remain valid; the commuting cycle benchmark (11) starts at m=4.

The exact script checks 19890 words and 1062144 layer channels, including
all identity words in S3,m4 and S4,m4,m6; full-cycle S3,m4 and S5,m4,m6;
m2 boundaries; and all 24 commuting benchmark words at m4,N8. It checks
endpoint preservation, the seam lift, reverse-vector detailed balance,
matching commutation and equality of layer/ordinary components. Exact
scalar certificates cover every eigenvalue-count type in matchings of
size up to 20. Twisted square-boundary channels are separately checked.
Finite checks validate formulas; they do not prove asymptotic gaps.

The first missing lemma for a growing full-cycle family is still an
inverse-polynomial ordinary cyclic (equivalently linear, up to (10))
Hurwitz-orbit gap. For global arbitrary endpoints it additionally takes
orbit-breaking updates; Section 7 supplies their explicit parallel form
but not a growing-N gap. For graph-only goals, full-chain bounds imply
marginal bounds, while failure to prove the full gap does not refute a
faster graph marginal. The previous support-projection warnings remain.

Stable paragraph for review: Independent ternary Hurwitz updates on
alternating matchings admit a spectral analysis without paying the
exponentially small probability of a prescribed update vector. On any
fixed Hurwitz orbit, with a product-preserving cyclic boundary, the layer
gap lies between (1/48)min{m gamma,1} and (m/2)gamma, where gamma is the
single-slot cyclic gap. The lower bound follows by local-orbit projection
comparison and the bounded-overlap detectability lemma. Parallel layers
therefore provide a sweep-scale speedup, but polynomial mixing remains
equivalent to the sequential orbit question. Pure layers do not change
Hurwitz orbits or establish global support-graph uniformity.
