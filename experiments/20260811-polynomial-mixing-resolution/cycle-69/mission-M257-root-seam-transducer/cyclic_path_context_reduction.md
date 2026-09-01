# M257 exact cyclic path-context reduction

Date: 2026-08-14 UTC.  Status: **proved raw contour reduction; RSPT remains
unresolved in a cyclic path-row lemma and a separate root-seam table lemma**.

## 1. Source, convention, and scope

The immutable M240, M242, M244, M247, M250, and M254 inventories verify at
the digests recorded in `checkpoint.md`.  The locked Duchi--Poulalhon--
Schaeffer PDF verifies at

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

Only M244 Theorem 3.1 in the scope accepted by M247, and the metric pruning
and common-nonchild results accepted by M254, are inputs.  The rejected M244
RSMI is not used.

There is no probability distribution or Markov kernel in this note.  The
object is the deterministic DPS closure for an ordinary odd edit.  White
rotations increase, black rotations decrease, and a literal local row is

```text
W^q S^e B_b^q -> S,       e in {1,3},
```

with second black endpoint `x_b` recorded exactly when `e=3`.

## 2. Exact cyclic incidence data

Fix `d>=5`, `2<=v<=d-1`, and rank `rho` equal to `d` or `d+1`.  Put
`M=2rho-2`.  For ordinary slots write

```text
L_a=2a-3,       R_a=2a-2=L_a+1.
```

At the edited black vertex `x_v`, these two incidences are reversed.  For a
rooted child `c` of a white vertex `a`, the actual label at `y_a` is

```text
kappa(c)=L_v,  if c=v,
         R_c,  otherwise.                              (2.1)
```

Intervals `W_a(u up_M w)` and `B_a(u down_M w)` contain the missing
half-edges strictly between `u,w` in increasing and decreasing cyclic order,
respectively.  This convention includes lower-index children reached after
wrap and allows empty intervals.

## 3. Proved raw context theorem

### Theorem 3.1 (exact cyclic stopped-path context; **PROVED**)

Let `a!=v` be a canonical vertex and order its rooted children
`c_1,...,c_t` by increasing cyclic order of `kappa(c_j)` after `L_a`.  Put
`q_0=L_a`, `q_j=kappa(c_j)`.  If `I_j` is the bridge-delimited excursion of
child `c_j`, then the literal excursion at `a` is

```text
P_a[I_1,...,I_t] =
 S^(L_a)
 product_(j=1)^t [W_a(q_(j-1) up_M q_j) S^(q_j) I_j]
 W_a(q_t up_M L_a) S^(L_a)
 B_a(L_a down_M R_a) S^(R_a).                         (3.1)
```

For every canonical off-path child `h`, the accepted metric pruning theorem
may be substituted as

```text
I_h -> S^(L_h) W^(R_h) S^(*) S^(R_h),                (3.2)
```

so its full parent block is

```text
S^(R_h) S^(L_h) W^(R_h) S^(*) S^(R_h).               (3.3)
```

These substitutions commute with the one retained path-child interval.
Leaving that interval as a hole defines a one-dimensional cyclic context
operator `P_(a,c)`.

At the initial edited vertex, order its canonical children increasingly
after `R_v`, put `q_0=R_v`, `q_j=R_(c_j)`, and use instead

```text
P_v^rev[I_1,...,I_t] =
 B_v(L_v down_M R_v) S^(R_v)
 product_(j=1)^t [W_v(q_(j-1) up_M q_j) S^(q_j) I_j]
 W_v(q_t up_M R_v) S^(R_v) S^(L_v).                  (3.4)
```

The full stopped-path contour is obtained by nesting (3.4) successively in
the unique path-child holes (3.1), pruning every other child by (3.2).

#### Proof

Cut the ordinary tree contour immediately after the parent-to-black crossing
of each path edge.  At a canonical `x_a`, decreasing black rotation from
`R_a` reaches `L_a` immediately, so the leading black interval is empty and
the first crossing is `S^(L_a)`.  Increasing rotation at `y_a` encounters
the actual child incidences in exactly the cyclic `kappa` order (2.1), giving
the product in (3.1).  The return along the `L_a` side, decreasing trailing
black interval, and return along `R_a` give the last line of (3.1).

At `x_v`, the parent incidence is `L_v` and child incidence is `R_v`.
Decreasing rotation therefore first traverses
`B_v(L_v down_M R_v)`, while `B_v(R_v down_M L_v)` is empty.  The two sides
of the child incidence are both `S^(R_v)` and the final parent side is
`S^(L_v)`, proving (3.4).

Every off-path interval is canonical and excludes `x_v`.  Accepted metric
pruning gives (3.2), and its complete dependency nodes do not cross either
bridge cut.  Hence those deletions commute with the retained child hole and
give (3.3).  A tree has one path child at every strict ancestor of `v`, so
iterating these contexts reconstructs the entire stopped-path contour. QED.

This proof uses cyclic incidence labels, not numerical child order.  It
therefore includes every lower-index post-wrap child.

## 4. Explicit root seam

Put

```text
m=2d-2,  alpha=m-1, beta=m, gamma=m+1, delta=m+2.
```

The only rank-dependent rooted-tree incidence at the stopped seam is

```text
rank d:    x_1 has (L_1,R_1)=(alpha,beta), parent y_d;
rank d+1:  x_1 has (L_1,R_1)=(gamma,delta), parent y_(d+1),
           y_1 has the new canonical child d with kappa(d)=R_d=beta.
                                                               (4.1)
```

All other inherited child incidences obey (2.1).  Formula (3.1), with the
two data rows in (4.1), explicitly includes the cyclic seam `a=1`, new child
`d`, both new labels, and exhaustion of the full label sets.  It does not
assume an unnamed fresh coordinate.

## 5. Two separate unresolved obligations

Define M250's exposed set

```text
E_v={2v-2} union
    union_{r:v<r<d, p(r)=v}{2r-3,2r-2}.              (5.1)
```

### CPR: cyclic path-row lemma (**UNRESOLVED**)

After the substitutions (3.2)--(3.3):

1. the edited base context (3.4) initializes exactly `O(E_v)`;
2. a path step from current child `c` to parent `a` with `c>a` transports
   every `e in E_v` only through distance-one rows and preserves state `O`;
3. the first step with `c<a` gives every still exposed label a
   distance-three endpoint which is the same at ranks `d,d+1`, producing
   state `C`;
4. a `C` input remains `C`; and
5. every inherited low label outside `E_v` has the same distance-three black
   endpoint at the two ranks throughout.

This is the literal content needed for M250 (4.2)--(4.3).  Its first
falsifier is one complete row of (3.1) with the wrong side count, or the
first rank-dependent named black token.  The statement includes the initial
edited coordinate, every larger direct child, every lower-index post-wrap
child, and all unnamed low labels.

### RST: root-seam table lemma (**UNRESOLVED, SEPARATE FROM CPR**)

Apply (3.1) to the two explicit seam rows (4.1), then perform the final root
completion.  For sealed input prove

```text
b_d(alpha)=b_d(beta)=d,
b_(d+1)(alpha)=b_(d+1)(beta)=1,
b_(d+1)(gamma)=b_(d+1)(delta)=d+1;                  (5.2)
```

for open input prove

```text
b_d(alpha)=v,       b_d(beta)=d,
b_(d+1)(alpha)=1,   b_(d+1)(beta)=1,
b_(d+1)(gamma)=v,   b_(d+1)(delta)=d+1.             (5.3)
```

These are exactly M250 (4.4) and (4.5), but are not consequences of the raw
context theorem alone.  Keeping RST separate prevents the changing modulus,
the new post-wrap child `d`, or final-root defaults from being hidden inside
the internal path induction.

CPR plus RST, together with the already accepted M250 metric pruning and
common-nonchild theorem, is sufficient for RSPT.  Neither lemma is proved
here, so RSPT and IDL remain unresolved.

## 6. Boundary audit and verdict

The formulas remain literal when `a=1`, a cyclic interval wraps, a child has
smaller numerical index, `v=d-1` makes the larger-child set empty, or a gap
contains no unnamed label.  Empty products and intervals are explicitly
allowed.  This checks definition-level coverage only; it does not prove CPR
or RST.

```text
PROVED:
  exact incidence rule (2.1);
  raw canonical path context (3.1);
  accepted off-path substitution (3.2)--(3.3);
  raw reversed base context (3.4);
  nesting reduction and explicit root-seam data (4.1).

UNRESOLVED:
  CPR metric open/sealed simplification;
  RST sealed/open root endpoint tables;
  hence RSPT, repaired RSMI+, IDL, and all-rank ordinary-edit Z2.

NOT CLAIMED:
  fixed edits; every-color synchronization; voltage-corrected length;
  congestion; a spectral gap; polynomial mixing; Terminal A or B.
```

No finite replay, expansion, or census was performed in M257.
