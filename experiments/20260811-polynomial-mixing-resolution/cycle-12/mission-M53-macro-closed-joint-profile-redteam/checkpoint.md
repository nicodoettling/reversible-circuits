# M53 halfway checkpoint

## Status

The joint-profile cut does **not** produce a bottleneck.  The two constraints
can be restored simultaneously by one controlled leaf attachment, including
the even balanced endpoint.  The resulting preliminary bound for both
macro-closed orientations is

```text
Phi_pm >= 1/[3 N m (N-1)^2 (m-2) D_N] >= 1/(24N^7),
D_N=(3N^2+N-12)/2.
```

This is a scoped anti-bottleneck theorem, not a global gap.

## Exact counting skeleton

Let

```text
H_N(q,r)=|{w in F_N: ell(T_J(w))>=q, b(T_J(w))>=r}|,
C_N(q,r)=|F_N|-H_N(q,r),
Lambda_N=binom(m,2)(N-1)^2,
m=2N-2.
```

Deleting a join-tree leaf changes the two statistics as follows:

```text
ell(T)-1 <= ell(T-v) <= ell(T),
b(T)-1   <= b(T-v)   <= b(T).
```

The accepted leaf-strand map deletes exactly two null increments, produces a
word in `F_(N-1)` with join tree `T-v`, and has at most `(N-1)^2` lifts after
the deleted label and null positions are fixed.  Choosing one leaf per word
therefore gives

```text
H_N(q,r) <= N Lambda_N H_(N-1)(q-1,r-1),
C_N(q,r) <= N Lambda_N C_(N-1)(q,r).                 (1)
```

## Simultaneous high insertion

Take a base tree on `N-1` vertices with `ell>=q-1,b>=r-1`.

- If only the leaf constraint is tight, attach the new leaf to any nonleaf.
- If only balance is tight, choose a balance witness, orient a smaller side,
  and attach inside that side.
- If both are tight and `r-1>=2`, attach at the bridge endpoint lying in the
  smaller side.  That endpoint has an internal neighbor and is a nonleaf, so
  leaf count rises while the witness split rises from `r-1` to `r`.
- If both are tight and `r-1=1`, the base has balance one and hence is a star.
  Tight leaf count forces `q=N-1`; but the only `N`-vertex tree with `N-1`
  leaves is again a star and has balance one.  Thus for `r=2` the target joint
  set is empty.  This is the sole apparent corner and is irrelevant whenever
  `H_N(q,r)>0`.

The feasibility condition `r<=floor(N/2)` ensures that increasing a smaller
side from `r-1` to `r` really gives balance at least `r`; this includes the
even endpoint split `N/2,N/2`.

Fix the new label `v=N` and choose one such attachment deterministically.
Inserting `(v,u)^2` in any of the `m-1` gaps gives

```text
(m-1) H_(N-1)(q-1,r-1)
```

distinct high-profile sources.

## Low-complement insertion

For a base in the complement:

- if `ell<q`, attach the new leaf to a canonical old leaf; the number of
  leaves is unchanged;
- otherwise `b<r`; attach at a canonical centroid.  Orient every old edge
  away from the centroid.  Its away-component has size at most half the old
  tree, and adding the new leaf at the centroid leaves every old edge balance
  unchanged; the new edge has balance one.  Hence `b` remains below `r`.

This constructs `(m-1)C_(N-1)(q,r)` distinct low-profile sources.

## Exact `H3` action and global orientation

Pad each inserted square by a neighboring base transposition, using the
right neighbor except at the final gap.  The block product is that padding
transposition.  Refresh the square to a fixed square on old labels.  The
specified outcome has exact probability

```text
(1/2)(1/3)(1/(m-2))(1/D_N)=1/[6(m-2)D_N],
```

and removes the new label, so the target lies in `F_N^c`.  Combining (1) with
the source counts gives a source fraction at least

```text
(m-1)/(N Lambda_N)=2/[N m (N-1)^2]
```

on whichever joint-profile side is the complement of the macro-closed cut.
Uniform reversibility lets the directed source flow be read in either
boundary orientation.  Since the conductance denominator is at most the
literal global mass of that profile side, no assumption about `pi(F_N)` or
which global side is smaller is made.  `H4` and `H5` remain nonnegative parts
of the full boundary flow.

## Exact bounded falsification

The deterministic audit

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M53-macro-closed-joint-profile-redteam/joint_profile_audit.py \
  --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M53-macro-closed-joint-profile-redteam/joint-profile-N4-N8.json
```

checks 61 threshold pairs and 108 shape-level attachment families through
`N=8`; all pass.  It also reproduces `|Omega(4,6)|=3936`, `|F_4|=2880`, and
`pi(F_4)=30/41`.  For `(N,q,r)=(4,2,2)`, the exact joint split is
`2136+744`, and the two global macro-closed orientations have masses
`89/164` versus `75/164` and `133/164` versus `31/164`, respectively.  These
finite calculations could falsify (1) or insertion existence but do not
prove them.

## Remaining audit before final report

1. Restate the fixed-position strand-lift proof sufficiently for a
   self-contained dependency trail.
2. Check every threshold endpoint, especially `q=N-1,r=1` and
   `r=floor(N/2)`.
3. Freeze exact hashes and repository hygiene.
4. State the next stronger mixed-quadrant/arbitrary-joint-layer proposition;
   this theorem does not control refinements within a profile cell.
