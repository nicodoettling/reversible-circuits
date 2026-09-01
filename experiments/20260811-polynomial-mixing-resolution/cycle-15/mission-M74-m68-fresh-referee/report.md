# M74 fresh referee report on frozen M68

Date: 2026-08-12.  Repository commit recorded by the source and reproduced by
the reruns: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, and frozen source audited

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are evaluated
left-to-right.  The source works at

```text
N>=5,  m=2N-2,  M=binom(N,2),
K=(1/2)I+(1/6) sum_(r=3)^5
       (1/(m-r+1)) sum_i H_(i,r),
```

with uniform target on `Omega(N,m)`.  Its exterior balls `E_k` and cuts
`C_k=A union E_k` use the accepted M64 definitions, where

```text
A={x in F_N(T_N):Core(x) in B} subset F_N(T_N)
```

for one fixed labeled path prefix-join tree `T_N` and a fixed nonempty proper
core cell `B`.

The frozen M68 report has the requested SHA-256

```text
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  report.md
```

and all sixteen supporting hashes displayed in its field 8 match.  M68 proves
a whole-exterior-macro average action theorem, a conditional fixed-word cover
theorem, a dense/partial macro dichotomy, and several exactly scoped route
obstructions.  It expressly leaves the one-radius partial-macrofiber step
open and claims neither Terminal A nor Terminal B.

There is one required append-only wording correction, proved in Section 2.3
below.  In M68 (2.14), “target support tree” must be replaced by “target
prefix join tree `T_J`.”  The frozen report is not mutated.  The corrected
argument proves the same `N-2` safe-target count with unchanged constants.

## 2. Full independent proof audit

### 2.1 DYZ normalization and marked-square incidence

Let `C_g(d)` count connected exact-support identity transposition words on a
fixed labeled `d`-set at length

```text
k=2(d-1)+2g,  d>=2,  g>=1,
a_(g,d)=C_g(d)/k!.
```

Dubrovin--Yang--Zagier, Proposition 1, equation (13), writes their normalized
Hurwitz number `h_(g,d)` as a positive sum over ordered splits
`d=d_1+d_2`.  With `j=ell-1`, each summand is, up to a positive constant
independent of `g`, a convolution of the two lower-degree genus sequences and

```text
b_j=d_1^(2j+3)d_2^2/(2j+2)!.
```

The consecutive ratio of this last sequence is at most `d_1^2/12`.  The
elementary convolution-ratio lemma and induction on `d` therefore give

```text
a_(g,d)/a_(g-1,d)<=d^3/12,
```

because

```text
d_1^3+d_2^3+d_1^2 <= (d_1+d_2)^3.
```

The normalization is exact.  DYZ divide the cover count by `k!`; the fixed
labeled-sheet transitive factorization count is `d!` times their cover count.
Thus `a_(g,d)=d! h_(g,d)`, and the degree-dependent factor cancels from every
adjacent-genus ratio.  The exact calibrations
`C_0(2)=1,C_0(3)=24,C_0(4)=2880` agree.  At the delicate endpoint `d=2`,
`C_g(2)=1` for every `g`, so the normalized ratio is
`1/[k(k-1)]<=2/3=d^3/12`; the first case is exactly `1/12`.

Insertion and deletion are a bijection between a marked deletable adjacent
square and

```text
(z,p,e): z counted by C_(g-1)(d),
         p one of k-1 insertion gaps,
         e one of binom(d,2) transpositions.
```

Consequently

```text
E[Z_int]
 =(k-1)binom(d,2)C_(g-1)(d)/C_g(d)
 >=12binom(d,2)/(d^3k)
 =6(d-1)/(d^2k).
```

No factorial, edge-choice, or marked-position multiplicity is missing, and
the derivation is uniform for all `d>=2,g>=1`.

### 2.2 Color interleaving and the global mark probability

Conditioned on a labeled weighted support-component macro, component words
are independently uniform and their color sequence is a uniform interleaving.
For any fixed consecutive pair among the `k` occurrences of one color, the
number of interleavings in which it is also globally consecutive is
`binom(m-1,k-1)`, out of `binom(m,k)`.  Hence the exact probability is

```text
binom(m-1,k-1)/binom(m,k)=k/m.
```

Linearity, without an independence assumption, gives

```text
E_Gamma Z>=6(d-1)/(d^2m).
```

Since `Z<=m-1` and `(d-1)/d^2>=1/(2N)` for `2<=d<=N`,

```text
Pr_Gamma(Z>=1)>=3/[Nm(m-1)].
```

This is correctly an average over a whole macro, not a pointwise assertion.

### 2.3 Exact padded `H3` action and the required join-tree correction

For a fixed transposition `a`, the number of length-three transposition words
with product `a` is

```text
D_N=M+3*2(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.
```

The three terms correspond respectively to the last factor being `a`,
sharing one endpoint with `a`, or being disjoint from `a`; the intervening
two-factor products have respectively `M`, `3`, and `2` factorizations.

A globally adjacent marked square can always be padded on the right, except
at the final pair where it is padded on the left.  The specified replacement

```text
(e,e,a)->(s,s,a),  or  (a,e,e)->(a,s,s)
```

therefore has exact literal-chain probability

```text
1/[6(m-2)D_N].
```

Multiplication by the marked-state probability proves exactly

```text
theta_N=1/[2Nm(m-1)(m-2)D_N].
```

Deleting the marked pair leaves its positive-genus component `U` connected;
adding a cross edge `s` twice merges it with one other component `V`.  The
new genus is `g_U+g_V-1>=0`.  Thus for `c>=3` this is a `c->c-1` exterior
move with average probability at least `theta_N`.

For `c=2`, the two genera sum to one.  After deletion, both component words
are minimal.  Let their prefix join trees be `J_U,J_V`.  Interleaving factors
on disjoint label sets preserves each internal join/cut status: factors in
the other component fix every cycle on the current component.  Immediately
before the inserted square the endpoints of the first `s` lie in different
prefix-permutation cycles, so the first `s` is a join; the second `s` restores
the preceding prefix permutation and is a cut.  All later join/cut statuses
are unchanged.  Therefore the target has

```text
T_J(target)=J_U union J_V union {s}.                 (2.1)
```

This is the exact correction to M68's phrase “target support tree.”  A
minimal word's full support graph need not itself be a tree, and the frozen
sentence that a tree has at most one edge across an arbitrary bipartition is
not literally true.  What is true and sufficient is sharper: with
`J_U,J_V` fixed, at most one cross edge `s` can make the union (2.1) equal
the one fixed tree `T_N` (if equality is possible, `s` is the unique edge of
`T_N minus (J_U union J_V)`).  Since

```text
A subset F_N(T_N),
```

every other `s` lands in `F_N minus A`.  There are
`|U|(N-|U|)>=N-1` cross edges, hence at least `N-2` safe choices.  Summing
their distinct heat-bath outcomes proves the corrected bound

```text
E_Gamma K(x,F_N minus A)>=(N-2)theta_N.
```

The correction changes no probability, path, or exponent.

### 2.4 Fixed-word translate-cover theorem

Assume fixed, state-independent Hurwitz words `beta_1,...,beta_L`, each of
length at most `D>=1`, cover a two-component macro by inverse translates of
its globally adjacent, connected-deletion square set.  Assign every source
`x in S` to the least covering word and follow its prefixes.

Every prefix is a bijection of the macro.  If a prefix first exits `S`, charge
that directed within-macro boundary edge.  Otherwise the final state is
marked, and the corrected Section 2.3 argument supplies a deterministic safe
square refresh into `F_N minus A`, hence outside `S`.

One right or inverse Hurwitz move is a specified padded `H3` outcome.  A
length-three conditional fiber has at most `M^2` words because its first two
transpositions determine the third.  Thus every path edge has

```text
p_H=1/[6(m-2)M^2]
```

as a lower bound.  For fixed word index `j` and prefix time `t`, the charged
edge's source state and inverse prefix recover at most one original source.
There are at most `LD` such pairs.  For a final refresh edge, its directed
source and `j` likewise recover at most one original source, giving load at
most `L<=LD`.  Therefore every `S subseteq Gamma` satisfies

```text
sum_(x in S)K(x,Omega minus S)
 >=p_H|S|/(LD)
 =|S|/[6(m-2)M^2LD].
```

The boundary may be restricted to the within-macro boundary and
`F_N minus A`.  Direction, source recovery, and constants are all correct.
The polynomial cover hypothesis itself remains unproved.

### 2.5 Dense/partial macros and the exact limit of the conclusion

For `S=E_k`, let `u_Gamma=1-|S intersect Gamma|/|Gamma|`, and let
`q(x)<=1` be the favorable probability whose whole-macro mean is at least
`theta_Gamma`.  Removing uniform macro mass `u_Gamma` can remove at most
`u_Gamma` from that mean, so

```text
(1/|Gamma|)sum_(x in S intersect Gamma)q(x)
 >=theta_Gamma-u_Gamma.
```

Thus a macro with `u_Gamma<=theta_Gamma/2` retains half its whole-macro
action.  For two components this action enters `F_N minus A` and is literal
boundary flow.  For a sparse partial macro, the accepted within-macro
Hurwitz diameter only implies

```text
Gamma intersect E_k nonempty => Gamma subset E_(k+H_N),
H_N=50Nm^3,
```

and hence the report's `H_N`-window volume-growth inequality.  It supplies
no bound at the particular one-step shell `L_k->L_(k+1)`.  M68 states this
limitation explicitly.  Its dense `c>=3` absorption relation also uses only
stationary inflow into the lower component layer and is correct; iterating it
multiplicatively would be superpolynomial and is not claimed.

### 2.6 Exact scope of every obstruction

1. **Partial initial macros.**  The independent `N=5,m=8` rerun reproduces
   90 exterior macros: 2 full, 47 partial, and 41 absent from `E_0`, with
   component-count occupancies `308409/739200`, `6362/23730`, and `0/10`.
   This refutes macro saturation only.
2. **Zero direct exit.**  The full `H3/H4/H5` rerun reproduces 90
   three-component and all 10 four-component states with
   `K(x,F_5 minus A)=0`.  For the infinite repeated-edge word
   `e^(2N-2)`, one update has support on at most twelve labels, proving zero
   direct full-support exit for `N>=13`.  A connected target uses at least
   `N-1` distinct support edges and can contain `e` in at most `N` positions,
   giving Hamming distance at least `N-2` and the stated layer-radius lower
   bound.  No stationary-mass or boundary upper bound follows.
3. **Direct two-deletion.**  From `P x U y S`, deletion preserves the
   identity exactly when `x=UyU^-1`; right-bubbling `x` then changes it to
   `U^-1xU=y`, exposing a square.  The rerun reproduces exactly 240 failures,
   all in two-component macros.  For the first word, only pairs `(0,4)` and
   `(2,6)` preserve identity, and both remaining support graphs disconnect.
4. **One-level four-null strand.**  The rerun reproduces 657,610 distinct
   genus-one component words and 37,200 failures.  This refutes the stated
   one-level disjunction, not recursive strand methods.
5. **Bounded square exposure.**  For
   `w_q=R_qR_qR_(q-1)R_(q-1)`, every initially relevant window contains
   distinct disjoint factors.  Its product has transposition length equal to
   the window length; hence every same-length factorization is reduced and
   consists of those same disjoint transpositions in some order.  Until equal
   factors become local, updates only permute such windows and move an
   occurrence by at most four positions.  Starting minimum separation
   `q-1` therefore gives distance at least `ceil((q-2)/4)` to adjacency.
   This is linear distance with no mass estimate, not slow mixing.
6. **Colors-only handle.**  The exact two-generator rerun starts from a
   connected genus-one identity word with connected minimal deletion core
   and reaches adjacent unequal marked factors.  Full product remains
   identity while marked deletion is a nonidentity 3-cycle.  It refutes only
   the two-color cancelability invariant.
7. **Unreduced arc fiber.**  In the displayed `S_4` word, the marked `a` and
   neighboring disjoint `b` commute, so the pure braid `sigma_2^2` fixes the
   entire factor tuple and returns the colors.  It is a Dehn twist about the
   two punctures; its powers give distinct winding/intersection numbers for
   the connecting arc.  Thus the literal full-arc lift has infinite fibers.
   This does not rule out a finite framing quotient, which M68 leaves open.
8. **Terminal coalescence.**  The inherited exponential ratio
   `|F_N^c|/|F_N|` and pigeonhole principle prove superpolynomial collision
   for deterministic coalescence into `F_N` with only polynomial terminal
   metadata.  A first-boundary randomized flow can stop earlier and is not
   refuted.
9. **Direct-certificate law.**  Uniform certificate projection has exact
   density `r(w)/E r`; the DYZ lower mean and `r(w)<=k-1` give the stated
   upper bound `dk^2/3`.  The exact zero-certificate words prevent a positive
   lower density.  This is a reservoir estimate, not a finite equivariant
   cover.

Every negative conclusion is therefore exact only at its named scope.  None
is a conductance upper bound for the literal chain.

## 3. Probability, runtime, path, density, and congestion accounting

- Whole-macro marked probability is at least `3/[Nm(m-1)]`.
- One specified favorable square refresh has exact probability
  `1/[6(m-2)D_N]`, including laziness, block-size scan, window scan, and
  conditional output.
- Whole-macro downward action is `theta_N`; the corrected two-component safe
  action is at least `(N-2)theta_N`.
- A padded Hurwitz edge has probability at least
  `1/[6(m-2)M^2]`.
- Under the fixed-cover hypothesis, path length is at most `D`, recovery load
  is at most `LD`, and subset boundary is at least
  `|S|/[6(m-2)M^2LD]`.
- `H_N=50Nm^3` is used only for multiradius volume growth, never as a
  congestion or conductance bound.
- The certificate projection has zero possible lower density and upper
  density `dk^2/3`.
- Exact block enumeration is polynomial because `r<=5`; no rerun is offered
  as a sampler or as asymptotic evidence.

The six M68 reruns took approximately 0, 8.46, 16.50, 15.69, 18.00, and
58.67 seconds.  The DYZ normalization rerun took seconds.  All are
deterministic, use Python 3.12.3, seed `null`, and no nonstandard dependency.

## 4. Dependencies and status

1. **PROVED IN M68 AND CHECKED HERE:** marked incidence and interleaving,
   favorable macro action with the Section 2.3 correction, dense/partial
   inequalities, fixed-cover implication, direct-certificate density, and
   the exactly scoped analytic obstructions.
2. **PRIMARY SOURCE CHECKED:** Dubrovin--Yang--Zagier, *Classical Hurwitz
   numbers and related combinatorics*, Proposition 1, equation (13), including
   the `h_(g,d)=H_(g,d)/k!` normalization and positive recurrence.
3. **INHERITED ACCEPTED:** M60--M64 definitions and boundary results;
   labeled weighted-component factorization; quantitative Classification H
   and diameter `50Nm^3`; minimal connected counts; exact heat-bath
   reversibility; and the M13 minimal-macro mass bound.
4. **STANDARD TOPOLOGICAL FACT:** the pure braid square is the two-puncture
   Dehn twist and has distinct powers on an arc crossing its curve.
5. **EXACT FINITE:** all six rerun results in Section 2.6.  They can falsify
   the named universal shortcuts but cannot prove asymptotic expansion.
6. **UNRESOLVED:** a polynomial fixed-word/finite-framing cover or equivalent
   one-radius first-boundary flow for arbitrary partial exterior macrofibers.

## 5. First unproved standalone step

> **ONE-RADIUS PARTIAL-MACRO MARKED-COVER / COAREA.**  Uniformly for
> `N>=5` and every intermediate exterior radius, construct polynomial-length
> literal local paths carrying the cut's smaller-side demand to their first
> boundary edge with polynomial directed-edge load.  Equivalently, supply a
> polynomial family of bijective marked covers inside partial macrofibers or
> a one-radius coarea inequality.  Component-merger histories must be charged
> additively and stopped at first crossing, rather than erased at a minimal
> global hub.

The fixed-word theorem proves this implication wherever its cover hypothesis
holds.  M68 neither assumes nor proves the universal cover.

## 6. Strongest self-attack

The universal positive estimate is only a whole-macro average.  An exterior
ball can preferentially contain zero- or low-certificate states.  Once its
missing macro fraction exceeds `theta_N`, the dense estimate is vacuous, and
the diameter supplies only growth across `H_N` radii.  Therefore the new
estimates do not control the exact one-radius term in M64's boundary identity.

The fixed-word theorem is conditional; its most direct two-deletion cover is
false.  The infinite-arc proof concerns the unreduced lift only and leaves a
finite handle-framing quotient open.  The terminal-collision argument concerns
global deterministic coalescence only.  Finally, the append-only correction
in Section 2.3 is essential: reading “support tree” literally would be false,
but the prefix-join-tree proof repairs the sentence locally without altering
the theorem or constants.

## 7. Calibration and exceptional cases

- The theorem is intentionally restricted to `N>=5,m=2N-2>=8`; both padding
  orientations and all of `H3,H4,H5` are present.
- The DYZ incidence argument includes `d=2` and all `g>=1`; an isolated
  second component in the `c=2` case is harmless, with empty join tree.
- For `c=2`, the corrected proof uses only `A subset F_N(T_N)`; its extra
  core-cell restriction can make more targets safe and never fewer.
- At `N=5,m=8`, all 762,940 exterior states and all 90 exterior macros are
  covered by the deterministic reruns.  The positive one-step square
  domination at this size is a finite fact only.
- Odd `m`, `m=0`, `m=2`, `N=2`, and the small `S_3/S_4` identity calibrations
  are outside this minimal exterior construction and are not changed.
- All analytic lower bounds retain `H4/H5` as nonnegative chain terms; the
  exact finite pointwise audit includes them literally.

## 8. Artifacts, hashes, and reproduction

Artifacts are under

```text
experiments/20260811-polynomial-mixing-resolution/cycle-15/
  mission-M74-m68-fresh-referee/
```

Hashes before adding this report are:

```text
df277fd6cbabd2771fb7c6c784058427289dddca59a0479874a567723c551a71  plan.md
6c9b6f5f0c4cde2b0ce9ca5d8db79118b44b7a92915d9f58589c29e910ab91c2  checkpoint.md
17f25a70090c9514e389e7e57d790e0c6a59fc0cfeb7b8ba199b480eda5f4014  colored-handle-rerun.json
99a36f8051c8c049b7bb0cebbb245ad12e4d5dea3d35ea0dce9a83215e878750  dyz-ratio-rerun.json
e702a3254ce05e3aba902dc1fd8578327065a45d9d350fb7730cc867692cf15b  four-null-rerun.json
60fc03cbbebde24384994f4148e42dc7975907795db3ff207e651ae4a210e175  macro-saturation-rerun.json
eaed8ab871875aec3837e8f96224ff5b5d9e223cadeef8014ad8e755ee14a78c  pointwise-exit-rerun.json
d87967a898a25fb20d6db2bc62ecaf9e00a732c575064ca9dae9a8763a2ff702  square-domination-rerun.json
5a27c7f8929aa821df5b9a5720574d9b9dabbfbbe433270c3a581c4b933e3c3b  two-deletion-rerun.json
```

Commands from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/colored_handle_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/colored-handle-rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_macro_saturation_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/macro-saturation-rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_pointwise_exit_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/pointwise-exit-rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_square_domination_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/square-domination-rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_two_deletion_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/two-deletion-rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/exact_n5_four_null_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/four-null-rerun.json
```

For `dyz-ratio-rerun.json`, run `hurwitz_ratio_test.py --n-max 12 --m-max 80`
from `cycle-02/mission-M12-intermediate-density/`, with the M74 output path.
After removing only `argv` and `elapsed_seconds`, all mathematical fields of
the six M68 reruns match their frozen JSON counterparts exactly.  No `/tmp`
file is a proof or reproduction dependency.

## 9. Verdict and numbered objections

**ACCEPT.**

1. **Required nonmaterial correction:** in the proof of M68 (2.14), replace
   “target support tree” by “target prefix join tree `T_J`,” and replace the
   false general sentence about arbitrary tree bipartitions by the exact
   union proof in Section 2.3 above.  Because `A subset F_N(T_N)` and at most
   one `s` can complete the fixed internal join trees to `T_N`, the same
   `N-2` safe outcomes and every displayed constant remain valid.
2. No further objections.  With that append-only correction, all scoped M68
   claims survive the recurrence, interleaving, kernel-normalization,
   source-recovery, obstruction, and exact-finite audits.

This acceptance is nonterminal.  M68 proves neither a universal
inverse-polynomial gap nor reducibility/superpolynomial slowdown for the
literal chain, so it is neither Terminal A nor Terminal B.
