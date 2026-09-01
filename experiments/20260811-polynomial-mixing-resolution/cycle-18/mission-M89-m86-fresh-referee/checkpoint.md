# M89 halfway checkpoint

Date: 2026-08-12.  Audited commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen provenance

The requested digests match exactly, and `sha256sum -c` accepts all ten M86
payload entries.  No frozen M86 source was edited.  The only transient M86
artifact created by importing its probe was `__pycache__`; that exact cache
directory has been removed.

## Provisional mathematical decision

The provisional decision is **ACCEPT with zero material objections**.  The
positive theorem is correctly restricted to the relabel/phase/interleaving
class, and the signed-distance statement is only a signed-Hurwitz lower bound.

The checks completed so far are:

1. `W_L` and `C_d` meet accepted M13 Classification-H: both are connected
   identity words on the same `d` labels with length `k`.  Two accepted
   `25 d k^3` normalizer paths give the safe `50 d k^3` pair path.  Once the
   index/sign sequence is computed on the two public templates, applying it
   is a fixed nonadaptive bijection.
2. A fixed positional signed generator commutes with simultaneous label
   conjugation, so the stored braid sends every `sigma W_L` to `sigma C_d`
   without requiring the normalizer itself to be equivariant.
3. With the stated convention, `rho_k=R_0...R_(k-2)` is cyclic left shift on
   identity words.  The two-stage stable sort has exact length
   `2k+1-a-b`, preserves genus-factor order, has uniform mean `k`, and leaves
   `e,e` last.  Therefore the family has exactly
   `P_L=k*binom(k+2,2)`, row hit at least `1/P_L`, the stated mean length,
   and the separately stated maximum length.
4. At `N=d+2,m=k+2=2N-2`, the endpoint has a genus-one connected-deletable
   square and a disjoint minimal component.  M75 gives
   `p_H=1/[6(m-2)M^2]`; its exact terminal fiber is
   `D_N=(3N^2+N-12)/2<=M^2`.  Applying endpoint charging only to
   `S subseteq X_(L,Gamma)` is valid: any wrong-index first exit from `S`
   is already a boundary edge, while all Hurwitz words remain bijections of
   the full macro.  The report explicitly does not extend this to a partial
   macro dominated by sources outside `X_(L,Gamma)`.
5. For each indexed word and prefix time, an actual directed edge source and
   the inverse prefix recover at most one starting source.  Averaging over
   indices gives path load at most `Dbar_L`, not `P_L Dbar_L`; endpoint load
   is at most one.  Thus the denominator `P_L*max(Dbar_L,1)` is correct.
6. Lemma 7.1's local count is an occurrence-strand count, not recursive
   substitution of the current transposition word.  A signed generator not
   meeting a marked strand carries the annulus unchanged; if one or both
   marked strands participate, only the sole conjugated occurrence changes,
   and its two endpoint tracks add at most two traversals of the other braid
   strand.  Continuing the inverse pullback carries that whole strand to its
   one original occurrence.  Hence at most `2q+2` original-band traversals
   occur.  Safety gives a nonseparating embedded curve; M84/M85's torus-cover
   injection gives a nonzero voltage in `L Z^2`; therefore
   `q >= (L-2)/2`.  This says nothing about unrestricted `H4/H5` distance.

## Independent falsification checks

- The exact M86 family audit was rerun at `L=1,2,3`; all identity,
  connectedness, phase, stable-sort, relabel, count, and length checks passed.
- The local signed-rectangle enumeration was rerun for `S_3` through `S_6`:
  all 740 oriented signed cases passed, including the both-occurrences-marked
  convention.
- An owned exact occurrence-conjugator/voltage probe checked four 5,000-step
  signed walks on `W_1`.  Across 10,234 adjacent equal-pair observations,
  including 5,050 safe pairs, deletion safety agreed with nonzero pulled-back
  torus homology with zero mismatches, and no `2q+2` bound failure occurred.
  This is finite falsification evidence only, not the proof of Lemma 7.1.

## Remaining work

Finish the boundary/Terminal audit, retain the strongest possible self-attack
against the occurrence-band induction, write the nine-field final report,
freeze owned hashes/manifest, confirm caches are absent, and report the exact
owned file set.
