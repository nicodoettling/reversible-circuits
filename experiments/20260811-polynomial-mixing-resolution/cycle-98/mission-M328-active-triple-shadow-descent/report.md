# M328 report — source-local edge charge stops at arbitrary weights

Date: 2026-08-14 UTC

Verdict: **OBSTRUCTION-PROGRESS.** The fixed MIDEC charging mechanism is formally obstructed. Actual `d>=6` AATSD is **unresolved**.

## Outcome

The exact locked recursion is

```text
W'=c_I(P),
Phi'=T_I(P),
rho'=2T_I(P)/c_I(P)^2,
```

with active pivots and the whole child `G_(I union {P})(U)`. M328 predeclared MIDEC before computation: a fractional transport of normalized child-edge demand to normalized parent-edge capacity, supported on literal alternating cycles of the M135 orbit-incidence multigraph. An unused-capacity reserve equal to `rho-rho'` was required to pay both logarithmic weight loss and the AATSD absolute decrement. Thus MIDEC would imply AATSD without replacing the child by an induced graph.

MIDEC cannot be supplied by unweighted M135 incidence data for arbitrary weights. If pivoting at `P` genuinely regenerates a child edge `{Q,R}`, its demand contains `lambda_Q lambda_R`. Every parent edge deleted by `P` contains at least one vertex outside `C_I(P)`. Scaling all outside weights by `epsilon` leaves the regenerated demand nonzero while every deleted-edge capacity vanishes. Literal off-matching rungs have no weight and bounded incidence congestion cannot change this coordinate mismatch.

The obstruction survives even after dropping the alternating-cycle support restriction, so it is not an artifact of cycle length or a missing expansion estimate. It is a quantifier obstruction to any weight-independent source-local transfer from regenerated pairs to deleted parent edges.

## What is and is not proved

| claim | status | evidence |
|---|---|---|
| exact child `W,Phi,rho` laws | proved, locked input | M324/M327 and direct algebra in the fixed note |
| MIDEC implies AATSD | proved conditionally | normalized demand/capacity sums give `rho'` and `rho` exactly |
| M135 incidence alone yields MIDEC for arbitrary weights | obstructed | independent-coordinate `epsilon` scaling |
| actual `d>=6` MIDEC | unresolved | no all-rank actual pivot-avoidance theorem |
| actual `d>=6` AATSD | unresolved | MIDEC failure does not rule out a weight-dependent choice of nonregenerative pivot |
| RATSD and low-density terminality | unresolved | strictly weaker next interface |

The authenticated `d=3` star/triple is used only as a boundary realization of the scaling pattern. No rank lift and no `d>=6` counterexample is claimed.

## Strictly weaker next interface

Relative active triple-shadow descent asks for a selected active pivot satisfying

```text
log(W/W') <= C log(d)(rho-rho'),
rho-rho' >= d^(-B) rho
```

when the child is nonterminal. This respects arbitrary rescaling of low-mass conflicts. It would still need a separate actual theorem that sufficiently low density admits an edgeless child; without that terminality input, relative descent alone does not give a polynomial number of pivots for arbitrary real weights.

The first useful actual-specific theorem is therefore not an unweighted edge charge. It must prove either weight-dependent avoidance of every regenerated heavy pair or low-density active terminality from the higher diagonal-orbit structure of the chart stabilizer.

## Scope firewall

No computation or `d=6` census was performed. No conflict-independence, pair-moment, transitivity, induced-child, or polynomial-support inference was used. No HPRN, APOH, WRAD, literal representative length, routing, voltage, congestion, spectral gap, mixing, or Terminal claim follows.

Fresh audit is required before integrating the obstruction or the repaired interface.
