# M169 halfway checkpoint

Date: 2026-08-13 UTC.

- Verified every frozen `SHA256SUMS` list in M135/M137, M141/M143,
  M146/M148, M154/M158, and M163/M164. No predecessor file was modified.
- **PROVED:** in `R_d=(Z_d x [d])/S_d ~= Z_d/Stab(d)`, if a quotient-loop
  transporter is `rho`, then its monodromy on the `d` white-root lifts is
  `rho^(-1)`. Its sign is exactly transporter parity.
- **PROVED:** for tuples, `V_stab` is the relative sign image of simultaneous
  white-root monodromies. For fixed physical endpoints, the route coset
  contains zero exactly when one quotient braid induces root-fiber
  permutations that are either all orientation-preserving or all
  orientation-reversing.
- **PROVED:** equivalently, the fixed physical relative-orientation lifts lie
  in the same braid orbit in the regular `F_2^s/Delta` cover. This formulation
  retains M163's section/coboundary caveat.
- **PROVED for accepted `d>=5` M135 subfamilies:** their tuple monodromy group
  contains `P_(d,s)` via accepted M141/M154 and fits into
  `1 -> P_(d,s) -> K_mon -> V_stab -> 1`.
- A marked M135 `H`-root hit tests only `rho(d)=d`, not `sgn(rho)`. The actual
  zero-coset test must retain the orientation of all `d` root lifts.

## Freeze decision

The structural reduction is theorem-level and exact, but it does not decide
whether `V_stab` is full for all `d>=5` matching subfamilies. Per the mission
cap, no `d=5` Schreier or broad group closure was launched. Freeze the exact
orientation-cover theorem with full voltage unresolved. Polynomial word
length, common-braid realization, and every spectral statement remain
separate.
