# M12 Cycle 02 Halfway Checkpoint

## Exact statistic and layer flow

Let `c(w)` be the number of connected components of the support graph,
including isolated labels.  If the nontrivial components have sizes `v_i`
and factor counts `k_i`, then

```text
G(w) = sum_i [k_i-2(v_i-1)]/2 = m/2-N+c(w).
```

Thus, at fixed `N,m`, every total-surplus threshold is exactly a support-
component-count threshold.  For a word `u` of length `m-2`, let

```text
I(u) = sum_C binom(|C|,2),       X(u) = binom(N,2)-I(u).
```

At a fixed slot, inserting `ee` with `e` internal to a component increases
`G` by one, while inserting a crossing `ee` leaves `G` unchanged and merges
two components.  Consequently the exact directed stationary flow of a fixed-
slot pair heat bath between adjacent surplus layers is indexed by

```text
sum_{u:G(u)=g} I(u)X(u).
```

This identity is exact, but by itself it does not compare the boundary layer
to the mass of either cumulative side.

## All-genus Hurwitz audit

Write `C_g(d)` for connected identity words on a fixed `d`-set of length
`k=2g+2d-2`.  Dubrovin--Yang--Zagier prove that, for fixed `d`, the associated
Hurwitz number is a finite signed linear combination of exponentials and

```text
C_g(d) ~ (2/d!) binom(d,2)^k                 (g -> infinity, d fixed).
```

Their displayed degree-six example has coefficients of both signs.  Their
fixed-genus asymptotics and their fixed-degree asymptotics do not supply a
joint error bound when both `d` and `g` grow.  Do--He--Robertson extend the
finite-exponential structure to fixed ramification profile, again with the
profile fixed in the large-genus limit.  No uniform positive recurrence
inequality for the ratio needed here is stated in either source.

More sharply, the natural fixed-slot pendant-square ratio is not uniformly
inverse-polynomial.  Inserting `(x a),(x a)` into a connected genus-`g` word
on the other `d-1` labels gives exactly

```text
R_g(d) = d(d-1) C_g(d-1)/C_g(d)
```

as the proportion counted by this construction.  The fixed-degree
asymptotic gives

```text
R_g(d) ~ [4d^2/((d-1)(d-2)^2)] ((d-2)/d)^(2g+2d-2).
```

For every fixed `d>=3`, this is exponentially small in `g`.  Therefore any
proof that assumes a uniform all-genus pendant bridge-square estimate is
false.  This is an auxiliary obstruction, not TERMINAL B: in the same dense
regime the disconnected stationary side is exponentially rare, so the
orientation-free conductance is governed by merging from that rare side.

For example, when `N=3` and `m` is even, the disconnected side consists of
exactly the three constant-edge words.  From each such word an `r=4` update
leaves the side with probability at least `(1/6)(24/27)=4/27` for `m>=6`.
Thus the exponentially small reverse split probability is exactly the wrong
orientation for a bottleneck.

## New theorem in progress

The recurrence route is replaced by a uniform finite-group trace estimate.
For a labeled support partition `P`, let

```text
e(P)=sum_{B in P} binom(|B|,2),   H_P=product_B S_B.
```

The number `Z_P(k)` of identity words confined to the internal transpositions
of `P` is the trace of the `k`th power of a central Cayley operator on `H_P`.
For even `k`, its two extremal eigenvalues are `+/-e(P)` and every other
eigenvalue has absolute value at most `e(P)-2`.  Hence

```text
2e(P)^k/|H_P| <= Z_P(k)
                   <= 2e(P)^k/|H_P|+(e(P)-2)^k.
```

When `k>=2N^3 log(2N)`, this estimate is uniform over every support
partition.  A union bound over proper refinements then shows that the exact-
support count `E_P(k)` satisfies

```text
e(P)^k/|H_P| <= E_P(k) <= 4e(P)^k/|H_P|.
```

These bounds imply both (i) a fixed-slot deletable internal square probability
at least `1/(4e(P))` inside every exact macro layer and (ii) geometric decay
of component-count layer masses.  The remaining work is to write the
constants and the deterministic partition-merge multiplicity carefully and
then transfer the resulting cut flow from the adjacent-pair chain `J` to `K`
using inherited ledger entry L-0020.

## Current smallest open implication

> Extend the uniform two-sided component-threshold conductance estimate from
> the proved extreme-dense regime `m-2>=2N^3 log(2N)` to the intermediate
> regime `2(N-1)<m<2+2N^3 log(2N)`, or construct a superpolynomial threshold
> cut there with exact two-sided mass and complete boundary flow.

