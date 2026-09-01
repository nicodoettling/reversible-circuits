# M169 plan: point-stabilizer parity voltage at `d=5`

Date: 2026-08-13 UTC.

## Objective

Work in the accepted M135 matching subfamilies for `d>=5` and determine one
exact qualitative datum left open by M163/M164: the image `V_stab` of the
point-stabilizer parity-voltage map, or, if the full image is not derivable,
the exact source-to-target zero-coset condition.  The first required step is a
proof of the rooted-cover interpretation: for a stabilizer braid, its parity
voltage equals the sign of its monodromy on the `d` white-root lifts.

## Target and conventions

The auxiliary target is uniform on the minimal connected identity sector

```text
Z_d={(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed tuple factors multiply
left-to-right.  Signed right-Hurwitz generators are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

Physical words and their `d` rooted DPS lifts are kept fixed.  Any voltage
coordinate is defined relative to an explicit section; changing the section
changes edge labels by a coboundary and must not be treated as an invariant
literal vector.

## Work program

1. Verify all frozen hashes and read accepted M135/M137, M141/M143,
   M146/M148, M154/M158, and M163/M164 artifacts in full.
2. Reconstruct M163's quotient graph, section, stabilizer, and voltage map
   without modifying predecessor files.
3. Prove the rooted-cover/monodromy lemma directly from equivariance of the
   Hurwitz action and the fixed physical-root covering.
4. Seek a structural description of the braid point stabilizer and its
   induced action on the root fiber.  Determine `V_stab` or the invariant
   zero-coset membership criterion for each accepted matching edge.
5. Only if it distinguishes the remaining alternatives, run a deterministic,
   tightly capped `d=5`, matching width at most `3` exact audit.  Do not run an
   unbounded Schreier closure.
6. Record a halfway checkpoint, proof/falsifier, compact machine-readable
   output if computation is used, report, hashes, freeze manifest, and final
   repository hygiene.

## Falsifiable alternatives

- `V_stab` is the full even-weight subspace allowed by M163's parity law.
- `V_stab` is a proper structurally described subspace (for example the image
  of root-monodromy signs under the matching incidence map).
- Literal section-dependent voltage vectors vary, but the source-to-target
  coset class has a section-independent zero-membership criterion.
- The proposed parity-only criterion is false, witnessed already at `d=5`
  and width at most `3`.

## Scope boundary

Even a full-voltage or zero-coset theorem is qualitative only.  It supplies
neither a polynomial signed-braid word-length bound nor a common-braid theorem
for arbitrary matching families.  It implies no UST comparison, physical
sector gap, original lazy exact `{3,4,5}` heat-bath gap, or Terminal outcome.

## Reproducibility

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Any exact computation will use Python 3, deterministic ordering, `seed=null`,
and no nonstandard dependency unless recorded otherwise.
