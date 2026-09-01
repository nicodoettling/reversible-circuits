# M52 halfway checkpoint

## Candidate theorem

For `s(T)` equal to leaf count `ell(T)` or edge/centroid balance `b(T)`, put

```text
H_q={w in F_N:s(T_J(w))>=q},  L_q=F_N\\H_q,
A_q^+=F_N^c union H_q,        A_q^-=F_N^c union L_q.
```

For every nontrivial threshold and both placements, the current proof gives

```text
Phi_pm^K(A_q^+)>=1/(24N^7),
Phi_pm^K(A_q^-)>=1/(24N^7).                           (C.1)
```

The key new ingredient, not present in M49/M51, is a low-profile source
reservoir for the placement that seals every old high-profile macro exit.

## Exact global masses and orientation

Let

```text
Z_N=|Omega(N,2N-2)|,
C_0(N)=|F_N|=(2N-2)!N^(N-3),
h_q=|H_q|, l_q=|L_q|=C_0(N)-h_q.
```

Then exactly

```text
pi(A_q^+)=1-l_q/Z_N,  pi((A_q^+)^c)=l_q/Z_N,
pi(A_q^-)=1-h_q/Z_N,  pi((A_q^-)^c)=h_q/Z_N.         (C.2)
```

Thus the `+` placement can always be bounded using flow divided by `l_q/Z_N`,
and the `-` placement using flow divided by `h_q/Z_N`; no guess about
`pi(F_N)` or the smaller side is made.

## New low-side reservoirs

Retain the strand-deletion fiber bound

```text
Lambda_N=binom(m,2)(N-1)^2,  m=2N-2.                 (C.3)
```

### Leaf count

For a tree leaf `v`, `ell(T-v)<=ell(T)`.  Choosing one leaf in every low
state and deleting its permutation strand gives

```text
l_N(q)<=N Lambda_N l_(N-1)(q).                       (C.4)
```

Conversely, from every base word with fewer than `q` leaves, choose a
canonical base-tree leaf `u`, insert `(v,u)^2` in any of the `m-1` gaps, and
fix `v=N`.  The old leaf becomes degree two and `v` becomes a leaf, so leaf
count is unchanged.  This gives exactly

```text
|S_low^leaf|=(m-1)l_(N-1)(q).                        (C.5)
```

### Edge/centroid balance

Deleting a tree leaf cannot increase the smaller side of any surviving edge,
so again

```text
l_N(q)<=N Lambda_N l_(N-1)(q).                       (C.6)
```

For the reverse source, attach `v` to a canonical centroid `u` of the base
tree.  For every old edge, its side not containing `u` is a centroid branch
of size at most half the base tree; adding `v` to the `u` side leaves that
smaller-side size unchanged.  The new edge has balance one.  Hence total
balance is unchanged, and

```text
|S_low^bal|=(m-1)l_(N-1)(q).                         (C.7)
```

Every source in (C.5) or (C.7) has one specified padded-`H3` refresh that
removes `v`, enters `F_N^c subset A_q^+`, and has exact probability

```text
p_N=1/[6(m-2)D_N], D_N=(3N^2+N-12)/2.                (C.8)
```

Equations (C.3)--(C.8) give

```text
Q(A_q^+,(A_q^+)^c)/(l_q/Z_N)
 >=1/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7).                                        (C.9)
```

This is not the previously counted high-side macro certificate.

## Opposite placement

For `A_q^-`, the complement is the high-profile side.  Repeating the full
high-side adjacent-square counts gives:

- leaf thresholds: at least the M51 exact rate, uniformly `1/(24N^7)`;
- balance thresholds: at least `1/(24N^6)` off the even endpoint and
  `1/(96N^6)` at it, both at least `1/(24N^7)` for `N>=4`.

In each case the refreshed target lies in `F_N^c subset A_q^-`, so this is a
genuine crossing rather than a sealed edge.

## Complete flow accounting

For either cut, decompose

```text
Q=Q_(3,macro)+Q_(3,internal)+Q_(4,macro)+Q_(4,internal)
  +Q_(5,macro)+Q_(5,internal).
```

The certificate uses one term of `Q_(3,macro)`.  Every internal crossing and
all `H4,H5` contributions remain present and nonnegative.  No upper-flow or
Terminal-B claim is made, so discarding nonnegative terms is valid.

## Remaining audit

1. Check nontrivial threshold ranges (`q>=3` for low leaf side and `q>=2`
   for low balance side) and both extreme endpoints.
2. Recheck source uniqueness, centroid preservation, and constants.
3. Record exact finite mass/source checks and freeze the full nine fields.

If these checks survive, the scoped verdict is `PROVED`; it still says
nothing about refinements within a profile layer or arbitrary cuts.
