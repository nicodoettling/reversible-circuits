# M178 proof audit of frozen M174

Date: 2026-08-13 UTC.

Status: **M174's strict reduction is correct.**  The boundary-response lemma
`(BR)` and PCS-bound remain **unresolved**.  This audit supplies the uniform
remainder estimate that M174 cited but did not display.

## 1. Exact probability interface

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  Put
`n=3k`, odd `k>=3`, `h=(0 1 ... n-1)`,

```text
A=(0,k,2k),                    B=(0,1)(k,2k).
```

For either source `g`, a uniform minimal factorization of `g^-1 h` has
length `n-3`.  If its first two factors have product `s`, the number of raw
ordered lifts is `a(s)` (three for a triangle and two for a double), and the
remaining completion count is

```text
C_g(s)=F_(n-5)((gs)^-1 h).
```

Thus, with `A_g=F_(n-3)(g^-1h)`, the exact product law is

```text
P_g(s)=a(s) C_g(s)/A_g.                              (1.1)
```

For `q=s^-1h`, let `S(s)` be the literal all-phase PC sum and
`A_s=F_(n-3)(q)`.  Therefore `f(s)=S(s)/A_s`, and direct conditioning gives

```text
Delta(C_k)=sum_s [P_B(s)-P_A(s)] f(s).               (1.2)
```

M168's already-audited physical event identity gives

```text
sum_y z_k(y)=2 Delta(C_k)/pi_y.                      (1.3)
```

For a fixed boundary double, the residual cycle sizes are `(1,1,n-2)`, so

```text
F_(n-3)(1,1,n-2)=(n-3)! tau(n-2)=(n-2)^(n-4),
pi_y=2n(n-2)^(n-4)/n^(n-2)
    =2/(n-2) (1-2/n)^(n-3).                          (1.4)
```

For `n>=9`, `e^-2 <= (1-2/n)^(n-3) <= 1`; the lower bound follows from
`log(1-x)>=-x/(1-x)`.  Since `k=n/3`, equations (1.3)--(1.4) prove

```text
k |sum_y z_k(y)|=O(1)  iff  n^2 |Delta(C_k)|=O(1).  (1.5)
```

Let `P_(g,j)` be M91's subprobability channel measures of common mass
`alpha_j`.  For `j=1,2`, define

```text
mu_j=(P_(B,j)+P_(A,j))/(2 alpha_j),
sigma_j=(P_(B,j)-P_(A,j))/(P_(B,j)+P_(A,j)).
```

Then `mu_j` is a probability measure, `E_(mu_j)sigma_j=0`, and

```text
P_(B,j)-P_(A,j)=2 alpha_j sigma_j mu_j.
```

The `J=0` measures agree, so (1.2) becomes exactly

```text
Delta(C_k)=2 sum_(j=1)^2 alpha_j Cov_(mu_j)(f,sigma_j). (1.6)
```

No Poincare inequality is used.

## 2. Component response and cycle-index shifts

For a minimal permutation with cycle sizes `d_i`,

```text
F_L=L! product_i tau(d_i),       tau(d)=d^(d-1)/d!.
```

A one-run residual component of size `d` has `g=d-1` generic boundary
edges and `(d-2)_+` adjacent generic pairs.  A two-run component with
positive run lengths `a,b`, `d=a+b`, has `g=d-2` and
`(a-2)_+ +(b-2)_+` adjacent pairs.  Dividing the post-cut completion count
by `A_s` gives exactly

```text
U_1(d)=(d-1) tau(d-1)/tau(d),
V_1(d)=(d-2)(d-3) tau(d-2)/tau(d),

U_2(a,b)=(d-2) tau(d-1)/tau(d),
V_2(a,b)=((d-2)(d-3)-2[(a-2)_+ +(b-2)_+])
             tau(d-2)/tau(d),                        (2.1)
```

with a zero contribution whenever a shifted subscript is invalid.  Hence

```text
f(s)=1/R_n [sum_i V_i+2 sum_(i<j) U_i U_j],
R_n=(n-3)(n-4).                                      (2.2)
```

Literal residual-cycle inspection gives three one-run components for a
triangle and two one-run plus one two-run component for a double.  The
clean-room checker verifies (2.2) against the literal all-phase sum for all
64 source-accessible intermediates at `k=3` and all 810 at `k=5`.

For `T(z)=sum_(d>=1)tau(d)z^d`, index shifting gives

```text
sum tau(d)U_1(d)z^d
 =sum (d-1)tau(d-1)z^d=z^2T'(z),

sum tau(d)V_1(d)z^d
 =sum (d-2)(d-3)tau(d-2)z^d=z^4T''(z).               (2.3)
```

The two-run expression in (2.1), summed over positive `a,b`, is indeed a
bivariate positive-composition convolution with the displayed boundary
correction.  M174 does not display a further closed bivariate series; none is
needed for its strict reduction.

## 3. Rigorous uniform decoration bound

This section supplies the detail omitted after M174 equation (3.1).  For
`d>=2`, direct cancellation of factorials gives

```text
A_d:=tau(d-1)/tau(d)=(1-1/d)^(d-2).                  (3.1)
```

Using

```text
|log(1-x)+x+x^2/2| <= x^3/[3(1-x)]     (0<=x<1),
```

one obtains

```text
log(e A_d)=3/(2d)+epsilon_d,       |epsilon_d|<=1/d^2.
```

Since `|3/(2d)+epsilon_d|<=2/d<=1`, Taylor's theorem for the exponential
then gives the explicit bound

```text
e A_d=1+3/(2d)+rho_d,
|rho_d| <= (1+2e)/d^2.                              (3.2)
```

Consequently

```text
u_1(d)=e(d-1)A_d-d-1/2
      =-3/(2d)+(d-1)rho_d,

u_2(a,b)=e(d-2)A_d-d+1/2
        =-3/d+(d-2)rho_d,                            (3.3)
```

so both are uniformly bounded.  The invalid `d=1` one-run case and the
minimal `d=2` two-run case are finite and agree with the zero-subscript
convention.

For `d>=4`, likewise

```text
B_d:=tau(d-2)/tau(d)
    =(1-1/d)(1-2/d)^(d-3).                           (3.4)
```

Applying the same logarithm remainder separately to `1/d` and `2/d` gives

```text
log(e^2 B_d)=3/d+delta_d,       |delta_d|<=9/d^2.
```

Here `|3/d+delta_d|<=21/16`.  Thus

```text
e^2 B_d=1+3/d+theta_d,
|theta_d|<=C_0/d^2,
C_0=9+(441/32)e^(21/16).                             (3.5)
```

For one run, with `D_1=(d-2)(d-3)=d^2-5d+6`,

```text
v_1(d)=D_1(1+3/d+theta_d)-d^2+2d
      =-9+18/d+D_1 theta_d.                          (3.6)
```

Because `0<=D_1<=d^2`, this is uniformly bounded.

For two positive runs, put

```text
I=1[a=1]+1[b=1].
```

The boundary correction is exact:

```text
(a-2)_+ +(b-2)_+=d-4+I,
D_2=(d-2)(d-3)-2[(a-2)_+ +(b-2)_+]
   =d^2-7d+14-2I.                                   (3.7)
```

Moreover `D_2` counts ordered disjoint pairs, so `0<=D_2<=d^2`.  Therefore

```text
v_2(a,b)=D_2(1+3/d+theta_d)-d^2+4d
        =-7-2I+(42-6I)/d+D_2 theta_d,                (3.8)
```

which is uniform over **all** positive `a,b`.  The remaining `d=2,3` cases
have zero `V_2` numerator and are finite.  Equations (3.2)--(3.8) rigorously
prove the uniform boundedness of all four M174 residual decorations.

## 4. Affine constants

Write, exactly,

```text
e U_i=d_i+epsilon_i+u_i,
e^2 V_i=d_i^2-c_i d_i+v_i,
```

where `(epsilon,c)=(1/2,2)` for one run and `(-1/2,4)` for two runs.  The
quadratic response in (2.2) is `(sum_i d_i)^2=n^2`.  Its deterministic
linear part is

```text
-sum_i c_i d_i
+2 sum_(i<j)(d_i epsilon_j+d_j epsilon_i).            (4.1)
```

For a triangle, all three components are one-run.  The two terms in (4.1)
are `-2n` and `+2n`, so

```text
L_T=0.
```

For a double, let `d_*` be the two-run component size.  The first term is
`-2(n-d_*)-4d_*=-2n-2d_*`, while the epsilon cross term is `2d_*`.  Hence

```text
L_D=-2.
```

This is a pointwise kind calculation.  Any transient value `7/5` results
from averaging incompatible kind/source weights before the pointwise affine
expansion and is **rejected**.  The clean-room script checks the full M174
boundary formula coefficientwise as a polynomial in a formal variable `E`
for every source-accessible `k=3,5` intermediate; it does not substitute a
floating approximation to `e`.

## 5. Exact kind transfer

Put `m=k-1`.  M91's literal ordered-color calculation gives

```text
alpha_2=2m(2m-1)/[(3m)(3m-1)]
       =2(2k-3)/[3(3k-4)].                           (5.1)
```

In channel `J=2`, the merged source has triangle probability `3/(2k-1)`.
For the split source, the two factors first choose the same `k`-cycle with
probability `(k-2)/(2k-3)`, then form a triangle with probability `3/k`.
Thus

```text
eta(T)=alpha_2 [3/(2k-1)-3(k-2)/(k(2k-3))].          (5.2)
```

The bracket simplifies independently to

```text
6(k-1)/[k(2k-3)(2k-1)].
```

Multiplying by (5.1) gives exactly

```text
eta(T)=12(k-1)/[3k(3k-4)(2k-1)],
eta(D)=-eta(T).                                      (5.3)
```

The denominator in M174 is therefore correct.  `J=0` cancels as a measure;
every `J=1` pair has disjoint exterior/middle supports and hence is a double,
so its kind mass also cancels.

## 6. Reduction and equivalence

Let `eta=P_B-P_A`.  Since `eta(1)=0`, `L_T=0`, and `L_D=-2`, applying `eta`
to the exact affine response gives

```text
Delta(C_k)=e^-2/R_n [2n eta(T)+eta(B_k)].             (6.1)
```

Equation (5.3) makes `2n eta(T)=O(1)`.  Also

```text
10/27 <= R_n/n^2 < 1                  (n>=9).
```

Combining this with (1.5) and (6.1) proves both directions:

```text
PCS-bound  iff  eta(B_k)=O(1).                        (6.2)
```

The reverse direction uses
`eta(B_k)=e^2R_n Delta(C_k)-2n eta(T)`; it is not merely a sufficient
condition.

## 7. Exact finite falsification

The independent checker reconstructs the source laws from literal ordered
first and second transpositions and computes `f` by a literal sum over all
ordered disjoint boundary-edge phases.  Only afterward does it read M174's
frozen JSON.  At `k=3,5` it verifies:

- exact source normalization and M91 channel masses;
- equality of the full `J=0` measures;
- zero `J=0,1` kind transfer and (5.3) in `J=2`;
- literal response equals (2.2) for every accessible intermediate;
- the affine and signed reduction identities as formal polynomials;
- (1.4), and the exact event/signed-cell normalization.

The exact event contrasts are

```text
k=3: 10075637745539/306307575000000,

k=5: 73077925347453973355779108467047756359425607682995598110051
     /10875678960328172710976155821460639902556381186560000000000000.
```

The corresponding signed cell sums match frozen M174 exactly.  These are
finite exact facts only and imply no asymptotic bound.

## 8. Scope

This audit proves no `(BR)`, PCS-bound, FD-bound, FCL1, broad quotient bound,
direct-L1/H0/gap, original heat-bath mixing, or Terminal statement.
