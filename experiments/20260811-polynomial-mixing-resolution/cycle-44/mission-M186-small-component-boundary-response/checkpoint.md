# M186 Checkpoint

## Start checkpoint

- Owned directory initialized before substantive work.
- The complete reversible-circuit-sampler skill has been read for this
  assignment.
- Target, composition convention, exact source pair, and prohibited
  inferences are fixed in `plan.md`.
- Next mandatory gate: verify accepted M91, M174/M178, M180/M182, and relevant
  fixed-cell dependency manifests before deriving or adopting claims.

No conclusion on `(SCBR)` or `(BIR)` has yet been reached.

## Halfway checkpoint

### Frozen dependency gate

Every accepted manifest in the fixed-cell chain passed: M91, M94/M100,
M102/M105, M155/M159, M161/M166, M168/M171, M174/M178, and M180/M182.
No predecessor has been edited.

### Exact combined critical-Borel formula

Let `F=C_- C_+` be A's two exterior `k`-cycles, `L` B's exterior
`(2k-1)`-cycle, and `M` the common middle `k`-cycle. For a residual
permutation `Q`, define its exact first-edge and ordered-pair laws

```text
lambda_Q(e)=F_(r(Q)-1)(eQ)/F_(r(Q))(Q),
Lambda_Q(e,f)=F_(r(Q)-2)(feQ)/F_(r(Q))(Q).
```

These are explicit critical-Borel products. If `chi_(r,d)(e,f)` counts
run-type-`r`, size-`d` components of `(ef)^-1h`, then the complete signed
coefficient is exactly

```text
M_r(d)=alpha_1{sum_(e in L,f in M)lambda_L(e)lambda_M(f)chi
               -sum_(e in F,f in M)lambda_F(e)lambda_M(f)chi}
      +alpha_2{sum_(e,f)Lambda_L(e,f)chi
               -sum_(e,f)Lambda_F(e,f)chi}.
```

Thus channels, kinds, shared-endpoint collisions, and both double colors are
inside a single coefficient before any absolute value. Grouping the first
exterior edge by its smaller split gives M91's exact Abel form with `p_s`,
`q_s`, `D_u`, and literal component-count profiles
`Phi_(j,s),Psi_(j,s)`; the checker is being used to verify that identity
coefficientwise only at `k=3,5`.

### Closed `J=1` face law

Put

```text
nu_D(a)=(D-2)! tau(a)tau(D-a)/D^(D-2),
rho_A(a)=(k-a)nu_k(a),                  1<=a<k.
```

For `D=2k-1`, let

```text
S_k(a)=(k-1-a)_+ +(k-a)_+,
C_k(a)=a-1       (2<=a<=k),
       =2k-a     (k<a<=2k-1),
       =0        otherwise.
```

Literal classification of an exterior chord as same-run or cross-run gives

```text
rho_B(a)=S_k(a)nu_D(a)+C_k(a)nu_D(a-1),              (H1-face)
```

with invalid indices zero. Both are probability laws. If

```text
G_n(a,b)=u_1(a)+u_1(b)+u_2(n-a-b),
```

then every `J=1` product, separated or nested, has this same charge with
`a` the exterior face avoiding `M` and `b~rho_A` the middle face. Hence,
before multiplying by `alpha_1`,

```text
M_1^(1)(d)=rho_B(d)-rho_A(d),
M_2^(1)(d)=sum_(a+b=n-d)[rho_B(a)-rho_A(a)]rho_A(b). (H1-coeff)
```

This is an exact one-dimensional collapse retaining the cross-run/two-run
boundary correction.

### Proved scale for the face law; remaining issue

Critical-Borel ratio stability gives

```text
sum_a |rho_B(a)-rho_A(a)|/a=O(1/k),
sum_(a,b)|rho_B(a)-rho_A(a)|rho_A(b)/(n-a-b)=O(1/k).
```

The proof splits `a<=k/2`, where the pointwise defect is
`O(a(b_a+b_(a-1))/k)`, from the bulk and the exact tail
`rho_B(2k-c)=c nu_(2k-1)(c)`. Therefore the conditional `J=1` charge has
the required `O(1/k)` scale. This estimate is **not** being used to split
the two channels under the final absolute value.

The unresolved work is the full channel-combined `J=2`/prefix cancellation.
The intended strict remaining lemma is a cumulative bound on the already
combined coefficients; signed summation by parts against the exact
`u_1-u_2` sequence will then imply `(SCBR)`. No SCBR/BIR conclusion is made
at halfway.

## Final checkpoint

- The cap was honored: no further broad derivation or computation was
  launched after isolating the full-channel prefix obligation.
- Exact `(CB)` and `(BA-C)` retain both channels, both residual kinds,
  triangles, double colors, and collision faces before any estimate.
- The complete `J=1` face law and its conditional `O(1/k)` charge are
  proved. The combined singleton coefficient is also `O(1/n)`.
- Exact signed summation by parts isolates `J=2` and the remaining combined
  cancellation in `(PCR)`/`(WPCR)`. Neither condition is proved, so
  `(SCBR)`, `(BIR)`, `(BR)`, and PCS-bound remain unresolved.
- The corrected finite diagnostic uses exactly `2<=d<=D`; exact `k=3,5`
