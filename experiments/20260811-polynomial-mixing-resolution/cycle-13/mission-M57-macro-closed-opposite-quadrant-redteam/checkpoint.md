# M57 halfway checkpoint

## Preliminary result

The opposite mixed quadrant also has a polynomial original-chain escape
certificate.  For

```text
Z_N(q,r)={w in F_N:ell(T_J(w))<q and b(T_J(w))>=r},
W_N=F_N minus Z_N,
```

both macro-closed placements have the preliminary bound

```text
Phi_pm>=1/[3Nm(N-1)^2(m-2)D_N]>=1/(24N^7),
D_N=(3N^2+N-12)/2.
```

## Deletion maps

With `Lambda_N=binom(m,2)(N-1)^2`, M49 strand deletion and

```text
ell-1<=ell(T-v)<=ell,
b-1<=b(T-v)<=b
```

give

```text
|Z_N(q,r)|
 <=N Lambda_N |{F_(N-1):ell<q,b>=r-1}|,             (1)

|W_N(q,r)|
 <=N Lambda_N |{F_(N-1):ell>=q-1 or b<r}|.          (2)
```

## Tight reverse insertions

For a base in (1), attach the new leaf to an old global leaf.  If `b>=r`,
any leaf works because balance never decreases.  If `b=r-1`, choose a
smaller side of a witness edge and a global tree leaf inside that side.  Such
a leaf always exists: for a singleton side its bridge endpoint is a leaf; for
a larger side, a vertex farthest from the bridge endpoint is a global leaf.
Attaching there keeps total leaf count unchanged and changes the witness split
from `r-1,N-r` to `r,N-r`.  Thus the result lies in `Z_N`.  This includes
`r=2` and even `r=N/2`.

For a base in (2), if `b<r`, centroid attachment preserves low balance and
lands in `W_N`.  Otherwise `ell>=q-1`; attaching at any nonleaf raises leaf
count to at least `q`, also landing in `W_N`.

Fixing new label `N` and inserting its adjacent square in all `m-1` gaps
gives each nonempty side a source fraction at least

```text
(m-1)/(N Lambda_N)=2/[Nm(N-1)^2].
```

The padded exact `H3` refresh removes `N` with exact probability
`1/[6(m-2)D_N]`.  Literal global mass orientation and nonnegative remaining
`H3,H4,H5` flow then give the displayed theorem.

## Exact bounded audit

The command

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/opposite_quadrant_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/opposite-quadrant-N4-N8.json
```

checks 61 threshold pairs and 108 attachment families through `N=8`; all
pass.  It is a named finite falsifier, not the universal proof.

## Remaining final checks

- Freeze exact `S_4,m=6` masses, hashes, and full nine-field report.
- Audit the witness-side leaf proof for singleton and tied smaller sides.
- State bounded rectangles/fixed profile cells as the next open family.
