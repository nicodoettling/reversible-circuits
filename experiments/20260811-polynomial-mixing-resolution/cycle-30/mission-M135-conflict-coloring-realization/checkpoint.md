# M135 halfway checkpoint

Status: decisive halfway theorem obtained; simultaneous realization remains
open.

The accepted frontier has been reconstructed.  M127/M130 prove that each
adjacent DPS label edit descends to a physical involution `tau_i`, while a
single global signed braid is impossible already at `d=3`.  M132/M134 prove
that every fixed-schedule agreement set is independent in the paired-subgroup
conflict graph, but `chi=3` versus true schedule-cover number `5` at `d=3`
shows that pairwise coloring alone does not imply simultaneous realization.
The tested `O(d^40)` two-label contour key is refuted at `d=4` and will not be
reused as a positive selector.

## New proved reduction

Let `G=S_d` act on `Z_d` by global conjugation and let
`H=Stab_G(d)`. Direct equivariance of the DPS closure proves that every
`tau_i` commutes with `H`, although it need not commute with all of `G`.
For `d=3` or `d>=5`, Goursat plus the normal-subgroup classification of
`S_d` shows that a coordinate-pair subgroup is either the graph of a global
conjugation (exactly when the two words are globally conjugate) or the full
parity-diagonal subgroup.

The `H`-orbits are therefore the right atoms. Make one edge for each
`H`-orbit, from its source `G`-orbit to the target `G`-orbit of its `tau_i`
image. Freeness of global conjugation gives exactly `d` `H`-orbits per
`G`-orbit; `H`-equivariance and bijectivity of `tau_i` make the incidence
multigraph `d`-regular on both sides. Repeated perfect matchings give a
`d`-edge-coloring. The union of the `H`-orbits in any one color is
conflict-independent. Thus the conflict-coloring half is **PROVED** with
`d` classes for `d=3` and every `d>=5`.

Rank four has the extra normal subgroup `V_4`; M132's `96 -> 288` witness
has neither source nor target pair globally conjugate, so the preceding
classification deliberately excludes it. The `2,880` singleton classes
give a uniform all-rank bound `q(d)<=d^6` (with the trivial `d=2` case).

## Exact calibration and remaining step

The independent script reconstructs all DPS coordinates at `d=3,4`, finds
zero `H`-equivariance failures, and reproduces regular incidence degrees
`3` and `4`. At `d=3` its three edge colors have eight physical states each
and zero paired conflicts. Complete action-image closure nevertheless gives
maximum one-schedule agreement six and minimum schedule cover five. Hence

```text
every orbit-incidence matching is one-schedule realizable: REFUTED at d=3.
```

The remaining obligation is now an exact quotient/coset problem: refine the
`d` matchings into polynomially many subsets whose corresponding braid-action
cosets have nonempty intersection, with a polynomial-length representative.
This is strictly the simultaneous-realization half; no paired conflict-color
bound remains open outside the finite rank-four exception.
