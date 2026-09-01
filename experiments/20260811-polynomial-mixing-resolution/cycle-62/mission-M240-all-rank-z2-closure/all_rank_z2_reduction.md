# M240 all-rank `Z_2` reduction

Date: 2026-08-13 UTC. Status: **proved strict symbolic reduction; all-rank
DPS closure remains unresolved**.

## 1. Exact setting

Fix `d>=5`. Let `T` be a tree on one-based white labels `[d]`, rooted at the
leaf `d`, with parent `p(1)=d`; equivalently `{1,d}` is the root edge. Adjoin
the new root leaf `{1,d+1}` and write

```text
T^+=T union {{1,d+1}},
pi_d=(2d-3,2d-2,1,2,...,2d-4).
```

Physical permutation labels are zero-based. For an ordinary inherited odd
edit

```text
i=2v-3,                    2<=v<=d-1,
N=F_d(T,s_i pi_d)(0,d)(0,d),
A=F_(d+1)(T^+,s_i pi_(d+1)),                         (1.1)
```

where `F_r` is the accepted plus-mirror DPS closure. Words are displayed
left to right. Chronological signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),          R_j^-1(a,b)=(aba,a).       (1.2)
```

Set

```text
x=v-1,     y=d-1,     z=0,     n=d.                  (1.3)
```

These four physical labels are distinct.

## 2. The exact remaining DPS lemma

Root `T` at `d`, let `P(v)=(v,p(v),...,1)`, and call this path decreasing when

```text
v>p(v)>p^2(v)>...>1.
```

This is equivalent to the M231 open condition `NOT(late OR ascent)`: if an
internal path vertex exceeds `v`, `late` holds; otherwise failure of strict
decrease is exactly an internal ascent.

The following is the standalone unresolved statement.

> **DPS INITIAL-DEFECT LEMMA (IDL).** With (1.1)--(1.3):
>
> 1. If `P(v)` is not decreasing, then `N=A`.
> 2. If `P(v)` is decreasing, then the two length-`2d` words have the
>    following exact coordinate relation. Initially
>
>    ```text
>    N_(2v-2)=(x,y),             A_(2v-2)=(x,n).      (IDL-a)
>    ```
>
>    For every `r` with `v<r<d`, put `u=r-1`. Its slot is
>    `I_r=(2r-3,2r-2)`.
>
>    - If `p(r)=v`, then
>
>      ```text
>      N|_(I_r)=((u,y),(u,y)),
>      A|_(I_r)=((u,n),(u,n)).                       (IDL-b)
>      ```
>
>    - If `p(r)!=v`, put `h_r=(r-1,p(r)-1)`. Then
>
>      ```text
>      N|_(I_r)=A|_(I_r)=(h_r,h_r),                  (IDL-c)
>      ```
>
>      and `h_r` is disjoint from `{x,y,n}`.
>
>    At the old/new-root boundary,
>
>    ```text
>    position             2d-3    2d-2    2d-1    2d
>    N                    (z,x)    (z,y)    (z,n)   (z,n)
>    A                    (z,y)    (z,y)    (z,x)   (z,n).     (IDL-d)
>    ```
>
>    At every coordinate not named in `(IDL-a)--(IDL-d)`, `N` and `A`
>    agree literally.

IDL is a statement about the global DPS stack closure, not a consequence of
group multiplication or ordinary Hurwitz algebra. DPS Proposition 3
constructs the rooted hairy tree, and DPS Lemma 2/Theorem 5 prove validity and
invertibility of its stack closure, but the source does not state IDL's
comparison of two edited closures. M214/M218, M231/M234, and M236/M237 prove
the corresponding endpoints at old ranks `d=5,6,7`; those are exact finite
calibrations and not a proof of IDL.

## 3. Unconditional local transport identities

All statements in this section are literal group identities.

### 3.1 Square transport

For arbitrary transpositions `c,h`, two chronological moves give

```text
R_j R_(j+1)       (c,h,h)=(h,h,c),                   (3.1)
R_j^-1 R_(j+1)^-1(c,h,h)=(chc,chc,c).                (3.2)
```

Indeed,

```text
(c,h,h) -> (h,hch,h) -> (h,h,c)
```

in (3.1), while

```text
(c,h,h) -> (chc,c,h) -> (chc,chc,c)
```

in (3.2).

For a direct larger child, use

```text
c_y=(x,y), h_y=(u,y),      c_n=(x,n), h_n=(u,n).
```

Then

```text
c_y h_y c_y=(u,x)=c_n h_n c_n.                       (3.3)
```

Thus an inverse pair sends the two differing triples to

```text
((u,x),(u,x),c_y),        ((u,x),(u,x),c_n),          (3.4)
```

respectively: it equalizes the square and advances the cursor.

For a nonchild slot, `(IDL-c)` makes `h_r` disjoint from both `c_y` and
`c_n`. Consequently either (3.1) or (3.2) leaves the common square
`h_r^2` unchanged and advances the two cursors.

### 3.2 Terminal carrier

Put

```text
B_d=R_(2d-4)^-1 R_(2d-3) R_(2d-2)^-1
    R_(2d-3)^-1 R_(2d-4)^-1.                         (3.5)
```

For distinct `x,y,z,n`, direct application of (1.2) gives

```text
(xy,zx,zy,zn)
 ->(zy,xy,zy,zn)
 ->(zy,zy,zx,zn)
 ->(zy,zy,xn,zx)
 ->(zy,xn,zy,zx)
 ->(xn,zy,zy,zx).                                    (3.6)
```

Hence `B_d` changes exactly the source four-block into the target four-block.

## 4. Conditional all-rank route theorem

For `0<=t<L=d-v-1`, let

```text
c_t=1[p(v+t+1)=v],
epsilon_0=-1 if c_0=1 else +1,
epsilon_t=-1 if c_t=1 else -epsilon_(t-1),

Q(v,epsilon)=product_(t=0)^(L-1)
  R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t.     (4.1)
```

The only property of this sign automaton used below is

```text
c_t=1 => epsilon_t=-1.                               (4.2)
```

In fact an absent-child sign may be chosen arbitrarily; the alternating rule
is sufficient but not necessary for endpoint correctness.

### Theorem 4.1 (route-normal closure conditional on IDL)

Assume IDL. For every `d>=5`, every declared `T`, and every ordinary odd
edit `i=2v-3`,

```text
P(v) not decreasing  => N=A,
P(v) decreasing      => act(N,Q B_d Q^-1)=A.         (4.3)
```

Equivalently, the M231 route-normal formula factors through

```text
Z_2=("closed",)                 if late OR ascent,
    ("open",v,epsilon)          otherwise.
```

#### Proof

The closed implication is IDL(1). Suppose the path is decreasing. Before
stage `t`, the source and target cursors are respectively `(x,y)` and `(x,n)`
at position `2(v+t)-2`. All positions strictly between the initial cursor
and that position already agree; later slots and the boundary still have the
IDL form.

Let `r=v+t+1`. If `p(r)=v`, then (4.2), `(IDL-b)`, and (3.2)--(3.4)
equalize slot `I_r` and put the unchanged cursors at position
`2(v+t+1)-2`. If `p(r)!=v`, `(IDL-c)` and (3.1)--(3.2) show that either
sign preserves the common square and advances the cursors to the same new
position. This proves the scan invariant by induction over `t`.

After the last stage, `act(N,Q)` and `act(A,Q)` agree outside positions
`2d-4,...,2d-1`; by `(IDL-d)` their four-blocks are exactly

```text
((x,y),(z,x),(z,y),(z,n)),
((x,n),(z,y),(z,y),(z,x)).
```

Equation (3.6) sends the first to the second. Finally, chronological
application of `Q^-1` sends `act(A,Q)` back to `A`. This proves (4.3). QED.

The conditional route has literal length

```text
2|Q|+|B_d|=4(d-v-1)+5 <= 4d-7.                       (4.4)
```

This is a conditional length bound for one declared endpoint only. It is not
an every-color route, a synchronized matching theorem, a recovery/congestion
bound, or a physical/original-chain gap.

## 5. Boundary and fixed edits

The `Z_2` theorem concerns only ordinary odd edits `1,3,...,2d-5`.
The remaining edit families are separate:

```text
internal even i<=2d-6        proposed word identity,
i=2d-4                       proposed word (R_(2d-5)^-1)^2,
i=2d-3                       proposed word R_(2d-2)^-1.
```

The generic tuple identities

```text
(R_j^-1)^2[a,b,a]=[b,aba,a],
R_j^-1[a,b]=[aba,a]                                   (5.1)
```

are unconditional. Their application at arbitrary rank still needs the
corresponding DPS boundary-factor shapes; M240 does not infer those shapes
from the finite `d=5,6,7` passes.

The minimal old ranks `d=5,6,7` are already covered exactly by the accepted
finite artifacts, including fixed edits. IDL and the boundary-shape
statements remain unproved for arbitrary `d`; another finite rank cannot
replace their proofs.

## 6. Verdict and first unproved step

M240 does **not** prove all-rank `Z_2` closure. It proves that the entire
ordinary-edit endpoint theorem follows from the explicit coordinatewise IDL,
using only the unconditional square-transport and carrier identities.

The first unproved step is now:

> Derive `(IDL-a)--(IDL-d)` and the closed equality from the DPS hairy-tree
> boundary stack for a decreasing versus nondecreasing stopped parent path.

This is a sharper obligation than the former unspecified "track the whole
contour" task: every coordinate and every required label is fixed. No
every-color conclusion, synchronized route, voltage correction, congestion,
spectral gap, polynomial mixing statement, or Terminal follows.

