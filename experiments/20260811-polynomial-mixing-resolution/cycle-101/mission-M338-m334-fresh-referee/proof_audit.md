# M338 independent proof audit of M334

Date: 2026-08-14 UTC

Verdict: **ACCEPT at the frozen AOEC-only scope.**

## 1. Exact active-owner identity

Fix a truncated endpoint `T`, exterior atom `e`, middle phase `a`, and target
phase `x`. If either target boundary tail is nongeneric, the term is zero. If
both tails have the same residual owner of size `d`, completing after consuming
two tails contributes

```text
kappa_(S_d)=tau(d-2)/tau(d)=b_d.
```

If the tails have distinct owners of sizes `d,e`, completing after consuming
one tail from each contributes

```text
kappa_(X_(d,e))
  =[tau(d-1)/tau(d)] [tau(e-1)/tau(e)]
  =a_d a_e.
```

Every inactive owner contributes `tau(r)/tau(r)=1`. Therefore grouping the
literal response only after summing the exact signed truncated exterior law,
all middle phases, and all target phases gives

```text
Psi(T)=sum_A kappa_A Delta_T(A).                    (AOTI)
```

This is an exact regrouping, with every `kappa_A>0`; it assigns no sign to an
individual `Delta_T(A)`.

For consecutive canonical endpoints put
`delta_(q,A)=Delta_(T_q)(A)-Delta_(T_(q-1))(A)`. Subtracting AOTI at the two
endpoints gives the exact coefficient-resolved coboundary

```text
Psi(T_q)-Psi(T_(q-1))=sum_A kappa_A delta_(q,A).
```

The ownerwise causal-flow equations are equivalent to the additional
ownerwise prefix inequalities `Delta_(T_q)(A)>=0`; they are not asserted by
the identity.

## 2. Clean-room fixed `k=7` reconstruction

`independent_aoec_audit.py` authenticates M311's no-import source, specializes
only `K=11` to `K=7` and its lag-count assertion, and reimplements the active
incidence accumulation without importing M334 code or JSON.

The reconstruction retains exactly:

- all `u=1,2,3` and all 7 middle phases for each `u`;
- all 18 admissible lags and all 21 target phases;
- every positive cross exterior atom;
- every negative internal atom and the seam atom separately;
- the exact quantile transport weights and all three canonical block
  endpoints.

It performs 31,752 statewise AOTI checks and 162 block-prefix AOTI checks.
The positive, absolute-negative, and transport masses all reproduce as

```text
656493830500/1792160394037.
```

Terminal signed-law reconstruction and lag reflection pass exactly.

## 3. First AOEC failure

The independently reconstructed first lexicographic negative is

```text
(u,ell,block,A)=(1,2,0,S_14),  endpoint b=3,
T=5665610708886866/30120839742579859.
```

At this prefix,

```text
positive cross mass     = 0,
negative internal mass = 11343430713381552/30120839742579859,
negative seam mass     = 5184/16807.
```

Since

```text
30120839742579859 / 16807 = 1792160394037
```

the seam numerator on the common denominator is
`5184*1792160394037=9290559482687808`. Hence

```text
Delta_T(S_14)
 =0-(11343430713381552+9290559482687808)
       /30120839742579859
 =-20633990196069360/30120839742579859 < 0.
```

The clean-room guard also reproduces exactly 2,920 negative and 7,364 nonzero
active-prefix instances. Its first row, exact components, aggregate fraction,
and counts agree field-for-field with frozen `aoec_k7.json`.

## 4. Logical scope

The displayed negative value is a direct counterexample to universal
active-owner componentwise nonnegativity, so `AOEC_1` is **refuted**.
AOTI and the coefficient-resolved coboundary remain exact identities.

The negative `S_14` component can still be offset by other active types after
the positive coefficients are applied. Thus the counterexample neither
refutes nor proves the scalar GQAC prefix inequality. GQAC and MCLP remain
**unresolved**. No conclusion follows for GOCI, OCI, CP, MS, FCL1, a spectral
gap, polynomial mixing, or Terminal status.

## 5. Numbered objections

1. Material objections: **none**.
2. Nonmaterial objections: **none**.
