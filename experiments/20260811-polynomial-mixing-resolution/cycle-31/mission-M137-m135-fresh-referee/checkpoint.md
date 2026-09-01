# M137 halfway checkpoint

Date: 2026-08-13 UTC.

Status: theorem audit and independent exact run complete; no material
objection found.

All six assigned immutable M135 digests match.  The fresh checker imports no
M135 or predecessor module/output.  It brute-enumerates `Z_3` and `Z_4`,
independently reconstructs the plus-mirror DPS image, and obtains equality of
the two targets with root-fiber sizes exactly `3` and `4`.

The exact checks reproduce:

- zero `H=Stab(d)` equivariance failures for every adjacent index at `d=3,4`;
- nonzero failures for full `S_d` equivariance, confirming that the root-
  stabilizer restriction is material;
- free global and root-stabilizer actions, with exactly `d` `H`-orbits in
  every global orbit;
- `d`-regular incidence multigraphs and `d` perfect-matching colors;
- at `d=3`, 80 conflict edges, a conflict triangle, zero conflicts within
  each of the three matching colors, and zero failures of the graph-versus-
  parity paired-subgroup dichotomy;
- signed action-image order `216`, maximum agreement `6`, and exact minimum
  schedule cover `5` for all three adjacent indices;
- at `d=4`, the nonconjugate `96 -> 288` witness, including literal equality
  with `(V_4 x V_4)Diag(S_4)` and the parity-diagonal subgroup, and
  `2880 < 4^6` for the singleton patch.

The universal proof also survives line-by-line audit: parity excludes the
Goursat full product; normal-subgroup classification leaves graph or parity
away from rank four; a graph automorphism must preserve transpositions and
is inner; the `S_6` outer automorphism is excluded because it exchanges the
two size-15 involution classes instead of preserving transpositions.  Hall's
argument and matching conflict-independence are correctly applied.

Provisional verdict: `ACCEPT`, zero material numbered objections.  The
simultaneous braid-realization/coset-refinement lemma remains unresolved, as
M135 states.
