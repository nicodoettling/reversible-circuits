# M247 proof audit of frozen M244

Date: 2026-08-14 UTC.

## 1. Immutable and source locks

Running `sha256sum -c SHA256SUMS` in frozen M244 returns `OK` for all nine
listed payloads.  The SHA-256 of M244's inventory file is exactly

```text
134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d.
```

The frozen M240 and M242 inventories also verify, at

```text
M240 2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242 49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663.
```

The locked author PDF of Duchi--Poulalhon--Schaeffer has SHA-256

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

The primary source supports exactly the inputs used by the pruning proof:
Proposition 3 roots the Cayley tree at `y_d`, inserts `x_a` on the first edge
from `y_a` toward the root, and installs the two slot labels; the hairy-tree
rule completes increasing white and oppositely oriented black cyclic label
orders; Lemma 2 makes a consecutive white/black pair a same-label legal
distance-one or distance-three closure; and RandomQuad/Theorem 5 implements
these closures with a LIFO stack.  The paper writes the factor product as
`tau_m ... tau_1=id`; the project endpoint convention is the already accepted
plus-mirror display.  The source does not state any comparison between the
two edited ranks, RSMI, or IDL.

## 2. Canonical slots and literal excursion

For

```text
pi_d=(2d-3,2d-2,1,2,...,2d-4),
```

the slot at inserted black `x_a` is

```text
L_a=2a-3,  R_a=2a-2                              (mod 2d-2).
```

Thus `R_a=L_a+1` cyclically.  The ordinary edit swaps only the two values in
slot `x_v`, reversing that slot.  Every component of `T\P(v)` excludes
`x_v`, so every slot to which Theorem 3.1 is applied remains canonical and
unedited.  This remains true under root extension; the inherited off-path
labels do not change.

Cutting immediately after the parent-to-`x_a` crossing gives a genuine
bridge-delimited contour interval.  Starting at black `x_a`, decreasing
rotation gives the leading black gap and the `L_a` crossing; increasing
rotation at `y_a` gives the ordered child excursions and white gaps; the
return gives the trailing black gap and `R_a` crossing.  This reconstructs
M244 equation (2.2) literally.  No finite-rank pattern is used.

## 3. Accepted pruning theorem

**Theorem 3.1 is accepted as a proved colored-stack statement.**  Here is the
independent induction.

After recursively pruning each child excursion `E_c`, replace it by its sole
surviving token `W^{R_c}`.  The increasing white gaps at `y_a`, together with
those child survivors, contain exactly one white token of every label except
`L_a`.  Since `R_a=L_a+1`, the leading decreasing black interval is empty.
The trailing decreasing black interval contains exactly one black token of
every label except `L_a,R_a`, in the reverse order.  Bottom-up LIFO closure
therefore removes nested equal-label pairs and leaves precisely the initial
`W^{R_a}`.

At every step the chosen pair is consecutive among remaining half-edges in a
valid pre-map.  DPS Lemma 2 supplies equality of its labels, a side distance
in `{1,3}`, and a legal local closure.  The nesting never crosses either cut
of `E_a`, so each deletion contains both half-edge endpoints and every side
token it consumes: it is a complete internal rewrite node.  Child nodes are
deleted before parent nodes, and no outside token changes.  Adjoining a
formal `B^{R_a}` balances the half-edge projection.  Without that formal
token the excursion has white-minus-black excess one, not zero.

This proves only colored one-open compression.  The residual side words can
still change whether later closure distance is one or three and which black
endpoint is recorded.  The reversed edited slot `x_v` lies on the retained
path and is never pruned.

## 4. Material rejection objections

### M-1. Literal RSMI(2) is false because its larger-child clause is not conditioned on the open path

Use `d=7`, `v=4`, and

```text
T={{1,7},{1,3},{1,6},{2,3},{2,4},{4,5}}.
```

Rooting at 7 gives

```text
P(v)=(4,2,3,1),
```

which is not strictly decreasing because `2<3`.  Nevertheless `a=5>v` is a
direct child of `v`.  The no-input clean-room DPS replay reconstructs the
two edited closures directly from the contour and LIFO rules.  It obtains

```text
N=A,
N|_(7,8)=A|_(7,8)=((2,4),(2,4))       (zero-based endpoints).
```

Unqualified RSMI(2) instead requires the two slot labels of `a=5` to close
against old final black `x_7` and new final black `x_8`, predicting

```text
((4,6),(4,6))  versus  ((4,7),(4,7)).
```

It is therefore refuted as written.  This one exact row does not address a
repaired clause restricted to the open/strictly-decreasing case.

### M-2. RSMI does not assert IDL-a

RSMI(3) says only that a strict descent “transmits” one interface and lists a
root behavior.  It nowhere asserts that the edited label at coordinate
`2v-2` closes against `x_d` at old rank and `x_{d+1}` at new rank.  Those are
the second endpoints needed to obtain

```text
N_(2v-2)=(v-1,d-1),   A_(2v-2)=(v-1,d).
```

Proposition 5.1's phrase “its first exposed edited face gives” is not derived
from Theorem 3.1 or any stated RSMI clause.

### M-3. RSMI(1) does not assert the absolute endpoint or disjointness in IDL-c

RSMI(1) preserves a retained old pair's side count and, in a distance-three
case, preserves its black endpoint *between ranks*.  It does not identify
that endpoint as `x_{p(r)}`.  Consequently it yields neither

```text
N|_(I_r)=A|_(I_r)=((r-1,p(r)-1),(r-1,p(r)-1))
```

nor disjointness from `{v-1,d-1,d}`.  Avoidance by the Cayley parent edge
controls the first/canonical incidence but does not by itself identify the
second black endpoint created by metric closure.

### M-4. The absorbed/closed transition has no factor-level or root equality clause

The words “absorbs it” in RSMI(3) do not define what happens to already
exposed metric endpoints, larger-child interfaces, unnamed coordinates, or
the final root sector.  In particular, no clause states that after absorption
all inherited factor coordinates coincide and the two new final coordinates
are `(0,d)^2`.  Thus the assertion `N=A` in the nondecreasing case is not a
consequence of the written premises.  Objection M-1 shows that interpreting
RSMI(2) literally in that same case is actually incompatible with `N=A`.

These are material objections.  Accordingly, the claimed exact remaining
RSMI lemma is refuted, and Proposition 5.1 is not an accepted derivation of
full IDL from a usable narrower hypothesis.

## 5. Exact repaired obligation

A replacement `RSMI+` must at minimum make the open/closed state split
literal and add all of the following factor-level assertions:

1. **Open-only larger-child clause.**  Apply the old-root/new-root endpoint
   rule of former RSMI(2) only when `P(v)` is strictly decreasing and the
   defect remains open through the root.  It must not apply to the closed row
   in M-1.
2. **Initial edited endpoint.**  In the open case, the label at coordinate
   `2v-2` has second black endpoint `x_d` at rank `d` and `x_{d+1}` at rank
   `d+1`, giving IDL-a exactly.
3. **Common nonchild endpoint.**  For every `v<r<d` with `p(r)!=v`, both slot
   labels close against `x_{p(r)}` at both ranks, giving `h_r^2`; state
   explicitly that `h_r` is disjoint from `{v-1,d-1,d}`.
4. **Sealed transition and root.**  If a larger path vertex or internal
   ascent absorbs the defect, then all inherited physical factor coordinates
   agree under the natural rank embedding, including any larger direct-child
   coordinates, and the root extension supplies exactly the two final
   `(0,d)` factors.  This is the metric content needed for closed `N=A`.
5. **Open root and exhaustion.**  In the open case, state the four physical
   factors at one-based positions `2d-3,...,2d` exactly as IDL-d, and state
   literal equality at every remaining unnamed coordinate.

Whether this repaired local interface lemma is true is unresolved.  The
counterexample above refutes only the frozen unqualified RSMI, not `RSMI+`.

## 6. Clean-room witness and scope

Run:

```text
python3 -B cleanroom_token_check.py
```

The script imports no predecessor code or data, uses Python 3.12.3, no
nonstandard dependency, and no seed.  It checks exactly the one declared
boundary row above.  The paired-word digest is

```text
2af24b962c405a057f2d54aac7f3bb24736c45a002e16c040b224b4b08ce27a7.
```

This audit proves no RSMI+, IDL, all-rank `Z_2`, fixed-edit theorem,
every-color route, voltage correction, route length, comparison bound,
spectral gap, mixing theorem, or Terminal conclusion.

