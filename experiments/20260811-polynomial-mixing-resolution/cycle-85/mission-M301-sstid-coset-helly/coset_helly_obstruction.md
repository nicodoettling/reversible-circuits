# M301: actual matching-fiber Helly obstruction and density reformulation

Date: 2026-08-14 UTC.

Status: **proved exact action-cover/density equivalence and exact finite
matching-subfamily obstruction; SSTID and the registered whole-matching MT2H
statement remain unresolved**.

## 1. Scope and conventions

For `d>=3`, put `m=2d-2` and

```text
Z_d={w in Transpositions(S_d)^m:
       product(w)=id, support(w) connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`.  The signed right-Hurwitz
generators act chronologically:

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a),
w^(x;y)=(w^x)^y.
```

Let `A_d` be the finite image of this braid action on `Z_d`.  Fix an adjacent
DPS edit index `i`, let `H=Stab_(S_d)(d)`, and let `M` be an actual perfect
matching in M135's orbit-incidence multigraph.  Each `Q in M` is an actual
`H`-orbit edge.  Choose `w_Q in Q` and use the exact finite endpoint fiber

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)}.                    (1.1)
```

The definition is independent of the representative because braid actions
commute with global conjugation and `tau_i` is `H`-equivariant.  M296/M299
identifies the word-level common intersection, after fixing one edge, with a
simultaneous transporter-coset intersection inside the literal doubled-star
stabilizer.  Projection preserves common nonemptiness, not shortest braid
length.

This note proves no route for every matching, representative-diameter bound,
voltage statement, congestion bound, gap, mixing theorem, or Terminal result.

## 2. Why coset form alone has no 2-Helly consequence

Even arbitrary group cosets are not 2-Helly.  In the additive group
`V=F_2^2`, with basis `e_1,e_2`, the three sets

```text
X=<e_1>={0,e_1},
Y=<e_2>={0,e_2},
Z=e_1+<e_1+e_2>={e_1,e_2}                           (2.1)
```

are cosets of subgroups.  Their pairwise intersections are respectively
`{0}`, `{e_1}`, and `{e_2}`, while `X intersect Y intersect Z` is empty.
Thus the statement “each `K_Q` is a coset of a varying stabilizer” cannot by
itself support any Helly inference.  Actual matching geometry would have to
add a new property.

The next section shows that the actual M135 edge universe already contains
the same obstruction at rank three.  That finite fact does not extend itself
to `d>=6`; it only rules out an unqualified formal coset-Helly shortcut.

## 3. One pre-registered exact finite diagnostic

The candidate fixed in `plan.md` before computation was:

> **MT2H.**  If every pair of fibers from one complete actual perfect
> matching intersects, then all fibers in that perfect matching intersect.

The SHA-gated script `mt2h_d3_diagnostic.py` reconstructs `Z_3`, the complete
signed-Hurwitz action image, every actual `H`-orbit incidence edge, every
perfect matching, and every relevant fiber intersection.  It imports only
M135's frozen DPS and permutation routines after checking

```text
M135 SHA256SUMS                 8d7ca3af...52a5358
M135 conflict_coloring_audit.py 79ed378a...6ad540.
```

The exact finite universe is

```text
|Z_3|=24,       |A_3|=216,
4 global S_3-orbits,       12 H-orbits,
|K_Q|=9 for every actual edge Q.                     (3.1)
```

For each `i=1,2,3`, there are exactly twelve perfect matchings.  No one of
the 36 indexed matching occurrences is pairwise compatible.  Hence the
antecedent of the registered complete-matching MT2H assertion never holds at
this guard:

```text
MT2H on complete perfect matchings at d=3:
  NOT REFUTED; VACUOUS ON THE ENUMERATED UNIVERSE.   (3.2)
```

It would be incorrect to promote the finite guard as support for MT2H at
higher rank.

### Proposition 3.1 (hereditary matching-subfamily 2-Helly; **REFUTED,
exact finite at `d=3`**)

There is an actual three-edge subfamily contained in an actual perfect
matching whose three action fibers intersect pairwise but have empty total
intersection.

#### Certificate

Use `i=1` and matching edge IDs `[0,1,2,9]` from the deterministic ordering
in `results.json`.  The witness subfamily is `[0,2,9]`.  Its left/right
global-orbit endpoints are

```text
Q_0: (0,1),       Q_2: (2,3),       Q_9: (3,2),     (3.3)
```

so both endpoints are distinct and these are literally a partial matching.
The chosen source and target words, in one-based transposition notation, are

```text
Q_0:  12 12 13 13   ->   12 23 12 13,
Q_2:  12 13 13 12   ->   12 23 13 23,
Q_9:  13 23 12 23   ->   23 12 12 23.               (3.4)
```

All six words are entries of the reconstructed `Z_3` endpoint table, and
the three arrows are the exact descended `tau_1` action.  With finite actions
sorted lexicographically by their permutations of the 24 states, the exact
intersections are

```text
K_0 intersect K_2 = {45},
K_0 intersect K_9 = {49},
K_2 intersect K_9 = {89},
K_0 intersect K_2 intersect K_9 = empty.             (3.5)
```

The distinct action IDs in (3.5) are deterministic certificate labels, not
group element names.  Complete closure under all six signed generators gives
the action image of order 216 before the intersections are evaluated.  This
proves the proposition.  QED.

### Consequence and exact stopping line

An independent set in the exact pairwise incompatibility graph need not be a
common-action class, even when it is a subfamily of one actual M135 perfect
matching.  Therefore

```text
color the pairwise graph + invoke 2-Helly
```

is **REFUTED as an unqualified shortcut**.  Proposition 3.1 does not refute
MT2H as registered for complete matchings, does not refute a bounded Helly
number depending polynomially on `d`, and does not imply any obstruction at
`d>=6`.

## 4. Exact higher-arity replacement: agreement hyperedges

For `a in A_d`, define the agreement hyperedge on a fixed matching `M` by

```text
E_a(M)={Q in M:a in K_Q}.                            (4.1)
```

Define the finite action-cover number

```text
kappa(M)=min{|R|:R subset A_d,
                   M=union_(a in R) E_a(M)}.         (4.2)
```

### Lemma 4.1 (common-class covers are action covers; **PROVED**)

The smallest number of subfamilies in a partition of `M`, each having a
nonempty total fiber intersection, is exactly `kappa(M)`.

#### Proof

Given such a partition, choose one common action from each cell.  The chosen
actions cover `M` by (4.1), so `kappa(M)` is no larger than the partition.
Conversely, given actions covering `M`, assign every edge to the first chosen
action whose agreement hyperedge contains it.  The assigned cells form a
partition, and each cell has that action in its total fiber intersection.
QED.

Thus higher-arity common realization is a set-cover problem for the actual
agreement hypergraph, not a graph-coloring problem.

## 5. Residual agreement density is polynomially equivalent

For nonempty `U subset M`, put

```text
rho(U)=max_(a in A_d) |E_a(M) intersect U|/|U|.       (5.1)
```

### Theorem 5.1 (cover-density equivalence; **PROVED**)

For any integer `q>=1`:

1. if `kappa(M)<=q`, then `rho(U)>=1/q` for every nonempty `U subset M`;
2. if `rho(U)>=1/q` for every nonempty `U subset M`, then

   ```text
   kappa(M)<=ceil(q(1+ln |M|)).                      (5.2)
   ```

#### Proof

For (1), restrict a fixed `q`-action cover to `U`.  Some one of its actions
covers at least `|U|/q` members by the pigeonhole principle.

For (2), start with `U_0=M`.  While the residual set is nonempty, choose an
action covering at least a `1/q` fraction and delete those covered edges.
After `t` steps,

```text
|U_t|<=|M|(1-1/q)^t<=|M| exp(-t/q).
```

Taking `t>q ln|M|` makes the right side smaller than one.  One final action
handles rounding, proving (5.2).  QED.

M112/M119's count and M135's free global action give

```text
|M|=|Z_d|/d!
   =d^(d-3)(2d-2)!/d!,                              (5.3)
ln|M|=O(d log d).
```

Consequently, a uniform inverse-polynomial lower bound on every residual
`rho(U)` is equivalent, up to the polynomial factor `O(d log d)`, to a
polynomial finite-action common-class cover.

### Lemma 5.2 (exact mean agreement; **PROVED under finite-action
transitivity on `Z_d`**)

If `A_d` is transitive on `Z_d`, then for every actual matching

```text
(1/|A_d|) sum_(a in A_d) |E_a(M)| = 1/d!.           (5.4)
```

More generally, the average of `|E_a(M) intersect U|` is `|U|/|Z_d|`.

#### Proof

Transitivity makes every endpoint fiber have size
`|K_Q|=|A_d|/|Z_d|`.  Double-counting incidences `(a,Q)` gives

```text
sum_a |E_a(M) intersect U|
 =sum_(Q in U)|K_Q|=|U||A_d|/|Z_d|.
```

For `U=M`, substitute `|M|=|Z_d|/d!`.  QED.

Equation (5.4) is not a negative theorem: rare actions can have very large
agreement.  It shows why sampling a generic finite action cannot prove the
needed density.  A polynomial cover requires explicit high-agreement actions
whose matching-specific correlations are invisible to the mean and, by
Proposition 3.1, are not determined by pairwise intersections.

## 6. First standalone unresolved lemma

The finite-action half of SSTID can now be isolated without a false Helly
step.

> **MATCHING RESIDUAL AGREEMENT DENSITY (MRAD).**  There is a universal
> constant `C` such that for every `d>=6`, every adjacent edit index `i`,
> every actual perfect matching `M` of `B_(d,i)`, and every nonempty
> `U subset M`, there is an action `a in A_d` satisfying
> ```text
> |{Q in U:a in K_Q}| >= |U|/d^C.                   (6.1)
> ```

MRAD is **UNRESOLVED**.  Theorem 5.1 and (5.3) show that it is polynomially
equivalent to the finite common-nonemptiness cover.  It is a genuinely
higher-arity statement on the actual selected edges.  Proposition 3.1 says
that exact pairwise compatibility alone cannot prove it by a 2-Helly rule.

Even MRAD would not finish SSTID.  One must additionally select the covering
actions with signed braid representatives of length `d^O(1)`, equivalently
use the short-lift version of (6.1).  M296/M299's two frame inequalities make
that word-length requirement equivalent in the original common schedule and
residual doubled-star formulations.  Finite nonemptiness must not be promoted
to polynomial literal length.

## 7. Boundary cases and nonimplications

- The exact obstruction is at `d=3,m=4`.  SSTID is stated for `d>=6`; no
  rank lift or asymptotic obstruction is claimed.
- At `d=3`, all complete matchings fail MT2H's premise, so this mission does
  not label MT2H false.
- The generic `F_2^2` example only denies a formal theorem about arbitrary
  cosets.  Proposition 3.1 is what places the obstruction in the actual M135
  edge universe.
- No finite-action diameter, short representative, every-color route,
  voltage correction, congestion, spectral gap, mixing-time bound, Terminal
  A, or Terminal B follows.
