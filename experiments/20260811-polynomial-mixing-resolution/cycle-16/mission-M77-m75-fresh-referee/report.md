# M77 fresh referee report on frozen M75

Date: 2026-08-12.  Recorded repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict

**ACCEPT.**

Numbered objections: **none**.

Material corrections: **none**.

Nonmaterial corrections: **none**.

The frozen M75 report proves exactly its two scoped positive statements—the
randomized bijective first-crossing implication and the post-certificate M60
null-push construction—while exactly refuting only the proposed radius-one
direct-certificate cover.  Its simple-positive-braid row bound and multilevel
merger occupation statement remain explicitly unresolved.  It does not claim
a full exterior-cut theorem, a Terminal result, a full-`K` conductance
upper bound, a spectral-gap bound, or polynomial mixing.

## 2. Frozen source and convention

The audited files have exactly the required SHA-256 values:

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
17bb22b3c041ec1917f206d0a3cf9a8fba2f049fd5a6b61da2eb004699a6b89b  M75 freeze_manifest.md
```

I also independently recomputed every artifact hash listed in the frozen
manifest; all nineteen entries match.  No M75 or predecessor artifact was
modified.

The source convention is consistent throughout:

```text
(pq)(x)=p(q(x)),
eval(t_1,...,t_m)=t_1...t_m,
R_i(...,a,b,...)=(...,b,bab,...).
```

The global target is uniform on `Omega(N,m)`.  The M75 theorem itself is
scoped to a two-component exterior Hurwitz macro at
`N>=5,m=2N-2` for the literal lazy `{3,4,5}` heat-bath kernel

```text
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r).
```

Every probability below includes laziness, block-size choice, valid-window
choice, and exact same-product conditional sampling.

## 3. Randomized coarea theorem

### 3.1 Normalization and first-crossing recovery

Let `mu` be a state-independent probability law on finite words in
bijective generators of a finite macro `Gamma`, let `G` be marked, and
assume

```text
inf_x Pr_beta[some prefix beta_[0:t] x lies in G] >= eta,
E_mu ell(beta) <= Dbar.
```

For every successful pair `(x,beta)`, stop at its first marked time.  If
the prefix path has already left `S`, charge its first actual directed
edge from `S` to `Gamma\S`; otherwise charge the designated terminal
edge out of the first mark.  The routed weighted demand is at least
`eta|S|`.

For a fixed word `beta`, prefix time `t`, and actual directed path edge,
the edge source and inverse prefix `beta_[0:t]^{-1}` determine at most one
original source.  Thus one path edge gets load at most

```text
sum_beta mu(beta) ell(beta)=Dbar.
```

For a fixed terminal edge and fixed `beta`, the first-hit time can be any
of `ell(beta)+1` values, each recovering at most one source.  Its load is
therefore at most

```text
sum_beta mu(beta)(ell(beta)+1)=Dbar+1.
```

This is genuine actual-edge source recovery; it does not count word labels
as if they were chain edges.  The proof remains valid for countably
supported `mu`: all loads are nonnegative and Tonelli's theorem permits
the sums to be interchanged.  Consequently

```text
sum_(x in S) K(x,(Gamma\S) union T)
 >= p eta |S|/(Dbar+1).
```

The cardinality of the word-law support correctly does not appear.

### 3.2 Endpoint-only variant and zero-length mass

If success is required only at the endpoint, a fixed terminal edge and fixed
word recover one source directly from the inverse full word; there is no
first-hit-time multiplicity.  The total terminal load is at most
`sum_beta mu(beta)=1`, even when `mu` places positive mass on the empty
word.  Path-edge load remains at most `Dbar`.  Thus the correct common
denominator is

```text
max(Dbar,1).
```

The fresh rational audit used a two-state macro with empty-word mass
`1/2`, expected length `Dbar=1/2`, and endpoint hitting probability
`eta=1/2` from each source.  All four subsets satisfy both bounds; the
endpoint version is sharp on the full macro.  This directly tests the
zero-length case omitted from most informal path arguments.

### 3.3 Specialization and cut target

For a two-component exterior macro, a marked state has a designated safe
square refresh into `F_N\A`.  If `S=E_k intersect Gamma`, then:

- a charged path edge leaving `S` within `Gamma` leaves `E_k`, hence
  leaves `C_k=A union E_k`;
- a terminal refresh lands in `F_N\A`, which is disjoint from `E_k`
  because the exterior balls lie in `F_N^c`, and hence also leaves
  `C_k`.

M75's statement that every target in its displayed specialization is
outside `C_k` is therefore correct.

## 4. M60 null-push algebra and literal realization

Choose certified positions `i<j` and write

```text
w=P x U y S,
z=P U S,
eval(w)=eval(z)=id.
```

Cancellation gives

```text
x U y=U,
x=U y U^{-1}.
```

A right Hurwitz bubble transports `x` across the factors
`u_1,...,u_q` of `U`.  After all `q=j-i-1` swaps the moving factor is

```text
U^{-1}xU=y,
```

so the endpoint is exactly `P U y y S`.  If a factor of `U` belongs to a
different support component, it is disjoint from `x,y`, its conjugation
is trivial, and the same global-position bubble is valid.  Hurwitz moves
preserve the entire labeled weighted support macro, so interleaving causes
no hidden preservation failure.

Each adjacent Hurwitz pair identity can be padded by a neighboring unchanged
factor and executed as a specified length-three same-product heat-bath
outcome.  The bubble has length `j-i-1<=m-2`.  Refreshing `y,y` to
`f,f` costs one specified H3 step; sliding
`f f c -> c f f` through the suffix costs `m-j-1`.  Hence the complete
cell path length is exactly bounded as M75 states:

```text
(j-i-1)+1+(m-j-1)=m-i-1<=m-1.
```

For fixed residual `z`, positions `(i,j)`, and later edge `y`, the
intervening word `U` is fixed and `x=UyU^{-1}` is forced.  There are at
most `binom(m,2)M` source descriptions.  For coarea, M75 uses only the
position-indexed bubble and stops at a safe refresh; a fixed word, time, and
directed edge recover the original source by inverse prefix.  It correctly
does not route through the common `zff` hub.

The independent null-push check used
`N=5,m=8`, `x=(02)`, `y=(01)`, and

```text
U=(34),(12),(34),
```

so another nontrivial support component is interleaved inside `U`.  All
six bubble/refresh/slide steps were verified as literal same-product H3
replacements preserving identity and the weighted component signature
`(({0,1,2},6),({3,4},2))`.  Among the 280 allowed
`binom(8,2)binom(5,2)` descriptions over the fixed residual, there were
241 distinct words, confirming the claimed upper—not equality—bound.

## 5. Exact ambient `N=6` radius-one obstruction

The fresh verifier imports no M75 code and exhausts the displayed word

```text
(01),(02),(03),(24),(02),(14),(24),(34),(02),(24)
```

using ambient labels `0,...,5`.  It independently verifies:

- the product is identity;
- labels `0,...,4` form one connected length-ten genus-one component and
  label 5 is isolated;
- among all 45 deletion pairs, exactly `(0,5)` and `(2,7)` preserve
  identity, and both residual supports on `0,...,4` are disconnected;
- all `2(m-1)=18` signed adjacent Hurwitz paths preserve the macro and none
  reaches a connected certificate;
- these paths have 15 distinct endpoints;
- among all `18^2=324` ordered signed two-step paths, exactly 104 reach a
  connected certificate.

Thus the distance to the certificate set is exactly two: absence at radii
zero and one proves the lower bound, and the exhibited two-step hits prove
the upper bound.  This is a complete audit for the particular witness and
rigorously refutes only the proposed radius-one cover.  It supplies no
asymptotic bottleneck or stationary-cut bound, exactly as M75 says.

M75's separate use of M68's infinite `w_q` family is also scoped correctly:
it refutes a universal constant literal-`K` radius to an adjacent square,
but each positive-genus two-label component already admits a direct
two-deletion certificate.  A position-pair bubble may take linear length;
this neither refutes the certificate route nor proves its congestion.

## 6. Positive simple braids, stabilizers, and Garside complementation

### 6.1 Length law

For each `pi in S_m`, the fixed canonical bubble-sort word is a reduced
positive permutation braid and has inversion-count length.  Under uniform
`pi`,

```text
E ell(beta_pi)=m(m-1)/4,
max ell(beta_pi)=binom(m,2).
```

The identity permutation contributes one empty word out of `m!`; the
endpoint theorem's `max(Dbar,1)` denominator handles it.  In M75's
`m=2N-2>=8` scope, `Dbar>1`, and substituting
`p_H=1/[6(m-2)M^2]` gives exactly

```text
p_H eta |S|/Dbar
=2 eta |S|/[3(m-2)M^2 m(m-1)].
```

### 6.2 Double regularity and stabilizer multiplicity

Give the bipartite incidence multigraph one edge
`x -> beta_pi x` for each `x` and `pi`.  Every row has degree `m!`.
For a fixed `pi`, `beta_pi` is a bijection of `Gamma`, so every target
has exactly one preimage for that `pi`.  Summing over `pi`, every column
also has degree exactly `m!`.  Parallel edges created by stabilizers are
edges with different `pi` labels and are included on both sides.  Hence

```text
sum_x #{pi:beta_pi x in G}=m! |G|.
```

This is an exact average identity, not a minimum-row estimate.

The fresh exhaustive `S_3,m=6` calculation enumerated all 240 connected
identity words and all 720 simple positive braids.  It found:

```text
marked states                           216
marked row-count range                  608..720
distinct row-count values               9
column-degree set                       {720}
distinct endpoints per row              15..119
maximum parallel multiplicity set       {12,16,24,48}
double-count totals                     155520=720*216
```

These reproduce the frozen values and explicitly demonstrate why exact
column regularity does not flatten rows.

### 6.3 Garside statement

At the simple-braid/Coxeter level, with longest permutation `w_0`, define
`q=w_0 p^{-1}`.  Then `qp=w_0` and
`ell(q)+ell(p)=ell(w_0)`; the corresponding positive lifts satisfy
`beta^L beta=Delta`.  For the action convention used by M75,

```text
beta x in G
iff Delta x in beta^L G.
```

The marked set moves under complementation.  The independent incidence audit
exhibits a concrete positive simple braid sending a marked word to an
unmarked word, so `G` is not invariant under all such actions.  Moreover,
the inverse of a nonidentity positive braid cannot be positive: its exponent
sum is negative.  M75's Garside paragraph is therefore correct and claims no
spurious row symmetry.

## 7. Probability normalizations

Let `M=binom(N,2)`.  For a fixed transposition `a`, classify a
length-three factorization by its last factor.  The exact count is

```text
D_N
=M+3*2(N-2)+2binom(N-2,2)
=(3N^2+N-12)/2.
```

The fresh script enumerates every length-three word for `2<=N<=8`; every
transposition product fiber has exactly the displayed `D_N`.  It also
checks that every nonempty length-three fiber has size at most `M^2`.
The latter holds generally because the first two output transpositions
uniquely force the third.

For `m=2N-2` and `N>=5`, the literal kernel chooses a nonlazy step and
`r=3` with total weight `1/6`, one of `m-2` windows, and one exact
conditional output.  Thus

```text
p_H=1/[6(m-2)M^2]
```

is a valid lower bound for every used padded Hurwitz edge.  A specified safe
marked refresh has exact probability

```text
p_term=1/[6(m-2)D_N].
```

The inequality `D_N<=M^2` already holds for `N>=2` (equality at
`N=2,3`), hence certainly throughout M75's stated range.  The inherited
whole-macro mark lower bound `3/[Nm(m-1)]` then gives

```text
theta_N=1/[2Nm(m-1)(m-2)D_N],
```

and summing at least `N-2` safe cross-edge outcomes gives
`(N-2)theta_N`.  M75 correctly distinguishes this whole-macro average from
the row-wise hypothesis required for arbitrary partial subsets.

## 8. Scope and dependency audit

The logical separation is sound:

| statement | audited status |
|---|---|
| randomized coarea implication under worst-source hit `eta` | proved |
| M60 null push after a chosen connected certificate | proved |
| displayed `N=6,m=10` radius-one cover | refuted exactly |
| whole two-component macro marked action | inherited accepted average |
| simple-positive-braid worst-row lower bound | unresolved |
| additive actual-edge occupation across `c>=3` mergers | unresolved |
| unconditional full exterior-cut flow | not claimed |
| Terminal A or Terminal B | not claimed |
| superpolynomial conductance upper bound | not claimed |
| inverse-polynomial full-`K` gap or mixing | unresolved and not claimed |

For `c>=3`, a favorable marked refresh generally moves only to component
count `c-1` while remaining exterior; it need not be the first edge out of
`E_k`.  M75 therefore correctly refuses to multiply per-level success
probabilities and instead names an additive actual-edge occupation lemma.
It also correctly avoids global coalescence at one minimal-macro hub, whose
terminal preimages can be superpolynomial.

No new literature theorem is invoked by M75.  Its inherited DYZ and safe
prefix-join-tree inputs were already audited and accepted by M74; M75 uses
their exact accepted statements.  The present verdict does not promote the
unproved simple-braid row bound, Classification-H congestion, a projection
gap, or any finite calibration.

Boundary cases are accurately scoped.  Odd `m` gives an empty bridge
space; `m=0`, `m=2`, and `N=2` do not have the positive-genus minimal
exterior geometry in use.  `S_4,m=4` is not on `m=2N-2`.  The theorem's
`N>=5` restriction is explicit.

## 9. Reproduction and artifacts

Fresh owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-16/mission-M77-m75-fresh-referee/
```

Exact command from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M77-m75-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M77-m75-fresh-referee/independent-results.json \
  --m75-report experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M75-partial-macro-coarea/report.md \
  --m75-manifest experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M75-partial-macro-coarea/freeze_manifest.md
```

Environment: Python 3.12.3; seed `null`; nonstandard dependencies `{}`.
The run is deterministic and standard-library only.  Its final assertions
report:

```text
radius_two_hits=104
braid_row_range=[608,720]
status="all assertions passed"
```

Pre-report owned hashes:

```text
1186fd961c8c53ad7cbcec1abf30b037e67225c424234048afb5aca8cb69dca0  plan.md
a3c43407dd523ce23240967beba710ce3fbfee690fd99228cc1121f234dd6a9a  checkpoint.md
c30e9bebf14693c618976eba042c5ec6e62fc8c7c5dbe7b67f34585a0808bf1e  independent_audit.py
4bc5af9f368d2c6133823ff1d4344f380e43e7576d686631b7137e2a73feac73  independent-results.json
```

The final hashes of these files and this report are recorded in
`freeze_manifest.md`.  Repository status was inspected at completion;
the experiment tree and `notes/` were already untracked globally.  The only
files created or changed by this referee are the six owned M77 artifacts:
the manifest and the five files hashed inside it.  No frozen directory, shared durable file,
manuscript section, skill, or project source was edited.

## 10. Final classification

M75 is acceptable as a **scoped proof-progress plus exact route-refutation**
report.  The result remains nonterminal for the project.  The next
two-component obligation is exactly the simple-positive-braid worst-row lower
bound; even if that succeeds, the separate `c>=3` additive merger
occupation lemma remains.
