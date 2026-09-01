# M271 checkpoint

Date: 2026-08-14

Status: substantive audit complete; final verdict **ACCEPT** with no material
objection and two nonmaterial qualifications.

The project source of truth, `GOAL_SPEC.md`, the reversible-circuit-sampler
skill, its sampling-problem reference, and the experiment standard were read
before the frozen mission was audited.  The following immutable gate has now
been completed.

## Immutable source lock

Every payload in each named inventory verifies.  The independently computed
SHA-256 digests of the inventory files are

```text
M269  c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
M262  eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a
M265  ced42bf8a6ccd7ca9ffffdca94919c366273b712875cfe08eeead393b88193f8
```

The accepted dependency boundary is unchanged: M250/M254 supply metric
canonical pruning and complete-node commutation; M257/M260 supply only raw
CP-1--CP-6; M262/M265 refute the old one-bit CPR transition.  None supplies
the M269 theorem under audit.

## Substantive local audit checkpoint

With `q_0=R_v`, every canonical slot `h!=v` has even coordinate
`t(h)` and occupies the adjacent pair `(t(h)-1,t(h))`.  Thus a canonical
gadget can straddle a cut only at `t=0`, `t=r`, or `t=s`; these are,
respectively, the edited slot, retained path slot, and current-parent slot,
not canonical sibling/direct-child gadgets.

The literal child block is independently recovered as

```text
W_b^(L_h) S^(R_h) S^(L_h) W_h^(R_h) S_h^(*) S^(R_h).
```

Against either black arm `B_x^(R_h) B_x^(L_h)`, its legal deletion chronology
is `R_h` first and `L_h` second; both rows have exactly three intervening
sides and record `x`.  The inverse chronology is therefore forced in the
opposite order: reopen the `L_h` closure before the nested `R_h` closure.
This verifies the port macro independently of M269's guard.

For initialization, parent-prefix deletion consumes the edited black arm
above width `r`, while the parent suffix has already consumed the
current-parent black tokens below `r`.  Hence a direct child of `v` persists
exactly when `t(h)<r`; for `t(h)>r` its `R_h,L_h` rows delete in that order
against `x_a`.  In a contraction `s<r`, ports below `s` remain and those in
`s<t(h)<r` delete against `x_b`.  In an expansion `s>r`, every incoming port
deletes against `x_b`.

## Final checkpoint

The complete analytic audit confirms

```text
initialization:  reversed CP-5 in CP-2 -> F_v(r),
s<r:             F_v(r) -> F_v(s),
s>r:             F_v(r) -> C_b,
sealed:          C_a -> C_b.
```

The special distance-three endpoints are `L_v -> x_a` at initialization;
`(L_a,R_a)->(x_v,x_b)` on contraction; and
`(L_a,R_a,R_v)->(x_v,x_b,x_b)` on expansion.  Every discharged direct port
closes `R_h` then `L_h` to `x_b` (to `x_a` during initialization), and every
inverse macro opens `L_h` then `R_h`.  Sibling blocks record the endpoint of
their paired black arm.  The exact residuals, post-wrap cases, empty arms,
and global inverse chronology all check.

The arbitrary-rank `O^+` and `O^-` pairs are valid trees and give different
sealed/lens outputs at the same directional tag.  The clean-room finite guard
passes the four declared schemas and four rank-nine witness rows; normalized
digest:

```text
9b6514b809c63648ed350496e78580ddc88c632ad72a9c28fa2bd0b645ddf29e.
```

Two nonmaterial qualifications are recorded in `proof_audit.md`: M269's own
guard is a schematic token guard rather than a slot-consistent full tree, and
“canonical vertex” should read “canonical nonroot slot.”  Neither affects the
analytic theorem.  The exact stop is before `a=1`; DL-RST, RSPT, IDL,
routing, length, gap, mixing, and both Terminals remain unresolved.
