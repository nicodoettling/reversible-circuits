# Repeated extreme contexts: exact weights and non-bottleneck calibration

Date: 2026-08-12.  This note analyzes the rightmost synthetic marked
family inside the minimal-long-cycle parking projection.  It neither proves
a gap lower bound nor gives a gap upper bound for the full chain.

## 1. Marked persistence

For `R=K-1`, marked inheritance remains exactly rightmost only on the
event `J=k`.  Its weight is

```text
nu_k=K/(K+k),
(K,R)->(K+k,K+k-1).                                 (1.1)
```

Along any sequence of inner root degrees `k_1,...,k_d`, the product of
these persistence weights telescopes:

```text
product_h K_(h-1)/(K_(h-1)+k_h)=K_0/K_d,
K_d=K_0+sum_h k_h.                                  (1.2)
```

Thus the positional mark alone suppresses a long history only
polynomially.  In particular one may not charge an arbitrary-context cost
only once.

## 2. Stationary deep-descendant law

There is, however, a separate stationary cost to continuing down a giant
last branch.  Take the limiting extreme conditional mean with `B=1` and
`K->infinity`.  For a composition whose last part is `t>1`,

```text
H_infinity(C)=w_(t-1)/w_t,
E H_infinity=m_s=w_s/w_(s+1).
```

Write `n=s-t` for the total size of the prefix before the last part.  Put

```text
A_n=sum_(p>=0) 1/(p+1)!
       sum_(a_1+...+a_p=n) product_i w_(a_i),
```

with the empty-prefix convention `A_0=1`.  Under the deep demand measure
`rho(C)H_infinity(C)/m_s`, the next local rank is `t-1=s-n-1` and

```text
P_s(prefix size=n)=A_n w_(s-n-1)/w_s,
                  0<=n<=s-2.                       (2.1)
```

This is exactly normalized.  Indeed, if

```text
T(z)=sum_(a>=1)w_a z^a=z exp(T(z)),
```

then

```text
A(z)=sum_n A_n z^n
    =sum_(p>=0)T(z)^p/(p+1)!
    =(exp(T(z))-1)/T(z),

A(z)T(z)=exp(T(z))-1=T(z)/z-1.                     (2.2)
```

Taking the coefficient of `z^(s-1)` in (2.2) gives
`sum_n A_n w_(s-n-1)=w_s`.

For each fixed `n`,

```text
w_(s-n-1)/w_s -> exp(-(n+1)).
```

At the dominant singular point `z=e^-1`, `T(z)=1`, so

```text
sum_(n>=0) A_n exp(-(n+1))
 =e^-1 A(e^-1)=1-e^-1.                             (2.3)
```

Thus the asymptotic mass which continues into a last branch of size
`s-O(1)` is `1-e^-1`, not one.  With asymptotic mass `e^-1`, the last
branch is not the condensed branch and the recursion drops to a much
smaller rank.

## 3. Exact unary corridor

The strict unary continuation has `n=0`, `k=1`.  Its stationary demand
weight at rank `q` is

```text
w_(q-1)/w_q,
```

and its marked persistence weight is `K/(K+1)`.  A depth-`d` unary
corridor therefore has the exact combined weight

```text
[K/(K+d)] [w_(s-d)/w_s].                           (3.1)
```

For `d` proportional to `s`, (3.1) is exponentially small in `s` by
Stirling's formula.  More generally, summing all depth-`d` prefix histories
gives the exact stationary factor

```text
(1/w_s) sum_N [z^N]A(z)^d w_(s-d-N),               (3.2)
```

and for fixed `d`, (3.2) tends `(1-e^-1)^d` as `s->infinity`.

## 4. Consequence for a proposed slow mode

The scalar coefficient `delta+a` has a uniform constant excess in the
same extreme family, but that fact alone is not a Rayleigh quotient or a
conductance bound.  A nested rightmost/unary corridor of linear depth has
exponentially small stationary demand mass by (3.1); a bottleneck based on
it still needs a nonnegligible side mass and exact full-chain boundary flow.
No such cut or Rayleigh test is obtained here.

The smallest surviving constructive statement is:

> **MARKED WEIGHTED CONTRACTION.**  In the full negative-hypergeometric
> recursion (2.2 of `marked_context_inheritance.md`), bound quotient
> residual energy after averaging over the exact descendant law (2.1),
> rather than taking the maximum over descendant ranks.  The combined
> marked/descendant operator must have polynomial Green growth, with actual
> edge source recovery retained.

The constant `1-e^-1` in (2.3) explains why a weighted proof may survive
even though every scalar absorption inequality considered in M56/M65 is
false.
