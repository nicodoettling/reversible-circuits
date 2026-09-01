# M122 final report: rooted-product local comparison

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, and scope

```text
FINAL VERDICT: KEEP AS A SCOPED THEOREM/OBSTRUCTION.
PROVED: an infinite linear DPS star cascade, its route lower bound,
        a universal source-recoverable O(d^2) full twist, and a sharper
        O(d) route for this star family.
REFUTED: bounded-output and O(1)-route locality for every adjacent DPS swap.
UNRESOLVED: all-edge congestion and ROOTED PRODUCT LOCAL COMPARISON.
```

The target is uniform on

```text
Z_d={w=(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  The physical auxiliary kernel is

```text
P_(0,d)=I/2+[1/(4(2d-3))]sum_i(R_i+R_i^(-1)),
R_i(a,b)=(b,bab), R_i^(-1)(a,b)=(aba,a).
```

This mission uses the accepted M112/M119 bijection
`rooted Z_d <-> UST(K_d) x S_(2d-2)`.  It proves no gap for `P_(0,d)`, no
arbitrary-product `Gamma_0` theorem, no `{3,4,5}` heat-bath gap, and neither
Terminal A nor Terminal B.

```text
candidate                 | fixed braid route for one infinite DPS ideal-edge family
claimed target            | uniform rooted minimal identity sector Z_d
identity ok               | proved; exact convention checks d=3..24
crosses Hurwitz components| not applicable; one connected minimal identity orbit
exact diagnostics         | closure tables, endpoint, path, prefix inversion, root factor
verdict                    | keep scoped theorem/obstruction; global comparison unresolved
```

## 2. Strongest exact result

For every `d>=3`, take the Cayley star

```text
T_d={{1,k}:2<=k<=d}
```

centered at white `y_1`, with white root `y_d`, and take `pi=id` in
`S_(2d-2)`.  Swap the adjacent values `1,2` of `pi`, keeping `T_d` fixed.
The universal DPS contour calculation in `star_cascade_obstruction.md`
proves that the two rooted states close to

```text
w_d =((1,d),(1,d),(1,2),(1,2),...,(1,d-1),(1,d-1)),
w'_d=((1,d),(1,d),(2,d),(2,d),...,(d-1,d),(d-1,d)).
```

Thus this one adjacent ideal permutation edit changes exactly `2d-4` of
`2d-2` physical factors.  Since a signed adjacent-Hurwitz move changes at
most two positions, every physical route has length at least `d-2`.
Accordingly, the named bounded-locality premises are rigorously refuted:

```text
all adjacent DPS value swaps change O(1) output factors;             REFUTED
all adjacent DPS value swaps admit O(1)-length Hurwitz routes.       REFUTED
```

This is not evidence of superpolynomial distance or congestion.  Linear
routes are compatible with polynomial comparison.

## 3. Universal full twist and sharper star route

For any transpositions `h,u_1,...,u_L` with `u_1...u_L=id`, put

```text
C_L=R_2 R_3 ... R_(L+1).
```

A direct cyclic-shift calculation proves that the full twist

```text
C_L^(L+1)
```

sends

```text
(h,h,u_1,...,u_L) -> (h,h,h u_1 h,...,h u_L h).
```

Indeed, on any `n`-tuple with product `P`, one sweep
`R_1...R_(n-1)` moves the first entry to the end conjugated by `P`; `n`
sweeps restore order and conjugate every entry by `P`.  Here the selected
subtuple product is `hU=h`.  The schedule has length `L(L+1)=O(L^2)`, depends
only on `L`, and works without an endpoint-incidence hypothesis.

For fixed direction, scheduled time, and full-twist descriptor, the source is
unique: invert the known action prefix.  If scheduled holding actions are
deleted and the descriptor retains only compressed physical-path time, at
most `L(L+1)` scheduled times can represent that compressed time.  The
resulting recovery multiplicity is therefore still polynomial, though not
literally one without scheduled time.

A shorter route is available when `u_L=h` or `u_L` shares one endpoint with
`h`.  In that case the fixed action word

```text
R_2 R_3 ... R_L R_(L+1)^(-1) R_L ... R_3 R_2
```

sends

```text
(h,h,u_1,...,u_L) -> (h,h,h u_1 h,...,h u_L h).
```

This is **PROVED** by pushing the second `h` across `u_1,...,u_(L-1)`, using
`u_1...u_(L-1)=u_L` and the shared-endpoint transposition braid relation at
the turn, and pushing the resulting `h` back left.  The route has length
`2L-1` and its positions/signs depend only on `L`.

For the DPS star family, `h=(1,d)`, `L=2d-4`, and the suffix ends in
`(1,d-1)`, so this gives a path of length `4d-9`.  All actions are
off-diagonal; all intermediates remain in `Z_d`.

The same prefix-inversion argument gives exact conditional source multiplicity
one for this shorter route.  Neither recovery statement bounds the number of
different ideal descriptors whose routes meet a physical edge.

## 4. Exact root-quotient accounting for this demand

The rooted lift has stationary mass `1/(d|Z_d|)` and refreshes the new root
uniformly after each word move.  Choose a deterministic root sequence between
the prescribed endpoint roots.  If `M=2d-2`, a specified lifted physical
action has capacity at least

```text
[1/(d|Z_d|)] [1/(4(M-1))] [1/d],
```

whereas the corresponding ideal permutation-coordinate edge in the equal
product mixture has capacity

```text
[1/(d|Z_d|)] [1/(4(M-1))].
```

The exact root refresh therefore costs a factor `d` for this single demand.
The universal full twist has single-demand load at most
`d(2d-4)(2d-3)=O(d^3)`; the shorter star route improves this to
`d(4d-9)=O(d^2)`.  This does not sum all ideal demands and is not an all-edge
congestion bound.

## 5. Boundary of the shorter route

The shared-endpoint hypothesis cannot be removed from the shorter `2L-1`
action word.  With disjoint

```text
h=(1,4), u=(2,3), U=(u,u),
```

the same action word `R_2 R_3^(-1) R_2` maps

```text
(h,h,u,u) -> (h,u,u,h),
```

not to the componentwise conjugated target `(h,h,u,u)`.  The six-action full
twist `(R_2R_3)^3` does return the target.  This exact example only refutes
overgeneralizing the shorter word; it has disconnected support and is not a
`Z_d` counterexample.

## 6. Universal DPS proof versus finite audit

The proof note derives the hairy-tree cyclic contours for `pi` and its swap
for arbitrary `d`.  It then performs the stack cancellation symbolically:

| rooted input | distance-one closures | distance-three closures | other black |
|---|---|---|---|
| `(T_d,pi)` | `d-2` for labels `1,2`; `d-3` for `3..m` | one for `3..m` | `x_1` |
| `(T_d,pi')` | `d-2` for every label | none | new `x_d` |

This is the completeness argument for the displayed words.  The script is an
independent finite convention/falsification audit, not the universal proof.
It imports no predecessor module and, for every `d=3,...,24`, checks:

- both DPS closure formulas and the complete closure-count tables;
- identity, connected support, and exact factor Hamming distance;
- the `d-2` Hamming lower bound and `4d-9` shorter route length;
- the `L(L+1)` full-twist schedule and both route endpoints;
- every intermediate identity/support and every shorter-route off-diagonal
  action;
- unique recovery from every scheduled prefix of both routes;
- failure of the shorter word, and success of the full twist, in the
  disjoint-last-factor example.

All finite checks pass.  The rows for `d=3,4,5` are exact instances of the
same symbolic family; no random or sampled inference is used.

## 7. First remaining lemma

The first open obligation remains:

> **ROOTED PRODUCT LOCAL COMPARISON.**  Route every adjacent-value permutation
> swap and every UST basis exchange through signed adjacent-Hurwitz paths with
> polynomial length and polynomial stationary edge congestion, including the
> exact white-root quotient.

M122 narrows the acceptable proof shape: it must permit linear closure
cascades.  The square-prefix route handles only one structured mechanism.
Arbitrary nested stack changes, repeated face transpositions, and the total
number/weight of ideal descriptors crossing one physical edge remain
uncontrolled.  Tree basis exchanges receive no new universal route here.

## 8. Reproduction, dependencies, and hygiene

Primary combinatorial input: Duchi--Poulalhon--Schaeffer, Proposition 3 and
Theorem 5, as already source-audited by M119.  No new external theorem is
used.

Deterministic command, Python `3.12.3`, dependencies `{}`, seed `null`:

```text
python3 -B star_cascade_audit.py --min-d 3 --max-d 24 \
  --output star_cascade_results.json
```

Owned artifacts are `plan.md`, `checkpoint.md`,
`star_cascade_obstruction.md`, `star_cascade_audit.py`,
`star_cascade_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  No manuscript, coordinator file, project skill, predecessor
artifact, or file outside the owned mission directory is edited.

```text
FINAL VERDICT: KEEP AS A SCOPED THEOREM/OBSTRUCTION; GLOBAL COMPARISON OPEN.
```
