# M340 analytic obstruction to XCRF

Date: 2026-08-14 UTC

Status: **the frozen complete-label XCRF is refuted by a singleton Hall
defect.  No M340 finite guard was run.**

## 1. Complete labels leave no transport freedom

Off `Exc_pf^*`, the accepted raw source switch is deterministic: a complete
raw endpoint label has exactly one opposite-source label, and switching back
recovers the original.  Consequently a complete raw token `omega` has only
the formal reverse pair `Phi(omega)` of `candidate.md`.

This gives the exact local alternatives:

```text
(i)  Phi(omega) is absent from the canonical reverse residual law;
(ii) Phi(omega) has the same derived cell, so no XCRF cross-cell arc exists;
(iii) one cross-cell arc exists, and its sole feasible flow amount must be
      both w(omega) and w(Phi(omega)).
```

Thus rational splitting cannot pool weights across cells while all complete
source-switch labels are retained.  In case `(iii)` the singleton Hall
condition is exactly

```text
w(omega)<=w(Phi(omega)),
```

and the reverse singleton condition plus total balance forces equality.
Cases `(i)` and `(ii)` instead have `N({omega})=empty`, so Hall requires
`w(omega)<=0`.

## 2. Accepted off-exception isolated supply

M335 constructed, and the fresh M336 audit accepted, one exact token with

```text
k=9, n=27, row H_2, c=(s,t)=(1,1),
Sigma={0,1,8,18,26}.
```

Its source-A endpoint is

```text
channel 2, split 1, e=(3,4), f=(4,5), slot 1,
profile P=0, empty marked-owner support, heads {2,3,4},
```

and its source-B endpoint is

```text
channel 2, split 1, e=(3,4), f=(4,6), slot 2,
profile Q=(-1,0,...,0,1),
marked-owner support {4}, heads {2,3,5}.
```

All displayed support/head sets miss `Sigma`.  Both opposite-source prefixes
exist with positive exact completion masses; switching back restores each
prefix.  Hence the original and formal switched raw pairs are both outside
the frozen `Exc_pf^*`.  This is an actual complete-label orbit, not a
profile-only surrogate.

The original exact residual factors include

```text
c_H=62/23,
pi_11=72057594037927936/168377826559400929,
rho_11=2354028198661286694240715
       /102166958637249138505285632,
a_11(P)=583013693948397585119897
        /34055652879083046168428544,
b_11(Q)=3296284725931531/9493588014497005568,
u_A=20841167403/73338099464768,
u_B=198428693313536/6311626321257167.
```

With all constituents combined as in `(1.1)` of `candidate.md`, its supply
mass is

```text
w(omega_0)
=425758390993809446972368496973627659814865534216945520778179328
 /160127614349801894448349798657905382956928144305646616084388152620616845
>0.                                                       (2.1)
```

Both switched endpoint splits remain 1, so

```text
c(Phi(omega_0))=(1,1)=c(omega_0).                    (2.2)
```

Moreover canonical positive-part disjointness in this cell gives exactly

```text
a_11(Q)=0,                  b_11(P)=0.               (2.3)
```

Therefore `Phi(omega_0)` is not a reverse residual token at all.  Even if a
same-cell arc were permitted, it would have zero demand mass; under the
frozen cross-cell relation it is excluded already by `(2.2)`.

## 3. First Hall obstruction

For the literal edge/orbit class containing `omega_0`, take
`A={omega_0}`.  Equations `(2.2)--(2.3)` give

```text
N(A)=empty,
mu^+(A)=w(omega_0)>0,
mu^-(N(A))=0.                                      (3.1)
```

The exact Hall inequality from `(4.1)` of `candidate.md` would require

```text
w(omega_0)<=0,                                     (3.2)
```

contradicting `(2.1)`.  XCRF therefore fails before a weight ratio, edge
norm, asymptotic estimate, or final-sign aggregate is consulted.  This is
the first analytic obstruction, so the optional `k=11,H_2` guard was neither
predeclared nor run.

## 4. Strongest surviving flow identity

For any partial source-local flow `F`, let

```text
r_c^+=M_c^+-sum_(c')F_(c,c'),
r_c^-=M_c^--sum_(c')F_(c',c).                       (4.1)
```

Then, before norms and separately in every literal edge/orbit class,

```text
M_c^+-M_c^-=div F(c)+r_c^+-r_c^-,                  (4.2)

sum_c(M_c^+-M_c^-)=sum_c(r_c^+-r_c^-).             (4.3)
```

The singleton Hall deficiency forces

```text
r_(1,1)^+ >= w(omega_0)                             (4.4)
```

inside its complete-label component.  Equation `(4.4)` refutes full XCRF
transport; it does **not** assert that other unmatched components cannot
cancel in the final edge coefficient.

The accepted token partition also remains exact:

```text
J=J_compatible+J_exceptional.                       (4.5)
```

M335's combined scalar reduction for `mass(Exc_pf^*)` remains valid, but its
H/A/C Borel scales remain unproved and would control only the exceptional
term.  They do not repair `(3.1)`.

## 5. Exact successor obligation

Any stronger cross-cell construction must change at least one premise of the
refuted candidate: either prove a new, explicitly declared source-geometric
relation that gives a complete-label supply node a genuine different-cell
reverse neighbor without consulting final signs, or add the no-reverse and
same-cell-switch locus to an explicit exception and prove the required
combined exceptional-mass scale.  Neither obligation is discharged here,
and no alternate grouping or surgery is proposed.

No MPCF, CMPAD, SOCL, gap, mixing, Terminal, or downstream conclusion
follows.
