# Polynomial reduction to adjacent-value parking flow

## Statement

Fix `r>=1`.  Let

```text
J_r={m in N^r: sum_i m_i=r and sum_(i=0)^k m_i>=k+1
                    for 0<=k<r}
```

and let `pi(m)` be proportional to `1/m!`.  Let `D_r` be the M36 chain:
delete type `i` with probability `m_i/r`, then insert uniformly among the
types that return the residual vector to `J_r`.  Let `A_r` retain exactly
the `D_r` off-diagonal transitions

```text
m -> m-e_i+e_j,        |i-j|=1,
```

and reject every other exit to the holding probability.  Then `A_r` is
reversible for `pi` and, with the gap-one convention for a singleton,

```text
gap(A_r)>=r^-7.                                         (1)
```

Consequently it is enough to compare adjacent-value ideal exchanges to the
actual projected parking heat bath.  An `H`-congestion flow for those
adjacent edges gives a comparison for all of `D_r` with an additional
factor at most `r^6 H`.

## Feasible canonical paths

Consider an off-diagonal `D_r` edge

```text
x -> y=x-e_i+e_j.
```

If `i<j`, use

```text
x^(k)=x-e_i+e_k,        i<=k<=j.
```

Because `y` is feasible, every `x` prefix from `i` through `j-1` has at
least one unit of slack.  The vector `x^(k)` subtracts one only from the
prefixes `i,...,k-1`, so every intermediate belongs to `J_r`.  If `j<i`,
the analogous path moves the unit left one index at a time; every affected
prefix increases, hence is feasible.  The path length is at most `r-1`.

For an intermediate `z=x-e_i+e_k`, `k!=i`, factorial weights give

```text
pi(z)/pi(x)=x_i/(x_k+1),
pi(x)/pi(z)=(x_k+1)/x_i<=r.                            (2)
```

## Recovery and congestion

Fix a directed adjacent edge `e=(z,z')` on one of these paths.  Its changed
index and direction are read from `e`.  Given the ordered original endpoint
indices `(i,j)`, the stage index `k` is therefore known and

```text
x=z+e_i-e_k.
```

There are at most `r^2` metadata pairs `(i,j)`, and the displayed recovery
gives at most one directed `D_r` transition per pair that uses `e`.  No
canonical macro hub is used.

Every positive off-diagonal transition of `D_r`, hence every retained edge
of `A_r`, has probability at least `r^-2`.  Therefore its stationary
capacity satisfies

```text
c_A(e)>=pi(z)/r^2.                                     (3)
```

For the standard path comparison load at `e`, use path length at most `r`,
the trivial bound `D_r(x,y)<=1`, (2), and the `r^2` recovery count:

```text
sum_((x,y):e in gamma_xy)
  pi(x)D_r(x,y)|gamma_xy|
 <= r^2 * (r pi(z)) * r
 = r^4 pi(z).
```

Dividing by (3) gives congestion at most `r^6`.  Hence

```text
E_D(f,f)<=r^6 E_A(f,f).
```

M36 proves `gap(D_r)>=1/r`, which yields (1).

## Boundary cases and scope

For `r=1`, `J_r` is a singleton.  For `r>=2`, all holding probabilities,
both exchange directions, rare types, and endpoint values `0,r-1` are
included because rejected exits remain on the diagonal.  The proof is
purely at the parking-macro level and uses exact stationary weights.  It
does not compare `A_r` to the actual adjacent raw-pair heat bath; that is
the remaining ADJACENT-VALUE PARKING FLOW proposition.
