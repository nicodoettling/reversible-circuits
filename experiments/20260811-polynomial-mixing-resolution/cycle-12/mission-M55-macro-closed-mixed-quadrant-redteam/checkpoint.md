# M55 halfway checkpoint

## Preliminary theorem

For `N>=4`, `m=2N-2`, and

```text
X_N(q,r)={w in F_N:ell(T_J(w))>=q and b(T_J(w))<r},
2<=q<=N-1, 1<=r<=floor(N/2),
```

both nontrivial macro-closed placements appear to satisfy

```text
Phi_pm >=1/[3Nm(N-1)^2(m-2)D_N]>=1/(24N^7),
D_N=(3N^2+N-12)/2.
```

This is the literal original-`K` conductance, not a tree-chain surrogate.

## Deletion and count inequalities

Put `Y_N=F_N minus X_N` and
`Lambda_N=binom(m,2)(N-1)^2`.  The accepted M49 strand deletion map has this
fixed-label fiber bound and removes a join-tree leaf.

- From `X_N`, deletion leaves `ell>=q-1` and cannot increase `b`, so it lands
  in `X_base={ell>=q-1,b<r}`.
- From `Y_N={ell<q or b>=r}`, deletion either preserves `ell<q` or leaves
  `b>=r-1`, so it lands in
  `Y_base={ell<q or b>=r-1}`.

Therefore

```text
|X_N|<=N Lambda_N |X_base|,
|Y_N|<=N Lambda_N |Y_base|.                         (1)
```

## Reverse insertions

Every base in `X_base` is restored by attaching the new leaf at a canonical
centroid.  On at least three old vertices a centroid is a nonleaf, so leaf
count rises by one.  Orienting each old edge away from the centroid shows
that every old edge balance is unchanged; the new edge has balance one.
Thus the result lies in `X_N`.

For a base in `Y_base`:

1. if `ell<q`, attach to a leaf, keeping `ell` unchanged;
2. if `ell>=q,b>=r`, any attachment works because adding a leaf never lowers
   old edge balance;
3. if `ell>=q,b=r-1`, attach inside a smaller side of a balance witness.  Its
   split rises from `r-1,N-r` to `r,N-r`, hence has balance at least `r`.

The last step includes the even endpoint `r=N/2`, where the old split
`r-1,r` becomes `r,r`.  The `r=1` edge case falls under item 2 because every
nontrivial tree has balance at least one.

Fixing new label `N` and using all `m-1` square-insertion gaps gives exact
source counts `(m-1)|X_base|` and `(m-1)|Y_base|`.  By (1), each nonempty
profile side has a certified source fraction at least

```text
2/[Nm(N-1)^2].
```

The marked square is removed by the same padded exact `H3` outcome as M53,
with probability `1/[6(m-2)D_N]`, landing in `F_N^c`.  Exact global
orientation uses the literal mass of `X_N` or `Y_N`; all other `H3` and all
`H4,H5` flow remains nonnegative.

## Bounded falsification

The exact command

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/mixed_quadrant_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/mixed-quadrant-N4-N8.json
```

checks 61 threshold triples and 102 shape-level attachment families through
`N=8`; all pass.  The finite calculation could falsify (1) or attachment
existence but cannot prove either universally.

## Remaining final audit

- Restate source injectivity and the exact global `Q` orientation.
- Check empty/trivial `r=1`, extreme `q=N-1`, and `S_4,m=6` masses.
- Freeze hashes and a nine-field report.
- Name the opposite mixed quadrant `{ell<q,b>=r}` as the next standalone
  profile cut if no hidden failure appears.
