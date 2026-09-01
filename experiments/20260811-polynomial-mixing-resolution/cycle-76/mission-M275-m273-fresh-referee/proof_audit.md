# M275 fresh immutable proof audit of M273

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

**ACCEPT** frozen M273's standalone decorated-lens root-seam theorem
(DL-RST).  Material objections: **none**.

The theorem is deterministic DPS side-token closure for ordinary odd edits
at `d>=5`; it is not a Markov-chain theorem.  The ambient sampler target
remains uniform on fixed-length identity words for the lazy exact
same-product `{3,4,5}` heat-bath chain.

The acceptance licenses the formal ordinary-edit composition in Section 11
below.  It does not license fixed edits, every-color synchronization,
voltage correction, any other routing family, congestion, a spectral gap,
polynomial mixing, or Terminal A/B.

## 2. Clean-room and immutable gates

This mission initialized `plan.md` and `checkpoint.md`, then fixed
`cleanroom_derivation.md`, before opening any M273 artifact.  The independent
derivation used only accepted raw CP-1--CP-6, metric pruning, and the
strict-internal decorated-lens theorem.

Every entry of M273's inventory verifies.  The independently computed digest
of its `SHA256SUMS` is

```text
4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550.
```

Every entry in every cited frozen dependency also verifies.  Their inventory
digests are

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

The locked DPS source verifies at

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

The dependency boundary is sound: M250/M254 supplies metric canonical
pruning, complete-node commutation, and the common-nonchild endpoint;
M257/M260 supplies raw CP contexts; M269/M271 supplies the strict-internal
decorated-width transducer.  Neither M262's refuted coarse rule nor M250's
false one-bit transition is used.

## 3. Seam coordinates and the `t+` map

Put

```text
m=2d-2, R_v=2v-2, s=m-R_v=2(d-v),
(alpha,beta,gamma,delta)=(m-1,m,m+1,m+2).
```

In coordinates `q_0=R_v`, the exact slot positions are

```text
old root 1: (s-1,s)     = (alpha,beta),
new child d:(s-1,s)     = (alpha,beta),
new root 1: (s+1,s+2)   = (gamma,delta).
```

For an inherited nonroot slot `h!=v`, direct modular subtraction gives

```text
t^+(h)=t(h)       for h>v,
t^+(h)=t(h)+2     for h<v.                          (3.1)
```

Above-`v` positions are all at most `s-2`; below-`v` positions are all at
least `s+2`.  Thus every inherited pairwise width comparison is preserved,
including comparisons across the cut.  No inherited slot occupies either
root cut, and `r=s` would make the path vertex the root.  The new child is
the only inserted slot.

This proves more than equality of abstract states: every port survives or
crosses its frontier at the same parent at both ranks and therefore records
the same black endpoint.

## 4. Full root complement and final-root rows

After the bridge-delimited root excursion returns along `R_1`, the outer
root-white contour contains one white of every label other than `R_1`, in
increasing cyclic order, followed by the second `R_1` tree crossing.  For a
contracted lens `F_v(s_r)`, the last outer white is `W_root^(L_1)`.  Cyclic
concatenation gives the literal first row

```text
W_root^(L_1) S^(R_1) S^(L_1) S_A B_v^(L_1) -> S.  (4.1)
```

It has exactly three sides and records `x_v`.  The subsequent labels down
the lens black arm each see only the side created by the preceding closure:

```text
W_root^q S B_v^q -> S.                              (4.2)
```

They have distance one.  These rows consume the outer copies, not the lens
aggregate copies.  A decorated port preserves one white of each of its two
labels in the aggregate, so every surviving port remains unrecorded and
defaults to the final root.  `R_v=q_0` is supplied by the root complement
and also defaults.  Exactly one white of every label remains.

For a canonical residual `C_1=S^(L_1) W_1^(R_1) S_D S^(R_1)`, adjoining the
same complement already leaves one white of every label and no black token.
There is no final distance-three row, so `L_1,R_1` default to the root.

Forward chronology in the open final-root part is
`L_1,q_(s_r-2),...,q_1`; inverse chronology is the reverse.  The independent
guard stores each complete closure node and reconstructs the exact rotated
input word from the nodes in reverse, so the finite checks test inverse as
well as forward closure.

## 5. The new child `d`

At new rank the complete child block is

```text
W_1^alpha S^beta S^alpha W_d^beta S_d^(*) S^beta.
```

After its right suffix is one side, its forced rows are

```text
W_d^beta   S S S B_1^beta  -> S,
W_1^alpha S S S B_1^alpha -> S.                    (5.1)
```

Thus forward order is `beta,alpha`, inverse order is `alpha,beta`, and both
labels record `x_1`.

The pair lies wholly on the current-parent arm in all input classes.  For
direct initialization and contraction, the suffix ends at new-root position
`(s+2)-2=s`.  For expansion, the inherited retained width is at most `s-2`,
so the nonwrapping suffix contains the whole pair `(s-1,s)`.  For `C` input
it is an ordinary sibling macro.  It never touches the `x_v` lens arm.

## 6. Exhaustive root-input table

The literal calculations give:

| input at `a=1` | old output | new output | new child |
| --- | --- | --- | --- |
| direct CP-5 base, `p(v)=1` | `F_v(s)` | `F_v(s+2)` | closes to `x_1` |
| lens, old `r>s` | `F_v(s)` | `F_v(s+2)` | closes to `x_1` |
| lens, old `r<s` | `C_1` | `C_1` | closes to `x_1` |
| canonical `C_a` | `C_1` | `C_1` | closes to `x_1` |

For a path vertex above `v`, `r^+=r<=s-2`; for one below `v`,
`r^+=r+2>=s+4` when compared with the shifted root cut.  Hence the old/new
inequality is identical and the table is exhaustive.  Empty arms use empty
products.

Arbitrary root siblings, including post-wrap slots, are disjoint adjacent
pairs.  None straddles the edited cut, retained-path cut, or current-root
cut; those slots belong to `v`, the path child, and the root.  Each sibling
therefore uses the accepted `R_h,L_h` two-row macro on one complete arm.

## 7. Individual ports and first crossing

For a direct child `h` of `v`:

1. `t(h)` above the initialization width closes `R_h,L_h` there.
2. Otherwise it remains literal until the first contraction with new width
   below `t(h)`, or until the first expansion; that row closes `R_h,L_h` to
   the current parent.
3. If no such event occurs, then `h>v`, and its `W_v^(L_h),W_h^(R_h)`
   representatives survive to the final root.

Equation `(3.1)` preserves each inequality and therefore the identity of
the first crossing parent.  In particular, for a decreasing path a smaller
child `h<v` closes at the first parent `b<h`, which can be nonroot.  It is
incorrect to assign all such ports to `x_1`; M273 does not make that error.

At the final open cut,

```text
t(h)<s  iff h>v,
t^+(h)<s+2 iff h>v.
```

Thus precisely the larger direct-child ports survive.  Forward macro order
is `R_h,L_h`; inverse order is `L_h,R_h`.  Contraction's special rows have
forward order `L_a,R_a`, expansion's have `L_a,R_a,R_v`, and the inverse
order reverses each list after later complete nodes are reopened.

## 8. Inherited labels and path classification

The inherited labels `1,...,m-2` are exhausted by canonical pruned slots,
strict path slots, `L_v,R_v`, and the direct-child ports above.  M250/M254
fixes canonical endpoints; M269/M271 fixes strict-path special endpoints;
`(3.1)` couples all those rows.  Therefore:

```text
sealed: b_(d+1)(q)=b_d(q) for every 1<=q<=m-2;

open:   q in E_v     => (b_d(q),b_(d+1)(q))=(d,d+1),
        q not in E_v => b_(d+1)(q)=b_d(q),

E_v={R_v} union {L_h,R_h : v<h<d and p(h)=v}.       (8.1)
```

The state is open at the root exactly for a strictly decreasing numerical
path.  Below `v`, numerical descent is cyclic-width contraction and ascent
is expansion.  A transition from below `v` to above it is a contraction,
but any later return to the below/root arc forces an expansion.  Since every
path ends at `1`, a nondecreasing path either expands internally or expands
in the root row.  Conversely, a strictly decreasing path contracts at every
step.  This validates M273's classification without a one-bit direction
premise.

## 9. Root endpoint tables and boundary cases

The open top rows are

```text
old: W_d^alpha       S^beta  S^alpha S_A B_v^alpha -> S,
new: W_(d+1)^gamma   S^delta S^gamma S_A B_v^gamma -> S.
```

Combining them with `(5.1)` and final-root defaults gives

```text
open:
  b_d(alpha)=v,       b_d(beta)=d,
  b_(d+1)(alpha)=1,   b_(d+1)(beta)=1,
  b_(d+1)(gamma)=v,   b_(d+1)(delta)=d+1;

sealed:
  b_d(alpha)=d,       b_d(beta)=d,
  b_(d+1)(alpha)=1,   b_(d+1)(beta)=1,
  b_(d+1)(gamma)=d+1, b_(d+1)(delta)=d+1.           (9.1)
```

At `v=d-1`, `s=2`, `s^+=4`, and no inherited larger child exists.  The new
child is positions `(1,2)`, the new root is `(3,4)`, and all omitted arms are
empty.  The same rows remain literal.  Direct-root `p(v)=1`, empty sibling
sets, empty port sets, and every post-wrap pair were separately covered.

## 10. Independent exact guard

`guard.py` imports no M273 or predecessor code/data.  It independently emits
the full hairy contour, cycle-linearizes it, performs LIFO closure, records
distance-one/three rows, and stores complete closure nodes whose recursive
expansion reconstructs the original token word.

Five targeted rows cover direct-root `v=d-1`, direct-root ports on both
sides of the cut, root contraction with a smaller port closing at nonroot
`x_3`, root expansion with a port, and already sealed `C`.  It then checks
every prescribed-root tree at `d=5,6` and every ordinary edit:

```text
trees: 16 at d=5, 125 at d=6
rows: 548
open / closed: 341 / 207
root inputs:
  direct-root 224, F contraction 117, F expansion 136, C 71
failures: 0
targeted digest: 567028761cbca5b5dc65fb41b3e32e29ae837ac6a599bd40f0bb6e6d957d4ae4
census digest:   376cb40fb0841155aabdf001a275fe742f7d08958f20856b2db900e7b9fae3b3
```

It also independently recomputed M273's frozen four-row normalized digest
as

```text
922fca4abe3fce67064cb5e5963a69ee222f4fa2fa2c6f89f110a5b0c62e1695.
```

These are exact finite calibrations only.  Sections 3--9 provide the
arbitrary-rank proof.

## 11. Formal downstream composition

The claimed dependency chain is **licensed**, with one wording discipline:
M250 `(4.2)` remains refuted and is replaced, not repaired by fiat.

1. M269/M271 proves the literal decorated-width initialization and every
   strict internal CP-2 row.
2. Accepted DL-RST proves the exhaustive root row and final completion.
   Together they give exactly the endpoint output M250 `(4.3)--(4.5)` and
   the decreasing/open versus nondecreasing/sealed dichotomy.
3. M250/M254's accepted coordinate proof uses those endpoint outputs,
   metric pruning, and the absolute common-nonchild endpoint.  It therefore
   now proves M240's ordinary-edit IDL.  No premise from false `(4.2)` is
   needed.
4. M240/M242 then proves, for every ordinary odd edit
   `i=2v-3`, `2<=v<=d-1`, the route-normal endpoint identity.  The open
   route is `Q(v,epsilon) B_d Q(v,epsilon)^(-1)` and has exact length

   ```text
   4(d-v-1)+5 <= 4d-7.
   ```

   The sealed endpoint is already equal and needs no route.

Thus ordinary odd-edit IDL and its route are no longer conditional on the
root seam.  They remain only one routing family inside the larger mixing
program.

## 12. Numbered objections and qualifications

### Material objections

None.

### Nonmaterial qualifications

1. **N-1 (partition wording).**  M273 Section 7's phrase “a canonical
   off-path slot” overlaps literally with a direct child of `v`.  In the
   exhaustive list it should read “a canonical off-path slot eliminated by
   pruning or a sibling macro”; retained direct-child slots are the separate
   item 5.  Sections 5 and 7 already prove the direct-child alternatives, so
   this is not a missing case.
2. **N-2 (inverse chronology is mostly implicit).**  M273 explicitly gives
   the new-child inverse and invokes complete-node commutation for the other
   rows, but does not list the final-root inverse order.  Section 4 above
   supplies it, and the independent guard reconstructs every full input.
   No endpoint or legality claim changes.

```text
PROVED AND ACCEPTED:
  standalone DL-RST;
  exact open/sealed inherited and root endpoint tables;
  M269/M271 + DL-RST => ordinary odd-edit IDL;
  ordinary odd-edit route-normal closure with length <=4d-7.

STILL REFUTED:
  M250 (4.2) as a coarse one-bit transition rule.

STILL OPEN:
  fixed edits; every-color synchronization; voltage correction;
  all other routing and congestion obligations; spectral gap;
  polynomial mixing; Terminal A or Terminal B.
```
