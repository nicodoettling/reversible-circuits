# M30 halfway checkpoint: second shell has inverse-polynomial leakage

## 1. Structural sandwich

Use `(pq)(x)=p(q(x))`, `M=binom(N,2)`, `m=4N^3+4`, and

```text
V^(0)={c>=2},
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.
```

For a vertex cut `P`, let `H_P` be its direct-product subgroup.  Define:

- `C_2`: all words for which the crossing-factor occurrences of some cut are
  coverable by two intervals, each of length at most five;
- `O_2`: all words for which those occurrences lie in one interval of length
  at most nine;
- `D_2`: all words for which those occurrences lie in two disjoint
  length-five intervals `I,J` and both ordered block products
  `h_I,h_J` lie in `H_P`.

Then

```text
D_2 subset V^(2) subset O_2 union D_2 subset C_2.       (C.1)
```

For the first inclusion, replace either `D_2` block by an internal
same-product length-five factorization; the intermediate word lies in the
exact one-window shell, so two replacements reach `V^(0)`.

For the middle inclusion, take `x in V^(1)`, its witness cut/window `I`, and
the update window `J` producing `y`.  All crossings of `y` lie in `I union
J`.  If their hull has length at most nine, `y in O_2`.  Otherwise the
windows are separated and can be extended to disjoint five-windows.  The
`I` product lies in `H_P` because every factor outside `I` in `x` is internal.
The `J` factors of `x` are factorwise internal and the update preserves their
product, so the `J` product in `y` is also in `H_P`.  Added extension factors
are internal.  Thus `y in D_2`.  This also covers `V^(1)` by the `O_2` case.

The last inclusion is immediate.  This is a rigorous sandwich; equality with
the coarse two-cover set is not asserted.

## 2. Exact-factorial mass upper bound

Put

```text
k=m-10=4N^3-6,                 E=binom(N-1,2).          (C.2)
```

Cover an `O_2` witness by one length-ten interval.  For `D_2`, retain its two
disjoint five-windows.  In both cases the `k` remaining factors are internal
to the witness cut and have even length.

For a cut with subgroup `H_P`, internal class sum `T_P`, internal-edge count
`e_P`, and group order `h_P`, every relevant block product is in `H_P`.
Centrality therefore combines all outside segments, and Cauchy--Schwarz plus
the frozen trace estimate gives

```text
[g]T_P^k<=[e]T_P^k<=4e_P^k/h_P.                        (C.3)
```

The exact cut-size sum, with `j=k`, is

```text
sum_P e_P^k/h_P<=2N E^k/(N-1)!.                        (C.4)
```

As in M28, the isolate cuts contribute exactly `N` after normalization; every
cut of smaller side `s>=2` contributes at most
`exp[-N^2(s-1)]` because `k/E>=8N`.

There are at most `m` ten-windows, `m^2` disjoint five-window pairs, and
`M^10` block tuples.  Hence

```text
|V^(2)|
 <=|O_2 union D_2|
 <=16N m^2 M^10 E^k/(N-1)!.                            (C.5)
```

Using `|Omega(N,m)|>=2M^m/N!` and `E/M=1-2/N`,

```text
pi(V^(2))
 <=8N^2m^2(1-2/N)^k
 <=exp(-5N^2)<1/2.                                    (C.6)
```

Thus the actual second shell is globally oriented, not only the structured
subhalo.

## 3. Two-window-robust identity tails

Let `d=N-1` and use the transposition alphabet of size `E=binom(d,2)`.  At
even length `k`, the number of identity tails is at least

```text
2E^k/d!.                                                (C.7)
```

Call one *two-window robust* if deleting the union of any two intervals, each
of length at most five, leaves connected support on `[d]`.  A bad tail has a
cut whose crossing occurrences lie in such a union.  For fixed cut/windows,
if their union has `u<=10` positions, the crude count is at most

```text
E^u e_P^(k-u)<=E^10 [E(1-2/d)]^(k-10).                 (C.8)
```

The endpoint constraint is deliberately discarded; no odd block is commuted
through a subgroup sum.  Summing at most `k^2` window pairs and `2^d` cuts,
then dividing by (C.7), bounds the bad fraction by

```text
(1/2)k^2 2^d d! exp[-2(k-10)/d]
 <=exp(-3N^2)<1/2.                                    (C.9)
```

Indeed the logarithm of the prefactor is at most `4N^2`, while
`2(k-10)/d>=7N^2`.  Hence there are at least

```text
R>=E^k/(N-1)!                                          (C.10)
```

robust identity tails.

## 4. Actual H5 boundary transition

Set `z=N`, `s=(z,1)`, and `q=(2,3)`.  For every robust identity tail
`u=(b_1,...,b_k)`, define

```text
y=(s,q,q,q,s, s,q,q,q,s, b_1,...,b_k).                (C.11)
```

Each five-block has product `q`, so the ten-prefix and the tail both have
product identity.  Across the isolate cut `{z}|[N-1]`, the crossing positions
are `1,5,6,10`, and the two five-block products lie in the cut subgroup.
Thus `y in D_2 subset V^(2)`.

Use the `H_5` window at positions ten through fourteen.  Four right Hurwitz
swaps push the factor at position ten through `b_1,...,b_4`, replacing it by
its conjugate at position fourteen.  The new `z`-edge positions are

```text
1,5,6,14.                                               (C.12)
```

They require at least three length-five intervals to cover.  Deleting any two
five-windows therefore leaves one `z`-edge.  It removes from the tail at most
two intervals of at most five factors, so tail robustness leaves `[N-1]`
connected.  The target lies outside `C_2`, hence outside `V^(2)` by (C.1).

The exact length-five fiber has size at most `M^4`; including all original-K
normalizations, this target has probability at least

```text
p=1/[6(m-4)M^4].                                       (C.13)
```

Equations (C.5), (C.10), and (C.13) prove

```text
Phi_pm^K(V^(2))
 >=1/[96N m^2(m-4)M^14]
 >=1/N^38.                                             (C.14)
```

The exact full flow is `Q_K=Q_3+Q_4+Q_5`; (C.14) retains only these certified
`Q_5` transitions.  All omitted terms are nonnegative.

## Current conclusion

`V^(2)` is proper, globally exponentially small, and has inverse-polynomial
conductance.  The next unresolved shell is `V^(3)`; conductance monotonicity
under enlargement is not assumed.
