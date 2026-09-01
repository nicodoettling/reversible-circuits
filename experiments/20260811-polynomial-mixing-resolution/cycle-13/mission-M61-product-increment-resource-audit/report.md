# M61 final report: product-increment base correlation

Date: 2026-08-12. Repository commit at assignment:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`. Python 3.12.3. All
computations are deterministic and use no random seed or nonstandard Python
dependency.

This report concerns the complete-pair auxiliary bridge. It does **not** claim
Terminal A or Terminal B for the original local `{3,4,5}` identity chain.

## 1. Exact claim and conventions

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are multiplied
from left to right. Let `E=T_N^2`, let `p(a,b)=ab`, and condition the uniform
law on `E^l` on

    p(X_1) ... p(X_l)=h.

Let `C_(l,h)` be the nonlazy complete-pair heat bath and

    A_(l,h)=l^(-1) sum_i E[ . | X_i]

the averaged one-coordinate projection. Write `mu_l(h)` for its top
mean-zero eigenvalue.

**Refuted claim.** There is no universal finite `A` such that

    mu_l(h) <= A/l                                      (1.1)

for every `N>=3`, feasible `h in A_N`, and
`3<=l<C_mix N log(N+1)`. More precisely, if `n=2l+1` and
`h_n=(0 1 ... n-1)`, then

    liminf_(l->infinity) sqrt(l) mu_l(h_n)
       >= 24/(sqrt(2)d_0)=1.5097776... > 0,             (1.2)

where

    d_0=8/sqrt(2 pi) int_0^1
          sin^4(pi x)/[x(1-x)]^(3/2) dx
       =11.2404385....                                  (1.3)

The endpoint `h_n` is even because `n` is odd, and a length-`2l=n-1`
transposition bridge to it is feasible. For every fixed `C_mix>0`, this
family is in the assigned base range for all sufficiently large `l`, since
`l/[n log(n+1)]` tends to zero. Thus (1.2) contradicts (1.1) for every
finite `A`.

## 2. Full argument and construction

The detailed proof, including all exact sums and convention translation, is
frozen in `minimal_long_cycle_refutation.md`. Here is the complete logical
chain.

### 2.1 Exact two-position moments

Under the bridge, the raw word

    t_1 ... t_(n-1)=h_n

is a uniform minimal transposition factorization. Put

    omega=exp(2 pi i/n),  u_v=omega^(-v),
    a((r s))=-(u_r-u_s)^2,
    A_k=k^(k-2)/(k-1)!=k^(k-1)/k!.

Because `sum_v u_v^2=0`, `a(t)=sum_v u_v u_(t(v))` is a frequency-two
matrix coefficient. Conjugation by the endpoint cycle preserves the bridge
and multiplies this coefficient by a nontrivial character, so it is centered.

Let `v_n=E|a(t_i)|^2` and
`c_n=E[conj(a(t_i))a(t_j)]` for `i!=j`. With
`T=sum_(t in T_n)t` in the group algebra, centrality gives the exact,
separation-independent law

    Pr(t_i=e,t_j=f)
      =[h_n] e f T^(n-3) / [h_n]T^(n-1),                (2.1)
    [h_n]T^(n-1)=n^(n-2).

The minimal-factorization count for residual cycle sizes `q_s` is

    (n-3)! product_s A_(q_s).                            (2.2)

It follows that

    v_n=8n (n-2)!/n^(n-2)
        sum_(d=1)^(n-1) A_d A_(n-d) sin^4(pi d/n),       (2.3)

and hence

    sqrt(n)v_n -> d_0.                                  (2.4)

For two disjoint extendible chords, use their four positive cyclic gaps
`a,b,u,v`. The residual cycle sizes are `a,b,u+v`. Cyclic starts and the two
noncrossing placements give the exact real contribution

    D_n=16n (n-3)!/n^(n-2)
        sum_(a,b,u,v>=1; a+b+u+v=n)
        A_a A_b A_(u+v)
        sin^2(pi a/n) sin^2(pi b/n)
        cos(2pi(v-u)/n).                                (2.5)

The shared-endpoint contribution is `O(n^(-3/2))`. Indeed,
`A_k<=C e^k k^(-3/2)` uniformly, while a chord of smaller cyclic gap `d`
has amplitude `O(d^2/n^2)`. Splitting the three-gap sum by the number of
macroscopic gaps makes the bulk `O(n^-2)`; the one-small/two-macroscopic
range is `O(n^-3/2)`; and the two-small range gains the missing power from
the two Fourier amplitudes. Dyadic summation is uniform up to the boundary.

The same bound and the sine zeros at each boundary face give integrable
Riemann-sum envelopes in (2.3) and (2.5). The limiting triangle integral is

    (4/pi^2) int_(x,y>0,x+y<1)
       sin^2(pi x)sin^2(pi y)sin(2pi(1-x-y))
       /[xy(1-x-y)]^(3/2) dxdy =12.                    (2.6)

One exact evaluation first integrates the convolution at `s=x+y`:

    int_0^s sin^2(pi x)sin^2(pi(s-x))/[x(s-x)]^(3/2) dx
      =pi^2/s[J_1(2pi s)-2cos(pi s)J_1(pi s)],          (2.7)

then uses the Bessel equation and integration by parts. Equivalently, the
absolutely convergent sine/Dirichlet series displayed in the proof note is
evaluated by duplication and Chu--Vandermonde twice. Therefore

    Re c_n=12/n+o(1/n).                                 (2.8)

The count (2.2) is Féray--Kortchemski, Lemma 2.1; their multiplication
convention is the reverse of the project convention, and reversing the tuple
translates it. The central class-sum proof (2.1) is internal to the project
convention.

### 2.2 Product-sector lift

Group consecutive raw factors as `X_i=(t_(2i-1),t_(2i))` and
`G_i=t_(2i-1)t_(2i)`. For a raw pair `X=(r,s)`, set

    B(X)=a(r)+a(s),
    f(g)=E[B(X) | rs=g].                                (2.9)

Thus `f` is a genuine function of a product coordinate, supported on
`{e,3-cycles,double transpositions}`, and it is centered by cyclic covariance.
The bridge density depends on a raw pair only through its product. Conditional
on two product coordinates, their raw lifts are independent and uniform on
the respective product fibers. Consequently, for `i!=j`,

    E[conj(f(G_i))f(G_j)]
      =E[conj(B(X_i))B(X_j)]=4c_n.                      (2.10)

Conditional expectation is an `L^2` contraction, so

    V_f=E|f(G_i)|^2
       <=E|B(X_i)|^2
       =2v_n+2 Re c_n
       =2d_0 n^(-1/2)+o(n^(-1/2)).                     (2.11)

Hence the real Rayleigh quotient of M16's forward product-correlation block
on `f` is at least

    (24/d_0)n^(-1/2)+o(n^(-1/2)).                      (2.12)

Put this same `f` in every one-coordinate slot of M16's exact Gram form. Its
Rayleigh quotient is

    1/l+(l-1)/l Re<f,Kf>/||f||^2.                      (2.13)

The nonzero spectra of the Gram operator and `A_(l,h_n)` coincide. Equations
(2.12)--(2.13), with `n=2l+1`, prove (1.2). The argument needs only a
Rayleigh witness; `f` need not be an eigenfunction. In the scalar notation,
if `kappa=Re<f,Kf>/||f||^2`, the aligned Gram value is exactly
`mu_f=1/l+(l-1)kappa/l`; this is the normalization converting (2.12) into
(1.2).

### 2.3 Additional exact results and failed routes

The investigation also proved the following scoped statements.

* If `N>=4l` and `h` is a product of `2l` disjoint transpositions, then the
  bridge is a uniform ordering of those atoms and
  `mu_l(h)=1/(l-1)`. Slice recursion gives
  `gap(C_(l,h))>=1/(l-1)`. Thus even an extremely thin geodesic endpoint need
  not violate the proposed order.
* Caputo's non-interference hypothesis is false for the group-product bridge.
  At `N=4,l=4,h=e`, two crossing coordinate-pair projections have an explicit
  matrix entry `P_bP_c=1/400` and `P_cP_b=0`. Thus Caputo Theorem 2.1 cannot be
  imported merely by changing normalization.
* The coordinate product-support representation under conjugation is
  `1+Ind_(C(3))1+Ind_(C(2,2))1`, so only partitions with at most four boxes
  below the first row occur. This does not bound left-regular Fourier degree:
  endpoint tilting by `Q^(l-1)(g^-1 h)` destroys full conjugation equivariance.
* For matching endpoints `(N,h)=(2l,2^l)`, an exact 18-state distinguished-edge
  quotient has `l mu` increasing from `2.3943` at `l=4` to `2.7989` at `l=14`.
  This does not refute `O(1/l)` and is retained only as a finite falsifier.

## 3. Probability, runtime, path length, and congestion accounting

The asymptotic proof is enumerative, not a path comparison. Its exact bridge
normalizer is `n^(n-2)`, and its exact two-position probabilities are (2.1)
with residual multiplicities (2.2). The product-fiber average in (2.9) has
`q(g)` ordered lifts; no lower bound on an individual lift is discarded,
because (2.10) conditions and sums over every lift exactly.

Evaluating the explicit witness `f(g)` by enumerating its ordered lifts costs
`O(N^2)` arithmetic operations per support element. The proof does not supply
canonical paths, a simulation of a heat-bath transition, or a congestion
bound, and no such quantity is silently inferred from the finite quotient.

The finite exact diagnostics use integer character/count tables followed by
floating diagonalization. The long-cycle cyclic quotient has dimension
`O(l)` after orbit reduction but constructs raw product data in polynomial
time for the recorded fixed lengths. The matching character calculations sum
over partitions and are diagnostics, not a claimed polynomial-time proof
algorithm. The original exact `{3,4,5}` block samplers and their polynomial
per-step implementation are outside this auxiliary claim.

## 4. Dependencies

* **Proved, inherited:** M16 leave-one-out recursion, normal scalar Gram
  blocks, equality of the nonzero Gram and averaged-projection spectra,
  product-support dimension `O(N^4)`, and microfiber eigenvalue `1/l`.
* **Proved here:** formulas (2.1), (2.3), (2.5), the shared-endpoint bound,
  limits (2.4), (2.8), the exact product-fiber identity (2.10), and the
  Rayleigh lift (2.11)--(2.13).
* **Cited with checked convention:** Féray--Kortchemski,
  arXiv:1712.06542, Lemma 2.1, Proposition 1.1, and Corollary 1.2, for minimal
  long-cycle factorization counts and cyclic-gap marginals. Their tuple is
  reversed to match the project convention; (2.1) independently fixes the
  order.
* **Cited only to reject applicability:** Caputo, arXiv:0807.3415,
  Theorem 2.1, assumes the non-interference/commuting residual projections
  refuted above. Carlen--Carvalho--Loss, arXiv:0705.3729, obtains exceptional
  modes from explicit sphere/Jacobi geometry absent here.
* **Conditional and unused in the refutation:** any asymptotic statement about
  positive-genus matching components or a matching pair-standard quotient.
* **Empirical only:** finite spectra, quotient eigenvectors, and exact moment
  checks through `n=51`. They audit constants but do not prove (1.2).

The resource search found no primary theorem for arbitrary-endpoint
noncommutative product bridges whose hypotheses include this law. This is a
negative search result, not a nonexistence theorem.

## 5. First unproved standalone step

> **LONG-CYCLE EXCEPTIONAL-CLOSURE GAP.** For the complete-pair chain on the
> minimal-long-cycle bridge, prove a universal inverse-polynomial gap on the
> invariant closure generated by the frequency-two witness, or prove an
> accumulated leave-one-out inequality that tolerates its
> `Omega(l^(-1/2))` correlation.

This is the smallest replacement for the now-refuted pointwise `A/l` input.
It remains an auxiliary-chain implication and is neither Terminal A nor
Terminal B.

## 6. Strongest self-attack

The two most audit-sensitive parts are the `16n` multiplicity in (2.5) and
the uniform `O(n^-3/2)` bound for shared-endpoint pairs. A missed chord
orientation would change the constant, and an unaccounted boundary regime
could invalidate the asymptotic separation. The proof note exposes both
counts rather than hiding them behind the numerical scripts; independent
exact enumeration through `n=51` agrees with them. The triangle-integral
identity (2.6) is also isolated with both a Bessel and an absolutely
convergent series evaluation.

Even if every displayed asymptotic is accepted, the conclusion is only a
lower bound on `mu_l(h_n)`. It does not prove a matching upper bound, an upper
bound on `gap(C_(l,h_n))`, an upper bound on the aligned `B`-sector gap, or
slow mixing of original `K`. If inserted mechanically into the naive CGL
product accumulation, a retention loss of order `l^(-1/2)` yields only
`exp(-Omega(sqrt(l)))`, rather than an inverse polynomial; this refutes that
proof hypothesis, not the underlying gap. The boundary `H_3` certificate for
a single original-`K` prefix fiber therefore does not conflict with this
internal mode. The smallest union where that certificate no longer orients
flow is already two prefix fibers (`N=3,m=4`), but all remaining boundary flow
is uncontrolled and no bottleneck is claimed.

## 7. Calibration suite

* Odd original `m`: the identity bridge is empty. Here `m=2l=n-1` is even.
* `m=0`: singleton; unrelated to the theorem.
* `N=2`, even `m`: singleton; excluded by `n=2l+1>=7`.
* `m=2`, `N>=3`: excluded disconnected regime; here `m>=6`.
* `S_3,m=4` (27 words), `S_4,m=4` (120 words), and `S_4,m=6` (3936 words):
  no claim or normalization is changed. In particular, whole-word `H_4` at
  `m=4` is not being omitted; original `K` is not the chain analyzed here.
* `N=3` and `N=4` complete-pair cases were enumerated in the
  non-interference audit. At `N=3`, disjoint conditional projections commute;
  the first crossing failure occurs at `N=4,l=4`.
* The inherited exact `N=6,l=3` rational witness already refutes coefficient
  `1/(l-1)` but not `A/l`. The new long-cycle family makes `l mu_l` diverge.
* The parity identity `Q=P_T^2` is respected: every product increment is even,
  and the long odd cycle `h_n` lies in `A_n`.
* Identity fixed-label and square modes remain valid finite calibrations; the
  witness here is a distinct frequency-two long-cycle mode.
* All endpoint cycle types through the inherited `N<=8` calculations are
  consistent. The proof is asymptotic and does not extrapolate from them.

## 8. Artifact paths and reproduction

Main proof and synthesis:

* `minimal_long_cycle_refutation.md`
* `checkpoint.md`
* `plan.md`

Principal commands:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature.py --n-values 7,9,11,13,15,17,19,21 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature_n21.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature.py --n-values 23,25,27,29,31,33,35,37,39,41,43,45,47,49,51 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/transposition_long_cycle_feature_n51.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/long_cycle_fourier_quotient.py --lengths 3,4,6,8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/long_cycle_fiber_witness_l8.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/geodesic_matching_spectrum.py --l-max 30 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/geodesic_matching_spectrum_l30.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_product_falsifier.py --N 4 --length 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/noninterference_product_N4_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_orbit_quotient.py --quotient pair-stabilizer --lengths 4,6,8,10,12,14 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M61-product-increment-resource-audit/matching_pair_stabilizer_l14.json
```

Each script records its parameters, Python version, and deterministic scope in
its JSON output. The finite calculations could falsify the moment constants,
orbit handling, and proposed quotient bounds; they are not the asymptotic
proof.

## 9. Verdict

**REFUTED**

The verdict applies exactly to universal PRODUCT-INCREMENT BASE CORRELATION
`mu_l(h)<=A/l`. Polynomial mixing of the complete-pair chain and of original
`K` remains open.
