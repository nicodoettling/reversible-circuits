# Synchronized Hurwitz gain graph and relative-orientation cycle space

Date: 2026-08-13 UTC.

## 1. Scope, target, and conventions

Let `d>=3`, `m=2d-2`, and let

```text
Z_d={(t_1,...,t_m): t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Chronological signed right-Hurwitz generators are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

Simultaneous `S_d` relabeling is free on `Z_d` and commutes with the braid
action.  Put `Q_d=Z_d/S_d`.  For ordered width `s`, put

```text
W_s=F_2^s/Delta,       Delta=<(1,...,1)>.
```

The target here is qualitative diagonal signed-Hurwitz orbit lifting in the
relative-orientation cover `Z_d^s/P_(d,s)->Q_d^s`.  No probability law,
Markov kernel, word-length bound, spectral gap, or sampler theorem is
claimed.

## 2. The explicit local orientation cocycle

Choose a section `sigma:Q_d->Z_d`.  For a signed generator
`g in {R_j^(+/-1)}` and `a in Q_d`, freeness gives a unique `rho_g(a) in S_d`
such that

```text
g sigma(a)=rho_g(a).sigma(ga).
```

Define the one-coordinate orientation label

```text
kappa_g(a)=sgn(rho_g(a)) in F_2.                     (2.1)
```

For a tuple vertex `x=(a_1,...,a_s) in Q_d^s`, define the synchronized
relative gain

```text
gamma_g(x)
 =[kappa_g(a_1),...,kappa_g(a_s)] in W_s.             (2.2)
```

This is an explicit local generator/cocycle description.  It requires only
the unique canonicalization transporter in each coordinate.  If
`e=(x --g--> gx)` is a directed edge, write `gamma(e)=gamma_g(x)`.  The
reverse edge is `(gx --g^(-1)--> x)`.  The transporter inverse identity gives

```text
gamma(e^(-1))=gamma(e),                              (2.3)
```

because `W_s` has exponent two.

For a chronological signed word `b=g_L...g_1` tracing vertices
`x_0,x_1,...,x_L`, the accepted groupoid cocycle specializes to

```text
nu(b,x_0)=sum_(ell=1)^L gamma_(g_ell)(x_(ell-1)).     (2.4)
```

Thus every route gain is a sum of explicit local labels.  A single local
label need not be a stabilizer voltage: only a closed synchronized route
represents a point-stabilizer braid.

## 3. The actual synchronized Schreier gain graph

Fix `q in Q_d^s`.  Let `Gamma(q)` be its connected component in the directed
signed-generator Schreier multigraph:

- vertices are tuple quotient states reached from `q`;
- for every signed generator and every vertex retain the directed labeled
  edge `x --g--> gx`;
- retain loops and parallel generator edges.

This is the **actual synchronized action graph**.  It is not the Cartesian
product of independently chosen coordinate routes, and it is not a graph
that forgets generator labels.

Choose a spanning tree `T` of the underlying connected multigraph.  Orient
its root paths away from `q`.  For a vertex `x`, let

```text
p_T(x)=sum {gamma(e): e lies on the tree path q->x}.  (3.1)
```

Equation (2.3) makes this independent of how a tree edge is traversed.  For
every directed edge `e:x->y`, define its chord column

```text
z_T(e)=p_T(x)+gamma(e)+p_T(y) in W_s.                 (3.2)
```

For the two directions of a tree edge this is zero.  Reverse edges have the
same column.  It suffices to retain one direction of every non-tree edge,
but keeping all columns does not change their span.

### Theorem 3.1 (exact realizable cycle-space theorem; **PROVED**)

For every `d>=3`, every width `s`, every `q in Q_d^s`, every section, and
every spanning tree,

```text
V_stab(q)=span_F2 {z_T(e): e is an edge of Gamma(q)}. (3.3)
```

In particular,

```text
dim V_stab(q)=rank of the chord-column matrix,
V_stab(q)=W_s  iff the rank is s-1,
V_stab(q)=0    iff every chord column is zero.         (3.4)
```

The last condition says precisely that the `W_s`-gain graph is balanced.

**Proof.**  Let `e:x->y` be a directed edge.  Follow the unique tree path
from `q` to `x`, traverse `e`, then follow the inverse tree path from `y`
back to `q`.  This is an actual chronological signed braid word fixing `q`
in the quotient.  Equations (2.3)--(3.2) show that its voltage is `z_T(e)`.
Thus every column lies in `V_stab(q)`, and their span is contained in it.

Conversely, take a point-stabilizer braid and its closed walk `C` in
`Gamma(q)`.  Insert after each directed edge `e:x->y` the tree route
`q->x`, its inverse, and the corresponding tree route at `y`; equivalently,
use the standard fundamental-cycle decomposition of a closed walk over
`F_2`.  At the gain level all paired tree paths cancel by (2.3), and

```text
gain(C)=sum_(e used by C) z_T(e).
```

The right side is in the chord span.  Equation (2.4) identifies `gain(C)`
with the stabilizer voltage.  This proves the reverse inclusion and (3.3).
Because `dim W_s=s-1`, the first criterion in (3.4) follows.  A gain graph is
balanced exactly when every fundamental cycle has zero gain, equivalently
when all chord columns vanish; this is the second criterion.  QED.

Every column in (3.3) is realizable by the displayed fundamental-cycle braid,
and concatenating these braids realizes every vector in their span.  This is
why (3.3) is not a formal cycle-space relaxation.  The construction may use
an exponentially large tree and yields no polynomial word bound.

## 4. Exact sequence on accepted matching subfamilies

For a nonempty ordered subfamily of an accepted `d>=5` M135 matching,
M169/M172 proves

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,
K_mon(q)=relative_sign^(-1)(V_stab(q)).               (4.1)
```

Combining (3.3) and (4.1) gives the promised explicit description

```text
K_mon(q)/P_(d,s)
 ~= column space of the synchronized chord matrix.   (4.2)
```

This does not decide the rank at `d>=5`.  It reduces that question to a named
finite combinatorial condition on the actual action component.

## 5. Fixed physical endpoints and the affine column-space test

Fix physical tuples `U,V` above quotient vertices `q,r`.  Their choice fixes
the endpoint orientation offset, exactly as in M163/M169.  Assume `r` lies in
`Gamma(q)`.  Let `b_T(q,r)` be the tree route and let

```text
a_T(U,V) in W_s                                      (5.1)
```

be its transporter-parity vector relative to these fixed physical endpoint
lifts.  (When both endpoints equal the section lifts, this is simply
`p_T(r)`.)

### Theorem 5.1 (fixed-endpoint affine cycle-space criterion; **PROVED**)

A quotient route from `q` to `r` with zero relative voltage for the fixed
physical endpoints exists if and only if

```text
a_T(U,V) in span_F2 {z_T(e)}.                         (5.2)
```

Equivalently, the complete fixed-endpoint route-voltage set is

```text
a_T(U,V)+colspan(z_T).                                (5.3)
```

**Proof.**  Every route from `q` to `r`, followed by the inverse tree route,
is a stabilizer loop at `q`; conversely prepend any stabilizer loop to the
tree route.  Hence all route voltages are the tree-route voltage plus
`V_stab(q)`.  Apply Theorem 3.1.  Since `W_s` has exponent two, the affine
coset contains zero exactly when its translate `a_T(U,V)` lies in the
column space.  QED.

Changing the section or independently changing endpoint lifts adds the
accepted endpoint coboundary to `a_T`; it also changes the displayed local
edge labels by the corresponding vertex coboundary.  Chord gains and
`V_stab` are unchanged, while the physical endpoint condition transforms in
the same way.  Thus (5.2) is intrinsic for the declared physical endpoints.
Simultaneously relabeling both members of a matched pair preserves it.

## 6. Exact minimal-rank calibration and falsification

The clean-room checker `relative_orientation_cycle_audit.py` reconstructs
only `d=3,4`; it imports no predecessor module or result.

At `d=3`, `|Q_3|=4`.  The diagonal action on all `16` ordered pairs has two
components, of sizes `4` and `12`.  Their chord ranks are both zero.  This
recovers the accepted exact statement that all rank-three pair stabilizer
voltages are trivial.

At `d=4`, `|Q_4|=120`.  The diagonal ordered-pair action has four components:

```text
(component size, chord rank)
  (120,0), (240,0), (4320,1), (9720,0).               (6.1)
```

Thus universal trivial voltage is false at the exceptional rank four.  A
short literal certificate is the ordered pair of canonical words

```text
u=((01),(01),(02),(02),(03),(03)),
v=((01),(01),(02),(02),(13),(13)).
```

The chronological positive word

```text
R_4 R_3 R_5 R_4                                      (6.2)
```

fixes both absolute quotient points.  Its physical transporters are

```text
rho_u=(2 3),          odd,
rho_v=(0 1)(2 3),    even,                             (6.3)
```

in zero-based labels.  Hence its relative voltage is one and the pair
component has full `W_2` voltage.  The checker directly replays (6.2), not
merely a formal cycle.

The stronger synchronized-character ansatz

```text
kappa_j(a)=theta(a)+theta(R_j a)+c_j                 (6.4)
```

is inconsistent already at `d=3` and again at `d=4`.  Therefore balancedness
of a particular tuple component must not be inferred from a universal
one-coordinate vertex potential plus a generator-only bit.

All statements in this section are **EXACT FINITE** calibration or
falsification facts.  Rank four is outside the accepted `d>=5` matching
theorem; no `d=5` quotient orbit was enumerated and no asymptotic inference is
made.

## 7. First unresolved local-cycle realization lemma

The exact next qualitative statement is:

> **ACCEPTED-MATCHING CHORD-RANK LEMMA.**  For every accepted nonempty
> ordered `d>=5` M135 matching subfamily, determine the span of the explicit
> fundamental-cycle columns (3.2); in particular decide whether its rank is
> `s-1`, and for its specified physical DPS source/target decide membership
> in (5.2).

This is narrower than abstract stabilizer-orbit classification because every
candidate generator is a local canonicalization sign and every relation is
an actual closed synchronized path.  It remains unresolved.  Even rank
`s-1` would be qualitative only: polynomial quotient word length and a short
aligned inner correction remain separate obligations.

No common M135 braid, polynomial matching refinement, polynomial word
length, physical-sector gap, original `{3,4,5}` heat-bath gap, mixing theorem,
or Terminal conclusion follows.

