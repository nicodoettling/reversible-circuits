# Halfway checkpoint: every fixed balanced separator has polynomial escape

## Exact scoped theorem

Fix `N>=3`, even `m>=4`, and a labeled balanced bipartition
`[N]=S disjoint union S^c`, with

```text
a=|S|=floor(N/2),  b=N-a,
L=binom(a,2)+binom(b,2).
```

Let

```text
A_S={w in Omega(N,m):every factor is internal to S or S^c}.
```

The current proof gives the exact two-sided bound

```text
Phi_pm^K(A_S)
 >=ab/[6L(m-2)D_N]
 >=1/[6(m-2)D_N]
 >=1/(12mN^2),
D_N=(3N^2+N-12)/2.                                   (C.1)
```

Thus a fixed balanced component separator is not a Terminal-B cut at any
allowed length, including the entire remaining low/base regime.  For
`N>=4`, both sides of the separator are nontrivial, so this is not an
isolated-label refresh.

## Exact mass and orientation

Write `Z_(d,j)=|Omega(d,j)|`, with `Z_(d,0)=1`, and set

```text
Z_(S|S^c,m)
 =sum_(j=0)^m binom(m,j)Z_(a,j)Z_(b,m-j).             (C.2)
```

The binomial factor retains every color interleaving.  Because disjoint
subgroups commute, (C.2) counts exactly the words with no crossing factor
and identity product.  Hence

```text
pi(A_S)=Z_(S|S^c,m)/Z_(N,m),
min-side mass
 =min{Z_(S|S^c,m),Z_(N,m)-Z_(S|S^c,m)}/Z_(N,m).      (C.3)
```

No asymptotic orientation is assumed.  Repeated internal and crossing
edges show both sides are nonempty.

## Product-walk square incidence

The `L` internal transpositions define a symmetric random walk on
`S_a x S_b`.  If `p_H(j)` is its identity return probability, spectral
decomposition gives

```text
p_H(j)=sum_theta w_theta lambda_theta^j,
w_theta>=0,  lambda_theta in [-1,1].                  (C.4)
```

Thus `p_H(m-2)>=p_H(m)` for even `m`.  Deleting a marked adjacent square is
a bijection with a length-`m-2` internal identity word, one of `L` inserted
edges, and one of `m-1` gaps.  If `Y` counts squares, then

```text
E[Y]=(m-1)L Z_(S|S^c,m-2)/Z_(S|S^c,m),
Pr(Y>=1)>=1/L.                                        (C.5)
```

This step uses no dense mixing, component-layer unimodality, or fixed-genus
count.

## Exact original-K boundary flow

Pad a selected square on its available side to an `H_3` window and replace
it by `(f,f)`, where `f` is any one of the `ab` separator-crossing edges.
Every outcome has the same ordered block product and leaves `A_S`.  The
exact conditional fiber has size `D_N`, so a certified state has exit
probability at least

```text
ab/[2|R_m|(m-2)D_N]>=ab/[6(m-2)D_N].                 (C.6)
```

Multiplying (C.5)--(C.6) gives the stationary flow.  Dividing by the exact
minimum in (C.3) can only increase the bound.  The full flow is
`Q_3+Q_4+Q_5` over available sizes; `Q_4,Q_5` are retained and nonnegative.
For a balanced split,

```text
2(ab-L)=N-(a-b)^2>0,
```

which proves the middle inequality in (C.1).

## Remaining overlap obstruction

The theorem does not union-bound over balanced separators.  A word with
several support components can belong to many `A_S`, and a crossing refresh
may leave one chosen `A_S` while remaining in another.  The next exact cut
is the union of balanced separators, or the stronger largest-component
threshold; its global mass and true exit flow remain open.
