# M213 independent proof audit of frozen M210

Date: 2026-08-13 UTC.

## 1. Verdict and scope

`ACCEPT`. M210 correctly freezes a reformulation and state-variable
obstruction, not a proof of the universal cumulative inequality. This audit
concerns only fresh-parent first-Jacobi accounting. It proves no universal
`C_3`, total AMV, spectral gap, mixing theorem, or project Terminal.

## 2. Exact accounting

Using M210's definitions,

```text
C_3 = U_1+U_2+U_3-(T_1^sector+T_2^sector+T_3^sector),
X_3 = T_reset+sum_(h>=4)T_h-(1-q-U_1-U_2-U_3).
```

Subtracting and collecting all orthogonal sector charges gives

```text
C_3-X_3
 =1-q-[T_reset+sum_(h>=1)T_h]
 =(1-q)-T_1.
```

Thus `C_3>=X_3` is logically identical to the open fresh boundary
`T_1<=1-q`; it is not a narrower amortized lemma.

## 3. Exact full-kernel recursion

For a PSD child Gram kernel `K_a(u,v)=<Phi_a(u),Phi_a(v)>`, Bayes likelihood
`L_a`, and `pi_a=E_mu L_a`, the actual retained feature coordinate is

```text
sqrt(eta/pi_a) L_a(u) Phi_a(u).
```

Its Gram contribution is therefore exactly

```text
eta L_a(u)L_a(v)K_a(u,v)/pi_a.
```

Distinct reset/history coordinates are orthogonal and the killed observation
`a=d` has no coordinate. Consequently

```text
K_zeta=R_zeta+sum_(live d,t) sum_(a<d) eta_(d,t) Lift_(d,a)[K_a],
Lift_(d,a)[K](u,v)=L_a(u)L_a(v)K(u,v)/pi_a.
```

This verifies the sensitive single `1/pi_a` factor and retains all
likelihood-weighted cross terms through the full Gram kernel.

## 4. Positive functional and monotonicity

For `U~mu_zeta`, mean `p`, variance `sigma^2`, define

```text
Q[K]=E K(U,U)
 -(1/sigma^2) E E'[(U-p)(U'-p)K(U,U')].
```

If `K=<Phi,Phi>`, then

```text
Q[K]=E||Phi(U)||^2-||E[(U-p)Phi(U)]||^2/sigma^2 >=0
```

by Hilbert-valued Cauchy--Schwarz/Bessel. The formula is linear in `K`, so
`Q` is a positive linear functional on the PSD cone. Likelihood lifting
preserves PSD because it replaces `Phi` by `L_a Phi/sqrt(pi_a)`. Hence

```text
K <=_PSD H  =>  Q[Lift K] <= Q[Lift H].
```

Applying `Q` to the recursion gives

```text
D_zeta=1-q_zeta-Q[R_zeta]-sum eta Q[Lift K_a].
```

Precision clarification: each child **charge map** is positive linear and
order-preserving; the residual `D_zeta` is affine and order-reversing in
each child kernel. M210's equations and Section 4 use this sign correctly.
Only its Section 1 phrase “the residual is a positive linear functional” is
imprecise, so this is nonmaterial.

## 5. Constant-kernel obstruction

Let `J(u,v)=1`. If `K=<Phi,Phi> <=_PSD cJ`, test the two-point Gram matrix
at `u,v` against coefficients `(1,-1)`. The `cJ` quadratic form is zero,
whereas the `K` form is `||Phi(u)-Phi(v)||^2`. Positivity of `cJ-K` would
force this squared norm to vanish for every pair. Thus a constant kernel can
PSD-dominate only a constant feature, proving M210's obstruction.

The weaker functional preorder
`K_zeta <=_(zeta,1) (1-q_zeta)J` is exactly
`Q[K_zeta]<=1-q_zeta`, hence merely restates the target.

## 6. Exact scalar-summary nonclosure

For child `Beta(1,2)`,

```text
P_2=u^2-(4/5)u+1/10,       ||P_2||^2=1/300,
P_3=u^3-(9/7)u^2+(3/7)u-1/35, ||P_3||^2=1/4900.
```

Both are orthogonal to degrees zero and one. After normalization they have
the same `(M,C,||Z||^2,T_1)=(0,0,1,1)`. For the retained `d=1,a=0`
likelihood `L=1-u` at a uniform parent, direct application of the parent
`Q` gives respectively `18/35` and `32/63`; both parent first-mode
subtractions vanish. Therefore the listed summaries cannot determine the
exact lifted charge.

The valid inference is limited: this unrestricted witness is not an
actual-history counterexample, does not rule out every scalar upper envelope,
and does not prove that a full Gram kernel is the uniquely minimal possible
state. It proves that an exact recursion needs information distinguishing
these likelihood-weighted residual shapes; the full kernel (or equivalent
queried moments) is sufficient.

## 7. Numbered objections

1. **Material objections:** none.
2. **Nonmaterial wording:** M210 Section 1 should call the child charge map,
   not the residual, positive linear. The residual is affine antitone. All
   displayed formulas and deductions have the correct sign.
3. **State minimality:** no objection. M210 explicitly limits nonclosure to
   the listed summaries and leaves new operator envelopes possible.
4. **Logical promotion:** no objection. M210 explicitly says the full-kernel
   majorant lemma is unresolved and not yet a strict logical reduction.
