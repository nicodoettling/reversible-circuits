# M261 checkpoint

Status: exact coefficient reduction proved; uniform estimate unresolved.

All required predecessor inventories pass. The sole mismatch is M256's
already-refereed nonmaterial transcription of the historical M166
freeze-manifest hash; `dependency_audit.md` records the correct value.

Before any finite diagnostic, `phase_difference_reduction.md` derived the
literal phase law

```text
z_k(y+1)-z_k(y)=Lambda_n/R_n
 [alpha_1 Xi_(1,y+1)+alpha_2 Xi_(2,y+1)],
```

where each `Xi` is M91's exact Abel coefficient law evaluated on a bounded
endpoint-incidence observable `E_ell`. Both channels, triangle/double kinds,
all cyclic phases, and the one-run/two-run jump endpoints remain inside the
single absolute value. The exact equivalence is

```text
FD-bound <=> sum_ell |alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)|=O(1/n).
```

This phase-boundary variation statement `(PBV)` is now the first standalone
unproved lemma. The accepted DE and Y-DV theorems cannot be applied directly:
their observables `X_D,Y_D` see only component size and one/two-run count,
while `E_ell` retains individual run endpoints, seam positions, literal
phase displacement, and owner-pair weights. Even hypothetical full DV for
`X_D,Y_D` would require a new observable-extension theorem before it could
control PBV.

The capped exact falsification suite reconstructs every adjacent frozen M161
score at `k=3,5,7`. Finite positivity is not promoted. The mission is ready
to freeze with PBV as the first standalone lemma.
