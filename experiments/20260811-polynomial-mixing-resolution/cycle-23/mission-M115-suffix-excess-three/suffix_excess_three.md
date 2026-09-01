# M115 suffix-excess-three full-excursion theorem

## 1. Scope, convention, and theorem

This note concerns only the auxiliary full **nonlazy stationary-flow
parking-degree projection** in the minimal-long-cycle sector.  It is not a
mixing theorem for the original lazy `{3,4,5}` heat-bath chain.  Permutations
compose as `(pq)(x)=p(q(x))`, with factors displayed left-to-right.

Use the accepted notation

```text
w_n=n^(n-1)/n!,
q_(s,B)=w_(s+1-B)w_B/w_(s+1),
H=A_0+QH=(I-Q)^(-1)A_0,
G=A+QG=(I-Q)^(-1)A.
```

Every `j=1,...,k` attachment rank is retained in `Q`; only `j=0` and
inactive targets are killed.  M109/M114 prove `G<=H` term by term and prove
`H<=q(1-q)` for right-heavy suffix excess `L<=2`, as well as the terminal
`L=0` bound for every reachable `(K,R)`.

> **Theorem (suffix-excess-three full-excursion contraction).**  For every
> `s>=4`, `K>=1`, and right-heavy context
> ```text
> x=(s,K,K-1,B),  B=s-3,
> ```
> the complete finite-DAG excursion obeys
> ```text
> H(x)<=q_x(1-q_x),  G(x)<=U(x)=q_x(1-q_x).
> ```

This extends the accepted boundary theorem exactly one layer, from `L<=2`
to `L<=3`.  It does not imply the all-`L` excursion statement, an auxiliary
gap, ROOT-MEAN LIFT, an original-chain gap, or either project terminal.

## 2. Parameters and the eight supported compositions

Put

```text
r=w_s/w_(s+1),       u=w_(s-1)/w_s,
v=w_(s-2)/w_(s-1),   y=w_(s-3)/w_(s-2),
a=uvy,                b=vy,
c=(3/2)a,             q=(8/3)ruvy,
hbar=(s-1)/(s+1),     h1=(s-3)/(s-1),
z=1/(K+1),
d=2z^2/(1+z),
e=6z^3/[(1+z)(1+2z)].
```

Here `q=q_(s,B)` because `w_4=8/3`.  The root-composition law and contextual
mean are

```text
rho(c_1,...,c_k)=prod_i w_(c_i)/(k! w_(s+1)),
f(k,t)=
  K binom(k+K-R-2,K-R-1)/binom(k+K-1,K-1),  t=B,
  q_(t-1,B)[1-binom(K,R+1)/binom(K+k,R+1)], t>B,
  0,                                                   t<B.
```

At `R=K-1`, direct substitution gives exactly eight supported ordered
compositions:

```text
composition       rho                         f
(3,B)             9q/32                       2z
(1,2,B)           q/16                        3d
(2,1,B)           q/16                        3d
(1,1,1,B)         q/64                        4e
(2,s-2)           3q/(16y)                    y(1-d)
(1,1,s-2)         q/(16y)                     y(1-e)
(1,s-1)           3q/(16vy)                   vy(1-d)
(s)               r                           (3/2)a(1-z).
```

Their `rho*f` sum is `q`.  Positivity of `f` occurs in the seven groups

```text
(1,s), (2,B), (2,s-2), (2,s-1),
(3,B), (3,s-2), (4,B),
```

where group `(2,B)` contains `(3,B)`, group `(3,B)` contains the two ordered
compositions of three into two parts, and group `(4,B)` contains
`(1,1,1,B)`.  This distinction between eight compositions and seven `(k,t)`
groups is used below.

## 3. Seven exceptional canonical basins

For a canonical endpoint `E=(A,c_2,...,c_k)`, let `B_E` consist of all
sources `(alpha,c_2,...,c_k)` with `alpha` an ordered composition of `A`.
Its current and scaled capacity are

```text
theta_E=sum_(C in B_E) rho(C)[f(C)-q],
cap_E=k rho(E).
```

An ordinary basin contains none of the eight supported compositions, so
`theta_E=-q rho(B_E)`.  The accepted estimate
`rho(B_E)/rho(E)<=k` bounds its energy by `q^2 rho(B_E)`.

Exactly seven basins are exceptional.  The table lists their full nesting;
`mass/q` counts supported source mass in the basin, with multiplicity across
nested basins.

```text
endpoint E       supported sources in B_E                  mass/q
(1,1,1,B)        (1,1,1,B)                                 1/64
(2,1,B)          (2,1,B), (1,1,1,B)                        5/64
(1,2,B)          (1,2,B)                                   1/16
(3,B)            (3,B), (1,2,B), (2,1,B), (1,1,1,B)       27/64
(1,1,s-2)        (1,1,s-2)                                 1/(16y)
(2,s-2)          (2,s-2), (1,1,s-2)                        1/(4y)
(1,s-1)          (1,s-1)                                   3/(16vy).
```

Thus their supported basin mass with multiplicity is

```text
q[37/64+5/(16y)+3/(16vy)].                       (3.1)
```

The endpoint `(1,1,1,B)` and `(1,1,s-2)` reset targets have rank one and
are inactive.  Adding these two edges, and any inactive ordinary edges, only
increases the nonnegative reset-energy upper bound.  This permits a clean
partition using the full canonical path height
`E[degree(root)-1]=hbar`.

Direct current/capacity substitution gives the seven exceptional energy
terms after division by `q`:

```text
endpoint          theta_E/q                              cap_E/q    energy/q
(1,1,1,B)         (4e-q)/64                              1/16       (4e-q)^2/256
(2,1,B)           (12d+4e-5q)/64                         3/16       (12d+4e-5q)^2/768
(1,2,B)           (3d-q)/16                              3/16       (3d-q)^2/48
(3,B)             (36z+24d+4e-27q)/64                    9/16       (... )^2/2304
(1,1,s-2)         [y(1-e)-q]/(16y)                       3/(16y)    [y(1-e)-q]^2/(48y)
(2,s-2)           [4y-3yd-ye-4q]/(16y)                   3/(8y)     [... ]^2/(96y)
(1,s-1)           3[vy(1-d)-q]/(16vy)                    3/(8vy)    3[vy(1-d)-q]^2/(32vy).
```

Combining (3.1), the ordinary-basin bound, and these exact currents yields

```text
A_0(x)/q <= R_s(z),

R_s(z)=q[hbar-q(37/64+5/(16y)+3/(16vy))]
 +(4e-q)^2/256
 +(12d+4e-5q)^2/768
 +(3d-q)^2/48
 +(36z+24d+4e-27q)^2/2304
 +[y(1-e)-q]^2/(48y)
 +[4y-3yd-ye-4q]^2/(96y)
 +3[vy(1-d)-q]^2/(32vy).                         (3.2)
```

This is an upper bound, not an equality, precisely because ordinary basins
use `beta_E<=degree(E)` and inactive edges were added.

## 4. Standalone non-right-heavy `L=1` proposition

The group `(2,s-1)` creates one non-right-heavy child, so M109's right-heavy
`L=1` theorem cannot simply be quoted for both ranks.  The needed replacement
is the following direct bound.

> **Proposition (general-attachment one-layer envelope).**  Let
> ```text
> X=(S,K_0,R_0,S-1),  S>=2, K_0>R_0>=1,
> D=K_0-R_0,  p=D/(K_0+1),
> y_0=w_(S-1)/w_S,
> b_0=w_(S-1)/w_(S+1),
> h_0=(S-1)/(S+1).
> ```
> Then the complete unweighted excursion satisfies
> ```text
> H(X)/b_0 <= F_(b_0,y_0,h_0)(p),
> F_(b,y,h)(p)=b(h-b/2)+(2p-b)^2/4+(1-p)(1-y).     (4.1)
> ```

**Proof.**  Exactly two root compositions have nonzero contextual mean:

```text
composition    mass       mean
(1,S-1)        b_0/2      2p
(S)            b_0/y_0    y_0(1-p).
```

Their weighted mean is `b_0`.  The first composition is the only exceptional
basin and is singleton, with score
`(b_0/2)(2p-b_0)` and scaled capacity `b_0`.  All ordinary basins are bounded
using `beta_E<=degree(E)` and have total path mass at most
`h_0-b_0/2`.  Hence

```text
A_0(X)<=b_0^2(h_0-b_0/2)+(b_0/4)(2p-b_0)^2.       (4.2)
```

The unary group is the sole possible deep group.  Its mass is `b_0/y_0`,
its killed rank has mass `p`, and its sole retained rank has mass `1-p`.
The child is

```text
(S-1,K_0+1,R_0+1,S-1),
```

so it is suffix-terminal and has split `y_0`.  Its deficit remains `D`: it
is right-heavy exactly when `D=1`, and is non-right-heavy when `D>1`.
The accepted suffix-terminal theorem applies to **every** reachable deficit,
not only right-heavy ones, and bounds its excursion by `y_0(1-y_0)`.  Thus
the deep charge is

```text
(b_0/y_0)(1-p)y_0(1-y_0)
 =b_0(1-p)(1-y_0).
```

Adding this to (4.2) and dividing by `b_0` proves (4.1).  When `S=2`, the
nominal reset and deep targets of rank one are inactive; adding the displayed
nonnegative reset charge and the zero deep charge (`y_0=1`) preserves the
bound. QED.

The proposition bounds `H/b_0`; it does **not** assert
`H/[b_0(1-b_0)]<=1` for arbitrary `p`.

## 5. Every live group and the descendant normalization

Only four groups can send live mass.  In the first two, every displayed
`j` is retained before aggregation:

```text
group (k,t)  root mass       killed       retained             child sector
(2,s-2)      3q/(16y)        j=0:d        j=1,2:1-d           L=0, split y
(3,s-2)      q/(16y)         j=0:e        j=1,2,3:1-e         L=0, split y
(2,s-1)      3q/(16vy)       j=0:d        j=1:nu_1, j=2:nu_2 L=1, split b=vy
(1,s)        r               j=0:z        j=1:1-z             RH L=2, split c.
```

Here

```text
nu_1=2z(1-z)/(1+z),       nu_2=(1-z)/(1+z),
p_1=2z/(1+2z),            p_2=z/(1+2z).
```

For `(2,s-1)`, the `j=1` child has deficit two and attachment parameter
`p_1`; the `j=2` child is right-heavy and has parameter `p_2`.  Applying
(4.1) with `(b_0,y_0,h_0)=(b,y,h1)` gives

```text
H(child_j)<=b F_(b,y,h1)(p_j).
```

Multiplication by the parent root mass and division by the parent `q` tracks
the normalization exactly:

```text
[3q/(16b)] sum_(j=1)^2 nu_j H(child_j) / q
 <=(3/16)[nu_1 F(p_1)+nu_2 F(p_2)].                (5.1)
```

The two terminal groups use the universal `L=0` theorem; the unary group
uses the accepted right-heavy `L=2` theorem and
`(r/q)c=9/16`.  Therefore all descendants add at most

```text
D_s(z)= [3(1-d)+(1-e)](1-y)/16
 +(3/16)[nu_1 F_(b,y,h1)(p_1)+nu_2 F_(b,y,h1)(p_2)]
 +(9/16)(1-z)(1-c).                                (5.2)
```

At `s=4`, the first two nominal groups have rank-one children and are
inactive.  Since then `y=1`, their displayed charge is zero, so (5.2)
remains valid without a boundary exception in the formula.

Equations (3.2) and (5.2) prove the full all-depth envelope

```text
H(x)/q <= E_s(z):=R_s(z)+D_s(z).                   (5.3)
```

No one-step or two-layer defect sign is used.

## 6. Exact universal sign certificate

It remains to show `E_s(z)<=1-q` for every `s>=4` and
`0<z<=1/2`.  Clear the positive denominator:

```text
T_s(z)=1728(1+z)^2(1+2z)^2[1-q-E_s(z)].            (6.1)
```

Direct algebra shows that `T_s` is a polynomial of degree at most six.

### Finite ranks `4<=s<=20`

For each of these seventeen exact Cayley-ratio tuples, `l3_exact.py`
interpolates (6.1) with `Fraction` arithmetic and converts it to the
degree-six Bernstein basis on `[0,1/2]`.  Every one of the 119 coefficients
is strictly positive.  The smallest coefficient for `s=4,...,20` is,
respectively, approximately

```text
129.7629, 54.3424, 46.6905, 45.5537, 45.6444, 46.0051,
46.4027, 46.7746, 47.1064, 47.3980, 47.6535, 47.8780,
48.0760, 48.2515, 48.4079, 48.5480, 48.6742.
```

All exact numerators and denominators are stored in `l3_exact.json`.
Positivity of Bernstein coefficients proves `T_s(z)>0` on the whole interval;
this is not an extrapolation from sampled `z` values.

### All ranks `s>=21`

Let `b_n=w_n/w_(n+1)=(n/(n+1))^(n-1)`.  The accepted monotonicity and lower
bound give `b_n>1/3`, while

```text
b_18=(18/19)^17<2/5.
```

Because `r,u,v,y` are consecutive ratios with smallest index `s-3>=18`,

```text
(r,u,v,y) in [1/3,2/5]^4.                          (6.2)
```

Replacing `hbar` and `h1` by one only increases the right side of (5.3).
For that enlarged envelope, the cleared slack `T^+` has multidegree at most

```text
(2,2,2,2,6) in (r,u,v,y,z).
```

After the affine map of `[1/3,2/5]^4 x [0,1/2]` to the unit five-cube, its
complete tensor Bernstein expansion has

```text
3*3*3*3*7=567
```

coefficients.  `l3_exact.py` derives all of them using independent tensor
Lagrange interpolation and exact rational arithmetic.  Every coefficient is
positive; the minimum is

```text
682328/28125
```

at tensor index `(2,2,2,0,0)`.  Thus `T^+>0` on the full box, so
`T_s>=T^+>0` for every actual tuple in (6.2).  This proves
`E_s(z)<1-q` for `s>=21` and completes the universal scalar sign.

Combining Sections 2--6 proves `H<=q(1-q)`.  Since the positive history
expansion gives `G<=H` and the seed is right-heavy,
`U=q(1-q)K/(R+1)=q(1-q)`.  The theorem follows. QED.

## 7. Independent checks and limitations

`l3_exact.py` reconstructs the grouped all-`j` recurrence, scalar reset
energy, support/live tables, closed envelope, 17 finite certificates, and all
567 box coefficients with exact standard-library arithmetic.  Its bounded
full-resolvent audit covers `4<=s<=20`, `K in {1,2,5,64}` with zero failures.

`independent_l3_audit.py` is a second implementation path: it enumerates every
ordered composition literally, constructs every canonical basin by all
refinements of its first part, computes each current/capacity directly, and
sums individual live attachment ranks recursively.  On all 56 right-heavy
rows `4<=s<=10`, `1<=K<=8`, it verifies

```text
exact reset <= reset envelope,
exact resolvent <= complete envelope <= q(1-q)
```

with exact fractions and zero failures.  These bounded comparisons audit the
formulas; the Bernstein arguments supply analytic completeness.

The strongest limitation is structural: exceptional-basin counts grow with
suffix excess, and this proof gives no uniform-in-`L` organization.  It
therefore removes only the first open boundary `L=3`; the universal
full-excursion contraction now begins at `L=4`.
