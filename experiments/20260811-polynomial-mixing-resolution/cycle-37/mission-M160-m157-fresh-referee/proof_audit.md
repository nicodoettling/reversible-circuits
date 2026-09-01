# M160 proof audit of frozen M157

Date: 2026-08-13 UTC.

## 1. Immutable gate and scope

All seven entries in M157's frozen `SHA256SUMS` verify.  In particular, the
coordinator-supplied digests for `report.md`, `two_beta_theorem.md`,
`two_beta_exact.py`, `two_beta_exact.json`, and `freeze_manifest.md` match
exactly; the supplied plan/checkpoint hashes also match.

The audited object is only the normalized full unweighted reset excursion
`F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection.  It
is not a sampler theorem, all-suffix contraction, auxiliary gap,
`ROOT-MEAN LIFT`, original `{3,4,5}` heat-bath result, polynomial-mixing
result, or project terminal.

## 2. Shared-observation posterior transfer

Let `mu=Beta(D,kappa-D)`,
`L_x(u)=binom(d,x)u^x(1-u)^(d-x)`, and `p_x=integral L_x dmu`.
Posterior conjugacy gives `dmu_x/dmu=L_x/p_x`.  Hence one shared branch
observation gives

```text
p_x mu_x(du)mu_x(dv)
 =[L_x(u)L_x(v)/p_x]mu(du)mu(dv).
```

The single factor `p_x`, rather than `p_x^2`, is essential: the two posterior
copies share `X=x`.  Integrating the right side gives `p_x`.  Therefore the
sum over retained `x=0,...,d-1` has mass `1-p_d`, while the displayed killed
kernel `L_d tensor L_d/p_d` has mass `p_d`.  No survival conditioning is
hidden.

The transfer is state-dependent because every `p_x` depends on `(kappa,D)`.
For `d=1`, the retained coefficient `1/p_0` is `2` at `(2,1)` and `3/2` at
`(3,1)`.  The clean-room checker verifies 504 monomial RN instances and 16
retained/killed mass rows.

## 3. Exact reset and finite equality recursion

For actual endpoint currents `J_E` and capacities `c_E`, direct expansion
gives

```text
A_0/q = integral integral
          [sum_E J_E(u)J_E(v)/(q c_E)] dmu(u)dmu(v).
```

There is no Jensen step here.  If a child equality kernel is multiplied by
the shared-X RN factor and then integrated, the identity in Section 2 gives
exactly the corresponding retained branch mass times the child posterior
expectation.  The exterior normalized coefficient is
`mbar q_child/q`.  Induction is finite because suffix excess strictly
decreases.  This proves M157's exact equality

```text
H(x)/q_x = integral integral K_x dmu_x dmu_x.
```

An independent definitions-level rebuild checks both reset and full equality
at `(3,2,1,1)`, `(8,2,1,2)`, and `(9,2,1,3)`.  At the last state it recovers
49 monomials, M157's coefficient digest
`771567a049b76b2a546874b32de3170b8d1be32b3c7293c1a36cd9d84dec28f4`,
and the exact value

```text
884793664847325174104678035065147237189087444781
/1562205337586660322231315333120000000000000000000.
```

## 4. PSD versus pointwise sign

The PSD assertion is valid as a history-feature assertion.  The reset kernel
is a positive sum of outer products `J_E tensor J_E`.  Inductively, if a
child kernel is `sum_gamma a_gamma f_gamma tensor f_gamma` with
`a_gamma>=0`, then multiplying by
`L_x(u)L_x(v)/p_x` and the positive branch coefficient replaces each feature
by `L_x f_gamma`, again with a nonnegative weight.  Finite suffix descent
therefore supplies an explicit positive sum of history-feature outer
products.  This proves PSD but says nothing about pointwise sign.

At ranks `s=1,2`, every active reset kernel is zero.  At the first possible
rank `s=3`, `B=1`, independent expansion gives exactly M157's displayed
reset polynomial and

```text
R(0,1)=-165/512.
```

For every degree `d>=1`, `L_x(0)` can be nonzero only for `x=0`, whereas
`L_x(1)` can be nonzero only for `x=d`.  No retained `x<d` satisfies both.
Thus every descendant shared-X multiplier vanishes at `(0,1)`, proving
`K_(3,2,1,1)(0,1)=-165/512` exactly.  The pointwise-nonnegative-kernel route
is therefore refuted at the smallest rank where a reset current is active.

## 5. Actual-history diagonal trace

For the actual feature representation,

```text
integral integral K dmu dmu
 =sum_gamma a_gamma(E f_gamma)^2
 <=sum_gamma a_gamma E[f_gamma^2]
 =integral K(u,u)dmu(u).
```

This is a valid Cauchy/Jensen inequality for M157's explicitly generated
features.  It does not invoke the universal ambient canonical-basin frame
refuted by M123/M128.  The clean-room checker verifies the inequality on all
21 fresh rows `B<=3,L<=6` and finds the first budget failure in that stated
order at `(s,kappa,D,B)=(8,2,1,2)`:

```text
trace =
10304304880412164262179965176912695056497059
/12663621893778357952841743000389707366400000,

trace-(1-q) =
132628808872888410508233058471582685297059
/12663621893778357952841743000389707366400000 > 0.
```

The independently computed true value is about `0.4386703515`, so the row
refutes only this positive repair, not the contraction target.

## 6. Relation to M152 polarization and M123/M128

Polarizing each reset feature before propagating child posteriors replaces
`J(u)J(v)` by the average of the two squares.  Under identical beta marginals
this gives the one-copy reward `E[J(Theta)^2]`; applying posterior conjugacy
at descendants gives exactly M152's one-copy killed-atom Bellman recursion.
The independent checker recovers at `(9,2,1,3)` the exact value

```text
200725034388752880197118033887607702918039504603683
/223395363274892426079078092636160000000000000000000,
```

whose positive budget margin is M152's accepted obstruction fraction.  Thus
M157 correctly distinguishes signed two-copy equality from local
polarization.

M123/M128 remains negative provenance only: it refutes generic ambient
canonical-basin frames, including centered variants, while M157 constructs
actual finite contextual/history features and uses no ambient-frame bound.

## 7. Referee disposition

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

Promote only the exact shared-X transfer, signed/PSD equality representation,
and the two scoped positive-repair obstructions.  A specialized
off-diagonal cancellation inequality, all-suffix contraction, every gap, and
both project terminals remain unresolved.
