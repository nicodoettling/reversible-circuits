# M152 initial checkpoint

Date: 2026-08-13 UTC.

## Source reconciliation completed

Read the required project skill, `HANDOFF.md`, `GOAL_SPEC.md`, the sampling
problem reference, and the experiment reference.  `AGENTS.md` names
`references/experiments.md`, which is absent; the available skill-owned file
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was used
and the discrepancy is retained here rather than silently ignored.

Read the frozen M147 proof/report and M151 proof audit/report, plus the
accepted M140 proof/report and M144 report.  M151's nonmaterial normalization
correction is adopted: if `A=A_0/q`, the barred reset display begins `A<=`,
not `A/q<=`.

## Exact starting identities

With `p=D/kappa` and `X=d-j`, the full attachment law is

```text
X ~ BetaBinomial(d,D,kappa-D),
(kappa',D')=(kappa+d,D+X).
```

Thus `E[D'/kappa']=p`.  The excursion subkernel deletes precisely `j=0`,
equivalently `X=d`; that atom has mass

```text
nu_0=(D)^(rise)_d/(kappa)^(rise)_d
```

and child ratio `(D+d)/(kappa+d)`.  Every potential calculation in this
mission will include this deleted atom explicitly.

## Falsifiable target

Determine whether a nonnegative suffix-indexed affine/quadratic potential in
`p` can dominate the corrected reset plus every retained descendant in the
M147 recurrence while remaining at most `1-q_(B,L)` on all right-heavy
states `D=1`.  A failure will be reported only for the precisely tested
family, not as a refutation of arbitrary nonlocal amortization.

## Theorem-level checkpoint

The low-degree affine/quadratic trial led to the exact beta-mixture closure,
which is stronger than a fixed degree ansatz.  If
`Theta~Beta(D,kappa-D)`, every accepted contextual mean is the expectation of
a point function `g_C(Theta)`.  Applying Jensen separately to each canonical
basin gives a nonnegative pointwise reset reward `r_(B,L)(Theta)`.  The
minimal pointwise Bellman integrand is

```text
phi_(B,L)(u)
 =r_(B,L)(u)
  +sum_(h,d) mbar_(L,B)(h,d)q_(B,h-1)
     (1-u^d)phi_(B,h-1)(u).
```

The factor `1-u^d` is exact: it removes the killed `j=0` atom.  Beta-binomial
posterior conjugacy proves universally that

```text
V_(B,L)(kappa,D)=E[phi_(B,L)(Theta)]
```

dominates the exact normalized excursion `H/q` at every valid state.

This natural global majorant is nevertheless exactly refuted as a
right-heavy contraction certificate.  At

```text
(s,kappa,D,B)=(9,2,1,3), L=6,
q=3176523/25000000,
```

the beta-Jensen value exceeds `1-q` by the positive rational

```text
5714491495302498676679596453643417785239504603683
/223395363274892426079078092636160000000000000000000.
```

The exact normalized excursion itself is approximately `0.566375`, leaving
budget slack approximately `0.306564`.  Thus this is an obstruction only to
the pointwise latent-beta Jensen supersolution family.  It does not challenge
the accepted M145/M149 right-heavy `L=6` theorem.  The capped boundary rows in
the JSON are diagnostics and prove no universal passed range.

