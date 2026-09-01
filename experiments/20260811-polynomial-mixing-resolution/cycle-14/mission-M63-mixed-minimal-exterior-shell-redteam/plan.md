# M63 plan: mixed minimal/exterior shell red team

## Exact target

Use `(pq)(x)=p(q(x))`, `m=2N-2`, and the literal lazy same-product
`r in {3,4,5}` chain.  Fix a labeled path tree `T_N` with original leaves
`v,w`.  Let `Core=Del_{v,w}` and let

```text
A_N={x in F_N(T_N):Core(x) in B_N}
```

for a nonempty proper, preferably balanced, core set `B_N`.

Construct a proper exterior halo `E_N subset F_N^c` that absorbs the
canonical M60 leaf-square exits, and analyze the mixed cut
`C_N=A_N union E_N` with exact global mass and all H3/H4/H5 flow.  Either
prove inverse-polynomial leakage or produce a literal Terminal-B sequence.

## Candidate 1: smallest specified-target halo

Choose leaf `v`, its path edge `f=(v,u)`, and let
`Z_N=Del_v(A_N)`.  Core membership is constant on each `v`-cell, so the hub
`z f f` lies in `A_N` for every `z in Z_N`.  Fix one transposition `s` on
`[N] minus {v}` and set

```text
E_N^(1)={z s s:z in Z_N}.
```

This is the smallest halo absorbing the one specified M60 exit from every
hub, and `|E_N^(1)|=|Z_N|` exactly.  Test the alternate same-fiber targets
`z(v,a)^2` with `a!=u`; these remain in `F_N` but outside the original path
sector.

## Candidate 2: maximal one-step exterior halo

Define

```text
E_N^(all)={y in F_N^c:there exists x in A_N with K(x,y)>0}.
```

This absorbs every exterior H3/H4/H5 outcome from every state of `A_N`, not
only the canonical hubs.  Its cardinality is at most the literal polynomial
outdegree

```text
|A_N| sum_(r=3)^5 (m-r+1)M^r <=3mM^5|A_N|.
```

Determine whether the alternate full-support square targets still give a
uniform polynomial boundary-to-mass ratio.

## Structurally distinct lane

If both one-step halos leak, define a positive-surplus insertion-history cut
inside the one-isolated-label macro: fix the isolated label and deletion base,
then threshold the surplus-square position/strand history.  Its halo is not
defined by the minimal path core.  Audit whether H3 square relocation or H4/H5
support restoration gives a polynomial boundary.

## Exact bounded calibration

At N=5 use the exact balanced core union of size 3,904 in the path fiber of
size 7,808.  Enumerate `Z`, the smallest halo, every alternate-leaf target,
and exact H3/H4/H5 flow for the smallest halo.  A finite zero or mismatch can
falsify the stated injection/normalization; positive finite flow cannot prove
the universal theorem.

