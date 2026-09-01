# M295 checkpoint

Status: candidate frozen before any new-rank computation.

## Frozen-input verification

`sha256sum -c SHA256SUMS` passes without drift in all eight prerequisite
directories M266/M268, M274/M277, M280/M283, and M285/M287.  The accepted
scope is odd `k>=3`, `n=3k`, and admissible lags `2<=ell<=n-2`, under
`(pq)(x)=p(q(x))` with displayed factors multiplied left-to-right.  I
independently transcribed the following convention guard:

```text
beta_1(s)=sum_(ef=s; e in T(L),f in T(M)) nu_L(e)nu_M(f)
 -1/2 sum_(C in {C_-,C_+})
       sum_(ef=s; e in T(C),f in T(M))nu_C(e)nu_M(f),

beta_2(s)=a(s)[F_(r-2)(s^-1L)/F_r(L)
                  -F_(r-2)(s^-1F)/F_r(F)].
```

Here `a(s)=3` on triangles and `2` on doubles; channel two receives no
additional `1/2`.  Every triangle/double has exactly three/four positive
cyclic-composition representations, with no additional `n`.  On admissible
lags the literal owner response equals

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
 +sum_(i:d_i>=3) delta_(d_i) C_ii^s(ell),
```

where every displayed summand is nonnegative.  Only the centered `beta_j`
remain signed.

## Single named candidate fixed before computation

Because channel one always has a double `s=ef` with exterior chord `e` and
middle chord `f`, its coefficient factors exactly as

```text
beta_1(ef)=gamma_k(e) nu_M(f),

gamma_k(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e),
```

with absent terms zero.  The candidate is the **fixed-middle fully
recombined pairing**

```text
(FMCP_1)  S_(k,ell)(f):=sum_e gamma_k(e)F_ell(ef) >= 0
```

for every odd `k>=3`, every admissible lag, and every middle chord
`f in T(M)`.  The sum over `e` includes all positive cross-seam and all
signed within/separate exterior coefficients before asking for a sign.  It
is therefore neither raw atomwise positivity nor a stochastic-order,
monotonicity, or PSD assertion.

Since `nu_M(f)>0`, exact factorization gives

```text
eta_1(F_ell)=sum_(f in T(M))nu_M(f)S_(k,ell)(f).
```

Thus `(FMCP_1)` would prove `(GOCI_1)`.  I will first attempt a direct
interval-overlap proof.  Only if that proof exposes an undecided sign will I
run one exact `k=5` falsifier for this candidate.  No other candidate or rank
will be tested in M295.
