# Smallest obstruction to moving only the distinguished leaf subtree

Date: 2026-08-11.  This refutes only the proposed corner-walk template in
which every full child-boundary rotation moves the same distinguished leaf
subtree and all other parent/child relations remain fixed.  It does not
refute a `Y_r`-to-`Pbar_r` comparison that swaps indistinguishable leaves or
moves auxiliary subtrees.

## Proposition

At `r=3`, the insertion-slot graph of a fixed distinguished leaf can be
disconnected under full child-boundary rotations that always move that leaf.

## Proof

Let the fixed base tree be the two-edge path

```text
root -- h -- c.
```

Insert the distinguished leaf `S` as the first child of `h`, before `c`.
Thus the source has root child `h` and ordered children `[S,c]` at `h`.
Its preorder degree vector is `(1,2,0,0)` and its parking macro is
`(0,1,1)`.

A full upward child-boundary rotation moves the later branch `B` into its
immediate left sibling along the left sibling right spine.  The marked
branch `S` cannot be `B`, because it is the first child of `h`.  Conversely,
a reverse rotation can lift `S` only when `S` is the last child of its
current parent.  It is not: `c` follows it.  No rotation at another vertex
moves `S`.  Hence this marked insertion slot has degree zero in the
distinguished-subtree-only move graph.

Deleting `S` and reinserting it at the root is a valid leaf-replanting move
and gives a different unmarked plane-tree shape, so the required corner
graph is not connected.

There is no obstruction to the full unmarked actual chain in this example.
For one of the root insertions, lifting the *other* leaf `c` produces the
same unmarked endpoint in one actual move.  Thus any successful comparison
must permit mark swapping or auxiliary-subtree motion and include that
choice in source-recovery metadata; the invariant distinguished-subtree
template is too rigid.
