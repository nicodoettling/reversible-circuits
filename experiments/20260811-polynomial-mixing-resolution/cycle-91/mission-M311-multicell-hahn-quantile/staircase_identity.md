# M311 Canonical Quantile Staircase and Sign Blocks

Date: 2026-08-14 UTC
Status: proved exact from accepted QTI_1 input

## 1. Setup

Fix odd `k>=3`, put `m=k-1` and `n=3k`, and fix
`1<=u<k/2`, `2<=ell<=n-2`.  The accepted positive masses satisfy

```text
A_c=sum_(i<=c)x_i,     B_d=sum_(j<=d)y_j,
A_0=B_0=0,             A_m=B_m=mu_k,
I_c=(A_(c-1),A_c],     J_d=(B_(d-1),B_d],
pi_cd=|I_c intersect J_d|.
```

Write

```text
D_cd=Xbar_c(k,u,ell)-Ybar_d(k,u,ell).
```

Every mean in `D_cd` contains the complete orbit of all `k` middle phases.
Accepted QTI_1 is

```text
P_(k,ell)(u)=sum_(c,d)pi_cd D_cd.                         (1.1)
```

## 2. Canonical monotone support path

Let

```text
0=t_0<t_1<...<t_s=mu_k
```

be the distinct sorted union of all cumulative endpoints `A_c,B_d`.
For each `r`, the interval `(t_(r-1),t_r]` lies in a unique pair
`I_(c_r),J_(d_r)`.  Its length is positive, and

```text
pi_(c_r,d_r)=t_r-t_(r-1).                                (2.1)
```

Conversely, a positive intersection `I_c intersect J_d` has no cumulative
endpoint in its interior, so it is exactly one such interval.  Therefore
`r -> (c_r,d_r)` lists every supported transport cell exactly once.

When a breakpoint is only `A_c`, the next cell increments the first
coordinate; when it is only `B_d`, it increments the second; and when it is
both, both coordinates increment.  Thus the support is a coordinatewise
nondecreasing staircase from `(1,1)` to `(m,m)`.  It has at most `2m-1`
cells, with equality when no internal `A_c` equals `B_d`.

This proves the path property without a genericity assumption and fixes the
orientation of its two axes.

## 3. Abel sign determines every off-diagonal rung

Set

```text
R_h=A_h-B_h,          h=0,...,m.                           (3.1)
```

For a supported cell let its rung be `h=min(c,d)`.

If `c>d`, then `h=d` and positive overlap implies

```text
A_d <= A_(c-1) < B_d,
```

so `R_h<0`.  If `c<d`, then `h=c` and positive overlap similarly implies

```text
B_c <= B_(d-1) < A_c,
```

so `R_h>0`.  Hence

```text
R_h<0: every off-diagonal rung-h cell has c>d;
R_h>0: every off-diagonal rung-h cell has c<d;
R_h=0: no off-diagonal rung-h cell exists.                (3.2)
```

The converses in `(3.2)` are intentionally not asserted: a sign need not
force an off-diagonal cell of that rung.  What is exact is that no rung can
contain both crossing directions.

## 4. Exact maximal sign-block partition

Define

```text
M_h=max(A_h,B_h),       h=0,...,m.                         (4.1)
```

For a mass point `t`, let `(c(t),d(t))` be its quantile cell.  Then

```text
min(c(t),d(t))>=a  iff  t>M_(a-1),
min(c(t),d(t))<=b  iff  t<=M_b.                            (4.2)
```

Indeed, both active indices are at least `a` precisely after both
`A_(a-1)` and `B_(a-1)` have been passed, and both exceed `b` precisely
after both `A_b` and `B_b` have been passed.  Therefore for every index
interval `[a,b]` the cells with `a<=min(c,d)<=b` form exactly the contiguous
path segment over

```text
(M_(a-1),M_b].                                             (4.3)
```

Because every `M_h` is itself a cumulative endpoint, `(4.3)` never slices a
supported cell.

Partition `{1,...,m}` into the unique maximal consecutive intervals

```text
H_q=[a_q,b_q]
```

on which `sgn(R_h)` is constant in `{-1,0,+1}`.  Call

```text
mathcal B_q={(c,d):pi_cd>0 and min(c,d) in H_q}            (4.4)
```

the corresponding Abel sign block.  Equations `(4.2)--(4.3)` show that the
`mathcal B_q` are consecutive maximal staircase segments, are pairwise
disjoint, and contain every supported cell exactly once.  Zero runs,
including the terminal `R_m=0` run, are retained as blocks rather than
silently merged or dropped.

## 5. Block decomposition identity

For every maximal sign block define

```text
C_q(k,u,ell)
 =sum_((c,d) in mathcal B_q) pi_cd(k) D_cd(k,u,ell)
 =integral_(M_(a_q-1))^(M_(b_q))
      [mathsf X(t)-mathsf Y(t)] dt.                        (5.1)
```

The exact partition proves

```text
P_(k,ell)(u)=sum_q C_q(k,u,ell).                           (QBD_1)
```

`(QBD_1)` is the strongest unconditional conclusion of this derivation.  It
is a rearrangement of QTI_1 along a canonical staircase partition, not a
positivity claim.
