# M271 final report: fresh immutable referee of M269

Date: 2026-08-14 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT M269'S DECORATED CYCLIC-WIDTH TRANSDUCER
FOR STRICT INTERNAL CP-2 ROWS.

MATERIAL OBJECTIONS: NONE.
NONMATERIAL QUALIFICATIONS: TWO.
```

## Field 2 — target, convention, and strict scope

The ambient target remains the global fixed-length uniform law on
`Omega(N,m)` for the lazy exact same-product `{3,4,5}` block heat-bath
kernel.  This mission audits only deterministic DPS side-token closure, with
white rotation increasing, black rotation decreasing, and a local row

```text
W_u^q S^e B_b^q -> S,       e in {1,3},
```

recording `x_b` only when `e=3`.  It makes no direct Markov-chain claim.

## Field 3 — immutable provenance

Every M269 payload verifies.  Its frozen inventory digest is

```text
c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb.
```

Every named M250/M254, M257/M260, and M262/M265 inventory also verifies at
the hashes in `checkpoint.md` and `proof_audit.md`.  The accepted boundary is
unchanged: metric pruning and raw CP contexts are inputs; neither the old
refuted CPR transition nor M269's theorem was imported as a premise.

## Field 4 — coordinates, lens, and child ports

Cutting at `q_0=R_v` puts every canonical nonroot slot at an even position
`t(h)`, with adjacent pair `(t(h)-1,t(h))`.  The literal child gadget is

```text
W_b^(L_h) S^(R_h) S^(L_h) W_h^(R_h) S_h^(*) S^(R_h).
```

Against either black arm, `R_h` closes first and `L_h` second, both at
distance three to that arm's black vertex.  Inverse chronology opens `L_h`
before `R_h`.  Replacing the corresponding white pairs below width `r`
gives exactly M269's decorated lens `F_v(r)`.

## Field 5 — initialization

At `a=p(v)!=1`, the CP-1 incidence is `L_v=q_(M-1)`.  Parent-prefix
deletion consumes the edited black arm above width `r`; parent-suffix
deletion consumes the current-parent black arm below it.  Consequently a
direct child of `v` persists exactly for `t(h)<r`; for `t(h)>r`, its
`R_h,L_h` rows close to `x_a`.  The special `L_v` row has three sides and
also records `x_a`.  Arbitrary siblings, including post-wrap siblings, use
the same exact two-row macro.  The residual is exactly `F_v(r)`.

## Field 6 — full strict-internal transition table

For a next strict parent `b!=1`, let `s=t(b)`.

```text
s<r:  F_v(r) -> F_v(s),
s>r:  F_v(r) -> C_b,
       C_a    -> C_b.
```

On contraction, `L_a` records `x_v`, `R_a` records `x_b`, ports below `s`
persist, and ports in `s<t(h)<r` discharge to `x_b`.  On expansion, the same
two special rows occur, every incoming port discharges to `x_b`, and `R_v`
records `x_b`; the residual is canonical `C_b`.  On sealed propagation,
`R_a,L_a` both record `x_b`.  Sibling blocks record the black endpoint of
the arm to which they are paired.  Every other row has distance one.

The complete-node deletion chronology reverses literally: each child macro
opens `L_h` then `R_h`; contraction opens the special `R_a` before `L_a`;
expansion opens special rows in reverse `R_v,R_a,L_a` order after undoing
later interval deletions.  No endpoint is changed by the reversal.

## Field 7 — direction insufficiency and boundaries

For every `rho>=9`, the two valid paths

```text
4 -> 5 -> 6 -> 1,       4 -> 7 -> 6 -> 1
```

give, respectively, expansion to `C_6` and contraction to `F_4(4)` from
incoming `O^+` states.  Likewise

```text
6 -> 2 -> 3 -> 1,       6 -> 4 -> 3 -> 1
```

give sealed and lens outputs from incoming `O^-` states.  Edge count,
connectivity, root leaf, parent maps, and strict-internal status hold for all
`rho>=9`; the argument is not finite interpolation.

No canonical gadget straddles `q_0`, `r`, or `s`: those three slots are the
edited slot, retained path slot, and current-parent slot.  Empty arms and
post-wrap intervals are therefore covered by the same induction.

## Field 8 — finite guard and numbered qualifications

The no-import clean-room checker uses rightmost complete-node deletion and
forces vertex names to agree with canonical slot positions.  It passes the
four M269 schemas at `rho=15` and the four witness rows at `rho=9`.  Its
normalized result digest is

```text
9b6514b809c63648ed350496e78580ddc88c632ad72a9c28fa2bd0b645ddf29e.
```

Python is 3.12.3; dependencies are empty; seed is null.  This is finite
calibration only.

1. **Material objections:** none.
2. **N-1, predecessor guard:** M269's own guard uses some decorative vertex
   names independently of normalized slot positions, so it is a symbolic
   token-schema guard rather than a full-tree instance, exactly as its scope
   suggests.  The proof is analytic, and the slot-consistent clean-room guard
   passes.
3. **N-2, domain wording:** “every canonical vertex” in M269 Section 2
   should read “every canonical nonroot slot.”  All theorem applications
   already have that domain.

## Field 9 — disposition and exact stop

Accept and promote M269 only as the exact decorated-lens theorem for
initialization and strict internal CP-2 rows.  The first unresolved step is
DL-RST: apply the literal rank-dependent CP-6 root contexts at `a=1`, include
the new child `d`, and perform final root completion on every possible
reversed-base, decorated-lens, or canonical input.

```text
DO NOT INFER:
  DL-RST; old CPR or RSPT; repaired RSMI+; IDL;
  routing or a routing-length bound; a gap; polynomial mixing;
  Terminal A or Terminal B.
```
