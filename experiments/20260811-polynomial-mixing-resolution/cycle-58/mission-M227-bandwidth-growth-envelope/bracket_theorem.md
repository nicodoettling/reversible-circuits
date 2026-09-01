# M227 exact rational bracket theorem

Date: 2026-08-13 UTC.

## 1. Scope and statement

Let `b=(b_(6,0),...,b_(6,6))^T` be the degree-six Bernstein vector and let

```text
e=(1,5/6,2/3,1/2,1/3,1/6,0)^T,   M=e e^T.           (1.1)
```

This is exactly the M221 unsaturated retained atom: multiply the degree-one
feature `(1,1)` by the likelihood atom `b_(1,0)=1-u`, then elevate from
degree two to six. Let `G` be the uniform fresh first-Jacobi charge matrix,

```text
G_ij=integral b_i(u)b_j(u) du
     -12 integral (u-1/2)b_i(u)du integral (u-1/2)b_j(u)du.  (1.2)
```

For `w=1,2`, define the optimal bandwidth-`w` PSD-majorant charge

```text
p_w=min <G,C>                    (P_w)
    subject to C-M >=_PSD 0,
               C_ij=0 if |i-j|>w.
```

Then exact rational certificates prove

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,   (1.3)
167478197/630630000 <= p_2 <= 894863807/3363360000.   (1.4)
```

In particular,

```text
p_1 > p_2 > <G,M>=1/4.                                  (1.5)
```

The exact optima are not identified. This theorem concerns one explicit
atom, not the full M221 actual kernel row and not a recursive construction.

## 2. Exact conic dual

Because the seventh row and column of `M` vanish, delete that coordinate.
The deleted coordinate does not change either optimum: restriction gives a
feasible six-dimensional primal point with the same objective, while a
six-dimensional primal point extends by a zero final row and column. The
extended slack is a direct sum with zero and remains PSD; the final charge
contribution is zero. Thus the six-dimensional and seven-dimensional programs
have identical feasible values. The analogous dual restriction/extension is
not needed for the weak-duality certificates below.

Writing `P=C-M`, Lagrange duality gives

```text
p_w=max <M,X>=e^T X e             (D_w)
    subject to X >=_PSD 0,
               X_ij=G_ij if |i-j|<=w.                (2.1)
```

Large diagonal `C` is strict feasible in the active six-dimensional block,
so strong duality holds. Only weak duality is used below.

## 3. Exact certificates

The complete rational matrices are frozen in `results.json`. Their matrix
digests are

```text
width 1 dual   f0a151f10acdfeb02ca627a08e94a195de1d88bdffec4e64bc316a4ea19e1f7f
width 1 primal ff073c9bb6861dec4283424970d23b37dfe970de2d6ff03084dab7844c1fb788
width 2 dual   321320c33f194a19b33d29034e4223661aebea19910a71f16f5d95cc8a1ed2ad
width 2 primal f62da8dabbaad2e8a99df10fc09198506d15d0292191fca5ec52bb223b571d12
```

For each dual matrix `X_w`, the checker verifies exactly that it agrees with
`G` on the width-`w` band. Every listed Fraction `LDL^T` pivot is positive,
so `X_w>0`. Hence `<M,X_w>` is a valid lower bound. For each primal matrix
`C_w`, the checker verifies exact band support and that every exact `LDL^T`
pivot of `C_w-M` is positive. Hence `C_w-M>0` and `<G,C_w>` is a valid upper
bound. Direct contractions give (1.3)--(1.4); the bracket widths are

```text
width 1: 14027287/10090080000,
width 2:  4940269/10090080000.                         (3.1)
```

The strict comparisons need no approximate arithmetic:

```text
lower(p_1)-upper(p_2)=10951531/155232000 > 0,
lower(p_1)-1/4       =15605731/180180000 > 0,
lower(p_2)-1/4       = 9820697/630630000 > 0.          (3.2)
```

## 4. Generic rank-one elevation formulation

For a degree-`n` Bernstein feature vector `z`, elevation to degree `L=n+h`
is the exact linear map

```text
(E_(n,L) z)_r
 = sum_k z_k C(n,k) C(h,r-k) / C(L,r),                (4.1)
```

where an out-of-range binomial coefficient is zero. Therefore every
rank-one atom elevates exactly as

```text
z z^T  ->  (E_(n,L)z)(E_(n,L)z)^T.                   (4.2)
```

For any declared PSD charge matrix `G_L` and desired bandwidth `w`, the exact
least compression charge of this rank-one atom is precisely

```text
min <G_L,C>                    max e^T X e
 s.t. C-ee^T>=0,               s.t. X>=0,
      C off-band=0;                 X=G_L on-band,    (4.3)
```

with `e=E_(n,L)z`. This is a conic formulation, not a degree-uniform bound.
M227 proves no formula controlling (4.3) uniformly in `L,n,w,G_L`.

## 5. Probabilistic bookkeeping and exclusions

An exact surviving history factor `lambda=eta/pi_a>0` sends `M` to
`lambda M`. Homogeneity sends any feasible certificate `C` to `lambda C` and
scales both primal and dual values by `lambda`. Thus the one-atom inequalities
preserve every exact `eta/pi_a`. Killed branches `a=d` remain absent and are
not reintroduced by the envelope.

No bound on the sum over retained atoms is proved. In particular, (1.3)--(1.5)
prove neither recursive bandwidth-one/two closure nor contraction, total AMV,
an all-state statement, a gap, mixing, or Terminal A/B.

## 6. Reproducibility

```text
python3 -B bandwidth_growth_exact.py --output results.json
```

The checker uses Python 3.12.3 standard-library `Fraction` arithmetic,
`seed=null`, and imports/reads no predecessor code or data. Numerical SDP
guided discovery only; no numerical quantity occurs in a promoted claim.
