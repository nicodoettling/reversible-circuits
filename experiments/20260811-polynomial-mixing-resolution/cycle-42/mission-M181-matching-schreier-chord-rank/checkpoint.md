# M181 checkpoint

Status: substantive proof complete; report/freeze pending.

- Ownership boundary: only this M181 directory is being edited.
- The project skill, `HANDOFF.md`, `GOAL_SPEC.md`, the sampling and experiment
  references, and the relevant manuscript sections were read before proof
  work.
- All fourteen assigned frozen `SHA256SUMS` manifests passed: M135/M137,
  M141/M143, M146/M148, M154/M158, M163/M164, M169/M172, and M175/M176.
- Reconciliation: an M135 perfect-matching color contains one **H-orbit
  edge** over each left global `G`-orbit, not each physical word.  The proof
  below selects that unique edge and conjugates the explicit word by an
  arbitrary coordinatewise `G`-relabeler; braid equivariance preserves the
  literal loop and transporter sign.  No invalid `H`-relabeling is assumed.
- Proved a narrower actual-matching realization lemma.  For every `d>=5`,
  every perfect-matching color, and every
  `1<=s<=1+floor((d-1)/3)`, that color has an accepted width-`s` source
  subfamily with `V_stab=W_s` and Schreier chord rank `s-1`.
- The words have connected support on all `d` labels, product one, and exact
  minimal length `2d-2`.  Shifted copies of one anchored six-factor relation
  fix all shared filler factors and realize the basis classes
  `[e_1],...,[e_(s-1)]` modulo `Delta`.
- Fixed physical endpoint membership follows for this family **only if** the
  matched target quotient tuple is in the source synchronized component.  No
  general quotient route, arbitrary-subfamily rank theorem, word-length
  theorem, gap, mixing, or Terminal conclusion is claimed.
- The tempting edge-vector symmetry shortcut is invalid in general: M135
  supplies no coordinate action on a fixed ordered tuple; moreover, when
  `s` is even, connected-graph vectors `e_i+e_j` span only the codimension-one
  image `E/Delta` in `W_s`.  The constructed single-coordinate classes avoid
  this parity defect.
