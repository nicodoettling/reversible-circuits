# Fresh referee report on frozen M60

Date: 2026-08-11.

Frozen bundle reviewed:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/report.md
SHA-256 ded582145111a72968fcd2ae2a89e9c488c0cac7dcf9b1f785c74341aa00df59
```

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The acceptance is scoped exactly as the report is scoped: Claims A--C are
valid, but Claim C controls only cuts `A subseteq F_N` and is not a
terminal theorem for the global chain.

## 1. Identities (2.3)--(2.6) and literal H3 realization

Write `h_a=(v,a)`, `h_b=(v,b)`, and `s=(a,b)`.  With
`(pq)(x)=p(q(x))`,

```text
s(s h_a s)=h_a s
```

because `s^2=id`, proving (2.3).  Also
`s=h_a h_b h_a`, hence

```text
s h_a=h_a h_b,
```

which is (2.4).  Equations (2.5)--(2.6) are the immediate square identities
`h^2=f^2=id`.

The padding exists in every case.  If the nulls are not adjacent and the
opening null is at `p`, the closing null is at least `p+2`, so position
`p+2` supplies the unchanged right padding factor.  Once the square is
formed, the base has length `m-2>=2`; a square at an endpoint has padding
on its other side, and an interior square has padding on either side.
Therefore every displayed pair rewrite is a literal same-product
length-three replacement, not an illicit H2 move.  A square-label refresh
which is already `f f` can simply be omitted.

The insertion-coordinate table makes the two swap cases exhaustive.  A
projected factor `s=(a,b)` is lifted either as `s`, transporting the
coordinate, or as `h_b`, retaining it.  The displayed Hurwitz and inverse
Hurwitz identities move that projected factor left while moving the opening
null right.  Thus `Del_v` and the order of the projected base word are
preserved.

## 2. Preservation of `F_N`

Every step preserves length and ordered product, hence remains an identity
word of length `2N-2`.  It also preserves `Del_v=z`, and the two null
increments remain factors incident to `v`.

The support-connectivity sentence in Section 2.3 is valid with the following
explicit component argument.  Let `G` be the transposition-support graph
of any intermediate word.  Every prefix permutation preserves each
connected component of `G`.  Erasing `v` from its cycles cannot merge
two such components, so the support of `Del_v(w)` cannot connect vertices
belonging to distinct components of `G`.  Since `z` has connected
support on `X=[N]\{v}`, all of `X` lies in one component of `G`.
At least one (indeed two null) factor is incident to `v`, so `v` lies
in that component as well.  Hence `G` is connected.

A connected identity word on `N` labels at length `2N-2` is in the
minimal full-support macro `F_N`.  This proves preservation even though
the prefix join tree can and sometimes does change.  The proof therefore
does not silently assert a fixed-`T` restriction path.

## 3. Exact transition lower bound

For any specified H3 replacement, the literal lazy kernel assigns at least

```text
[1/(2|R_m|)] [1/(m-2)] [1/|fiber|].
```

There are `M=binom(N,2)` transpositions, so every ordered length-three
fiber has size at most `M^3`.  Consequently

```text
p_*=1/[2|R_m|(m-2)M^3]
```

is correct.  It includes laziness, block-size choice, all `m-2` windows,
and heat-bath normalization.  H4 and H5 remain nonnegative additional
flow; the proof does not renormalize after discarding them.

## 4. Cell size, hub uniqueness, and load recovery

The accepted M49 strand-deletion lemma gives exactly two ordered null
positions.  There are `binom(m,2)` choices, and for fixed positions at most
`(N-1)^2` lifts, so

```text
|C_(T,v,z)|<=Lambda_N=binom(m,2)(N-1)^2.
```

The hub `z f f` belongs to its cell and has join tree `T`: first `z`
builds `T-v`, the first `f` joins `v`, and the second does not join.
Hubs from distinct chosen cells are distinct because a word determines its
prefix join tree, the deterministic chosen leaf, its leaf edge, and then
its deleted base.

For an internal first-crossing edge and a candidate deleted label `v`,
both endpoints recover the same `z=Del_v`.  There are at most `N`
choices of `v` and `N-1` choices of its original neighbor `u`.
The data `(v,z,u)` determine `T=T_J(z)+(v,u)` and the cell.  It has at
most `Lambda_N` possible starts.  Thus the directed edge load is at most

```text
N(N-1)Lambda_N.
```

No additional factor `2m-3` belongs here.  Each starting state is charged
once, to the first directed edge leaving `A`; this is a boundary
cardinality argument, not a comparison flow charging every path edge.
Macro-exit edges leave `F_N`, while these canonical-path crossings remain
inside `F_N`, so the two reservoirs are disjoint.

## 5. Claim C normalization and constants

If a cell hub lies in `A`, one hub edge has capacity at least
`p_*/|Omega|`, which is at least
`(p_*/|Omega|)a_C/Lambda_N`.  If the hub is outside `A`, the load bound
gives at least
`(p_*/|Omega|)a_C/[N(N-1)Lambda_N]`.  Weakening the first denominator,
summing cells, and using `pi(A)=|A|/|Omega|` gives exactly

```text
Q(A,A^c)/pi(A)>=p_*/[N(N-1)Lambda_N].
```

Since `min(pi(A),pi(A^c))<=pi(A)`, the symmetric conductance statement
holds for either mass orientation.

Finally,

```text
2|R_m|<=6,  m-2<=2N,  M^3<=N^6,
N(N-1)<=N^2,  Lambda_N<=2N^4,
```

so the total denominator is at most `24N^13`.  The claimed coarse
constant is conservative and correct, including `N=3,m=4` where
`|R_m|=2`.

## 6. Claim A and scope

Cycle erasures commute, and removing stuttering identity increments before
the next erasure does not change the final compressed prefix path.  Hence
every original-leaf cell move preserves the all-original-leaves core.  A
path with `N>=5` has a remaining path on at least three vertices; two
different orders of doubled edge pairs give distinct nonempty core fibers,
and appending the two leaf-edge squares lifts both.  This proves the
infinite reducibility family.

The report correctly refuses to extend Claim C to a cut containing exterior
states: such a cut can absorb every explicit `z s s` hub target.  It also
does not claim a fixed-tree restriction gap.

## 7. Independent smallest checks

I independently evaluated (2.3)--(2.6) for every ordered triple of distinct
labels through `N=7`, and recomputed the exact denominator and
`24N^13` inequality for `3<=N<=7`; there was no failure.  I also reran
the smallest exhaustive path falsifier:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/strand_canonical_path_falsifier.py \
  --N 4 --shape all --output /tmp/m60-referee-strand-N4.json
```

It checked 914 state-leaf pairs over the star and path representatives,
with zero failures and maximum path length 5 (below `2m-3=9`).  This
finite rerun is only a falsifier; the acceptance rests on the algebraic and
counting arguments above.
