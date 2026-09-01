# M208 rooted one-leaf correction: exact d5-to-d6 theorem

Date: 2026-08-13 UTC.

## 1. Convention and rooted coordinates

Let `F_d(T,pi)` be the accepted plus-mirror rooted DPS closure, with Cayley
tree `T` on one-based white labels `[d]`, root `d`, and `pi` listing the two
edge labels placed at black vertices `x_1,...,x_(d-1)`. Physical labels are
zero-based. Signed right Hurwitz generators act chronologically by

```text
R_j(...,a,b,...)    =(...,b,bab,...),
R_j^-1(...,a,b,...)=(...,aba,a,...).
```

Let `s_i pi` exchange the values `i,i+1` in `pi`.

For the two named M181 patterns, the distinguished-root d=5 coordinates are

```text
T_0={{1,2},{1,3},{1,5},{2,4}},
T_1={{1,2},{1,3},{1,4},{1,5}},
pi_5=(7,8 | 1,2 | 3,4 | 5,6).
```

The exact d=6 one-leaf source extension is

```text
E(T_b)=T_b union {{1,6}},
pi_6=(9,10 | 1,2 | 3,4 | 5,6 | 7,8).                (1.1)
```

This has a direct rooted-tree meaning. Old root 5 is a leaf adjacent to 1.
After making 6 the new root adjacent to 1, the old black slot at child 1
moves to the new child-5 edge, while the new child-1 edge receives labels
9,10. Direct closure gives

```text
F_6(E(T_b),pi_6)=F_5(T_b,pi_5)(05)(05),              (1.2)
```

for `b=0,1`, exactly the M181 d=6 sources.

## 2. Naive and actual edited endpoints

For each inherited edit `1<=i<=7`, define

```text
N_(b,i)=F_5(T_b,s_i pi_5)(05)(05),
A_(b,i)=F_6(E(T_b),s_i pi_6).                         (2.1)
```

M203/M205 proved that `N_(b,i)` and `A_(b,i)` are not generally even globally
relabeling-equivalent. The correction below does not identify them; it gives
an explicit signed-Hurwitz route between the physical endpoints.

## 3. Exact synchronized correction theorem

### Theorem 3.1 (named M181 d5-to-d6 correction; **PROVED, EXACT FINITE**)

For every `i=1,...,7`, one signed Hurwitz word `C_i` sends both naive endpoints
to their corresponding actual endpoints:

```text
C_i N_(0,i)=A_(0,i),        C_i N_(1,i)=A_(1,i).      (3.1)
```

Chronological words are

```text
C_1=R2 R3 R4^- R5^- R6^- R7 R8^- R7^- R6^- R5 R4 R3^- R2^-
C_2=id
C_3=R4 R5 R6^- R7 R8^- R7^- R6^- R5^- R4^-
C_4=id
C_5=R6^- R7 R8^- R7^- R6^-
C_6=(R5^-)^2
C_7=R8^-.
```

Their lengths are respectively

```text
13, 0, 9, 0, 5, 2, 1.                                (3.2)
```

**Proof.** `rooted_extension_audit.py` reconstructs `T_b,pi_5,E(T_b),pi_6`
from the accepted DPS boundary closure, constructs all fourteen physical
words in (2.1), and applies every displayed Hurwitz generator using the
formulas in Section 1. All fourteen literal endpoint equalities (3.1) pass.
The checker imports no route table or endpoint result from M203; the routes
are literal constants in M208. This is a complete finite proof of (3.1).
QED.

The words show a partial transport pattern. Put

```text
B=R6^- R7 R8^- R7^- R6^-.
```

Then `C_5=B` and `C_3=(R4 R5)B(R4 R5)^-1`; `C_1` is another explicit
conjugate of `B`, with conjugator `R2 R3 R4^- R5^-`. Generator support moves
toward the newly adjoined factor pair. This is an observed exact formula for
the named template, not yet a general contour theorem.

### Corollary 3.2 (finite distinguished d=6 synchronized route; **PROVED**)

Take any accepted d=5 synchronized braid from the two M181 d=5 sources to
the pair `F_5(T_b,s_i pi_5)`. Apply it to the first eight positions of the d=6
sources, leaving `(05)^2` fixed, and then apply `C_i`. The composite reaches
the actual pair `A_(b,i)`. Hence the distinguished rooted M181 pair has an
exact synchronized physical quotient route at d=6 for inherited edits
`i=1,...,7`.

This corollary does not cover the two new d=6 indices 8,9, arbitrary H-orbit
representatives, arbitrary matching colors, or arbitrary d.

## 4. Falsification of the candidate universal schedule table

The same coordinate extension (1.1) makes sense for every d=5 Cayley tree in
which root 5 is a leaf adjacent to 1. There are exactly 16 such trees. Applying
the seven already displayed `C_i` to all `16*7=112` corresponding endpoint
pairs gives 21 failures, split

```text
edit 1: 11,       edit 3: 9,       edit 5: 1.         (4.1)
```

The first failure uses

```text
T_*={{1,2},{1,3},{1,5},{3,4}},       i=3.             (4.2)
```

It has the same root-extension path `5-1-6` and the same orders `pi_5,pi_6`
as the named patterns. But `C_3` sends the naive target to

```text
(12)^2,(02),(25),(34)^2,(04)^2,(02),(05),
```

while the actual target is

```text
(12)^2,(02),(25),(35)^2,(04)^2,(02),(05).             (4.3)
```

Thus the explicit schedule table of Theorem 3.1 is sensitive to off-contour
tree attachment and is not a universal recurrence on this 16-tree template.
This does **not** prove that no other common or tree-dependent correction word
exists for (4.2); no radius miss is used as an obstruction.

## 5. Strict surviving lemma

The general structural obligation is now narrower:

> **ROOTED LEAF-EXTENSION SCHEDULE LEMMA (UNRESOLVED).** Given a rooted DPS
> coordinate `(T,pi)` whose old root is a leaf, describe sufficient local tree
> data around the rerooting contour and construct a signed braid taking
> `F_d(T,s_i pi)` with the new doubled leaf appended to
> `F_(d+1)(E(T),s_i E(pi))`, with a proved bound uniform in `d` and with
> synchronized compatibility for the matching subfamily under study.

The bare root path plus edit index and order do not justify reusing the M208
schedule table: (4.2) is the first exact warning. An alternative schedule may
still exist, so the universal lemma remains unresolved rather than refuted.

## 6. Scope

No `Q_6` graph was enumerated. The theorem is exact finite d5-to-d6 and covers
only the two named M181 patterns and old edits 1..7. It proves no d>=7
recursion, every-color statement, arbitrary-representative route, polynomial
route length, voltage-correction length, spectral gap, mixing, or Terminal
claim.

