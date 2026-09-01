# Mission M262 substantive checkpoint

Status: **arbitrary-rank literal obstruction isolated; CPR as stated is
refuted before the `a=1` root row**.

## Immutable gate

All entries of M240/M242, M244/M247, M250/M254, and M257/M260 verify.
Their inventory-file digests are

```text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
```

The locked DPS PDF verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.

## Pre-test frontier calculation

For a descending stopped prefix

```text
v=a_0>a_1>...>a_j=a>=2
```

the direct interval calculation suggested the literal open-frontier schema

```text
S S
B_v^[L_a down R_v)
S^(R_v)
Y_v^(R_v up R_a]
S S.                                                   (F-a)
```

Here `[L_a down R_v)` is the decreasing cyclic list beginning at `L_a` and
ending just before `R_v`; `Y_v^(R_v up R_a]` is the *actual* increasing
white word at `y_v`, with every retained direct-child incidence expanded by
the accepted CP-4 block, restricted to the indicated cyclic arc. Thus this
is a token word, not an `O/C` bit. Nesting (F-a) into a strict descent
`a>b` closes the boundary labels `L_a` and `R_a` at distance three, deletes
the intervening ordinary rows at distance one, and returns (F-b). In
particular, an exposed label lying outside the swept boundary interval is
transported by a distance-one row. This was fixed before any finite replay.
The final frozen theorem below needs only, and proves completely, its
branch-simple `v=4`, `a=6` instance; the general decorated schema is a guide
for the repaired transducer and is not promoted as a theorem by M262.

## Exact first obstruction

Take every rank `rho>=8`, modulus `M=2rho-2`, edited vertex `v=4`, and the
rooted tree whose stopped path begins

```text
4 -> 6 -> 1,
```

with no child of `4`; attach every unused nonroot vertex to `1`. This is a
valid tree with root leaf `rho`. The exposed set is `E_4={6}`. CP-5 gives

```text
B_4^4 B_4^3 B_4^2 B_4^1 B_4^M ... B_4^7
S^6
W_4^7 W_4^8 ... W_4^M W_4^1 ... W_4^5
S^6 S^5.                                             (F-0)
```

At the strict internal parent `a=6`, one has `(L_6,R_6)=(9,10)` and the
actual reversed-child incidence is `kappa(4)=L_4=5`. Substitution of (F-0)
in CP-2 and bottom-up deletion of all complete rows leaves

```text
S^9 S_A
B_4^9 B_4^8 B_4^7
S^6
W_4^7 W_4^8 W_4^9 W_4^10
S_C S^10.                                            (F-6)
```

The decisive exposed-label row is literally

```text
W_6^6 S B_6^6 -> S.                                 (F-E)
```

It has distance one. Label `6` has no distance-three endpoint in this row,
and the actual residual (F-6) is another open frontier, not a sealed
canonical `S W^10 S S` word. The same symbolic deletion works at rank
`rho+1`; the two new modulus labels occur only in the displayed distance-one
chains and disappear before (F-6).

This directly refutes the M257 CPR clause that the first step `c<a` (or the
first path vertex above `v`) gives every exposed label a distance-three
endpoint before the root seam. The counterfamily never enters the
rank-dependent `a=1` row.

## Repaired obligation

The next lemma must distinguish at least two literal open frontiers:

```text
O^- : current path vertex a<v,
O^+ : current path vertex a>v.
```

Entering `O^+` need not seal any exposed face. A later internal row may
seal it when its swept cyclic interval crosses `E_v`; in the boundary path
`v<a->1`, the actual `O^+` word reaches RST. Therefore the existing RST
tables with only abstract `O/C` inputs are not yet well-posed for this row;
RST must consume the literal frontier (F-6) or a proved sufficient
refinement.

No finite-rank interpolation, RSPT, IDL, fixed-edit, routing, gap, mixing, or
Terminal inference is made.
