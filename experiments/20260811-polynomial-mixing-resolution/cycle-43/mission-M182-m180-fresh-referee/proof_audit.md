# M182 clean-room proof audit of frozen M180

Date: 2026-08-13 UTC.

Status: **ACCEPT** the five assigned M180 propositions/reductions. There are
no material objections and two nonmaterial exposition qualifications. This
does not prove `(SCBR)`, `(BIR)`, `(BR)`, PCS-bound, a gap, mixing, or a
Terminal.

## 1. Immutable input and exact setting

Before reading M180's proof, its own `sha256sum -c SHA256SUMS` passed for all
eight listed artifacts. Independent top-level recomputation gave

```text
report.md                    9054e112dbecc7151560f5f52aebf7d4556140805193a1757c152e6c13ef50ad
boundary_charge_reduction.md 99e55f6a5484cf3b4a6e1c6831d0f869f8a441d74de43d9c35abcea56933d5d0
freeze_manifest.md           3355c8c5a9bd1fb2518c20de31a711c2f8ea14d4bdb4d13d0a443f035f7f4a03
SHA256SUMS                    b362d629eaae627432efb3d6de97a825ed1bb17c0ca17ffb39c342db5c9d76d6
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` with odd
`k>=3`, `h=(0 1 ... n-1)`, and

```text
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform law on minimal length-`n-1` transposition
factorizations of `h`; the operator is M73's nonlazy cyclic rank-two
coordinate kernel. It is not the global identity bridge or its local
heat-bath chain.

## 2. Independent ratio calculation

Put `x=1/d` and `tau(d)=d^(d-1)/d!`. Direct factorial cancellation gives

```text
A_d=tau(d-1)/tau(d)=(1-x)^(d-2),
B_d=tau(d-2)/tau(d)=(1-x)(1-2x)^(d-3).
```

For the first ratio,

```text
log(e A_d)=1+(x^-1-2)log(1-x).
```

The coefficient of `x^r`, `r>=1`, is

```text
a_r=2/r-1/(r+1).
```

Thus `a_1=3/2`, `a_2=2/3`. The tail from `r=3` onward is `O(x^3)` uniformly
for `0<x<=1/2`, so exponentiation with a uniform remainder gives

```text
e A_d=1+3/(2d)+43/(24d^2)+O(d^-3).                  (2.1)
```

For the second ratio,

```text
log(e^2 B_d)=2+log(1-x)+(x^-1-3)log(1-2x).
```

Its `x^r` coefficient is

```text
b_r=-2^(r+1)/(r+1)+3*2^r/r-1/r.
```

Hence

```text
b_1=3,                         b_2=17/6,
```

and the exponential's quadratic coefficient is exactly

```text
b_2+b_1^2/2=17/6+9/2=22/3.                           (2.2)
```

Because `2x<=2/3` for `d>=3`, the remaining logarithmic series is uniformly
`O(x^3)` and exponentiation preserves that order. Therefore

```text
e^2 B_d=1+3/d+22/(3d^2)+O(d^-3).                    (2.3)
```

Multiplying (2.1) by `d-1` and `d-2` gives

```text
u_1(d)=  7/(24d)+O(d^-2),
u_2(d)=-29/(24d)+O(d^-2).                            (2.4)
```

For a two-run component, write

```text
I=1[a=1]+1[b=1],
(a-2)_+ +(b-2)_+=d-4+I.
```

The exact two-run numerator is consequently `d^2-7d+14-2I`. Multiplying
(2.3) by the one- and two-run numerators gives, uniformly in every positive
split `a+b=d`,

```text
v_1(d)=-5/3+O(d^-1),
v_2(a,b)=1/3-2I+O(d^-1).                             (2.5)
```

The finitely many zero-shift cases are bounded directly. Thus there is one
absolute `C` such that

```text
|u_r|<=C/d,
|v_1+5/3|<=C/d,
|v_2-1/3+2I|<=C/d.                                  (2.6)
```

This independently confirms the material coefficient `22/3` and every
sharp center used by M180.

## 3. Exact boundary-charge decomposition and uniform remainder

For component `i`, let

```text
(epsilon_i,c_i)=(1/2,2)  for one run,
(epsilon_i,c_i)=(-1/2,4) for two runs,
eU_i=d_i+epsilon_i+u_i,
e^2V_i=d_i^2-c_i d_i+v_i.
```

M174's exact response, after the already-audited pointwise affine
cancellation `L_T=0,L_D=-2`, expands to

```text
B=sum_i v_i+2sum_(i<j)epsilon_i epsilon_j
  +2sum_i(n-d_i)u_i
  +2sum_(i<j)(epsilon_i u_j+epsilon_j u_i+u_i u_j).  (3.1)
```

Put `Q=sum_i u_i`. For three one-run components, the constant in the first
line is

```text
3(-5/3)+2*3*(1/2)^2=-7/2.
```

For two one-run and one two-run component it is

```text
2(-5/3)+(1/3-2I_D)
 +2[(1/2)(1/2)+2(1/2)(-1/2)]=-7/2-2I_D.
```

After defining

```text
w_i=v_i+5/3                    (one run),
w_i=v_i-1/3+2I_D               (two runs),

R=sum_i w_i-2sum_i d_i u_i
  +2sum_(i<j)(epsilon_i u_j+epsilon_j u_i+u_i u_j), (3.2)
```

(3.1) becomes the exact identity

```text
B=2nQ-7/2-2I_D+R.                                    (3.3)
```

Equation (2.6) proves uniformity without hiding a macroscopic term:
`|d_i u_i|<=C`; each `w_i`, `epsilon_i u_j`, and `u_i u_j` is bounded;
there are exactly three components; and `0<=I_D<=2`. Therefore

```text
sup_(n,s)|R(s)|<infinity.                             (3.4)
```

For `eta=P_B-P_A`, `eta(1)=0` and its signed-measure `l^1` norm is at most
two. Applying `eta` to (3.3) shows that `eta(B)-2n eta(Q)` is uniformly
bounded. Both implications follow:

```text
eta(B)=O(1)  iff  n eta(Q)=O(1).                     (3.5)
```

No channel, kind, or collision contribution has been bounded separately.

## 4. Raw signed coefficients, moments, and the large tail

The exact raw row is

```text
P_g(s)=a(s)/R_n * beta_5(g,s)/beta_3(g),
R_n=(n-3)(n-4).
```

Consequently, for M180's complete signed contrast `delta_k`,

```text
eta(s)=P_B(s)-P_A(s)=a(s)delta_k(s)/R_n.             (4.1)
```

Thus its coefficient is literally the signed component pushforward:

```text
M_r(d)=sum_s eta(s)N_r(d;s).
```

Fubini gives

```text
eta(Q)=sum_d[M_1(d)u_1(d)+M_2(d)u_2(d)].             (4.2)
```

Let `t=eta(T)`. A triangle has component-count vector `(N_1,N_2)=(3,0)`;
a double has `(2,1)`; and `eta(D)=-eta(T)`. Therefore

```text
sum_d M_1(d)=3t+2(-t)=t,
sum_d M_2(d)=-t.                                    (4.3)
```

Every residual has total component size `n`, so

```text
sum_d d[M_1(d)+M_2(d)]=eta(n)=0.                    (4.4)
```

Moreover, every state has exactly three components and
`sum_s|eta(s)|<=2`; the triangle inequality only after the signed source
contrast has been formed gives

```text
sum_(r,d)|M_r(d)|<=3 sum_s|eta(s)|<=6.               (4.5)
```

For `d>n/2`, (2.6) and (4.5) imply

```text
sum_(d>n/2)|M_1(d)u_1(d)+M_2(d)u_2(d)|
 <=(2C/n)sum_(r,d)|M_r(d)|
 <=12C/n.                                            (4.6)
```

This verifies the claimed large-component `O(1/n)` tail. It says nothing
about the remaining small-component sum and does not attempt `(SCBR)`.

## 5. Exact boundary-incidence identity and BIR equivalence

Let `E_n` be the cyclic boundary transpositions. For a rank-two product
`t`, let `L(t)` be its `a(t)` ordered transposition lifts and set

```text
W(t)=a(t)^-1 sum_((a,b) in L(t))
                    [1[a in E_n]+1[b in E_n]].       (5.1)
```

Conjugation by `h` permutes `E_n` and the lifts, so `W` is cyclic invariant
and descends to the quotient. Conditional on product `t`, every lift has
the same remaining completion count; hence `KW` is exactly the expected
number of boundary factors in the next ordered pair.

Put `L=n-3`. A boundary transposition is an admissible next minimal factor
precisely when both endpoints are in one residual component. Within a
one-run size-`d` component there are `d-1` such edges; within a positive
two-run component there are `(a-1)+(b-1)=d-2`. Each cuts off a singleton,
so its completion-count ratio is

```text
1/L * tau(d-1)/tau(d).
```

The first factor therefore lies in `E_n` with probability `H/L`, where
`H=sum_i U_i`. The two positions have the same marginal: in the group
algebra, if `C` is the central sum of all transpositions and `D` is the sum
over `E_n`, the relevant coefficients are those of `DC^(L-1)` and
`CDC^(L-2)=DC^(L-1)`. Thus

```text
(bar K W)(O_s)=2H(s)/(n-3).                          (5.2)
```

The exact centered definition gives

```text
Q=eH-n-sum_i epsilon_i.
```

The epsilon sum is `3/2` on triangles and `1/2` on doubles. If
`t_k=eta(T)`, then

```text
eta(Q)=e eta(H)-t_k.                                 (5.3)
```

Since `eta=(delta_B-delta_A)bar K` on cyclic-invariant observables, (5.2)
also gives exactly

```text
eta(H)=(n-3)/2[(bar K^2W)(O_B)-(bar K^2W)(O_A)].     (5.4)
```

The accepted kind formula

```text
t_k=12(k-1)/[3k(3k-4)(2k-1)]=O(n^-2)
```

and (3.5) show that `(BR)` is equivalent to `eta(H)=O(n^-1)`. Equation
(5.4), with `n>=9`, is then equivalent in both directions to

```text
|(bar K^2W)(O_B)-(bar K^2W)(O_A)|=O(n^-2).           (5.5)
```

This verifies the exact `KW` identity and the stated BIR equivalence; BIR
itself remains unresolved.

## 6. Independent exact calibration

`cleanroom_boundary_audit.py` imports no M180 code or data. It builds the
two sources, all ordered transposition-pair products, completion counts,
residual ambient runs, decorations, signed component coefficients, and
boundary-lift averages from literal definitions. Arithmetic is `Fraction`
and response identities are formal polynomials in an indeterminate `E`.
Only `k=3,5` are permitted.

The run checked:

- both source rows normalize exactly;
- (4.1) holds at every source-accessible intermediate;
- (3.3) and the full affine response hold coefficientwise in `E`;
- (4.2)--(4.5) hold exactly;
- (5.2) holds from literal ordered-lift averaging on all 64 (`k=3`) and
  810 (`k=5`) source-accessible intermediates;
- (5.3)--(5.4) hold exactly.

Post-check floating displays agree with M180:

| `k` | `n eta(H)` | `n eta(Q)` | `n^2 Delta_W` | `eta(B)` |
|---:|---:|---:|---:|---:|
| 3 | 2.0725360 | 4.6737370 | 6.2176081 | 5.3716368 |
| 5 | 1.4820926 | 3.5438970 | 3.7052316 | 5.5840961 |

These values are exact-formula calibration only and imply no asymptotic
bound or sign.

## 7. Numbered objections and qualifications

1. **Material objections: none.** Every assigned proof-critical identity is
   correct.
2. **Nonmaterial notation qualification.** M180 writes `(bar K W)(s)` and
   `bar K^2W(B)-bar K^2W(A)` while `bar K` acts on cyclic orbits. Because
   `W` and `H` are cyclic invariant, the intended expressions at
   `O_s,O_A,O_B` are unambiguous and the proof is unchanged.
3. **Nonmaterial small-size qualification.** The displayed ratio formulas
   contain shifted `tau` indices at the smallest component sizes. M180 does
   invoke M174's zero convention and finite-case treatment later in the
   proof; stating that convention adjacent to the displays would make the
   proposition self-contained. No estimate or exact identity changes.

## 8. Referee conclusion

**ACCEPT M180 as a correct strict reduction.** Promote only the five audited
identities and the reduction to unresolved `(SCBR)`/`(BIR)`. Keep `(SCBR)`,
`(BIR)`, `(BR)`, PCS-bound, FD-bound, direct-L1, H0/gap, mixing, and both
Terminals explicitly unresolved.
