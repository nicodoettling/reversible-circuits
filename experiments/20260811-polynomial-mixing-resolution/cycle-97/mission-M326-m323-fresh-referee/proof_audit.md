# M326 independent proof audit of frozen M323

Date: 2026-08-14 UTC

## 1. Combined normalization and token

Put `m=k-1`.  Direct algebra gives

```text
alpha_1=4m/[3(3m-1)],
alpha_2=2(2m-1)/[3(3m-1)],
alpha_1+alpha_2=2(4m-1)/[3(3m-1)].
```

The literal mark emits three H/A owner slots and six ordered distinct-owner
C slots, including a zero profile for every mismatch or genuine zero.
Therefore

```text
c_X=r_X(alpha_1+alpha_2),
r_H=r_A=3, r_C=6,
c_H=c_A=2(4m-1)/(3m-1),
c_C=4(4m-1)/(3m-1).
```

This is exactly the corrected M313 normalization; omitting `c_X` would break
the divergence identity.

M323's raw atom fields retain source, live channel, exterior split, ordered
first factors and product, positive-composition kind/anchor/gaps, marked
slot, response profile, completion-count mass, representation factors,
phases, seams, incidences, and zero slots.  Both channels are combined before
normalization.  Disintegrating `g_s` and `f_t` over these complete fibers
gives, for `a=[g-f]_+`, `b=[f-g]_+`,

```text
w(omega)=c_X pi_(s,t) a(P)b(Q)/rho
         Pr[xi_A|s,P]Pr[eta_B|t,Q].
```

Its orientation is `P->Q`; summation recovers the M319/M321 literal edge
coefficient, including profile zero.  The reconstruction is correct.

## 2. Frozen surgery and exception are source-local

`S_pf` switches A/B sources, retains each literal ordered prefix/product and
marked slot/profile, then exchanges token endpoints.  When both switched raw
atoms and the derived residual cell exist, this preserves the unordered
profile edge and reverses orientation.  Its definition does not inspect the
final edge sign.

Likewise

```text
Exc_pf(omega)=Touch_Sigma(xi_A) or Touch_Sigma(eta_B)
```

uses only the marked-owner indicators, support heads, and fixed seam set
`Sigma={0,1,k-1,2k,3k-1}`.  It is sign-independent, source-local, and was
frozen before the sole guard.  Weight equality, supported landing, and
involution on its complement were targets, not previously proved facts.

## 3. Exact source-B bad-prefix witness

At `k=7`, both source residuals have three cycles and hence rank `21-3=18`:

```text
Q_A: C_-=(0,...,6), M=(7,...,13), C_+=(14,...,20),
Q_B: {0}, L=(1,...,6,14,...,20), M=(7,...,13).
```

For the frozen prefix

```text
e=(6,14),       f=(3,5),
```

`e` lies inside B's long cycle `L`, so it cuts that cycle; after this cut,
`3,5` remain in one child cycle and `f` cuts again.  Thus the B ranks are

```text
18 -> 17 -> 16.
```

For A, `6` and `14` lie in distinct exterior cycles, so `e` joins them and
raises rank.  The second edge then cuts the joined cycle:

```text
18 -> 19 -> 18.
```

Therefore this literal B prefix has no opposite-source A raw atom in a
minimal completion.  This component/rank obstruction is exact.

For its H2 slot, the frozen result has

```text
marked owner support {3},
support heads        {2,4,5,13},
Sigma                {0,1,6,14,20}.
```

Both displayed intersections with `Sigma` are empty.  Notice that the prefix
edge itself uses seam vertices `6,14`; the frozen `Exc_pf` deliberately tests
only the marked owner and heads, so the B atom is outside its atom-level
`Touch_Sigma` predicate.

## 4. Exact rational consistency

For `m=6`, `c_H=46/17`.  The first quantile-cell mass is

```text
pi_(1,1)=p_1=(12/13)^10=61917364224/137858491849.
```

The witness profile has

```text
g_A(Q)=0,
f_B(Q)=b(Q)=21484375/54238159872,
rho=49168032837363259/1633552709319917568>0.
```

Its B raw conditional marked mass is
`21484375/40089074688`.  The exact relation

```text
c_H f_B(Q)=2(21484375/40089074688)
```

shows that this particular B atom has conditional probability `1/2` inside
its normalized profile fiber.  Summing its token weight over the entire A
positive residual side cancels `sum_P a(P)/rho=1` and gives

```text
c_H pi_(1,1)b(Q)(1/2)
 =pi_(1,1)(21484375/40089074688)
 =22000000000/91400180095887>0.
```

Thus all reported rational values are mutually consistent.  The exact count
`420` is also what the authenticated loop records: B-side non-Touch,
positive-residual, opposite-prefix-invalid raw-slot/cell incidences.

## 5. Material endpoint-quantifier gap

The preceding positive mass is integrated over **all** A residual atoms.
But token-level nonexceptionality requires both

```text
not Touch_Sigma(xi_A),       not Touch_Sigma(eta_B).
```

The guard constructs `marks_a` only as an aggregated profile measure and
discards the A raw-slot list.  Its candidate loop iterates only through B
raw slots and applies both seam-intersection tests only to that B atom.  No
A atom `xi_A` is recorded, and no positive A residual mass outside
`Touch_Sigma` is established anywhere else in the frozen package.

Consequently the package proves that the bad B atom participates in positive
token mass and is itself non-Touch; it does **not** prove that any token
carrying it lies outside the OR-defined `Exc_pf`.  All of its A partners
could, on the frozen evidence, be exceptional.  Therefore the conclusions

```text
there is an actual token outside Exc_pf,
S_pf is undefined off Exc_pf,
SLPF is refuted at its stated domain
```

do not follow.  This is a material gap, not a request to rerun the guard.

## 6. Enlarged exception and exact flux split

For a source-R raw prefix, `BadPref_R` tests whether the same ordered prefix
fails the two rank-decreasing conditions for the opposite source.  It uses
only fixed source components and the literal prefix, not a final profile-edge
sign.  The frozen B witness satisfies `BadPref_B` by `18->19->18` under A.

On the complement of

```text
Exc_pf^*=Exc_pf union BadPref_A(xi_A) union BadPref_B(eta_B),
```

both opposite-source prefixes pass the minimal-rank support test.  Partitioning
the literal signed token measure by this predicate gives the exact linear
identity

```text
J=J_compatible+J_exceptional.
```

This partition proves no cancellation.  Landing in a supported reverse
residual cell and exact compatible weight equality/coboundary remain open.
The combined exceptional bounds

```text
mass(Exc_pf^{*,H_d}) <= C d b_d/k,
mass(Exc_pf^{*,A_d}) <= C d b_d/k,
mass(Exc_pf^{*,C_de})<= C max(d,e)b_d b_e/k
```

also remain open formulations.  M323 does not prove or estimate any one of
them, and it correctly makes no MPCF or downstream inference from `SLPF*`.

## Scope result

No new guard, row, rank, source surgery, final-sign matching, scalar path
bound, channel/type/cell split, or downstream theorem has been used.
