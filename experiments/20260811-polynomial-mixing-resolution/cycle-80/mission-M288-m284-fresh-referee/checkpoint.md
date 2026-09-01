# M288 Halfway Checkpoint

Status: substantive audit past halfway; verdict not yet frozen.

## Immutable gate

- M284's `SHA256SUMS` digest independently recomputes to
  `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3`.
- Every one of M284's six inventoried payload files passes.
- Every payload in all sixteen cited M135/M137, M175/M176, M181/M183,
  M200/M202, M240/M242, M269/M271, M273/M275, and M278/M281 inventories
  passes. Their top digests agree exactly with M284's checkpoint.
- The corresponding coordinator ledger dispositions were inspected. M284
  imports no statement outside their accepted scopes.

## Independent derivation reached

- The lower action fiber, lower braid preimage, upper correction word, and
  upper action fiber have distinct types. The correction begins at the
  old-edited padded state, so it cannot replace the lower same-rank action.
- Adding two inert strands makes `j_d(beta)` act only on the lower prefix.
  It maps `U_T=u_T k_d^2` to `N_T=u'_T k_d^2`; the accepted correction then
  maps `N_T` to `A_T`.
- Translation by one common terminal braid element is injective. Together
  with injectivity of the standard braid inclusion this gives the exact
  common-`c` word-fiber intersection. This says nothing converse-like about
  intersections after quotienting to finite action images.
- The local indices partition into ordinary odds, internal evens, the cross
  seam, and the last seam. Choosing all optional nonchild scan signs
  negative is licensed by M240/M242 after the accepted M273/M275 composition;
  the resulting alphabet is at most two and the displayed maximum increment
  is `4d-7`, including `d=5` and `v=d-1`.
- For `V_D`, the first four factors multiply to identity, later factors are
  squares, every star edge survives, and the length is `2D-2`. Its first
  canonical pair is unequal. Simultaneous conjugation preserves coordinate
  equality, excluding the whole global orbit from unedited extension charts.
  M135 left-perfectness then puts exactly one chartless `H`-edge over this
  left orbit in every matching color.

## Remaining work

Run the compact no-import convention guard, freeze the exact action-image and
true-refinement scope, record any numbered objections, and hash M288. No
predecessor or coordinator file has been edited.
