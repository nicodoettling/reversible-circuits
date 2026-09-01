# Fresh immutable audit request for M284

Please audit frozen M284 independently and do not edit it.

## Required gates

1. Verify every M284 checksum and every cited M135/M137, M175/M176,
   M181/M183, M200/M202, M240/M242, M269/M271, M273/M275, and M278/M281
   checksum inventory.
2. Reconstruct the exact source ordering: `beta` acts on the old word,
   `j_d(beta)` maps the upper unedited padded source `U_T` to the old-edited
   padded state `N_T`, and only then does `c_(T,i)` map `N_T` to the
   new-edited target `A_T`.
3. Check that `j_d` is the standard injective braid embedding fixing the last
   two strands, that `j_d(beta);c` is chronological composition, and that
   right cancellation proves the displayed literal braid-set intersection.
4. Check the action-image qualification: identical upper actions may have
   different braid representatives, so the word-set identity is sufficient
   recursive construction rather than a classification or lower bound.
5. Verify that a correction `c` is common only within a class having the same
   literal word, and independently audit M240's permission to choose every
   optional absent-child scan sign negative.
6. Check the complete adjacent-index partition and the `<=2` alphabet at old
   rank `d=5`, ordinary endpoint `v=d-1`, internal-even endpoint, physical
   cross seam, and last new-child/root seam; also verify `|c|<=4d-7`.
7. Recompute the arbitrary-rank family `V_D` for symbolic `D>=6`: all factors
   transpositions, first-four product identity, later square cancellation,
   connected star support, and minimal length `2D-2`.
8. Verify from M278's canonical-slot lemma that every unedited chart source
   has consecutive equal pairs and that simultaneous global conjugation
   preserves this equality pattern, excluding the full global orbit of
   `V_D`.
9. Verify from M135 left-perfectness that every perfect-matching color, for
   every fixed adjacent index, contains exactly one `H`-edge over `[V_D]`.
10. Enforce the claim boundary: Proposition 7.1 refutes only
    chart/local-type-only coverage. It is not a lower bound on the number of
    schedule classes and does not resolve polynomial refinement. M181 remains
    conditional on quotient routing; M200 remains finite `d=5`; no
    voltage-length, congestion, gap, mixing, or Terminal conclusion follows.

The most important possible objections are a hidden source/target reversal in
the rank lift, an unlicensed passage from braid words to finite action images,
or an overstatement of the `V_D` obstruction. A clean-room symbolic check is
preferred; broad `Q_D` or product enumeration is neither needed nor allowed.

