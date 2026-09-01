# M78 halfway checkpoint: elimination law exact; depths 0 and 1 refuted

Date: 2026-08-12.  Repository commit recorded by the exact output:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Convention, scope, and target

Permutations compose as `(pq)(x)=p(q(x))`, words evaluate left-to-right,
and the right Hurwitz generator is

```text
R_i(...,a,b,...)=(...,b,bab,...).
```

The global target remains uniform on `Omega(N,m)`, and the literal ambient
regime is `N>=5,m=2N-2`.  This checkpoint concerns only M75's canonical
simple-positive-braid row law in a two-component macro.  In this regime the
component genera sum to one, so exactly one nontrivial component has genus
one and the other is genus zero.  If the genus-one component has `d`
vertices, its length is `k=2d`.

No finite result below is a spectral-gap or Terminal claim.

## 2. Exact canonical elimination law

Label the original `k` factor positions.  M75's canonical bubble-sort lift
of a target label order is equivalently the following elimination process.
If the requested original label is currently at residual position `j` with
current transposition `b`, output `b`, delete that position, and replace each
current factor `a` strictly to its left by

```text
bab.
```

Factors to its right are unchanged.  This is exactly the result of bubbling
the requested label left using `R(a,b)=(b,bab)`.

After prior current outputs `b_1,...,b_q`, the current value of an unselected
original factor `t_j` is

```text
G_j^(-1) t_j G_j,
G_j = product, in selection order, of those prior current outputs b_s
      whose original labels j_s satisfy j_s>j.       (2.1)
```

Indeed a selected factor to the right of `j` conjugates the current value of
`j` once; a selected factor to its left does not.  Induction through the
elimination rule proves (2.1).

Define **success at depth `q`** to mean that the first `q` outputs are
preliminary, outputs `q+1,q+2` are equal, and deleting those last two leaves
the word consisting of the first `q` outputs followed by the current
residual tuple connected.  One successful ordered prefix of length `q+2`
has probability exactly

```text
1/(k)_(q+2),                                        (2.2)
```

under a uniform full target order.  Here `(k)_r=k(k-1)...(k-r+1)`.
Consequently any universal constant-depth existence theorem would imply the
needed inverse-polynomial row bound.

Success at a prefix is equivalent to the final positive-braid endpoint
containing that marked adjacent square.  Later eliminations act only to its
right, so the equal pair stays adjacent; those later Hurwitz moves preserve
connectedness of the word with the pair deleted.  Conversely every marked
endpoint pair arose at its emission prefix.  This permits exact prefix-hit
counting by an absorbing elimination recursion.

## 3. Exact finite results

The deterministic standard-library audit exhausts every connected genus-one
identity word for `d=3,4`:

| component | words | minimum success depth |
|---|---:|---|
| `d=3,k=6` | 240 | all 240 at depth 0 |
| `d=4,k=8` | 131040 | 130992 at depth 0; 48 first succeed at depth 1 |

Thus depth zero is already nonuniversal.

On `d=5,k=10`, the all-distinct word

```text
(01)(02)(03)(12)(14)(24)(04)(23)(13)(34)           (3.1)
```

is connected and evaluates to identity.  It has zero depth-zero prefixes
and exactly 14 successful ordered depth-one prefixes.  This refutes every
proof that starts from an original repeated edge, while still giving the
finite lower bound `14/(10)_3` from depth one.  An exact absorbing recursion
counts `1569216/10!` full orders with a marked prefix.

The stronger one-preliminary-elimination statement is false.  On labels
`0,...,7`, with bipartition `{0,1,2,3}|{4,5,6,7}`, the all-distinct word

```text
(35)(34)(15)(25)(16)(04)(37)(27)
(05)(36)(14)(17)(06)(24)(26)(07)                  (3.2)
```

uses every edge of `K_(4,4)` once, is connected, and evaluates to identity.
It has exact successful-prefix counts

```text
depth 0: 0,
depth 1: 0,
depth 2: 76.                                       (3.3)
```

The depth-one zero has a direct proof.  In an all-distinct word, after one
factor `b` is selected, equality among two remaining current factors can
only be a cross-boundary equality `bab=c`, where one original position was
left of `b` and one was right.  For distinct transpositions `a,b,c`, this
identity requires the three edges to form a triangle.  The support `K_(4,4)`
is triangle-free.

## 4. Facial-cycle conjecture refuted at connectivity

The factor-order rotation system of (3.2) has eight faces, each of length
four:

```text
[0,2,4,9], [0,1,5,8], [1,6,7,13], [2,3,7,11],
[3,8,12,14], [4,10,13,14], [5,10,11,15],
[6,9,12,15].                                      (4.1)
```

Across all `8*4!=192` facial orderings, 32 create equal last two current
factors, but **zero** leave connected support after deleting that pair.  For
example, facial order `(2,4,0,9)` has original edges

```text
(15),(16),(35),(36)
```

and current outputs

```text
(15),(16),(36),(36),                               (4.2)
```

but deletion isolates vertex 3.

A successful nonfacial support 4-cycle is `(1,2,0,10)`, with original edges

```text
(34),(15),(35),(14)
```

and current outputs

```text
(34),(15),(14),(14).                               (4.3)
```

After deleting the last pair, all eight vertices remain connected.  Thus
the algebraic cycle-to-collision mechanism is real, but average facial
length does not prove the required nonseparating deletion.  The proposed
short-face proof route is refuted literally at its connectivity step.

## 5. Status and next exact obligation

The canonical law itself remains unresolved: (3.2) has many depth-two hits
and therefore is not a zero row.  The current standalone alternatives are:

1. prove every connected genus-one identity factorization has a
   nonseparating elimination cycle of length at most an absolute constant;
2. construct an infinite high-edgewidth genus-one map/factorization family
   and upper-bound the **total** marked-prefix probability, not merely its
   earliest possible depth; or
3. derive an exact full-prefix recursion with enough structure to prove a
   polynomial worst-row bound directly.

The exact K4,4 full-prefix count is not yet computed: direct enumeration has
`16!` orders, and the naive memoized current-tuple recursion is too large.
A Monte Carlo estimate can guide the next theorem, but cannot certify a
positive lower bound.

## 6. Artifacts and reproduction

Owned artifacts:

```text
plan.md
checkpoint.md
exact_elimination_audit.py
exact-results.json
```

Exact command from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/exact_elimination_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/exact-results.json
```

Python 3.12.3; seed `null`; nonstandard dependencies `{}`.  The run is
deterministic and takes about five seconds on the recorded machine.
