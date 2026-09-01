# M306 Plan: MRAD Agreement-Hypergraph Continuation

Date: 2026-08-14 UTC

## Objective and scope

Work only with actual M135 perfect matchings and the finite action fibers

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)}.
```

The target is MRAD for `d>=6`: every nonempty residual subfamily `U` should
contain an agreement hyperedge of inverse-polynomial relative size.  The
ambient sampler target remains the uniform fixed-length identity bridge for
the lazy exact `{3,4,5}` heat-bath chain, but this mission proves no chain
estimate.

## Candidate fixed before computation

The single analytic candidate is the **residual conditional-overlap moment**
`(RCOM)`.  Under transitivity, all point fibers have size
`k_d=|A_d|/|Z_d|`.  For nonempty `U subset M`, seek an anchor `P in U` with

```text
(1/k_d) sum_(Q in U)|K_P intersect K_Q| >= |U|/d^C.  (RCOM)
```

Averaging `|E_a(M) intersect U|` over uniform `a in K_P` would then yield
one action agreeing with at least this many edges.  This route uses pairwise
intersection *masses* only as a conditional expectation; it never invokes a
2-Helly implication.  In particular, it must remain valid as a formulation
in the presence of M301/M304's `d=3` triple `[0,2,9]`, whose pair
intersections are nonempty but whose triple intersection is empty.

## Work plan

1. Verify the accepted M301/M304 and M296/M299 source locks.
2. Derive the exact conditional-moment and second-moment identities, with
   all actual edges retained.
3. Determine whether accepted multisource subgroup/class invariants can
   force `(RCOM)`, or isolate the first exact missing weighted-orbit input.
4. Relate any surviving finite-action criterion to the M301 action-cover
   theorem and MRAD, without claiming literal length.
5. Only after the analytic result, use at most one compact finite diagnostic
   for boundary falsification.
6. Freeze a proved result or strict obstruction for fresh audit.

## Firewall

Even a proof of MRAD would leave polynomial literal braid representatives
open.  No full SSTID, every-color route, voltage, congestion, gap, mixing, or
Terminal inference is authorized.

