# M81 final report: fresh acceptance of M78 and an exact duplicate-state reduction

Date: 2026-08-12.  Repository commit recorded by the exact artifacts:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Referee decision

**ACCEPT, with zero material objections.**

The accepted claim is deliberately narrow:

> For every `L>=2`, M78's explicit word `W_L` is a connected, simple,
> bipartite, genus-one identity transposition factorization, and its canonical
> positive-elimination process has no safe prefix at depths zero, one, or two.

Also accepted are the canonical elimination formula, the safe-prefix/marked-
endpoint equivalence, and M78's exact finite counts.  The verdict does **not**
accept a total row-probability bound, a canonical simple-braid row lemma, a
stationary bottleneck, a heat-bath gap estimate, or Terminal B.  Those claims
remain unresolved exactly as M78 states.

There are no numbered mathematical objections:

```text
Material objections: none.
```

One nonmaterial provenance note is retained: M78 supplied no separate freeze
manifest.  This is not an acceptance blocker because its complete eight-file
payload was immutable, the requested report digest matched, every file was
independently hashed before audit, and every decisive computation was
separately reimplemented.  The M78 digests are:

| artifact | SHA-256 |
|---|---|
| `report.md` | `c6b0e36ef09608e3fe962e0d85ad572db02b756726a8128548738473855576e1` |
| `plan.md` | `5762b712a6a56c93634b0545e3d3ae4e09a6f87e0570c9b4c50f815b796b85ab` |
| `checkpoint.md` | `25331d5b511c5a4744aa4239e9c3708d6fdfedee6d13842270f88dbf98476c97` |
| `exact_elimination_audit.py` | `18860de073bafca95316b0f82e0130a3ae70d289420068fde89702944853980a` |
| `exact-results.json` | `d854a949f569bada68f926747aaf2971e3f7db44d85ec12411d4ecbcbdfdc007` |
| `voltage_lift_audit.py` | `9de5e1d7b44b1cd9d4a6dffb5a38a8624d23feb96a142df1dca1b642bff2e1c4` |
| `voltage-results.json` | `e69170a8a22eb50626000ca1cae9dc1d5d6c12d5e2c1890b3586abccd97c148e` |
| `monte-carlo-prefix-results.json` | `36e85925f9e5c5ef51db0c8c3aae71946024889846825aca69e53c04c05d224c` |

## 2. Convention, target, and scope

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are evaluated
left-to-right; and the right Hurwitz generator is

```text
R(a,b)=(b,bab).
```

The global target remains uniform on `Omega(N,m)`, under the literal lazy
exact same-product `{3,4,5}` heat-bath kernel.  This mission concerns only the
canonical positive-braid row law inside M75's two-component minimal-macro
reduction.  Adding one isolated ambient label puts `W_L` at

```text
N=8L^2+1,  m=16L^2=2N-2.
```

An obstruction for this one state-independent braid law would not be a
spectral obstruction for the heat-bath chain.

## 3. Independent audit of the elimination law

Suppose the requested current factor `b` lies after current factors
`a_1,...,a_j`.  Bubbling it left gives

```text
(a_1,...,a_j,b,...) -> (b,ba_1b,...,ba_jb,...).     (3.1)
```

Thus elimination outputs `b`, deletes its residual position, conjugates every
residual factor to its left by `b`, and does nothing to its right.  Induction
gives, for an unselected original label `j`,

```text
current(t_j)=G_j^(-1)t_jG_j,
G_j=product in selection order of earlier outputs whose labels exceed j.
                                                               (3.2)
```

This independently verifies M78's convention and orientation.

If outputs `q+1,q+2` are equal, later eliminations occur strictly in the
residual suffix.  The pair remains adjacent, and the later Hurwitz moves
preserve the weighted support components after that pair is deleted.  Hence a
connected deletion at the emission prefix remains connected at the endpoint.
Conversely, invert the later suffix-only Hurwitz moves from any marked
endpoint; its adjacent equal pair was emitted consecutively and its deletion
was already connected.  This proves the safe-prefix/marked-endpoint
equivalence.

A specified ordered prefix of length `r` occurs with probability exactly
`1/(k)_r` under a uniform order of the `k` original labels.  Ambient commuting
interleavings do not change this relative-order law.

## 4. Fresh exact finite reproduction

The independent script imports no M78 code.  It reproduced the following
deterministic facts.

| case | independent result | M78 result | decision |
|---|---:|---:|---|
| all connected `d=3,k=6` identity words | `240`, all depth 0 | same | match |
| all connected `d=4,k=8` identity words | `131040`; `130992/48` at depths `0/1` | same | match |
| M78 `d=5,k=10` word | depth counts `[0,14]` | same | match |
| exact total hit count for that word | `1569216/10!=227/525` | same | match |
| M78 `K_(4,4)` word | depth counts `[0,0,76]` | same | match |
| chronological faces | eight, all length four | same | match |
| facial collision/safe orders | `32/0` | same | match |

The `K_(4,4)` word evaluates to identity, is connected, contains each of the
16 bipartite edges exactly once, and its eight facial collision patterns each
isolate one different base vertex.  The advertised nonfacial safe prefix was
also reproduced by the general depth count.

## 5. The infinite voltage family

### 5.1 Identity, support, connectedness, and genus

At each base factor, the lift inserts a full matching between two fibers.  A
lifted token therefore follows its base token trajectory, adding the signed
edge voltage each time.  The fresh computation gives the eight one-based
signed trajectory lists

```text
0: +6,-11,+12,-16       4: -2,+7,-8,+14
1: +3,-4,+8,-12         5: -1,+2,-6,+9
2: +4,-9,+13,-15        6: -5,+11,-14,+15
3: +1,-3,+5,-10         7: -7,+10,-13,+16.
```

Every row returns to its starting base vertex and has signed voltage `(0,0)`.
Thus every lifted token returns to its original fiber coordinate, proving
`W_L=id` for every modulus `L`.

Different base factors have different base endpoint pairs, and a lifted base
edge is a matching, so the support is simple.  It is bipartite and 4-regular.
The base graph is connected.  Its displayed closed walks have voltages
`(-1,0)` and `(0,1)`, which generate `Z_L^2`; the standard voltage-cover
lifting argument therefore connects every fiber over a fixed base vertex and
then every lifted vertex.  Hence the support is connected.

Finally

```text
d_L=8L^2,  k_L=16L^2=2d_L.
```

For a connected identity transposition factorization,
`k=2(d-1)+2g`; therefore `g=1`.  No literature theorem is used in these
checks.

### 5.2 Depths zero and one

Depth zero is impossible because the original support is simple.  After one
preliminary selection `b`, factors on one side are conjugated by `b` and
those on the other are unchanged.  Equal values on the same side would be an
original repeat.  A cross-side equality has form `bab=c`.  For distinct
transpositions this either reduces to a repeat when `a,b` are disjoint, or
the three edges form a triangle when they intersect.  The lifted support is
bipartite, hence triangle-free.  This proves no depth-one hit.

### 5.3 Four-factor classification

Elimination on any selected label set depends only on the corresponding
chronologically extracted subword.  Thus four labels producing outputs
`x,y,p,p` are Hurwitz-related, as a four-factor tuple, to their four original
transpositions.  Hurwitz moves preserve labeled weighted support components.

Assume the original support is simple and triangle-free.  The component that
contains `p,p` cannot have weight two: two distinct original edges cannot have
the same two-vertex support component.  It cannot have weight three: the
endpoint component `p,p,x` spans at most three vertices, whereas three
distinct connected triangle-free original edges either span at least four
vertices or would form a triangle.  Therefore all four factors lie in one
component.  Its endpoint has at most three distinct edges and hence spans at
most four vertices.  A connected simple triangle-free graph with four edges
on at most four vertices must have exactly four vertices and be a four-cycle.

Consequently every depth-two collision is supported on an original support
four-cycle.  This is a proof, not an inference from the finite `K_7` check.

### 5.4 Exactly eight base cycles can lift closed

The fresh enumeration of all 36 base `K_(4,4)` four-cycles gives the exact
integer-voltage distribution

```text
(-1,-1):1, (-1,0):2, (0,-1):2, (0,0):8,
(0,1):6,  (1,0):6,  (1,1):11.                    (5.1)
```

The eight zero-voltage edge-index sets are exactly

```text
[0,1,5,8],   [0,2,4,9],    [1,6,7,13], [2,3,7,11],
[3,8,12,14], [4,10,13,14], [5,10,11,15], [6,9,12,15].
                                                               (5.2)
```

They are exactly the eight faces of the chronological base rotation system.
Every nonzero vector in (5.1) has a coordinate equal to `+1` or `-1`, so it
cannot vanish modulo any `L>=2`.

A simple four-cycle in a graph cover projects to a reduced closed walk of
length four.  Since the simple bipartite base has girth four, this projection
is a base four-cycle.  It closes in the lift exactly when the base voltage
vanishes modulo `L`.  Thus every lifted support four-cycle is one of the
`L^2` translates of a cycle in (5.2), and there are exactly `8L^2` of them.

### 5.5 Why all four collision orders disconnect, uniformly in `L`

This was the most delicate referee obligation.  Relabel one chronological
face as

```text
AD, AB, BC, CD.                                    (5.3)
```

Among its `4!` elimination orders, exactly four make the final two outputs
equal:

```text
(AB,BC,AD,CD), (AB,BC,CD,AD),
(BC,AB,AD,CD), (BC,AB,CD,AD).                      (5.4)
```

The first two outputs are respectively `AB,BC` or `BC,AC`, and the deleted
pair is always `CD,CD`.  More importantly, direct symbolic conjugation shows
that all four orders induce the same endpoint maps on unselected original
factors in the five chronological intervals cut out by (5.3):

```text
I_0: CABD,  I_1: DABC,  I_2: ADBC,
I_3: ABDC,  I_4: ABCD.                             (5.5)
```

Reading each string as the images of `A,B,C,D`, an unselected transformed
edge can meet endpoint `D` only if its original edge meets, respectively,

```text
D in I_0, A in I_1, B in I_2, C in I_3, D in I_4. (5.6)
```

But a face in the chronological rotation system says exactly that there is
no such incident dart: `CD` and `AD` are cyclically consecutive at `D`, and
`AD/AB`, `AB/BC`, `BC/CD` are consecutive at `A,B,C`.  The preliminary
outputs in (5.4) also avoid `D`, while `CD,CD` is deleted.  Hence `D` is
isolated after deletion.

The lifted chronological rotations inherit the base rotations because each
base-factor matching occupies one consecutive block and contributes exactly
one incident edge at each lifted vertex.  Therefore (5.3)--(5.6) apply to
every translate of every zero-voltage face, independent of fiber coordinate
and modulus.  Every depth-two collision disconnects for every `L>=2`.

As redundant exact checks, the independent implementation found:

| `L` | lifted four-cycles | collision orders | safe | isolated vertices per collision |
|---:|---:|---:|---:|---:|
| 2 | 32 | 128 | 0 | 1 |
| 3 | 72 | 288 | 0 | 1 |
| 4 | 128 | 512 | 0 | 1 |

M78's code was separately rerun through `L=8` and agreed with the formulas
`8L^2`, `32L^2`, and zero.

## 6. Continuation: exact safe-duplicate reduction

The audit yields a sharper exact formulation of the total-prefix problem.
Consider any preliminary elimination state with emitted tuple `O` and current
residual tuple `R`.  Select positions `i<j` next.

If `R_i=R_j=p`, either selection order emits `p,p`.  Conversely, if the next
two outputs agree, undoing the one conjugation shows their two values were
already equal in `R`.  Moreover, after deleting the equal outputs, both
selection orders give the same word

```text
O + R[:i] + (p R[i+1] p,...,p R[j-1] p) + R[j+1:]. (6.1)
```

Call `{i,j}` a **safe duplicate pair** when (6.1) has connected support.  If
`|R|=s` and there are `a` safe unordered duplicate pairs at this state, then
the conditional probability that the next two uniformly selected labels
produce a safe hit is exactly

```text
2a/[s(s-1)].                                       (6.2)
```

Thus `eta_L` is a killed-random-elimination occupation problem for states
having safe duplicate pairs.  This is more precise than a search over support
cycles and avoids waiting for a sampled order accidentally to choose an
available duplicate pair.

The next standalone alternatives are now:

> **SAFE-DUPLICATE REACHABILITY FOR `W_L`.**  Either prove that every reachable
> preliminary state has `a=0`, which gives the exact zero row `eta_L=0`, or
> prove a polynomial lower bound on the probability-weighted occupation and
> hazard (6.2) of states with `a>0`.

A finite `L=2` decision can be encoded exactly as reachability under the
elimination rule, with state `(O-support,R)` and acceptance predicate (6.1).
Any SAT/DP implementation must certify completeness under a stated symmetry
quotient; a stochastic absence of hits is not such a certificate.

## 7. Continuation diagnostics and falsifications

The recorded fixed-seed full-order diagnostic inspects every actual
consecutive collision and exact deletion connectivity.  It found:

| `L` | trials | orders with collision | collision prefixes | safe orders |
|---:|---:|---:|---:|---:|
| 1 | 20000 | 1879 | 1956 | 1245 |
| 2 | 50000 | 1663 | 1684 | 0 |
| 3 | 10000 | 348 | 351 | 0 |

At `L=2`, the unsafe residual component shapes were `(31,1)` 1646 times and
`(30,2)` 38 times.  At `L=3`, they were `(71,1)` 343 times and `(70,2)` eight
times.  Therefore the attractive stronger claim “every collision isolates
exactly one vertex” is **refuted**.

The selected original-edge subgraph was also audited for cycle rank and
nonzero torus homology.  Many unsafe long-prefix collisions already had
nonzero homology.  For example, one exact replayable `W_2` prefix of length
39 had labels

```text
22,38,58,18,40,13,61,28,11,46,49,26,4,45,34,19,35,33,15,52,
0,39,31,48,37,44,9,27,56,7,20,55,23,14,47,36,62,3,32,
```

then emitted the equal edge `(8,20)`, while its selected-edge subgraph had
cycle rank eight and homology witnesses `(0,1),(1,1)`; deletion still left
components `(31,1)`.  Hence “nonzero selected-prefix homology implies safe”
is **refuted**.  A second exact replayable prefix of length 22,

```text
27,43,54,56,0,13,25,11,38,40,17,35,49,61,39,24,30,12,8,46,2,58,
```

emits `(10,26)` twice and leaves components `(30,2)`, refuting the singleton-
only picture.

All zero-hit statements in the table remain **empirical**.  They neither prove
`eta_2=0` nor imply asymptotic decay.

For calibration, exhaustive literal simple cycles of lengths `3` through `9`
have exactly `2(r-2)!` full elimination orders whose last outputs agree, a
conditional rate `2/[r(r-1)]`.  This exact finite pattern reinforces the
warning: obtaining a collision on a named cycle can be only polynomially
rare; the hard issue is reaching a collision whose deletion remains connected.
No general cycle formula is promoted without a separate proof.

## 8. Claim ledger and verdict

| claim | status | evidence | action |
|---|---|---|---|
| M78 payload identity | verified | all SHA-256 digests match | freeze |
| canonical braid equals elimination | proved | (3.1)--(3.2) | accept |
| safe prefix iff marked endpoint | proved | suffix Hurwitz invariance | accept |
| M78 finite counts | exact | independent full reimplementation | accept |
| `W_L` identity/connected/simple/bipartite/genus one | proved | trajectory and voltage-cover arguments | accept |
| all depth `<=2` prefixes unsafe for every `L>=2` | proved | Sections 5.2--5.5 | accept |
| total row probability `eta_L` is zero/small | unresolved | zero-hit Monte Carlo is insufficient | continue via (6.1)--(6.2) |
| canonical row lemma | unresolved | depends on total incidence | do not promote |
| heat-bath Terminal B | unresolved | canonical-law result alone cannot imply it | do not promote |

Final referee verdict:

```text
ACCEPT M78 WITH ZERO MATERIAL OBJECTIONS.
OPEN NEXT STEP: SAFE-DUPLICATE REACHABILITY / OCCUPATION FOR W_L.
NO TERMINAL CLAIM.
```

## 9. Artifacts and reproduction

Owned artifacts are:

```text
plan.md
checkpoint.md
independent_audit.py
independent-results.json
total_prefix_probe.py
total-prefix-results.json
m78-exact-rerun.json
m78-voltage-rerun.json
m78-voltage-extra-L4-L8.json
report.md
```

Decisive commands from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M81-m78-referee-voltage/independent_audit.py \
  --m78-dir experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M81-m78-referee-voltage/independent-results.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M81-m78-referee-voltage/total_prefix_probe.py \
  --case 1 20000 --case 2 50000 --case 3 10000 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M81-m78-referee-voltage/total-prefix-results.json
```

Python `3.12.3`; exact seed `null`; Monte Carlo seed `810081` with deterministic
case offsets; nonstandard dependencies `{}`.  The scripts use only the Python
standard library.
