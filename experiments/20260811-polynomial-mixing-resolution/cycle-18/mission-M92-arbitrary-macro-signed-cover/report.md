# M92 final report: distributed-root Hurwitz cover reduction and canonical-arborescence obstruction

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, target, and scoped outcome

Permutations compose as `(pq)(x)=p(q(x))`, tuple factors evaluate
left-to-right, and the signed right Hurwitz generators are

```text
R_i(a,b)=(b,bab),             R_i^(-1)(a,b)=(aba,a).
```

The project target remains uniform on

```text
Omega(N,m)={w in Trans(S_N)^m:eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` heat-bath kernel.  This
mission works only at `N>=5,m=2N-2` in one two-component minimal exterior
Hurwitz macro `Gamma`.  Its unique positive-genus component has genus one.
M75's marked set `G_Gamma` consists of states with a globally adjacent square
in that component whose deletion leaves it connected.

The scoped outcomes are:

1. **PROVED:** a polynomial worst-source hitting bound for the declared lazy
   physical signed-Hurwitz walk on `G_Gamma` gives a state-independent law on
   fixed bijective signed words, polynomial expected length, inverse-
   polynomial marked hit, and M75's arbitrary-subset coarea inequality with
   exact actual-edge occupation.
2. **PROVED REDUCTION, CONDITIONAL POLYNOMIALITY:** it suffices to prove an
   inverse-polynomial signed-Hurwitz gap only for connected genus-one words of
   length `2d` on `d` labels.  The genus-zero component can be projected out.
   This is not a new gap proof.
3. **PROVED:** every chronological genus-one factorization torus has an
   elementary tree--cotree certificate with exactly two leftover edges whose
   fundamental cycles form an integral homology basis.
4. **PROVED:** there is an explicit unmarked subset of size `d^(d-2)` in one
   two-component macro.  Any adaptive normalizer sending these states to one
   fixed canonical marked state needs at least `d^(d-2)` distinct fixed
   positional transcripts.
5. **REFUTED, SCOPED:** a fixed-root/polynomial-root random spanning
   arborescence has exponential terminal-edge occupation; a natural uniform
   global-tree guess-and-abort normalizer has marked-hit probability at most
   `d^(-(d-2))` on the explicit unmarked source family.
6. **UNRESOLVED:** no unconditional arbitrary-macro cover, direct partial-
   macro flow, full exterior theorem, full-`K` gap, or Terminal result is
   proved.

All transport paths below are signed Hurwitz paths, realized by specified
padded `H3` outcomes.  No statement is made about unrestricted `H4/H5`
distance.  The full proof note is `oblivious_cover_reduction.md`.

## 2. Full argument

### 2.1 Random-time marked hitting gives an oblivious bijective cover

Declare the physical macro Hurwitz walk

```text
P_Gamma=(1/2)I+[1/(4(m-1))]
                   sum_(i=1)^(m-1)(R_i+R_i^(-1)).       (2.1)
```

It is lazy and reversible for the uniform macro law.  No transitivity theorem
is needed in this subsection: the worst-source hypothesis below itself
supplies all required reachability.  Let `tau_G` be its first hitting time of
`G_Gamma`.
Suppose

```text
inf_(x in Gamma)Pr_x(tau_G<=T)>=a.                    (2.2)
```

Choose `J` uniformly in `{0,...,T}`, sample `J` independent proposals of
(2.1), and omit the holding symbols.  This is a source-independent law on
fixed positional signed-generator words: every sampled word and every prefix
is a bijection on `Gamma`.  Conditional on `J=j`, its endpoint law is
`P_Gamma^j`, so

```text
Pr(beta x in G_Gamma)
 =[1/(T+1)]sum_(j=0)^T P_Gamma^j(x,G_Gamma)
 >=a/(T+1).                                           (2.3)
```

The inequality uses only that every trajectory which hits by `T` contributes
at least one marked visit.  Since `E J=T/2` and half the proposals are
holding, the expected signed-word length is exactly `T/4`.

M75/M77's endpoint first-crossing theorem therefore gives, for every
`S subseteq Gamma`,

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >=p_H a|S|/[(T+1)max(T/4,1)],                       (2.4)
p_H=1/[6(m-2)M^2],       M=binom(N,2).               (2.5)
```

For fixed sampled word, prefix time, and actual directed path edge, inverse
prefix recovers at most one source.  Terminal-edge load is at most one per
word.  Thus (2.4) counts actual `K` edges; the exponentially large support of
the random-word law never appears.  If `S=E_k intersect Gamma`, the charged
targets lie outside `C_k=A union E_k` by the accepted M75 boundary argument.

This yields the strictly targeted next proposition:

> **UNIFORM MARKED HITTING TIME (open).**  There is a polynomial `H(N,m)`
> such that `max_x E_x tau_(G_Gamma)<=H(N,m)` for every two-component minimal
> exterior macro and the walk (2.1).

If it holds, choose `T=ceil(2H)`.  Markov's inequality gives `a>=1/2`; for
`T>=4`, (2.4) becomes

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >=2p_H|S|/[T(T+1)].                                  (2.6)
```

This is weaker than controlling every eigenmode or every set of every
connected Hurwitz orbit.

### 2.2 Exact reduction to the genus-one connected-Hurwitz gap

The accepted DYZ/M68/M74 marked-incidence bound is

```text
pi_Gamma(G_Gamma)>=zeta:=3/[Nm(m-1)].                (2.7)
```

Let `U` be the unique genus-one component.  If it has `d` labels, it has
`2d` factors.  Define

```text
gamma_1(d)=gap(P_H^(d,2d)),                          (2.8)
```

where this is the half-lazy signed-Hurwitz chain on connected identity words
on the fixed labeled support.

The accepted component factorization is the exact bijection

```text
Gamma=I_(k_U,k_V) x X_U x X_V,                      (2.8a)
```

where `I_(k_U,k_V)` is the color-interleaving fiber.  Uniform measure is the
product uniform law.  Project by

```text
psi(sigma,u,v)=(sigma,u),
barGamma=I_(k_U,k_V) x X_U.
```

Every projected state has exactly `|X_V|` preimages, hence
`pibar_Gamma=Unif(I_(k_U,k_V)) tensor Unif(X_U)`.

The strong lumping is pointwise.  Fix `z=(sigma,u)`, any `v in X_V`, and
`x=(sigma,u,v)`.  Put `r_i=|{j<=i:sigma_j=U}|`.  The projection of the
labeled oriented proposal at position `i` is

```text
barR_(i,epsilon)(sigma,u)=
  (sigma,R_(r_i)^epsilon u),  if sigma_i=sigma_(i+1)=U;
  (S_i sigma,u),              if sigma_i != sigma_(i+1);
  (sigma,u),                  if sigma_i=sigma_(i+1)=V. (2.8b)
```

The two mixed orientations agree because the component supports are
disjoint; a `V,V` move can change `v` but is a projected self-loop.  Thus for
every `z' in barGamma`,

```text
sum_(y:psi(y)=z') P_Gamma(x,y)
 = (1/2)1_{z'=z}
   +[1/(4(m-1))]sum_(i,epsilon)
       1_{z'=barR_(i,epsilon)z},                     (2.8c)
```

independently of the omitted `v`.  This defines `Pbar_Gamma`.  Finally,
M75's event is determined by the global color positions and the internal
`U` word, so for some `Gbar_Gamma subseteq barGamma`,

```text
G_Gamma=psi^(-1)(Gbar_Gamma),
pibar_Gamma(Gbar_Gamma)=pi_Gamma(G_Gamma)>=zeta.      (2.8d)
```

Compare this projected chain `Pbar_Gamma` to the equal mixture `P_*` of the
half-lazy adjacent color-interchange chain and the internal `U` chain.  The
accepted color gap is at least `2/m^3` (singleton color convention one), so
conditional variance gives

```text
gap(P_*) >=(1/2)min(2/m^3,gamma_1(d))
          >=gamma_1(d)/m^3.                           (2.9)
```

The exact inherited comparison is M05 Sections 2.3--2.5.  Its equation
(2.8) gives the fixed signed shuttle between consecutive internal `U`
occurrences at physical positions `a<b`, of length `2(b-a)-1<2m`.  Its
equations (2.12)--(2.14) recover the source from
`(a,b,epsilon,stage)` and bound internal congestion by `<m^6`; equations
(2.15)--(2.16) route color swaps directly and give total comparison
congestion `A<=m^6+1<=2m^6`.  The proof uses only `(sigma,u)`, so it applies
to the projected chain.  Consequently

```text
gap(Pbar_Gamma)>=gamma_1(d)/(2m^9)
                >=gamma_1(d)/m^10.                   (2.10)
```

No gap estimate for the genus-zero component is required.  Define

```text
t_Gamma=ceil[(m^10/gamma_1(d))
              {(m/2)log M+log(1/zeta)}].             (2.11)
```

The projected state space injects into `Gamma` after fixing one omitted
component word, so it has size at most `M^m`.  For its uniform law and its
half-lazy reversible walk,

```text
||Pbar_Gamma^t(z,.)-pibar_Gamma||_TV
 <=(1/2)sqrt(|barGamma|)exp[-gap(Pbar_Gamma)t].       (2.12)
```

Equations (2.10)--(2.12) make the distance at time `t_Gamma` at most
`zeta/2`.  By the exact multiplicity identity (2.8d), its stationary
projected mass is still (2.7).  Thus
exactly `t_Gamma` independent proposals of (2.1), with
holding symbols omitted, form a state-independent law with

```text
E ell=t_Gamma/2,
inf_x Pr(beta x in G_Gamma)>=zeta/2.                 (2.13)
```

M75's endpoint theorem gives the explicit arbitrary-subset bound

```text
sum_(x in S)K(x,(Gamma minus S) union (F_N minus A))
 >=|S|/[2Nm(m-1)(m-2)M^2 t_Gamma].                  (2.14)
```

Therefore the narrower unresolved proposition

```text
gamma_1(d)>=c d^(-C)   for every d>=2                (2.15)
```

would make (2.11) polynomial and prove the arbitrary two-component signed
cover.  This report does not prove (2.15).  The older uniform connected-
Hurwitz gap for all genera and lengths implies (2.15), but is strictly
stronger than needed.  The marked-hitting proposition in Section 2.1 is
narrower still and could survive a slow unrelated genus-one mode.

### 2.3 What the torus certificate proves—and does not prove

The chronological ribbon surface of a connected genus-one identity word on
`d` labels with `2d` factors is a cellular torus with

```text
V=d, E=2d, F=d.
```

Choose a primal spanning tree `T`.  The complementary dual graph is
connected: otherwise the cellular boundary of a nonempty face set would be a
nonempty even subgraph inside the tree.  Choose a dual spanning tree `T*`
there.  Exactly

```text
2d-(d-1)-(d-1)=2                                    (2.16)
```

edge occurrences remain.  Contracting `T` and merging faces along `T*`
produces a one-vertex, one-face, two-edge torus cellulation.  Cellular
homology makes the two loop edges an integral `H_1` basis.  Before
contraction they are the two leftover edges closed along their unique
`T`-paths, hence two embedded nonseparating fundamental cycles.

This is not yet a connected-deletable square.  Literal braid surgery must
transport a full fundamental path into the annular core of an equal pair.
The exact owned `S_4`, length-eight audit found two actual chronological tori
with the same ascending-Kruskal tree positions `(0,3,5)`, cotree positions
`(1,4,6)`, leftover positions `(2,7)`, and leftover labels `(01),(13)`, but
the tree path closing `(13)` is `(0,3,5)` in one and `(0,5)` in the other.
Thus those position sets and two leftover labels do not determine the
tree-path transcript.  This exact collision refutes only that proposed
metadata sufficiency; a fixed braid might still work on both for another
reason.

### 2.4 An exponential unmarked family and transcript entropy

For each labeled tree `T` on `[d]`, `d>=3`, choose a deterministic pair of
incident edges `a_T,b_T`, and put

```text
u_T=(a_Tb_T)^3 product_(e in T minus {a_T,b_T}) e^2,   (2.17)
```

with the remaining edges in lexicographic order.  The product `a_Tb_T` is a
three-cycle, so its cube is identity.  Equation (2.17) is therefore a
connected identity word of length `2d`, genus one, and support exactly `T`.
It is unmarked: its alternating prefix has no square, and deleting any tail
square removes a bridge of `T`.

Append a doubled edge on two new labels.  All resulting states lie in the
same two-component macro

```text
Gamma_d: N=d+2, m=2d+2=2N-2,
          labeled component weights (2d,2).           (2.18)
```

Distinct trees have distinct supports.  The elementary Pruefer
correspondence gives an unmarked subset `U_d` with

```text
|U_d|=d^(d-2).                                       (2.19)
```

Now fix one labeled canonical marked word `c in Gamma_d` and choose an
adaptive signed-Hurwitz normalizer transcript `beta_x` with `beta_xx=c` for
each `x in U_d`, if such transcripts are supplied.  If the same induced
bijection occurred for `x` and `y`, it
would send both to `c`, contradicting injectivity unless `x=y`.  Hence the
normalizer has at least `d^(d-2)` distinct positional transcripts.  The
project's claim that every such route exists with polynomial length remains
conditional on the unverified Classification-H/transitivity source; that
claim is not needed for the transcript lower bound.

This is the exact audit requested after M86: any arbitrary adaptive
normalization to one fixed labeled target cannot be represented by
polynomially many fixed transcripts.  M86 is not contradicted:
its one fixed transcript sends relabeled sources to correspondingly relabeled
targets, rather than coalescing them at one state.

If one stores one exact-canonical transcript per `y in U_d` and samples it
uniformly, then from every `x in U_d` the exact canonical-root hit is

```text
Pr(beta_yx=c)=1/|U_d|=d^(-(d-2)).                   (2.20)
```

Indeed `beta_yx=c=beta_yy` iff `x=y`.  Wrong transcripts could land in other
members of the larger marked set.  Thus (2.20) refutes canonical-root replay,
not every possible marked-set law.

### 2.5 Random arborescences need exponentially distributed roots

Suppose a direct routing sends at least `eta` successful demand from every
source of a macro through within-macro paths to `q` marked roots and then
through at most `b` designated terminal edges per root.  Apply it to
`S=Gamma`.  No Hurwitz prefix leaves `S`; all successful demand is terminal.
Some actual terminal edge has occupation at least

```text
eta|Gamma|/(bq).                                     (2.21)
```

For M75's deterministic terminal rule `b=1`.  Even allowing every adjacent
mark and cross-square choice gives `b<=(m-1)M`.  Equations (2.19)--(2.21)
show that an inverse-polynomial-success, polynomial-root arborescence has
superpolynomial actual-edge occupation.  Its fixed-root endpoint map also
coalesces sources and is not bijective, so M75's inverse-prefix proof is
unavailable.

The natural uniform global-tree guess-and-abort law fails even before this
occupation issue.  Guess one of the `d^(d-2)` labeled Cayley trees
independently, run a tree-supported normalizer only when the guessed tree is
contained in the source support, and otherwise do nothing.  The unmarked
source `u_T` has support exactly the unique tree `T`.  Every wrong guess
leaves it unmarked, so its literal marked-hit probability is at most

```text
d^(-(d-2)).                                          (2.22)
```

Conditioning the tree choice on the source repairs (2.22) by violating the
required state-independent word law; the adaptive map is also not
automatically bijective.  This rigorously refutes that natural universal
tree law.  It does not refute a reversible arborescence whose roots are
distributed across exponentially many marked states.  The random-walk laws
of Sections 2.1--2.2 are precisely such distributed-endpoint candidates.

## 3. Probability, runtime, path, and congestion accounting

| item | exact value or bound | status |
|---|---:|---|
| physical Hurwitz holding probability | `1/2` | definition |
| each labeled signed proposal | `1/[4(m-1)]` | definition |
| random-time word expected length | `T/4` | proved |
| random-time endpoint hit | `>=a/(T+1)` | proved |
| specified padded-H3 path/terminal edge | `p_H=1/[6(m-2)M^2]` | inherited M75 |
| hitting-to-coarea bound | `p_H a|S|/[(T+1)max(T/4,1)]` | proved |
| whole-macro marked density | `zeta=3/[Nm(m-1)]` | inherited M68/M74 |
| projected physical Hurwitz gap | `>=gamma_1(d)/(2m^9)>=gamma_1(d)/m^10` | proved projection plus M05 paths |
| gap-based word length | equation (2.11) | proved reduction |
| gap-based expected length | `t_Gamma/2` | proved reduction |
| gap-based marked hit | `>=zeta/2` | proved reduction |
| gap-based coarea | equation (2.14) | conditional on `gamma_1(d)` size |
| unmarked sources in `Gamma_d` | `d^(d-2)` | proved |
| exact canonical transcripts | `>=d^(d-2)` | proved |
| polynomial-root terminal occupation | `>=eta|Gamma|/(bq)` | proved |
| global-tree guess hit on `u_T` | `<=d^(-(d-2))` | proved/refuted law |

Sampling either random-walk word takes time linear in its proposal horizon.
The gap-based law is polynomial in `N,m` under the inverse-polynomial
genus-one connected-Hurwitz gap (2.15).  Every successful fixed-word path
retains
literal inverse-prefix source recovery.  No canonical hub is used in the
positive reductions.  The tree/arborescence lower bounds are exponential in
`d=N-2`, hence superpolynomial in the declared parameters `N,m`.

## 4. Dependencies and claim status

| input or claim | status here | dependence/evidence |
|---|---|---|
| M75 randomized endpoint first-crossing theorem and `p_H` | inherited accepted M75/M77 | exact actual-edge charging |
| marked density `zeta` and safe terminal refresh | inherited accepted M68/M74 and M75/M77 | DYZ incidence and prefix join tree |
| Classification H/transitivity | conditional pending source/convention audit | not used in either positive reduction; positive hitting or `gamma_1(d)` supplies reachability |
| projected shuttle comparison (2.10) | proved here from inherited M05 paths | omitted component becomes self-loops |
| genus-one connected-Hurwitz gap (2.15) | unresolved narrow dependency | not promoted |
| uniform all-genus connected-Hurwitz gap | unresolved older proposition | sufficient but not needed here |
| random-time hitting-to-cover theorem | proved here | visit-count identity and M75 |
| fixed-time mixing-to-cover theorem | proved here, polynomiality conditional | spectral TV bound and M05 |
| tree--cotree two-edge homology basis | proved here | elementary cellular argument |
| constant leftover metadata determines surgery | refuted in the tested form | exact `S_4,m=8` collision |
| Cayley-tree unmarked family | proved here | order-three relation and tree bridges |
| canonical transcript entropy | proved here | bijectivity |
| polynomial-root arborescence occupation | proved here | terminal-demand pigeonhole |
| uniform global-tree guess-and-abort law | refuted | equation (2.22) |
| arbitrary-macro unconditional cover/direct flow | unresolved | exact first open step below |
| full-`K` gap/mixing or Terminal | unresolved | not claimed |

No new literature theorem is invoked.  The tree count uses the elementary
Pruefer bijection; the torus tree--cotree argument is proved directly.
Classification H remains a conditional project dependency.  It is relevant
only if one additionally asserts existence and polynomial length of every
adaptive canonicalizer transcript, not to the hitting transfer, strong-lump
gap reduction, or transcript-count implication proved here.

## 5. First unproved standalone step

The narrowest surviving positive statement is:

> **UNIFORM TWO-COMPONENT MARKED HITTING.**  There is a polynomial `H(N,m)`
> such that for every `N>=5,m=2N-2`, every two-component minimal exterior
> macro `Gamma`, and the precise lazy physical signed-Hurwitz walk (2.1),
>
> ```text
> max_(x in Gamma) E_x tau_(G_Gamma)<=H(N,m).
> ```

Theorem (2.4)--(2.6) would then give the desired arbitrary-partial-macro
coarea bound.  This is more targeted than the genus-one connected-Hurwitz
gap (2.15), which is one sufficient route through the strong projection and
shuttle comparison (2.8)--(2.14).  That genus-one gap is itself strictly
narrower than the old all-genus, all-length connected-Hurwitz proposition.

An alternative standalone step is a **distributed-root reversible surgery**:
construct a state-independent law of fixed signed words whose successful
endpoints range over exponentially many actual marked roots and whose
inverse-prefix occupation is polynomial.  Polynomial-root arborescences and
adaptive collapse to one canonical normal form are now rigorously excluded.

## 6. Strongest self-attack

1. The random-time theorem does not prove a hitting bound; it only converts
   one into the required word law and coarea estimate.
2. The gap-based law is not unconditional.  Calling (2.11) polynomial without
   proving (2.15) would silently assume the new genus-one restricted-fiber
   gap obligation.
3. The marked-hitting statement may still be as difficult as a significant
   part of the connected-Hurwitz gap.  “Strictly weaker” is logical scope,
   not evidence that it is easy.
4. The tree--cotree certificate identifies nonseparating cycles, not equal
   transposition occurrences.  No braid surgery theorem is inferred from
   homology alone.
5. The exact metadata collision refutes only one proposed encoding.  A fixed
   word can react algebraically to different factor labels without explicitly
   storing the tree path.
6. Exponential adaptive canonical transcripts do not refute an oblivious
   marked cover with heavy overlap.  Wrong canonical transcripts might hit
   other marked states; this is why (2.20) is scoped to the exact root `c`.
7. The terminal occupation lemma rules out few actual roots, not few word
   indices.  M86 correctly uses polynomial word metadata while its endpoints
   vary injectively across a large symmetry class.
8. A random spanning arborescence with exponentially diffuse roots is not
   ruled out.  Its analysis has been reduced to the same worst-row
   hitting/flow issue, not declared impossible.
9. All transport capacities use signed Hurwitz as padded `H3`.  One `H4/H5`
   update may bypass these paths; no distance or obstruction for the full
   heat bath follows.

## 7. Boundary cases and exact falsification checks

- Odd `m`, `m=0`, `m=2`, and `N=2` do not instantiate the two-component
  minimal genus-one exterior geometry.  The theorem is scoped to
  `N>=5,m=2N-2`.
- The explicit family begins at `d=3`, hence exactly at ambient `N=5,m=8`.
  Both components are nontrivial, with weights `(2d,2)`.
- The owned exact script verifies the path specialization of (2.17) through
  `d=12`; those checks are not the universal proof.
- It exhausts all labeled Cayley trees for `d=3,4,5,6`, respectively
  `3,16,125,1296` trees, with zero identity, length, support, or markedness
  failures.  The all-`d` statement uses the displayed algebra and bridge
  proof plus the Pruefer bijection.
- It independently enumerates connected genus-one `S_4` identity words at
  length eight until the exact tree--cotree metadata collision.  The witness
  appears after 1,589 candidate words, 150 identity words, and 75 connected
  genus-one words.  Both surfaces have exactly four chronological faces.
- The collision is finite falsification of a universal metadata claim; it is
  not evidence for or against asymptotic hitting, conductance, or mixing.
- M84's zero row for canonical positive elimination is untouched.  The laws
  in Section 2 use signed positive/inverse proposals and would require the
  unresolved quantitative hitting/gap input.

## 8. Artifacts, reproduction, and cache hygiene

Owned artifacts are:

```text
plan.md
checkpoint.md
oblivious_cover_reduction.md
tree_cotree_metadata_audit.py
tree-cotree-metadata-results.json
report.md
freeze_manifest.md
SHA256SUMS
```

Exact command from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M92-arbitrary-macro-signed-cover/tree_cotree_metadata_audit.py \
  --collision-n 4 --path-d-max 12 --all-tree-d-max 6 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M92-arbitrary-macro-signed-cover/tree-cotree-metadata-results.json
```

Python was `3.12.3`; seed `null`; nonstandard dependencies `{}`; the run is
deterministic.  The JSON records its command, commit, convention, elapsed
time, tested claim, and finite-scope warning.  Predecessor hashes and final
owned hashes are in `freeze_manifest.md` and `SHA256SUMS`.  Bytecode was
disabled and the owned directory contains no `__pycache__` or `.pyc` file.
No predecessor, shared durable file, manuscript section, skill, or other
worker directory was edited.

## 9. Verdict

```text
PROVED, SCOPED:
  worst-source marked hitting for the declared physical Hurwitz walk
  transfers to a state-independent bijective signed-word law and exact
  arbitrary-subset coarea;
  the genus-one connected-Hurwitz gap would supply this cover quantitatively
  after strongly projecting out the genus-zero internal word;
  torus tree--cotree leaves a two-cycle homology certificate;
  arbitrary exact canonicalization has exponential transcript entropy;
  polynomial-root arborescences have exponential terminal occupation.

REFUTED, SCOPED:
  uniform global-tree guess-and-abort as a universal marked-cover law;
  polynomial-root canonical/arborescence routing as a polynomial-occupation
  direct-coarea proof;
  leftover positions/labels as sufficient tree-path surgery metadata.

UNRESOLVED:
  uniform two-component marked hitting;
  an unconditional arbitrary-macro signed cover or direct partial-macro flow;
  unrestricted H4/H5 behavior, full-K gap/mixing, and Terminal A/B.
```

The exterior frontier is therefore no longer “find any oblivious
normalizer.”  It is a precise distributed-root hitting/flow problem.  A
fixed or polynomial family of canonical roots is impossible, while the
declared Hurwitz random walk supplies the correct bijective law as soon as
the narrower marked-hitting bound—or the stronger genus-one connected-
Hurwitz gap—is proved.  No all-genus gap is needed for this reduction.
