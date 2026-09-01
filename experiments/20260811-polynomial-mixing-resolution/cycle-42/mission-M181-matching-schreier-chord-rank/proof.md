# An actual-matching family with full Schreier chord rank

Date: 2026-08-13 UTC.

## 1. Scope and conventions

Let `d>=5`, `m=2d-2`, `G=S_d`, and

```text
Z_d={(t_1,...,t_m):t_1...t_m=id, support connected on [d]},
Q_d=Z_d/G.
```

Permutations compose as `(p q)(x)=p(q(x))`.  Factors and signed braid
symbols are applied chronologically from left to right.  On adjacent
transpositions,

```text
R_j(a,b)=(b,b^(-1)ab),       R_j^(-1)(a,b)=(aba^(-1),a).
```

The frozen orbit-incidence statements use one-based `[d]` and
`H=Stab_G(d)`.  The explicit words below use zero-based labels
`0,...,d-1`; their anchor `0` is a gadget label and is not assumed to be
the distinguished M135 white root.

For an ordered width-`s` quotient tuple `q`, write

```text
W_s=F_2^s/Delta,       Delta=<(1,...,1)>.
```

M175/M176 proves that the span of literal Schreier fundamental-cycle gains
is exactly `V_stab(q)`.  This note proves full rank only for an explicit
family of source subfamilies inside every M135 perfect-matching color.  It
does not prove the universal accepted-matching chord-rank lemma.

## 2. Frozen-input reconciliation

All assigned frozen manifests passed before use.  The imported statements
are:

1. M135/M137: for fixed `(d,i)`, an edge of `B_(d,i)` is an `H`-orbit
   `Q` in `Z_d`, where `H=Stab_G(d)`; its left and right endpoints are
   global `G`-orbits.  A color is a perfect matching, so it has exactly one
   edge incident to every left vertex and every right vertex.
2. M141/M143 and M146/M148: every nonempty subfamily of such a matching has
   aligned source and target factor group `P_(d,s)` and no further
   conjugacy-multiset obstruction.
3. M154/M158: the accepted elementary braid `E_j` conjugates an identity
   word by its factor in position `j`; aligned products in `P_(d,s)` give
   literal simultaneous inner-conjugation loops.
4. M163/M164, M169/M172, and M175/M176: relative orientation is the remaining
   quotient, with

   ```text
   1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,
   ```

   and fixed-endpoint zero routing is exactly affine tree-offset membership
   in the actual chord-gain column space.

There is no conflict among these inputs.  In particular, a matching color
does **not** contain every physical word over a left quotient vertex; it
contains exactly one `H`-orbit edge there.  Section 6 handles this distinction
explicitly.

## 3. An anchored binary six-factor relation

On labels `0,1,2,3`, put

```text
U=(01),(01),(02),(02),(03),(03),
V=(01),(01),(02),(02),(13),(13).
```

The M175 four-move chronological word

```text
beta=(4,3,5,4)
```

has the directly checked endpoints

```text
beta U=(23).U,
beta V=(01)(23).V.                                  (3.1)
```

The second transporter is even but moves the intended anchor.  We now remove
it by an accepted literal inner correction.

For a six-factor identity word, use the exact M154 elementary word

```text
E_j=(-j,...,-5)(5,4,3,2,1,1,2,3,4,5)(5,...,j).
```

It maps `X` to `x_j^(-1).X`, where the dot denotes global relabeling.
Let

```text
I=(1,3,1,3,5,3,5,3,5,1,3,1).
```

At the pair `(beta U,beta V)`, direct multiplication of the aligned factors
at the positions in `I` gives

```text
p=(id,(01)(23)).                                    (3.2)
```

Indeed their factors at positions `1,3,5` are

```text
beta U: (01),(03),(02);       beta V: (01),(13),(02),
```

and the displayed twelve-factor product is (3.2).  Concatenating the
elementary words in reverse expression order,

```text
C=E_(I_12) E_(I_11) ... E_(I_1),
```

conjugates the aligned pair by `p^(-1)`.  This is the standard reverse-word
induction behind M154: after each conjugation, the next current factor is
the corresponding conjugate of the original factor, so the accumulated
transporter telescopes to the inverse displayed product.

Let `h` be the chronological concatenation `beta C`.  Equations
(3.1)--(3.2) give

```text
h U=(23).U,               h V=V.                    (3.3)
```

Thus the two transporter signs are `1,0`, and both transporters fix label
`0`.  The explicit word has `196` correction moves and `200` moves in
total.  This finite count only identifies the reproducible certificate; no
general route-length conclusion is drawn.

Relabel (3.3) on four distinct labels `0,a,b,c`.  With

```text
U(a,b,c)=(0a)^2(0b)^2(0c)^2,
V(a,b,c)=(0a)^2(0b)^2(ac)^2,                         (3.4)
```

the same factor-index word satisfies

```text
h U(a,b,c)=(b c).U(a,b,c),
h V(a,b,c)=V(a,b,c).                                 (3.5)
```

The nontrivial transporter fixes the common anchor `0` and every label
outside `{a,b,c}`.

## 4. Minimal connected all-label embeddings

Set

```text
r=floor((d-1)/3),       t=d-1-3r.
```

For `k=1,...,r`, set

```text
(a_k,b_k,c_k)=(3k-2,3k-1,3k).
```

For a binary pattern `epsilon in F_2^r`, define `W_epsilon` by
concatenating block `U(a_k,b_k,c_k)` when `epsilon_k=1`, block
`V(a_k,b_k,c_k)` when `epsilon_k=0`, and finally

```text
(0x)^2
```

for each remaining label `x=3r+1,...,d-1`.

Every displayed edge occurs as an adjacent doubled pair, hence
`W_epsilon` has product identity.  Each block connects all three new labels
to `0`: in the `V`-block, `c_k` connects through `a_k`.  Each filler
label connects directly to `0`.  Therefore the support is connected on all
`d` labels.  Finally,

```text
|W_epsilon|=6r+2t=2(d-1)=2d-2.                       (4.1)
```

These are genuine members of the accepted minimal connected sector `Z_d`,
not six-factor words padded by disconnected or nonminimal filler.

Let `h_k` be (3.5) shifted to the six factor positions of block `k`.
It never crosses a block boundary.  Equation (3.5) and the disjointness of
the nonanchor labels give the **literal whole-word endpoint**

```text
h_k W_epsilon =
  (b_k c_k).W_epsilon,   if epsilon_k=1,
  W_epsilon,             if epsilon_k=0.             (4.2)
```

The swap fixes `0`, all other blocks, and every filler edge.  Thus the
shared filler is synchronized and fixed, not silently discarded.

## 5. Distinct quotient vertices and full voltage

Fix

```text
1<=s<=r+1
```

and use patterns

```text
epsilon^0=0,       epsilon^j=e_j  (1<=j<=s-1).
```

The quotient points `[W_(epsilon^j)] in Q_d` are pairwise distinct.
Suppose, to the contrary, a relabeler maps a word having a `U`-block at
some differing position to one having a `V`-block there.  The first and
third local factors are the distinct edges `{0,a_k}` and `{0,b_k}` on
both sides.  Their unique common endpoint forces the relabeler to fix `0`;
it then fixes `a_k` and `b_k`.  But it cannot map the last local edge
`{0,c_k}` to `{a_k,c_k}`.  The inverse direction is equally impossible.
Factor positions also prevent permuting blocks.  Hence no global conjugacy
exists.

Apply `h_k`, for `1<=k<=s-1`, diagonally to the ordered tuple

```text
q=([W_0],[W_(e_1)],...,[W_(e_(s-1))]).
```

Equation (4.2) shows that this is an actual closed synchronized quotient
walk.  Its transporter-parity vector has representative

```text
(0,...,0,1,0,...,0)=e_k'
```

with the `1` in tuple coordinate `k` and zero in coordinate `0`.  The
classes of these `s-1` single-coordinate vectors form a basis of
`W_s=F_2^s/Delta`: any linear combination has coordinate `0` equal to
zero, so it cannot equal the nonzero diagonal vector; it is zero only when
all coefficients vanish.  Consequently

```text
V_stab(q)=W_s,             dim V_stab(q)=s-1.         (5.1)
```

By M175, the actual Schreier fundamental-cycle chord columns have this same
span and rank.  The loops (4.2) themselves are literal closed-braid cycle
generators, so no generator-forgetting or Cartesian-product relaxation is
used.

### Why an edge-vector symmetry argument would not suffice

M135 gives no action permuting coordinates of a fixed ordered tuple:
reordering only identifies `V_stab(q^pi)=pi V_stab(q)`, not invariance of
`V_stab(q)` under `pi`.  There is also a parity defect.  The span in
`F_2^s` of connected-graph edge vectors `e_i+e_j` is the even-weight
space `E`.  If `s` is odd, its image in `W_s` is full; if `s` is even,
`Delta<=E` and the image `E/Delta` has dimension `s-2`, one short of
`W_s`.  For `s=2`, `e_1+e_2` is the diagonal and is zero in the
quotient.  The single-coordinate classes above avoid this issue for all
`s`.

## 6. Exact inclusion in every M135 perfect-matching color

Fix `d>=5`, a DPS edit `i`, and any one perfect-matching color `M` of
`B_(d,i)`.  Its left vertex set is `Q_d`.  For each constructed quotient
point `q_c=[W_(epsilon^c)]`, perfectness gives exactly one incident edge
`Q_c in M`.  Here `Q_c` is an `H`-orbit of physical words whose containing
global orbit is `q_c`.  Distinct `q_c`'s select distinct edges, and their
right endpoints are distinct because `M` is a matching.

Choose any physical representative `u_c in Q_c`.  Since its global orbit
is `q_c`, there is an `alpha_c in G` such that

```text
u_c=alpha_c.W_(epsilon^c).                            (6.1)
```

In general `alpha_c` need not lie in `H`, and the matching need not contain
the literal word `W_(epsilon^c)`.  Neither is required.  Braid action
commutes with arbitrary global relabeling in each coordinate, so (4.2)
becomes

```text
h_k u_c =
 (alpha_c delta_(c,k) alpha_c^(-1)).u_c,              (6.2)
```

where `delta_(c,k)` is either `(b_k c_k)` or `id`.  Conjugation preserves
sign.  Thus the very same synchronized braid has exactly the basis voltage
computed in Section 5 on the actual representatives of the selected
`H`-orbit edges.  Although the conjugated odd transporter fixes
`alpha_c(0)` rather than necessarily the distinguished white root `d`,
that is precisely allowed in the global quotient stabilizer whose root
monodromy M169 measures.

We have proved:

> **Theorem 6.1 (explicit actual-matching full-rank family; PROVED).**
> For every `d>=5`, every adjacent DPS edit `i`, every M135
> perfect-matching color, and every
> `1<=s<=1+floor((d-1)/3)`, the color contains an accepted ordered
> width-`s` source subfamily whose actual synchronized Schreier chord-gain
> column space is all of `W_s`, of rank `s-1`.

For `s=1`, `W_1=0` and the statement is vacuous.  For `s>=2`, the
explicit loops above give the asserted basis.

## 7. Endpoint membership and the M169 interface

For the actual representatives selected in Section 6, put

```text
U=(u_c),       V=(tau_i(u_c)),       q=[U],       r=[V].
```

If `r` lies in the synchronized quotient component `Gamma(q)`, then every
M175 fixed-physical-endpoint tree offset `a_T(U,V)` lies in `W_s`.  By
(5.1), `W_s=V_stab(q)=colspan(z_T)`; hence

```text
a_T(U,V) in colspan(z_T).                            (7.1)
```

M175's affine criterion then supplies a zero-relative-voltage quotient
route.  This is intrinsic under section changes and endpoint coboundaries,
because both (7.1) and M175's criterion are.

At the source, M169's accepted exact sequence specializes to

```text
1 -> P_(d,s) -> K_mon(q) -> W_s -> 1,
```

so `K_mon(q)=S_d^s`.  This is an exact qualitative monodromy conclusion for
the constructed source family.

The hypothesis `r in Gamma(q)` is not discharged here.  Full stabilizer
voltage cannot create a quotient route between different components.
Therefore this note does not prove simultaneous realization of the selected
M135 source/target pairs.

## 8. Exact remaining obligations

The construction rules out a universal zero-voltage invariant at `d>=5`
and proves full rank inside actual accepted matchings for widths growing
linearly with `d`.  It leaves unresolved:

1. chord rank and fixed-endpoint membership for an arbitrary accepted
   matching subfamily;
2. existence of a synchronized quotient route from the constructed source
   tuple to its matched DPS target tuple;
3. any polynomial bound on quotient routes or aligned inner corrections.

No broad `d=5` quotient enumeration, qualitative-connectivity inference,
physical gap, mixing theorem, or Terminal conclusion is made.
