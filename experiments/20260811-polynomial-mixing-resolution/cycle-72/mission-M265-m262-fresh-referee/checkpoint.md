# M265 Checkpoint

Date: 2026-08-14

Status: **substantive audit complete; ACCEPT is supported, subject to the
nonmaterial RST qualification below**.

The source-of-truth documents and the reversible-circuit-sampler skill were
read before inspection.  M262's `SHA256SUMS` has the required digest

```text
eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a
```

and every one of its nine payload hashes verifies.  The frozen M257 and M260
inventories also verify at

```text
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
```

as do the exact M250/M254 RSPT records at their top digests
`243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7`
and `77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04`.

For arbitrary `rho>=8`, the displayed family has `rho-1` edges and is
connected, hence is a tree; rooting at the leaf `rho` gives
`p(4)=6`, `p(6)=1`, `p(1)=rho`.  Vertex `4` has no rooted child, so the
M250 exposed set is exactly `E_4={6}`.  The strict nonroot CP-2 row at `a=6`
has `(L_6,R_6)=(9,10)` and edited-child incidence
`kappa(4)=L_4=5`.

Literal CP-5 substitution followed by the prescribed complete-node order
gives the left distance-one chain

```text
4,3,2,1,M,M-1,...,10,
```

then the distance-one rows `8,7,6` at `x_6`, the distance-three label-`5`
row, and the final distance-one chain

```text
4,3,2,1,M,M-1,...,11.
```

Thus the sole exposed label has the unique internal row

```text
W_6^6 S B_6^6 -> S
```

and the exact residual is M262's `(F-6)`.  Increasing rank adds only labels
`M+1,M+2` inside the two distance-one chains, leaving the inherited residual
unchanged.  The next vertex is `a=1`, so no later strict internal row exists;
the root seam is not entered.

An independently written deterministic guard confirms the tree, exposed set,
complete-node order, label-6 distance, common residual, and added labels at
`rho=8,9`.  It is explicitly not used for the universal quantifier.

This is a direct counterexample to M250 `(4.2)` / M257 CPR's required first
`a>v` (`c<a`) transition to `C`.  It leaves M257/M260 CP-1--CP-6 intact.
The old one-bit `O/C` description is not a proved sufficient input quotient
for the separated RST obligation once this transition fails; RST must use
the literal incoming frontier or a newly proved sufficient refinement.
This does not itself refute endpoint tables `(4.4)--(4.5)`, prove that
`O^- / O^+` is sufficient, or refute IDL.
