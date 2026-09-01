# Exact additive-flow recurrence and its first missing coefficient

Date: 2026-08-11.  This note uses the full nonlazy parking projection
`Pbar_s`, its stationary law `pi_s`, and

```text
alpha_s=2/[3s(s-1)].
```

It concerns only the minimal long-cycle sector, not the original identity
bridge chain `K`.

## 1. A contextual demand and its root filtration

Fix one contextual suffix-cut observable supplied by the universal locality
theorem, and normalize it as

```text
f=alpha_s phi >=0,       q=E_(pi_s) f.
```

The fixed suffix size is `B`.  For a root composition
`C=(c_1,...,c_k)`, put `h(C)=E[f|C]` and split the composition space into

```text
Z={C:c_k<B},  T={C:c_k=B},  D={C:c_k>B}.
```

Recursive contextual locality proves:

- `f=0` on every `Z` fibre;
- `f=h(C)` is constant on every `T` fibre;
- on a `D` fibre, `f` depends only on the standardized last-branch
  macro and is another contextual suffix-cut observable.

Define the exact deep-continuation fraction

```text
delta(f)=E[f 1_D]/q.                                 (1.1)
```

## 2. Telescoping of the internal recursive demand

Fix `C in D`, let `t=c_k-1<s` be the number of internal edges in its
last branch, and write the induced lower-rank contextual observable as
`f_t=alpha_t phi_t`.  The constrained-shuffle normalization and the
product restriction give the same coefficient

```text
gamma_(s,t)=t(t-1)/[s(s-1)]=alpha_s/alpha_t,
f=gamma_(s,t) f_t,
E_C=gamma_(s,t) E_(Pbar_t)+other nonnegative coordinates.   (2.1)
```

Suppose a lower-rank flow routes
`pi_t(f_t-Ef_t)` with energy at most `T_t E f_t`.  Scale that flow by
`gamma_(s,t)` and embed it in the last coordinate.  Its demand is exactly
`pi(.|C)(f-h(C))), while its conditional energy is

```text
gamma_(s,t)^2/[gamma_(s,t)] T_t E f_t
 =T_t h(C).                                         (2.2)
```

After multiplying by `rho_s(C)` and summing over `D`, all internal
recursive demands therefore cost at most

```text
delta(f) q max_(t<s) T_t.                           (2.3)
```

There is no Radon--Nikodym loss in (2.3).  Along active sizes
`s=s_0>s_1>...>s_j`, both the demand and capacity coefficients telescope:

```text
product_i gamma_(s_(i-1),s_i)
 =s_j(s_j-1)/[s(s-1)]=alpha_s/alpha_(s_j).          (2.4)
```

## 3. Exact quotient disintegration coefficient

Let `R_s` be the accepted stationary-flow root-composition quotient and
`Q_R(C,C')=rho_s(C)R_s(C,C')`.  Route the mean charge

```text
rho_s(C)(h(C)-q)
```

by a quotient electrical flow `theta`.  Put

```text
a(f)=(1/q) sum_e theta_e^2/Q_R(e)
    =||h-q||_(-1,R_s)^2/q.                          (3.1)
```

For one quotient edge `e=(A,B)`, disintegrate `theta_e` over the actual
fine crossing edges in proportion to stationary flow.  If `A` is the
refined composition and `B` the coarse one, the fixed merge boundary has
constant pointwise rate on `A`.  Thus the refined endpoint is exactly
`pi(.|A)`.  At a coarse state `x`, the endpoint density is

```text
p_e(x)/q_e,   p_e(x)=Pbar_s(x,F_A),
q_e=E_(pi(.|B))p_e,
```

and the residual fine demand is exactly

```text
theta_e pi(x|B)[p_e(x)/q_e-1].                      (3.2)
```

The contextual locality and norm-cancellation theorem turns (3.2) into a
strictly lower-rank contextual demand.  If its normalized flow cost is at
most `T_<s`, scaling its base flow gives energy exactly

```text
T_<s theta_e^2/Q_R(e).                              (3.3)
```

Hence, in the marked network in which residual commodities belonging to
different quotient edges have separate capacity copies, (2.3) and
(3.1)--(3.3) give the exact recurrence

```text
T_s(f) <= a(f)+[delta(f)+a(f)] max_(t<s)T_t.         (3.4)
```

This derivation retains all factors `rho(B)`, `q_e`, `gamma`, and
`alpha`; in particular, (3.3) is neither `T theta_e/q_e` nor
`T theta_e^2/q_e^2`.

## 4. The sufficient scalar absorption inequality

The scalar estimate

```text
a(f)<=1-delta(f)                                    (4.1)
```

would make the recursive coefficient in (3.4) at most one.  If the marked
commodities can also be projected to actual capacities without a
multiplicative collision loss, then

```text
T_s<=1+max_(t<s)T_t<=s.                             (4.2)
```

Thus every individual split coefficient would be at most `s`; summing
over at most `r` one-split refinements would prove M54's H-minus bound
with a fixed polynomial.  M41 Section 11 and M50's balanced induction would
then give an inverse-polynomial gap for the full parking projection.

The exact scalar proposition is:

> **CONTEXTUAL QUOTIENT ABSORPTION.**  For every contextual suffix-cut
> observable produced by constrained-shuffle disintegration,
> ```text
> ||E[f|root composition]-Ef||_(-1,R_s)^2
>   <= E[f 1_{last root branch size = B}].
> ```
> The right side equals `q(1-delta(f))` because the observable vanishes
> when the last branch is smaller than `B`.

This has not been proved.  Applying only the accepted quotient gap gives
`a(f)<=3e Var(h)/q`, which does not compare sharply enough with the
terminal mass and would multiply a constant once per spine depth.

## 5. The separate capacity-collision obligation

Even (4.1) is not alone sufficient.  Equations (3.3)--(3.4) add the
energies of edge-labelled residual commodities.  In the actual unmarked
chain, recursively routed commodities can share an internal edge.  The
inequality

```text
(sum_j F_j(e))^2/Q(e) <= sum_j F_j(e)^2/Q(e)
```

is false without cancellation or disjointness.  A crude Cauchy bound by
the number of contexts introduces a factor as large as `s` at every
depth and destroys (4.2).

The exact remaining flow proposition is therefore:

> **MARKED ADDITIVE SOURCE RECOVERY.**  Choose the quotient flows and their
> recursively disintegrated contextual flows so that each actual fine edge
> can recover its active-depth/root-boundary history with total squared
> load bounded by the right side of (3.4), up to one universal polynomial
> added over all depths, not multiplied at every depth.

Root-composition martingale differences at different active depths use
rotations at different vertices, so a depth mark is a plausible recovery
key.  No universal injection or fractional collision bound has yet been
proved.

## 6. Exact bounded falsification

`contextual_macro_energy.py` computes `a(f)`, `delta(f)`, and their
sum for every ambient split context through `r=7`.  There is no quotient
nullspace failure.  The largest observed values of
`delta(f)+a(f)` are

```text
ambient r       3        4        5        6        7
maximum       .5278    .6667    .7569    .8178    .8634
```

(the last displayed decimal is rounded upward; the stored value is about
`.8633184`).  The largest observed ratio
`a(f)/(1-delta(f))` is about `.382884`.  Thus (4.1) survives this
bounded falsifier with slack.  These floating electrical solves are finite
diagnostics only; they prove neither (4.1) nor the source-recovery claim.

The smallest open implication is CONTEXTUAL QUOTIENT ABSORPTION.  After it,
MARKED ADDITIVE SOURCE RECOVERY is still required before (4.2) is a proof
for the actual chain.
