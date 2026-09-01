# M221 exact minimal-bandwidth theorem

Date: 2026-08-13 UTC.

## 1. Scope and status

This note proves a finite-row statement about the normalized fresh
first-Jacobi actual kernel at `(B,L,kappa,D)=(1,6,2,1)`. It determines the
least bandwidth in one declared degree-six Bernstein coefficient cone. It
does not construct a recursive supersolution and proves no contraction,
total-AMV, spectral-gap, mixing, or Terminal statement.

## 2. Coefficient cone and charge matrix

Put

```text
b(u)=(b_(6,0)(u),...,b_(6,6)(u))^T,
b_(6,j)(u)=C(6,j)u^j(1-u)^(6-j).
```

The evaluation matrix of these seven functions at seven distinct points is
invertible. Hence `b(u)^T M b(v)` is a PSD kernel iff the symmetric
coefficient matrix `M` is PSD. For `w=0,...,6`, define

```text
B_6^(w)={b(u)^T C b(v): C>=_PSD0,
         C_ij=0 whenever |i-j|>w}.                    (2.1)
```

Write the exact actual kernel as `K=b^T A b`. For uniform `U`, the fresh
first-Jacobi functional is

```text
Q[H]=E H(U,U)
     -12 E E'[(U-1/2)(U'-1/2)H(U,U')].               (2.2)
```

Thus there is an exact PSD charge matrix `G` with

```text
Q[b^T C b]=<G,C>,
G_ij=E[b_i(U)b_j(U)]
     -12 E[(U-1/2)b_i(U)]E[(U-1/2)b_j(U)].            (2.3)
```

Here `<M,N>=Tr(MN)=sum_ij M_ij N_ij` for symmetric matrices.

## 3. Exact primal and dual

Let `beta=1-q`. The least possible charge in bandwidth `w` is

```text
p_w=min <G,C>
    subject to C-A>=_PSD0,
               C_ij=0 for |i-j|>w.                   (P_w)
```

The explicit condition `C>=0` is redundant because the actual kernel is PSD.
To derive the dual, put `P=C-A`. Then `P>=0` and
`P_ij=-A_ij` off the width-`w` band. A symmetric multiplier `Y` supported
off that band gives `X=G+Y`; minimizing the Lagrangian over `P>=0` yields

```text
d_w=max <A,X>
    subject to X>=_PSD0,
               X_ij=G_ij for |i-j|<=w.               (D_w)
```

For sufficiently large rational `t`, `C=tI` has bandwidth zero and
`tI-A>0`. Therefore every `(P_w)` has a strict feasible point and conic strong
duality applies. For the minimal-bandwidth decision below, only weak duality
is needed: a dual value above `beta` obstructs the budget, and a primal point
at or below `beta` proves feasibility.

## 4. Exact reconstruction

The standalone checker reconstructs the reset/history recursion using grouped
Cayley root masses, every exterior `eta`, the single `1/pi_a`, and deletion of
killed `a=d`. It imports and reads no predecessor code or data. It obtains 49
nonzero monomial coefficients and the digests

```text
actual kernel       d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
A coefficient       d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
G charge matrix     9bd460a8da3fbf2a7f3dd8698eae88116bb1608dc2b1db9746ddfd9b1b2f5c0c
```

The first two match the independently accepted M216/M219 reconstruction. It
also gives

```text
q=117649/262144,
beta=1-q=144495/262144.
```

## 5. Width zero is impossible

Let

```text
sign=(-1,-1,-1,+1,+1,+1,+1),
r=(1/5,4/25,17/100,9/50,17/100,4/25,1/5),
v_j=sign_j r_j,
X_0=vv^T+diag(G_jj-r_j^2).
```

The seven diagonal remainders are

```text
(633/254800, 18427/17517500, 39213/17517500,
 6757/7507500, 39213/17517500, 18427/17517500,
 633/254800),
```

all positive. Hence `X_0>=0` and `(X_0)_jj=G_jj`, so `X_0` is feasible for
`(D_0)`. Exact contraction gives

```text
<A,X_0>-beta
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.     (5.1)
```

By weak duality, no diagonal degree-six Bernstein kernel can dominate `A`
and meet the budget.

## 6. Width one is feasible

Let `C_1` be the symmetric tridiagonal matrix with

```text
diag(C_1)
=(101/50,111/100,43/100,19/25,39/25,99/50,21/5),

(C_1)_(i,i+1)
=(1/3,2/15,1/12,1/5,3/5,11/8).                     (6.1)
```

All other entries vanish. The exact strict signed-diagonal-dominance margins
of `C_1` are

```text
(253/150,193/300,16/75,143/300,19/25,1/200,113/40),
```

so `C_1>0`. Direct subtraction gives a symmetric matrix `C_1-A` whose seven
strict signed-diagonal-dominance margins are positive; the smallest is

```text
22066085580152050340437577895121
/9632366434287095922007474176000000 > 0.             (6.2)
```

Therefore `C_1-A>0`, so the kernel in (6.1) PSD-dominates the actual kernel.
Its exact charge and slack are

```text
<G,C_1>=4937603/9172800,

beta-<G,C_1>
=485323987/37571788800 > 0.                          (6.3)
```

Combining (5.1) and (6.1)--(6.3) proves:

> **Theorem (exact minimal bandwidth at the decisive row).** For the actual
> fresh kernel at `(B,L,kappa,D)=(1,6,2,1)`, the least integer `w` for which
> some `J in B_6^(w)` PSD-dominates the actual kernel and satisfies
> `Q[J]<=1-q` is exactly `w=1`.

This is existence at one row, not the optimum value `p_1` and not a recursive
construction.

## 7. Retained-lift stability

Likelihood multiplication is exact:

```text
b_(d,a)b_(ell,j)
 =[C(d,a)C(ell,j)/C(d+ell,a+j)]b_(d+ell,a+j).         (7.1)
```

If `d+ell=L`, (7.1) shifts both coefficient indices by `a` and rescales them
diagonally, so it preserves bandwidth exactly. If `n=d+ell<L` and
`h=L-n`, degree elevation sends index `k` into the interval
`{k,...,k+h}`. Consequently an exact raw width-`w` coefficient matrix can
acquire bandwidth as large as

```text
min(L,w+h).                                           (7.2)
```

The loss is real. Take the width-one degree-one rank-one child coefficient
matrix generated by vector `(1,1)`. Under the retained likelihood
`d=1,a=0`, its degree-two feature vector is `(1,1/2,0)`. Elevation to cap six
gives

```text
(1,5/6,2/3,1/2,1/3,1/6,0),
```

whose outer product has bandwidth five. Thus the raw fixed-width-one cone is
not closed under unsaturated retained lifts.

A coarse positive-linear stabilization always exists: for a PSD lifted
coefficient matrix `M`,

```text
Env(M)=Tr(M)I >=_PSD M.
```

This lands in bandwidth zero, hence inside bandwidth one, but no charge bound
is proved for it. Constructing a cost-controlled reset/lift envelope that
returns to bandwidth one at every reachable state remains unresolved. The
one-row matrix `C_1` does not supply that recursion.

## 8. Boundary and limitations

No adjacent row was needed. The theorem does not determine `p_1`, prove
closure of a recursive width-one ansatz, treat arbitrary `L`, or address the
larger all-degree dictionary. It does not imply fresh contraction, total AMV,
a spectral gap, polynomial mixing, or Terminal A/B.

## 9. Reproducibility

```text
python3 -B banded_bernstein_exact.py --output results.json
```

The checker uses Python 3.12.3 standard-library `Fraction` arithmetic,
`seed=null`, one top row and its forced descendants, and no numerical SDP in
any promoted check.

