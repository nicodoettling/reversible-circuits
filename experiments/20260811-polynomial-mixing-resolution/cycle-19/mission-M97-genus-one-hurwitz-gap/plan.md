# M97 plan: genus-one connected Hurwitz gap

## Objective

For fixed labels `[d]`, let `X_d` be the connected identity transposition
words of exact length `2d`.  The declared target is `Unif(X_d)`, and the
declared auxiliary kernel is the half-lazy signed adjacent Hurwitz walk

```text
P_d=(1/2)I+[1/(4(2d-1))]
             sum_(i=1)^(2d-1)(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),  R_i^(-1)(a,b)=(aba,a).
```

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  The primary target is an inverse-polynomial lower bound on
`gap(P_d)`.  The strictly weaker accepted target is a polynomial worst-source
hitting time to the connected-deletable adjacent-square set.

## Attack

1. Define the prefix genus defect from prefix cycle count and prefix support
   components.  Prove that every state has a unique handle-creation time and
   that one Hurwitz move moves this time by at most one.
2. Cut at the handle time.  Test, then prove or refute, that both sides are
   componentwise minimal (genus zero).  If true, formulate an exact
   restriction/projection decomposition; if false, retain the smallest exact
   obstruction.
3. Audit a chronological-torus/tree--cotree or polygonal-side-matching
   comparison only after specifying its exact lifted state law and literal
   simulated moves.  Do not infer expansion from marked incidence alone.
4. Use finite `d=2,3,4` enumeration only to falsify structural claims and
   calibrate boundary cases.  No finite spectrum will be promoted to an
   asymptotic gap statement.

## Expected failure modes

- the seam suffix retains positive genus, defeating a two-genus-zero product;
- the handle-time partition is not a strong lump and has state-dependent
  crossing rates;
- a tree--cotree contraction erases the growing state entropy or has
  nonuniform/state-dependent lift multiplicities;
- a comparison silently routes through a canonical hub;
- an external fixed-genus map chain has the wrong stationary law or moves.

## Deliverables

`checkpoint.md`, a proof/obstruction note, any deterministic falsification
script plus machine-readable output, and a nine-field `report.md`.  All
claims will be labeled proved, conditional, empirical, refuted, or unresolved.
