# M15 halfway checkpoint

Date: 2026-08-11  
Commit audited: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

All statements below use `(pq)(x)=p(q(x))` and displayed word order
`t_1...t_m`.  Gaps are Poincare constants
`inf_{Var_pi f>0} E_P(f,f)/Var_pi(f)`.  For the explicitly lazy reversible
kernel `K` this is `1-lambda_2(K)` and all eigenvalues lie in `[0,1]`.

## C-1. A separate mean-lift estimate is not needed with standard restrictions

**Status: proved by direct application of a checked primary theorem.**

Primary source: M. Jerrum, J.-B. Son, P. Tetali, and E. Vigoda,
"Elementary bounds on Poincare and log-Sobolev constants for decomposable
Markov chains," *Annals of Applied Probability* 14 (2004), 1741--1765,
Theorem 1, equations (3)--(5), DOI
[`10.1214/105051604000000639`](https://doi.org/10.1214/105051604000000639),
[arXiv:math/0503537](https://arxiv.org/abs/math/0503537).

Let the nonempty fibers of the macro map be `Omega_a`.  Define exactly

```
bar_pi(a) = sum_{x in Omega_a} pi(x),
bar_K(a,b) = bar_pi(a)^(-1)
             sum_{x in Omega_a,y in Omega_b} pi(x)K(x,y).
```

For each fiber, the JSTV **restriction** is

```
K_a(x,y) = K(x,y)                                      (x != y in Omega_a),
K_a(x,x) = 1 - sum_{y in Omega_a, y != x} K(x,y)
           = K(x,x) + K(x, Omega \ Omega_a).
```

Thus every off-fiber transition is rejected into the diagonal.  It is not
deleted and the remaining moves are not renormalized.  The stationary laws
are `bar_pi` and `pi(. | Omega_a)`.

Write `bar_lambda=gap(bar_K)`,
`lambda_min=min_a gap(K_a)`, and

```
gamma = max_a max_{x in Omega_a} K(x, Omega \ Omega_a).
```

JSTV Theorem 1 states, for a finite reversible chain whose projection and
restrictions have the displayed positive Poincare constants,

```
gap(K) >= min{bar_lambda/3,
              bar_lambda*lambda_min/(3*gamma+bar_lambda)}.       (C-1)
```

No pointwise regularity of inter-fiber flow and no mean-lift hypothesis occurs
in this theorem.  Since `gamma<=1`, and since the lazy projection and lazy
restrictions have gaps at most one, (C-1) gives the generic corollary

```
gap(K) >= bar_lambda*lambda_min/4.                              (C-2)
```

Indeed, the first term in (C-1) is at least the product divided by three,
while `3*gamma+bar_lambda<=4`.  For the exact kernel under review the explicit
half-hold gives the sharper `gamma<=1/2`; hence
`3*gamma+bar_lambda<=5/2`, both terms in (C-1) are at least the product divided
by three, and

```
gap(K) >= bar_lambda*lambda_min/3.                              (C-3)
```

Consequently inverse-polynomial gaps for the stationary-flow projection and
the **rejected-exit restrictions** suffice for TERMINAL A (once the global
irreducibility dependency is closed).  With inverse gaps `q_proj,q_fib`, the
loss is at most `3 q_proj q_fib`; there is no third `q_lift` factor.

### Normalization audit and self-attack

The current manuscript says "restricted-fiber Poincare inequality" but does
not define its transition matrix.  Therefore C-1 is a correction/clarification,
not yet a literal citation for whatever kernels M04/M05 may choose.  If a
fiber analysis conditions on the selected update staying in the fiber, or
renormalizes only macro-preserving moves to total mass one, its gap cannot be
inserted as `lambda_min`.  A separate Dirichlet comparison must restore the
possibly state-dependent action rate.  In the actual restriction, an update
of length `r` at position `i` retains its full-chain selection weight

```
1 / (2 |R_m| (m-r+1)),
```

and every outcome outside the fiber contributes holding probability.

Zero projection edges cause no singularity: JSTV's proof only defines its
edge-conditioned distributions when `bar_K(a,b)>0`.  But if the entire
projection is reducible then `bar_lambda=0`, and if any restriction is
reducible then `lambda_min=0`; C-1 then proves nothing.  Global irreducibility
implies projection irreducibility, but does not by itself imply irreducibility
of every rejected-exit restriction.  Those are still genuine obligations.
The bound `gamma<=1/2` uses the exact explicit laziness and is valid even when
all nonlazy mass exits a fiber.

## C-2. Whole-word boundary cases

**Status: proved.**  Each heat bath is an orthogonal conditional-expectation
projection, so every `I-H_{i,r}` is positive semidefinite.  For `m=4`,
`R_m={3,4}` and the whole-word projection `H_{1,4}` occurs in `I-K` with
coefficient `1/4`.  On mean-zero functions it is the identity, whence

```
gap(K_{N,4}) >= 1/4                 for every N>=3.
```

For `m=5`, `R_m={3,4,5}` and the same argument with `H_{1,5}` gives
`gap(K_{N,5})>=1/6`; the identity bridge is empty for odd `m`, so this is only
an algebraic parity check, not a principal-regime claim.  Thus every admissible
`m=4` case is quantitatively settled independently of support geometry.

## C-3. Independent parity-block bridge route

**Status: exact reduction proved; bridge gap open.**

Put `m=2n` and pair the letters:
`Y_j=t_{2j-1}t_{2j}`.  If `P_N` is the uniform transposition measure and
`Q_N=P_N*P_N` on `A_N`, the uniform measure on `Omega(N,2n)` maps to the
`Q_N`-increment bridge

```
Pr(Y_1=y_1,...,Y_n=y_n | Y_1...Y_n=id)
  proportional to product_j Q_N(y_j),
```

with independent uniform microfactorizations of each `y_j` conditional on the
increment vector.  Explicitly, with `M=binom(N,2)`, `Q_N(id)=1/M`, a specified
3-cycle has mass `3/M^2`, a specified product of two disjoint transpositions
has mass `2/M^2`, and all other elements have mass zero.

Define on the original word space the aligned nonlazy subchain

```
B_{N,n} = (1/(n-1)) sum_{j=1}^{n-1} H_{2j-1,4}.                (C-4)
```

Under the pairing, (C-4) is exactly the two-consecutive-increment heat bath of
the `Q_N` return bridge, including fresh uniform microfactorizations.  For
`m>=6`, `|R_m|=3`, and direct coefficient comparison gives

```
E_K(f,f) >= ((n-1)/(6(m-3))) E_B(f,f)
          = ((m-2)/(12(m-3))) E_B(f,f)
          >= (1/12) E_B(f,f).                                (C-5)
```

Therefore `gap(K_{N,2n}) >= gap(B_{N,n})/12`.  This route uses neither a
support-component projection nor paths through a normal form.

The deterministic exact check in `aligned_r4_connectivity.py` found one
component for `(N,m)=(3,4),(4,4),(4,6)`, of sizes 27, 120, and 3936.  This only
fails to falsify the next proposition.

**First unproved standalone proposition (Parity-block bridge Poincare).**
There are universal constants `c>0,C<infinity` such that, for every `N>=3`
and every integer `n>=3`, the chain `B_{N,n}` in (C-4), on the uniform
length-`2n` transposition identity bridge, is irreducible and

```
gap(B_{N,n}) >= c (N n)^(-C).
```

The strongest self-attack is that an inverse-polynomial gap for the base walk
`Q_N` does not imply any gap for its fixed-endpoint path Glauber dynamics;
hard bridge constraints can create disconnected common-neighbor graphs or
long-range influence.  The small connectivity check is not evidence for the
quantified proposition.

