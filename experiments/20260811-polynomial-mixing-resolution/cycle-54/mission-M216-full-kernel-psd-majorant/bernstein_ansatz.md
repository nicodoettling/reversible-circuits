# M216 analytic ansatz before diagnostics

Date: 2026-08-13 UTC.

## Named family: degree-cap diagonal Bernstein PSD envelopes

For suffix excess `ell`, write

```text
b_(ell,j)(u)=binom(ell,j)u^j(1-u)^(ell-j),  0<=j<=ell,
J_zeta(u,v)=sum_(j=0)^ell c_(zeta,j)b_(ell,j)(u)b_(ell,j)(v),
c_(zeta,j)>=0.
```

This is a nonconstant finite-dimensional PSD kernel family. It is chosen
because Bernstein features multiply exactly:

```text
b_(d,a)(u)b_(ell,j)(u)
 =[binom(d,a)binom(ell,j)/binom(d+ell,a+j)]
   b_(d+ell,a+j)(u).
```

If the new degree `d+ell` saturates the parent's degree cap, the exact lift
remains diagonal in that cap (up to the exact `1/pi_a`). In an unsaturated
branch, `d+ell<L`, degree elevation writes the lifted feature as a positive
sum of degree-`L` Bernstein features and its outer product becomes
nondiagonal. Thus exact-degree diagonality is **not** literally closed under
every raw lift.

The named ansatz repairs this by the canonical positive-linear PSD envelope.
If `b_(n,k)=sum_j e_j b_(L,j)`, `e_j>=0`, then

```text
(e e^T) <=_PSD (sum_j e_j) diag(e).
```

This is weighted Cauchy--Schwarz. Applying it atom by atom after the exact
likelihood multiplication defines a positive-linear map back into the
degree-cap diagonal cone. Killed `a=d` is deleted before this operation.

## Supersolution certificate

The named envelope ansatz would prove the full-kernel lemma if coefficients
could be chosen recursively so that, for every reachable state,

```text
J_zeta >=_PSD R_zeta
  +sum_(live d,t)sum_(a<d) eta_(d,t)Lift[J_(zeta_a)],
```

and at each fresh parent

```text
Q_zeta[J_zeta] <= 1-q_zeta.
```

The first inequality contains a diagonal PSD envelope of the exact reset
boundary and the positive-linear envelope of every exact lift. It implies
`K_zeta<=_PSD J_zeta` inductively. The residual is affine antitone, so the
second inequality then proves the desired budget.

## Decisive necessary test

Let `A_zeta` be the coefficient matrix of the exact actual kernel `K_zeta`
in the degree-`ell` Bernstein basis. Any diagonal-Bernstein supersolution at
that state necessarily has

```text
diag(c_zeta)-A_zeta >=_PSD 0.
```

Therefore the exact semidefinite lower bound

```text
min sum_j c_j Q_zeta[b_(ell,j) tensor b_(ell,j)]
subject to diag(c)-A_zeta >=_PSD 0
```

is a necessary budget cost. A rational dual feasible matrix with objective
larger than `1-q_zeta` gives an analytic obstruction to every degree-cap
diagonal Bernstein envelope, regardless of which positive-linear elevation
or reset envelope produced its coefficients.

Only after this formulation were compact fresh rows through `L<=6`
inspected to locate a decisive exact certificate. No claim is made about the
larger cone containing diagonal Bernstein atoms of all degrees simultaneously;
that cone is outside this obstruction.
