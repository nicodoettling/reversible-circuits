# Conditional quotient routing for anchored doubled-tree representatives

Date: 2026-08-13 UTC.

## 1. Scope and conventions

Let `d>=5`, `m=2d-2`, `G=S_d`, `H=Stab_G(d)`,

```text
Z_d={(t_1,...,t_m):t_1...t_m=id, support connected on [d]},
Q_d=Z_d/G.
```

Permutations compose as `(p q)(x)=p(q(x))`.  Signed Hurwitz symbols are
chronological and

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

M181 supplies the source words `W_epsilon`, each an ordered concatenation of
`d-1` doubled tree edges.  M135 associates, for a fixed adjacent DPS value
edit `tau_i`, an `H`-orbit edge over each source quotient point.  This note
addresses only whether one braid sends an ordered M181 source quotient tuple
to the quotient tuple of its matched physical DPS targets.

## 2. The representative gap

Fix a perfect-matching color and a constructed source quotient vertex
`q_c=[W_c]`.  The color selects one edge

```text
Q_c=H.u_c,
```

where `u_c=alpha_c.W_c` for some generally arbitrary `alpha_c in G`.  Its
right endpoint is

```text
r_c=[tau_i(u_c)].                                      (2.1)
```

The accepted equivariances have different ranges:

```text
b(alpha.w)=alpha.b(w)      for every braid b and alpha in G,
tau_i(h.w)=h.tau_i(w)      only for h in H.             (2.2)
```

M181 uses the first identity to transfer source stabilizer loops from `W_c`
to `u_c`.  It cannot use that identity for (2.1) when `alpha_c` moves the
distinguished root.  Thus the full source voltage theorem proves no quotient
route to the matched target.  Perfectness adds only uniqueness of the chosen
`H`-orbit over every left quotient and distinctness of right endpoints; it
does not select a rooted coordinate for which `tau_i` is block-local.

This is a logical obstruction to the proposed every-color proof, not a proof
that an arbitrary selected tuple is unreachable.  In particular, the
accepted generated-subgroup and factor-class tests are necessary only and
are not assumed sufficient.

## 3. A narrow conditional representative theorem

Write a doubled-tree source as

```text
W=(e_1,e_1,e_2,e_2,...,e_(d-1),e_(d-1)),              (3.1)
```

where the distinct edges `e_k` form a tree on `[d]`.  Choose a white root
`rho`, relabel it to the distinguished DPS root, and let `(T,pi)` be the
corresponding accepted rooted DPS coordinate of `W`.  Say that this
coordinate is **pair-aligned at `i`** when the edited DPS values `i,i+1`
are exactly the two boundary labels on one inserted black vertex of the
hairy tree.  Say it is **boundary-aligned at `i=2k`** when they are the
touching boundary labels of the consecutive doubled edges `e_k,e_(k+1)`
and these edges are disjoint or their unique common white vertex is `rho`.

The DPS construction gives the following local identities.

### Lemma 3.1 (rooted block-local edit; proved)

For a coordinate satisfying the preceding hypothesis:

1. in the pair-aligned case, swapping values `i,i+1` changes only the order
   of the two sides of one degree-two black vertex.  After root forgetting,
   the closed word is globally conjugate to (3.1), so its quotient endpoint
   is `[W]`;
2. in the boundary-aligned case, the four relevant hairy-tree sides are
   consecutive in the boundary tour.  Exchanging the middle two labels and
   applying the distance-one/distance-three closure is exactly

   ```text
   (e_k,e_k,e_(k+1),e_(k+1))
      -> (e_k,e_(k+1),e_(k+1)^(-1)e_k e_(k+1),e_(k+1)),
   ```

   with every outside factor unchanged.  Hence the quotient endpoint is
   `R_i[W]`.

**Proof.**  In the rooted DPS hairy tree, each nonroot white vertex has one
degree-two black vertex inserted in its first parent edge, and its two edge
labels occupy the paired slots of `pi`.  In the first case the value swap
reverses the two labels on that one black vertex.  The boundary walk meets
the same two sides consecutively and the intrinsic noncrossing closure
reverses their local orientation; forgetting the marked white root makes
the results isomorphic.

In the second case, disjointness or meeting at the root makes the two black
vertex sectors noninterleaving in the cyclic order.  All closure pairs away
from their four sides are identical before and after the value swap.  On the
four-side disk, direct application of the accepted DPS distance-one and
distance-three closure rule gives the displayed right-Hurwitz replacement.
Thus the edit is local and leaves the other factors literal.  If the edges
meet at a nonroot white vertex, their sectors can interleave with its parent
sector and this reduction is not valid; no claim is made in that case. QED.

### Theorem 3.2 (conditional synchronized route; proved)

For an ordered M181 source tuple, suppose the matching-selected edge in every
coordinate has a representative whose rooted DPS coordinate is of the same
type at the common edit index `i`:

- pair-aligned in every coordinate; or
- boundary-aligned in every coordinate.

Then the matched target quotient tuple lies in the source synchronized
component.  The explicit common route is respectively the empty word or the
single generator `R_i`.

**Proof.** Apply Lemma 3.1 coordinatewise.  Since quotient endpoints ignore
the independent global relabelers used to present the rooted representatives,
the same empty word or `R_i` gives every coordinate endpoint. QED.

The hypothesis is genuinely additional.  M135 perfectness does not imply
that a color contains the pair-aligned or boundary-aligned `H`-orbit over any
given left quotient vertex, let alone over all selected vertices.  Therefore
Theorem 3.2 is a conditional anchored-edge routing theorem, not an every-color
theorem.

## 4. Exact targeted `d=5` witnesses

The clean-room checker uses only the width-two M181 source pair

```text
V=(01)^2(02)^2(13)^2(04)^2,
U=(01)^2(02)^2(03)^2(04)^2.                            (4.1)
```

For each word and each of its five white roots it reconstructs one rooted DPS
coordinate by the literal hairy-tree closure, swaps one adjacent pair of DPS
values, and canonically records the target quotient.  Across the seven edit
indices and root pairs, there are 54 distinct eligible target quotient tuples
(the two right endpoints are distinct).  A bounded quotient BFS from (4.1)
to radius five supplies 14 exact positive endpoint certificates, with route
lengths

```text
0,1,1,1,1,1,1,2,2,3,3,3,3,5.
```

For the common gadget anchor as both distinguished roots, the exact positive
routes are

| DPS edit `i` | route |
|---:|---:|
| 1 | empty |
| 2 | `R_2` |
| 3 | empty |
| 4 | `R_4` |
| 6 | `R_6` |
| 7 | empty |

At `i=5`, the two consecutive doubled edges are `(13)` and `(04)`: they are
disjoint, but only the `U` coordinate is pair-trivial in the reconstructed
rooted presentation and no radius-five common certificate was found for the
root-zero pair.  This miss is not used as evidence of nonreachability and is
outside Theorem 3.2's uniform same-type hypothesis.

The other positive paths are stored by the checker.  The finite audit neither
enumerates `Z_5`/`Q_5` nor establishes coverage; the forty targets not found
within radius five have no negative interpretation.  Separate exhaustive
`d=3,4` doubled-tree convention tests found the local identities exactly when
the stated rooted incidence hypotheses held.  Those boundary rows audit the
proof convention and do not replace it.

## 5. Exact conclusion

```text
PROVED: conditional pair-aligned / boundary-aligned synchronized routes.
EXACT FINITE: 14 positive d=5 quotient-route certificates among 54 targets.
UNRESOLVED: every-color quotient reachability for M181's matched targets.
```

No new voltage invariant was sought.  No generated-subgroup/class data were
treated as sufficient.  Full M181 source voltage would solve physical
endpoint orientation only after one of these quotient routes exists.  No
route-length asymptotic, spectral gap, mixing, or Terminal conclusion follows.
