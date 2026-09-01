# M112 halfway checkpoint: marked deletion is viable but not yet a gap proof

Date: 2026-08-12

## 1. Exact target and current status

The target is uniform on

```text
Z_d={w in T_d^(2d-2):eval(w)=id, support(w) connected},
P_(0,d)=I/2+[1/(4(2d-3))]sum_i(R_i+R_i^(-1)).
```

The desired bound `gap(P_(0,d))>=d^(-O(1))` is **UNRESOLVED**.  No claim
below implies the full `{3,4,5}` heat-bath gap or either Terminal criterion.

## 2. Exact bounded facts from the independent falsifier

For a prefix-join-tree leaf `v`, the accepted M49 strand deletion gives
`Del_v(w)=z in Z_(d-1)`.  I independently enumerated `d=2,3,4` and formed
the fixed marked fibers

```text
F_(v,z)={w in Z_d:v is a join-tree leaf and Del_v(w)=z}.
```

The exact results are:

| `d` | `|Z_d|` | marked incidences | fibers | fiber sizes | components/fiber |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 2 | 2 | 1 | 1 |
| 3 | 24 | 48 | 3 | 16 | 1 |
| 4 | 2880 | 6504 | 96 | 67 or 68 | 1 |

Thus fixed `(v,z)` fibers are connected in every tested case.  This is an
**EXACT FINITE** fact, not a universal gap theorem.  The raw `d=4` fiber
histogram is `24` fibers of size `67` and `72` of size `68`.  The smaller
fibers occur exactly when the three-label base word is a concatenation of
two distinct edge squares; this correlation is being incorporated into an
exact transfer recurrence rather than extrapolated.

For every physical signed adjacent-Hurwitz proposal which retains `v` as a
join-tree leaf, deletion produced either the same base word or one literal
signed adjacent-Hurwitz neighbor.  There were zero bad deletion images.  At
`d=4`, the oriented marked proposals split into

```text
identity deletion: 38,352
one base move:      19,056
mark lost:           7,632.
```

The stronger statewise lifting statement is **REFUTED at d=4**: among
`29,328` requested nontrivial oriented base moves over all lifts, `10,992`
have no one-step physical lift from that particular state.  This refutes only
statewise domination.  It leaves aggregate projected-flow domination and
bounded-length randomized simulation open.

The prefix join/cut word is a Dyck excursion and one Hurwitz move performs at
most one adjacent `JC <-> CJ` flip, but the Dyck path is already known from
accepted M13 to fail exact lumpability at `d=3`.  I therefore do not promote
a Markov projection onto Dyck paths.  A restriction/projection treatment
would have to retain conditional factorization data.

## 3. Exact insertion-coordinate recurrence being proved and reproduced

Let the base have `q=d-1` labels and length `L=2q-2`.  Choose the two null
positions of the deleted strand, equivalently an interval of base-factor
indices `0<=i<=j<=L`.  During that interval track the predecessor coordinate
of `v` in its permutation cycle.

For a base factor `s=(x,y)`:

- if `s` is a prefix support join, the lift is forced and the coordinate is
  transposed by `(x,y)`;
- if `s` is a prefix cycle cut, coordinates outside `{x,y}` are fixed, while
  either endpoint has two lifts and can emerge at either endpoint.  The
  transfer matrix is the identity with its `{x,y}` principal block replaced
  by the `2 x 2` all-ones matrix.

Starting with the all-ones vector and summing its final mass, then summing
over all intervals, counts `|F_(v,z)|`.  The matrix recurrence is a direct
restatement of the M49 insertion table, but its universal bijectivity and
bounded-distortion consequence are not yet frozen.  An independent script
is in progress to reproduce the direct `d=4` sizes and the coordinator's
`d=5`-fiber prediction `170..188` without enumerating `Z_5`.

## 4. Stationary-law issue and the next comparison

The spectrum-preserving everywhere-defined leaf lift must use

```text
Y_d={(w,v):v a join-tree leaf},
tilde_pi(w,v)=Unif(Z_d)(w)/number_of_leaves(T_J(w)).
```

Uniform measure on marked incidences is instead leaf-biased.  Their density
ratio can be as large as order `d`; silently using the raw marked law would
accumulate a potentially factorial distortion under recursion.  Even under
the raw law, standard restriction--projection gives a product of a fiber gap
and a projection gap.  Repeating a fresh polynomial fiber loss at every
label would be superpolynomial.  A successful proof therefore needs both:

1. a near-unit (or telescoping) comparison of the deletion projection with
   `P_(0,d-1)`, using the exact lift-count recurrence and aggregate flows;
2. an additive variance/Dirichlet decomposition, or a fiber action rate and
   gap whose recursion does not multiply a fresh `d^C` at every level.

The next exact tests aggregate physical flow by `(v,z)->(v,z')`, measure its
minimum ratio to the stationary base edge flow, and compute bounded distance
from an arbitrary lift to some lift of a requested base move.  Any paths will
be randomized over insertion histories; no canonical hub is being used.

## 5. Scope of `Gamma_0(d)`

Controlling `Z_s` alone is **not yet sufficient** for M104's entire
`Gamma_0(d)`.  Its other coordinates are minimal transitive factorizations

```text
F(C,q,k),   k=|C|+cycles(q)-2,
```

of arbitrary products `q`, not necessarily identity.  The identity case
`q=id` is exactly `Z_|C|`.  No literal label-preserving bijection or
gap-preserving reduction from every arbitrary-product coordinate to an
identity sector has been proved here.  Those coordinates remain an
additional obligation unless a quantitative capping/doubling construction
is supplied.

## 6. Current verdict

**KEEP / INCONCLUSIVE.**  Marked leaf deletion survives the first decisive
fiber-connectivity and equivariance tests and has unexpectedly mild raw
fiber-size distortion.  The naive statewise one-step lift is exactly false,
and neither aggregate flow nor a nonmultiplicative recursive Poincare bound is
yet proved.
