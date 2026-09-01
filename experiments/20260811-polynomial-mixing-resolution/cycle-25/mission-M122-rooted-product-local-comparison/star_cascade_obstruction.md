# A linear DPS closure cascade with a recoverable braid route

Date: 2026-08-12.

## 1. Scope, target, and convention

For `d>=2`, let

```text
Z_d={w=(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, and displayed tuple factors
multiply left-to-right.  A right signed Hurwitz generator is

```text
R_i(...,a,b,...)= (...,b,bab,...),
R_i^(-1)(...,a,b,...)=(...,aba,a,...).
```

The physical auxiliary kernel is

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_(i=1)^(2d-3)(R_i+R_i^(-1)).
```

M112/M119 are accepted inputs for the exact rooted DPS bijection

```text
rooted Z_d <--> {Cayley trees on [d]} x S_(2d-2).
```

This note proves one explicit ideal-edge theorem and refutes bounded closure
locality.  It does **not** prove the ROOTED PRODUCT LOCAL COMPARISON, a gap for
`P_(0,d)`, any arbitrary-product `Gamma_0` estimate, or the `{3,4,5}`
heat-bath gap.

## 2. The exact rooted star edge

Use the accepted `+`-mirror DPS convention.  Write the white vertices as
`y_1,...,y_d`, take `y_d` as root, and let

```text
T_d={{1,k}: 2<=k<=d}
```

be the Cayley star centered at `y_1`.  Put `m=2d-2`.  Let `pi` be the identity
permutation in `S_m`, and let `pi'=(1 2) pi`, meaning that the adjacent values
`1,2` are interchanged wherever they occur.  This is one nontrivial ideal
permutation-coordinate edge for every `d>=3`.

### Proposition 2.1 (exact DPS star cascade; **PROVED**)

The two rooted product states `(T_d,pi)` and `(T_d,pi')` close to

```text
w_d =((1,d),(1,d),(1,2),(1,2),...,(1,d-1),(1,d-1)),
w'_d=((1,d),(1,d),(2,d),(2,d),...,(d-1,d),(d-1,d)).       (2.1)
```

Both words lie in `Z_d`.

#### Proof

DPS Proposition 3 inserts `x_i` on the first edge from `y_i` toward the root.
Thus `x_1` lies between `y_1,y_d`, while for `2<=i<=d-1`, `x_i` lies between
`y_i,y_1`.  For `pi=id`, the incidences are

```text
x_1--y_1 has label 1,       x_1--y_d has label 2,
x_i--y_i has label 2i-1,    x_i--y_1 has label 2i  (2<=i<d).     (2.2)
```

For `pi'`, only the labels on the two halves incident with `x_1` are
interchanged.

Here is a direct symbolic audit of the DPS stack closure for arbitrary `d`.
It is included to make (2.1) a proof rather than an extrapolation from small
ranks.  Complete every white rotation increasingly and every black rotation
decreasingly, as in DPS Theorem 5.  Let `W_i^a` (respectively `B_i^a`) denote
the loose half-edge of label `a` at `y_i` (respectively `x_i`).  Brackets
`[a up b]` and `[a down b]` list a cyclic interval of labels modulo `m`, with
endpoints included.

With (2.2), the loose half-edges on the outer contour, in cyclic order, are

```text
W_1^2 W_1^3
prod_(i=2)^(d-2) (
  W_i^[2i up 2i-2] B_i^[2i-2 down 2i+1] W_1^(2i+1)
)
W_(d-1)^[m up m-2] B_(d-1)^[m-2 down 1]
B_1^[m down 3] W_d^[3 up 1].                            (2.3)
```

The product is empty at `d=3`.  Formula (2.3) follows by walking each actual
tree edge twice: the only absent label at `y_i`, `2<=i<d`, is `2i-1`; the
only absent labels at `x_i` are `2i-1,2i`; at `y_1` the actual labels are
`1,4,6,...,m`; and at `y_d` the only actual label is `2`.

Now run the LIFO local closure.  At each leaf branch `i=2,...,d-1`, every
label except `2i-1,2i` closes between a white and black half-edge based at
that branch, at boundary distance one.  Reading (2.3) by descending cyclic
label and then increasing `i` proves this assertion inductively: deleting
one such pair shortens the displayed white and black cyclic intervals by one
at the same end and exposes the next pair.  Hence labels `1,2` each undergo
`d-2` distance-one closures, while every label `3,...,m` undergoes `d-3`.

After exactly these distance-one closures, the reduced cyclic half-edge
boundary is

```text
W_(d-1)^m,
B_1^m B_1^(m-1) ... B_1^3,
W_d^3 W_d^4 ... W_d^m W_d^1,
W_1^2 A_3 A_4 ... A_(m-1),                              (2.4)
```

where `A_a=W_1^a` for odd `a`, and `A_(2i)=W_i^(2i)` for even
`a=2i`.  The first pair `W_(d-1)^m,B_1^m` is at distance three.  Closing it
exposes `A_(m-1),B_1^(m-1)` at distance three; continuing downward exposes
`A_a,B_1^a` for `a=m-2,...,3`.  This is again a literal induction on (2.4):
each closure replaces the enclosed three sides by one outer closure side.
There is therefore exactly one distance-three closure for every label
`3,...,m`, and its black endpoint is `x_1`.  The final unmatched white set is

```text
W_d^3,W_d^4,...,W_d^m,W_d^1,W_1^2,                     (2.5)
```

one half-edge of every label; DPS attaches these to the new black vertex
`x_d`.

For `pi'`, the cyclic contour is instead

```text
W_d^[2 up m] B_1^[m down 3] W_1^3
prod_(i=2)^(d-2) (
  W_i^[2i up 2i-2] B_i^[2i-2 down 2i+1] W_1^(2i+1)
)
W_(d-1)^[m up m-2] B_(d-1)^[m-2 down 1] W_1^1.          (2.6)
```

The same branchwise induction closes every non-incident label internally at
each `x_i`, `2<=i<d`.  The initial root block now also closes every label
`3,...,m` between `y_d` and `x_1` at distance one.  Thus every label has
exactly `d-2` distance-one closures and there is no distance-three closure.
The unmatched white half-edges are

```text
W_1^1,W_d^2,W_1^3,W_2^4,W_1^5,W_3^6,...,
W_1^(m-1),W_(d-1)^m,                                    (2.7)
```

again one of every label, all attached to `x_d`.

In the DPS closure, a distance-one closure makes a digon that is contracted.
A distance-three closure makes the quadrangle of that face label; its two
black vertices give the corresponding factor.  Therefore labels `1,2` in
the first case give `(x_1,x_d)`, while labels `2i-1,2i`, `i>=2`, give
`(x_1,x_i)`.  In the second case every label uses the new `x_d`, so labels
`2i-1,2i` give `(x_i,x_d)`.  Relabeling `x_i` by sheet `i` proves (2.1).
Each displayed factor occurs in an adjacent square, so the product is
identity.  Each support graph is a star on all `d` sheets, hence connected.
QED.

The closure calculation can be summarized as follows.

| rooted input | distance-one closures | distance-three closures | other black vertex |
|---|---|---|---|
| `(T_d,pi)` | `d-2` for labels `1,2`; `d-3` for `3..m` | one for every `3..m` | `x_1` |
| `(T_d,pi')` | `d-2` for every label | none | new `x_d` |

## 3. A rigorous locality obstruction

### Corollary 3.1 (linear factor cascade and route lower bound; **PROVED**)

The ideal adjacent-value edge in Proposition 2.1 changes exactly `2d-4` of
the `2d-2` output factors.  Every signed adjacent-Hurwitz path from `w_d` to
`w'_d` has length at least `d-2`.

#### Proof

The first two factors in (2.1) agree.  At each remaining position, `(1,k)`
and `(k,d)` are distinct because `2<=k<=d-1`.  Thus the factor Hamming
distance is `2d-4`.  One signed Hurwitz move changes only its two selected
coordinates, so the Hamming distance between its endpoints is at most two.
The triangle inequality along a path of length `r` gives `2d-4<=2r`.
QED.

Consequently both named assertions

```text
every adjacent DPS face-label swap changes O(1) output factors;
every adjacent DPS face-label swap has an O(1)-length Hurwitz simulation
```

are **REFUTED**.  This is not an obstruction to polynomial comparison:
linear-length routes are permitted.

## 4. Fixed recoverable routes through the cascade

The star cascade is a square-prefix conjugation.  A full twist gives a robust
route for every identity suffix; a shorter route is available under an extra
endpoint-incidence condition.

### Lemma 4.1 (universal square-prefix full twist; **PROVED**)

Let `h,u_1,...,u_L` be transpositions, `L>=2`, with

```text
u_1...u_L=id.
```

Put

```text
C_L=R_2 R_3 ... R_(L+1),
F_L=C_L^(L+1).                                           (4.1)
```

Then

```text
F_L(h,h,u_1,...,u_L)
  =(h,h,h u_1 h,...,h u_L h).                           (4.2)
```

The scheduled word has length `L(L+1)` and depends only on `L`.  Deleting
scheduled actions that happen to hold gives a physical path of length at most
`L(L+1)`.

#### Proof

First consider any group tuple `(g_1,...,g_n)`, using the usual extension
`R_i(a,b)=(b,b^(-1)ab)`, with product `P=g_1...g_n`.  Applying
`R_1,...,R_(n-1)` pushes `g_1` through the other entries.  If
`A=g_2...g_n=g_1^(-1)P`, the last entry is

```text
A^(-1) g_1 A=P^(-1)g_1P.
```

Thus

```text
(R_1...R_(n-1))(g_1,...,g_n)
  =(g_2,...,g_n,P^(-1)g_1P).                            (4.3)
```

Hurwitz moves preserve `P`.  Iterating (4.3) exactly `n` times restores the
order and conjugates every entry by `P`:

```text
(R_1...R_(n-1))^n(g_1,...,g_n)
  =(P^(-1)g_1P,...,P^(-1)g_nP).                         (4.4)
```

Apply this to the subtuple in global positions `2,...,L+2`, namely
`(h,u_1,...,u_L)`.  Its product is `P=h`, because the suffix product is
identity, and `h^(-1)=h`.  Equation (4.4) gives (4.2).  There are `L`
generators per sweep and `L+1` sweeps.  QED.

For Proposition 2.1, take

```text
h=(1,d),
U=((1,2),(1,2),...,(1,d-1),(1,d-1)),
L=2d-4.
```

Conjugating `(1,k)` by `h` gives `(k,d)`.  Hence (4.1) gives a universal
source-independent route from `w_d` to `w'_d` of scheduled length

```text
(2d-4)(2d-3)=O(d^2).                                    (4.5)
```

Every nontrivial intermediate remains in `Z_d`: signed Hurwitz moves preserve
the ordered product and generated subgroup, while `w_d` is transitive.

### Corollary 4.2 (full-twist source recovery; **PROVED**)

Fix `L`, a direction of (4.1), and a scheduled time.  Given the physical
oriented edge at that time, the route source is unique: apply the inverses of
the known scheduled prefix actions in reverse order.  This remains true when
some earlier scheduled actions held, because every `R_i` is a bijection.
Thus source multiplicity conditional on this full-twist descriptor and time
is exactly one over every identity suffix `U`.

If holding actions are removed and only compressed physical-path time is
retained, at most `L(L+1)` scheduled times can map to that time.  The recovery
multiplicity is then at most `L(L+1)`, still polynomial.

This is conditional descriptor recovery.  It does not count how many
different ideal-edge descriptors use one physical edge.

### Lemma 4.3 (shorter shared-endpoint route; **PROVED**)

Under the hypotheses of Lemma 4.1, additionally assume `u_L=h` or `u_L`
shares exactly one endpoint with `h`.  Then

```text
A_L=R_2 R_3 ... R_L R_(L+1)^(-1) R_L ... R_3 R_2        (4.6)
```

also gives (4.2), now in `2L-1` scheduled moves.

#### Proof

Write `U_r=u_1...u_r`.  The first `L-1` moves push the second `h` rightward
and leave the penultimate factor

```text
U_(L-1)^(-1) h U_(L-1)=u_L h u_L=:k.
```

If `u_L=h`, then `k u_L k=h` and `k=h u_L h`.  If they share one endpoint,
the rank-two transposition braid identity gives
`u_L h u_L=h u_L h`, and conjugating `u_L` by the third transposition gives
`k u_L k=h`.  The middle inverse move therefore sends `(k,u_L)` to
`(h,h u_L h)`.  Finally `R_L,...,R_2` move this `h` left, using

```text
(u_i,h)->(h,h u_i h).
```

This proves (4.2), and the length is `(L-1)+1+(L-1)=2L-1`.  QED.

The DPS star suffix ends in `(1,d-1)`, which shares endpoint `1` with `h`.
Thus (4.6) sharpens (4.5) for this family to an off-diagonal path of length

```text
4d-9.                                                    (4.7)
```

During its forward half the moving transposition alternates between `(1,d)`
and `(k,d)` while crossing `(1,k),(1,k)`; during its reverse half `(1,d)`
crosses `(1,k)`.  Its middle pair is `(d-1,d),(1,d-1)`, so every action is
nontrivial.  Prefix inversion again gives conditional source multiplicity one.

### Exact white-root accounting for this single edge

The spectrum-preserving rooted lift has stationary mass
`1/(d |Z_d|)` per rooted state and refreshes the new root uniformly after
each physical word move.  Choose any deterministic intermediate root sequence
with the prescribed endpoint roots.  Every lifted step is legal.  Put
`M=2d-2`.  For one specified nontrivial signed action its lifted capacity is
at least

```text
[1/(d|Z_d|)] [1/(4(M-1))] [1/d].                       (4.8)
```

The corresponding permutation-coordinate ideal edge in the equal product
mixture has capacity

```text
[1/(d|Z_d|)] [1/(4(M-1))].                             (4.9)
```

Thus exact root refresh costs a factor `d` for this routed demand.  The full
twist contributes at most `d(2d-4)(2d-3)=O(d^3)` single-demand load; the
shorter star route improves this to `d(4d-9)=O(d^2)`.  Neither calculation
bounds the sum of all ideal demands using a physical edge; that all-edge
congestion is the missing theorem.

## 5. Why the shorter-route hypothesis cannot be dropped

### Proposition 5.1 (disjoint-last-factor counterexample; **PROVED**)

The shorter statement of Lemma 4.3 is false if `u_L` is disjoint from `h`.
The full twist in Lemma 4.1 remains valid.  Let

```text
h=(1,4), u=(2,3), U=(u,u), L=2.
```

Then componentwise conjugation by `h` fixes `U`, so the claimed target would
be `(h,h,u,u)`.  But (4.6) is `R_2 R_3^(-1) R_2`, and direct use of
`hu=uh` gives

```text
(h,h,u,u) -> (h,u,h,u) -> (h,u,u,h) -> (h,u,u,h),
```

which differs from the claimed target.  By contrast, the six-action full
twist `(R_2R_3)^3` returns the claimed componentwise conjugated tuple.  This
example only refutes overgeneralizing the shorter word; its support is
disconnected and it is not a counterexample in `Z_d`.

## 6. What remains unresolved

The star family shows that a useful proof must tolerate linear stack cascades,
but it also shows that such a cascade can have a short, perfectly recoverable
route.  The unresolved ROOTED PRODUCT LOCAL COMPARISON still requires, for
**every** adjacent-value edit and UST basis exchange:

1. a polynomial-length signed-Hurwitz route;
2. a polynomial bound on the number/weight of route descriptors meeting each
   physical lifted edge, including all `d` roots;
3. the resulting stationary congestion bound.

Nothing proves that a general adjacent DPS edit decomposes into polynomially
many square-prefix conjugations of the form in Lemma 4.1; arbitrary nested
stack changes and the descriptor sum remain open.  Nothing here applies
automatically to arbitrary-product `Gamma_0` sectors.
