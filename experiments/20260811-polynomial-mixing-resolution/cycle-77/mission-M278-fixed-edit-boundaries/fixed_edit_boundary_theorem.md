# M278 arbitrary-rank fixed-edit boundary theorem

Date: 2026-08-14 UTC.  Status: **proved analytically; fresh audit
requested**.  The small guard described in Section 8 is a falsifier for
transcription and boundary errors, not the proof.

## 1. Statement and conventions

Let `d>=5`.  Let `T` be a tree on `[d]`, rooted at the leaf `d`,
with root edge `{1,d}`, and let `p(u)` be the parent of `u`.  Put

```text
m=2d-2,
pi_d=(m-1,m | 1,2 | 3,4 | ... | m-3,m-2).
```

Thus the root-child slot `1` is `(m-1,m)`, while the slot of child
`u>=2` is

```text
(L_u,R_u)=(2u-3,2u-2).
```

Let `F_d(T,pi)` be the factor word produced by the DPS RandomQuad closure,
in increasing label order.  An edit `s_i pi` means the literal interchange
of the values `i,i+1` in the port order.  Adjoin a new root leaf at
`1`,

```text
T^+=T union {{1,d+1}},
```

and compare

```text
N_i=F_d(T,s_i pi_d) (0,d)^2,
A_i=F_(d+1)(T^+,s_i pi_(d+1)).                       (1.1)
```

Tuples are displayed in factor-position order.  Products and Hurwitz moves
use the chronological left-to-right convention

```text
R_j[x,y]=[y,yxy],
R_j^(-1)[x,y]=[xyx,x].                               (1.2)
```

Every displayed letter is a transposition.  Under these conventions,
for every `T`:

```text
i=2,4,...,2d-6 : N_i=A_i;
i=2d-4         : A_i=(R_(2d-5)^(-1))^2 N_i;
i=2d-3         : A_i=R_(2d-2)^(-1) N_i.              (1.3)
```

Here a route acts in the written chronological order.  In particular, the
two negative generators in the middle line really are two successive
inverse moves at the same position.

## 2. The DPS incidence calculation

We use only RandomQuad Steps 3--4 of the locked DPS source.  Write
`W_x^q` and `B_y^q` for open white and black half-edges with label
`q`, and `S` for a traversed side.  White rotation increases labels,
black rotation decreases labels.  LIFO closure has the local rule

```text
W_x^q S^epsilon B_y^q -> S,    epsilon in {1,3};      (2.1)
```

the black endpoint `y` is recorded exactly when `epsilon=3`.  A label
with no distance-three record is attached in Step 4 to the final root.
If `b_1(q)` is the child whose original black port carries `q`, and
`b_2(q)` is the recorded black endpoint or the final root, the factor at
position `q` is

```text
(b_1(q)-1,b_2(q)-1),                                  (2.2)
```

with the endpoints put in increasing order.

Two elementary consequences will be used.

**Canonical-slot lemma.**  Put

```text
E_u=(u-1,p(u)-1),  2<=u<=d-1,
G=(0,d-1).
```

Then

```text
F_d(T,pi_d)=E_2^2 E_3^2 ... E_(d-1)^2 G^2.            (2.3)
```

Indeed, erase leafmost complete half-edge intervals using (2.1).  The two
ports in slot `u` have first endpoint `u`; after all descendant
intervals have been erased, their last distance-three black endpoint is
`p(u)`.  The two ports in the root-child slot have first endpoint `1`
and no later black endpoint, so Step 4 supplies root `d`.  Induction on
the number of erased nonroot slots proves (2.3).  Applied to `T^+`, this
also gives the unedited rank identity

```text
F_(d+1)(T^+,pi_(d+1))=F_d(T,pi_d)(0,d)^2.             (2.4)
```

**Two-slot erasure lemma.**  Interchanging the adjacent labels between two
consecutive slots can be calculated after erasing every complete interval
outside those slots.  Such an interval has the same nested LIFO matching on
both sides of the comparison and reduces to one `S` by (2.1).  The only
data left are the two tree edges and whether they have a common endpoint.
For two distinct tree edges, the exhaustive possibilities are: a common
parent, either parent-child orientation, or disjointness.

For completeness, the literal symbolic scan for an internal cut is shown
below.  Let `i=2v-2`, let `r=p(v)`, `s=p(v+1)`, and list labels
`i-1,i,i+1,i+2`.  After the edit their first black endpoints are always

```text
b_1=(v,v+1,v,v+1).
```

Repeated use of (2.1) on the four contracted incidence skeletons gives:

| incidence | last distance-three endpoints `b_2` |
|---|---|
| `r=s` | `(r,r,v+1,r)` |
| `s=v` | `(r,r,r,v)` |
| `r=v+1` | `(s,v,s,s)` |
| otherwise | `(r,s,r,s)` |

This table is an all-rank symbolic reduction: subtrees and the contracted
path between disjoint edges consist only of complete nested intervals, so
they are removed before the displayed skeleton.  Conversely, expanding any
erased interval reverses the same distance-one rows and cannot change a last
distance-three endpoint in the table.  This proves both locality and the
claim that every unshown factor remains its canonical factor from (2.3).

## 3. Internal even edits

Let

```text
i=2v-2<=2d-6,     2<=v<=d-2,
e=(v-1,p(v)-1),   f=(v,p(v+1)-1).                    (3.1)
```

Translating the endpoint table of Section 2 through (2.2), the exact
four-factor window at positions `i-1,i,i+1,i+2` is

```text
p(v)=p(v+1): D_v=[e,f,fef,f];
p(v+1)=v:    D_v=[e,efe,e,f];
p(v)=v+1:    D_v=[c,e,c,f],  c=fef=efe;
otherwise:   D_v=[e,f,e,f].                          (3.2)
```

In the last line `e,f` are disjoint.  In the third line they meet in one
endpoint, so the two conjugates are the same third transposition.  The tree
property makes the four lines exhaustive.

Passing from root `d` to root `d+1` changes only `p(1)`, from `d`
to `d+1`.  Since `v,v+1>=2` and `v+1<=d-1`, neither edge in (3.1)
changes.  The incidence case and every factor in (3.2) are therefore
identical at both ranks.  All factors outside the window agree by the
two-slot erasure lemma and (2.4).  Hence

```text
N_i=A_i                                                     (3.3)
```

with the empty route.  In particular, there is no hidden exceptional
internal-even row.

## 4. The cross-boundary edit `i=2d-4`

Put

```text
alpha=m-1, beta=m, gamma=m+1, delta=m+2,
j=m-3,
h=(d-2,p(d-1)-1),
g=(0,d-1), k=(0,d),
a=ghg, b=aga.                                          (4.1)
```

The root `d` is a leaf adjacent only to `1`.  Hence `h` and `g`
meet exactly when `p(d-1)=1`; otherwise they are disjoint.

At rank `d`, the edit swaps `R_(d-1)=m-2` with the root-slot port
`alpha=m-1`.  It is therefore across the cyclic physical seam between
the last ordinary slot and the root-child slot, even though its two numeric
labels are adjacent.  Contracting all other complete intervals leaves the
following literal DPS endpoint table.  An asterisk means that no
distance-three row survives and Step 4 supplies the displayed root.

| label | old `b_1` | old `b_2`, `p(d-1)=1` | old `b_2`, `p(d-1)!=1` |
|---|---:|---:|---:|
| `j` | `d-1` | `*d` | `p(d-1)` |
| `j+1` | `1` | `d-1` | `*d` |
| `alpha` | `d-1` | `*d` | `p(d-1)` |
| `beta` | `1` | `*d` | `*d` |

Thus the old four factors are uniformly

```text
N_(j,j+1,alpha,beta)=[a,b,a,g].                       (4.2)
```

At rank `d+1`, the old root becomes the new child `d` in slot
`(alpha,beta)`, while the new root-child slot is `(gamma,delta)`.
The same contracted LIFO scan gives:

| label | new `b_1` | new `b_2` |
|---|---:|---:|
| `j` | `d-1` | `p(d-1)` |
| `j+1` | `d` | `1` |
| `alpha` | `d-1` | `d` if `p(d-1)=1`, otherwise `p(d-1)` |
| `beta` | `d` | `1` |
| `gamma` | `1` | `*(d+1)` |
| `delta` | `1` | `*(d+1)` |

Consequently, including the old padding in (1.1),

```text
N_(j,j+1,alpha,beta,gamma,delta)=[a,b,a,g,k,k],
A_(j,j+1,alpha,beta,gamma,delta)=[h,g,a,g,k,k].       (4.3)
```

All earlier factors agree by the same complete-interval erasure.  Notice
that (4.3) includes both post-wrap regimes.  When `p(d-1)=1`, the old
`j,alpha` ports default across the wrap to root `d`, while the new
`alpha` port closes to child `d`.  When `p(d-1)!=1`, `h` is
disjoint from `g`, the inherited-parent records persist, and the remaining
high ports default exactly as displayed.  The new root ports
`gamma,delta` close the numeric wrap `delta -> 1` and both give `k`.

## 5. The last edit `i=2d-3`

This edit reverses `(alpha,beta)`.  At rank `d` that is the old
root-child slot; at rank `d+1` it is the new-child-`d` slot.  The
new root-child slot `(gamma,delta)` itself is not edited.  The exact
seam endpoint table is:

| label | old `b_1` | old `b_2` | new `b_1` | new `b_2` |
|---|---:|---:|---:|---:|
| `alpha` | `1` | `*d` | `d` | `1` |
| `beta` | `1` | `*d` | `d` | `*(d+1)` |
| `gamma` | padding | padding | `1` | `d` |
| `delta` | padding | padding | `1` | `*(d+1)` |

The nondefault new seam rows are `alpha -> B_1` and then
`gamma -> B_d` in forward LIFO chronology; inverse closure opens the
`gamma` row before the `alpha` row.  Translating the table gives

```text
N_(alpha,beta,gamma,delta)=[g,g,k,k],
A_(alpha,beta,gamma,delta)=[g,gkg,g,k].               (5.1)
```

Every lower factor agrees.  This explicitly includes the interaction after
the physical root wrap: `gamma` records the old root/new child `d`,
whereas `delta` defaults to the new final root.

## 6. Unconditional tuple identities and signs

For the cross-boundary case, `b=aga` and `a=ghg`.  Therefore two
chronological negative moves give

```text
[a,b,a] --R_j^(-1)--> [aba,a,a]=[g,a,a]
        --R_j^(-1)--> [gag,g,a]=[h,g,a].              (6.1)
```

This calculation is valid whether `h,g` meet or are disjoint.  In the
disjoint case `a=h,b=g`, the first negative move swaps `h,g` and the
second swaps them back.  Thus (6.1) does not use the false unrestricted
identity `[a,b,a]->[b,aba,a]` rejected in M242.

For the last edit, one chronological negative move at `beta=m` gives

```text
[g,k] --R_beta^(-1)--> [gkg,g].                       (6.2)
```

Equations (4.3), (5.1), (6.1), and (6.2) prove the last two lines of
(1.3).  The inverse routes, from `A_i` back to `N_i`, are respectively
`R_j,R_j` and `R_beta`.  There are no suppressed sign changes.

## 7. Minimal rank and all seams

At `d=5`, `m=8`.  The internal-even cases are exactly `i=2,4`
(`v=2,3`), the cross-boundary case is `i=6` with two
`R_5^(-1)` moves, and the last case is `i=7` with
`R_8^(-1)`.  The old root slot is `(7,8)`; after extension, child
`5` occupies `(7,8)` and the new root slot is `(9,10)`.  Hence
every index in Sections 3--6 exists and no interval collapses onto a
different slot.

There are exactly two cross-boundary geometric regimes,
`p(4)=1` and `p(4)!=1`, already retained in the tables of Section 4.
The numeric post-wrap from `delta=10` to `1` is retained in Section 5.
Thus `d=5`, root-leaf placement, new-child placement, and both post-wrap
possibilities introduce no exception.

## 8. Guard boundary

Only after equations (3.2), (4.3), and (5.1) were frozen in
`checkpoint.md`, a no-predecessor-import guard was authorized for all
root-leaf templates at `d=5,6`.  It reconstructs RandomQuad Steps 3--4
from the locked source, checks the literal endpoint windows and routes, and
records incidence-class counts.  This finite check can falsify an indexing,
sign, minimal-rank, or wrap transcription; the all-rank proof is the
symbolic complete-interval erasure above.

## 9. Formal composition and strict stopping line

Accepted M269/M271 plus the accepted standalone DL-RST M273/M275 license the
ordinary-edit endpoint output while replacing, not reviving, false M250
(4.2).  M250/M254 then license ordinary IDL by conditional endpoint
exhaustion, and M240/M242 give the ordinary odd-edit route

```text
Q(v,epsilon) B_d Q(v,epsilon)^(-1)
```

of length `4(d-v-1)+5<=4d-7`.  The present theorem supplies the three
previously omitted fixed families, of lengths `0,2,1`, respectively.
Subject to a fresh audit of this theorem, the formal local rooted-row route
table therefore covers every adjacent edit index at length at most
`4d-7`.

This is not yet a separate assembly theorem.  It does **not** establish
every-color synchronization, voltage correction, other routing obligations,
congestion, a spectral gap, polynomial mixing, or Terminal A/B.
