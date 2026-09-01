# Halfway checkpoint: coverage threshold lowered by a factor eight

## New scoped theorem

Let `A>=1` be the audited parity-aware pointwise return constant, let

```text
B_*=32(A+1)=C_*/8,
```

and use natural logarithms.  For `N>=3`, even `m`, and

```text
m-2>=B_*N log(N+1),                                   (C.1)
```

the current proof gives, simultaneously for every `1<=q<=N-2`,

```text
Phi_pm^K({X>=q})
>=q/[8(N-q-1)(m-2)D_N]
>=1/(16mN^3),
D_N=(3N^2+N-12)/2.                                    (C.2)
```

This is not a restatement of M21: it proves the entire factor-eight interval

```text
2+B_*N log(N+1)<=m<2+C_*N log(N+1),                   (C.3)
```

which has growing surplus and was outside M21.

## New pointwise-to-support lemma

Let `delta_n(j)` be the probability that the factorization graph is
disconnected under a length-`j` identity bridge on `S_n`.  The new estimate
is

```text
delta_n(j)<1/4                                        (C.4)
```

for every `n>=3` and even `j>=B_*n log(n+1)`.

For a vertex cut with smaller side `q`, put `b=n-q`,
`M=binom(n,2)`, and

```text
L=binom(q,2)+binom(b,2)=M-qb,
alpha=binom(b,2)/L>=1/2.
```

The unconditioned probability of using no crossing edge is `(L/M)^j`.
Conditional on that event, the number `J` of steps in the larger factor is
`Bin(j,alpha)`.  Since

```text
A b log(b+1)<=E[J]/2,
```

Chernoff gives

```text
Pr[J<A b log(b+1)]<=exp(-j/16).                       (C.5)
```

Odd `J` has zero return probability; at a large even `J`, the audited
pointwise estimate bounds it by `3/b!`.  Keeping the small-factor return at
most one, dividing by the full even return lower bound `2/n!`, and unioning
all cuts gives

```text
delta_n(j)
 <=(3/2)sum_(q=1)^[floor(n/2)]
       [e n^2 exp(-j/n)]^q
   +2^(n-1)n!exp(-j/16).                              (C.6)
```

With `R=e n^2(n+1)^(-B_*)`, the first term is at most `3R<1/8`.
Also

```text
2^(n-1)n!exp(-j/16)
 <=(n+1)^[-(B_*/16-2)n]
 <=4^-6<1/8,                                          (C.7)
```

because `B_*>=64`.  This proves (C.4) without losing an unexplained
factorial at the subgroup return.

## Exact overlap and full-K flow

For `T_q={X>=q}`, exact factorial moments still give

```text
mu_q=E[binom(X,q)]=binom(N,q)Z_(N-q,m)/Z_(N,m).
```

The same pointwise return estimate yields

```text
mu_(q+1)/mu_q
 <=3d^2 exp(-2m/d)/[2(q+1)]
 <=1/[2(q+1)],   d=N-q.
```

Thus `pi(X=q)>=pi(T_q)/2`.  Equation (C.4) gives
`pi(T_q)<=pi(U)<1/4`, so the orientation is exact.  Applied at degree `d`
and length `m-2`, it also makes the exact safe-square incidence at least
`3/[4binom(d,2)]`.  A boundary-safe `H_3` refresh has `qd` distinct crossing
outcomes and exact probability `qd/[6(m-2)D_N]`.  Their product proves
(C.2); the `r=4,5` stationary flows remain present and nonnegative.

## Remaining red-team frontier

No superpolynomial cut emerged.  The exact remaining support-coverage
question is below `B_*N log(N+1)`.  The proof of (C.4) only fails there as a
sufficient estimate; that failure is not evidence of a bottleneck.
