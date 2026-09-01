# M189 clean-room proof audit of frozen M186

Date: 2026-08-13 UTC.

Status: **ACCEPT** M186's strict exact coefficient and signed-prefix
reduction. There are no material objections and two nonmaterial exposition
qualifications. This does not prove `(PCR)`, `(WPCR)`, `(SCBR)`, `(BIR)`,
`(BR)`, PCS-bound, or any downstream claim.

## 1. Immutable input and exact setting

Before reading M186 as evidence, its complete eight-entry `SHA256SUMS`
passed. Independent top-level hashes are

```text
report.md                       dd8d46b3d05f20dd3e3616bd3709f877b3e997bfbb465171179a7188ac7737f7
component_boundary_reduction.md 59116384a8dd2b9dc280b5774022eae62e0e23bb98473d76270525d445edd02a
freeze_manifest.md              9bd47230cc9c6ab6af7030559f886bae045dea8901e24ff9ba5af2f40d67d248
SHA256SUMS                      9d5aa5ff628f8bf15051c09fd1537ffa240fba72ad2a9945356c8adfe8ebd7bd
```

M186 was not edited. Use `(pq)(x)=p(q(x))`, displayed factors
left-to-right, `n=3k` for odd `k>=3`, and

```text
h=(0,1,...,n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform law on minimal length-`n-1` transposition
factorizations of `h`; the operator is the fixed-cell nonlazy cyclic
rank-two coordinate kernel. It is not the global identity bridge or the
lazy `{3,4,5}` heat-bath chain.

## 2. Completion-count and Borel normalization

For a minimal residual `R` with cycle sizes `d_1,...,d_l` and transposition
rank `r=sum_i(d_i-1)`, the exact completion count is

```text
F_r(R)=r! product_i tau(d_i),       tau(d)=d^(d-1)/d!.
```

If `e` is an admissible first factor, and `f` is admissible after it, every
minimal factorization has a unique first factor and ordered first pair.
Consequently

```text
lambda_R(e)=F_(r-1)(eR)/F_r(R),
Lambda_R(e,f)=F_(r-2)(feR)/F_r(R)
```

normalize exactly to one. The order `feR` is correct because the remaining
residual after the displayed prefix `ef` is `(ef)^-1R=feR`.

Put `D=2k-1` and `b_d=e^-d tau(d)`. For one `D`-cycle, factorial
cancellation gives

```text
lambda_L(e)=b_a b_(D-a)/[(D-1)b_D].                 (2.1)
```

For two `k`-cycles, the untouched cycle cancels from the first-factor ratio:

```text
lambda_F(e)=b_a b_(k-a)/[2(k-1)b_k].                (2.2)
```

The common middle cycle similarly gives

```text
lambda_M(e)=b_a b_(k-a)/[(k-1)b_k].                 (2.3)
```

After an ordered pair, let `x_i` be all positive residual sizes descended
from the active source component or components, including size-one pieces.
Their total is unchanged, so every exponential in the `b` notation cancels.
The ordered-pair laws are therefore

```text
Lambda_L(e,f)=product_i b_(x_i)/[(D-1)(D-2)b_D],
Lambda_F(e,f)=product_i b_(x_i)/[(2k-2)(2k-3)b_k^2]. (2.4)
```

There is no missing factor two: the two equal A-exterior components are
already sampled by the normalized first-factor law of their product
residual. There is no missing triangle/double lift factor because `(e,f)`
is a literal ordered pair before projection to its product.

## 3. Combined coefficient signs and component Abel identity

The accepted residual decomposition is

```text
A^-1h=C_- M C_+,             B^-1h={0} L M.
```

Conditioning on the number `J` of exterior colors among the first two
factors gives equal channel masses `alpha_j` at A and B. The `J=0` law is
the same ordered first-pair law of `M` and cancels. Since
`eta=P_B-P_A`, the two remaining contrasts are exactly

```text
alpha_1[(L first edge)*(M first edge)
        -(F first edge)*(M first edge)]

+alpha_2[(L ordered pair)-(F ordered pair)].         (3.1)
```

In `J=1`, exterior and middle factors have disjoint supports and commute;
the two possible color orders are already in `alpha_1`. In `J=2`, the
ordered `Lambda` law is retained. Testing (3.1) against the literal component
multiplicity `N_r(d;(ef)^-1h)` proves M186's `(CB)` with signs `+L-F` in
both braces. This keeps same- and cross-run doubles, shared-endpoint
triangles, unit gaps, and repeated component sizes before any estimate.

Let `p_s,q_s` be the B/A first-exterior smaller-split laws and let
`phi_(j,s),psi_(j,s)` be the corresponding normalized component profiles.
Then

```text
H_(j,B)-H_(j,A)=sum_s p_s phi_(j,s)-sum_s q_s psi_(j,s)
 =sum_s(p_s-q_s)phi_(j,s)+sum_s q_s(phi_(j,s)-psi_(j,s)). (3.2)
```

With `D_s=sum_(t<=s)(p_t-q_t)`, normalization gives
`D_0=D_(k-1)=0`. Since `p_s-q_s=D_s-D_(s-1)`, finite summation by parts is

```text
sum_s(p_s-q_s)phi_s
 =sum_(u=1)^(k-2)D_u(phi_u-phi_(u+1)).               (3.3)
```

Equations (3.2)--(3.3) give `(BA-C)` coefficientwise with the displayed
plus signs and no endpoint remainder.

## 4. Exact `J=1` face laws

For a chord of a directed `d`-cycle whose source arcs have sizes `a,d-a`,
put

```text
nu_d(a)=(d-2)! tau(a)tau(d-a)/d^(d-2).
```

In a contiguous `k`-block, exactly `k-a` chords have ambient separation
`a`, so

```text
rho_A(a)=(k-a)nu_k(a),              1<=a<k.          (4.1)
```

The B exterior cycle consists of runs of lengths `k-1` and `k`. Same-run
chords with ambient face `a` number

```text
S_k(a)=(k-1-a)_+ +(k-a)_+.                           (4.2)
```

For a cross-run chord `(i,2k+t)`, where `1<=i<=k-1` and `0<=t<=k-1`, the
ambient face avoiding the middle run is `a=k+i-t`; its split inside `L` is
`a-1` or its complement. Solving for `t` gives

```text
C_k(a)=a-1,                  2<=a<=k,
       =2k-a,                k<a<=2k-1,
       =0                    otherwise.              (4.3)
```

As a count checksum,

```text
sum_a S_k(a)=(k-1)^2,
sum_a C_k(a)=k(k-1),
sum_a[S_k(a)+C_k(a)]=(2k-1)(2k-2)/2.
```

Thus every exterior chord is counted once and

```text
rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1).   (4.4)
```

Both laws normalize. For `a=2k-c`, `1<=c<=k-1`, the same-run count is
zero and the cross count is `c`. Symmetry of `nu_D` gives the exact tail

```text
rho_B(2k-c)=c nu_(2k-1)(c).                          (4.5)
```

The middle chord is independent with face `b~rho_A`. Whether the exterior
chord is same-run (separated double) or cross-run (nested double), the
ambient residual component data are

```text
(one run,a), (one run,b), (two runs,n-a-b).
```

Therefore, before multiplying by `alpha_1`,

```text
M_1^(1)(d)=rho_B(d)-rho_A(d),
M_2^(1)(d)=sum_(a+b=n-d)[rho_B(a)-rho_A(a)]rho_A(b). (4.6)
```

## 5. Uniform weighted `J=1` estimates

Robbins' uniform Stirling bounds imply

```text
b_m=(2 pi)^(-1/2)m^(-3/2)exp(O(1/m)).
```

Hence, uniformly for `1<=a<=m/2`,

```text
m nu_m(a)=b_a[1+O(a/m)],
nu_m(a)<=C b_a/m.                                   (5.1)
```

For `2<=a<=k/2`, substitution in (4.1)--(4.4) gives

```text
|rho_B(a)-rho_A(a)|
 <=C a[b_a+b_(a-1)]/k.                              (5.2)
```

At `a=1`, the same ratio estimate directly gives `C b_1/k`; no `b_0` is
needed. Since `sum_a b_a=1` (summability alone suffices) and
`b_(a-1)<=C b_a`, the low-face part of
`sum |rho_B-rho_A|/a` is `O(1/k)`. For `a>k/2`, use `1/a<=2/k` and
`||rho_B-rho_A||_1<=2`. Thus

```text
sum_a |rho_B(a)-rho_A(a)|/a=O(1/k).                 (5.3)
```

For the two-run term, `a<=k` gives denominator
`n-a-b>=k+1`, hence `O(1/k)` by total variation. For `a>k`, put
`a=2k-c` and `b=k-r`. Then

```text
rho_B(a)=c nu_(2k-1)(c),        rho_A(b)=r nu_k(r),
sum_r r nu_k(r)=1.
```

Consequently

```text
sum_b rho_A(b)/(n-a-b)
 =sum_r r nu_k(r)/(c+r)<=1/c.                       (5.4)
```

Multiplying (5.4) by the tail law leaves

```text
sum_(c=1)^(k-1)nu_(2k-1)(c)=1/(2k-1),               (5.5)
```

because `(2k-1)nu_(2k-1)(c)` is the normalized smaller-split law of an odd
cycle. This is a slightly sharper justification than M186's `O(1/k)` use
of (5.1). Therefore

```text
sum_(a,b)|rho_B(a)-rho_A(a)|rho_A(b)/(n-a-b)=O(1/k). (5.6)
```

The exact ratios give `|u_1(d)|+|u_2(d)|<=C/d`. Applying (5.3) and (5.6)
to (4.6) proves the conditional `J=1` charge is `O(1/k)=O(1/n)`. This
subchannel result is not used to split the final two-channel absolute value.

## 6. Singleton coefficient

Let `W(s)` be the ordered-lift average number of cyclic-boundary factors.
For an accessible double, a one-run singleton is exactly a boundary factor,
so `N_1(1;s)=W(s)`. For an accessible oriented triangle, each support edge
appears in two of its three ordered lifts, hence

```text
N_1(1;s)=3W(s)/2.
```

Pointwise over both kinds,

```text
N_1(1)=W+(1/2)W 1_T,
M_1(1)=eta(W)+(1/2)eta(W 1_T).                       (6.1)
```

M180's accepted exact one-step boundary identity, applied only to the two
source residuals, gives

```text
eta(W)=2[U_2(2k-1)-2U_1(k)]/(n-3).                  (6.2)
```

Indeed A has three one-run `k`-components, while B has a two-run
`(2k-1)`-component, one one-run `k`-component, and a singleton with
`U_1(1)=0`. The exact ratio expansion makes the bracket in (6.2) uniformly
bounded, so `eta(W)=O(1/n)`.

The exact conditional triangle probabilities are

```text
Pr(T|J=0)=3/k,              Pr(T|J=1)=0,
Pr_B(T|J=2)=3/(2k-1),
Pr_A(T|J=2)=3(k-2)/[k(2k-3)]<=3/k.                  (6.3)
```

These follow from the standard Cayley-tree/first-pair count for a cycle,
which gives probability `3/d` that its first two factors share an endpoint;
on the A side of `J=2`, both factors choose the same exterior component with
probability `(k-2)/(2k-3)`. Since `0<=W<=2`, (6.3) gives
`eta(W1_T)=O(1/k)`. Equations (6.1)--(6.3) prove

```text
M_1(1)=O(1/n).                                       (6.4)
```

## 7. Signed summation by parts and prefix implication

Let `m=(n-1)/2`,

```text
P_d=M_1(d),                 N_d=M_1(d)+M_2(d),
A_D=sum_(2<=d<=D)N_d,       C_D=sum_(2<=d<=D)P_d,
r_d=u_1(d)-u_2(d)=e tau(d-1)/tau(d)-1.
```

Because two-run components have size at least two, the small charge is

```text
S_k=M_1(1)u_1(1)+sum_(d=2)^m[N_du_2(d)+P_dr_d].     (7.1)
```

Twice applying finite Abel summation gives exactly

```text
S_k=M_1(1)u_1(1)+A_m u_2(m)+C_m r_m
 +sum_(d=2)^(m-1){A_d[u_2(d)-u_2(d+1)]
                  +C_d[r_d-r_(d+1)]}.               (7.2)
```

There is no omitted endpoint. Uniform Taylor bounds for
`tau(d-1)/tau(d)=(1-1/d)^(d-2)` give

```text
|u_2(d)|+|r_d|<=C/d,
|u_2(d)-u_2(d+1)|+|r_d-r_(d+1)|<=C/d^2.             (7.3)
```

If `(PCR)` holds, `|A_D|+|C_D|<=C sqrt(D)/n`, then the endpoint terms in
(7.2) are `O(1/(n sqrt(m)))` and the interior is bounded by

```text
C/n sum_(d>=2)sqrt(d)/d^2=O(1/n).
```

Together with (6.4) and constant `u_1(1)`, this proves `(SCBR)`. Likewise,
substitution of (7.3) shows the displayed `(WPCR)` condition is precisely
sufficient. M186 proves neither prefix condition, and this audit does not
attempt them.

## 8. Clean-room exact reconstruction

`cleanroom_component_audit.py` is standard-library only, imports no M186
code or data, and rejects every rank except exact `k=3,5`. It independently
constructs:

- both literal completion-count source rows and their `J=0,1,2` channels;
- isolated first-factor and ordered-pair component laws and their closed
  factorial-cancellation values;
- component profiles, the signed `(CB)` combination, and `(BA-C)`;
- `rho_A,rho_B`, their exact tail and both weighted face sums;
- all ordered lifts, boundary incidence, pointwise singleton identities,
  and the source `eta(W)` formula; and
- the small charge and `(SBP)` as equal formal polynomials in `E`.

All assertions pass on 64 and 810 source-accessible states. The exact channel
masses are

```text
k=3: (1/15,8/15,2/5),
k=5: (1/11,16/33,14/33).
```

The `k`-scaled sums in (5.3)+(5.6) are `1.93871746` and `1.46710702`.
These values calibrate only the exact identities; they provide no sign,
monotonicity, uniform-constant, or asymptotic evidence.

## 9. Numbered objections and decision

### Material objections

None.

### Nonmaterial exposition qualifications

1. M186 equation (4.10) displays `b_(a-1)` while its stated range includes
   `a=1`; `b_0` was not defined. Handle `a=1` separately as above (or define
   the invalid term to be zero). The estimate is unchanged.
2. The low-face summation after (4.10) should explicitly cite
   `sum_a b_a<infinity` (indeed the critical-Borel identity gives one). This
   is standard and the missing citation does not create a proof gap.

```text
VERDICT: ACCEPT M186'S STRICT REDUCTION.
MATERIAL OBJECTIONS: 0. NONMATERIAL QUALIFICATIONS: 2.
PCR, WPCR, SCBR, BIR, BR, PCS-BOUND, AND ALL DOWNSTREAM CLAIMS: UNRESOLVED.
```
