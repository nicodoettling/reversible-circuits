# M304 Independent Proof Audit of M301

Date: 2026-08-14 UTC

## Verdict and scope

```text
ACCEPT M301 AS FROZEN AT ITS EXACT FINITE-ACTION SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

The audited object is the auxiliary minimal connected sector

```text
Z_d={w in T_d^(2d-2): product(w)=id, support(w) connected},
```

with `(pq)(x)=p(q(x))` and chronological signed right-Hurwitz action.  This
is not a theorem about the global bridge law or the lazy exact `{3,4,5}`
heat-bath chain.

## 1. Generic cosets do not have the proposed Helly property

In `F_2^2`, M301's three cosets are

```text
X={0,e_1},       Y={0,e_2},       Z={e_1,e_2}.
```

Their pair intersections are `{0}`, `{e_1}`, and `{e_2}`, while their triple
intersection is empty.  This correctly denies a formal 2-Helly inference for
arbitrary varying subgroup cosets.  M301 also correctly refrains from using
this generic example as an actual project-edge witness.

## 2. Complete clean-room `d=3` reconstruction

The sole independent checker reads and imports no project artifact.  It
directly enumerates all `3^4` length-four transposition words, filters product
identity and connected support, and obtains `|Z_3|=24`.  Its independent DPS
construction has the same 24-word image with exactly three rooted preimages
per word.  Swapping adjacent DPS labels gives the three descended `tau_i`
maps.

Closure under all six signed Hurwitz generators gives the finite action
image `|A_3|=216`.  Independent canonicalization under `S_3` and
`H=Stab(3)` gives four global orbits and twelve `H`-orbits.  For each
`i=1,2,3`, exhaustive incidence and matching enumeration gives

```text
12 actual H-orbit edges,
12 perfect matchings,
|K_Q|=9 for every edge,
0 pairwise-compatible complete perfect matchings.
```

Thus all 36 indexed complete-matching occurrences fail the premise of MT2H.
There is no complete `d=3` counterexample: MT2H is vacuously true on this
finite guard and remains unresolved in its registered all-rank form.

For `i=1`, the independently reconstructed matching `[0,1,2,9]` contains
the subfamily `[0,2,9]`.  Its bipartite endpoints are

```text
(0,1), (2,3), (3,2),
```

so the left endpoints and right endpoints are separately distinct.  The
three source/target words under `tau_1` agree exactly with M301's displayed
certificate.  Lexicographically sorting the 216 action permutations gives

```text
K_0 intersect K_2={45},
K_0 intersect K_9={49},
K_2 intersect K_9={89},
K_0 intersect K_2 intersect K_9=empty.
```

This is an exhaustive exact finite witness.  It refutes hereditary 2-Helly
for actual matching subfamilies and the unqualified pairwise-graph shortcut,
but not complete-matching MT2H and not any `d>=6` statement.

M301's own SHA-gated diagnostic was also replayed with output isolated in
`/tmp`; it reported no full counterexample and did report the subfamily
counterexample.

## 3. Action covers equal common-intersection partitions

For an action `a`, put `E_a(M)={Q:a in K_Q}`.  If a partition of `M` has
nonempty total intersection in every cell, selecting one common action per
cell gives an action cover.  Conversely, an action cover may overlap, but
assigning each edge to its first covering action makes disjoint cells, each
with that action in its total intersection.  Empty assigned cells can be
discarded.  Therefore the two minimum numbers are exactly equal; no
disjointness of the original agreement hyperedges was assumed.

## 4. Residual-density equivalence and cover factor

Suppose `kappa(M)<=q`.  On any nonempty `U subset M`, the restrictions of
the `q` covering hyperedges still cover `U`.  Their incidence counts sum to
at least `|U|`, even if they overlap, so one covers at least `|U|/q`.

Conversely, if every residual `U` has an action covering at least a `1/q`
fraction, greedy deletion gives

```text
|U_t|<=|M|(1-1/q)^t<=|M|exp(-t/q).
```

After more than `q ln|M|` steps the integer residual is empty; M301's looser
uniform rounding bound

```text
kappa(M)<=ceil(q(1+ln|M|))
```

is valid, including `q=1` and `|M|=1`.

The accepted count and free global relabeling action give

```text
|M|=|Z_d|/d!=d^(d-3)(2d-2)!/d!.
```

Stirling's bound, or simply bounding the factorial logarithms termwise,
gives `ln|M|=O(d log d)`.  Hence polynomial action-cover size implies
inverse-polynomial residual density with no loss, while inverse-polynomial
residual density implies polynomial cover size with the stated multiplicative
`O(d log d)` loss.

## 5. Exact mean agreement

This statement correctly retains its transitivity hypothesis.  If `A_d` is
transitive on `Z_d`, orbit-stabilizer gives

```text
|K_Q|=|A_d|/|Z_d|.
```

Double-counting `(a,Q)` for any `U subset M` yields

```text
(1/|A_d|)sum_a |E_a(M) intersect U|=|U|/|Z_d|.
```

For `U=M`, use `|M|=|Z_d|/d!` to obtain the exact mean `1/d!`.  This is an
average, not an upper bound on maximum agreement and not a cover
obstruction; M301 states that firewall explicitly.

## 6. MRAD and literal-length separation

M301's MRAD is correctly restricted to `d>=6`, every adjacent edit index,
every actual perfect matching, and every nonempty residual subfamily.  Its
lower bound `rho(U)>= d^-C`, combined with Section 4, is polynomially
equivalent to the finite-action common-nonemptiness cover.  The `d=3`
witness neither proves nor refutes MRAD.

MRAD controls only an action in the finite image.  Projection of the literal
braid group preserves common nonemptiness but not shortest signed-generator
length.  M296/M299's frame inequalities compare literal endpoint and
residual representatives only after a representative has been chosen; they
do not turn a finite action into a polynomial-length lift.  Therefore a
short-lift condition remains independent and SSTID does not follow from
MRAD alone.

## 7. Objections and stopping line

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
3. **Accepted:** exact hereditary `d=3` obstruction, complete-matching
   vacuity guard, action-cover/partition equality, cover-density equivalence,
   and the transitivity-conditional `1/d!` mean.
4. **Unresolved:** complete-matching MT2H, MRAD for `d>=6`, polynomial
   literal representatives, and SSTID.
5. **No inference:** every-color routing, rank lift, voltage, congestion,
   spectral gap, polynomial mixing, or either Terminal.

