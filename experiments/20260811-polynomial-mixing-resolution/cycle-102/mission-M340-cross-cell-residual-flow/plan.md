# M340 plan — cross-cell residual flow

Date: 2026-08-14 UTC

## Objective

Continue the accepted M335/M336 source-local lane. Replace the refuted
same-cell endpoint swap by one explicitly source-local rational transport
between different supported quantile cells, while respecting the canonical
residual signs and every complete raw label. Prove the resulting XCRF
candidate or freeze its first exact obstruction.

## Declared signed measure

The object is M313/M319's exact fully combined profile-edge token measure,
with corrected `c_X`, literal zero slots, both channels, all `T/S/N` kinds,
phases, seams, incidences, raw lifts, representation factors, and quantile
cell masses retained before any norm. A positive token in cell `(s,t)` has
profile orientation `P->Q` only when

```text
a_(s,t)(P)>0,       b_(s,t)(Q)>0.
```

A reverse token must therefore be a genuine `Q->P` residual token in a
supported, possibly different cell `(s',t')`; it is never created by merely
swapping endpoints inside the same cell.

## Candidate schema to freeze before computation

After authentication and exact reconstruction, freeze XCRF as a rational
bipartite flow for each unordered literal profile edge and complete
source-geometric label class:

1. supply nodes are nonexceptional `P->Q` raw residual tokens;
2. demand nodes are nonexceptional `Q->P` raw residual tokens in supported
   cells `(s',t') != (s,t)`;
3. an arc is allowed only by the existing product/prefix-preserving raw source
   switch and a fixed source-geometric relation, never by final edge signs or
   arbitrary mass matching;
4. row and column balances use exact token weights, including cell `pi`,
   residual masses, raw conditional weights, and `c_X`;
5. all zero slots and complete channel/kind/phase/seam/incidence fields remain
   inside the same transport problem.

The explicit exception, transport relation, exact cell marginals, Hall
conditions, and divergence equations will be frozen in `candidate.md` before
any guard.

## Analytic route

1. SHA-lock M305/M310, M313/M316, M319/M321,
   M323/M326/M329/M330/M333, M335/M336, and the complete raw-profile input
   chain.
2. Import the accepted M335 same-cell obstruction and M336 audit boundary.
3. Define the raw-switch cross-cell bipartite graph without consulting final
   orientation surpluses.
4. Derive exact necessary and sufficient rational-flow/Hall conditions and
   their cell-level marginal/divergence consequences.
5. Test those conditions analytically. Only if one fixed finite clause remains
   undecided may a sole `k=11,H_2` guard be predeclared after the formulas are
   frozen.

## Firewalls

- No same-cell endpoint swap.
- No arbitrary final-sign interval pairing or globally ordered mass match.
- No scalar path length and no separate channel/type/cell/orientation bound.
- No alternate grouping, second rank, or broad search.
- No MPCF, CMPAD, SOCL, spectral-gap, mixing, or Terminal inference.

## Deliverable

Freeze an exact proof or first obstruction, the strongest surviving
cell-flow identity, reproducible artifacts if a guard is needed, and a request
for genuinely fresh immutable audit.

