# Exact refutation of contextual quotient absorption

Date: 2026-08-12.  This is an auxiliary result for the nonlazy
minimal-long-cycle parking projection.  It is not a statement about the
identity-bridge chain `K` and is not a global terminal outcome.

## 1. Feasible infinite family

For every integer `K>=1`, take ambient rank `r=K+2`, outer coarse root
composition

```text
b=(3,1,...,1)                 (K parts),
```

and split its leftmost branch as `3=2+1`.  Thus the selected local rank is
`s=2`, the suffix is `B=1`, and the number of outer branches to the right
is `R=K-1`.  This is a genuine contextual split in the accepted M50/M56
decomposition.

The two inner root compositions, their stationary probabilities, and the
normalized quotient rates `G_2=R_2/alpha_2` are

```text
C              (2)       (1,1)
rho(C)          2/3        1/3

G_2((2),(1,1))=1,          G_2((1,1),(2))=2.        (1.1)
```

The closed contextual formula gives

```text
H((2))   =K/(K+1),
H((1,1))=2/(K+1).                                  (1.2)
```

Indeed the first state is deep and has
`D_(K,K-1)(1)=1-1/(K+1)`, while the second is terminal and has

```text
T_(K,K-1)(2)=K/binom(K+1,K-1)=2/(K+1).
```

## 2. Exact dual norm

Equation (1.1) is a reversible two-state generator with nonzero
eigenvalue `3`.  Therefore

```text
E H=2/3,

Var_rho(H)=2(K-2)^2/[9(K+1)^2],

||H-EH||_(-1,G_2)^2
 =Var_rho(H)/3
 =2(K-2)^2/[27(K+1)^2].                            (2.1)
```

Only `(1,1)` has last part `B`, so the proposed absorbing budget is

```text
E[H 1_(last=B)]=2/[3(K+1)].                         (2.2)
```

Dividing (2.1) by (2.2) gives

```text
(K-2)^2/[9(K+1)].                                   (2.3)
```

This exceeds one exactly when `K^2-13K-5>0`, hence for every integer
`K>=14`.  The first failure, `K=14` (ambient rank `r=16`), has ratio
`16/15`.

Equivalently, in the notation of M56's marked recurrence,

```text
delta=K/(K+1),
a=(K-2)^2/[9(K+1)^2],
delta+a -> 10/9.                                    (2.4)
```

At the first failure `delta+a=226/225`.

## 3. Exact scope and surviving proposition

Equations (2.1)--(2.3) rigorously **refute CONTEXTUAL QUOTIENT
ABSORPTION** as stated in M56.  They also refute any uniform recurrence
claim requiring `delta+a<=1` context by context.

They do not refute a polynomial flow or gap.  In this family the only deep
composition is `(2)`, whose last branch has one internal edge; the excess
coefficient therefore feeds directly into the rank-one base case rather
than recurring through a long active spine.

The smallest surviving constructive proposition is:

> **SIZE-AWARE CONTEXTUAL ABSORPTION.**  For every contextual mean at
> local rank `s`, bound the deep residual by its actual descendant rank
> and prove an additive polynomial recurrence in which coefficients above
> one can only occur on branches whose remaining recursive depth or
> accumulated Green cost is correspondingly small.

A sufficient scalar surrogate would be a universal
`delta+a<=1+O(1/s)` together with a depth-weighted potential whose decrease
absorbs the `O(1/s)` excess.  The family above is compatible with that
surrogate because its local rank is fixed at two, but does not prove it.
