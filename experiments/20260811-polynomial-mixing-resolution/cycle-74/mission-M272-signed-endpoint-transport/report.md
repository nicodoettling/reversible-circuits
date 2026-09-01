# M272 report: signed endpoint transport

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, and scope

```text
VERDICT: EXACT FULL D/q ENDPOINT-COUPLING IDENTITY AND STRICT COLLISION
COEFFICIENT REDUCTION.
CHANNEL-ONE COLLISION DERIVATIVE: O(1/k) PROVED.
CHANNEL-TWO TRIANGLES: O(1/k) PROVED.
CIBV, DOR, SET, PBV, AND FD: UNRESOLVED.
```

For odd `k>=3`, `n=3k`, this mission concerns only the balanced first
fixed cell of the auxiliary uniform minimal-long-cycle factorization law and
M73's nonlazy cyclic rank-two kernel.  Permutations compose as
`(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.

The target remains

```text
sum_(ell=2)^((n-3)/2)|sum_K<w,T_(K,ell)>|=O(n^-2).  (SET)
```

This is not the global fixed-length identity-word sampler or the lazy
`{3,4,5}` heat-bath chain.  No FCL1, direct-L1, gap, mixing, or Terminal
conclusion is inferred.

## 2. Source lock

Every payload named by the required frozen checksum ledgers passed before
use.  The ledger digests are

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
```

M267 was frozen but under M270 audit.  Every M267 identity used here was
independently rederived from the literal owner-charge definition.  No
predecessor file was edited.

## 3. Full merged-law coupling

For each channel, the mission first constructs literal couplings of
`Phi_(j,u),Phi_(j,u+1)`.  Channel one shares the middle chord; channel two
maximally couples the exact completion-count conditional second-factor
laws.  The phase, ordered factors, triangle/double kind, owner-pair
`kappa`, and profile normalization remain explicit.

Let `S~q`, `T~p` be the monotone quantile coupling.  Since
`D_u=sum_(s<=u)(p_s-q_s)<0`,

```text
Pr(S<=u<T)=-D_u.
```

Couple the actual two-cycle and long-cycle embedding at split `S`, then
compose the adjacent kernels through level `T`.  The endpoint laws are
literally

```text
Y_S~H_(j,A),                    X_T~H_(j,B).
```

### Main exact identity (proved)

For every test function `g`,

```text
E[g(X_T)-g(Y_S)]
 =sum_s q_s[Phi_(j,s)-Psi_(j,s)](g)
  +sum_u D_u[Phi_(j,u)-Phi_(j,u+1)](g),

eta(g)=sum_(j=1)^2 alpha_j E_j[g(X_T)-g(Y_S)].       (3.1)
```

For the owner endpoint response, the independently rederived phase law is

```text
sum_K<w,T_(K,ell)>
 =1/n sum_(j=1)^2 alpha_j
       E_j[E_ell(X_T)-E_ell(Y_S)].                  (3.2)
```

Equations (3.1)--(3.2) perform the complete signed `D_u/q_u`
cancellation before any cost.  The outside `1/n` is visible.  Applying
the accepted statewise lag-l1 envelope now gives only `O(1/n)` for the
left side, one factor `n` short of SET; no full-state TV estimate is
asserted.

## 4. Exact phase incidence and channel-one collision

The combined-channel raw coefficient is partitioned by the literal
first-edge indicators

```text
b_B(e)=1[e crosses the two runs of L],
b_A(e)=1[0 is an endpoint of e].
```

This is an exact identity before absolute values.  The shortcut that the
complementary phases cancel identically is false at `k=3`; exact values
through `k=7` show that both parts remain material.  This only refutes the
seam-only equality, not a seam-weighted asymptotic proof.

For channel one, direct chord classification gives the exact exterior-face
laws

```text
rho_A(a)=(k-a)nu_k(a),
rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1).
```

With `delta rho=rho_B-rho_A`, exterior endpoint-intensity difference
`delta a`, and common middle intensity `m`,

```text
eta_1(I_ell)=delta rho(ell)+delta rho(n-ell)
             +(delta a*m)(ell)+(m*delta a)(ell).    (4.1)
```

Critical-Borel ratio products prove
`sum_a|Delta delta rho(a)|=O(1/k)`; the cross convolutions are
`O(1/k^2)`.  Hence

```text
sum_(ell=2)^(n-3)|eta_1(Delta I_ell)|=O(1/k).        (4.2)
```

The checker independently constructs both sides of (4.1) over
`Fraction` and verifies equality at `k=3,5,7`.

## 5. Exact channel-two collision reduction

Under the literal ordered pair laws `Lambda_L,Lambda_F`, shared endpoints
give triangles.  Re-deriving the marked critical-Cayley convolution yields

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3),

sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].
```

Every triangle collision derivative has l1 at most `12`, so the entire
signed triangle contribution is `O(1/k)`.

For disjoint ordered pairs put

```text
p_hat_s=p_s(1-gamma_L(s)),
q_hat_s=q_s(1-gamma_F(s)),
E_u=sum_(s<=u)(p_hat_s-q_hat_s).
```

The nonzero endpoint and exact vector Abel identity are

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)],

R_D=E_(k-1)Phi_(k-1)^D
 +sum_(u=1)^(k-2)E_u[Phi_u^D-Phi_(u+1)^D]
 +sum_(s<k/2)q_hat_s[Phi_s^D-Psi_s^D].              (5.1)
```

Also `|E_u|<=C sqrt(u)/k`.  The first two terms of (5.1), kept as one
signed vector, are `(CSBV)`; the final literal embedding vector is
`(CEBV)`.  Proving each has lag-l1 `O(1/k)` would close channel two.
Neither is proved.  Together with the proved complete channel-one theorem
and triangle part, they are the strict remaining subcoefficients of the
mission-level channel-combined collision lemma

```text
(CIBV)
sum_ell|alpha_1 eta_1(Delta I_ell)
             +alpha_2 eta_2(Delta I_ell)|=O(1/k).   (5.2)
```

Termwise insertion of the statewise bound creates

```text
sum_u sqrt(u)||Phi_u^D-Phi_(u+1)^D||_1,
```

which is the wrong norm.  Its exact values `0,6.0563,25.4890` at
`k=3,5,7` grow sharply, while `k` times the signed CSBV-vector norm is
`0.9600,0.8543,0.9642`.  This refutes the statewise adjacent-triangle
inference as a target-scale route; it neither disproves CSBV nor establishes
asymptotic divergence.

## 6. First open decorated coefficient

M261's exact pointwise affine split is

```text
e^2 eta(E_ell)=eta(Delta I_ell)+eta(Delta Q_ell).
```

Even after collision closure, the separate first open owner-ratio lemma is

```text
(DOR)  sum_(ell=2)^(n-3)|eta(Delta Q_ell)|=O(1/k),
```

or a joint collision/decorated estimate before absolute value.  A splice
incidence of order `s/k` plausibly pairs with a literal owner defect
`O(1/s+1/(k-s))`, but this multiplication has not been proved for the
complete channel/kind/phase law.  CIBV (strictly reduced to CSBV/CEBV),
DOR, SET, PBV, and FD remain open.

## 7. Exact finite diagnostics

Both retained checkers are deterministic, standard-library only, Python
`3.12.3`, with `seed=null`.

| `k` | `n sum|eta(E)|` | `k||eta_2(Delta I)||_1` | `k||CSBV||_1` | `k||CEBV||_1` |
|---:|---:|---:|---:|---:|
| 3 | 2.01300 | 5.33689 | 0.96000 | 3.28889 |
| 5 | 2.41867 | 5.01606 | 0.85430 | 5.10173 |
| 7 | 1.97841 | 4.62738 | 0.96422 | 4.59372 |

All asserted reflection, channel-one coefficient, shared-endpoint mass,
nonzero endpoint, and vector Abel identities pass exactly.  The table is
falsification/calibration only; it proves no sign or uniform asymptotic
bound.

Retained commands are printed verbatim in the two JSON artifacts.  No
network, nonstandard package, quotient shell, SR/TPR inference, or finite
sign extrapolation was used.

## 8. Final action

**FREEZE THE EXACT FULL-PATH COUPLING, CHANNEL-ONE COLLISION BOUND,
CHANNEL-TWO TRIANGLE/DISJOINT COEFFICIENT REDUCTION, AND THE ADJACENT-NORM
OBSTRUCTION; REQUEST A FRESH IMMUTABLE AUDIT.**

The two mission-level unresolved lemmas are `(CIBV)` and `(DOR)`;
CIBV's strict remaining subcoefficients are `(CSBV)` and `(CEBV)`.
SET/PBV/FD and every downstream statement remain unresolved.
