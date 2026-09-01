# Halfway checkpoint: every dense coverage threshold has polynomial full-K escape

## Scoped theorem now proved

Let `A` be the universal parity-aware pointwise mixing constant audited in
cycle-04 M07 and put `C_*=256(A+1)`.  For `N>=3`, even `m`, and

```text
m-2 >= C_* N log(N+1),
```

define `X(w)` to be the number of unused labels and, for
`1<=q<=N-2`, let `T_q={X>=q}`.  The current argument gives

```text
Phi_pm^K(T_q)
 >= q/[12(N-q-1)(m-2)D_N]
 >= 1/(24mN^3),
D_N=(3N^2+N-12)/2.                                    (C.1)
```

Thus `U_(N,m)=T_1` and every missing-support threshold are rejected as
Terminal-B cuts throughout an `O(N log N)` parity-mixed regime.  For all
sufficiently large `N`, this includes a nonempty part of the previously open
intermediate window below `2+4 binom(N,2)log(2N)`.

## Exact overlap and orientation calculation

Write `Z_(d,m)=|Omega(d,m)|`, and let `E_(d,m)` count words on `[d]` whose
exact support is all `[d]`.  Then

```text
E_(d,m)=sum_(j=0)^d (-1)^(d-j) binom(d,j) Z_(j,m),
pi(X=k)=binom(N,k)E_(N-k,m)/Z_(N,m).                   (C.2)
```

For `mu_q=E[binom(X,q)]`, exchangeability gives the exact factorial moments

```text
mu_q=binom(N,q)Z_(N-q,m)/Z_(N,m).                     (C.3)
```

Put `d=N-q`.  For `d>=3`, parity-aware return bounds give

```text
mu_(q+1)/mu_q
 <=[3d^2/(2(q+1))] exp(-2m/d).                        (C.4)
```

The right side is at most `1/[2(q+1)]` under the displayed length
assumption.  For `d=2`, it is zero because no positive-length
transposition word uses at most one label.  Since

```text
binom(k,q)<=(q+1)binom(k,q+1),   k>=q+1,
```

(C.3)--(C.4) imply

```text
pi(X=q)>=mu_q/2>=pi(T_q)/2.                            (C.5)
```

This directly controls all overlaps; no sum of fixed-label conductances is
used.  The inherited connected-support estimate also gives

```text
pi(U)<=Pr(support graph disconnected | product=id)
     <=1/[512(m+2)]<1/2.                              (C.6)
```

Hence every `T_q subset U` is itself the correctly oriented smaller side.

## Exact safe-square flow

Conditional on `X=q` and on its missing set, the word is uniform among the
`E_(d,m)` exact-support words on the other `d=N-q` labels.  Mark an adjacent
square whose deletion leaves exact support.  Deleting a marked square is a
bijection with an exact-support core of length `m-2`, one of
`M_d=binom(d,2)` edges, and one of `m-1` insertion gaps.  If `Y` is the
number of marks, then

```text
E[Y]=(m-1)M_d E_(d,m-2)/E_(d,m).
```

Using `Y<=m-1`, even-return monotonicity, and the inherited dense bound on
disconnected support at length `m-2`,

```text
Pr(Y>=1)>=M_d E_(d,m-2)/E_(d,m)>=1/(2M_d).            (C.7)
```

Choose one mark and pad it on the available side to an actual `H_3` window.
Replacing `(e,e,a)` by `(f,f,a)`, or `(a,e,e)` by `(a,f,f)`, with `f`
crossing between the `q` missing and `d` used labels, gives `qd` distinct
outcomes in `X=q-1`.  The exact triple-fiber size is `D_N`; laziness,
block-size choice, window scan, and conditional heat bath give certified
exit probability

```text
qd/[2*3*(m-2)D_N].                                    (C.8)
```

Multiplying (C.5), (C.7), and (C.8), and using
`M_d=d(d-1)/2`, gives (C.1).  The exact boundary flow remains the sum of the
`r=3,4,5` terms; the latter two are nonnegative and have not been discarded
from the chain.

## Remaining adversarial frontier

The proof deliberately uses parity-aware smoothing twice.  Below
`C_*N log(N+1)`, neither failure of boundary-layer domination nor failure of
the safe-square lower bound has been proved; those are only missing
sufficient estimates.  The smallest remaining coverage question is a
uniform bound, or an explicit superpolynomial cut, for `T_q` in the
low/intermediate interval below this threshold.
