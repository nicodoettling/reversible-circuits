# Mission M273 checkpoint

Status: **analytic theorem and predeclared four-case guard complete; ready to
freeze**.

## Immutable gate

Every payload in M240/M242, M244/M247, M250/M254, M257/M260,
M262/M265, and M269/M271 verifies against its frozen inventory. The top
inventory digests are

```text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
M262  eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a
M265  ced42bf8a6ccd7ca9ffffdca94919c366273b712875cfe08eeead393b88193f8
M269  c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M271  ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73
```

The locked DPS PDF verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
The relevant source definitions, Proposition 3, Lemma 2, and
RandomQuad/Theorem 5 were read directly.

## Fixed seam coordinates

Put `m=2d-2`, `alpha=m-1`, `beta=m`, `gamma=m+1`,
`delta=m+2`, and cut at `q_0=R_v`. Define

```text
s=m-R_v=2(d-v).
```

Then the old root slot is

```text
(L_1,R_1)=(q_(s-1),q_s)=(alpha,beta),
```

whereas at rank `d+1` the new child and new root slots are consecutive:

```text
(L_d,R_d)=(q_(s-1),q_s)=(alpha,beta),
(L_1,R_1)=(q_(s+1),q_(s+2))=(gamma,delta).
```

Thus the new child `d` is not an anonymous interval token. Its literal
six-token block is the M269 child macro at positions `(s-1,s)`. In every
admissible root input (reversed base, contracted/expanded lens, or sealed
state) it lies wholly on the current-parent arm. Its two forced rows are

```text
W_d^beta   S S S B_1^beta  -> S,
W_1^alpha S S S B_1^alpha -> S,
```

so both labels record `x_1`.

## Fixed root-output calculation

For an open decreasing-path input, the old root row contracts to `F_v(s)`
and the new row contracts to `F_v(s+2)`. The root-white complements close
the top lens labels through exactly

```text
old: W_d^alpha       S^beta  S^alpha S_A B_v^alpha -> S,
new: W_(d+1)^gamma   S^delta S^gamma S_A B_v^gamma -> S.
```

Each is a distance-three row and records `x_v`. Every lower black-arm label
then closes in a distance-one row `W_root^q S B_v^q -> S`. The remaining
white half-edges are matched in DPS Step 4 to the final root.

The surviving decorated ports are individual, not summarized by a count.
At the old cut `t(h)<s`, and at the new cut `t^+(h)<s+2`, hold exactly for
the direct children

```text
D_v={h:v<h<d and p(h)=v}.
```

For each such `h`, the literal port leaves `W_v^(L_h)` and `W_h^(R_h)`;
both are attached to the final root. A direct child `h<v` has `t(h)>s`
(and `t^+(h)>s+2`) and cannot survive final completion. It discharges at
the first path parent `b` whose new lens width is below `t(h)` (equivalently,
on a decreasing path, the first `b<h`), or at initialization if it lies
above the initial width. Only when that first crossing is the root is its
endpoint `x_1`; in general it is `x_b`. The shifted inequalities at rank
`d+1` choose the same `b`, so its endpoint is rank-stable. The exposed
`R_v` white also reaches the final root.

Consequently the fixed endpoint table is

```text
open old: b_d(alpha)=v, b_d(beta)=d;
open new: b_(d+1)(alpha)=b_(d+1)(beta)=1,
          b_(d+1)(gamma)=v, b_(d+1)(delta)=d+1.
```

If the incoming state is `C_a`, or an open lens expands at the root, the
row leaves `C_1`. At old rank all `alpha,beta` whites reach the final root;
at new rank the seam macro has already recorded `x_1` for `alpha,beta`,
while `gamma,delta` reach the final root. Hence

```text
sealed old: b_d(alpha)=b_d(beta)=d;
sealed new: b_(d+1)(alpha)=b_(d+1)(beta)=1,
            b_(d+1)(gamma)=b_(d+1)(delta)=d+1.
```

The direct-root base case `p(v)=1` initializes `F_v(s)` / `F_v(s+2)` and
uses the same completion. The boundary `v=d-1` has `s=2` and is literal.

## Rank coupling fixed for proof

For every inherited nonroot slot `h`,

```text
t^+(h)=t(h)     if h>v,
t^+(h)=t(h)+2   if h<v.
```

Therefore all strict internal contraction/expansion decisions, port
persistence/discharge events, and recorded inherited black endpoints agree
between ranks. In the final open state precisely `R_v` and the two labels
of each `h in D_v` have no earlier distance-three record and reach the two
different final roots. In the sealed state every inherited low label has
the same recorded endpoint at both ranks.

## Predeclared finite guard

After the formulas above were fixed, the allowed guard was frozen to exactly
four schemas:

1. direct-root reversed base with `v=d-1` (empty larger-child set);
2. decreasing multilevel lens with one persistent larger direct-child port
   and one discharged smaller direct-child port;
3. above-`v` lens expanding at the root, with a port discharged there;
4. already sealed `C_a` input.

The no-import full-contour replay checks the two seam-macro rows, the old/new
top-lens rows, the exact surviving whites by label, the corrected nonroot
first-crossing port, and the four endpoint tables. All four cases pass. The
normalized row digest is

```text
922fca4abe3fce67064cb5e5963a69ee222f4fa2fa2c6f89f110a5b0c62e1695.
```

This is only a transcription/boundary falsifier; the interval proof carries
the quantifiers.
