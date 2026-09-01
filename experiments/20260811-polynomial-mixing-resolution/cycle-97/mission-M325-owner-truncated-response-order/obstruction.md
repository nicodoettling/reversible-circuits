# M325 exact analytic obstruction to TOEC_1

Date: 2026-08-14 UTC
Status: `TOEC_1` is refuted; no computation was used

## 1. First boundary owner composition

Take the first allowed rank with a nonunit middle cut,

```text
k=5, n=15, u=2, ell=2, T=mu_5.
```

The terminal `T` is a canonical QBD endpoint and retains every sign block.
On the negative exterior law take the actual seam chord and middle phase

```text
e=z_1={0,1},             f=f_(0,2)={5,7}.
```

The four cyclic gaps are

```text
(g_1,g_2,g_3,g_4)=(1,4,2,8).
```

This is a separated double.  The exact M285 owner law gives residual owner
sizes

```text
(g_1,g_3,g_2+g_4)=(1,2,12).                         (1.1)
```

Its size-12 two-run owner has generic-tail intervals `{1,2,3}` and
`{7,...,13}`.  Hence at target phase `x=1`, both `x` and `x+ell=3` are
generic tails of that same owner.  The full completion signature is

```text
sigma_*= {{(1,0),(2,0),(12,2)}}                    (1.2)
```

and its exact response weight is

```text
w(sigma_*)=tau(10)/tau(12)>0.                       (1.3)
```

The actual terminal negative Borel mass of `z_1` is

```text
v_5(1)/2 = 8/125 >0,                                (1.4)
```

so this single decorated configuration proves

```text
m^-_(mu_5)(sigma_*) >= 8/125 >0.                    (1.5)
```

## 2. No positive completion-profile mate

Every positive exterior chord has one endpoint `i in {1,2,3,4}` and one
endpoint `j in {10,11,12,13,14}`.  With its two middle endpoints ordered as
`p<q` in `{5,6,7,8,9}`, the positive state is nested and its residual sizes
are

```text
q-p,             15-j+i,             (p-i)+(j-q).   (2.1)
```

For the complete `u=2` phase orbit, `q-p` is either `2` or `3`.  The other
two quantities in `(2.1)` are at least

```text
15-14+1=2,       and       (5-4)+(10-9)=2.           (2.2)
```

Thus no positive state has a singleton residual owner.  In particular,

```text
m^+_(mu_5)(sigma_*)=0.                              (2.3)
```

Equations `(1.5)` and `(2.3)` refute the same-full-signature capacity
condition in `TOEC_1`.  The reflected lag `15-2=13` has the same obstruction
by reversing the ordered target pair.  No endpoint is omitted and no
quantile cell is sliced at `T=mu_5`.

## 3. Exact scope of the obstruction

The singleton owner is inactive (`r=0`) in `(1.2)`.  Its factor in the
literal completion weight is exactly one, so positive configurations with
different inactive-owner data can still compensate its negative mass in
the total weighted sum.  Therefore:

```text
TOEC_1 is false,
but this does not refute GQAC_1 or MCLP_1.            (3.1)
```

The failure is not a cell, fixed-middle, or sign-block sign counterexample.
It is a support obstruction to the predeclared full-completion-profile
matching interface after the required complete aggregation.

Because the analytic obstruction is decisive, the authorized `k=15` guard
was not run.

