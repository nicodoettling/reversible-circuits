# M319 plan: global profile-edge Borel pairing

Date: 2026-08-14 UTC
Role: author

## Scope

Work only from accepted M313/M316 on the auxiliary marked-profile flux.  For
each H/A/C row, use the corrected

```text
J(P,Q)=c_X sum_(s,t) pi_(s,t)
        [kappa_(s,t)(P,Q)-kappa_(s,t)(Q,P)],
c_X=r_X(alpha_1+alpha_2).
```

The edge table is expanded only after both Abel sums, both channels, every
T/S/N kind, phase, seam, owner incidence, raw lift, and zero slot have been
combined.  No constituent norm is permitted.

## Single predeclared candidate PEBP

For an unordered profile edge `e={P,Q}`, fix the lexicographic orientation
`P<Q`.  Expand the already-combined residual-product couplings and their
literal proportional raw lifts into finite weighted edge-preimage tokens.
A token has positive weight and orientation `+` for `P->Q`, `-` for `Q->P`.
Concatenate all positive tokens and all negative tokens separately in the
same fixed lexicographic order on the complete labels

```text
(s,t, raw source state, positive representation, owner slot(s), profile pair).
```

Atom-split the resulting weighted intervals as necessary.  Pair equal mass
coordinates from the two orientation intervals and let `Theta_e` exchange
the paired pieces.  It is a literal weight-preserving involution, preserves
the unordered profile edge, and reverses orientation.  The unpaired terminal
interval is denoted `Boundary_e`.

> **Profile-Edge Borel Pairing (PEBP), frozen candidate.**  For every odd
> `k>=3`, after the complete combination above, the canonical involutions
> `Theta_e` have total unpaired boundary mass
>
> ```text
> sum_e mass(Boundary^H_d_e)       <= C d b_d/k,
> sum_e mass(Boundary^A_d_e)       <= C d b_d/k,
> sum_e mass(Boundary^C_(d,e)_e)   <= C max(d,e)b_d b_e/k,
> ```
>
> for one absolute `C`.

This is the only pairing candidate.  Its qualitative involution and exact
coboundary identity will be proved first; the quantitative boundary estimate
must then be shown to be a genuinely narrower statement, not a relabeling of
MPCF.

## Work order and decision rule

1. Source-lock M91, M276/M279, M297/M302, M305/M310, M313/M316.
2. Prove the exact token expansion, involution, and edge-boundary identity.
3. Attempt an all-rank Borel-scale estimate using literal owner structure,
   never scalar path length or constituent bounds.
4. Only if the fixed candidate leaves a falsifiable finite structural claim,
   run at most one exact `k=15,H_2` guard.  Do not run a guard that can only
   produce an arbitrary finite constant.
5. Freeze either a proof or the first exact obstruction plus the strongest
   surviving coefficient identity, then request fresh immutable audit.

## Firewalls

No alternative pairing, rank, row, coupling, residual-mass bound, separate
quantile-cell/channel/type/orientation norm, or scalar path-length estimate.
No MPCF, CMPAD, C/BPV, SOCL, routing, voltage, congestion, gap, mixing, or
Terminal inference absent an all-rank proof.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
