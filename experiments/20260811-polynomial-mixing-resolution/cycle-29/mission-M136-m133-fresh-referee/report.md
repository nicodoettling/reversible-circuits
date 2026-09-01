# M136 final report: fresh referee of M133

Date: 2026-08-13 UTC.

## 1. Verdict

**ACCEPT** the frozen M133 package within its stated scope, with zero
objections.

- **PROVED, relative to the accepted M125/M129 coefficient formula:** the
  connected-unicycle diagonal has M133's subtraction-free decomposition by a
  unique even core and recursively planted opposite-colour trees.  The least
  core edge, orientation, length-two core, atom indexing, and all incidence
  weights are handled correctly.
- **REFUTED:** pairwise polarization of fixed-core profiles fails first at
  `d=4,c=3`; the exact `(core 2,core 4)` margin is `-17309376`.
- **EXACT FINITE:** the positive recurrence agrees with literal partition
  pairs for all 37 eligible integer cycle types through total size seven and
  reconstructs the frozen core profiles through `d=8`.  M133's targeted
  positive ordinary-log-concavity signs at `d=23,24,25,26` are accepted only
  as capped finite facts; three triples were independently recomputed and the
  fourth was consistency-audited as detailed below.
- **UNRESOLVED:** two-edge-core log-concavity, the full coefficient inequality,
  DEFECT NO-VALLEY, every downstream incidence/handle/fiber comparison gap,
  and the original lazy exact `{3,4,5}` same-product heat-bath gap.

Neither Terminal A nor Terminal B follows.

## 2. Target, convention, and dependency boundary

The audited target is the M113/M118 auxiliary incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
M[d,r]=sum_(R(kappa)=r)|C_kappa|,
H[d,c]=M[d,d-c].
```

It is not the original uniform identity-word law and not the lifted
`bar_pi` law.  M133 uses the project convention `(pq)(x)=p(q(x))`, with tuple
factors multiplied left-to-right.  No permutation operation is newly used in
the coefficient proof.

I inspected the frozen M113/M118 cell-formula reduction and the frozen
M125/M129 coefficient theorem and fresh audit.  The sole enumerative input
used by M133 is the already accepted formula

```text
H[d,c]
 = sum_(lambda partition d, length c)
     n(lambda) product_i (a_i^a_i/(a_i-1)!)^2
     sum_(L=1)^(c-1)
       (d+c-2L)!(d-c+2L)!
       [y^L z^(c-L)]C_lambda(y,z).
```

M133's complete checksum inventory passes.  Its assignment-supplied report,
proof, positive checker/result, core checker/result, manifest, and inventory
hashes all match exactly.

## 3. Independent bijection audit

Fix indexed atoms `E`, with positive sizes `a_e`, and block weight

```text
w(I)=(sum_(e in I)a_e)^(|I|-3).
```

An ordered pair `(pi_L,pi_R)` of atom partitions gives an edge-labelled
bipartite multigraph: coloured partition blocks are vertices and every atom
is one edge.  Its connected components are exactly the blocks of
`pi_L join pi_R`; hence join-indiscreteness is graph connectivity.  On the
required diagonal

```text
|pi_L|+|pi_R|=|E|,
```

the connected graph has `V=E`, so its cyclomatic number is one.  It therefore
has one graph-theoretic cycle.  Bipartiteness makes the core even, with two
parallel labelled edges as the legitimate length-two case.

Let `e_0` be the least core edge.  Its left endpoint has exactly one other
core edge, `e_1`; alternately following right and left endpoints determines

```text
(e_0,e_1,...,e_(2k-1))
```

uniquely.  Thus the least edge removes rotations and the fixed *left*
endpoint removes the orientation choice.  Reversing a core of length at least
four exchanges the coloured matchings and represents a different ordered
partition pair; for the two-edge core there is only one tail sequence.  A
fresh fixed-first inventory found respectively `1,6,120,5040` sequences and
the same number of distinct coloured cores for lengths `2,4,6,8`, with
maximum multiplicity one in every case.

After deleting the core edges, every remaining component contains exactly
one core vertex.  Zero would contradict connectivity; two would give a second
cycle.  Such a component is a tree.  Deleting its root vertex uniquely
partitions its internal edge set into branch edge sets, and each branch has a
unique edge incident to the root.  Recursing at the opposite-colour endpoint
is exactly M133's planted polynomial

```text
T_epsilon(B;S)
 = x_epsilon
   sum_(pi partition S)
   sum_(r_D in D for D in pi)
     w(B union {r_D})
     product_(D in pi)T_bar(epsilon)({r_D};D-{r_D}).
```

Conversely, one even core plus these planted trees is connected and
unicyclic.  Every incidence vertex is introduced once, its full incident edge
block receives exactly one factor `w`, and each atom correctly appears at
both coloured endpoints.  The two constructions are inverse and preserve
the `y,z` block counts and weights.  This proves M133's identity

```text
U_E(y,z)
 = sum_(connected ordered pairs, |pi_L|+|pi_R|=|E|)
     y^|pi_L| z^|pi_R|
     product_(B in pi_L union pi_R)w(B).
```

The core length is intrinsic, so every individual `U_(E,2k)`, not only their
sum, is invariant under reindexing.  Equal cycle lengths introduce no extra
factor: the atoms are actual indexed permutation cycles, while
`n(lambda)=d!/product_s(s^m_s m_s!)` accounts for permutation cycle type.

## 4. Positive coefficient decomposition and boundaries

Substitution into the accepted M125 formula gives exactly

```text
H[d,c]=sum_(2k<=c) H_(2k)[d,c]
```

with every summand a positive rational expression.  This genuinely removes
the subtractive connected-component extraction on the required diagonal.  It
does not imply that the sum is log-concave.

The boundaries are correct:

- `c=1` is impossible because both colours must have a nonempty partition;
- at `d=2,c=2`, the two labelled atoms form one parallel-edge core and the
  coefficient formula gives the one-state mass `1`;
- the two-edge core occurs once, without a factor two or a vertex
  automorphism divisor;
- all recursive boundary and internal edge sets are disjoint, so a selected
  child root cannot duplicate a core/boundary edge.

## 5. Clean-room exact checks

`independent_referee.py` imports no M133 or M125 Python module.  It separately
implements restricted-growth-string set partitions, incidence-graph leaf
pruning, literal core classification, the stated positive recurrence, and a
connected-component recurrence aggregated by equal atom size.  The last uses
a dynamic root convention (largest current multiplicity, ties toward the
smaller size), different from M125 and M129.

`independent_results.json` has zero failures:

- all 58 eligible integer cycle types through `d=8` match the independent
  connected-component recurrence coefficient-by-coefficient on the unicycle
  diagonal;
- all 37 eligible types through `d=7` also match literal ordered partition
  pairs, after examining 864,261 pairs;
- graph pruning verifies a unique even core and unique off-core attachment
  root for every accepted literal pair;
- the weighted fixed-core profiles reconstruct every frozen value through
  `d=8`;
- at `d=4`, the core-two and core-four profiles across `c=2,3,4` are

  ```text
  (80136,109440,44928),
  (0,0,216).
  ```

Consequently the pairwise polarization at center `c=3` is exactly

```text
2*109440*0 - 80136*216 - 0*44928
  = -17309376.
```

This is the first possible rank because a four-edge core first appears at
`c=4`.  It refutes only the termwise sufficient inequality; the total `d=4`
row remains ordinarily log-concave.

## 6. Capped frontier audit

The independent dynamic-root recurrence completed these exact comparisons
before the coordinator capped the finite-only scan:

| `d` | center defect | exact comparison | ratio |
|---:|---:|:---:|---:|
| 23 | 7 | match | `1.0080697027067378` |
| 24 | 8 | match | `1.0062524521873242` |
| 25 | 8 | match | `1.0034208061391020` |

Here `match` required equality of all three exact masses, cycle-type counts,
the exact integer margin, and the reduced ratio numerator and denominator.
The combined process was interrupted during `d=26,r=9` before its JSON write;
`frontier_partial.md` records the completed stdout and limitation.

For all four frozen cases, including `d=26`, `independent_results.json`
independently recounts the fixed-length integer partitions and recomputes the
stored exact margin and reduced ratio from the stored masses.  All checks
pass; the `d=26` ratio is `1.0023705599074406`.  This last check is explicitly
not an independent recomputation of the `d=26` masses.  The omission is not a
mathematical objection: the recurrence is proved and accepted upstream, the
frozen exact checker and payload are immutable, and these four signs are
claimed only as finite falsification data.

The shrinking ratios provide no asymptotic conclusion and prove neither
ordinary log-concavity nor DEFECT NO-VALLEY.

## 7. Numbered objections

1. **None.**  No material or minor mathematical, computational, provenance,
   or scope objection survives the fresh audit.

## 8. Scope guard and action

**Action:** accept M133's positive unique-cycle theorem, positive fixed-core
coefficient decomposition, and exact `d=4` polarization obstruction into the
coordinator ledger.  Retain the `d=23..26` signs only as exact finite facts.

Do not infer universal two-edge-core or total log-concavity, DEFECT NO-VALLEY,
an incidence/handle projection gap, or a gap for the original heat-bath
chain.  M133 correctly identifies TWO-EDGE-CORE LOG-CONCAVITY plus a
quantitative higher-core correction bound as a narrower open route, not as a
proved lemma.

## 9. Reproduction and provenance

From this directory:

```text
python3 -B independent_referee.py \
  --small-max-d 8 --direct-max-d 7 \
  --output independent_results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, exact deterministic arithmetic, `seed=null`.

Fresh pre-report hashes:

| artifact | SHA-256 |
|---|---|
| `independent_referee.py` | `b76fbfd9683953913f87b729f8dd165d37f4a20a85e549b2e961c0d8c73ab178` |
| `independent_results.json` | `26374d992d7c8a38e09307f9af039e119dc55c788e14f51d93d80c1c330f75ad` |

No predecessor, coordinator, manuscript, skill, or other worker file was
edited.  No package was installed, no stochastic claim was made, and no
continuation work is included.
