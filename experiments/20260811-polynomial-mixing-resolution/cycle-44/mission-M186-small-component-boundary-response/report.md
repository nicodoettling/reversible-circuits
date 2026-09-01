# M186 report: small-component boundary response

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: STRICT EXACT COEFFICIENT/PREFIX REDUCTION.
SCBR, BIR, BR, AND PCS-BOUND: UNRESOLVED.
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` with odd
`k>=3`, and

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform minimal-factorization law of the long cycle and
the operator is M73's nonlazy cyclic rank-two coordinate kernel. This is not
the global identity-word target or its local heat-bath chain. No FD/FCL1,
direct-L1, H0/gap, mixing, or Terminal statement is proved or inferred.

## 2. Frozen dependencies and accepted starting point

Before use, every frozen manifest passed for M91, M94/M100, M102/M105,
M155/M159, M161/M166, M168/M171, M174/M178, and M180/M182. No predecessor
was edited.

M180/M182's accepted exact input is

```text
eta(Q)=sum_d[M_1(d)u_1(d)+M_2(d)u_2(d)],
```

where `M_r(d)=sum_s eta(s)N_r(d;s)` already combines both source channels,
both intermediate kinds, and every collision. The part `d>n/2` is
`O(1/n)`; `(SCBR)` is the corresponding sum over `d<=n/2`.

## 3. Closed critical-Borel coefficient formula

Let `F=C_-C_+` be A's exterior two-cycle permutation, `L` B's exterior
`(2k-1)`-cycle, and `M` the common middle cycle. For a minimal residual `R`,
define

```text
lambda_R(e)=F_(r(R)-1)(eR)/F_(r(R))(R),
Lambda_R(e,f)=F_(r(R)-2)(feR)/F_(r(R))(R).
```

These are normalized first-edge and ordered-pair laws. With
`b_j=e^-j tau(j)`, they have the closed forms

```text
lambda_L(e)=b_a b_(D-a)/[(D-1)b_D],              D=2k-1,
lambda_F(e)=b_a b_(k-a)/[2(k-1)b_k],
lambda_M(e)=b_a b_(k-a)/[(k-1)b_k],

Lambda_L(e,f)=product_i b_(x_i)/[(D-1)(D-2)b_D],
Lambda_F(e,f)=product_i b_(x_i)/[(2k-2)(2k-3)b_k^2],
```

where `x_i` are the positive source-residual sizes after the ordered pair.
If `chi_(r,d)(e,f)=N_r(d;ef)`, this mission proves exactly

```text
M_r(d)=alpha_1{
 sum_(e in L,f in M)lambda_L(e)lambda_M(f)chi
-sum_(e in F,f in M)lambda_F(e)lambda_M(f)chi}

+alpha_2{
 sum_(e,f)Lambda_L(e,f)chi
-sum_(e,f)Lambda_F(e,f)chi}.                         (CB)
```

All signs remain outside the complete chord sums. `(CB)` retains triangles,
both double colors, shared endpoints, unit gaps, and lower-support
collisions.

## 4. Exact component-valued Abel formula

Group the first exterior chord by its smaller source split. Let `p_s,q_s`
be M91's exact conditioned-Borel split laws, `D_u=sum_(s<=u)(p_s-q_s)`, and
let `phi_(j,s;r,d),psi_(j,s;r,d)` be the normalized B/A component-count
profiles obtained by restricting `(CB)` to that split. Discrete summation by
parts gives, coefficientwise,

```text
M_r(d)=sum_(j=1)^2 alpha_j{
 sum_(u=1)^(k-2)D_u[
   phi_(j,u;r,d)-phi_(j,u+1;r,d)]
+sum_(s<k/2)q_s[
   phi_(j,s;r,d)-psi_(j,s;r,d)]}.                    (BA-C)
```

This is a closed exact critical-Borel/Abel formula for the requested
one-dimensional coefficients. The two channels are combined in `M_r(d)`
before every later prefix or charge estimate.

## 5. Proved `J=1` face law and asymptotic scale

For a contiguous `k`-block face,

```text
nu_d(a)=(d-2)!tau(a)tau(d-a)/d^(d-2),
rho_A(a)=(k-a)nu_k(a).
```

For B's two-run exterior cycle, let

```text
S_k(a)=(k-1-a)_+ +(k-a)_+,
C_k(a)=a-1  (2<=a<=k),   C_k(a)=2k-a (k<a<=2k-1).
```

Same-run versus cross-run chord counting gives exactly

```text
rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1).
```

Every `J=1` product, separated or nested, has component data
`(1,a),(1,b),(2,n-a-b)`. Consequently its conditional signed coefficients
are

```text
M_1^(1)(d)=rho_B(d)-rho_A(d),
M_2^(1)(d)=sum_(a+b=n-d)[rho_B(a)-rho_A(a)]rho_A(b).
```

Uniform critical-Borel ratio bounds prove

```text
sum_a |rho_B-rho_A|(a)/a=O(1/k),
sum_(a,b)|rho_B-rho_A|(a)rho_A(b)/(n-a-b)=O(1/k).
```

Thus the conditional `J=1` charge has the desired scale. This is a proved
subchannel fact only; it is not used to split the final two-channel absolute
value.

## 6. Signed prefix reduction and first boundary term

Put `m=(n-1)/2`,

```text
P_d=M_1(d),                    N_d=M_1(d)+M_2(d),
A_D=sum_(d=2)^D N_d,           C_D=sum_(d=2)^D P_d,
r_d=u_1(d)-u_2(d)=e tau(d-1)/tau(d)-1.
```

The full channel-combined `(SCBR)` sum is exactly

```text
S_k=M_1(1)u_1(1)+A_m u_2(m)+C_m r_m
 +sum_(d=2)^(m-1){
   A_d[u_2(d)-u_2(d+1)]+C_d[r_d-r_(d+1)]}.           (SBP)
```

This mission also proves the first boundary coefficient

```text
M_1(1)=O(1/n).
```

The proof uses the pointwise identity
`N_1(1)=W+(1/2)W1_T`, M180's exact
`eta(W)=2[U_2(2k-1)-2U_1(k)]/(n-3)`, and the `O(1/k)` triangle probability.

Since `u_2,r=O(1/d)` and their first differences are `O(1/d^2)`, `(SCBR)`
would follow from the fully combined prefix lemma

> **PREFIX COMPONENT RESPONSE `(PCR)` (unresolved).** Uniformly for
> `2<=D<=m`,
>
> ```text
> |A_D|+|C_D|=O(sqrt(D)/n).
> ```

The weaker weighted condition

```text
n[(|A_m|+|C_m|)/m
  +sum_(d=2)^(m-1)(|A_d|+|C_d|)/d^2]=O(1)
```

also suffices. These use the already combined `(CB)` coefficients and do not
discard collisions or split channels.

## 7. Exact falsification and calibration

`component_abel_check.py` is deterministic, standard-library only, and
capped at exact `k=3,5`. It constructs literal source rows, separately
constructs the Borel chord profiles, and checks `(CB)`, `(BA-C)`, the `J=1`
face collapse, and `(SBP)` coefficientwise over `Fraction`. All assertions
passed, and the complete coefficients match frozen M180 exactly.

| `k` | `max_(2<=D<=n/2) n max(|A_D|,|C_D|)/sqrt(D)` | `k` times the two `J=1` weighted sums |
|---:|---:|---:|
| 3 | 2.78720 | 1.93872 |
| 5 | 1.64136 | 1.46711 |

These values only calibrate the formulas and fail to falsify `(PCR)` at two
ranks. No boundedness, sign, decrease, or asymptotic limit is inferred.

## 8. First unproved step and strongest self-attack

`(PCR)` is not a consequence of M180's three global moments. A signed
component measure may satisfy zero total mass and first moment while having
order-one prefixes. Nor does the proved channel-1 estimate control the
channel-2 collision terms: taking a triangle inequality between channels is
explicitly disallowed and could lose the needed cancellation.

The exact `Lambda_L-Lambda_F` term in `(CB)` is therefore the remaining hard
object. Its prefixes combine the one-cycle/two-cycle source difference with
shared-endpoint triangles, cross-run doubles, and every small Borel layer.
The next proof must establish `(PCR)` or the weaker weighted prefix bound on
that **fully combined** coefficient, not on isolated generic topologies.

## 9. Artifacts, command, hygiene, and final action

Owned artifacts are `plan.md`, `checkpoint.md`,
`component_boundary_reduction.md`, `component_abel_check.py`,
`component_abel_results.json`, `results.json`, this report, and the freeze
files.

Retained deterministic command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-44/mission-M186-small-component-boundary-response/component_abel_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-44/mission-M186-small-component-boundary-response/component_abel_results.json
```

Python `3.12.3`; standard library only; `seed=null`. No network, package
installation, broad shell/quotient computation, `k=7`, or finite-sign
inference was used. Final action: **freeze the exact coefficient, `J=1`,
singleton-boundary, and signed-prefix reductions; keep `(PCR)` and every
downstream bound open; request a fresh immutable audit.**
