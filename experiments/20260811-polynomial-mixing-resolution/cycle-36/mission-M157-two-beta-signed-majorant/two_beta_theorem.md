# M157 exact two-beta signed-current representation

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the normalized full unweighted reset excursion
`F=H/q` of the auxiliary nonlazy minimal-long-cycle parking projection.  The
project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.

The results are:

1. a proved shared-observation two-posterior transfer identity, including the
   killed attachment atom;
2. a proved finite exact two-copy kernel recursion for `F` which retains all
   signed cross-beta reset cancellation;
3. an exact pointwise sign obstruction to a nonnegative-kernel induction; and
4. an exact fresh right-heavy counterexample to the natural diagonal-trace
   positive majorant.

The exact representation is useful bookkeeping but does not prove the
right-heavy contraction.  No auxiliary gap, `ROOT-MEAN LIFT`, original-chain
gap, polynomial mixing result, Terminal A, or Terminal B is claimed.

## 2. Shared-X posterior transfer

Fix `1<=D<kappa`, degree `d>=1`, and let

```text
mu=Beta(D,kappa-D),
L_x(u)=binom(d,x)u^x(1-u)^(d-x),
p_x=integral L_x dmu.
```

Thus `p_x` is the accepted beta-binomial attachment probability and the
posterior after observing `X=x` is

```text
mu_x=Beta(D+x,kappa-D+d-x),
dmu_x/dmu=L_x/p_x.                                  (2.1)
```

Let `K_x` be any integrable kernel for the child state.  If two posterior
copies share the same attachment observation `X=x`, Bayes' rule gives the
exact identity

```text
p_x integral integral K_x(u,v) mu_x(du)mu_x(dv)
 =integral integral K_x(u,v)
    [L_x(u)L_x(v)/p_x] mu(du)mu(dv).                (2.2)
```

Consequently the retained transfer for one fixed child kernel `K` is

```text
T_ret^(kappa,D,d)(u,v)
 =sum_(x=0)^(d-1) L_x(u)L_x(v)/p_x.                (2.3)
```

The removed branch is exactly

```text
T_kill^(kappa,D,d)(u,v)
 =L_d(u)L_d(v)/p_d.                                (2.4)
```

In particular, its `mu tensor mu` mass is `p_d`, while (2.3) has mass
`1-p_d`.  Nothing is conditioned on survival and no atom is omitted.

Unlike M152's one-copy Doob multiplier `1-u^d`, (2.3) depends on the current
beta law through every denominator `p_x`.  This dependence is already
visible for `d=1`, where

```text
T_ret(u,v)=(1-u)(1-v)/p_0,
p_0=(kappa-D)/kappa.
```

The coefficient is `2` at `(kappa,D)=(2,1)` and `3/2` at `(3,1)`.  Hence
there is no state-independent two-variable transfer polynomial.

## 3. Exact signed reset kernel

For each active canonical endpoint `E`, use M152's point current

```text
J_E(u)=sum_(C in B_E)rho(C)[g_C(u)-q],
c_E=degree(E)rho(E).
```

The exact reset energy, not a Jensen bound, is

```text
A_0/q
 =sum_E [integral J_E dmu]^2/(q c_E)
 =integral integral R_(B,L)(u,v) mu(du)mu(dv),      (3.1)

R_(B,L)(u,v)=sum_E J_E(u)J_E(v)/(q c_E).           (3.2)
```

This preserves cross-beta cancellation.  The kernel is positive
semidefinite in the quadratic-form sense because it is a sum of rank-one
features, but it is not pointwise nonnegative.

The first exact sign witness in the capped order occurs at `B=1,L=2`, so
`s=3`.  Direct expansion gives

```text
R(u,v)=193/1536-(u+v)/4-19(u^2+v^2)/96
       +(2/3)uv+(u^2v+uv^2)/3+(u^2v^2)/3,

R(0,1)=-165/512.                                  (3.3)
```

This does not contradict PSD: a covariance-type kernel may be negative
off-diagonal.

## 4. Finite exact kernel recursion

For a valid state `x=(B,L,kappa,D)`, define recursively

```text
K_x(u,v)=R_(B,L)(u,v)
 +sum_(h,d) mbar_(L,B)(h,d) q_(B,h-1)
    sum_(a=0)^(d-1)
      [L_a(u)L_a(v)/p_a]
      K_(B,h-1,kappa+d,D+a)(u,v),                 (4.1)
```

with the same active-boundary indicator as M147/M151.  Every child has
smaller suffix excess, so (4.1) is finite.  Applying (2.2) to every child and
(3.1) to the reset proves by induction

```text
F_(B,L)(kappa,D)
 =integral integral K_x(u,v)mu(du)mu(dv).          (4.2)
```

Each transfer multiplier in (4.1) is a nonnegative rank-one kernel.  Since
the base reset kernel is PSD, induction also shows `K_x` is PSD.  Equivalently
the recursion expands into the exact signed-current history squares already
foreshadowed by M123/M128, now represented against two beta copies.  This is
an exact equality, not a Bessel or positivity estimate.

At `(s,kappa,D,B)=(3,2,1,1)` every likelihood product
`L_a(0)L_a(1)` vanishes: a binomial count cannot have positive likelihood at
both endpoints.  Thus every descendant transfer vanishes at `(0,1)`, and

```text
K_x(0,1)=R(0,1)=-165/512.                          (4.3)
```

So no proof which requires the exact kernel itself to be pointwise
nonnegative can start even in this smallest nontrivial case.

## 5. Why the equality is not yet a contraction theorem

Equation (4.2) exactly reproduces the nilpotent recurrence in a different
coordinate system.  The state-dependent denominators `p_a` prevent closure
by one fixed bivariate polynomial, and PSD does not bound the expectation of
`K_x(U,V)` by the right-heavy budget.  A new inequality specialized to the
actual history-current features is still required.

There are two obvious positive repairs; both fail as uniform certificates.

### Pointwise polarization

At each reset feature, before propagating through the child posterior, use

```text
F_z(u)F_z(v)<=[F_z(u)^2+F_z(v)^2]/2.
```

Applying this locally at every reset and then using the one-copy retained
posterior identity is exactly the Jensen Bellman lift of M152, not a sharper
route.  It reproduces the accepted failure at

```text
(s,kappa,D,B)=(9,2,1,3),
value approximately .89851925 > 1-q approximately .87293908.
```

### Actual-kernel diagonal trace

Instead assemble the full exact history kernel first.  Because `K_x` is a
sum of rank-one kernels, its product-beta expectation obeys

```text
integral integral K_x dmu dmu
 <=integral K_x(u,u)mu(du).                        (5.1)
```

This is a valid inequality for the actual contextual/history kernel.  It is
not the universal canonical-basin Bessel inequality refuted by M123/M128.
Nevertheless it first fails in the capped fresh right-heavy grid at

```text
(s,kappa,D,B)=(8,2,1,2), L=6,

integral K_x(u,u)dmu
 =10304304880412164262179965176912695056497059
  /12663621893778357952841743000389707366400000
 approximately .8136933467,

1-q=3841777/4782969 approximately .8032201338.
```

The positive excess is exactly

```text
132628808872888410508233058471582685297059
/12663621893778357952841743000389707366400000.
```

The true value is only about `.4386703515`, with positive budget slack about
`.3645497823`.  Hence the failure is again looseness of a positive repair,
not failure of contraction.

## 6. Relation to the M123/M128 frame obstruction

M123/M128 refute a universal ambient canonical-basin analysis-frame bound,
including centered supplements.  No such bound is assumed here.  Equations
(2.2)--(4.2) are exact algebraic equalities for the actual contextual
currents.  The diagonal inequality (5.1) uses only the explicitly constructed
actual-history feature decomposition, and its exact fresh counterexample is
therefore logically independent of the ambient frame obstruction.

The common lesson is narrower: retaining signed cross-copy cancellation is
essential, but discarding it by a generic positive square/trace domination
is too loose.  A future route needs an off-diagonal cancellation inequality
specialized to the beta law and the reachable history features.

## 7. Exact diagnostics and remaining lemma

The standalone exact checker, capped at `B<=3,L<=6,kappa<=16`, verifies:

- 51,840 monomial instances of the shared-X posterior identity;
- 720 retained/killed transfer-mass identities;
- 2,520 exact two-copy reset identities;
- seven exact full-kernel recursion identities, including the M152 witness;
- the exact sign witness (3.3), the first capped trace failure above, and
  all 21 fresh right-heavy target values through `L=6`.

All checks pass.  The 21 target passes are finite diagnostics only; the
accepted M145/M149 theorem is the reason `L<=6` right-heavy contraction is
known uniformly.

The first open standalone lemma is:

> Prove an off-diagonal cancellation inequality for the recursively generated
> PSD kernels `K_(B,L,kappa,1)` which bounds their product-beta expectation by
> `1-q_(B,L)` without replacing the kernel by its pointwise polarization,
> diagonal trace, positive part, absolute value, or a universal ambient basin
> frame.  The inequality must accommodate the state-dependent shared-X
> transfer denominators and must retain the killed `x=d` term exactly.
