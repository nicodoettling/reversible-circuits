# M230 corrected full-dimensional bracket theorem

Date: 2026-08-13 UTC.

## 1. Referee disposition

M230 **REJECTS M227 AS A SELF-CONTAINED FROZEN PROOF** for material objection
M-1 below. M230 independently salvages the numerical theorem by supplying the
missing exact seven-dimensional dual certificates. Nothing in M227 was
changed.

## 2. Clean-room reconstruction

Write `b_i=b_(6,i)`. Direct beta integrals give

```text
integral b_i b_j
 = C(6,i)C(6,j)(i+j)!(12-i-j)!/13!,
integral (u-1/2)b_i(u)du=(i-3)/56.                    (2.1)
```

Thus M230 reconstructs, without M227 code or data,

```text
G_ij=integral b_i b_j
     -12 integral (u-1/2)b_i integral (u-1/2)b_j.     (2.2)
```

Multiplying the degree-one feature `(1,1)` by `b_(1,0)` gives degree-two
coefficients `(1,1/2,0)`. Exact elevation from degree two to six gives

```text
e=(1,5/6,2/3,1/2,1/3,1/6,0)^T,   M=ee^T.             (2.3)
```

Direct exact contraction gives `<G,M>=1/4`.

## 3. Full primal and dual

For `w=1,2`, the declared full seven-coordinate program is

```text
p_w=min <G,C>                         (P_w)
    s.t. C-M>=_PSD 0,
         C_ij=0 for |i-j|>w.

p_w=max <M,X>                         (D_w)
    s.t. X>=_PSD 0,
         X_ij=G_ij for |i-j|<=w.      (3.1)
```

The dual follows by putting `P=C-M` and using symmetric multipliers off the
band. A sufficiently large diagonal is a strict primal point, so conic strong
duality holds. The certificate proof below needs only weak duality.

## 4. Material objection M-1

M227 section 2 says restriction of an arbitrary full primal point to the
first six coordinates has the same objective. This is false: permitted
entries involving coordinate six can contribute

```text
2 sum_(i<6) G_(i,6)C_(i,6)+G_(6,6)C_(6,6),            (4.1)
```

and PSD domination does not force them to vanish. Therefore primal
restriction alone proves no equality between the six- and seven-coordinate
optima. Moreover, M227's six-dimensional dual matrices are not themselves
feasible points of the declared seven-dimensional dual. This is a material
gap in the frozen proof.

## 5. Exact full-dimensional salvage

Let `Xbar_w` be M227's six-dimensional rational dual matrix, independently
transcribed and verified in M230. Its exact entries and all active `LDL^T`
pivots are frozen in `results.json`. Complete it as

```text
X_w = [ Xbar_w  y_w ]
      [ y_w^T   G_66].                                  (5.1)
```

For width one, set

```text
y_1=(G_56/G_55)Xbar_1[:,5]=(869/1494)Xbar_1[:,5].      (5.2)
```

Then `(X_1)_(5,6)=G_56`, and its final Schur/`LDL^T` pivot is

```text
G_66-G_56^2/G_55=25/747>0.                             (5.3)
```

For width two, set

```text
y_2=(-43/54)Xbar_2[:,4]+(419/324)Xbar_2[:,5].          (5.4)
```

These coefficients solve the exact `G_{4,5}` clique equations, so
`(X_2)_(4,6)=G_46` and `(X_2)_(5,6)=G_56`. The final pivot is

```text
G_66-[G_46 G_56]G_{4:5,4:5}^{-1}[G_46 G_56]^T
=97/3564>0.                                            (5.5)
```

All earlier pivots equal the six positive active pivots. Hence both full
matrices are positive definite and agree with `G` everywhere on their
respective bands. Their exact entries and complete seven-pivot lists are in
`results.json`; their digests are

```text
w=1 73f302213b3de78b2da2b4bba7968d59c2fab0aa93a2f6548be13ac02ec4f6d6
w=2 4d70d7645a7f74443a2c7c575279cfc065e794512bc588323607b5b8ebdb7190
```

Because `e_6=0`, these completions preserve the dual objectives. Conversely,
zero-extending each six-dimensional primal matrix gives a full bandwidth-`w`
matrix whose slack is the direct sum of the positive-definite active slack
and zero; its objective is unchanged. Thus the independently corrected full
certificates prove

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,     (5.6)
167478197/630630000 <= p_2 <= 894863807/3363360000.     (5.7)
```

Exact subtraction gives

```text
lower(p_1)-upper(p_2)=10951531/155232000>0,
lower(p_1)-1/4       =15605731/180180000>0,
lower(p_2)-1/4       = 9820697/630630000>0.             (5.8)
```

Therefore the corrected theorem is `p_1>p_2>1/4` for this atom. No exact
optimum is claimed.

## 6. General rank-one formulation and bookkeeping

For `L=n+h`, exact Bernstein elevation is

```text
(E_(n,L)z)_r
 =sum_k z_k C(n,k)C(h,r-k)/C(L,r),                    (6.1)
```

with out-of-range binomial terms zero. Thus `zz^T` elevates to
`(E_(n,L)z)(E_(n,L)z)^T`, and its least declared band charge has precisely
the primal/dual form (3.1) with `e=E_(n,L)z`.

For a surviving branch weight `lambda=eta/pi_a>0`, scaling `M,C` by `lambda`
preserves PSD domination and scales both objectives by `lambda`. The envelope
acts after branch construction and creates no branch, so killed `a=d`
branches remain absent.

This supplies no degree-uniform factor, branch aggregation, recursive closure
or contraction, all-state theorem, gap, mixing statement, or Terminal result.

## 7. Reproducibility

```text
python3 -B fresh_referee_exact.py --output results.json
```

Python 3.12.3, standard library only, exact `Fraction`, `seed=null`. The
checker reads/imports no M227 code or data.

