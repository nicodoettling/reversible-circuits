# M86 final report: a signed marked-cover bypass on the voltage symmetry class

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, target, and scoped outcome

Permutations compose as `(pq)(x)=p(q(x))`, tuple factors are evaluated
left-to-right, and signed right Hurwitz generators are

```text
R_i(a,b)=(b,bab),          R_i^(-1)(a,b)=(aba,a).
```

The project target remains uniform on

```text
Omega(N,m)={w in T_N^m:eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` heat-bath kernel

```text
K=(1/2)I+(1/6) sum_(r=3)^5
      (1/(m-r+1)) sum_i H_(i,r).
```

This mission concerns only M75's two-component minimal-exterior marked-cover
subproblem after M84/M85 proved an exact zero row for the canonical positive
elimination law.

The main outcomes are:

1. **PROVED:** M84's voltage family does not obstruct all state-independent
   signed laws.  For `d=8L^2`, `k=16L^2`, there is a polynomial-time
   samplable indexed family of literal signed Hurwitz words covering `W_L`,
   every global relabeling, every cyclic factor phase, and every interleaving
   with the disjoint ambient doubled edge.  Its exact size and row bound are

   ```text
   P_L=k binom(k+2,2),                 eta_L>=1/P_L.
   ```

   Its expected length is at most

   ```text
   Dbar_L<=50 d k^3 +(k-1)^2/2+k.
   ```

   Every successful endpoint has a connected-deletable square in the
   genus-one component.
2. **PROVED:** the law has literal inverse-prefix actual-edge recovery and,
   on each fixed labeled-macro slice of the covered class, plugs into M75's
   accepted endpoint coarea theorem with all heat-bath normalizations shown
   below.
3. **PROVED:** every signed Hurwitz word taking `W_L` to a safe adjacent
   square has at least `(L-2)/2` generators.  This only rules out uniformly
   bounded signed templates; it is polynomial in the ambient parameters.
4. **EXACT FINITE / EMPIRICAL:** fixed-seed random signed walks produced
   replay-verified safe endpoints at lengths `68` for `L=1` and `23789` for
   `L=2`.  No hit occurred in `200000` steps at `L=3`; that miss is empirical
   only and is not used in either proof.
5. **UNRESOLVED:** the cover is not proved for every word in an arbitrary
   two-component macro.  It gives no full exterior conductance bound, no gap
   estimate for `K`, and neither Terminal A nor Terminal B.

The complete proof is `signed_cover_theorem.md`.

## 2. Full construction and proof

### 2.1 A fixed marked target and fixed template braid

Define the length-`k` word

```text
C_d=(01)^2(12)^2...((d-2)(d-1))^2(01)^2.          (2.1)
```

It is an identity word.  Its support is the connected path on `d` vertices,
and deleting the final surplus `(01)^2` leaves the connected identity doubled
path.  Thus the last two factors are a literal M75 deletion certificate.

The accepted M13/L-0037 constructive Classification-H audit supplies a
signed path of at most `25 d k^3` moves from any one connected identity word
to its componentwise canonical word and hence pairwise diameter at most
`50 d k^3`.  Make its constructive procedure deterministic using
lexicographically first shortest support paths, earliest eligible factor
occurrences, and leftmost pair-reordering choices.  Run it on each of the two
fixed public templates `W_L,C_d`, concatenate the first path with the reverse
of the second, and freeze the emitted index/sign sequence as `beta_L`.  Then

```text
beta_L(W_L)=C_d,                 |beta_L|<=50 d k^3.   (2.2)
```

The branching needed to compute `beta_L` happens once on the public
templates.  Applying the stored word is one fixed bijection, not a
source-adaptive search.  The audited construction uses graph searches,
linear scans, and explicit `R_i^{+/-1}` rewrites, so both generation time and
output length are polynomial.

For any global label permutation `sigma`, conjugation commutes with each
signed Hurwitz generator.  In particular,

```text
beta_L(sigma W_L)=sigma C_d.                       (2.3)
```

This is generator-by-generator equivariance, not a cardinality argument.

### 2.2 Cyclic phases and ambient interleavings

Put

```text
rho_k=R_0R_1...R_(k-2).                            (2.4)
```

On any identity word, `rho_k` is literal cyclic left shift: the conjugated
last factor is `S^(-1)t_0S=t_0` because `t_0S=id`.  Therefore
`rho_k^(-q)` corrects phase `q` in exactly `q(k-1)` signed generators.  The
worst phase cost is `(k-1)^2`; its uniform-`q` mean is `(k-1)^2/2`.

Adjoin the doubled edge `e=(d,d+1)`.  Let `I={a,b}`, `a<b`, be its two
slots among the `k+2` ambient positions.  The fixed word `S_I` first bubbles
the right occurrence through indices `b,...,k` and then the left occurrence
through `a,...,k-1`.  On the matching source these are ordinary disjoint
commutations, so

```text
S_I Interleave_I(u,e,e)=u,e,e,
|S_I|=2k+1-a-b<=2k,             E_I|S_I|=k.         (2.5)
```

For every global relabeling `sigma`, phase `0<=q<k`, and pair-slot set `I`,
define

```text
x_(sigma,q,I)=Interleave_I(sigma rho_k^q(W_L),sigma(e),sigma(e)),
gamma_(I,q)=S_I rho_k^(-q) beta_L.                 (2.6)
```

The latter two words act only on the first `k` slots after sorting.  Directly,

```text
gamma_(I,q)x_(sigma,q,I)=sigma(C_d),sigma(e),sigma(e),   (2.7)
```

whose specified genus-one square is globally adjacent and safe.  Uniform
choice of the indexed pair `(I,q)` is independent of the source and gives

```text
P_L=k binom(k+2,2),            eta_L>=1/P_L.        (2.8)
```

Possible duplicate braid representations are parallel indexed family
members; they do not remove the matching index's probability `1/P_L`.
Uniform `q` has mean `(k-1)/2`, so (2.2) and (2.5) give

```text
Dbar_L<=50 d k^3 +(k-1)^2/2+k.                     (2.9)
```

Separately, the maximum family-word length is

```text
max_(I,q)|gamma_(I,q)|<=50 d k^3+(k-1)^2+2k.       (2.10)
```

### 2.3 Actual-edge recovery and restricted-class coarea

Every prefix of every indexed word is a bijection on its full Hurwitz macro.
Given word index, prefix time, and an actual directed path edge, applying the
inverse prefix recovers at most one original source.  Parallel family entries
remain distinguished by their indices.  Thus the weighted load is controlled
by `Dbar_L`, exactly as in M75; there is no factor equal to family cardinality.

Use ambient parameters

```text
N=d+2,        m=k+2=2N-2,        M=binom(N,2).      (2.11)
```

Every specified signed Hurwitz step is a padded `H3` transition with

```text
p_H=1/[6(m-2)M^2].                                 (2.12)
```

The terminal marked refresh has exact probability
`1/[6(m-2)D_N]`, where `D_N=(3N^2+N-12)/2<=M^2`, so (2.12) lower-bounds it
as well.

Fix one labeled two-component macro `Gamma` and let `X_(L,Gamma)` be its
slice of sources in (2.6).  M75's endpoint charging then gives, for every
`S subseteq X_(L,Gamma)`,

```text
sum_(x in S) K(x,(Gamma minus S) union (F_N minus A))
 >=p_H |S|/[P_L max(Dbar_L,1)].                    (2.13)
```

A wrong index may leave `X_(L,Gamma)`; if it leaves `S`, that is already a
valid first crossing.  Equation (2.13) is therefore a literal
arbitrary-subset coarea bound for the covered source class.  It does not
control a partial macro whose mass lies mostly outside that class.

### 2.4 The signed-distance lower bound

Suppose a signed word of `q` generators maps `W_L` to a safe adjacent equal
pair.  Mark the two endpoint factor occurrences and pull their pair annulus
back through the braid diagram.  A local inverse Hurwitz rectangle disjoint
from both marked strands changes nothing.  If a marked strand participates,
the sole conjugated factor's two endpoint tracks add or remove at most two
traversals of the other occurrence band; the same statement covers the case
where both marked strands participate.  Equal factors are fixed.

Crucially, this is an occurrence-strand count: under the full pullback each
carried band returns to one original `W_L` occurrence band.  It is not
expanded recursively as a path representing its current transposition.  The
two closing bands contribute two traversals, and each generator contributes
at most two more.  Because every original band has each integral base-voltage
coordinate in `{-1,0,1}`, the pulled-back curve has

```text
|V_x|,|V_y|<=2q+2.                                  (2.14)
```

Safety means this embedded curve is nonseparating.  M84's accepted torus
cover theorem gives

```text
V in L Z^2 minus {(0,0)}.                           (2.15)
```

Thus one coordinate has magnitude at least `L`, and

```text
q>=(L-2)/2.                                        (2.16)
```

This counts signed Hurwitz generators, equivalently specified padded-`H3`
steps.  An unrestricted `H4/H5` move need not admit this tracking, so (2.16)
is not an unrestricted heat-bath distance lower bound.  Since
`N,m=Theta(L^2)`, it is not a superpolynomial obstruction.

## 3. Probability, runtime, path, and congestion accounting

| item | exact value or bound | status |
|---|---:|---|
| voltage vertices/factors | `d=8L^2`, `k=16L^2=2d` | inherited proved |
| ambient parameters | `N=d+2`, `m=k+2=2N-2` | proved |
| fixed template path `beta_L` | `<=50 d k^3` signed generators | inherited constructive diameter, specialized here |
| cyclic phase correction | exact `q(k-1)`; worst `(k-1)^2`; mean `(k-1)^2/2` | proved |
| stable pair sort | `2k+1-a-b<=2k`; uniform mean `k` | proved |
| indexed family size | `P_L=k binom(k+2,2)` | proved |
| worst covered-row hit | `eta_L>=1/P_L` | proved |
| expected word length | `Dbar_L<=50dk^3+(k-1)^2/2+k` | proved |
| maximum word length | `<=50dk^3+(k-1)^2+2k` | proved |
| specified signed path edge | `p_H=1/[6(m-2)M^2]` | inherited accepted M75 |
| specified marked refresh | `1/[6(m-2)D_N]>=p_H` | inherited accepted M75 |
| actual-edge load | endpoint form `<=max(Dbar_L,1)` | proved via inverse prefixes |
| restricted-class coarea | equation (2.13) | proved |
| signed distance to mark | `q>=(L-2)/2` | proved |
| full-macro row bound | none | unresolved |
| full-`K` gap/conductance | none | unresolved |

With `d=Theta(k)=Theta(m)`, the dominant cover word bound is `O(m^4)`;
`P_L=O(m^3)`.  Sampling an index and emitting its word is polynomial in
`N,m`.  The construction is not claimed efficient in wire count
`log_2 N`.

## 4. Dependencies and claim status

| input or claim | status | evidence/dependence |
|---|---|---|
| `W_L` identity, connected support, torus cover | inherited proved, M78/M81/M84/M85 | frozen accepted artifacts |
| M84 canonical positive law has zero row for `L>=11` | inherited proved | M84 accepted by M85 |
| quantitative Classification-H algorithm and `50N m^3` pair diameter | inherited proved | M13, ledger L-0037 |
| deterministic fixed-template specialization `beta_L` | proved here | fixed tie breaking plus two accepted normalizer paths |
| relabel equivariance | proved here | generator algebra (2.3) |
| phase/interleaving correction | proved here | explicit braid words (2.4)--(2.6) |
| polynomial indexed cover of the symmetry class | proved here | endpoint identity (2.7) |
| exact coarea constants | inherited M75, specialized here | equations (2.11)--(2.13) |
| crossing-voltage/signed-distance lemma | proved here | band-occurrence pullback and M84 cover homology |
| exact `L=1,2` random-walk paths | exact finite | replay and inverse checks in owned script |
| `L=3` random-walk miss | empirical | one fixed seed, not used in proof |
| arbitrary two-component macro cover | unresolved | symmetry class may be negligible |
| Terminal A or Terminal B | unresolved | no full-chain gap or bottleneck follows |

No new literature theorem is invoked.  The only classification input is the
already audited and coordinator-accepted constructive result.

## 5. First unproved standalone step

The exact surviving exterior obligation is:

> **ARBITRARY-MACRO NONCANONICAL MARKED-COVER LEMMA.**  For every labeled
> two-component minimal exterior macro `Gamma`, construct a polynomial-time
> state-independent law on bijective local transport words with polynomial
> expected length and inverse-polynomial marked-hit probability for every
> `x in Gamma`; or prove a direct arbitrary-partial-macro first-boundary flow
> inequality with polynomial actual-edge occupation.

Classification H gives each source a polynomial adaptive route to the marked
target, but an arbitrary macro may realize exponentially many branches of the
normalizer.  The present theorem succeeds because the voltage symmetry class
collapses all source variation to polynomial metadata `(I,q)` plus a global
relabeling handled equivariantly.  Proving an analogous polynomial metadata
collapse, or bypassing word covers with direct flow, is the first unproved
step.

## 6. Strongest self-attack

1. The theorem deliberately uses the safe `50 d k^3` pairwise bound.  It does
   not assume that the doubled path (2.1) is literally the normalizer's
   tie-broken canonical output.
2. `beta_L` is fixed only after polynomial precomputation on the public
   templates.  Re-running the adaptive normalizer separately on an unknown
   source would violate state independence and is not part of the law.
3. The cover handles global relabelings for free by equivariance, but not
   arbitrary Hurwitz-orbit variation.  A large symmetric orbit of one
   template need not have nonnegligible stationary macro mass.
4. Family cardinality alone is not a congestion bound.  The proof uses
   indexed-word probability, expected length, and literal inverse-prefix
   recovery; parallel indices are retained.
5. The delicate new point is Lemma (2.14).  It counts carried occurrence
   bands in the inverse braid diagram, not arbitrary current transposition
   paths.  A referee should redraw the local signed rectangle, especially
   when a marked collision strand participates, rather than infer the bound
   from M84's positive-elimination subset formula.
6. Even if (2.16) were sharpened, any polynomial signed distance is compatible
   with polynomial mixing.  It supplies no stationary cut or smaller-side
   mass estimate.
7. The finite random paths are not the family used in the proof and their
   observed lengths are not extrapolated.

## 7. Boundary cases and falsification checks

- The construction holds for every integer `L>=1`.  M84's zero-row theorem
  begins only at `L>=11`; there is no contradiction because the present words
  use inverse moves and a fixed Classification-H route rather than canonical
  positive elimination.
- At `L=1,2,3`, the exact family audit verifies `W_L` identity and
  connectedness; `C_d` identity and safe final deletion; phase correction at
  `q=0,1,floor(k/2),k-1`; all `153` pair interleavings at `L=1`; all `2145`
  at `L=2`; representative extremes at `L=3`; and respectively `64,100,100`
  signed-generator relabel-equivariance checks.
- The local signed-rectangle audit exhausts all `18+72+200+450=740`
  oriented signed transposition-pair cases in `S_3` through `S_6`.  It finds
  zero inverse, occurrence-label, or two-endpoint-bound failures, including
  the convention where both factor occurrences are declared tracked.  This
  is a finite falsification check of the local algebra, not the all-length
  pullback induction.
- The exact family sizes are `2448`, `137280`, and `1524240` for
  `L=1,2,3`, matching `k binom(k+2,2)`.
- Fixed-seed path replay verifies product identity, connected safe deletion,
  endpoint hash, and inverse return to `W_L`.  The exact move-sequence hashes
  are `01569901365f1ae24d55d71df8e3281002e611dae36b8c12fdbb36223fc84086`
  at `L=1` and
  `d9b346d1fe8fe2328e5240811ecb5fc636399c79f7e1591fb20b53a2bce925fb`
  at `L=2`.
- Odd `m`, `m=0`, `m=2`, and `N=2` do not instantiate this positive-genus
  two-component construction.  They are not counterexamples or omitted cases
  of the theorem.

Finite checks are falsification tests.  Universal claims use the algebraic,
constructive, and topological proofs above.

## 8. Artifacts and exact reproduction

Owned artifacts are:

```text
plan.md
checkpoint.md
signed_cover_theorem.md
family_audit.py
family-audit-results.json
signed_bypass_probe.py
signed-bypass-probe-results.json
local_signed_rectangle_audit.py
local-signed-rectangle-results.json
report.md
SHA256SUMS
```

Commands from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/family_audit.py \
  --L 1 2 3 --seed 860086 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/family-audit-results.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/signed_bypass_probe.py \
  --case 1 10000 8601 --case 2 200000 8602 --case 3 200000 8603 \
  --check-every 1 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/signed-bypass-probe-results.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/local_signed_rectangle_audit.py \
  --N 3 4 5 6 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/local-signed-rectangle-results.json
```

Python was `3.12.3`; all three scripts use only the standard library.  The family
audit seed is `860086`; signed-walk seeds are `8601,8602,8603`.  JSON outputs
record commit, exact arguments, convention, Python version, dependencies,
elapsed time, and exact/empirical scope.  `SHA256SUMS` freezes the payload.

## 9. Verdict

```text
PROMOTE, SCOPED:
  PROVED polynomial noncanonical signed marked cover on the entire natural
  relabel/phase/interleaving class of W_L.

PROVED:
  any signed-Hurwitz route from W_L to a safe square has length at least
  (L-2)/2.

RETAIN:
  M84 still refutes the canonical positive-elimination row law.

UNRESOLVED:
  arbitrary two-component macro cover/direct partial-macro flow;
  full-K conductance, spectral gap, Terminal A, and Terminal B.
```

The voltage family is therefore a discriminator between transport laws, not
an obstruction to all polynomial signed transport.  The next useful work is
to discover whether arbitrary macro words admit a comparable polynomial
metadata collapse or require a direct flow construction.
