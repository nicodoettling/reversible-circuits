# Mission M257 analytic checkpoint

Status: **source gate verified; exact cyclic path-context recurrence fixed;
RSPT itself unresolved**.

## Immutable gate

Every entry of each predecessor `SHA256SUMS` verifies.  The inventory-file
digests are

```text
M240  2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242  49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M244  134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d
M247  de68dcb09b4462359ba4de95fbcdafddfb7dc4f04a2d29dac19566a63973950b
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
```

The locked `/tmp/DuPoSc13.pdf` verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
Only M244 Theorem 3.1 in its M247-accepted scope and the M250/M254 accepted
metric upgrades are used.  M244's RSMI remains rejected.

## Exact raw path-row recurrence

Fix a rank `rho` with modulus `M=2rho-2`.  At a white vertex `a`, let
`C_rho(a)` be its rooted children.  For a child `c`, define the label of the
actual incidence at `y_a` by

```text
kappa(c)=L_v,  if c=v is the reversed edited child,
         R_c,  otherwise.                              (CP-1)
```

This distinction is essential: treating the edited child as a canonical
`R_v` incidence gives the wrong cyclic row.  Order the children
`c_1,...,c_t` by the cyclic increasing order of `kappa(c_j)` after `L_a`,
and put `q_0=L_a`, `q_j=kappa(c_j)`.  If `a` is canonical, direct contour
reading gives the literal context

```text
P_a[I_1,...,I_t] =
 S^(L_a)
 product_(j=1)^t [ W_a(q_(j-1) up q_j) S^(q_j) I_j ]
 W_a(q_t up L_a) S^(L_a)
 B_a(L_a down R_a) S^(R_a).                          (CP-2)
```

The omitted leading block is `B_a(R_a down L_a)`, which is empty because
`R_a=L_a+1`.  Here `I_j` is the bridge-delimited excursion beginning just
after the crossing into `x_(c_j)` and ending with the return crossing to
`y_a`.  Formula (CP-2) is valid across the cyclic seam: numeric child index
is irrelevant; a lower-index post-wrap child is placed by `kappa`, not by
its index.

For every off-path canonical child `h`, the accepted metric pruning theorem
substitutes, with side identities retained,

```text
I_h -> S^(L_h) W^(R_h) S^(*) S^(R_h).                (CP-3)
```

Thus its complete parent block is

```text
S^(R_h) S^(L_h) W^(R_h) S^(*) S^(R_h),              (CP-4)
```

and all deletions commute with the one retained path-child interval.  If
`c` is that child, equations (CP-2)--(CP-4), with `I_c` left as a hole,
define a one-dimensional cyclic context operator `P_(a,c)`.  This is the
exact stopped-path recurrence; no colored projection or unspecified
"absorption" is used.

At the initial edited vertex, child-side and parent-side labels are reversed.
If its canonical children are `c_1,...,c_t`, now ordered increasingly after
`R_v`, the exact base operator is

```text
P_v^rev[I_1,...,I_t] =
 B_v(L_v down R_v) S^(R_v)
 product_(j=1)^t [ W_v(q_(j-1) up q_j) S^(q_j) I_j ]
 W_v(q_t up R_v) S^(R_v) S^(L_v),                  (CP-5)
```

where `q_0=R_v`, `q_j=R_(c_j)`.  The final omitted block
`B_v(R_v down L_v)` is empty.  Because `R_v=L_v+1`, the leading black block
contains every label except `L_v,R_v`, in decreasing cyclic order.  Larger
direct children `r>v` occur before the wrap and lower-index children occur
after it; (CP-5) includes both.

## Root seam and first unresolved row lemma

For ancestors strictly between `v` and `1`, the same operator
`P_(a,c)` occurs at ranks `d` and `d+1`; only the ambient modulus and the
outside root completion differ.  The seam is exceptional and is not hidden
inside this statement:

```text
old rank:  x_1 has (L_1,R_1)=(alpha,beta), parent y_d;
new rank:  x_1 has (L_1,R_1)=(gamma,delta), parent y_(d+1),
           and y_1 has the new canonical child d with
           kappa(d)=R_d=beta.                         (CP-6)
```

The first still-unproved row package is now:

> **Cyclic path-row lemma (unresolved).**  First simplify (CP-5) to the exact
> initial state `O(E_v)`.  Then reduce every complete off-path
> block in (CP-2) by (CP-3)--(CP-4).  Couple the old/new copies of the
> retained hole by inherited labels.  If the input has M250's exposed set
> `E_v`, then the literal side-token closure of `P_(a,c)` (i) transports all
> exposed labels through distance-one rows when the current path step is a
> strict descent with no prior seal; (ii) gives every exposed label a common
> rank-stable distance-three black endpoint at the first internal ascent or
> first path vertex above `v`; and (iii) preserves all other inherited low
> endpoints.  This must hold for the cyclic post-wrap sector, not merely for
> numerically increasing child indices.

Once this row lemma is proved, the separate explicit old/new seam-table lemma
from (CP-6) remains to derive M250 (4.4)--(4.5).  Conversely,
(CP-2)--(CP-6) show exactly where
a symbolic counterfamily would occur: the first exposed label whose complete
row has side count other than the asserted `1` or `3`, or whose black token
lies at different named vertices at the two ranks.

No finite expansion or census has been run in M257.  The four frozen M250
rows have not been replayed.  No IDL, fixed-edit, every-color, voltage,
length, gap, mixing, or Terminal inference is made.

Final disposition: the raw CP-1--CP-6 recurrence is frozen as proved; the
metric CPR simplification and the separate CP-6 root tables are unresolved.
