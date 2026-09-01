# M260 Checkpoint

Status: **fresh audit complete; raw CP-1--CP-6 accepted with no material
objection; CPR and RST remain separate and unresolved**.

This mission is locked to a fresh immutable audit of M257. The required
project sources and M257 plan/audit request have been read. No finite replay
or census has been or will be used.

All six entries of M257's `SHA256SUMS` verify, and the digest of that inventory
is exactly

```text
9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1.
```

Every payload in M240, M242, M244, M247, M250, and M254 verifies. Their
inventory digests are, respectively,

```text
2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04.
```

The locked DPS PDF verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
Direct reading of DPS Proposition 3, the hairy-tree cyclic-order definition,
Lemma 2, and RandomQuad/Theorem 5 supports the contour/LIFO inputs and no
two-rank endpoint theorem.

## Independent contour findings

- At a canonical `x_a`, arrival on parent side `R_a` followed by decreasing
  black rotation reaches `L_a` immediately. Traversing the white vertex in
  increasing cyclic order, then returning on `L_a`, gives CP-2 including the
  trailing `B_a(L_a down R_a)` block. Ordering by the actual parent incidence
  `kappa` includes every post-wrap child.
- The reversed slot has parent incidence `L_v` and child incidence `R_v`.
  Arrival on `L_v` therefore traverses the full strict decreasing interval to
  `R_v`; the return from `R_v` reaches `L_v` immediately. This gives CP-5,
  rather than the canonical row with the labels merely renamed.
- Accepted M250 metric pruning replaces an off-path canonical excursion by
  `S^(L_h) W^(R_h) S^(*) S^(R_h)`. Its parent crossing contributes the
  leading `S^(R_h)`, giving the five-token CP-4 block. M250's complete-node
  clause licenses all such substitutions without crossing the retained path
  hole.
- At old rank, `x_1` has `(alpha,beta)` and parent `y_d`. At new rank, `x_1`
  has `(gamma,delta)` and parent `y_(d+1)`, while the rerooted old leaf `d` is
  the new canonical child of `1` with parent incidence `R_d=beta`. This is
  exactly CP-6; the rank-specific modulus supplies all intervening and new
  half-edge labels without any fresh-label assumption.

The proved material supports only the raw CP-1--CP-6 context and nesting
reduction. CPR metric O/C simplification and RST endpoint tables remain
hypotheses; neither implies RSPT until both are proved. The exact accepted
partition reads CPR as stopping before the rank-dependent a=1 context, which
RST alone consumes. The fuller audit records that and two other nonmaterial
wording clarifications. No hidden RSPT claim is present.
