# M168 halfway checkpoint: exact phase collapse and scalar closure

Date: 2026-08-13.

The complete `IS/IN/X`, triangle/double, and two-source-channel score can be
summed over lag before taking an absolute value. Fix a supported intermediate
product `s`, put `q=s^{-1}h`, and let its residual cycles have sizes `d_i`.
A boundary edge `E_r=(r,r+1)` is internal to a `q` cycle in a nonzero target
completion exactly when

```text
q(r)=r+1  <=>  s(r+1)=r+1.
```

Call such an edge generic. Let `g_i` be the number of generic boundary
edges in residual cycle `i`, and let `a_i` count cyclically adjacent tails
`r,r+1` for which both `E_r,E_(r+1)` are generic. Summing M161's literal lag
slices and circular correlations over `y=1,...,n-3` gives exactly

```text
same-cycle ordered disjoint pairs in i: g_i(g_i-1)-2a_i,
cross-cycle ordered pairs in i,j:       2g_i g_j.
```

For each class the completion count depends only on the cycle sizes after
the two cuts. With `F=F_(n-5)`, the complete phase/lag sum for `s` is

```text
S(s)=sum_i [g_i(g_i-1)-2a_i]
          F(sort(d_1,...,1,1,d_i-2,...,d_3))
    +sum_(i<j)2g_i g_j
          F(sort(d_(other),1,d_i-1,1,d_j-1)).          (PC)
```

Terms with invalid sizes are zero. Formula `(PC)` combines `IS` and `IN`
inside the same-cycle count and `X` inside the cross-cycle count; the signed
source/intermediate sum is still taken afterward. It uses no schemawise
absolute value and omits no lower-support term.

Substitution into the accepted raw convolution gives

```text
sum_y z_k(y)
 = n^(n-2)/(n F_(n-3)(t_1^-1 h))
   sum_s a(s) S(s)/F_(n-3)(s^-1h)
     [F_(n-5)((B_ks)^-1h)/F_(n-3)(B_k^-1h)
      -F_(n-5)((A_ks)^-1h)/F_(n-3)(A_k^-1h)].         (PCS)
```

The narrow owned checker verifies `(PCS)` over exact `Fraction` against all
frozen M161 scores at `k=3,5,7`, without a quotient matrix. Because each
physical boundary-double orbit appears twice in the colored `y` list and
`pi_y` is constant, one also has exactly

```text
Delta_k(C_k):=bar K^2(O_B,C_k)-bar K^2(O_A,C_k)
             =(pi_y/2) sum_y z_k(y),                  (CE)
```

where `C_k` is the physical fixed boundary cell.

Finite calibration only: exact `k=3,5,7` and targeted floating
`k=9,11,13,15` give `k sum_y z_k(y)` approximately

```text
3.12033, 2.43231, 2.17959, 2.05295, 1.97715, 1.92673, 1.89079.
```

An additional targeted exact fixed-cell evaluation at `k=9` has all 24
scores positive and `A_k(1,1)=0.7698574787`; positivity through `k=9` is
explicitly not promoted.

There is a deterministic route needing no sign theorem. For any real
sequence `x_1,...,x_N`, with path variation
`V(x)=sum_(i<N)|x_(i+1)-x_i|`, every entry differs from the mean by at most
`V(x)`, so

```text
sum_i |x_i| <= |sum_i x_i|+N V(x).                   (TV-close)
```

Applying this to `x_y=Z_k(y)=kz_k(y)` and `N=3k-3` proves that `(FCL1)`
follows from

```text
(PCS-bound)  k |sum_y z_k(y)|=O(1),
(FD-bound)   k^2 sum_y |z_k(y+1)-z_k(y)|=O(1).        (SC)
```

Status ledger:

- **proved:** exact phase collapse `(PC)--(PCS)`, event identity `(CE)`,
  and deterministic closure `(TV-close)--(SC)`;
- **exact finite only:** frozen matches at `k=3,5,7` and targeted positivity
  check at `k=9`;
- **unresolved:** both universal bounds in `(SC)`, hence `(FCL1)`.

Thus `k^2` sequence variation is not yet the sole open lemma: the universal
signed-sum bound also still needs proof. No direct-L1, all-edge, H0, gap,
bridge, identity-chain, or Terminal inference is drawn.

