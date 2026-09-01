# M273 decorated-lens root-seam theorem

Date: 2026-08-14 UTC. Status: **proved as a standalone exact root theorem;
fresh immutable audit required before promotion or downstream use**.

## 1. Scope, convention, and immutable boundary

Fix `d>=5`. Let `T` be a tree on `[d]`, rooted at the leaf `d`, with
`{1,d}` an edge. Root extension adds `{1,d+1}` and roots the resulting tree
at `d+1`. Choose an ordinary odd edit at `2<=v<=d-1`. White rotations
increase, black rotations decrease, and a complete local row is

```text
W_u^q S^e B_b^q -> S,                 e in {1,3}.    (1.1)
```

Only `e=3` records second black endpoint `x_b`. If no distance-three row is
ever recorded for label `q`, DPS RandomQuad Step 4 gives it the final root
as second endpoint. Write that one-based endpoint as `b_d(q)`.

Every payload in M240/M242, M244/M247, M250/M254, M257/M260,
M262/M265, and M269/M271 verifies at the top inventory digests recorded in
`checkpoint.md`. The locked DPS PDF verifies at

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

The primary-source inputs used here are only Proposition 3, the increasing /
decreasing hairy-tree rotations, Lemma 2, and RandomQuad/Theorem 5. The
accepted mathematical inputs are M250/M254 metric canonical pruning and
complete-node commutation, M257/M260 raw contexts CP-1--CP-6, and M269/M271's
literal decorated transducer for strict internal CP-2 rows. The refuted bare
`O -> C` transition of M262 is not a premise.

There is no probability distribution or Markov kernel in this theorem. It
is a deterministic comparison of two DPS closures.

## 2. The two seam coordinate systems

Put

```text
m=2d-2,
alpha=m-1, beta=m, gamma=m+1, delta=m+2,
R_v=2v-2,
s=m-R_v=2(d-v).                                    (2.1)
```

At a rank with modulus `M`, cut the cyclic labels at the edited incidence:

```text
q_j=1+((R_v-1+j) mod M).                            (2.2)
```

Use a superscript `+` only when ambiguity between the two moduli matters.
Since `2<=v<=d-1`, one has `2<=s<=m-2`. At old rank `d`,

```text
q_(s-1)=alpha,       q_s=beta,
(L_1,R_1)=(alpha,beta).                             (2.3)
```

At new rank `d+1`, the old root `d` is the new canonical child of `1` and
the root slot moves two positions forward:

```text
(L_d,R_d)=(q_(s-1),q_s)=(alpha,beta),
(L_1,R_1)=(q_(s+1),q_(s+2))=(gamma,delta).          (2.4)
```

Thus no fresh coordinate is hidden at the seam: the new child occupies
exactly the old root slot, and the new root occupies the next slot.

For every inherited nonroot slot `h in {2,...,d-1}`, M269's cyclic position
obeys

```text
t^+(h)=t(h),       h>v,
t^+(h)=t(h)+2,     h<v.                             (2.5)
```

Indeed `t(h)` is `(R_h-R_v)` modulo the relevant modulus. Above `v` the
difference is positive and unchanged; below `v` it wraps once and therefore
increases with the modulus by two. It follows that the strict order of every
pair of inherited slot positions is unchanged: two positions on the same
side of the cut receive the same shift, while every above-`v` position lies
before every below-`v` position at both ranks. In particular:

- every internal contraction/expansion decision is the same at the two
  ranks;
- every direct-child port has the same persistence/discharge event; and
- whenever a port discharges, it records the same inherited current-parent
  black vertex.

The two added modulus labels in strict internal rows belong only to the
ordinary distance-one interval chains. The complete endpoint ledger in
M269/M271 therefore gives a rank-coupled strict-internal history, not merely
the same abstract state.

## 3. The exact full root contour

The bridge-delimited CP-2 context at `a=1` is preceded in the full contour by
the white-root complement. If the current root label is `R_1`, write

```text
U_root(R_1)=W_root(R_1 up_M R_1) S^(R_1),           (3.1)
```

where the open cyclic interval contains exactly one white half-edge of every
label except `R_1`, in increasing order. Thus the full remaining contour is
the cyclic concatenation

```text
U_root(R_1) [the reduced CP-2 excursion at 1].       (3.2)
```

This is the portion suppressed by every strict-internal transducer: after
all local black half-edges have closed, its remaining whites are exactly the
ones attached to the final root in RandomQuad Step 4.

At new rank the child `d` is an ordinary sibling of the retained path child
inside the CP-2 row at `1`. Its full literal six-token block is

```text
W_1^alpha S^beta S^alpha W_d^beta S_d^(*) S^beta.  (3.3)
```

After the cyclic suffix on its right has become one side, the forced macro
rows are

```text
W_d^beta   S_d^(*) S^beta S_suffix B_1^beta  -> S_beta,
W_1^alpha S^beta S^alpha S_beta   B_1^alpha -> S_alpha.       (3.4)
```

Both rows have distance three and record `x_1`. Their forward chronology is
`beta` then `alpha`; the inverse chronology is `alpha` then `beta`.

The new root position is `s+2`, while the child block ends at position `s`.
Consequently (3.3) lies wholly on the current-parent arm in every possible
root input:

- for direct-root initialization, the parent suffix ends at `(s+2)-2=s`;
- for contraction, the cyclic suffix ends at `(s+2)-2=s`;
- for expansion, the nonwrapping suffix ends there, and the retained slot
  has even position at most `s-2`; and
- for a sealed input it is an ordinary canonical sibling macro.

It can therefore never pair with the `x_v` lens arm. Equations (3.3)--(3.4)
are the exact source of

```text
b_(d+1)(alpha)=b_(d+1)(beta)=1                     (3.5)
```

in every case.

## 4. Exhaustive root-input transition lemma

Let `F_v^(M)(r)` be M269's literal decorated lens at modulus `M`, including
every direct-child port with `t(h)<r`, and let `C_a` be its literal canonical
residual. The following three cases are exhaustive.

### Lemma 4.1 (root CP-6 transition; proved)

1. **Direct-root reversed base.** If `p(v)=1`, inserting the CP-5 reversed
   base directly into the old/new CP-6 rows leaves

   ```text
   rank d:    F_v^(m)(s),
   rank d+1:  F_v^(m+2)(s+2).                       (4.1)
   ```

   At new rank, the child-`d` macro (3.4) occurs on the parent suffix.

2. **Decorated-lens input.** Suppose the last strict internal path vertex is
   `a`, and the paired incoming lenses have widths `r,r^+`. Then

   ```text
   r>s  =>  r^+>s+2 and the outputs are
             F_v^(m)(s), F_v^(m+2)(s+2);

   r<s  =>  r^+<s+2 and both outputs are C_1.        (4.2)
   ```

   Equality cannot occur because the path vertex `a` cannot occupy the root
   slot (or the new-child slot). At new rank, (3.4) occurs on the
   current-parent suffix in both subcases.

3. **Canonical input.** Paired inputs `C_a` both leave `C_1`; the new row
   also performs (3.4).                              (4.3)

Every other canonical sibling, including every post-wrap sibling, reduces
by M269's two-row child macro on the arm containing its complete slot pair.

#### Proof

The strict-internal proof of M269 Theorem 4.1 is an interval proof inside the
CP-2 word. It excludes `b=1` only because the rank-dependent slot and final
root complement were not evaluated there. At a fixed rank, `x_1` is still a
canonical nonroot slot, so the same literal prefix/suffix interval deletion
applies. We repeat its boundary facts rather than extending the theorem by
name.

For initialization, the path incidence is `L_v=q_(M-1)`. Parent-prefix
deletion removes the edited black arm above the current-parent width, while
parent-suffix deletion removes the current-parent black arm below it. The
special `L_v` row has three sides and records `x_1`. What remains is exactly
the lens at the root width. At new rank the final suffix slot is (3.3), and
(3.4) removes it before the same residual is reached. This proves (4.1).

For a lens input, the root position is `s` old and `s+2` new. Formula (2.5)
gives

```text
r^+=r       if a>v,
r^+=r+2     if a<v.                                 (4.4)
```

An above-`v` path slot always has `r<=s-2`, whereas a below-`v` path slot
always has `r>=s+2`; hence the two inequalities in (4.2) are preserved and
exhaust all possibilities. When the root width is smaller, the prefix
removes the upper lens black arm, the suffix removes the matching white arm,
and the output is the contracted lens at that width. When it is larger, the
wrapped prefix and suffix exhaust the lens, including all of its ports, the
`R_v` row has distance three against `B_1^(R_v)`, and the output is `C_1`.
These are exactly M269's two interval inductions with `b=1`.

For new-rank contraction the child-`d` pair `(s-1,s)` lies in the suffix
ending at `(s+2)-2`; for expansion the retained even slot is at most `s-2`,
so the same pair again lies wholly in the nonwrapping suffix. Thus it always
uses (3.4), never the lens arm. This proves (4.2). A canonical retained child
and every sibling use the same two-row macro against `B_1`, leaving `C_1`;
this proves (4.3). Every deletion is a complete dependency node, so accepted
complete-node commutation licenses the displayed order. QED.

## 5. Final completion of a contracted lens

The old contracted lens begins

```text
F_v^(m)(s)=
 S^alpha S_A
 B_v^alpha B_v^(q_(s-2)) ... B_v^(q_1)
 S^(R_v) A_v(s) S_C S^beta.                         (5.1)
```

The last root white in `U_d(beta)` is `W_d^alpha`. In the cyclic
concatenation (3.2), its next black half-edge is `B_v^alpha`, with exactly
the three displayed sides between them:

```text
W_d^alpha S^beta S^alpha S_A B_v^alpha -> S.        (5.2)
```

Thus label `alpha` records `x_v`. After (5.2), process the remaining lens
black arm from `q_(s-2)` down to `q_1`. Each row is exactly

```text
W_d^q S B_v^q -> S                                  (5.3)
```

and has distance one.

At new rank the contracted lens begins instead with

```text
S^gamma S_A
B_v^gamma B_v^beta B_v^alpha ... B_v^(q_1),         (5.4)
```

and the last root white before the crossing is `W_(d+1)^gamma`. Therefore

```text
W_(d+1)^gamma S^delta S^gamma S_A B_v^gamma -> S    (5.5)
```

has distance three and records `x_v`. Every remaining label, including
`beta` and `alpha`, then uses the distance-one row (5.3). Their earlier
records from (3.4) are consequently not changed.

After these rows there is no black half-edge. The remaining whites can be
listed exactly, rather than counted abstractly:

- for each position in the lens aggregate, `A_v` contains one white of that
  label;
- a persistent direct-child slot `h` replaces the ordinary pair by the two
  literal whites `W_v^(L_h)` and `W_h^(R_h)`, still one of each label; and
- every label outside the aggregate has its unique white in the root
  complement (3.1), including `R_v=q_0`.

Hence exactly one white of every label remains and RandomQuad Step 4 attaches
all of them to the final root.

At the old final width,

```text
t(h)<s  iff  h>v                                   (5.6)
```

for a direct child `h` of `v`: if `h>v`,
`t(h)=2(h-v)<=s-2`; if `h<v`, then
`t(h)-s=2(h-1)>0`. Equation (2.5) gives the identical criterion
`t^+(h)<s+2` at new rank. (The impossible vertex `h=1` cannot be a child of
`v`, because `p(1)` is the root.) Thus the ports reaching Step 4 are exactly

```text
D_v={h:v<h<d and p(h)=v},                            (5.7)
```

and both labels of every such port receive the final-root endpoint. The
edited `R_v` label likewise reaches Step 4.

The four root-label endpoints are now literal:

```text
b_d(alpha)=v,                 b_d(beta)=d,
b_(d+1)(alpha)=1,             b_(d+1)(beta)=1,
b_(d+1)(gamma)=v,             b_(d+1)(delta)=d+1.   (5.8)
```

## 6. Final completion of a canonical residual

The old and new canonical residuals at `1` are

```text
C_1^(d)   =S^alpha W_1^beta  S_D S^beta,
C_1^(d+1) =S^gamma W_1^delta S_D S^delta.           (6.1)
```

They contain no black half-edge. Concatenating the appropriate root
complement leaves one white of every label: the complement supplies every
label except `R_1`, and (6.1) supplies `W_1^(R_1)`. Step 4 attaches all of
them to the final root.

At old rank neither `alpha` nor `beta` can have had a prior distance-three
row: before the root they are not inherited nonroot-slot labels, and every
occurrence in a strict-internal high interval is an ordinary distance-one
row. At new rank (3.4) has already recorded `x_1` for `alpha,beta`, while
`gamma,delta` have no prior distance-three row. Therefore the exact sealed
table is

```text
b_d(alpha)=b_d(beta)=d,
b_(d+1)(alpha)=b_(d+1)(beta)=1,
b_(d+1)(gamma)=b_(d+1)(delta)=d+1.                  (6.2)
```

This applies whether `C_1` arose from an earlier canonical input or from a
lens expanding in the root row.

## 7. Every port and every inherited low label

It remains to show that the endpoint comparison is not hiding a port count.
Consider a direct child `h` of `v` and the actual width sequence of an open
lens.

- If `t(h)` lies above the initialization width, the two port labels
  discharge during initialization against the initial current parent.
- Otherwise they persist until the first contraction whose new width lies
  below `t(h)`. M269's exact macro then closes `R_h` and `L_h`, in that
  order, both at distance three to that current-parent black vertex.
- If the first width increase occurs while the port persists, the expansion
  discharges both labels against that current-parent black vertex.
- If there is no such event, (5.6) says precisely that `h>v`, and both
  literal port whites reach the final root.

For a decreasing numerical path, a smaller port `h<v` that survives
initialization discharges at the first parent `b<h`; this parent need not be
`1`. Only a port whose first crossing is the root records `x_1`. Equation
(2.5) proves that the first crossing, and hence the endpoint `x_b`, is the
same at both ranks. This is the promised individual-port statement.

Now partition the inherited low labels `1,...,m-2`, which are exactly the
two slot labels of vertices `2,...,d-1`.

1. A canonical off-path slot receives its accepted parent endpoint from
   M250/M254 pruning or from the identical sibling macro at both ranks.
2. A strict path slot receives the special endpoints in M269/M271's ledger;
   (2.5) makes the sequence of those rows rank-coupled.
3. `L_v` receives the same initial current-parent endpoint at both ranks.
4. `R_v` receives the same endpoint at the first expansion, or reaches the
   two final roots if no expansion occurs.
5. Each direct-child slot follows the individual port alternatives above.

This exhausts every inherited low label. If the process seals, every low
label has the same distance-three endpoint at both ranks. If it remains open,
the only labels without such a record are exactly

```text
E_v={R_v} union
    union_(h:v<h<d, p(h)=v){L_h,R_h},                (7.1)
```

and Step 4 gives those labels endpoints `d` and `d+1`, respectively. Hence

```text
sealed: b_(d+1)(q)=b_d(q)                  for 1<=q<=m-2;

open:   q in E_v     => (b_d(q),b_(d+1)(q))=(d,d+1),
        q not in E_v => b_(d+1)(q)=b_d(q).           (7.2)
```

## 8. Open versus sealed paths

Let the stopped path be

```text
P(v)=(v,a_1,...,a_k=1).
```

For a nonroot inherited vertex `a`, its old cyclic width is

```text
t(a)=2(a-v),            a>v,
t(a)=m-2(v-a),          a<v.                        (8.1)
```

M269 proves that a lens remains open exactly across strict decreases of
these widths; a width increase seals it.

If `P(v)` is strictly numerically decreasing, every vertex after `v` is
below `v`, (8.1) decreases at every step, and the final root width is `s`.
Thus direct-root initialization or root contraction leaves the open lens of
Section 5.

Conversely, suppose the numerical path is not strictly decreasing. If an
internal width increases, the state is already canonical. If no internal
width increases, an open path that ever crosses from the below-`v` sector to
the above-`v` sector cannot cross back without a width increase. Its last
nonroot width is therefore above `v`, hence at most `s-2`, and the root row
expands it to `C_1`. The same conclusion holds when `a_1>v`. Thus

```text
P(v) decreasing      iff final state is the lens of Section 5,
P(v) not decreasing  iff final state is C_1.        (8.2)
```

The rank shift (2.5) and root shift `s -> s+2` preserve this dichotomy.

## 9. Main theorem and formal downstream composition

### Theorem 9.1 (DL-RST; proved, awaiting fresh audit)

For every `d>=5`, every declared rooted tree, and every ordinary odd edit
`2<=v<=d-1`, consume the literal M269/M271 input at `a=1`: the reversed base
when `p(v)=1`, a decorated lens `F_v(r)` when the frontier remains open, or
`C_a` when it has sealed. Apply the old/new CP-6 contexts, including every
post-wrap sibling and the new child `d`, and then RandomQuad Step 4.

- If `P(v)` is not decreasing, the inherited endpoints obey the sealed line
  of (7.2), and the root labels obey (6.2).
- If `P(v)` is decreasing, the inherited endpoints obey the open lines of
  (7.2), and the root labels obey (5.8).

All persistent ports are the explicit individual ports (5.7); every other
port has the rank-stable first-crossing endpoint described in Section 7.
The three root inputs are exhaustively partitioned by Lemma 4.1. QED.

The boundary cases are literal:

- `p(v)=1` is (4.1), not an omitted internal row;
- `v=d-1` gives `s=2`, an empty larger-child set, and the same top row;
- empty cyclic arms, empty sibling sets, and empty port sets use empty
  products;
- the root/path equality `r=s` is impossible; and
- every post-wrap slot remains an adjacent pair and is included in the same
  interval induction.

**Formal composition, conditional on fresh acceptance of Theorem 9.1.**
M269/M271 supplies the strict-internal decorated transducer; Theorem 9.1
would supply its missing root row. Their endpoint consequence is exactly
M250 equations `(4.3)--(4.5)`, with M250's false one-bit transition `(4.2)`
replaced by the literal cyclic-width state. M250/M254's already accepted
metric pruning, common-nonchild theorem, and coordinate exhaustion would
then prove M240's ordinary-edit IDL. M240/M242 would in turn give the
ordinary-odd-edit route-normal closure and its length bound `<=4d-7`.

This paragraph is a dependency implication, not a current promotion:
Theorem 9.1 must first survive a fresh immutable referee. It does not repair
M250's refuted abstract transition table, and it says nothing about fixed
edits, every-color synchronization, route congestion, a spectral gap,
polynomial mixing, or either Terminal.

## 10. Predeclared four-case guard

Only after equations (2.1)--(8.2) were fixed in `checkpoint.md`, the no-import
script `root_seam_guard.py` replayed exactly four full contours:

1. direct-root `v=d-1` with no larger child;
2. a decreasing multilevel lens with one persistent larger port and one
   smaller port discharging at a nonroot first crossing;
3. an above-`v` lens whose persistent port discharges on root expansion;
4. a path already sealed before the root.

All seam-macro rows, top-lens rows, individual port endpoints, inherited-low
comparisons, and four root-label tables pass. The normalized four-row digest
is

```text
922fca4abe3fce67064cb5e5963a69ee222f4fa2fa2c6f89f110a5b0c62e1695.
```

This is exact finite calibration only; Sections 2--9 carry the universal
quantifiers.

```text
PROVED IN THIS FROZEN CANDIDATE:
  literal CP-6 transition for reversed-base, decorated-lens, and C inputs;
  exact new-child seam macro and final-root complement;
  individual persistent/discharged port endpoints;
  inherited low endpoint comparison and both root four-block tables;
  DL-RST as a standalone deterministic theorem.

AWAITING INDEPENDENT AUDIT:
  promotion of DL-RST and every downstream composition.

NOT CLAIMED:
  resurrection of the refuted one-bit CPR rule; fixed edits;
  every-color routing; congestion; a gap; mixing; Terminal A or B.
```
