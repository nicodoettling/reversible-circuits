# M271 fresh proof audit of frozen M269

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

**ACCEPT** M269's decorated cyclic-width transducer for every strict
internal CP-2 path row, including canonical sibling gadgets, post-wrap
slots, and direct-child ports.

Material objections: **none**.

The acceptance stops before the rank-dependent `a=1` context and final root
completion.  It accepts no DL-RST, old CPR, RSPT, repaired RSMI+, IDL,
routing theorem, routing-length bound, spectral gap, mixing theorem, or
Terminal conclusion.

## 2. Immutable gates and dependency boundary

Every entry in each frozen inventory verifies.  The independently computed
digests of the inventory files are

```text
M269  c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
M262  eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a
M265  ced42bf8a6ccd7ca9ffffdca94919c366273b712875cfe08eeead393b88193f8
```

The dependency boundary is sound.  M250/M254 supply exact metric canonical
pruning, its literal residual, and complete-node commutation.  M257/M260
supply only the raw cyclic contexts CP-1--CP-6.  M262/M265 refute the old
one-bit `O -> C` CPR rule and motivate, but do not prove, a refinement.  I
used none of M269's transition claims as a premise.

There is no probability law or Markov kernel in this local theorem.  The
ambient project target remains the uniform law on fixed-length identity
words for the lazy exact same-product `{3,4,5}` heat-bath chain; this audit
does not advance its gap directly.

## 3. Coordinates, slot boundaries, and the literal child macro

Put `M=2rho-2` and cut the cyclic labels at `q_0=R_v`, with

```text
q_j = 1 + ((R_v-1+j) mod M).
```

For a canonical nonroot slot `h!=v`, `R_h-R_v` is even modulo the even
modulus `M`.  Hence its unique position `t(h)` lies in
`{2,4,...,M-2}`, and

```text
L_h=q_(t(h)-1),        R_h=q_(t(h)).
```

The ordinary slot is therefore exactly the adjacent pair
`(t(h)-1,t(h))`.  A canonical gadget could straddle the edited cut only if
`t=0`, the retained-path cut only if `t=r`, or the current-parent cut only
if `t=s`.  Those slots belong, respectively, to `v`, the path child `a`, and
the current parent `b`; none can be a canonical sibling or a direct child of
`v`.  This proves the arm partition, including post-wrap pairs.  Empty
intervals cause no exceptional row.

Substituting M250's accepted residual

```text
I_h -> S^(L_h) W_h^(R_h) S_h^(*) S^(R_h)
```

after the parent crossing and the last parent white before that crossing
gives the literal six-token block

```text
W_b^(L_h) S^(R_h) S^(L_h) W_h^(R_h) S_h^(*) S^(R_h).
```

If a processed suffix contributes one side and the opposite black arm is
`B_x^(R_h) B_x^(L_h)`, the forced deletion chronology is

```text
W_h^(R_h) S_h^(*) S^(R_h) S_suffix B_x^(R_h) -> S_R,
W_b^(L_h) S^(R_h) S^(L_h) S_R B_x^(L_h)       -> S_L.
```

Both rows have exactly three intervening sides and both record second black
endpoint `x`.  Thus the forward chronology is `R_h` then `L_h`, while the
inverse chronology is `L_h` then `R_h`.  Processing disjoint slot pairs from
the right end proves the arbitrary-length sibling interval induction.

## 4. Bare and decorated lens

With no direct child port, the exact bare residual after the initial path
row is

```text
S^(q_(r-1)) S_A
B_v^(q_(r-1)) ... B_v^(q_1)
S^(q_0)
W_v^(q_1) ... W_v^(q_r)
S_C S^(q_r).
```

For a rooted child `h` of `v` whose pair lies below the width, replace the
two whites at `t(h)-1,t(h)` by the six-token child block.  The opposite
`B_v` pair remains on the black arm.  This is exactly M269's `A_v(r)` and
decorated `F_v(r)`.  Equality `t(h)=r` is impossible because `h` cannot be
both a rooted child and the path ancestor occupying that slot.

No hidden side is suppressed: the two leading sides are the parent
`L`-side and the prefix-closure side; the middle `S^(q_0)` is the edited
child-side crossing; and the two terminal sides are the suffix-closure side
and the parent `R`-side.

## 5. Initialization, including direct ports and siblings

Let `a=p(v)!=1` and `r=t(a)`.  CP-1 puts the retained incidence at
`L_v=q_(M-1)`, not `R_v`.  The parent prefix occupies positions
`r,...,M-2`; deleting it from the path cut consumes the edited black arm
from `M-2` down through `r`.  Ordinary pairs have distance one, while every
canonical sibling block wholly in this arm uses the two-row macro against
`B_v` and records `x_v` twice.

The parent suffix occupies `0,...,r-2` and deletes against the current-parent
black arm.  Its sibling blocks record `x_a` twice.  Its surviving side joins
the two CP-5 return sides, so

```text
W_v^(q_(M-1)) S S S B_a^(q_(M-1)) -> S
```

is the special distance-three `L_v` row and records `x_a`.

Now descend through the edited white aggregate.  If a direct child has
`t(h)>r`, its current-parent black pair is still present and its `R_h,L_h`
rows delete, in that order, at distance three to `x_a`.  If `t(h)<r`, the
parent suffix has already consumed those two `B_a` tokens while the
corresponding `B_v` tokens remain below the width.  The child gadget
therefore remains literally as a port.  These cases exhaust the disjoint
even slot pairs and leave exactly `F_v(r)`.

The chosen inverse insertion chronology reverses these complete-node
deletions: reopen discharged direct-child blocks from the residual outward,
using `L_h` before nested `R_h`, reopen the special `L_v` row, then undo the
suffix and prefix chains.  Persistent ports are never reopened because they
were never deleted.  Complete-node commutation licenses this exact reversal.

## 6. Contraction `F_v(r) -> F_v(s)` for `s<r`

Let `b=p(a)!=1`, `r=t(a)`, and `s=t(b)<r`.  The parent prefix occupies
positions `s,...,r-1`.  At its right boundary the literal row is

```text
W_b^(q_(r-1)) S^(q_r) S^(q_(r-1)) S_A
B_v^(q_(r-1)) -> S.
```

It has distance three, is the `L_a=q_(r-1)` row, and records `x_v`.
The prefix interval then consumes the lens black arm down through position
`s`, leaving the arm through `s-1`.  Sibling gadgets on this arm record
`x_v` twice.

The suffix after the path hole is the cyclic interval
`r+1,...,M-1,0,1,...,s-2`.  Delete it from its right end; its sibling
gadgets record `x_b` twice and it leaves one side.  The next row is

```text
W_v^(q_r) S_C S^(q_r) S_suffix B_b^(q_r) -> S.
```

It has distance three, is the `R_a=q_r` row, and records `x_b`.
Continuing down the lens aggregate removes positions through `s+1` against
`B_b`.  A port with `s<t(h)<r` consequently deletes via `R_h,L_h` to
`x_b`; a port with `t(h)<s` lies outside this interval and remains literal.
The four boundary sides, shortened black arm, and shortened decorated white
aggregate are exactly `F_v(s)`.

The relative special-row chronology is `L_a` before `R_a`; the inverse row
opens `R_a` before `L_a`, with every removed port opened `L_h` then `R_h`
in the globally reversed interval order.  This reconstructs the original
word without changing any recorded black endpoint.

## 7. Expansion and sealed propagation

### Expansion `s>r`

The parent prefix wraps through positions
`s,...,M-1,0,1,...,r-1`.  Its boundary with the lens gives the same
distance-three `L_a` row to `x_v`.  After the nonwrapping suffix
`r+1,...,s-2` has reduced, the same terminal calculation gives the
distance-three `R_a` row to `x_b`.

The second pass consumes the full decorated aggregate through position one.
Every incoming direct-child port therefore deletes by `R_h,L_h` against
`x_b`.  At the remaining edited cut,

```text
W_b^(q_0) S S^(q_0) S B_b^(q_0) -> S
```

has exactly three sides, so `R_v=q_0` records `x_b`.  The remaining wrapped
prefix deletes by the same interval induction.  Its sole unmatched white is
`W_b^(q_s)=W_b^(R_b)`, and the exact residual is

```text
C_b = S^(L_b) W_b^(R_b) S_D S^(R_b).
```

Sibling blocks paired to the lens arm record `x_v`; all other sibling
blocks record `x_b`.  All ordinary rows have distance one.  The relative
special chronology is `L_a`, then `R_a`, then `R_v`; inverse insertion sees
them in the opposite order, with the globally later high-prefix deletions
undone first and every child macro reopened `L_h` then `R_h`.

### Sealed input

For input `C_a`, the retained child block is exactly the accepted canonical
child macro.  The `R_a` row deletes first and the `L_a` row second; both have
distance three against `B_b` and record `x_b`.  Every canonical sibling
block does the same.  One parent survivor `W_b^(R_b)` remains, so the output
is exactly `C_b`; no edited lens token can reopen.  The inverse macro opens
`L_a` before `R_a`.

The complete distance-three endpoint ledger is therefore:

| row | labels | recorded black endpoint |
| --- | --- | --- |
| initialization special | `L_v` | `x_a` |
| initialization discharged direct port | `R_h,L_h` | `x_a,x_a` |
| contraction special | `L_a,R_a` | `x_v,x_b` |
| contraction discharged direct port | `R_h,L_h` | `x_b,x_b` |
| expansion special | `L_a,R_a,R_v` | `x_v,x_b,x_b` |
| expansion discharged direct port | `R_h,L_h` | `x_b,x_b` |
| sealed retained child | `R_a,L_a` | `x_b,x_b` |
| any sibling gadget | `R_h,L_h` | the black arm paired with the gadget |

This matches every endpoint asserted by M269.  Every unlisted local row is
distance one.

## 8. Direction-insufficiency families and finite guards

For the `O^+` pair, the edge set in M269 has `rho-1` edges and consists of
the path `4--a--6--1--rho` plus leaves at `1`, so it is a tree rooted at the
leaf `rho`.  At `v=4`,

```text
a=5: r=2<s=4  -> C_6,
a=7: r=6>s=4  -> F_4(4).
```

Both incoming current vertices are above `v`, yet the outputs differ.

For the `O^-` pair, the corresponding tree is the path
`6--a--3--1--rho` plus leaves at `1`.  At `v=6`,

```text
a=2: r=M-8<s=M-6  -> C_3,
a=4: r=M-4>s=M-6  -> F_6(M-6).
```

Both incoming current vertices are below `v`, yet the outputs differ.  The
edge count, connectivity, root leaf, parent maps, and strict-internal status
hold symbolically for every `rho>=9`.  Thus the universal insufficiency is
analytic, not inferred from finite ranks.

The clean-room script `cleanroom_lens_guard.py` imports no predecessor code
or data, chooses the rightmost rather than leftmost complete node, and forces
every endpoint vertex to agree with its canonical slot.  It checks exactly
M269's four declared schemas at `rho=15` and the four witness rows at
`rho=9`.  All eight pass.  Its normalized-result digest is

```text
9b6514b809c63648ed350496e78580ddc88c632ad72a9c28fa2bd0b645ddf29e.
```

The raw result file has SHA-256
`61f088b43acbcf9cb0b30d0fd939b7a66bb1f8b089ef929597462168c2fce7c5`.
This is finite calibration only; the interval and slot-partition arguments
above carry every rank and every admissible sibling set.

## 9. Objections, qualifications, and exact stop

### Material objections

None.

### Nonmaterial qualifications

1. **N-1 (predecessor guard is schematic).**  M269's own four-row script
   assigns some decorative vertex names independently of their normalized
   slot positions.  It is therefore best read exactly as advertised: a
   symbolic token-schema guard, not an admissible full-tree instance.  This
   does not support the universal theorem, but the theorem is analytic; the
   slot-consistent clean-room guard independently passes the same four
   schemas.
2. **N-2 (domain wording).**  Section 2's phrase “every canonical vertex”
   should mean every canonical **nonroot slot**.  The root has no inserted
   black slot.  Every object quantified in Theorem 4.1 is already a rooted
   child or strict nonroot path vertex, so this wording does not omit a case
   or alter the result.

The first unresolved lemma is exactly M269's DL-RST: consume the literal
reversed base, a decorated `F_v(r)`, or a sealed `C_a` in the two explicit
rank-dependent CP-6 root contexts, include the new child `d`, and perform
final root completion.  M269 never enters `a=1`; its theorem is separately
valid at each rank and makes no two-rank endpoint comparison by itself.

```text
PROVED AND ACCEPTED:
  exact coordinate and decorated-lens state;
  initialization and every strict-internal CP-2 transition;
  complete sibling/post-wrap/direct-port treatment;
  all distance-three endpoints and inverse chronology;
  arbitrary-rank O+ and O- insufficiency families.

UNRESOLVED:
  DL-RST at a=1 and final root completion;
  hence RSPT, repaired RSMI+, IDL, and all-rank ordinary-edit Z2.

NOT CLAIMED:
  fixed edits; every-color synchronization; routing or route length;
  congestion; a spectral gap; polynomial mixing; Terminal A or B.
```
