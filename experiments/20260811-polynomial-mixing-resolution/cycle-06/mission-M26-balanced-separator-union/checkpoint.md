# Halfway checkpoint: exact overlap reduction and full-support zero-exit states

## Exact union/profile masses

Let `P` range over labeled support-component partitions of `[N]`, including
isolated singleton blocks, and let `E_P(m)` be the exact number of words
whose factorization graph has component partition `P`.  Put
`a=floor(N/2)` and define

```text
b(P)=1{some union of blocks of P has size a},
c(P)=1{max_(D in P)|D|<=N/2}.
```

Then the exponentially overlapping events are counted once by

```text
pi(B)=Z_(N,m)^(-1) sum_P b(P)E_P(m),
pi(C)=Z_(N,m)^(-1) sum_P c(P)E_P(m).                  (C.1)
```

The exact smaller sides are the minima of each displayed numerator and its
complement in `Z_(N,m)`.  This is the correct mass formulation; summing the
fixed-separator masses from M24 overcounts a word once for every balanced
block union it possesses.

## A universal deep interior

Let `V(w)` be the set of used labels.  For `N>=24`, set

```text
D={w:|V(w)|<=a-10}.
```

An update of length `r<=5` introduces at most `2r<=10` labels outside
`V(w)`.  Every possible heat-bath output from `D` therefore uses at most
`a` labels and has at least `N-a>=a` isolated labels.  Choosing any `a`
isolated labels gives a balanced no-crossing separator, and every component
has size at most `a`.  Thus, for every `w in D`, exactly

```text
K(w,B^c)=K(w,C^c)=0.                                  (C.2)
```

This includes all `r=3,4,5` outcomes and laziness, not only the square
subchain.  Consequently, with `Sigma_B=B minus D` and `Sigma_C=C minus D`,

```text
Q_K(B,B^c)=Q_K(Sigma_B,B^c)<=pi(Sigma_B)/2,
Q_K(C,C^c)=Q_K(Sigma_C,C^c)<=pi(Sigma_C)/2.           (C.3)
```

The factor `1/2` is the total nonlazy mass.  Equation (C.3) isolates the
exact stationary shell-mass question required for an upper-conductance
proof; it does not itself estimate that mass.

## Full-support deep states and exponential overlap

The preceding obstruction is not only an isolated-label effect.  Let
`N=4k>=60`, `m=N`, fix a perfect matching, and take a word containing each
matching edge exactly twice in arbitrary order.  Its component partition is
`2^(N/2)`.  In an `r<=5` update, deleted old factors affect at most `r`
matching pairs and new factors touch at most `2r` further pairs.  At least

```text
N/2-3r>=N/2-15>=N/4
```

pair components remain untouched.  Their union supplies a balanced
separator, while every changed component has at most `6r<=30<=N/2`
vertices.  Therefore every such full-support state also satisfies (C.2).

The exact number of these matching words is

```text
W_match(N)=(N!)^2/[2^N(N/2)!].                       (C.4)
```

A fixed repeated-edge word already lies in

```text
binom(N-2,a-2)+binom(N-2,a)
```

fixed balanced-separator events, asymptotic to half of all
`binom(N,a)` separators.  This explicitly demonstrates exponential overlap.

## The simplest zero-exit mass hypothesis is false

Write `N=2a` with `a>=3`.  At length `m=N`, compare (C.4) with the profile

```text
(a,2,1^(a-2)),                                        (C.5)
```

where the size-`a` component is a connected genus-zero identity word, the
pair is a square, and the rest are isolated.  Its exact count is

```text
W_cap(N)
 =binom(2a,a)binom(a,2)N! a^(a-3)/2.                 (C.6)
```

Using `C_0(a)=(2a-2)!a^(a-3)`, the ratio is

```text
W_cap/W_match
 =4^(a-1)(a-1)a^(a-2)/a!
 >=4^(a-1)(a-1)/a^2.                                 (C.7)
```

Thus the explicit full-support zero-exit family is exponentially smaller
than one boundary profile already inside both `B` and `C`.

Moreover, the two factors of the size-two component occupy adjacent slots
with exact probability `2/N`.  Refreshing that square to any of the
`2a=N` edges joining the pair to the size-`a` component creates a component
of size `a+1` and leaves one isolated vertex.  This exits both `B` and `C`
with conditional full-`K` probability at least

```text
(2/N)[N/(6(N-2)D_N)]=1/[3(N-2)D_N].                  (C.8)
```

All other block sizes contribute nonnegative flow.

## Exact remaining implication

The zero-exit construction refutes any pointwise escape proof, but (C.7)
refutes the simplest claim that matching states dominate the union cut.
A Terminal-B proof still needs an explicit sequence for which the complete
boundary shell in (C.3), not one selected interior family, has
superpolynomially small mass relative to the correctly oriented side.
