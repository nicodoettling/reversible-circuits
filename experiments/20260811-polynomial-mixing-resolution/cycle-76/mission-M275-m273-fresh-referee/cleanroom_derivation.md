# M275 clean-room derivation fixed before inspecting M273

Date: 2026-08-14 UTC.  Independence status: **frozen before any M273
artifact was opened**.

## 1. Gate and conventions

The only inputs are the M260-accepted raw contexts CP-1--CP-6, the
M254-accepted metric canonical-child macro and complete-node commutation,
and the M271-accepted M269 strict-internal decorated-lens theorem.  No M273
statement, code, or data is used here.

At rank `rho` put `M=2rho-2`.  White rotation increases, black rotation
decreases, and

```text
W_u^q S^e B_b^q -> S,              e in {1,3},
```

records second black endpoint `x_b` exactly for `e=3`.  A label with no
distance-three row has the final root black as second endpoint.

Fix `d>=5`, `2<=v<=d-1`, and write

```text
m=2d-2,  alpha=m-1, beta=m, gamma=m+1, delta=m+2.
```

For the edited slot use cyclic coordinates

```text
q_j=1+((R_v-1+j) mod M),  q_0=R_v,
t(h)=(R_h-R_v) mod M.
```

Every ordinary nonroot slot is the adjacent even-ended pair
`(q_(t(h)-1),q_(t(h)))=(L_h,R_h)`.

## 2. Exact rank map at the seam

Let `s=2(d-v)`.  The old root slot and the new child/root slots are

```text
rank d:    (L_1,R_1)=(alpha,beta)
           (t(L_1),t(R_1))=(s-1,s);

rank d+1:  child d: (L_d,R_d)=(alpha,beta), positions (s-1,s),
           root 1 : (L_1,R_1)=(gamma,delta), positions (s+1,s+2).
```

Thus the old root width is `s`, the new root width is `s^+=s+2`, and the
new child `d` occupies exactly the old root slot.

For every inherited nonroot slot `h!=v`, the new position is

```text
t^+(h)=t(h)       if h>v,
t^+(h)=t(h)+2     if h<v.                            (2.1)
```

The same rule holds for the width of every inherited path vertex.  Therefore
every strict comparison between a port position and a current path width is
preserved at the two ranks.  This remains true across the edited cut: a slot
above `v` and a path vertex below `v` lie respectively in the small and large
arcs at both ranks, and conversely.  Equality cannot occur: it would identify
the direct child with the path vertex.  The sole inserted pair is child `d`.

Consequently an inherited port persists through exactly the same contraction
rows at both ranks and is discharged at the same first width crossing, with
the same black endpoint.  Under a contraction `F_v(r)->F_v(r')`, a port with
`r'<t(h)<r` closes in the order `R_h,L_h`, both at distance three to the
current parent.  Under an expansion every incoming port closes in that same
order to the current parent.  Inverse insertion opens `L_h` before `R_h`.

## 3. Literal final-root calculation

Suppose the root CP-2 row leaves the open lens `F_v(s_r)`, where
`s_r=t(1)` at the current rank.  Its literal residual is

```text
S^(q_(s_r-1)) S_A
B_v^(q_(s_r-1)) ... B_v^(q_1)
S^(q_0) A_v(s_r) S_C S^(q_(s_r)).                  (3.1)
```

After the return side `S^(R_1)`, the unprocessed outer contour at the root
white vertex is

```text
W_root^(q_(s_r+1)) ... W_root^(q_(M-1))
W_root^(q_0) W_root^(q_1) ... W_root^(q_(s_r-1))
S^(R_1),                                             (3.2)
```

with empty intervals omitted.  In the cyclic word `(3.1)(3.2)`, the first
consecutive white/black pair is

```text
W_root^(q_(s_r-1))
 S^(R_1) S^(L_1) S_A
B_v^(q_(s_r-1)) -> S.                               (3.3)
```

It has exactly three sides.  Since `q_(s_r-1)=L_1`, this records `x_v` as
the second endpoint of `L_1`.  Thereafter, for
`j=s_r-2,s_r-3,...,1`, the row joining
`W_root^(q_j)` to `B_v^(q_j)` has only the side created by the preceding
closure and hence has distance one.

The half-edge projection makes the consequence transparent.  Before these
rows it is

```text
B_(s_r-1) ... B_1;
W_1 ... W_(s_r);
W_(s_r+1) ... W_(M-1) W_0 W_1 ... W_(s_r-1).
```

The final-root rows consume the *outer* copies
`W_(s_r-1),...,W_1` against the lens black arm.  They do not consume the
copies in `A_v(s_r)`.  A decorated direct-child port replaces the relevant
two `A_v` whites by two whites with the same labels plus sides, so it too
survives intact.  After `(3.3)` and the distance-one rows, exactly one white
of every label remains, as required by the DPS closure.  Hence:

- `L_1` records `x_v`;
- `R_1=q_(s_r)` has no distance-three row and defaults to the final root;
- every still-open label in the lens, including `R_v` and both labels of
  every surviving port, has no distance-three row and defaults to the final
  root;
- earlier distance-three records, such as the new-child records below, are
  unchanged.

Forward final-root chronology is `L_1,q_(s_r-2),...,q_1`; inverse chronology
is `q_1,...,q_(s_r-2),L_1`.  Persistent port tokens are never deleted in
this stage and therefore are not reopened.

For sealed residual

```text
C_1=S^(L_1) W_1^(R_1) S_D S^(R_1),                 (3.4)
```

adjoining `(3.2)` leaves one white token of every label and no black token.
There is no further local row.  Both `L_1,R_1` therefore default to the
final root.

## 4. Four complete input classes at the root

### 4.1 Direct-root reversed base, `p(v)=1`

Insert CP-5 directly in the CP-6 root context.  The same interval deletion
as the accepted initialization row applies with width `s_r=t(1)`: the root
prefix deletes the high edited-black arm, and the root suffix deletes the
current-parent arm.  It leaves exactly `F_v(s_r)`.

A direct child `h` of `v` persists iff `t(h)<s_r`.  For inherited vertices
this is exactly `h>v`; a child `h<v` closes in rows `R_h,L_h` to `x_1`.
The special `L_v` row also records `x_1`.  At rank `d+1`, the new sibling
child `d` has pair positions `(s-1,s)` inside the root suffix for width
`s+2`; its canonical macro closes `R_d=beta` and then `L_d=alpha`, both at
distance three to `x_1`.  The final-root calculation of Section 3 applies.

### 4.2 Decorated-lens contraction at the root

For incoming `F_v(r)` with `s_r<r`, the accepted contraction calculation is
still internal to the bridge-delimited root excursion and gives
`F_v(r)->F_v(s_r)`.  Its special rows are

```text
L_a -> x_v,       R_a -> x_1.
```

Ports below `s_r` persist; each port in `s_r<t(h)<r` closes `R_h,L_h` to
`x_1`.  Formula `(2.1)` makes the persistence and first-crossing discharge
identical at the two ranks.  In the new row, child `d` lies wholly in the
suffix ending at `s_r-2`; it closes `R_d,L_d` to `x_1`.  Section 3 then
finishes the open row.

### 4.3 Decorated-lens expansion at the root

For `s_r>r`, the accepted expansion calculation gives
`F_v(r)->C_1`.  Its special rows are

```text
L_a -> x_v,       R_a -> x_1,       R_v -> x_1.
```

Every incoming port closes `R_h,L_h` to `x_1`.  At the new rank the new
child has `t^+(d)=s=s_r-2`; because an inherited path child `a>v` has
`r<=s-2`, the entire child pair `(s-1,s)` lies in the nonwrapping suffix and
closes `R_d,L_d` to `x_1`.  The residual is `(3.4)`, so final root completion
is sealed.

### 4.4 Sealed input `C_a`

The retained child macro and every root sibling macro close `R_h,L_h` to
`x_1`, leaving `C_1`.  In particular the new child `d` records
`b(alpha)=b(beta)=1`.  Equation `(3.4)` then has no final-root
distance-three row.

For every macro in Sections 4.1--4.4, forward order is `R_h,L_h` and inverse
order is `L_h,R_h`.  Contraction's special forward order is `L_a,R_a`;
expansion's is `L_a,R_a,R_v`; inverse chronology reverses these lists after
undoing later rows.  The new-child inverse is therefore `L_d,R_d`, and the
final-root inverse is the reverse order stated in Section 3.

## 5. Endpoint tables

Sections 3--4 give, without an abstract one-bit path rule, the exact root
tables.

For a sealed input:

```text
b_d(alpha)=b_d(beta)=d,
b_(d+1)(alpha)=b_(d+1)(beta)=1,
b_(d+1)(gamma)=b_(d+1)(delta)=d+1.                 (5.1)
```

For an open input:

```text
b_d(alpha)=v,       b_d(beta)=d,
b_(d+1)(alpha)=1,   b_(d+1)(beta)=1,
b_(d+1)(gamma)=v,   b_(d+1)(delta)=d+1.            (5.2)
```

In the open case the labels that survive without a distance-three record
before the root are exactly

```text
E_v={R_v} union {L_h,R_h : h>v and p(h)=v}.
```

They default respectively to `x_d` and `x_(d+1)`.  Every other inherited
low label either belongs to the accepted common-nonchild class or closes at
the same first width crossing and to the same black endpoint under `(2.1)`.
In the sealed case every inherited exposed label has already closed at a
rank-stable endpoint.  Thus the endpoint conclusions of M250 `(4.3)--(4.5)`
follow from the decorated-width theorem plus this literal root calculation;
the refuted coarse transition table M250 `(4.2)` is neither asserted nor
used.

## 6. Path classification and boundary

An open lens reaches the root iff `P(v)` is strictly decreasing.  If all
path values are below `v`, width is increasing with the vertex value, so a
numeric descent is a width contraction and a numeric ascent is an expansion.
If the path enters the arc above `v`, the cyclic width becomes small; a later
return to the root arc forces an expansion.  Since the path ends at `1`, any
nondecreasing path has an expansion somewhere.  Once expansion produces
`C`, sealed propagation is permanent.  This proves the open/closed endpoint
split using the full width, not the refuted `O^+` or `O^-` projection.

At `v=d-1`, `s=2` and `s^+=4`.  No inherited child is larger than `v`, so
the direct-port set is empty.  The new child occupies positions `(1,2)` and
the new root occupies `(3,4)`; all interval statements above allow empty
arms.  The only open low label is `R_v=2d-4`, and `(5.2)` remains literal.

## 7. Conditional downstream consequence fixed for later audit

If a frozen standalone DL-RST proves exactly Sections 2--6, then accepted
M269/M271 plus DL-RST establish the **endpoint output** M250
`(4.3)--(4.5)` and the open/closed split, while replacing rather than
reviving false M250 `(4.2)`.  M250/M254's coordinate-exhaustion proof may
then be applied directly to obtain ordinary-edit IDL.  Accepted M240/M242
then give the chronological signed-Hurwitz route

```text
Q(v,epsilon) B_d Q(v,epsilon)^(-1)
```

of exact length `4(d-v-1)+5 <= 4d-7` for every ordinary odd edit.  This
composition still says nothing about fixed edits, every-color
synchronization, voltage correction, other routing obligations, congestion,
a spectral gap, polynomial mixing, or Terminal A/B.
