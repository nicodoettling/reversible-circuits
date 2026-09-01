# M150 checkpoint

Date: 2026-08-13 UTC.

## Reconciled starting state

The frozen accepted M135/M137, M141/M143, and M146/M148 reports were read.
They leave simultaneous action-coset intersection unresolved after closing,
for `d>=5`, literal generated subgroup and aligned factor-class multiset as
possible refinements.

## Final theorem checkpoint

The reduced class-lift construction and its signed-Hurwitz invariance are
proved from the explicit real Clifford/Pin extension. In the full
`P_(d,s)`, an all-even centralizer tuple localized at coordinate `q` has
coordinate `t_q v_q`, for `v_q` disjoint from `t_q`. Its lift commutator is
exactly `z_q`. Hence every coordinate kernel generator is killed and the
reduced invariant is trivial for all `d>=4,s>=1`.

At `d=3`, the Pin extension splits: the two simple root lifts satisfy the
literal `S_3` Coxeter relations. The coordinatewise split section makes every
product-one lifting value identity. Exact audit results:

```text
d=3: all 24 connected minimal words have sign +1;
     all 9 accepted matchings and all 135 nonempty subfamilies have equal
     source/target residual vectors.
d=5: all 1,110 transposition tuples through width 3 and all 3,210 localized
     coordinate witnesses pass; one DPS representative and all 7 edits pass
     identity, connectedness, and unique reduced value.
```

Final candidate verdict: **KEEP NEGATIVE**. The natural reduced Pin/Schur
lifting invariant is automatically passed and supplies no matching refinement.

## Scope guard

Even a constant lifting invariant proves only that this necessary obstruction
is absent. It does not imply a common signed braid, a polynomial braid word,
or any mixing result.

This closes only the natural reduced Pin descriptor. It does not classify all
central extensions or Nielsen invariants. The mission is ready for a fresh
independent referee.
