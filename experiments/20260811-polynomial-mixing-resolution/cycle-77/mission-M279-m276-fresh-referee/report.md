# M279 fresh immutable referee report on M276

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: ACCEPT M276'S APPEND-ONLY SALVAGE AS FROZEN.
MATERIAL OBJECTIONS TO M276: NONE.
NONMATERIAL OBJECTIONS TO M276: NONE.

M272 AS FROZEN: REMAINS REJECTED FOR ITS MATERIAL J1 BV GAP.
CORRECTED CHANNEL-ONE/J1 DERIVATIVE O(1/k): PROVED BY M276.
```

The theorem is for odd `k>=3`, `n=3k`, in the balanced first fixed cell of
the auxiliary uniform minimal-long-cycle factorization law under the nonlazy
cyclic rank-two quotient kernel, with `(pq)(x)=p(q(x))`.  It is not a theorem
about the global identity-word law or its lazy exact same-product `{3,4,5}`
heat-bath chain.

## 2. Frozen provenance

Every inventoried payload verifies.  The independently recomputed
inventory-file SHA-256 digests are

```text
M276  882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M272  af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270  6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
```

M91/M94 supply the previously accepted Borel decomposition and coefficient
bounds; M261/M264 the collision/decorated reductions; and M267/M270 the
literal endpoint-profile normalization and PBV/SET equivalence.  None of
those dependencies supplies M276's new weighted-tail proof.

## 3. Frozen M272's material error

M272 treats `k/2<a<=k` as a bulk range in which every Borel index is
comparable to `k` and each face summand is `O(k^-3/2)`.  But its short-cycle
term at the last interior point is

```text
rho_A(k-1)=nu_k(1)
 =(k-1)^(k-3)/k^(k-2)
 =(1/k)(1-1/k)^(k-3)=Theta(1/k).
```

Hence `k rho_A(k-1)->e^-1`, while
`k^(3/2)rho_A(k-1)` diverges.  M272's next tail display starts at `a>k`,
where `rho_A=0`, and does not cover this point.  The gap is material to its
claimed channel-one bounded-variation proposition.  Accepting M276 does not
edit, rehabilitate, or retroactively accept M272.

## 4. Independent weighted-Borel repair

Put

```text
b_j=e^-j j^(j-1)/j!,
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2),
R_k(c)=b_(k-c)/b_k.
```

For `1<=c<k/2`, the exact ratio identity and its logarithmic expansion give

```text
R_k(c)=O(1),
|R_k(c+1)-R_k(c)|=O(1/k).
```

For `h_c=c b_c`, Stirling and the exact adjacent ratio give

```text
h_c=O(c^-1/2),
|h_(c+1)-h_c|=O(c^-3/2).
```

Symmetry of `nu_k` identifies the omitted near-end profile as

```text
g_k(c):=rho_A(k-c)=c nu_k(c)=h_c R_k(c)/(k-1).
```

Therefore

```text
g_k(c)=O(1/[k sqrt(c)]),
|g_k(c+1)-g_k(c)|
 =O(1/[k c^(3/2)]+1/[k^2 sqrt(c)]).
```

Both difference series are summable over `c<k/2`; the boundary against
`g_k(0)=0` costs `O(1/k)`.  Thus the complete short-cycle near-end tail has
variation `O(1/k)`.

## 5. Corrected channel-one/J1 theorem

The accepted low-range cancellation remains `O(1/k)`.  The genuine
long-cycle central range has per-chord mass `O(k^-5/2)`, adjacent difference
`O(k^-7/2)`, and piecewise-linear counts of size `O(k)`, so its variation is
`O(k^-3/2)`.  The long-cycle far tail is handled by the same weighted-Borel
argument.  Both junctions close; in particular

```text
rho_B(k)=(k-1)nu_(2k-1)(k-1)=rho_B(k+1).
```

Consequently

```text
sum_a |Delta(rho_B-rho_A)(a)|=O(1/k).
```

The exact collision identity has two face terms and two convolution terms.
Using `||delta a||_1=2/k` and `||Delta m||_1=4/k`, each convolution
derivative is at most `8/k^2`.  M276 therefore proves, append-only,

```text
sum_(ell=2)^(n-3)
 |eta_1(I_(ell+1)-I_ell)|=O(1/k).
```

## 6. Unaffected raw laws, coupling, and phase

Clean reconstruction confirms the exact completion laws

```text
F_r(Q)=r! product_i tau(d_i),
nu_Q(e)=F_(r-1)(e^-1Q)/F_r(Q),
N_Q(e,f)=F_(r-2)((ef)^-1Q)/F_r(Q),
```

including both normalizations.  Channel two's fair component choice is
already inside `N_F`; no extra factor `1/2` is present.

The split laws normalize.  With
`D_u=sum_(s<=u)(p_s-q_s)<0`, common-uniform quantiles give `S<=T` and exact
crossing mass `Pr(S<=u<T)=-D_u`.  The full telescoping formula has the sign

```text
E[g(X_T)-g(Y_S)]
 =sum_s q_s(Phi_s-Psi_s)(g)
  +sum_u D_u(Phi_u-Phi_(u+1))(g).
```

It is an expectation identity, not a pathwise response order.  Literal
phase averaging contributes exactly the outside factor `1/n`; stabilizers
of short cyclic orbits introduce no further factor.  The good/bad raw source
partition is exact.  A finite nonzero good vector refutes seam-only equality
but proves no asymptotic signed inequality.

## 7. Unaffected channel-two/J2 reduction

The shared-endpoint probabilities and total masses are exactly

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3),
sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].
```

Their triangle collision derivatives contribute `O(1/k)`.  For the
disjoint masses `p_hat=p(1-gamma_L)` and `q_hat=q(1-gamma_F)`, the endpoint
is nonzero:

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].
```

The exact vector Abel identity retains that boundary term:

```text
R_D=E_(k-1)Phi_(k-1)^D
 +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D)
 +sum_(s<k/2)q_hat_s(Phi_s^D-Psi_s^D).
```

The available `|E_u|=O(sqrt(u)/k)` bound does not permit termwise absolute
values without a new derivative estimate.  M276 makes no such inference.

## 8. Independent checker, objections, and status ledger

M279's checker was written after the analytic proof.  It imports no project
or predecessor module and reads no M276/M272 artifact.  At predeclared
`k=3,5,9` and tail ranks `k=3,5,9,31,101`, it checks the raw completion
normalizations, split laws, quantile crossings, phase factor, shared masses,
nonzero endpoint, vector Abel identity, material flaw, `g_k` identity,
junction closures, and full finite `delta rho` variation.  All checks pass.
The normalized result digest is

```text
39f879bc696d59f5d850ad7d39c9352eb7626353d0d4d18480feaefd8f649cf9.
```

M276's standard-library checker also has no predecessor read.  A replay to
`/tmp` is byte-identical to its frozen results, whose SHA-256 is
`99611a4d3fa23cb6d092f89da9fbeff0ff5ef2d828d3fd2b1440d1bc09b16f09`.
These are finite calibration and reproducibility checks only.

1. Material objections to M276: none.
2. Nonmaterial objections to M276: none.
3. Material objection to M272: its frozen near-end `A`-tail proof gap remains.

```text
M276 and all cited inventories                         verified
corrected weighted-tail BV and J1 O(1/k)               proved
raw laws, coupling, phase, and literal partition       proved exact
J2 shared triangles and vector Abel reduction          proved/exact
CSBV, CEBV, CIBV, DOR                                  unresolved
SET, PBV, FD, FCL1                                     unresolved
gap, polynomial mixing, Terminals                      unresolved
```

## 9. Exact stop, artifacts, and final action

The surviving implication hierarchy is exactly

```text
CSBV + CEBV => CIBV,
CIBV + DOR  => PBV <=> SET.
```

None of `CSBV`, `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, `FD`, or `FCL1` is
proved here.  No bridge/local sampler gap, polynomial mixing theorem, or
Terminal follows.

Artifacts are the plan and checkpoint, detailed proof audit, no-import
checker and retained results, this nine-field report, run manifest, freeze
manifest, and `SHA256SUMS`.  Final action: **accept M276's append-only
salvage at its exact auxiliary scope; leave frozen M272 rejected and every
named downstream obligation unresolved.**
