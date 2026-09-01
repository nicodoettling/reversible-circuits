# M235 proof of the signed two-run coefficient moment

Date: 2026-08-13 UTC.

Status: **proved**, subject to fresh independent audit.  This proves exactly
M226/M229's standalone `(TCM)`.  It does not prove `(YCM)`, `(WBE)`,
`(DE)`, conditional `J2`, any downstream response, a gap, mixing, or a
Terminal.

## 1. Immutable interface and exact theorem

Use the convention `(pq)(x)=p(q(x))`, with displayed factors multiplying
left-to-right.  Put

```text
k >= 3 odd,       D=2k-1,       R=2k-3,       j=(k-1)/2,
2 <= ell <= (3k-1)/2,
b_r=e^(-r)r^(r-1)/r!,
K_R(r,d)=b_d b_(r-d)/(R b_r),             1<=d<r,
q_s=[k/(k-1)]b_s b_(k-s)/b_k,             1<=s<=j.
```

The `q_s` form a probability law.  In the accepted literal M199/M207 law,
let `T^B_(k,y)` and `T^A_(k,y)` be the q-averaged **raw** masses of the
unique complementary two-run face of size `y` on the B and A sides.  Each
ordered tuple contributes with multiplicity, even if two residual faces have
the same size.  Define

```text
T_B(k,ell)=sum_(y=2)^ell T^B_(k,y),
T_A(k,ell)=sum_(y=2)^ell T^A_(k,y).
```

By accepted M226/M229,

```text
sum_(y=2)^ell c^T_(k,y)=T_B(k,ell)-T_A(k,ell).       (1.1)
```

### Theorem (TCM)

Uniformly on the displayed integer domain,

```text
|T_B(k,ell)-T_A(k,ell)| <= 160 sqrt(ell)/k.          (1.2)
```

The constant is deliberately loose.  The proof in fact bounds both positive
raw masses separately.  Equation (1.1) then proves M226's signed two-run
coefficient moment `(TCM)`.

## 2. Elementary Borel estimates with explicit constants

The standard Stirling bounds

```text
sqrt(2 pi) r^(r+1/2)e^(-r) <= r!
 <= e r^(r+1/2)e^(-r)
```

give

```text
e^(-1)r^(-3/2) <= b_r <= (2 pi)^(-1/2)r^(-3/2).     (2.1)
```

In particular, whenever `v/2<=u<=v`,

```text
b_u/b_v <= [e/sqrt(2 pi)](v/u)^(3/2) < 4.           (2.2)
```

Also

```text
M(L):=sum_(r=1)^L r b_r <= sqrt(L),                 (2.3)
```

because `sum_(r<=L)r^(-1/2)<=2sqrt(L)` and
`2/sqrt(2pi)<1`.  The rooted-tree convolution is

```text
sum_(a=1)^(m-1)b_a b_(m-a)=2(m-1)b_m/m <=2b_m.      (2.4)
```

For `s<=j`, (2.1) gives

```text
q_s <=5b_s,          sum_s q_s s <=5sqrt(k).        (2.5)
```

We also use `sum_s q_s=1`, `sum_(r>=1)b_r=1`,
`R>=k`, and `D/R<=5/3`.  All hold at the smallest case `k=3`;
there is no omitted asymptotic threshold.

## 3. Exact B two-seam formula

Write the B exterior word as

```text
V=(1,...,k-1,2k,...,3k-1).
```

Its `D` directed edge increments around the ambient `3k`-cycle are one
except at two distinguished edges:

```text
Delta_beta=k+1,       Delta_sigma=2.                 (3.1)
```

Thus `beta` carries extra increment `k` and `sigma` extra increment one.
Fix first smaller split `s`, parent orientation
`r in {s,D-s}`, middle child length `d`, and put

```text
t=r-d.
```

The second chord has a placement `1<=a<=t-1`.  For cyclic first start `i`,
let

```text
E(i;r,d,a)=[i,i+a) union [i+a+d,i+r)                (3.2)
```

be the two retained boundary arcs, interpreted as a set of directed V-edges
modulo `D`.  It has exactly `t` edges.  M199's two one-run faces are the
outside first arc and the middle child; hence their complementary face is
exactly the retained union (3.2).  Its ambient size is therefore

```text
y_B(i;r,d,a)
 =t+k 1{beta in E(i;r,d,a)}
     +1{sigma in E(i;r,d,a)}.                       (3.3)
```

This identity retains a simultaneous hit of both seams, all same/cross
placements, both parent orientations, and every size collision.

The complete raw B prefix is consequently

```text
T_B(k,ell)
 =sum_(s=1)^j q_s (1/D) sum_(i=0)^(D-1)
   sum_(r in {s,D-s}) sum_(d=1)^(r-1) K_R(r,d)
   sum_(a=1)^(r-d-1) 1{2<=y_B(i;r,d,a)<=ell}.       (3.4)
```

Empty placement sums are zero.  Formula (3.4) is before any estimate and
contains the literal normalization `1/D` and placement multiplicity.

For fixed `r,d,a`, translation in `i` puts `beta` in the `t`-edge set
`E` exactly `t` times.  Since (3.3) is at least `t`, and a qualifying
placement with `t>ell-k` must exclude `beta`,

```text
(1/D)sum_i 1{y_B(i;r,d,a)<=ell}
 <=1{t<=ell-k}+[(D-t)/D]1{t<=ell}.                  (3.5)
```

The small seam can only increase (3.3), so retaining it can never invalidate
this upper bound.  Summing the `t-1` placements and using kernel symmetry
`K_R(r,d)=K_R(r,t)` gives

```text
T_B(k,ell)
 <=sum_s q_s sum_(r in {s,D-s}) sum_(t=2)^(r-1)
   (t-1)K_R(r,t)
   {1{t<=ell-k}+[(D-t)/D]1{t<=ell}}.                (3.6)
```

## 4. Uniform B bound

For the short parent `r=s`, the brace in (3.6) is at most
`2 1{t<=ell}`.  Cancelling `b_s` between `q_s` and `K_R(s,t)`, then
using (2.4) with `u=s-t`, gives

```text
B_short
 <=[3/R]sum_(t<=ell)t b_t
   [sum_(u=1)^(k-t-1)b_u b_(k-t-u)/b_k]
 <=(24/R)M(ell)
 <=24 sqrt(ell)/k.                                  (4.1)
```

Only `t<s<=j` occurs, so `k-t>=k/2` and (2.2) justifies the displayed
constant.

For the long parent put `r=D-s`.  The first indicator in (3.6) has
`t<=ell-k<=j`; then `r-t>=r/2`, and (2.2)--(2.3) give

```text
B_long,free <=4 sqrt(ell)/k.                        (4.2)
```

For the second indicator, first take `t<=r/2`.  Again (2.2) gives

```text
B_long,low <=4 sqrt(ell)/k.                         (4.3)
```

It remains to treat `t>r/2`.  Put `d=r-t`.  Here, and only here, the
long-parent parametrization gives the exact identity

```text
D-t=s+d.                                            (4.4)
```

By (2.2), `b_t/b_r<4`, while
`(t-1)/R<=D/R<=5/3`.  Each summand in this high range is therefore at most

```text
7[(s+d)/k]b_d.                                      (4.5)
```

Since `d<r/2<D/2<k`, (2.3), `sum b_d=1`, and (2.5) yield

```text
B_long,high <=42/sqrt(k).                           (4.6)
```

This range is nonempty only if

```text
ell>r/2 >=(D-j)/2=(3k-1)/4.
```

Hence `1/sqrt(k)<=sqrt(3/2)sqrt(ell)/k`, and (4.6) is at most
`52sqrt(ell)/k`.  Combining (4.1)--(4.3) and (4.6),

```text
T_B(k,ell) <=84 sqrt(ell)/k.                        (4.7)
```

## 5. Exact A marked and untouched formulas

Each A exterior `k`-cycle is a contiguous ambient block.  Its source-cycle
edge increments are one except for the unique block seam, whose extra
increment is `2k`.

If the second edge lies in a marked parent
`r in {s,k-s}`, retain `t=r-d` source edges.  Averaging the cyclic first
start over the `k` positions, the retained union has ambient size `t`
with mass `(k-t)/k` and size `t+2k` with mass `t/k`.  Since
`ell<2k`, only the first case can qualify.  Thus the complete marked raw
prefix is exactly

```text
T_A^mark(k,ell)
 =sum_(s=1)^j q_s sum_(r in {s,k-s})
   sum_(t=2)^min(ell,r-1)
    (t-1)K_R(r,t)(k-t)/k.                           (5.1)
```

This includes both marked parent orientations in both exterior blocks; the
factor two from the blocks cancels the literal first-edge normalization
`1/(2k)`.

If the second edge lies in the untouched exterior block, the first one-run
face has size `s` with mass `(k-s)/k` or size `k-s` with mass `s/k`.
The second one-run face of size `y` has raw mass

```text
(k-y)K_R(k,y).                                      (5.2)
```

The choice `x=s` cannot qualify: even at `y=k-1`, its complementary
two-run face has size

```text
3k-s-(k-1)>=2k+1-j=(3k+3)/2>ell.
```

For the choice `x=k-s`, write the qualifying second face as `y=k-c`.
The two-run size is exactly `k+s+c`, and (5.2) becomes
`cK_R(k,c)`.  Therefore

```text
T_A^unt(k,ell)
 =sum_(s=1)^j q_s(s/k)
   sum_(1<=c<=ell-k-s)cK_R(k,c),                    (5.3)
```

with an empty inner sum if the upper endpoint is below one.  Formulas
(5.1)--(5.3) retain marked/untouched kinds and all equal-size collisions.

## 6. Uniform A bound

For the short marked parent `r=s`, the same cancellation and convolution
as in (4.1), now without the factor two from (3.6), gives

```text
A_mark,short <=12 sqrt(ell)/k.                      (6.1)
```

For `r=k-s`, cancel `b_(k-s)` and sum first over `s`.  With
`u=k-t>=2`, (2.4) gives

```text
A_mark,long
 <=(3/R)sum_(2<=t<=min(ell,k-2))
      t b_t (u/k)b_u/b_k,       u=k-t.              (6.2)
```

For `t<=k/2`, (2.2)--(2.3) bound (6.2) by
`12sqrt(ell)/k`.  For `t>k/2`, use `b_t/b_k<4`,
`t/R<=1`, and sum in `u=k-t` to obtain

```text
A_mark,long,high <=12/sqrt(k)
 <=17 sqrt(ell)/k,                                  (6.3)
```

where the last inequality uses that this range requires `ell>k/2`.
Together,

```text
T_A^mark(k,ell)<=41sqrt(ell)/k.                     (6.4)
```

In (5.3), nonemptiness forces `c<=ell-k-s<=j`.  Hence
`K_R(k,c)<=4b_c/R` by (2.2), and (2.3),(2.5) give

```text
T_A^unt(k,ell)
 <=(4/R)[sum_s q_s(s/k)][sum_(c<=j)c b_c]
 <=20/k
 <=20sqrt(ell)/k.                                   (6.5)
```

Thus

```text
T_A(k,ell)<=61sqrt(ell)/k.                          (6.6)
```

## 7. TCM and the failed local shortcut

Both raw masses are nonnegative.  Equations (4.7) and (6.6) imply

```text
|T_B-T_A|<=T_B+T_A<=145sqrt(ell)/k
                         <=160sqrt(ell)/k,
```

which proves (1.2), hence `(TCM)` through (1.1).

This does not resurrect M226's refuted assertion that a fixed first
edge/parent/unordered-child class has at most `4min(ell,a)` qualifying
placements.  That pointwise count is exactly false (five placements at
`k=5`, and eight at `k=7`).  The proof above instead:

1. averages the exact B placement over every cyclic first start;
2. keeps the large-seam exclusion factor `(D-t)/D`;
3. weights each child by the exact Borel kernel; and
4. averages the first split with the exact signed-reduction weight `q_s`.

The Borel convolution and truncated first moment control this weighted
average even though an individual fixed-placement count exceeds four.

## 8. Dependency and scope ledger

- **Proved inputs:** M199/M207 literal ordered-double formulas; M217/M222 raw
  q-averaging and block partition; M226/M229 identity (1.1); elementary
  Stirling bounds; rooted-tree convolution (2.4).
- **New proved step:** exact formulas (3.3)--(3.6), (5.1), (5.3), and the
  universal separate positive bounds (4.7), (6.6), hence `(TCM)`.
- **Finite falsification:** the standard-library checker compares the literal
  ordered tuples with the independent formulas coefficient-by-coefficient
  at `k=3,5,7`; this is not used to prove universality.
- **Still open:** `(YCM)`; therefore `(WBE)`, `(DE)`, conditional `J2`,
  `PCR/WPCR`, all downstream responses, every spectral-gap or mixing claim,
  and both Terminals.
