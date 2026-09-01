# M245 checkpoint

Status: source reconstruction complete; analytic adjacent-split audit active.

The exact accepted statement is the following.  Put `D=2k-1`,
`R=2k-3`, `b_d=e^{-d}d^{d-1}/d!`,

```text
K_R(r,d)=b_d b_(r-d)/(R b_r),
h(r)=(r-1)(r-2)/(rR),
H_s=h(s)+h(D-s)=1-gamma_L(s).
```

For the literal normalized B-side ordered-disjoint-double profile,

```text
Phi_s^D(Y_l)=1/H_s * {
 h(s)F_l(D-s)+h(D-s)F_l(s)
 +W_s(F_l)+W_(D-s)(F_l)},

W_r(f)=sum_(d=1)^(r-1)(r-d-1)K_R(r,d)f(d).
```

`Phi_s^D(X_l)` uses the same literal tuple law and adds the complementary
two-run face before cyclic averaging.  Collision atoms are counted with
multiplicity.  The exact obligation is, for every odd `k>=3`, both
`Z=X_l,Y_l`, and `2<=l<=(3k-1)/2`,

```text
sum_(s=1)^(k-2) sqrt(s)
  |Phi_(s+1)^D(Z)-Phi_s^D(Z)| <= C sqrt(l).       (DV)
```

Thus “adjacent split” means `s -> s+1` variation of the **normalized literal
conditional double profile**.  There is no `q_s` or `q_hat_s` weight in
`(DV)`: the weight is exactly `sqrt(s)`, inherited from M192's cumulative
Abel coefficient bound.  The `q_hat_s` subprobability weights occur only in
the separate `(DE)` signed embedding average.

M211 refutes pointwise `(IKBE-b)` only.  Its witness and its `q_hat` issue do
not refute, prove, or alter `(DV)`.

No theorem, refutation, or downstream implication has yet been accepted.

