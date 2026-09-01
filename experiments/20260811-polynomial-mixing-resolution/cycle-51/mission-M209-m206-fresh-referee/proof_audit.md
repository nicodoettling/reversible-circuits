# M209 independent proof audit of frozen M206

Date: 2026-08-13 UTC.

## Referee verdict

**ACCEPT, with no material objections.** Frozen M206 correctly proves its
universal `B=2` suffix-zero annihilation and the stated exact two-row
slack-ladder facts. It correctly refutes only a universal terminal-only
transfer. It does not promote the finite `h=1,2` payment to a universal
theorem and does not claim a universal contraction result.

## 1. Immutable-source gate

M206 has exactly nine files, comprising its SHA ledger and eight payloads.
All eight payload hashes verify, and the ledger digest is

```text
32aaa34fc8ec8a19851621a912d834eec5d7b00e339fea8826a589286417a866.
```

The complete accepted ledgers M173/M177, M179/M184, M193/M197, and
M201/M204 also pass. No predecessor was edited.

## 2. Definitions and sign audit

Let the exact fresh-parent orthogonal decomposition be

```text
T_1=T_reset+sum_(h=1)^L T_h.
```

Using M206's definitions

```text
Delta=1-q-U_1-U_2-U_3,
S_h=U_h-T_h,                         h=1,2,3,
X=T_reset+sum_(h=4)^L T_h-Delta,
```

one obtains, identically,

```text
S_1+S_2+S_3-X
=U_1+U_2+U_3- T_1-T_2-T_3
 -T_reset-sum_(h>=4)T_h+Delta
=(1-q)-T_1.
```

Thus the signs are correct: `S_h>0` is unused accepted lower-sector budget,
whereas `X>0` is reset/high-tail charge above the nominal residual. The
unresolved cumulative lemma `X<=sum S_h` is equivalent to the desired fresh
parent inequality; M206 does not assert it has been proved.

## 3. Universal B=2 annihilation

A fresh `B=2` height-one branch has `t=3`, hence child total/bottom `(2,2)`
with beta parameters depending on the observation. The only ordered
compositions are `(2)` and `(1,1)`.

- No last part exceeds bottom two, so no root descendant is live.
- `(2)` has no cut.
- The only cut of `(1,1)` has activity score `1+1-1=1<2`, so no canonical
  reset endpoint is active.

Both components of the recursive feature space are empty. Therefore
`Phi_(2,kappa,D,2)=0` for every valid `kappa,D`, independently of beta
parameters. Every fresh `B=2` height-one actual charge is zero for every
`L>=1`. M206's universal statement is correct.

## 4. Independent exact-history reconstruction

The M209 checker is standard-library only and imports no predecessor. It
uses grouped Cayley root masses, rather than the literal ordered-root engine
used by M206. At each live group it applies

```text
eta=m_s(d,t)q_child/q_parent,
eta/pi_a * L_a(u)L_a(v)K_child(u,v),
a=0,...,d-1.
```

The killed value `a=d` is absent. The bivariate Gram kernel retains all
within-branch likelihood cross terms. The final functional retains the exact
parent covariance subtraction. Applying `T_1` to the assembled kernel equals
the sum of reset and all height-sector charges at both audited rows.

## 5. Exact B=2,L=4 terminal payment

The independent reconstruction gives

```text
S_1=3299/56250,
X=480024264873449410111/8339940489100500000000,

S_1-X
=9103978211751469889/8339940489100500000000>0.
```

Thus terminal unused slack alone pays the reset/height-four excess in this
one decisive row. The full true slack is also positive, exactly as M206
states.

## 6. Exact B=3,L=4 obstruction and finite next rung

The grouped-root reconstruction independently reproduces every charge and
bound and gives

```text
S_1-X
=-58850574391835735352420545363
  /1474064677007114895360000000000<0,

S_1+S_2-X
=183315802718619702462160882861
  /1474064677007114895360000000000>0.
```

Therefore this row is an exact counterexample to universal terminal-only
payment and an exact finite positive two-rung row. Its true slack is

```text
445256035370256335108738960557
/1474064677007114895360000000000>0,
```

so it is not a contraction counterexample.

## 7. Orthogonality and logical scope

The actual-history Hilbert space is an orthogonal direct sum of reset and
distinct `(d,t,a)` branch copies. Both the raw trace and the squared norm of
the centered mean split across those copies. Hence `T_1` is sector-additive;
there is no literal cross-sector Gram cancellation. This does not delete
cross terms internal to a likelihood-weighted child, all of which the exact
Gram recursion retains.

Positive `U_h-T_h` is an inequality residual, not necessarily actual feature
energy. The zero `B=2` terminal feature with positive `U_1` makes this
distinction explicit. M206 states it correctly.

## 8. Numbered objections

1. **Material objections: none.** Every promoted exact claim reproduces.
2. **Sign challenge, dismissed.** Direct algebra gives the displayed master
   identity with the stated signs.
3. **Universality challenge, dismissed.** The `B=2` proof is independent of
   `kappa,D,L`; the `B=3` two-rung payment is explicitly labeled finite.
4. **Missing-cross-term challenge, dismissed.** Sector additivity follows
   from orthogonal copies, while all within-sector cross terms remain present.
5. **Overreach challenge, dismissed.** M206 leaves the cumulative three-rung
   lemma unresolved and makes no total-AMV, gap, mixing, or Terminal claim.

## 9. Scope boundary

This referee certifies only M206's exact definitions, universal `B=2`
annihilation, and the two named `L=4` rows. No other row, tail inequality,
universal two-rung claim, contraction theorem, total AMV, gap, mixing, or
Terminal conclusion was tested or inferred.
