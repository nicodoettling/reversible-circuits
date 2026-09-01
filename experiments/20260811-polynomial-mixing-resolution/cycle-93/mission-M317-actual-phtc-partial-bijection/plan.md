# M317 Plan: Actual PHTC via Stabilizer Partial-Bijection Extension

Date: 2026-08-14 UTC.

## Scope

Fix `d>=6`, one adjacent edit index, one actual M135 perfect matching `M`,
nonzero weights `lambda>=0`, and the M312 anchored residual hierarchy in the
finite chart-stabilizer action.  Literal braid length remains a separate
SSTID obligation.

## Candidate fixed before computation

For a compatible pivot tuple `I` and witness `s_I`, put

```text
H_I=Stab_S((x_P)_(P in I)),
z_Q^I=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I:x_Q^h=z_Q^I}.
```

The residual family on `V=G_I(supp(lambda))` defines the partial assignment

```text
f_(I,V): x_P -> x_P       (P in I),
           x_Q -> z_Q^I   (Q in V).
```

**SPBE (stabilizer partial-bijection extension).**  There are universal
constants `B,C` such that every weighted actual matching admits a
positive-weight anchor and compatible `I`, `|I|<=d^B`, for which:

1. `lambda(V)>=||lambda||_1/d^C`;
2. every pair of residual constraints in `V` is jointly realizable in
   `H_I` (so the displayed assignment is equality-consistent and injective);
3. every pairwise-consistent partial assignment of this stated actual form
   extends to one element of `H_I`.

The intended exact consequence is that one `h in H_I` lies in every
`D_I(Q)`, `Q in V`, hence the node collapses and PHTC holds.

SPBE is predeclared before any computation.  The audit must distinguish the
heavy pairwise-consistent-cell extraction from the structural extension
step; neither may be silently imported from M135's conflict coloring.

## Obligations

1. Source-lock M135/M137, M296/M299, M301/M304, M306/M309, and M312/M315.
2. Translate residual signatures exactly into source-target partial maps.
3. Prove `SPBE => PHTC => WRAD` with the outer-anchor quantifier intact.
4. List equality/injectivity, base-pivot, pair-orbit, and higher-tuple-orbit
   obstructions.
5. Compare generic `Sym/Alt` partial-bijection extension with the actual
   finite chart stabilizer without identifying them.
6. If SPBE fails formally, freeze the first exact obstruction and the
   strongest strictly surviving reduction.

## Computation firewall

Analytic work comes first.  At most one selected `d=6` matching guard is
allowed after SPBE is fixed; no full universe or stabilizer census is
authorized.  No routing, voltage, congestion, spectral-gap, mixing, or
Terminal conclusion may be inferred.
