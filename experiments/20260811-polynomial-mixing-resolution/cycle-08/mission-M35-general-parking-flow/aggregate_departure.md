# Exact aggregate departure from a duplicated parking value

## Statement

Let `n=r+1>=3`, let `F_r` be the minimal transposition factorizations of
the long cycle on `{0,...,r}`, and let `P_r` be the nonlazy uniform scan of
the `r-1` adjacent exact rank-two heat baths.  Write

```text
L((a_1,b_1),...,(a_r,b_r))=(a_1,...,a_r),  a_s<b_s,
```

and project by the multiplicity vector `m`, where `m_h` is the number of
coordinates of `L` equal to `h`.  If `bar P_r` is the stationary-flow
projection and `pi(m)` its parking-macro stationary law, then for every
feasible `m` and every `0<=h<r`,

```text
sum_(j>h) bar P_r(m,m-e_h+e_j)
  = 2 m_h(m_h-1) / [3r(r-1)].                         (1)
```

Consequently

```text
sum_(j>h) Q_barP(m,m-e_h+e_j)
  = pi(m) 2 m_h(m_h-1) / [3r(r-1)].                  (2)
```

If `m_h>=2`, at least one target `j>h` therefore has stationary capacity
at least

```text
4 pi(m) / [3r^2(r-1)].                               (3)
```

Equations (1)--(3) concern the aggregate over targets.  They give no
lower bound for a prescribed target value.

## Proof

Biane's type-A theorem, equivalently Stanley's labeling theorem, says that
the lower-sequence map `L` is a bijection from `F_r` to the parking
functions of length `r`.  Conditional on a multiplicity vector `m`, the
raw state is consequently uniform over all `r!/product_h m_h!`
permutations of that multiset.  At any fixed adjacent scan position, the
probability that both lower labels equal `h` is exactly

```text
(m_h)_2/(r)_2 = m_h(m_h-1)/[r(r-1)].                 (4)
```

A minimal long-cycle factorization has a tree as its factorization graph,
so its two factors are distinct.  If their common lower endpoint is `h`,
they are `(h,a)` and `(h,b)` for distinct `a,b>h`.  Their ordered product
is a 3-cycle and has exactly three ordered transposition decompositions.
The current decomposition has lower-label multiset `{h,h}`; each of the
other two has lower-label multiset `{h,min(a,b)}`.  Thus its exact
rank-two heat bath changes the macro with probability `2/3`, always by
replacing one `h` by some value strictly larger than `h`.

Multiplying (4) by `2/3` proves (1); averaging over the uniform scan does
not change the value.  Multiplication by `pi(m)` gives (2).  There are at
most `r` possible targets, and `m_h(m_h-1)>=2` when `m_h>=2`, which gives
(3).

The convention is `(pq)(x)=p(q(x))`, with factor tuples multiplied
left-to-right.  Reversing the pair orientation reverses the 3-cycle but
does not change the three-decomposition or lower-label-multiset argument.

## Sharp warning from the binary calibration

For `r=7` and the adjacent ideal edge

```text
x=0^4 1^3  ->  y=0^3 1^4,
```

write `T=8^6` for the raw Dénes count.  Exact enumeration gives

```text
Q_barP(x,y)=1/(9T),       pi(x)/r^2=35/(49T),
Q_barP(x,y)/(pi(x)/r^2)=7/45.                         (5)
```

The aggregate identity (2) is much larger because most equal-zero pairs
raise to targets other than `1`.  Hence (1) cannot be silently converted
to a prescribed adjacent-target estimate.

## Dependencies

- **Cited:** Biane, *Parking Functions of Types A and B*, EJC 9 (2002),
  Theorem 3.1, DOI `10.37236/1668`.
- **Proved/cited:** the factorization graph of a minimal long-cycle
  transposition factorization is a tree.
- **Proved here:** all probability and heat-bath normalizations in
  (1)--(3).
- **Empirical exact calibration only:** the individual edge value (5);
  the harness verifies it by complete enumeration.
