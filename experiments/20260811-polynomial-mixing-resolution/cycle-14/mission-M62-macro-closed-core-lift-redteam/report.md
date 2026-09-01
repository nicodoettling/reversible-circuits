# M62 final report: macro-closed core lifts are already polynomial

## 1. Exact claim, quantifiers, and convention

Use `(pq)(x)=p(q(x))`, `m=2N-2`, and the exact lazy chain

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

with global uniform stationary law `pi` on `Omega(N,m)`.  Let `F_N` be the
minimal connected full-support macro, let `A` be any nonempty proper subset
of `F_N`, and define

```text
S =F_N^c union A,
S'=F_N^c union (F_N minus A).                        (1.1)
```

This includes every single component or balanced union of the path-tree
all-original-leaves core invariant assigned in M62.

**Theorem (proved).** For every `N>=3` and every such `A`, both literal cuts
in (1.1) satisfy

```text
Phi_pm^K(S), Phi_pm^K(S')
 >= c_N
 :=1/[2|R_m|N(N-1)Lambda_N(m-2)M^3]
 >=1/(24N^13),                                      (1.2)

M=binom(N,2),
Lambda_N=binom(2N-2,2)(N-1)^2.
```

This is an append-only correction to the frozen M60 report, whose proposed
next gap incorrectly listed the macro-closed core lift.  M60 itself is not
mutated.  The true remaining family must split both `F_N` and `F_N^c`.

## 2. Full proof

### 2.1 Inherited arbitrary-minimal-side theorem

M60 proves, with the exact kernel above, that every nonempty `B subseteq F_N`
satisfies

```text
Q_K(B,B^c)/pi(B)>=c_N.                               (2.1)
```

Its proof partitions each join-tree fiber into strand-deletion cells of size
at most `Lambda_N`, gives every cell an explicit local-H3 path to an adjacent
leaf-square hub, and charges each starting state only to its first cut
crossing.  A directed crossing is charged at most `N(N-1)Lambda_N` times and
every specified H3 outcome has probability at least
`1/[2|R_m|(m-2)M^3]`.  Thus (2.1) includes laziness, the exact block-size and
window probabilities, and the full conditional-fiber denominator.  H4 and
H5 remain nonnegative additional flow.

Since

```text
min{pi(B),pi(B^c)}<=pi(B),
```

(2.1) already implies the two-sided bound

```text
Phi_pm^K(B)>=c_N                                    (2.2)
```

whether `B` is the smaller or larger side.

### 2.2 Exact complement identities

The two assigned cuts have the literal complements

```text
S^c    =F_N minus A,
(S')^c =A.                                           (2.3)
```

Both right sides are nonempty subsets of `F_N`.  Stationary flow and the
two-sided denominator are complement invariant:

```text
Q_K(C,C^c)=Q_K(C^c,C),
min{pi(C),pi(C^c)}=min{pi(C^c),pi(C)}.               (2.4)
```

The first equality follows from reversibility (or from the equality of total
stationary flow across a cut); the second is tautological.  Apply (2.2) to
`F_N minus A` and to `A`, then use (2.3)--(2.4).  This proves (1.2).

The point is subtle but exact: macro exits from `A` are indeed absorbed by
`S`, but its complementary minimal-macro side `F_N minus A` has its own M60
boundary certificate.  Similarly, `S'` is the complement of `A` itself.

### 2.3 Exact stationary masses

For arbitrary `A`, with `a=|A|`, `W=|Omega(N,m)|`, and `F=|F_N|`, the four
masses are exactly

```text
pi(S)     =(W-F+a)/W,       pi(S^c)     =(F-a)/W,
pi(S')    =(W-a)/W,         pi((S')^c)  =a/W.        (2.5)
```

No orientation is assumed: equations (2.2)--(2.4) handle whichever entry of
each pair is smaller.

### 2.4 N=5 balanced-core calibration

For the N=5 path fixed-tree fiber, the exact core-component sizes are

```text
1068,1068,997,997,997,997,842,842.
```

Choose one 1068 component, two 997 components, and one 842 component.  Then

```text
|A|=1068+997+997+842=3904=7808/2.
```

The exact global counts are

```text
|Omega(5,8)|=1,770,940,
|F_5|=1,008,000,
|F_5^c|=762,940.
```

Therefore (2.5) gives the side sizes

```text
S:   766,844 versus 1,004,096,
S':  1,767,036 versus 3,904.                         (2.6)
```

At these parameters, `|R_m|=3`, `M=10`, and `Lambda_5=448`, so the exact
universal lower bound is

```text
c_5=1/[6*20*448*6*1000]=1/322,560,000.              (2.7)
```

The finite calculation checks the arithmetic and orientation only; the
universal proof is (2.1)--(2.4).

## 3. Probability, runtime, path length, and congestion accounting

- Every inherited canonical H3 step has probability at least
  `1/[2|R_m|(m-2)M^3]`.
- The inherited first-boundary charge is at most
  `N(N-1)Lambda_N`; it is a cut injection, so no path-length factor appears.
  The underlying constructive path still has length at most `2m-3`.
- Their product is exactly `c_N` in (1.2).  With `|R_m|<=3`,
  `Lambda_N<=2N^4`, `m-2<=2N`, and `M^3<=N^6`, it is at least
  `1/(24N^13)`.
- M62 introduces no new path routing or congestion.  Complementation changes
  neither stationary boundary flow nor the two-sided denominator.
- The N=5 mass check is deterministic constant-time integer arithmetic with
  no random seed and no nonstandard dependency.

## 4. Dependencies with status

1. **PROVED HERE:** complement identities (2.3), exact mass formulas (2.5),
   and the deduction of (1.2) from M60.
2. **PROVED / INHERITED M60, FRESH REVIEW REQUESTED:** arbitrary-minimal-side
   escape (2.1), including its local H3 identities, full-support path,
   probability, and first-boundary multiplicity accounting.
3. **PROVED / INHERITED:** uniform heat-bath reversibility/stationarity.
   Reversibility supplies (2.4); stationarity alone also balances total cut
   flow.
4. **EXACT FINITE FACT:** the N=5 core-component sizes and counts in (2.6).
5. **UNRESOLVED:** cuts that contain a proper nonempty portion of both `F_N`
   and `F_N^c`.

## 5. First unproved standalone proposition

**PARTIAL-EXTERIOR CORE-SHELL LEAKAGE.** For a path-tree core union
`A_N subset F_N`, let `E_N subset F_N^c` contain the one-step H3 macro targets
`z s s` of its canonical leaf-square hubs, but not all of `F_N^c`.  Prove a
universal inverse-polynomial lower bound on the two-sided conductance of

```text
C_N=A_N union E_N,                                  (5.1)
```

including the stationary mass of `E_N` and every H3/H4/H5 boundary outcome,
or construct an explicit sequence for which (5.1) has superpolynomially small
conductance.  Both `C_N intersect F_N` and `C_N intersect F_N^c`, and both
corresponding complements, must be nonempty.  The cases `E_N=empty` and
`E_N=F_N^c` are now sealed by M60 and M62 respectively.

## 6. Strongest self-attack / failure mode

M62 is a logical closure, not an independent new flow construction.  If the
fresh audit finds a defect in M60's strand canonicalization or
first-boundary multiplicity, (1.2) reopens with it.  Subject to M60, however,
there is no mass-orientation loophole: two-sided conductance is exactly
complement invariant.

The theorem says nothing about a partial exterior set `E_N`.  Such a set can
absorb the particular hub exits from `A_N` without putting the entire
minimal-macro complement on the opposite side, so neither direct application
of M60 nor complementation reduces it to a subset of `F_N`.  This is the true
next counterexample lane.

## 7. Calibration suite

- Odd `m`: `Omega` is empty; the theorem concerns `m=2N-2`.
- `m=0` and `N=2` even are singleton calibrations; `m=2,N>=3` is excluded.
- `N=3,m=4`: `Omega` has 27 words and pure Hurwitz has 4 components.
  Here `|R_m|=2`, and H4 is whole-word.  M60's exact `|R_m|` formula, hence
  M62, retains that stronger normalization and all H4 flow.
- `S_4,m=4`: 120 words and 13 Hurwitz components; whole-word H4 cannot be
  omitted.  This is below the four-label minimal full-support length.
- `S_4,m=6`: 3,936 bridge words and 17 pure-Hurwitz components; M60 was
  checked on both fixed-tree shapes and all 2,880 minimal words.
- At N=5 the eight reducible core components and exact balanced union produce
  the masses (2.6); they do not produce a bottleneck.
- Path and doubled-tree endpoints are retained as ordered words.  No parity,
  graph-only quotient, commuting-color simplification, or failed length-two
  simulation is used.
- No canonical-hub congestion is hidden in M62.  Its only routing dependency
  is M60's polynomial deletion-cell construction and explicit recovery load.
- Every r=4 and r=5 transition remains in the literal kernel and adds
  nonnegative flow; the proof lower-bounds with a fully normalized H3 subset.

## 8. Artifacts and reproduction

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-14/mission-M62-macro-closed-core-lift-redteam/
```

Command from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M62-macro-closed-core-lift-redteam/mass_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M62-macro-closed-core-lift-redteam/mass-check.json
```

The calculation tests the exact N=5 masses and constant and could falsify an
arithmetic/orientation transcription; it cannot prove the universal theorem.
Metadata: commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
3.12.3, seed `null`, no nonstandard dependency.

SHA-256:

```text
6b395cc223db3db53b590d225a8ed26eb4dacb53d57b7d5e4ff0b601d0dd0cf4  mass_check.py
88b28be03286d4964c4baf6db57d02717ef035d65f660df5b4ac10a0f1155c4e  mass-check.json
```

The universal dependency and its full falsification artifacts are frozen in

```text
cycle-13/mission-M60-fixed-tree-leaf-cell-expansion/
```

with hashes recorded in the M60 report.

## 9. Verdict

**PROVED.** Both macro-closed placements in (1.1), including every assigned
path-core component or balanced union, have the universal inverse-polynomial
two-sided conductance bound (1.2).  This scoped verdict is nonterminal for the
global goal.

