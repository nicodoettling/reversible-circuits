# M291 Halfway Checkpoint

Status: halfway dependency audit and structural split complete.

- The exact chartless base-route interface and type firewall were fixed in
  `plan.md` before substantive inspection.
- All payloads in M135/M137, M175/M176, M181/M183, M200/M202,
  M240/M242, M269/M271, M273/M275, M278/M281, and M284/M288 pass their
  frozen SHA256SUMS.  The rooted-DPS count inputs M112/M119 also pass.
- The accepted Hurwitz diameter audit M13 supplies an explicit route from
  every `w in Z_d` to the fixed doubled-star chart `c_d` of length at most
  `50 d (2d-2)^3`.  Applying this independently at both endpoints of the
  actual H-orbit edge selected by an arbitrary M135 color gives a route of
  length at most `100 d (2d-2)^3` for each edge separately.
- With `BStab_d` the *literal braid stabilizer* of `c_d`, the exact braid
  fiber for a chosen source representative `w_Q` and its selected endpoint
  `tau_i(w_Q)` is

  ```text
  alpha_Q ; BStab_d ; delta_Q^{-1}.
  ```

  Thus a common literal braid schedule for a family is exactly a common
  element of these framed stabilizer translates.  At this fixed rank,
  projecting all fibers through the global braid-action quotient preserves
  common nonemptiness, but collapses distinct braid words and does not
  determine shortest braid length.  No cross-rank action embedding is used.
- A strict arbitrary-rank obstruction has been found for the named
  **common-prefix paired-chart cover**.  The broad paired-tree set has size
  `d^(d-2)(d-1)!`, whereas every physical M135 color has size
  `d^(d-4)(2d-2)!`.  Injectivity of every braid action forces at least

  ```text
  (2d-2)! / (d^2 (d-1)!) >= d^(d-3)
  ```

  common chart-canonicalizing prefix classes, even with unbounded prefix
  length.  This includes every valid doubled-tree extension chart and holds
  for the actual H-edge chosen over each global orbit by any fixed color.
- This counting result does **not** obstruct cancellation between the
  source and target frames through `BStab_d`; consequently it neither proves
  nor lower-bounds the true M135 polynomial common-schedule refinement.
- No predecessor or coordinator file has been edited.
