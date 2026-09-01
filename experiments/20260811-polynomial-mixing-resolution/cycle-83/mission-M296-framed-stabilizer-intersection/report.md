# M296 final report: framed-stabilizer common intersection

Date: 2026-08-14 UTC.

## 1. Verdict

```text
FINAL VERDICT: PROMOTE THE EXACT CHART-STABILIZER TRANSPORTER REDUCTION.
               KEEP THE POLYNOMIAL COVER UNRESOLVED.
```

M296 does not prove the requested `d^O(1)` common-schedule cover. It does
strictly sharpen the first open interface: after fixing one selected edge,
the whole problem becomes a simultaneous transporter problem inside the
literal doubled-star point stabilizer. Pairwise compatibility is an exact
double-coset equality, and every nonempty constraint is a coset of an
explicit two-point stabilizer.

## 2. Exact theorem

Let `S=BStab_d` fix

```text
c_d=(1,2)^2(1,3)^2...(1,d)^2.
```

For matching-selected edge `Q`, use M291's short frames
`u_Q^alpha_Q=c_d`, `v_Q^delta_Q=c_d`. Fix `Q_0` and put

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q,
x_Q=c_d^(L_Q),
y_Q=c_d^(R_Q^(-1)).
```

Then

```text
C_Q={s in S:L_Q;s;R_Q in S}=Trans_S(x_Q,y_Q),

intersection_Q
 (alpha_Q;S;delta_Q^(-1))
 =alpha_0;(intersection_Q C_Q);delta_0^(-1).          (2.1)
```

Thus a whole family has one schedule exactly when one chart-stabilizer
element simultaneously maps every relative source point to its relative
target point.

For each individual `Q`, exact pairwise compatibility is

```text
C_Q != empty
iff S;L_Q;S=S;R_Q^(-1);S.                            (2.2)
```

If `s_Q in C_Q`, then

```text
C_Q=s_Q;(S intersect R_Q;S;R_Q^(-1)),                (2.3)
```

where the subgroup is the stabilizer in `S` of `y_Q`. Hence the
higher-arity problem is an intersection of cosets of varying two-point
stabilizers, not a one-sided common chart prefix.

Frame changes apply one common two-sided translate to all `C_Q`; all
nonemptiness predicates are intrinsic. Projection to the finite action
preserves common nonemptiness exactly but not representative length. With
M291's `L_d=50d(2d-2)^3` frames, the common braid `beta` and residual
stabilizer element `s` obey

```text
|beta|<=2L_d+|s|,       |s|<=2L_d+|beta|.             (2.4)
```

Polynomial literal length is therefore equivalent on the two sides.

## 3. Actual doubled-star stabilizer structure

Writing `c_d=e_1^2...e_(d-1)^2`, `e_r=(1,r+1)`, the following are proved
literal stabilizer elements:

```text
R_(2r-1),            1<=r<=d-1,
R_(2r)^3,            1<=r<d-1.
```

The four-letter braid

```text
q_r=R_(2r);R_(2r-1);R_(2r+1);R_(2r)
```

exchanges adjacent square blocks, so `q_r^2 in S` with length eight.
Importantly, `q_r` itself sends the chart only to a global relabeling and is
not in the literal chart stabilizer. This is the exact global-orbit/literal
type distinction required by the mission.

There is also a complete Reidemeister--Schreier generating inventory. Choose
one M13 route `t_x:c_d->x` for every `x in Z_d`. The loops

```text
t_x;R_j^(+/-1);t_(x^R_j^(+/-1))^(-1)
```

generate all of `S`, each with length at most
`100d(2d-2)^3+1`. The inventory has at most

```text
2(2d-3)d^(d-3)(2d-2)!
```

rows. Its individual words are short, but its cardinality is enormous; it
does not imply a polynomial stabilizer orbit diameter or cover.

## 4. First remaining lemma

The first complete obligation is **SSTID**: cover every arbitrary M135
matching color by `d^O(1)` subfamilies such that, relative to one edge in
each subfamily, the higher-arity intersection

```text
intersection_Q C_Q
```

is nonempty and contains an `S` element of length `d^O(1)`. By (2.1) and
(2.4), this is necessary and sufficient for the true framed-stabilizer
common-schedule cover with polynomial representative diameter.

The pairwise double-coset graph from (2.2) is an exact necessary diagnostic
inside SSTID. M135's generated-subgroup conflict coloring does not settle
that sharper graph, and pairwise compatibility alone is not promoted to a
higher-arity intersection because the stabilizer subgroups vary. SSTID is
an exact fixed-rank finite-action transporter/coset problem plus a separate
literal length bound, retaining the actual `H`-edge selected by the matching
color.

## 5. Dependencies and audit

All 60 frozen payload rows in M112/M119, M135/M137, M284/M288, and
M291/M294 pass; M13's observed proof hashes reproduce. Full provenance is in
`dependency_audit.md`.

No compact finite guard was run: all new statements are exact group-action
identities. No predecessor, coordinator, manuscript, skill, or
source-of-truth file was edited.

## 6. Numbered qualifications

1. The short local loops are not claimed to generate all of `S`; the
   complete Schreier inventory is separate and exponentially indexed.
2. Polynomial length of each Schreier generator does not bound the length of
   a transporter assembled from them.
3. The exact pairwise double-coset condition is stronger than M135 conflict
   independence and remains unresolved uniformly on matching families.
4. Pairwise compatibility is not sufficient here without an actual theorem;
   SSTID retains the higher-arity intersection and short-representative
   diameter in one obligation.
5. No common-prefix paired-chart cover is revived, and no every-color
   synchronization, voltage, congestion, gap, mixing, or Terminal statement
   follows.

Material objections to the proved reductions at their stated scope: none
found. Fresh immutable audit requested.
