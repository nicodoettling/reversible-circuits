# Fresh referee audit of M58

Frozen bundle audited:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M58-macro-closed-profile-rectangle-redteam/report.md
SHA256 a895de3ba34c92ce97820cbf7cd3913ab8f69121272a52280bd25f9b5a96433c
```

## Verdict

**ACCEPT.**  I found no valid objection to the scoped arbitrary-labeled-join-tree-family conductance theorem.  This accepts only M58 theorem (1.3), not a global spectral-gap or mixing claim.

## Independent checks

1. **Pair recording and forward lift multiplicity.**  M49 fixes the deleted label, output word, and the two null positions and proves at most `(N-1)^2` lifts.  Recording the deleted tree leaf's unique neighbor is additional conditioning, so it cannot enlarge this fiber.  Choosing one leaf deterministically for each source makes the forward map single-valued.  Summing over `binom(m,2)` null-position pairs and all valid `(v,z,u)` therefore gives (2.3) without a missing leaf-choice factor.

2. **Reverse insertion and join-tree membership.**  Because the base word avoids `v`, immediately inserting `(vu),(vu)` makes the first copy a cycle join from the fixed point `v`, the second copy returns to the old prefix permutation, and every later prefix is the base prefix.  Thus the resulting minimal word has join tree exactly `T_J(z)+{v,u}`.  All `m-1` word gaps are valid, including the two endpoint gaps.

3. **Source-recovery collision factor.**  For a fixed generated label `v`, the resulting source has exactly two `v`-incident factors.  They are the adjacent equal square, so their locations, `u`, the insertion gap, and the deletion-recovered base `z` are unique.  Thus there is at most one generating quadruple for each fixed `v`.  A source can be generated for at most `N` choices of `v`; division by `N` in (2.7) is therefore sufficient.  No injectivity across labels is assumed.

4. **Ratio arithmetic.**  Combining the forward multiplicity and reverse source count gives

   ```text
   |S_A|/|R_A|
   >= (m-1)/[N binom(m,2)(N-1)^2]
   = 2/[N m (N-1)^2].
   ```

   The same argument applies literally to the complementary arbitrary family.

5. **No flow double counting.**  Selecting one generating quadruple for each distinct source before assigning its `H3` transition means exactly one outgoing edge is counted per source even if the source has several eligible labels or squares.

6. **Exact heat-bath transition.**  Padding the chosen square by the adjacent base factor always supplies a length-three window, including endpoint gaps.  The base factor avoids the chosen `v`; replacing the marked square by a fixed old-label square removes every occurrence of `v`.  The old and new ordered products are the same neighboring transposition.  With the stated lazy kernel, the probability is exactly

   ```text
   (1/2)(1/3)(1/(m-2))(1/D_N)
   = 1/[6(m-2)D_N].
   ```

7. **Both global cut orientations.**  For `B_A`, the complement is `C_A`, so the sources constructed from the complementary tree family enter `F_N^c subset B_A`; for `B_C`, sources from `A` do the analogous job.  Reversibility permits counting either stationary-flow orientation.  Since the smaller global side has mass at most the relevant profile-side mass, division yields theorem (1.3).  The result is asserted only for nontrivial cuts, so empty-family endpoint cases cause no denominator problem.

8. **Final constants and discarded moves.**  Multiplying the source fraction by the one-edge transition probability gives

   ```text
   1/[3 N m (N-1)^2 (m-2) D_N].
   ```

   With `m=2N-2`, the displayed `1/(24N^7)` weakening is valid.  Unused `H3` outcomes and all `H4,H5` flow are nonnegative and may be discarded in a lower bound.

## Numbered objections

None.

## Strongest remaining limitation

The theorem controls only cuts saturated by the labeled join-tree statistic inside the minimal macro.  It gives neither a Poincare inequality within individual join-tree fibers nor control of surplus-length macros, exactly as M58 states.
