# M73 theorem and exact reduction: the invariant coordinate-correlation block

Date: 2026-08-12.

## 1. Setup and conventions

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are read from
left to right.  Let

```text
n=2l+1,  l>=2,  h=(0 1 ... n-1),
Omega={ (t_1,...,t_(n-1)): each t_i is a transposition and
                              t_1...t_(n-1)=h }.
```

The law on `Omega` is uniform and `|Omega|=Z_n=n^(n-2)`.  Put
`G_i=t_(2i-1)t_(2i)` and

```text
theta(g)=h^(-1) g h.
```

The invariant one-coordinate space consists of functions `f` satisfying
`f(theta(g))=f(g)`.  This is the zero cyclic-frequency block called `H_0`
below.  This note concerns M16's coordinate-correlation/Gram operator, not a
Poincare gap for the full fixed-endpoint bridge.

For a permutation `q`, define

```text
F_r(q) = r! product_(cycles C of q, |C|>1)
                    |C|^(|C|-2) / (|C|-1)!             (1.1)
```

when the transposition length `ell_T(q)=r`, and `F_r(q)=0` otherwise.  Also
let

```text
a(g)=#{(u,v): u,v are transpositions and uv=g}.         (1.2)
```

Thus `a(g)=3` for a 3-cycle and `a(g)=2` for a product of two distinct
disjoint transpositions.

## 2. Proved exact orbit kernel

**Proposition 2.1 (proved).**  Let

```text
X={g: a(g)F_(n-3)(g^(-1)h)>0}.
```

Then `X` is the rank-two part of the absolute-order interval `[e,h]`: its
elements are the cyclically oriented 3-cycles and the noncrossing products
of two disjoint transpositions.  The product marginal and the ordered
two-coordinate joint law are

```text
pi(g) = a(g) F_(n-3)(g^(-1)h) / Z_n,                  (2.1)

J(g,s)= a(g)a(s) F_(n-5)((gs)^(-1)h) / Z_n.           (2.2)
```

Consequently the forward product-coordinate correlation kernel is

```text
K(g,s)=a(s)F_(n-5)((gs)^(-1)h)/F_(n-3)(g^(-1)h).      (2.3)
```

For a `theta`-orbit `O` and representative `g in O`, its exact invariant
restriction is

```text
bar pi(O)=|O|a(g)F_(n-3)(g^(-1)h)/Z_n,                (2.4)

bar K(O,O')=sum_(s in O')
       a(s)F_(n-5)((gs)^(-1)h)/F_(n-3)(g^(-1)h).      (2.5)
```

The right side of (2.5) is independent of the representative, every row
sums to one, and `bar K` is self-adjoint in `L^2(bar pi)`.

**Proof.**  If `q` has nontrivial cycle sizes `d_1,...,d_c`, a minimal
transposition factorization cannot join distinct cycles of `q`.  Dénes gives
`d_i^(d_i-2)` factorizations of each cycle; interleaving their
`d_i-1` factors gives (1.1).  Fixing one ordered pair-product `g`, including
its `a(g)` micro-lifts, leaves a minimal factorization of `g^(-1)h` of length
`n-3`, which proves (2.1).  Fixing two pair-products leaves the residual
`(gs)^(-1)h` and proves (2.2).  Equivalently, for nonadjacent pair positions
the same count follows because the pair-step group-algebra element
`(sum_t t)^2` is central.  Division proves (2.3), and summing a row over a
target orbit proves (2.5).

Conjugation by `h` preserves all counts.  The bridge rotation gives the
twisted pair symmetry

```text
J(g,s)=J(s,theta(g)).                                  (2.6)
```

Summing (2.6) over cyclic orbits makes the quotient joint law symmetric.
This proves exact reversibility.  The Python artifact independently checks
normalization and detailed balance over the rational numbers.  QED.

## 3. Proved lower bound on negative correlations

Let `v` be a mean-zero `theta`-invariant eigenfunction of `K`, normalized by
`E|v(G_1)|^2=1`, and write `Kv=kappa v`.  M16's normality identity gives
`K=K*` on this invariant block, so `kappa` is real.

**Proposition 3.1 (proved).**  Every such eigenvalue satisfies

```text
-1/(l-1) <= kappa <= 1.                               (3.1)
```

In particular, if `kappa_min` is the bottom invariant mean-zero eigenvalue,
the transverse branch of M16's coordinate Gram spectrum obeys

```text
(1-kappa_min)/l <= 1/(l-1).                           (3.2)
```

**Proof.**  The random variables `Y_i=v(G_i)` have diagonal covariance one.
For `i<j`, central two-position symmetry and the definition of `K` give
`E[conj(Y_i)Y_j]=kappa`; the reverse covariance is also `kappa` because it is
real.  Their `l` by `l` covariance matrix is therefore

```text
(1-kappa)I_l + kappa 11*.
```

It is positive semidefinite.  Its eigenvalues are `1-kappa`, with
multiplicity `l-1`, and `1+(l-1)kappa`, once, proving (3.1).  Substitution
gives (3.2).  QED.

This argument does **not** say that `K` is positive semidefinite.  `K` is a
cross-coordinate conditional-correlation operator and has negative
eigenvalues already at `n=5`.  It is the full `l`-coordinate covariance/Gram
matrix above that is positive semidefinite.

Let `kappa_+` be the largest mean-zero eigenvalue of `bar K`.  Including the
within-product microfiber eigenvalue `1/l`, M16's exact scalar blocks and
(3.2) give the proved reduction

```text
mu_l^(H0) <= max{ [1+(l-1)kappa_+]/l, 1/(l-1), 1/l }. (3.3)
```

Therefore `kappa_+<=A/l` implies

```text
mu_l^(H0) <= max{(1+A)/l,1/(l-1)}=O(1/l).             (3.4)
```

Only the positive correlation edge remains open.

## 4. Proved cyclic collision identities

Define the raw two-coordinate likelihood ratio

```text
R(g,s)=J(g,s)/(pi(g)pi(s))
      =Z_n F_(n-5)((gs)^(-1)h)
          /[F_(n-3)(g^(-1)h)F_(n-3)(s^(-1)h)],        (4.1)
```

and its cyclic phase average

```text
R_0(g,s)=n^(-1)sum_(r=0)^(n-1) R(g,theta^r(s)).       (4.2)
```

The value in (4.2) depends only on the two `theta`-orbits, including when an
orbit has a nontrivial stabilizer.  It is the quotient joint likelihood
`bar J/(bar pi tensor bar pi)`.

Put `L_0=bar K-Pi`, where `Pi f=bar pi(f)` is the constant projection.
For independent `G,S` with law `pi`, exact expansion gives

```text
Tr(L_0^2)=E[(R_0(G,S)-1)^2]                            (4.3)

 =n^(-1)sum_(d=0)^(n-1)
    E[(R(G,S)-1)(R(G,theta^d(S))-1)].                  (4.4)
```

Writing `A_g=F_(n-3)(g^(-1)h)` and
`B_(g,s)=F_(n-5)((gs)^(-1)h)`, this is the completely explicit completion
collision sum

```text
Tr(L_0^2)
 = n^(-1) sum_d sum_(g,s in X)
       a(g)a(s) B_(g,s)B_(g,theta^d(s))/(A_g A_s) - 1. (4.5)
```

**Proof.**  Equation (4.3) is the Hilbert--Schmidt identity for a reversible
finite kernel.  Expanding the square of (4.2), using the simultaneous
`theta` covariance of `R`, turns the two phase indices into their difference
and proves (4.4).  Substituting (2.1) and (4.1) cancels both copies of `Z_n`
and proves (4.5).  QED.

There is an equally explicit four-cycle identity.  For independent
`G_1,...,G_4` with law `pi` and `G_5=G_1`,

```text
Tr(L_0^4)=E product_(i=1)^4 [R_0(G_i,G_(i+1))-1].      (4.6)
```

Inserting (4.2) expands (4.6) into four cyclic phase sums and four completion
counts `B`; it is the eight-fixed-pair collision sum requested by the M70
bridge analysis.  More explicitly, because `L_0=bar K-Pi` and
`bar K Pi=Pi bar K=Pi`, it is

```text
Tr(L_0^4)=Tr(bar K^4)-1
 = n^(-4) sum_(r_1,...,r_4) sum_(g_1,...,g_4 in X)
       product_(i=1)^4
       [a(g_i)B_(g_i,theta^(r_i)(g_(i+1)))/A_(g_i)] - 1. (4.7)
```

No spectral approximation enters (4.3)--(4.7).

## 5. First unproved standalone lemma

Define the exact two-step quotient likelihood

```text
R_0^(2)(g,t)=E_(S~pi)[R_0(g,S)R_0(S,t)].              (5.1)
```

It is obtained from (4.1)--(4.2) using only one sum over an intermediate
rank-two product and two cyclic phases.

> **TWO-STEP CYCLIC COMPLETION SMOOTHING.**  There is an absolute constant
> `C` such that, for every `l>=3` and `g in X`,
>
> ```text
> E_(T~pi)|R_0^(2)(g,T)-1| <= C/l^2.                   (5.2)
> ```

This pointwise completion inequality immediately finishes the H0
coordinate-correlation step.  Indeed, `L_0^2=bar K^2-Pi`, and the left side
of (5.2) is exactly the absolute row sum of its signed kernel.  Hence

```text
rho(L_0)^2=rho(L_0^2)<=||L_0^2||_(infinity to infinity)<=C/l^2,
```

so every mean-zero invariant `|kappa|<=sqrt(C)/l`.  Proposition 3.1 and
(3.3) then give the desired `O(1/l)` coordinate-Gram bound.

Two other sufficient but currently less targeted statements are
`Tr(L_0^4)<=C/l^4`, using (4.7), and
`Tr(L_0^2)<=C/l^2`, using (4.5).  The latter may be too strong: the second
trace aggregates a growing number of very small modes, whereas (5.2) and
the fourth trace directly control the spectral edge.  No asymptotic claim
about `Tr(L_0^2)` is made here.

The completion weights in (4.5) are explicit rooted-tree weights.  If the
three cycles of `g^(-1)h` have sizes `d_1,d_2,d_3`, then

```text
A_g=(n-3)! product_i d_i^(d_i-1)/d_i!.                (5.2)
```

Thus (5.2) and (4.7) are finite weighted-composition inequalities, with no
hidden Markov-chain or lumpability assumption.  A direct termwise absolute bound is
not sufficient: the recorded phase diagnostic shows large signed
cancellation between cyclic separations.  At `n=9`, for example, the
`d=0` centered contribution is about `4.7617`, while their cyclic average is
only about `0.3302`.  A proof must perform the cyclic sum before estimating.

## 6. Exact finite calibration

The sparse kernels, characteristic polynomials, and rational root-isolating
intervals are exact.  Only the displayed decimals below are abbreviations.

```text
n  l  dim(H0)  kappa_min          kappa_+             mu_l^(H0)
5  2      4    -1                 1                    1
7  3     15    -0.421436329511     0.283844546680       0.522563031120
9  4     38    -0.259951817373     0.170053682321       0.377540261741
```

At `n=5`, the exact characteristic polynomial is `(x+1)(x-1)^3`; this is the
known `l=2` obstruction and is outside the proposed `l>=3` collision lemma.
At `n=7`, the factor degrees are `1,3,11`; at `n=9`, they are `1,11,26`.

The exact centered moments are

```text
n=7: Tr(L_0^2)=7931999329/11664000000,
     Tr(L_0^4)=9641667417737415673/136048896000000000000;
n=9: Tr(L_0^2)=9400228464753737917807/28466996869463040000000,
     Tr(L_0^4)=
       2216633222322833415970680638682183983299777409
       /182333229922354166914873033359360000000000000000.
```

Numerically, `l^2 Tr(L_0^2)` is `6.1204,5.2834` and
`l^4 Tr(L_0^4)` is `5.7404,3.1122` at `n=7,9`.  Floating diagnostics through
`n=21` keep `l kappa_+` between `0.624` and `0.852`, keep
`l^2 Tr(L_0^2)` between `4.99` and `6.13`, and decrease
`l^4 Tr(L_0^4)` from `5.74` to `1.42`.  These finite data support but do not
prove a moment bound.  The stronger pointwise diagnostic for (5.2) is exact
at the two smallest nonexceptional ranks:

```text
n=7: max_g E|R_0^(2)(g,T)-1| = 10656857/29172150,
     l^2 times this value = 3.2877834853;
n=9: max_g E|R_0^(2)(g,T)-1| = 804941560384/3987468253125,
     l^2 times this value = 3.2298852677.
```

Floating checks at `n=11,13,15,17` give the scaled values
`2.4909,2.3551,2.5561,2.2964`.  These support but do not prove (5.2).

## 7. Final sharpened reduction: adjacent shared-factor influence

The global pointwise lemma (5.2) remains sufficient, but it is no longer the
smallest open step.  Let `Gamma_n` be the graph on `theta`-orbits of
rank-two products in which two vertices are adjacent if representatives have
ordered transposition-pair lifts sharing their first raw transposition or
sharing their second.

**Proposition 7.1 (proved).**  `diam(Gamma_n)<=2` for every odd `n>=5`.

Choose lifts `(a,b)` and `(c,d)` of the two orbits.  Rotate the second lift
until `a theta^r(d)` is an admissible noncrossing rank-two prefix.  Such a
rotation always exists: put the shorter chord `theta^r(d)` strictly inside
the larger arc cut by `a`; in the sole extremal case where there is no room,
make the two chords share an endpoint in the admissible three-cycle
orientation.  The intermediate lift `(a,theta^r(d))` shares one factor with
each endpoint lift, proving the claim.  Full gap-coordinate details and the
exact four-schema kernel are in `gap_parameterization.md`.

The first unproved standalone lemma is now

> **SHARED-FACTOR TWO-STEP INFLUENCE.**  There is an absolute `C` such that
> for every adjacent `O,O'` in `Gamma_n`,
>
> ```text
> ||bar K^2(O,.)-bar K^2(O',.)||_TV <= C/n^2.         (7.1)
> ```

Proposition 7.1 would turn (7.1) into
`delta(bar K^2)<=2C/n^2`.  Since `bar K` is self-adjoint, every nonconstant
eigenvalue would satisfy `|kappa|<=sqrt(2C)/n=O(1/l)`.  Proposition 3.1 and
(3.3) would then prove the desired `O(1/l)` H0 coordinate-Gram bound.

Equivalently, `bar K^2` is the two-block data-augmentation kernel for the
exact symmetric quotient joint law `bar J`: sample the second rank-two
product conditional on the first, then resample the first conditional on the
second.  Thus (7.1) is a strong-data-processing/coupling inequality for two
posterior predictives whose source products share one raw factor.

Exact exhaustive calibration gives

```text
n  diam(Gamma_n)  max-adjacent TV       n^2 times TV
7       2          7185517/30375000       11.5914513
9       2          2094407996609/19603684800000  8.6538347
```

Floating checks through `n=21` keep the diameter two and the scaled adjacent
maximum between `6.72` and `7.36` for `n>=11`.  They prove no asymptotic
bound.

The stationary weights and all local row laws admit exact cyclic-composition
formulas.  Every row is a sum of four residual-forest schemas
`{I3,IS,IN,X}`, so its square is a signed sum of sixteen schema pairs.  The
cross-cycle first-edge law is exactly two independent critical Borel tree
sizes conditioned on their sum.  A naive small-tree coupling loses
`Theta(d^-1/2)` and is insufficient; (7.1) must couple the full two-step
posterior or preserve cancellation across schemas.

Finally, the apparently stable fixed moments are not promoted.  At `n=21`,
the positive contributions to `l^2 Tr(L_0^2)` grouped by minimum residual
size approximately follow a `1/k` profile.  The analogous fourth-moment
profile is weaker but visible.  This is finite numerical evidence only—not
a proof of logarithmic divergence—and is why (7.1), rather than a fixed
Schatten-moment bound, is the primary analytic target.
