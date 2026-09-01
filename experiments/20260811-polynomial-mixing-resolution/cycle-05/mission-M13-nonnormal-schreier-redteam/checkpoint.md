# Halfway checkpoint: minimal-full-support and first-join cuts

## Analytic result surviving self-audit

Let `m=2N-2`, `M=binom(N,2)`, `B=|R_m|`, and let `F_N` be the
global identity words whose factorization graph is connected on all `N`
labels.  The exact count is

```text
|F_N|=(2N-2)! N^(N-3).
```

Mark an adjacent square `(uv),(uv)` when `v` occurs nowhere else and
deleting the pair leaves a connected minimal identity word on the other
`N-1` labels.  Inserting such a pair gives a bijection with

```text
(v,u,gap,base word) in
[N] x ([N]\{v}) x [2N-3 gaps] x F_(N-1).
```

If `Z` is the number of marks in a uniform state of `F_N`, then

```text
E Z
 = N(N-1)(2N-3)|F_(N-1)|/|F_N|
 = (1/2)(1-1/N)^(N-4)
 >= 1/8.
```

One omitted label gives at most one mark, so `Z<=N` and
`Pr(Z>=1)>=1/(8N)`.

For a marked pair beginning before the last position, use the length-three
window `(e,e,a)` and replace it by `(f,f,a)`; at the last pair use
`(a,e,e)->(a,f,f)`.  Here `f` is any edge avoiding the omitted label.
The exact block product is unchanged and the output has support on only
`N-1` labels.  Since a three-factor conditional fiber has at most `M^2`
elements, a specified exit has probability at least

```text
q=1/[2B(m-2)M^2].
```

Therefore the original chain, not a restriction, satisfies

```text
Q_K(F_N,F_N^c)
 >= pi(F_N)/[16BN(m-2)M^2],
Phi_pm(F_N)
 >= 1/[16BN(m-2)M^2].
```

This rejects the entire minimal-full-support macro as a superpolynomial
bottleneck.  Its exact global stationary mass is

```text
pi(F_N)
 = (2N-2)!N^(N-3)
   / [(1/N!) sum_{lambda partition N}(f^lambda)^2 c_lambda^(2N-2)],
```

where `c_lambda` is the sum of Young-diagram contents.  The mass need not be
oriented because `min(pi(F_N),1-pi(F_N))<=pi(F_N)`.

## Secondary nonnormal visible coordinate

For any even `m>=4`, fix a label `v` and let
`A_v={w:t_1` is incident to `v}`.  Global conjugation gives
`pi(A_v)=2/N`.  If `a=t_1` and `b=t_2`, one exact length-three output
leaves `A_v`:

- if `b` avoids `v`, use the right Hurwitz move;
- if `a,b` are distinct star edges, use the inverse Hurwitz move, whose
  first edge joins their two non-`v` endpoints;
- if `a=b`, replace `(a,a,t_3)` by `(f,f,t_3)` for an edge `f`
  avoiding `v`.

Thus `Phi_pm(A_v)>=q`.  In the minimal full-support orbit this is the star
cut on the first join-tree edge.

## Exact falsification

The deterministic full-kernel verifier enumerates every `r=3,4,5`
contribution and both directed flows.

- `S_3,m=4`: `|Omega|=27`, `pi(F_3)=8/9`,
  `Phi_pm(F_3)=4/9); marked-square expectation `3/4`.
- `S_4,m=4`: `|Omega|=120); the first-join star cut has
  `pi=1/2`, `Phi=37/200`; the whole-word `H_4` contribution is included.
- `S_4,m=6`: `|Omega|=3936`, `pi(F_4)=30/41`,
  `Phi_pm(F_4)=298449/938080); marked-square expectation `1/2`.
  The `r=3,4,5` boundary contributions are all positive and exact.

No terminal cut has emerged.  The remaining sharp proposition is polynomial
embedded expansion for every subset of the nonnormal Hurwitz orbit `F_N);
normal quotient triviality and polynomial diameter do not control its
stationary edge congestion.
