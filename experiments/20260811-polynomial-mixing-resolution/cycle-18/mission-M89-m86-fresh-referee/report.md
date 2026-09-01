# M89 fresh referee report on frozen M86

Date: 2026-08-12.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact decision, claim, convention, and scope

**ACCEPT.**

Numbered material objections: **none**.

The accepted positive theorem is exactly the following scoped statement.
For `L>=1`, put

```text
d=8L^2,  k=16L^2,  N=d+2,  m=k+2=2N-2.
```

There is a polynomial-size indexed, state-independent law on literal signed
Hurwitz words which, from every source obtained from `W_L` by a global label
relabeling, cyclic factor phase, and interleaving with one disjoint doubled
edge, reaches M75's marked set with probability at least

```text
eta_L >= 1/[k binom(k+2,2)].
```

Its expected and maximum word lengths have the bounds stated by M86.  On each
fixed labeled-macro slice of that source class, it yields M86 equation (2.13)
for every subset of the slice.  Separately, any signed-Hurwitz word taking
`W_L` to a safe adjacent equal pair has length at least `(L-2)/2`.

The accepted statement is **not** a cover of an arbitrary two-component
macro, a coarea theorem for subsets not contained in the covered class, an
unrestricted `H4/H5` distance bound, a full-`K` conductance or gap theorem, or
Terminal A/B.

The convention is consistent throughout:

```text
(pq)(x)=p(q(x)),
eval(t_0,...,t_(m-1))=t_0...t_(m-1),
R_i(a,b)=(b,bab),  R_i^(-1)(a,b)=(aba,a).
```

The target remains uniform on `Omega(N,m)` for the literal lazy exact
same-product `{3,4,5}` heat-bath kernel.

## 2. Full independent audit

### 2.1 Frozen provenance and the M13 stored braid

The three requested digests match exactly:

```text
5c09b466fc404ee7145f87125456f23e539fffb1e8c0aeff0264ded32a78a6ff  M86 report.md
c147163c711ba06b82b8248d0d86fe4ef6ecd7d8b8ae9c2014944e1bc7e25682  M86 signed_cover_theorem.md
34e1d07d5cda1188dc757d3eb9b6bd32ff5c6daddef5471bdb9f2a124e7d5cbd  M86 SHA256SUMS
```

I also ran `sha256sum -c` on M86's ten-entry manifest; every entry passed.
No frozen M86 source was modified.

M13's accepted quantitative Classification-H statement applies to two
identity transposition words with the same labeled weighted support
components.  Both `W_L` and

```text
C_d=(01)^2(12)^2...((d-2)(d-1))^2(01)^2
```

are length-`k` identity words on the same `d` labels with one connected
support component of weight `k`.  They therefore satisfy the hypotheses.
The accepted construction supplies at most `25 d k^3` literal signed
generators from either word to the same componentwise canonical word, hence
a safe pairwise bound `50 d k^3`.

The extra state-independence step is valid.  Choose deterministic tie breaks
in the accepted finite searches and scans, run the algorithm only on the two
fixed public templates, concatenate the first emitted sequence with the
reverse of the second, and store that positional index/sign word as
`beta_L`.  All adaptive choices occur during public precomputation.  Later
application is one fixed bijection.  M13's bounded searches, scans, and
literal rewrites give polynomial generation time as well as polynomial
output length.  This use is a template-to-template path, not a canonical-hub
comparison routing.

### 2.2 Generatorwise relabel equivariance

For simultaneous conjugation by a label permutation `sigma`,

```text
sigma(bab)sigma^(-1)
 =(sigma b sigma^(-1))(sigma a sigma^(-1))(sigma b sigma^(-1)).
```

The same identity holds for the inverse generator.  Thus every fixed
positional signed generator, and hence the stored `beta_L`, commutes with
global relabeling.  Therefore

```text
beta_L(sigma W_L)=sigma C_d.
```

The normalizer algorithm itself need not make equivariant branching; only
the already stored word acts on relabeled sources.

### 2.3 Phase and stable interleaving correction

For `rho_k=R_0R_1...R_(k-2)`, bubbling `t_0` right produces final factor
`S^(-1)t_0S`, where `S=t_1...t_(k-1)`.  Identity of the total product and
involutivity give `S=t_0`, so `rho_k` is literal cyclic left shift.  Hence
`rho_k^(-q)` exactly reverses phase `q` with length `q(k-1)`.  Uniform `q`
has mean cost `(k-1)^2/2` and maximum `(k-1)^2`.

For pair slots `I={a,b}`, `a<b`, the M86 stable sort first applies indices
`b,...,k`, then `a,...,k-1`.  Because the doubled edge is disjoint from every
genus-one factor, all these moves are ordinary commutations.  The right copy
ends in slot `k+1`, the left copy ends in slot `k`, and the relative genus-word
order is unchanged.  Its exact length is

```text
(k+1-b)+(k-a)=2k+1-a-b,
```

with maximum `2k` and uniform mean `k`.  Thus the composite order

```text
gamma_(I,q)=S_I rho_k^(-q) beta_L
```

first sorts, then corrects phase, then applies `beta_L`, as required.

### 2.4 Marked target and indexed-law accounting

Deleting the final `(01)^2` of `C_d` leaves the identity doubled path on all
`d` vertices, so that square is a connected-deletable genus-one certificate.
After stable sorting, the ambient disjoint square remains the other minimal
component.  For the matching metadata,

```text
gamma_(I,q) x_(sigma,q,I)=sigma(C_d),sigma(e),sigma(e),
```

which lies in M75's marked set.

There are exactly

```text
P_L=k binom(k+2,2)
```

indexed pairs `(q,I)`.  Uniform indexed sampling is independent of the
source, and at least one matching index succeeds for every covered source,
so `eta_L>=1/P_L`.  Duplicate source representations or duplicate braid
group elements cannot reduce the mass of that indexed entry.  The length
bounds are consequently

```text
E ell <= 50 d k^3 +(k-1)^2/2+k,
max ell <= 50 d k^3 +(k-1)^2+2k.
```

### 2.5 M75 specialization and the restricted-source issue

Here `N=d+2>=10`, `m=k+2=2N-2`, and `M=binom(N,2)`.  Every specified signed
generator is a padded `H3` outcome with lower bound

```text
p_H=1/[6(m-2)M^2].
```

M75's marked refresh has exact probability

```text
1/[6(m-2)D_N],
D_N=(3N^2+N-12)/2 <= M^2,
```

so `p_H` lower-bounds it too.

The apparent difference from M75—M75 states a worst-source hit hypothesis on
all of `Gamma`, while M86 proves it only on `X_(L,Gamma)`—does not invalidate
equation (2.13).  Rerun M75's charging proof with demand sources only
`x in S`, where `S subseteq X_(L,Gamma)`.  The matching index supplies
endpoint success mass at least `1/P_L` for every such `x`.  For any sampled
index, if the path first leaves `S`, charge that first edge.  In particular,
an edge from `X_(L,Gamma)` to `Gamma minus X_(L,Gamma)` is an edge from `S`
to `Gamma minus S` and is counted, even though it remains in the same macro.
If the successful matching path never leaves `S`, charge its terminal edge
to `F_N minus A`.

All signed Hurwitz paths remain bijections of the full macro `Gamma`.  Thus
the restricted demand has the same actual-edge load bound, and

```text
sum_(x in S) K(x,(Gamma minus S) union (F_N minus A))
 >= p_H |S|/[P_L max(Dbar_L,1)]
```

is valid exactly for `S subseteq X_(L,Gamma)`.  It gives no conclusion for an
arbitrary `S subseteq Gamma` containing uncovered sources.

### 2.6 Inverse-prefix actual-edge recovery

Fix an indexed word, a prefix time, and an actual directed path edge.  Its
source state followed by the inverse prefix determines at most one original
source.  Summing over prefix times and indexed-word probabilities therefore
bounds path-edge load by

```text
sum_gamma mu(gamma) ell(gamma)=Dbar_L,
```

not by family cardinality times `Dbar_L`.  In the endpoint-only version, a
fixed terminal directed edge and full indexed word recover one source, so
terminal load is at most one.  The common denominator
`max(Dbar_L,1)` is correct.  Parallel indexed entries remain separate only in
the probability sum and cause no additional factor.

### 2.7 Occurrence-band pullback and signed-distance lemma

Lemma 7.1 counts factor-occurrence strands in the inverse braid diagram.  It
does not recursively expand a current conjugated transposition into a word in
original graph edges.  Under one inverse local signed Hurwitz rectangle:

- if neither marked strand meets it, the pulled-back annulus is unchanged;
- if a marked strand meets it, only the sole conjugated occurrence changes,
  and its two endpoint tracks add or remove at most two traversals of the
  other occurrence band;
- if both marked collision occurrences meet it, the same statement applies:
  one output occurrence is conjugated and the other is carried; equal factors
  are literally fixed.

Every current occurrence band is the image of one earlier occurrence band
under the accumulated ribbon homeomorphisms.  Pulling a traversal of that
whole carried band through all earlier rectangles therefore returns one
original `W_L` occurrence band, rather than expanding its current
transposition path.  Induction gives at most two closing-band traversals plus
two per signed generator.  Since every original voltage-band coordinate lies
in `{-1,0,1}`,

```text
|V_x|,|V_y| <= 2q+2.
```

The endpoint equal-pair annulus has an embedded core.  Safety is exactly
nonseparation; inverse Hurwitz ribbon slides preserve embeddedness and
nonseparation.  M84/M85's accepted integral torus-cover calculation makes the
homology map injective with image `L Z^2`.  Hence the pulled-back safe curve
has

```text
V in L Z^2 minus {(0,0)}.
```

Some coordinate has magnitude at least `L`, proving
`q>=(L-2)/2`.  This is a signed-generator, equivalently specified padded-`H3`,
distance lower bound.  It does not constrain one unrestricted `H4` or `H5`
update and is only polynomial in `N,m`.

## 3. Probability, runtime, path, and congestion accounting

| item | accepted value or bound | status |
|---|---:|---|
| public-template braid | `<=50 d k^3` signed generators | inherited M13, valid specialization |
| phase cost | exact `q(k-1)` | proved |
| stable-sort cost | exact `2k+1-a-b`; mean `k`; max `2k` | proved |
| indexed family | `P_L=k binom(k+2,2)` | proved |
| covered-row hit | `eta_L>=1/P_L` | proved |
| expected length | `<=50dk^3+(k-1)^2/2+k` | proved |
| maximum length | `<=50dk^3+(k-1)^2+2k` | proved |
| signed path edge | `p_H=1/[6(m-2)M^2]` | inherited M75 |
| marked refresh | `1/[6(m-2)D_N]>=p_H` | inherited M75 |
| actual path-edge load | `<=Dbar_L` | proved |
| endpoint-edge load | `<=1` | proved |
| restricted coarea denominator | `P_L max(Dbar_L,1)` | proved |
| signed distance | `q>=(L-2)/2` | proved |

Because `d,k,m` are of the same order, cover words have `O(m^4)` length and
the family index space has `O(m^3)` size.  Sampling and emitting an indexed
word is polynomial in `N,m`, not necessarily in wire count `log_2 N`.  No
canonical-hub congestion claim is made.

## 4. Dependencies and claim ledger

| claim/input | status | audit action |
|---|---|---|
| `W_L` identity, connected support, genus-one cover | inherited proved M78/M81/M84/M85 | hypotheses checked |
| Classification H and `50Nm^3` pair diameter | inherited accepted M13 | exact component hypotheses and use checked |
| deterministic stored `beta_L` | proved M86 | accepted |
| generatorwise relabel equivariance | proved M86 | algebra checked |
| phase/interleaving cover | proved M86 | symbolic and finite checks passed |
| M75 endpoint charging and constants | inherited accepted M75/M77 | restricted-demand specialization checked |
| Lemma 7.1 occurrence-band bound | proved M86 | local cases and global induction checked |
| cover homology implication | inherited proved M84/M85 | convention and nonzero-image use checked |
| arbitrary-macro cover | unresolved | correctly excluded |
| full-`K` gap/conductance and Terminals | unresolved | correctly excluded |

No new literature theorem is invoked by M86.  The delicate inputs are already
accepted project dependencies, not silently upgraded empirical claims.

## 5. First unproved standalone proposition

The first surviving obligation remains M86's stated one:

> For every labeled two-component minimal exterior macro, construct a
> polynomial-time state-independent bijective marked-cover law with
> polynomial expected length and inverse-polynomial worst-source hit, or
> directly prove the needed arbitrary-partial-macro first-boundary flow bound
> with polynomial actual-edge occupation.

The accepted voltage symmetry class need not carry nonnegligible mass inside
an arbitrary macro, so this is strictly unresolved.

## 6. Strongest self-attack, corrections, and objections

The strongest possible attack is on Lemma 7.1: algebraically expanding the
current conjugated transposition could make an added traversal appear to
expand recursively under earlier moves.  That would destroy the linear
`2q+2` count.  The proof avoids exactly that invalid representation.  A
Hurwitz rectangle is a ribbon homeomorphism with labeled occurrence bands;
the added arc follows one whole current band, whose complete inverse image is
one original occurrence band.  The local both-marked case still conjugates
only one occurrence.  I find this topological occurrence-strand induction
valid.

Numbered material objections:

```text
None.
```

Nonmaterial corrections:

```text
None required.
```

The owned finite probe is supporting falsification evidence only; acceptance
of Lemma 7.1 rests on the occurrence-band/ribbon argument, not on that probe.

## 7. Boundary cases and independent calibrations

- The theorem starts at `L=1`, so its actual ambient instances have
  `N>=10,m>=18`.  Odd `m`, `m=0`, `m=2`, and `N=2` are outside its geometry,
  not missing cases.
- M84's positive-elimination zero row starts only at `L>=11`; M86 uses signed
  inverse moves and a different stored law, so there is no contradiction.
- The family audit was independently rerun at `L=1,2,3`.  It passed every
  checked identity, connectedness, marked-target, phase, stable-sort,
  relabel-equivariance, family-count, and length identity.  All `153` pair
  interleavings at `L=1` and all `2145` at `L=2` were exhausted.
- The local signed-rectangle audit was rerun for `S_3` through `S_6`.  All
  `740` oriented signed transposition-pair cases passed, including the
  convention where both factor occurrences are tracked.
- An independent exact occurrence-conjugator/voltage probe followed four
  fixed-seed 5,000-step signed walks on `W_1`.  It checked `10,234` adjacent
  equal-pair observations, including `5,050` safe pairs.  Safety agreed with
  nonzero pulled-back torus homology in every case, and no `2q+2` failure was
  found.  These are exact facts about the replayed states and empirical
  coverage of possible states.

No finite check is used to prove a universal theorem.

## 8. Artifacts and exact reproduction

Owned artifacts are:

```text
plan.md
checkpoint.md
general_pullback_probe.py
family-rerun.json
local-rectangle-rerun.json
pullback-probe.json
report.md
freeze_manifest.md
SHA256SUMS
```

Commands from repository root were:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/family_audit.py \
  --L 1 2 3 --seed 860086 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M89-m86-fresh-referee/family-rerun.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/local_signed_rectangle_audit.py \
  --N 3 4 5 6 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M89-m86-fresh-referee/local-rectangle-rerun.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M89-m86-fresh-referee/general_pullback_probe.py \
  --case 8601 5000 --case 8902 5000 --case 8903 5000 --case 8904 5000 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M89-m86-fresh-referee/pullback-probe.json
```

Python was `3.12.3`; all scripts use only the standard library.  JSON files
record commit, exact arguments, seeds, convention, runtime, and scope.  All
bytecode caches created during review were removed.  `SHA256SUMS` freezes the
owned payload, and `freeze_manifest.md` records the source boundary.

## 9. Final classification

```text
ACCEPT M86 WITH ZERO MATERIAL OBJECTIONS.

PROVED, SCOPED:
  polynomial indexed signed marked cover for the complete
  relabel/phase/interleaving class of W_L;
  M75 coarea bound for S subseteq X_(L,Gamma);
  signed-Hurwitz distance q >= (L-2)/2 from W_L to a safe square.

UNRESOLVED:
  arbitrary two-component macro cover or partial-macro flow;
  unrestricted heat-bath distance;
  full-K conductance, spectral gap, polynomial mixing, Terminal A/B.
```
