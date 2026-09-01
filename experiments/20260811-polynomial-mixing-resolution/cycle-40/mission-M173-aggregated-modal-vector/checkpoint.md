# Mission M173 checkpoint

Date: 2026-08-13 (UTC)
Status: halfway theorem derivation complete; aggregate estimate in progress

## Immutable/source gate

The required project skill and core source-of-truth documents were read. All
`SHA256SUMS` entries in frozen M147/M151, M157/M160, M162/M165, and M167/M170
verify. M170's two nonmaterial corrections are carried forward: cite M167's
report (not its truncated theorem Section 6) for the AMV target, and separate
the `r=n` line in the terminal eta bound.

## Corrected exact branch normalization

For retained observation `a<d`, the feature block is

```text
f_a(u)=sqrt(eta/pi_a) L_a(u) Phi_a(u),
L_a dmu_parent=pi_a dmu_a.
```

Thus

```text
E_parent||f_a||^2
 =(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_mu_a[L_a||Phi_a||^2],
```

not `eta E_parent[L_a||Phi_a||^2]`. Its parent mean and centered covariance
are `sqrt(eta*pi_a)M_a` and
`sqrt(eta*pi_a)(delta_a M_a+C_a)`, respectively. Therefore its exact
contribution to parent `T_1` is

```text
eta { E_mu_a[L_a||Phi_a||^2]
      -(pi_a/sigma_parent^2)||delta_a M_a+C_a||^2 }.
```

The killed atom `a=d` is absent exactly and is never survival-conditioned.

## Modal decomposition and closure distinction

Writing under the child law

```text
Phi_a=M_a+(u-p_a)C_a/sigma_a^2+Z_a,
E Z_a=E[(U-p_a)Z_a]=0,
```

the likelihood-weighted trace expands into six vector terms: weighted
`||M||^2`, `||C||^2`, `||Z||^2`, and the three cross terms
`<M,C>`, `<M,Z>`, `<C,Z>`, followed by the exact subtraction above. This is
an exact recursion only when `Z_a` is retained as the full Hilbert-valued
polynomial (or equivalently all required `L_a`-weighted moments). It does not
close on the finite summary `(M,C,||Z||^2)`.

A compact unrestricted-operator witness is already exact: for parent
`Beta(1,1)`, degree-one retained `a=0`, and child `Beta(1,2)`, take the
unit-normalized child Jacobi polynomials of degrees two and three. Both have
`M=C=0` and `||Z||=1`, yet their lifted parent `T_1` charges are `18/35` and
`32/63`, respectively. These are unrestricted operator examples, not claimed
actual histories.

## Current terminal target

For the terminal `h=1` exterior weights `eta_(n,r)` and the accepted fresh
constant-child operator charge `R_(r+1)`, test analytically the standalone
aggregate inequality

```text
S_n=sum_(r=1)^n eta_(n,r)R_(r+1) <= 1/4.
```

Only a proof will be promoted; finite values are diagnostic. Even if proved,
this controls only the normalized constant-child terminal operator sector,
not reset terms, general actual child norms, the AMV budget, or the universal
all-suffix boundary. No `L=7` enumeration or broad scan has been run.
