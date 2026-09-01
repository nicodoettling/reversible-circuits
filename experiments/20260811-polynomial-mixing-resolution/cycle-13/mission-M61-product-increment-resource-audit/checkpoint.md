# M61 halfway checkpoint

Date: 2026-08-11. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`. Python 3.12.3.

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are read
left-to-right. Write `E=T_N^2`, `p(a,b)=ab`, and condition the uniform law
on `E^l` on `p(X_1)...p(X_l)=h`. The complete-pair chain and auxiliary
operator are exactly those in the plan.

## H-001: an extreme rare-endpoint family has exact `O(1/l)` correlation

**PROVED (scoped).** Let `l>=3`, `N>=4l`, and let `h` be the product of
`2l` pairwise-disjoint transpositions. Then

    mu_l(h)=1/(l-1).

Indeed, transposition length is `|h|_T=2l`. A raw bridge point is a
length-`2l` transposition factorization of `h`. Since multiplication by one
transposition changes transposition length by exactly one, equality between
word length and endpoint length forces every prefix step to increase length.
The cycle partition can only coarsen. Every merge is therefore internal to a
final two-cycle of `h`; hence every factor is one of the prescribed `2l`
transpositions and each occurs once. Conversely, every ordering works because
these transpositions commute. Thus the bridge is a uniform random ordering of
`n=2l` distinct atoms, grouped into `l` ordered pairs.

Given `X_1=(a,b)`, `X_2` is a uniform ordered pair `(c,d)` from the `n-2`
remaining atoms. The forward correlation operator is

    Kf(a,b)=1/[(n-2)(n-3)] sum_{c!=d; c,d notin {a,b}} f(c,d).

On reversal-antisymmetric functions it is zero. On reversal-symmetric
functions it is the normalized adjacency operator of `KG(n,2)`, whose
mean-zero eigenvalues are

    kappa_1=-2/(n-2)=-1/(l-1),
    kappa_2=2/[(n-2)(n-3)]=1/[(l-1)(2l-3)].

For completeness, the standard Kneser calculation can be obtained directly.
For each atom `u`, the centered star indicator
`1_{u in A}-2/n` has eigenvalue `-2/(n-2)`. Their span has dimension `n-1`.
The remaining centered symmetric subspace is orthogonal to every star; the
identity `A^2=(d-1)I+(lambda)A+(mu)(J-I-A)` for the strongly regular
disjointness graph, or direct common-neighbor counting, gives eigenvalue
`1/binom(n-2,2)=2/[(n-2)(n-3)]`. Dimensions exhaust the two-subset space.

Insert these values and `kappa=0` into M16's proved real scalar Gram formula.
For `kappa_1`, the two Gram values are `0` and `1/(l-1)`; for `kappa_2`
they are

    2(l-1)/[l(2l-3)] and (1-kappa_2)/l,

both at most `1/(l-1)` for `l>=3`; the antisymmetric value is `1/l`.
Therefore the displayed value of `mu_l(h)` is exact. This family is
near-minimal and extremely endpoint-tilted, so it is a nontrivial calibration,
but it does not cover arbitrary `h`.

The complete-pair chain itself also has a polynomial gap on this family:

    gap(C_(l,h)) >= 1/(l-1).

To see this, condition on any one microcoordinate `(a,b)` and apply M16's
leave-one-out proof without replacing its slice constant by a global worst
case. Deleting `(a,b)` leaves exactly the same family with the other
`2(l-1)` prescribed disjoint atoms. Hence, if `delta_l` is the minimum gap
within this family at length `l`, M16's proved inequality and the exact value
of `mu_l` above give

    delta_l >= delta_(l-1) (l-2)/(l-1).

At `l=2`, the unique coordinate pair is a whole-state heat bath, so
`delta_2=1`; telescoping proves the claim.

There is also a completely independent, weaker comparison check:

    gap(C_(l,h)) >= 1/[6(l-1)].

Identify a bridge state with a permutation of the `n=2l` distinct atoms in
the `2l` word slots. Choosing two microcoordinate bins and heat-bathing them
uniformly permutes the four atoms in their four slots, so its kernel is the
uniform average over `S_4` on those positions. Let `R_n` be the nonlazy
random-transposition shuffle on all `n` positions. A transposition between
different bins occurs in exactly one selected-bin heat bath, with transition
coefficient `1/[24 binom(l,2)]`; a within-bin transposition occurs in `l-1`
such heat baths and has larger coefficient. Therefore, as Dirichlet forms,

    E_C >= alpha_l E_R,
    alpha_l=binom(2l,2)/[24 binom(l,2)]
           =(2l-1)/[12(l-1)].

The standard representation (or the elementary card-position eigenfunctions
plus the random-transposition spectrum) gives `gap(R_n)=2/(n-1)`. Multiplying
the two exact normalizations gives the claimed `1/[6(l-1)]`. This comparison
uses no deterministic hub and has per-transition implementation polynomial in
`l`.

The deterministic rational substitution check through `l=30` is
`geodesic_matching_spectrum_l30.json`. It can falsify the displayed algebra,
not prove the universal geodesic argument.

## H-002: Caputo's three-coordinate reduction fails its exact hypothesis

Pietro Caputo, *On the spectral gap of the Kac walk and other binary
collision processes*, arXiv:0807.3415v1, defines the conditioned product law
through an additive conservation law in (2.1), names the resulting residual
conditioning identity the **non-interference property**, and uses it in the
proof of Theorem 2.1. In particular, equations (1.11) and (the proof following)
(2.3) require `E_b E_b'=E_b' E_b` for disjoint coordinate pairs. Its generator
is `L=N^{-1} sum_b(E_b-I)`, whereas our discrete chain satisfies

    -L=(l-1)(I-C_l)/2.

The hypothesis, not just the normalization, fails here.

**PROVED exact counterexample to non-interference.** Take `N=4,l=4,h=e`,
and work first on functions of the product of each raw microincrement. The
product support is all of `A_4`, with raw lift weights `6` for `e`, `3` for
each three-cycle, and `2` for each double transposition. Let

    b={1,3}, c={2,4}

(one-based coordinate positions), let the source product word be
`(e,e,e,e)`, and let the target be `(a,d,a^{-1},d')`, where in one-line,
zero-based permutation notation

    a=(0,2,3,1),       d=(1,0,3,2),
    a^{-1}=(0,3,1,2), d'=(2,3,0,1).

Thus `d` and `d'` are distinct double transpositions and the target product is
identity. In the order `P_b` then `P_c`, the unique intermediate product word
that can reach the target is `(a,e,a^{-1},e)`. In an identity fiber the
two-coordinate product normalizer is

    6^2+8*3^2+3*2^2=120.

The first selection has probability `3^2/120=3/40`. Conjugation and inversion
preserve the lift weights, so the second has probability `2^2/120=1/30`.
Consequently

    (P_b P_c)(source,target)=1/400.

In the reverse order, the first update would have to leave positions 2 and 4
equal to the distinct self-inverse elements `d,d'`; their product is not
identity, so no intermediate bridge word exists and

    (P_c P_b)(source,target)=0.

This product-sector witness lifts to the raw bridge, since conditional
resampling of product coordinates has exactly the displayed lift weights.
Therefore the two raw conditional expectations do not commute. The exact
artifact is `noninterference_product_N4_l4.json`. As a useful calibration,
the separated complementary pairs `{1,2},{3,4}` commute in the same artifact,
and all disjoint pairs commute for `N=3` because `A_3` is abelian
(`noninterference_N3_l4.json`).

Hence Caputo Theorem 2.1 and its triangle proof do not apply to this ordered
noncommutative bridge. This refutes a proof route, not a polynomial gap.

## H-003: low conjugation degree does not give low walk-Fourier degree

**PROVED structural reduction and obstruction.** Under simultaneous
conjugation by `S_N`, the product-support coordinate space is

    1 + Ind_{C_{S_N}((123))}^{S_N} 1
      + Ind_{C_{S_N}((12)(34))}^{S_N} 1.

The two centralizers contain `S_{N-3}` and `S_{N-4}`, respectively. By
Frobenius reciprocity and the branching rule, any Specht module `S^lambda`
occurring here satisfies `N-lambda_1<=4` (with the usual conjugate-pair
identification after restriction to `A_N`). This validates the proposed
`O(N^4)` low-conjugation-level description.

It does **not** allow one to retain only low-degree character ratios in the
random-transposition convolution. Conjugation type and left-regular Fourier
support are different: the singleton function `delta_e` is conjugation
invariant, yet its Fourier transform is the identity matrix in every
irreducible representation. Moreover, for arbitrary endpoint `h`,

    rho_h(g) proportional to w(g) Q^{l-1}(g^{-1}h)

and the kernel from M16 are equivariant only under the centralizer `C(h)`, not
under all `S_N`. At a rare endpoint the denominator can be supported on a
thin geodesic layer. Thus neither the branching reduction nor ordinary
random-transposition character-ratio decay controls `K_(l,h)` without a new
endpoint-uniform ratio theorem. The geodesic matching proof above handles one
such thin layer directly.

## H-004: exact near-geodesic matching reduction, and its remaining asymptotic block

Now let `l` be even, set `N=2l`, and let `h_l` be a fixed-point-free
involution of cycle type `2^l`. Its transposition length is `l`, while the raw
bridge has `2l` gates. This is the finite data's dangerous near-geodesic
family, distinct from H-001's fully geodesic `2^(2l)` endpoint.

The centralizer of `h_l` is the hyperoctahedral group. It has eight orbits on
the one-product support `{e, 3-cycles, double transpositions}` for every tested
`l>=4`. Fixing one distinguished matching edge gives 17 orbits at `l=4` and
18 for `l>=6`. The exact script `matching_orbit_quotient.py` canonically
constructs these orbits without enumerating the centralizer. It evaluates
every completion count by the proved central character formula

    (2l)! H_s(q)=sum_(lambda |- 2l)
                     d_lambda chi_lambda(q)c_lambda^(2s),

then sums exact integer transition numerators before the final floating
diagonalization of an at-most-18-dimensional reversible quotient. Since
`h_l` itself belongs to the distinguished-edge stabilizer, the twist `U` is
identity on this quotient and its forward kernel is self-adjoint. Detailed
balance errors are below `7e-18` in all recorded cases.

At `l=4`, the distinguished-edge quotient gives

    kappa=0.4647655273004439,
    mu=0.5985741454753329,

exactly reproducing M16's independently enumerated full leading value. Thus
the dangerous mode is already present in the pair-standard matching sector;
it is not visible in the fully centralizer-invariant eight-state quotient.
The exact finite sequence is:

| `l` | pair-edge quotient `mu` | `l mu` |
|---:|---:|---:|
| 4 | 0.5985741455 | 2.394296582 |
| 6 | 0.4123665135 | 2.474199081 |
| 8 | 0.3221423928 | 2.577139142 |
| 10 | 0.2663047654 | 2.663047654 |
| 12 | 0.2279811462 | 2.735773755 |
| 14 | 0.1999202301 | 2.798883221 |

The leading `kappa` at `l=14` is `0.1383756324`, so the data are compatible
with `kappa~2/l` and `mu~3/l`; they do not refute `A/l`. A simple indicator
that the product increment preserves the distinguished matching edge setwise
has weighted correlation `0.9406` with the leading quotient eigenfunction at
`l=14`, making that endpoint-edge block a concrete analytic target. This is
finite exact-count evidence only. Nontrivial centralizer representations not
having an edge-stabilizer fixed vector also remain unaudited.

The central square mode is safer: exact Murnaghan--Nakayama values through
`l=12` give `l` times its additive Gram Rayleigh quotient between `1.006` and
`1.010`. Again, this is only a falsifier.

There is a rigorous component-assembly warning. A connected support component
containing `k` endpoint two-cycles has `2k` vertices and product with `k`
cycles. If it contains `r` gates, join/cut accounting gives

    r=3k-2+2g,  g>=0.

Indeed only a join can merge two current factorization-graph components, so a
connected word has at least `2k-1` joins; the endpoint cycle count then forces
at least `k-1` cuts. For a global length-`2l` word with `c` support components
and total genus `G`, summing gives `c=l/2+G`.

In the all-genus-zero sector, the Goulden--Jackson genus-zero Hurwitz formula
for a fixed permutation of type `2^k` gives

    F_k=(3k-2)! (2k)^(k-3) 4^k.

After word interleaving, the labeled component EGF is

    B(z)=sum_(k>=1) 4^k(2k)^(k-3) z^k/k!
        =(1/8)(T-3T^2/4+T^3/6),  T=8z exp(T).

At its radius `rho=1/(8e)`, `T=1`, hence

    B(rho)=5/96,  rho B'(rho)=1/16,
    rho B'(rho)/B(rho)=6/5.

But genus zero at total length `2l` has exactly `c=l/2` components, hence
conditioned mean component size `l/c=2`. Since `2>6/5`, there is no
subcritical saddle that could yield the tempting uniform exponential
component-size tail. This is a universal obstruction to that proof route,
not a correlation counterexample. Exact genus-zero mass in the full bridge is
`1520/1721=0.8832` at `l=4` and decreases to `0.7620` at `l=12`; its
asymptotic full-bridge mass is open. A condensation theorem for the isolated
genus-zero assembly would still not control positive-genus mass or the
pair-standard correlation block.

The smallest near-geodesic standalone step exposed by this audit is:

> **MATCHING PAIR-STANDARD CORRELATION.** For every even `l>=4`, the largest
> nonconstant eigenvalue of the exact distinguished-edge-stabilizer forward
> quotient for `(N,h)=(2l,2^l)` is at most `C/l` for a universal `C`.

Even this proposition would only control one centralizer sector. A full
matching-endpoint theorem must additionally compare every other centralizer
isotypic block to it or bound those blocks separately.

## H-005: reconciliation with original-`K` prefix-fiber escape

Coordinator Theorem 13.1 proves that every exact prefix-product fiber
`A_(k,h)` of the original lazy local chain has pointwise exit probability at
least `1/[2|R_m|(m-2)M^3]`. M61 studies an **internal** complete-pair chain at
a fixed endpoint. Thus a slow M61 mode would obstruct the current comparison
proof, but it would not make one exact prefix fiber a bottleneck for original
`K`; the boundary `H_3` move bypasses that internal mode.

The smallest endpoint-shell union for which the single-fiber certificate no
longer automatically orients boundary flow has two fibers. In the calibration
`N=3,m=4,k=1`, choose distinct transpositions `a,b` and the identity word

    w=(a,b,b,a).

For its first window, Theorem 13.1's `a!=b` replacement is

    (a,b,b) -> (b,bab,b).

It preserves the triple product but moves the prefix from `a` to `b`.
Therefore its certified edge is internal to
`A_(1,a) union A_(1,b)`. This proves only that the one-fiber certificate cannot
be summed verbatim for the smallest nontrivial shell union. It does **not**
show that this two-fiber union, or any larger endpoint shell, has small
conductance; all other `H_3,H_4,H_5` boundary flow still has to be counted.

## Primary-resource audit so far

1. Caputo, arXiv:0807.3415v1, Theorem 2.1: exact additive residual law and
   commuting-disjoint-projection hypothesis fail by H-002.
2. Carlen--Carvalho--Loss, arXiv:0705.3729v1: their correlation-operator
   program analyzes a specific sphere/energy bridge via explicit Jacobi
   polynomial spectra and then identifies the exceptional additive
   eigenspaces. The abstract noncommuting-projection decomposition is already
   represented by M16, while the explicit geometric diagonalization has no
   analogue for the arbitrary group endpoint.
3. Targeted searches for a noncommutative group-product bridge Efron--Stein
   theorem or a random-transposition endpoint-bridge Poincare theorem did not
   locate a primary theorem with this state space and complete-pair heat bath.
   This is a negative resource finding, not a nonexistence theorem.
4. Goulden--Jackson's classical genus-zero transitive transposition formula,
   as rederived in Carrell--Goulden, arXiv:1607.02518, applies exactly to the
   fixed type `2^k` component count above. It exposes a supercritical
   genus-zero assembly, but supplies no spectral inequality.
5. Stufler, *Gibbs partitions: the convergent case*, arXiv:1609.08859,
   proves giant-component results for convergent weighted assemblies. Using it
   for the present fixed-linear-component-count genus-zero slice requires a
   checked conditioning translation; even then, positive-genus sectors and
   correlation remain. It is therefore recorded as conditional, not invoked.

## H-006: minimal long cycles refute universal `A/l` product correlation

**PROVED.** Let `n=2l+1` and let `h_n` be the long `n`-cycle. There is an
explicit frequency-two product-sector function `f_n` for which M16's Gram
Rayleigh quotient gives

    liminf_(l->infinity) sqrt(l) mu_l(h_n)
       >=24/(sqrt(2)d_0)=1.5097776...,

where

    d_0=8/sqrt(2pi) int_0^1
          sin^4(pi x)/[x(1-x)]^(3/2) dx
       =11.2404385....

The full proof is frozen in `minimal_long_cycle_refutation.md`. For a
transposition `t=(r s)`, put

    a(t)=-(omega^(-r)-omega^(-s))^2,

and for a raw pair `X=(r,s)` with product `g=rs`, define

    f(g)=E[a(r)+a(s) | rs=g].

This is a legitimate product-fiber function. Féray--Kortchemski's exact
minimal-prefix count and a four-gap Stirling/Riemann-sum calculation give,
uniformly for any two distinct raw transposition positions,

    E|a(t_i)|^2=d_0/sqrt(n)+o(n^(-1/2)),
    Re E[conj(a(t_i))a(t_j)]=12/n+o(n^(-1)).

Centrality makes the latter joint law independent of the separation.
Conditional independence inside distinct raw product fibers gives exactly

    E[conj(f(G_i))f(G_j)]=4 E[conj(a(t_1))a(t_2)],

while conditional-expectation contraction gives

    E|f(G_i)|^2<=2d_0/sqrt(n)+o(n^(-1/2)).

Putting the same `f` in every coordinate of M16's exact block Gram form
proves the displayed lower bound. Hence no universal finite `A` can satisfy
`mu_l(h)<=A/l` for every endpoint. This refutes the literal
PRODUCT-INCREMENT BASE CORRELATION proposition, not polynomial mixing: it
does not upper-bound the complete-pair gap and does not create an
original-`K` bottleneck.

The exact cyclic Fourier quotient was corrected to handle non-free cyclic
orbits when `2l+1` is composite. It reproduces the inherited full
`(N,l)=(7,3)` value exactly and gives `l mu=2.2409,...,4.0912` through
`l=10`. The exact fiber-averaged witness agrees with the proof. These finite
checks audit the algebra only.

## Exact frontier

The universal `mu_l(h)<=A/l` statement below is now **REFUTED by H-006**.
It is retained verbatim to identify the superseded frontier:

> **PRODUCT-INCREMENT BASE CORRELATION.** There is a universal finite `A`
> such that for every `N>=3`, feasible `h in A_N`, and
> `3<=l<C_mix N log(N+1)`, every mean-zero eigenvalue sector of the normal
> forward product kernel gives Gram top eigenvalue at most `A/l`.

A representation proof must control the endpoint-tilted completion ratios,
not merely the `O(N^4)` coordinate dimension. A Caputo-style proof must replace
the false crossing-pair commutation by a quantitative commutator or braid
error bound.

The new smallest standalone step is:

> **LONG-CYCLE EXCEPTIONAL-CLOSURE GAP.** Prove a universal inverse-polynomial
> gap for the complete-pair chain on the invariant closure generated by the
> frequency-two minimal-long-cycle witness, or replace the false pointwise
> `A/l` estimate by an accumulated inequality that tolerates these
> `Theta(l^(-1/2))` modes.

This remains an auxiliary-chain implication, not Terminal A or B.

## Reproduction

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_falsifier.py --N 3 --length 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_N3_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_product_falsifier.py --N 4 --length 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_product_N4_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/geodesic_matching_spectrum.py --l-max 30 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/geodesic_matching_spectrum_l30.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/perfect_matching_square_mode.py --lengths 4,6,8,10,12 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/perfect_matching_square_mode_l12.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_orbit_quotient.py --quotient pair-stabilizer --lengths 4,6,8,10,12 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_pair_stabilizer_l12.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_genus_zero_audit.py --lengths 4,6,8,10,12 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_genus_zero_l12.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature.py --n-values 7,9,11,13,15,17,19,21 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature_n21.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/long_cycle_fourier_quotient.py --lengths 3,4,6,8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/long_cycle_fiber_witness_l8.json
```

All are deterministic and use no seed or nonstandard dependency.
