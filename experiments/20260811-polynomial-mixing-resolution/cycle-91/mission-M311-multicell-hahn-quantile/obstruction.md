# M311 Exact Obstruction to QBP_1

Date: 2026-08-14 UTC
Status: QBP_1 refuted exactly at the sole authorized new rank `k=11`

## 1. Static coefficient geometry

At `k=11`, `n=33`, the exact Abel signs are

```text
R_1,R_2,R_3,R_4<0;
R_5,R_6,R_7,R_8,R_9>0;
R_10=0.
```

The 19 supported quantile cells therefore split into the three predeclared
maximal sign blocks

```text
block 0: h=1,...,4,  sign -1,  8 cells;
block 1: h=5,...,9,  sign +1, 10 cells;
block 2: h=10,       sign  0,  1 cell.
```

The checker verifies that these are consecutive staircase segments, that
their exact masses are `M_b-M_(a-1)`, and that they cover every cell once.

## 2. First lexicographic counterexample

The first negative block in the frozen order `(u,ell,block_index)` is

```text
(u,ell,block_index)=(1,2,1),
block sign=+1,
block rungs h=5,...,9.
```

Its ten cells are

```text
(5,5),(5,6),(6,6),(6,7),(7,7),
(7,8),(8,8),(8,9),(9,9),(9,10).
```

The exact complete block sum is

```text
-2061577314459922172641215612586209282269020583869992685957021396704823223246367368524303337392898219047370249489990505551190598969997087218733977014686080513732765909680273626243354879974696670860872661297162706082605379671283262275186077612570547848875709
/57279694330006960277221458518965386699701247536817041392297378955423047072191462802544866890587366849437209220150089143598727486477148871354092375414658109189979205585843112644773807166449670610550843123177619456000000000000000000000000000000000000000000000
```

which is approximately `-0.03599141613051397`.  Every middle phase and every
cell in the block is included.  This single exact strict inequality refutes
universal QBP_1.

The other two block values in the same row are approximately

```text
block 0: +0.19410751881292468,
block 2: -0.008194439239596727.
```

Their full sum is exactly positive, approximately `0.149921663442814`.
Thus this witness refutes the blockwise strengthening but does not refute
MCLP_1.

## 3. Complete sole-rank counts

The guard covers

```text
5 middle classes * 30 lags = 150 rows,
150 rows * 3 blocks = 450 block instances.
```

Exactly 154 block instances are negative, and 118 of the 150 rows contain a
negative block.  Nevertheless all 150 full QTI_1 aggregates are strictly
positive.  Their minimum is approximately `0.09958803705967692`, attained at

```text
(u,ell)=(2,10),(2,23),
```

an exact reflected pair because `33-10=23`.  The checker asserts reflection
for every `Xbar_c`, `Ybar_d`, block value, and aggregate.

All statements in this section are exact finite facts at `k=11`; the decimal
values are only readable renderings of stored rational numbers.

## 4. Strongest surviving result

The analytic staircase and block decomposition QBD_1 survive unchanged:

```text
P_(k,ell)(u)=sum_q C_q(k,u,ell)
```

for every stated odd `k` and endpoint.  What fails is the proposed sign
`C_q>=0` for each block.  MCLP_1 remains unresolved because inter-block
cancellation is positive in every tested row but is not controlled at all
ranks.
