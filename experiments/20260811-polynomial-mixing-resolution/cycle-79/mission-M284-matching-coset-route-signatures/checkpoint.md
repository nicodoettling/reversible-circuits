# M284 checkpoint

Status: halfway theorem fixed; final proof write-up complete and awaiting a
fresh immutable audit.

The mission is scoped to the exact concatenation interface between a valid
base route and the accepted local rooted adjacent-edit corrections.  The first
hard guard is already fixed: M278/M281's old-padded/new-rank correction word is
not, by notation or type, an element of the same-rank coset
`K_Q={a:a(w_Q)=tau_i(w_Q)}`.  Any bridge between them must be explicitly
constructed and proved.

No polynomial refinement, every-color theorem, quotient route, voltage,
congestion, gap, mixing, or Terminal claim has yet been made.

## Immutable gate

Every entry in every assigned inventory passes `sha256sum -c SHA256SUMS`.
The top inventory digests are:

```text
M135  8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358
M137  47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5
M175  f2718a493b7e30a615da1f6e4dbafad9d6501bcbd07822fd791b21eafbb26d88
M176  92fe0752f2014fd320f8bf3ff10e09266872865f705a66ed32787c876592fe4a
M181  d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0
M183  ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46
M200  6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045
M202  33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M269  c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M271  ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73
M273  4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550
M275  8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa
M278  352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad
M281  8a775c75b63b897405a6fc29a455ba322eff7c6e70b13fca735b719ab0e89c8d
```

## Fixed halfway result

Let `B_m` be the signed braid group acting on length-`m` words and let
`j_d:B_(2d-2)->B_(2d)` be the standard embedding which leaves the last two
positions fixed.  For a base endpoint fiber use the word-level preimage

```text
Ktilde_Q={beta in B_(2d-2): beta(w_Q)=tau_i(w_Q)}.
```

For a valid M278 root-extension chart, write `c_(T,i)` for its accepted
old-edited-padded-to-new-edited correction.  The exact liftable upper fiber is

```text
L_(T,i)={j_d(beta);c_(T,i): beta in Ktilde_Q}.
```

Here `;` is chronological concatenation.  Then

```text
L_(T,i) subset Ktilde_(Q+).
```

If a family has one common correction `c`, right cancellation and injectivity
of `j_d` give the exact recursive intersection identity

```text
intersection_Q L_(Q,i)
 = {j_d(beta);c : beta in intersection_Q Ktilde_Q}.       (H.1)
```

This is the standalone **rank-lifted schedule-intersection lemma**.  It is a
word-level statement because an action in the finite rank-`d` image has no
licensed canonical embedding into the rank-`d+1` action image; an explicit
braid representative is also required to retain a length bound.

For fixed `(d,i)`, the accepted local table can be standardized to at most
two correction words.  In an ordinary open row choose every optional scan
sign negative; M240's proof uses only “direct child implies negative” and
allows either sign at a nonchild.  Thus the words are identity versus one
fixed `Q B_d Q^(-1)`.  Internal even, cross-boundary, and last edits each have
one fixed word.  Consequently a `q`-class lower cover lifts to at most `2q`
classes on a family possessing valid charts, with length increment at most
`4d-7`.

## Analytic coverage obstruction

That factor-two recurrence is not an M135 matching-color cover.  For every
upper rank `D>=6`, take the canonical star doubled-tree word

```text
U_D=a,a,b,b,e_3,e_3,...,e_(D-1),e_(D-1),
a=(0,1), b=(0,2),
```

and apply `R_2`, obtaining

```text
V_D=a,b,bab,b,e_3,e_3,...,e_(D-1),e_(D-1).
```

The first four factors multiply to the identity, the later factors are
squares, every star edge remains in the support, and the length is `2D-2`.
Thus `V_D in Z_D` is connected, product-identity, and minimal.  Every
unedited M278 extension-chart source, and every global conjugate of one, has
equality in each consecutive pair, whereas `(V_D)_1!=(V_D)_2`; global
conjugation preserves this equality pattern.  Hence the global orbit of
`V_D` has no such chart.  Every M135 perfect-matching color contains exactly
one `H`-edge over this left global orbit by M135 left-perfectness.

Therefore refinement by the local correction type alone does not even cover
one arbitrary M135 color.  This refutes only the named naive use of the local
table.  It does not refute a polynomial schedule cover using additional base
routes, and it does not change M200's finite `d=5` theorem.

## Exact stop

The polynomial number of common-action classes over an entire M135 color is
still **unresolved**.  The minimally safe recursive signature is a valid
extension chart, an explicit lower-rank braid representative (or its full
word-level endpoint fiber), and the local correction word; the exact semantic
state is the translated embedded fiber `L_(T,i)`.  M181's voltage consequence
remains conditional on quotient routing, and M200 remains finite `d=5` only.
