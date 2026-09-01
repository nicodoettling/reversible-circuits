# M157 halfway checkpoint

Status: final derivation and capped exact audit complete; frozen report is
being prepared.

The exact Bayes calculation gives, for
`L_x(u)=binom(d,x)u^x(1-u)^(d-x)` and
`p_x=E_mu[L_x]`,

```text
p_x mu_x(du)mu_x(dv)
 =L_x(u)L_x(v)/p_x mu(du)mu(dv).
```

Therefore the retained transfer is the positive but state-dependent kernel

```text
T_ret(u,v)=sum_(x=0)^(d-1)L_x(u)L_x(v)/p_x.
```

The removed `x=d` term is not discarded.  The exact reset kernel is

```text
R(u,v)=sum_E J_E(u)J_E(v)/(q c_E),
```

which has a nonnegative double-beta integral but need not be pointwise
nonnegative.  The finite exact recursion is PSD but pointwise signed.  Its
first sign witness is `K_(3,2,1,1)(0,1)=-165/512`.  The natural full-history
diagonal-trace majorant first exceeds budget in the capped fresh grid at
`(s,kappa,D,B)=(8,2,1,2)`, while the true value has large slack.  Local reset
polarization separately reproduces M152's accepted Jensen obstruction.  The
standalone checker reports zero failures under the assigned caps.
