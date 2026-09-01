# Audit correction: exact scope of the rooted condition

The only proved conditional routing statement in this mission is the following
exact representative-selection criterion.

For a matching-selected `H`-orbit edge over a doubled-tree source `W`, call a
representative **zero-aligned at `i`** if

```text
[tau_i(W)]=[W],
```

and call it **one-step aligned at `i`** if

```text
[tau_i(W)]=R_i[W].
```

If every coordinate in an ordered selected subfamily is zero-aligned, the
empty synchronized braid reaches the matched target quotient tuple. If every
coordinate is one-step aligned, the synchronized braid `R_i` does. This is
immediate and exact.

The more geometric language in `proof.md` and `report.md` about a
pair-aligned black vertex or noninterleaving boundary sectors should be read
only as motivation for finding such representatives, not as an independently
proved all-`d` DPS-locality lemma. The bounded `d=3,4` checks are finite
falsification/convention evidence only. M135 does not guarantee that every
perfect-matching color selects zero-aligned or one-step-aligned edges.

Accordingly, the substantive outcome remains:

```text
EXACT FINITE: 14 positive d=5 width-two quotient-route certificates.
PROVED BUT FORMAL: the exact endpoint representative-selection criterion.
UNRESOLVED: every-color quotient routing and any nonformal all-d selection rule.
```

No bounded-search miss is a nonreachability result.
