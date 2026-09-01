# M204 independent proof audit of frozen M201

Date: 2026-08-13 UTC.

## Referee statement

**ACCEPT.** Frozen M201 correctly proves the following strict route
obstruction at the single fresh parent `(B,L)=(2,4)`: reserving its compatible
same-parent accepted `h=1,2,3` upper bounds leaves a residual `Delta` that is
strictly smaller than the exact actual-history reset plus `h=4` charge.

This does **not** refute the true parent contraction inequality, the accepted
height-one theorem, the accepted height-two theorem, or the accepted
height-three theorem. It proves no new tail lemma.

## 1. Immutable-source gate

M201's complete eight-payload SHA ledger passes, its inventory is exactly the
ledger plus those eight payloads, and its SHA-ledger digest is

```text
9ede2ffaf0815cc76d8a7811d542d4a967370ee10791af73a590692ecacd524a.
```

The accepted M173/M177, M179/M184, and M193/M197 input ledgers also pass.
No predecessor was edited.

## 2. Parent probabilities and compatible reservations

With `w_j=j^(j-1)/j!`, literal substitution gives

```text
q = w_5 w_2/w_7 = 3750/16807 = 26250/117649,
q0= w_2/w_3     = 2/3.
```

For `h=1`, the three exact rows at `n=L-1=3` are

```text
r    eta^(1)    R_(r+1)
1    18/125     3/4
2     8/125     649/700
3     1/125     113/105
```

They give `A1(3)=3299/18750` and hence
`U1=(1-q0)A1=3299/56250`. The accepted exact exterior formulas give

```text
M2(2)=36/125,   U2=(2/3)M2(2)=24/125,
M3(1)=36/125,   U3=(3/4)M3(1)=27/125.
```

Therefore

```text
Delta=1-q-U1-U2-U3=293289307/945393750.
```

These are compatible same-`L` coefficients, not a sum of the three global
worst-case constants.

## 3. Independent actual-history normalization

The referee checker imports no M201 artifact and does not reuse M201's grouped
Cayley-root routine. It enumerates literal ordered compositions `c` with root
mass

```text
rho(c)=prod_i w(c_i)/(len(c)! w(sum(c)+1)).
```

The exact masses normalize to one at every recursive size used. For a live
branch it applies the exterior `rho(c) q_child/q_parent`, the beta-binomial
probability `pi_a`, and the polynomial likelihood for `a=0,...,d-1`. The
killed observation `a=d` is absent. It lifts the entire child bivariate Gram
kernel by both likelihood polynomials, so all likelihood-weighted cross terms
remain present.

Finally it evaluates

```text
E ||Phi||^2
- ||E[(U-EU)Phi]||^2 / Var(U)
```

exactly under the parent beta law. Thus reset currents, Bayes normalization,
observation dependence, and covariance subtraction are independently checked.

## 4. Exact decisive charges

The independent expansion reproduces

```text
T_reset=6628367198857337/21450464220937500,
T_h1   =0,
T_h2   =22259/1575000,
T_h3   =6974311/300000000,
T_h4   =1735419680239/29524500000000.
```

No `h>4` child exists at `L=4`. The claimed route margin is exactly

```text
T_reset+T_h4-Delta
=480024264873449410111/8339940489100500000000 > 0.
```

This proves failure of the independent-reservation route at the named state.

## 5. Full-parent self-attack

Adding every actual first-level term gives

```text
T1=422384074903914714287/1042492561137562500000.
```

Since `1-q=13057/16807`, the exact true contraction slack is

```text
(1-q)-T1
=387506171468022785713/1042492561137562500000 > 0.
```

Thus the witness is not a contraction counterexample. Actual `h=1` is zero,
and actual `h=2,h=3` are each strictly below the accepted reservations; the
unused lower-height slack is precisely what the rejected additive route
discarded.

## 6. Numbered objections

1. **Material objections: none.** All decisive fractions independently
   reproduce by a differently organized exact recursion.
2. **Normalization challenge, dismissed.** Literal root masses remove any
   dependence on M201's grouped multiplicity formula and still give the same
   reset and descendant charges.
3. **Killed-atom challenge, dismissed.** The independent branch loop is
   exactly `a=0,...,d-1`; adding `a=d` would be a different, invalid history.
4. **Scalarization challenge, dismissed.** The checker carries the complete
   bivariate Gram kernel and all likelihood cross terms through covariance
   subtraction.
5. **Logical-overreach challenge, dismissed.** M201's theorem and final report
   explicitly limit the refutation to independent lower-sector reservation;
   they explicitly retain true contraction and the individual accepted sector
   results.

## 7. Scope boundary

This audit certifies only the exact `(B,L)=(2,4)` route obstruction. It makes
no claim about a tail bound, the proposed joint amortization lemma, nonfresh
states, total AMV, all `L`, a spectral gap, mixing, or Terminal A/B.
