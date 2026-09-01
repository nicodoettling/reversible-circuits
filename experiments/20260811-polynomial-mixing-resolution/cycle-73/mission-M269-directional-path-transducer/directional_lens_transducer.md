# M269 directional lens transducer

Date: 2026-08-14 UTC. Status: **proved exact full CP-2 internal-row
transducer with canonical sibling gadgets and direct-child ports; the
rank-dependent `a=1` row and RST remain unresolved**.

## 1. Immutable gate, convention, and scope

The accepted source inventories are locked in `checkpoint.md`. Only the
M260-accepted M257 contexts CP-1--CP-6, the M254-accepted M250 metric
canonical pruning, and the M265-accepted M262 counterfamily are used. The
bare `O -> C` rule refuted by M262 is not a premise.

Fix `rho>=5` and an ordinary edit vertex `2<=v<=rho-1`. At rank `rho`, put
`M=2rho-2`. White rotations increase and black rotations
decrease. A complete row is

```text
W_u^q S^e B_b^q -> S,             e in {1,3},        (1.1)
```

and only `e=3` records second black endpoint `x_b`. This note treats the
deterministic DPS closure. There is no probability distribution or Markov
kernel. Every theorem below stops at a strict internal parent `b!=1`; the
changing root modulus, the new child `d` at `1`, and final root completion
remain assigned to RST.

## 2. Cyclic coordinates and literal gadgets

Fix the edited vertex `v`. Let

```text
q_j = 1 + ((R_v-1+j) mod M),       0<=j<=M-1.         (2.1)
```

Thus `q_0=R_v` and `q_(M-1)=L_v`. For every canonical vertex `h!=v`, define
the unique position `t(h)` by

```text
R_h=q_(t(h)),       L_h=q_(t(h)-1),
1<=t(h)<=M-1.                                      (2.2)
```

All `t(h)` are even in the cyclic slot order. In particular no canonical
two-label slot straddles the cut at `q_0`.

After accepted off-path pruning, a canonical child `h` of a current parent
`b` occupies the literal six-token gadget

```text
G_b(h) =
 W_b^(L_h) S^(R_h) S^(L_h) W_h^(R_h) S_h^(*) S^(R_h).
                                                               (2.3)
```

This is the parent white `L_h` token, the crossing `S^(R_h)`, and M250's
four-token residual for `I_h`. If a processed suffix contributes one side
immediately after this gadget, then

```text
W_h^(R_h) S S S B_x^(R_h) -> S,
W_b^(L_h) S S S B_x^(L_h) -> S.                    (2.4)
```

Both rows have distance three, both record `x`, and the gadget, suffix side,
and the two descending black tokens reduce to one side. This **macro lemma**
is literal: the first row sees `S_h^(*)`, `S^(R_h)`, and the processed suffix;
the second sees `S^(R_h)`, `S^(L_h)`, and the first closure side. It is valid
with `x=v` or `x=b`.

Because the slot positions are disjoint adjacent pairs, any collection of
gadgets wholly contained in a monotone cyclic interval may be substituted
for the corresponding ordinary two-label rows. Process from the interval's
right end. Each ordinary label uses one side and (1.1) with `e=1`; each
gadget uses (2.4) and again leaves one side. This proves an arbitrary-length
interval induction and includes every post-wrap child.

## 3. The actual open state

Let `D_v` be the set of canonical rooted children of `v`. For
`1<=r<=M-1`, define `A_v(r)` from the increasing word

```text
W_v^(q_1) W_v^(q_2) ... W_v^(q_r)                  (3.1)
```

by replacing the adjacent pair at positions `t(h)-1,t(h)` by

```text
W_v^(L_h) S^(R_h) S^(L_h) W_h^(R_h) S_h^(*) S^(R_h)
                                                               (3.2)
```

for every `h in D_v` with `t(h)<r`. Equality `t(h)=r` cannot occur when
`r=t(a)` for a path ancestor `a`: one vertex cannot be both a rooted child
and a parent of `v`.

The **decorated lens frontier** of cyclic width `r` is

```text
F_v(r) =
 S^(q_(r-1)) S_A
 B_v^(q_(r-1)) B_v^(q_(r-2)) ... B_v^(q_1)
 S^(q_0)
 A_v(r)
 S_C S^(q_r).                                      (3.3)
```

`S_A,S_C` are actual closure sides, not empty placeholders. Each child
`h in D_v` with `t(h)<r` contributes a literal port (3.2), together with the
still present black tokens `B_v^(R_h),B_v^(L_h)` on the opposite arm.

For a strict path vertex `a`, write

```text
r_v(a)=t(a)=(R_a-R_v) mod M.                        (3.4)
```

The old directional tags are visible but are only projections:

```text
a>v  => O^+ with r_v(a)=2(a-v),
a<v  => O^- with r_v(a)=M-2(v-a).                   (3.5)
```

The sealed interface at a canonical vertex `b` is

```text
C_b = S^(L_b) W_b^(R_b) S_D S^(R_b),               (3.6)
```

the literal M250 canonical residual.

## 4. Full internal-row theorem

### Theorem 4.1 (decorated cyclic-width transducer; **PROVED**)

Apply accepted pruning to every canonical off-path child excursion. Allow
arbitrary canonical siblings of the retained path child, in their actual
cyclic order, including children reached after wrap.

1. **Initialization.** Suppose `a=p(v)!=1` and insert the reversed CP-5
   excursion at `v` into the full CP-2 row at `a`. Put `r=r_v(a)`. Complete
   bottom-up deletion leaves exactly `F_v(r)`. A direct child `h` of `v`
   persists as a port exactly when `t(h)<r`; if `t(h)>r`, both of its slot
   labels close at distance three against `x_a`. The label `L_v=q_(M-1)`
   closes at distance three against `x_a`.

2. **Open transition.** Suppose a processed path child `a` presents
   `F_v(r)` to a strict internal parent `b=p(a)!=1`, and put `s=r_v(b)`.
   Then

   ```text
   s<r  =>  F_v(r) -> F_v(s),
   s>r  =>  F_v(r) -> C_b.                          (4.1)
   ```

   In the contraction row `s<r`, the special distance-three rows are

   ```text
   L_a=q_(r-1) against B_v^(L_a), recording x_v;
   R_a=q_r     against B_b^(R_a), recording x_b.    (4.2)
   ```

   Ports with `t(h)<s` persist. Ports with `s<t(h)<r` disappear through
   two distance-three rows against `x_b`.

   In the expansion row `s>r`, the special rows are (4.2) and

   ```text
   R_v=q_0 against B_b^(R_v), recording x_b.        (4.3)
   ```

   Every port in the incoming lens disappears through two distance-three
   rows against `x_b`.

3. **Sealed transition.** If the processed path child presents `C_a`, the
   full CP-2 row leaves `C_b`. The two slot labels `L_a,R_a` close at
   distance three against `x_b`; no defect lens reopens.

For every canonical sibling `h` of the retained child, its slot pair belongs
wholly to one of the two row arms. If its gadget is paired with the lens
black arm, both rows record `x_v`; if paired with the current-parent black
arm, both record `x_b`. All remaining ordinary rows have distance one.

#### Proof of initialization

In the `q` coordinates, CP-5 at `v` has black arm

```text
B_v^(q_(M-2)) ... B_v^(q_1) S^(q_0)                (4.4)
```

followed by the increasing white aggregate at `v` from positions `1` through
`M-1`, then `S^(q_0)S^(q_(M-1))`. Direct children of `v` appear in that
aggregate precisely as (3.2).

The path incidence seen at `a` is CP-1's `L_v=q_(M-1)`. The parent prefix
therefore supplies positions `r,...,M-2`; starting at the path cut, they
close against (4.4) from `M-2` down to `r`. Ordinary labels use distance one.
Any sibling gadget of `a` wholly in that arm uses (2.4) with `x=v`. The
result is one side followed by the remaining lens black arm
`B_v^(q_(r-1))...B_v^(q_1)`.

From the other end, the parent suffix supplies positions
`0,1,...,r-2`. It and every sibling gadget in that arm reduce against the
current-parent black word, leaving one processed suffix side. Then
`W_v^(q_(M-1))` sees, in order, the two CP-5 return sides and that suffix
side, so it closes at distance three against `B_a^(q_(M-1))`. Continue
downward through positions `M-2,...,r+1`.

A direct-child gadget at position `t>r` is now followed by one processed
side and invokes (2.4) with `x=a`, so it disappears and records `x_a` twice.
If `t<r`, the later parent-suffix whites at positions `t-1,t` have already
consumed the corresponding `B_a` tokens. The direct-child gadget and the
opposite `B_v` tokens therefore remain as a port. The two cases exhaust the
disjoint slot pairs; none straddles `r` or `q_0`. The residual is exactly
(3.3).

#### Proof of the contraction row

Assume `s<r`. In CP-2 the prefix from `L_b=q_(s-1)` to the path incidence
`R_a=q_r` occupies positions `s,...,r-1`. At its right boundary,

```text
W_b^(q_(r-1))
 S^(q_r) S^(q_(r-1)) S_A
 B_v^(q_(r-1))                                     (4.5)
```

is a distance-three row, proving the first line of (4.2). Moving left,
ordinary positions and sibling gadgets reduce by the interval induction.
This removes exactly positions `s,...,r-1` and leaves the lens black arm
through position `s-1`.

The suffix after the path hole occupies

```text
r+1,...,M-1,0,1,...,s-2.                            (4.6)
```

Reduce it from its right end, using (2.4) for every sibling gadget. Its one
remaining side follows the two terminal sides of `F_v(r)`, so

```text
W_v^(q_r) S_C S^(q_r) S B_b^(q_r) -> S             (4.7)
```

has distance three and proves the second line of (4.2). Continue through
positions `r-1,...,s+1`. A direct-child port with `s<t(h)<r` is removed by
(2.4) against `x_b`; a port with `t(h)<s` is shielded by the later suffix
tokens of the same labels and remains literal. What survives is precisely
the black arm, aggregate, and four sides in `F_v(s)`.

#### Proof of the expansion row

Assume `s>r`. The parent prefix now wraps and occupies

```text
s,...,M-1,0,1,...,r-1.                              (4.8)
```

Equation (4.5) and the first interval induction again remove positions
`r-1,...,1`. The nonwrapping suffix `r+1,...,s-2` reduces from the other end;
(4.7) then removes position `r`, followed by positions `r-1,...,1` of the
lens white aggregate. Direct-child ports use (2.4) against `x_b` in this
second pass.

Exactly three sides now lie between the prefix token and parent black token
at the exposed cut:

```text
W_b^(q_0) S S^(q_0) S B_b^(q_0) -> S.              (4.9)
```

This is (4.3). The remaining wrapped prefix positions
`M-1,...,s+1` reduce by the interval induction. The sole unmatched parent
white is `W_b^(q_s)=W_b^(R_b)`, and the residual is exactly `C_b`.

The sealed-input statement is the same macro induction with the retained
child interface already equal to (3.6); it is also the local child step in
M250's accepted metric canonical pruning. Every deleted interval above is a
complete dependency node, so accepted complete-node commutation licenses the
chosen bottom-up order. This proves all clauses. QED.

## 5. Direction alone is insufficient at arbitrary rank

The cyclic width, not merely the sign in (3.5), decides (4.1). This failure
already occurs with no direct-child ports and no siblings.

### `O^+` pair

For every `rho>=9`, let `v=4`, `b=6`, and choose `a` equal to `5` or `7`.
Use tree edges

```text
{1,rho}, {1,6}, {6,a}, {a,4},
{1,u} for every unused 2<=u<=rho-1.                 (5.1)
```

The stopped path begins `4 -> a -> 6 -> 1`, and both incoming states at
`a` are `O^+`. Their widths are

```text
a=5: r=2,     b=6: s=4,     so expansion gives C_6;
a=7: r=6,     b=6: s=4,     so contraction gives F_4(4).      (5.2)
```

### `O^-` pair

For every `rho>=9`, let `v=6`, `b=3`, choose `a` equal to `2` or `4`, and
use

```text
{1,rho}, {1,3}, {3,a}, {a,6},
{1,u} for every unused 2<=u<=rho-1.                 (5.3)
```

Both incoming states are `O^-`, but

```text
a=2: r=M-8,   b=3: s=M-6,   so expansion gives C_3;
a=4: r=M-4,   b=3: s=M-6,   so contraction gives F_6(M-6).    (5.4)
```

The edge sets have `rho-1` edges, are connected, have root leaf `rho`, and
the displayed rows are strict internal CP-2 rows. Equations (5.2)--(5.4) are
all-rank consequences of Theorem 4.1, not finite interpolation. Thus neither
`O^+` nor `O^-` is a sufficient state without the cyclic-width/literal-port
data.

## 6. Exact stop and first open lemma

Theorem 4.1 resolves the internal CP-2 recurrence only. It does not enter
the rank-dependent `a=1` row. In particular, it does not evaluate the old
`(alpha,beta)` slot, the new `(gamma,delta)` slot, the new canonical child
`d`, or final root defaults.

The first remaining lemma in this lane is therefore:

> **DECORATED-LENS ROOT-SEAM TABLE (DL-RST; UNRESOLVED).** Couple ranks
> `d,d+1` using M257 CP-6. Its input is the actual state delivered by
> Theorem 4.1: the reversed CP-5 base if `p(v)=1`, a decorated lens `F_v(r)`
> if no internal expansion occurred, or `C_a` if one did. Apply the two
> explicit `a=1` contexts, including the new child `d` at position
> `R_d=beta`, and perform final root completion. Prove the complete
> inherited-label endpoint comparison and the sealed/open root four-blocks
> required by M250 `(4.3)--(4.5)`, with every persistent direct-child port
> exhausted explicitly.

This input is literal and falsifiable. A first counterexample is a named
port or ordinary inherited label with the wrong `1/3` side count, the wrong
black endpoint, or an unconsumed token after root completion.

Empty cyclic arms and empty child sets are allowed throughout. Distinct path
vertices have distinct even widths, so the omitted case `s=r` cannot occur.
The cases `p(v)=1` and `b=1` are intentionally inputs to DL-RST, not hidden
boundary cases of Theorem 4.1. The theorem is valid separately at each rank;
it does not by itself assert a two-rank endpoint comparison.

```text
PROVED:
  exact decorated lens state;
  full strict-internal CP-2 initialization and transition;
  arbitrary canonical siblings, post-wrap slots, and direct-child ports;
  cyclic contraction versus expansion rule;
  all-rank O+ and O- insufficiency families.

UNRESOLVED:
  DL-RST at a=1 and final root completion;
  hence RSPT, repaired RSMI+, IDL, and all-rank ordinary-edit Z2.

NOT CLAIMED:
  fixed edits; every-color synchronization; route length or congestion;
  a spectral gap; polynomial mixing; Terminal A or Terminal B.
```
