# M73 final report: cyclic product kernel, diameter-two influence frontier

Date: 2026-08-12.  Base repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, conventions, and scope

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  Fix odd `n=2l+1`, `l>=2`, endpoint

```text
h=(0 1 ... n-1),
Omega_n={(t_1,...,t_(n-1)): t_i transpositions, t_1...t_(n-1)=h},
```

and the uniform law on `Omega_n`, whose size is `n^(n-2)`.  Put
`G_i=t_(2i-1)t_(2i)` and
`theta(g)=h^(-1)gh`.  This mission studies only M16's one-pair product
correlation operator restricted to `theta`-invariant functions, and the
resulting input to M70's fixed-long-cycle `H_0` question.

The main result is a proved exact reduction, not a gap theorem.  The
stationary quotient kernel has explicit cyclic-composition weights and four
residual-forest row schemas.  A natural graph on source product orbits has
universal diameter at most two.  Consequently the entire positive
coordinate-correlation edge reduces to one local posterior-influence
inequality between source products sharing one raw transposition:

```text
max_(O~O') TV(bar K^2(O,.),bar K^2(O',.)) <= C/n^2.  (SF)
```

The diameter theorem is proved below; (SF) is the exact named open step.

This report does **not** prove a Poincare gap for the `H_0` quotient, the full
minimal fixed-endpoint bridge, the original identity-conditioned local
`{3,4,5}` chain, or Terminal A/B.

## 2. Full argument and construction

### 2.1 Exact invariant product kernel

For a permutation `q` of transposition length `r`, let

```text
F_r(q)=r! product_(cycles C of q, |C|>1)
                 |C|^(|C|-2)/(|C|-1)!,
```

and put `F_r(q)=0` at every other rank.  Let
`a(g)=#{(u,v):u,v transpositions, uv=g}`.  Fixing one or two pair products
in a minimal long-cycle factorization gives, exactly,

```text
pi(g)=a(g)F_(n-3)(g^-1h)/n^(n-2),
J(g,s)=a(g)a(s)F_(n-5)((gs)^-1h)/n^(n-2),
K(g,s)=a(s)F_(n-5)((gs)^-1h)/F_(n-3)(g^-1h).
```

The support `X` consists exactly of cyclically oriented three-cycles and
noncrossing double transpositions.  For cyclic orbits `O,O'`,

```text
bar pi(O)=|O|a(g)F_(n-3)(g^-1h)/n^(n-2),
bar K(O,O')=sum_(s in O')
  a(s)F_(n-5)((gs)^-1h)/F_(n-3)(g^-1h).
```

Every row normalizes exactly and `bar K` is self-adjoint in `L^2(bar pi)`.
No parking statistic is being treated as a strong lumping.

If `kappa` is a real invariant one-coordinate eigenvalue, the covariance
matrix of the `l` coordinate evaluations is

```text
(1-kappa)I_l+kappa 11*.
```

Positive semidefiniteness proves
`kappa>=-1/(l-1)`.  Thus M16's transverse Gram branch is at most
`1/(l-1)`; only the positive edge `kappa_+` is open.  M16's exact block
formula gives

```text
mu_l^(H0)<=max{[1+(l-1)kappa_+]/l,1/(l-1),1/l}.
```

Therefore `kappa_+=O(1/l)` would prove the required `O(1/l)` H0
coordinate-Gram estimate.  It is not itself asserted here to be a complete
proof of M70's quotient Poincare gap.

### 2.2 Exact gap compositions and four row schemas

Write `tau(d)=d^(d-1)/d!` and `T(z)=sum_(d>=1)tau(d)z^d`, so `T=ze^T`.
An oriented three-cycle is a cyclic positive composition `[x,y,z]` of `n`;
its complement cycle sizes are `(x,y,z)` and

```text
bar pi_3([x,y,z])
 =o_3[x,y,z] 3(n-3)!tau(x)tau(y)tau(z)/n^(n-2),
```

where the orbit size is `n`, except that the balanced triple has size `n/3`.
A double transposition is a colored cyclic four-composition.  For positive
`(x,y,z,w)`, the separated color `S` has complement sizes
`(x,z,y+w)`; the nested color `N` has sizes `(x+z,y,w)`.  Every double orbit
has size `n` for odd `n`, and

```text
bar pi_D=n 2(n-3)! product_(three complement sizes d)tau(d)/n^(n-2).
```

The generating-function identity

```text
[z^n]T^k=k n^(n-k-1)/(n-k)!,
[z^n]T^4/(1-T)=n^(n-4)/(n-4)!
```

proves total masses `3/n` and `(n-3)/n` for the two kinds.

For a source `g`, let the three residual cycles of `g^-1h` have sizes `d_i`
and ranks `r_i=d_i-1`; their total rank is `r=n-3`.  Let `nu_d` be the
first-edge law in a uniform minimal factorization of a `d`-cycle and `mu_d`
the first-pair-product law.  If deleting an edge makes sizes `u,d-u`,

```text
nu_d(e)=(d-2)!tau(u)tau(d-u)/d^(d-2).
```

If `p` is a local rank-two product,

```text
mu_d(p)=a(p)(d-3)! product_(cycles D of p^-1c_d)tau(|D|)/d^(d-2).
```

Uniform component-factorization interleaving gives the exact row identity

```text
K_g=sum_i r_i(r_i-1)/[r(r-1)] Emb_i(mu_(d_i))
   +sum_(i<j) 2r_i r_j/[r(r-1)]
                    Emb_(ij)(nu_(d_i) tensor nu_(d_j)).
```

Thus every row is the sum of only four schema classes: same-cycle oriented
three-cycle `I3`, same-cycle separated/nested double `IS,IN`, and
cross-cycle double `X`.  The square `bar K^2` is the signed sum of the
sixteen ordered schema pairs.  The absolute value must be taken after this
sum; separate triangle bounds erase the observed cancellation.

Summing the row over three-cycle targets gives the proved closed formula

```text
K_g(3)=3[n-9+2 sum_i 1/d_i]/[(n-3)(n-4)],
|K_g(3)-3/n|<=6/[n(n-4)].
```

The same bound holds after every positive number of `K` steps by sup-norm
contraction.  Coarse product kind is therefore already controlled at the
needed `n^-2` scale, but the within-kind distribution remains essential.

### 2.3 Conditioned-Borel identity and its exact limitation

Let `b_j=e^-j j^(j-1)/j!`, the critical Borel(1) law.  Orient an edge from
`nu_d` and let `U,d-U` be its cyclic gap sizes.  Then

```text
Pr(U=u)=Pr(B_1=u | B_1+B_2=d)
       =b_u b_(d-u)/sum_(v=1)^(d-1)b_v b_(d-v).
```

Hence every cross-cycle schema is a product of conditioned-Borel tree
splits followed by deterministic embedding.  However, if
`S_d=min(U,d-U)`, monotonicity of the Borel mass and the Borel--Tanner
convolution give the exact identity

```text
TV(Law(S_d),Law(B_1))=Pr(B_1>floor(d/2))
                     ~2/sqrt(pi d).
```

A small-tree/giant-side coupling of individual schemas is therefore too
lossy.  A successful proof must couple the complete two-step posterior or
retain the signed sixteen-schema cancellation.

### 2.4 Diameter-two reduction and Gibbs formulation

Let `Gamma_n` have the cyclic product orbits as vertices.  Join two vertices
when representatives admit ordered pair lifts sharing their first raw
transposition or sharing their second.

**Proved:** `diam(Gamma_n)<=2` for every odd `n>=5`.  Choose lifts `(a,b)`
and `(c,d)`.  Rotate the second lift.  The shorter chord `theta^r(d)` can be
placed strictly inside the larger arc cut by `a`, making
`a theta^r(d)` a noncrossing double transposition.  The only no-room case
has the two arcs and the shorter chord at their odd extremal lengths; make
the chords share an endpoint in cyclic order instead, yielding the
admissibly oriented three-cycle.  The intermediate lift
`(a,theta^r(d))` shares one coordinate with each endpoint lift.

Because `bar K` is self-adjoint, `bar K^2` is the two-block
Gibbs/data-augmentation kernel for the exact symmetric quotient joint law:
sample `S` conditional on `G`, then resample `G'` conditional on `S`.
Therefore it suffices to prove one local strong-data-processing inequality:

```text
max_(O~O') TV(bar K^2(O,.),bar K^2(O',.)) <= C/n^2.  (SF)
```

Diameter two would imply `delta(bar K^2)<=2C/n^2`, hence every nonconstant
invariant eigenvalue obeys `|kappa|<=sqrt(2C)/n=O(1/l)`.  This is the final
standalone obstruction.

The stronger uniform estimate

```text
sup_O chi^2(bar K^2(O,.) || bar pi)<=C/n^4
```

would also suffice, by Cauchy--Schwarz, but is likewise unproved.

## 3. Probability, runtime, path, and congestion accounting

- All probability kernels in Sections 2.1--2.4 are exact, nonlazy
  conditional laws.  The only projection is simultaneous endpoint-cycle
  conjugation, with literal stationary orbit masses `bar pi`.
- A source pair product has `a(g)=3` ordered lifts for a three-cycle and
  `a(g)=2` for a double transposition.  All completion factors and
  interleaving coefficients are displayed above.
- `Gamma_n` paths have length at most two, with no canonical hub.  If (SF)
  holds with constant `C`, its triangle loss is exactly at most two.
- The exact rank-two support sizes at `n=5,7,9` are `20,105,336`; quotient
  dimensions are `4,15,38`.
- Exact n=5 and n=7 schema verification checks `400` and `11025` row entries.
  Both complete in seconds on this host.
- The deterministic compressed-kernel scaling suite uses Python `3.12.3`,
  NumPy `1.26.4`, `seed=null`, and reaches `n=21`, dimension `634`, in about
  two minutes on this host.  Exact rational spectra are retained only through
  `n=9`; larger eigensystems and norm diagnostics are floating.
- Earlier Stanley quotient comparison paths have maximum shortest lengths
  `4,12` and lexicographic normalized loads `333/20,81887/168` at `n=5,7`.
  These are finite calibrations and no universal congestion claim is made.

## 4. Dependencies, labeled by status

- **Proved here:** exact raw and quotient product kernels; exact
  reversibility; covariance lower bound `kappa>=-1/(l-1)`; cyclic
  three/four-composition weights and normalization; four row schemas;
  collapsed kind bound; conditioned-Borel split and its TV loss; universal
  diameter-two source graph; exact finite rational certificates.
- **Proved input from M16:** normality and self-adjointness on cyclic
  frequency zero; the scalar coordinate-Gram block formula.  M73 uses only
  this scoped correlation machinery, not a global base-scale theorem.
- **Proved/frozen M70 context:** the zero-frequency quotient is exactly the
  uniform stationary-flow cyclic quotient; nonzero frequency sectors have a
  polynomial floor.  M73 does not import or claim an `H_0` gap.
- **Accepted M67 input used only for orientation:** the bad
  `Theta(l^-1/2)` additive correlation lives in nonzero cyclic frequency.
  No M67 asymptotic sum is used in an M73 proof.
- **Standard enumerative dependency:** minimal transposition factorization
  counts for disjoint cycles, obtained from Dénes plus independent cycle
  interleaving.  Every use is also checked exactly at `n=5,7`.
- **Primary-source algorithms audited only as routes:** Stanley,
  Moszkowski, Goulden--Yong/mind-body dual, Goulden--Pepper, and the
  Adin--Roichman maximal-interval construction.  Their relevant induced
  cyclic actions were tested; no unaudited literature theorem is used to
  prove (SF) or Proposition 2.4.
- **Exact finite / empirical only:** floating spectra and norm scaling above
  `n=9`; the apparent harmonic moment profile; identification of the
  balanced-third extremal family beyond `n=9`.
- **Open:** (SF), the uniform chi-square alternative, the H0 quotient gap,
  and every larger endpoint/global mixing conclusion.

## 5. First unproved standalone step

> **SHARED-FACTOR TWO-STEP INFLUENCE.**  For odd `n>=7`, let `O,O'` be two
> cyclic orbits of admissible rank-two products.  Suppose they have ordered
> transposition-pair lifts `(a,b)` and `(a,b')`, or lifts with a shared second
> factor.  Then there is an absolute constant `C` such that
>
> ```text
> TV(bar K^2(O,.),bar K^2(O',.))<=C/n^2.
> ```

The exact coupling interface is the residual forest after deletion of the
common chord.  Both posterior-predictive laws can be generated by the
conditioned-Borel component factorizations and the same uniform color
interleaving.  What remains is to couple the differing second chord while
retaining cancellation among all sixteen two-step schemas.  A proof of this
single inequality plus the proved diameter-two lemma gives the desired H0
coordinate-correlation bound.

## 6. Strongest self-attack

1. The mission proves a coordinate-correlation estimate only conditionally
   on (SF).  Even after (SF), one must invoke the appropriate M16/M70
   decomposition to turn that estimate into any bridge gap; this report does
   not silently perform that synthesis.
2. The natural Borel small-fragment coupling fails at order `d^-1/2`, much
   larger than `n^-2`.  Merely naming the residual forest is not a coupling
   proof.
3. Product kind is not a strong lumping.  More sharply, two sources with the
   same unordered residual sizes `(3,2,2)` have exact n=7 two-step kind masses
   differing by `259/2160`.  Source matching color/embedding is a real
   counterterm.
4. Pointwise relative minorization is false at the target scale.  The rare
   balanced-three-cycle diagonal makes
   `bar K^2(O,O)/bar pi(O)-1` much larger than `n^-2`, even though row TV and
   chi-square remain small in finite ranks.
5. Fixed Schatten moments are unsafe.  The positive contributions to
   `l^2 Tr((bar K-Pi)^2)` grouped by minimum residual size look proportional
   to `1/k` at `n=21`; trace four has a weaker similar profile.  This is
   **finite numerical evidence only**, not a proof of logarithmic divergence.
6. Finite spectra, stable scaled TV, and failure to find a cut do not prove
   polynomial mixing.  The balanced-third maximizer is itself a bulk family,
   so a proof cannot discard it as a rare boundary state.

## 7. Calibrations and falsification attempts

### 7.1 Exact H0 kernel checks

```text
n  l  dim(H0)  kappa_min        kappa_+          H0 Gram top
5  2     4     -1                1                1
7  3    15     -.4214363295       .2838445467      .5225630311
9  4    38     -.2599518174       .1700536823      .3775402617
```

At `n=5`, the exact characteristic polynomial is `(x+1)(x-1)^3`, the
expected excluded `l=2` obstruction.  Exact exhaustive adjacent-source
two-step TV maxima are

```text
n=7: 7185517/30375000,       n^2 times TV = 11.5914513;
n=9: 2094407996609/19603684800000, n^2 times TV = 8.6538347.
```

The full two-step Dobrushin coefficients scaled by `l^2` are
`2.689,2.161,1.727,1.627,1.738,1.542,1.643,1.812` for
`n=7,9,...,21`.  `bar K^2` has full support at all these sizes.  These are
finite facts only.

The exact schema verifier passes every stationary weight, complement type,
orbit size, row entry, normalization, and collapsed-kind formula at `n=5,7`.
At `n=9`, exhaustive exact Dobrushin maximization identifies the balanced
three-cycle `[3,3,3]` versus the near-balanced separated double
`[2,2,2,3]_S`; their exact TV is
`15514386669199/114865340625000`.  The full rational target vector is saved.

### 7.2 Refuted transfer shortcuts

- The raw support edge set is not injective as a factorization-to-tree map;
  commuting disjoint factors already collide at `n=4`.
- Stanley cyclic conjugation is neither global cyclic tree relabeling nor
  diagonal Pruefer translation: tree-shift matches are `5/125,6/16807` and
  Pruefer-shift matches are `4/125,5/16807` at `n=5,7`.  A single Hurwitz
  edge can remain quotient tree/Pruefer distance `n-2` at `n=7`.
- A single contiguous Hurwitz bubble covers only `950/1860` ideal micro
  exchanges at `n=5` and `68168/730170` at `n=7`; an explicit infinite
  Stanley one-exchange family is impossible by one bubble for every
  `n>=7`.
- Lex-shortest quotient routing is connected but has finite normalized load
  `16.65` at `n=5` and `487.42` at `n=7`; recovery collisions prevent a
  universal congestion inference.
- Moszkowski and Goulden--Yong agree with some global tree shift on only
  `10/125,27/16807` states; Goulden--Pepper on only `3/125,3/16807`.
  The latter changes the degree profile on `58/125,9212/16807` states.
- Cyclic averaging does not flatten maximal weak-order interval incidence:
  max/min quotient incidence ratios are `3.5` at `n=5` and `22` at `n=7`;
  thus the proposed uniform-incidence transfer is already exactly false at
  the smallest tested sizes.  These finite ratios make no asymptotic claim.
- The Pollak/parking shortcut is false.  Stanley parking labels never become
  a diagonal translation under `U` in `125` or `16807` states.  At the
  middle pair for `n=7`, even the ordered labels, full multiplicity vector,
  and occurrence ranks leave `991` ambiguous metadata keys, with up to six
  distinct product orbits.

### 7.3 Required scope calibration

| candidate | claimed target | endpoint check | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---:|---:|---|---|
| `bar K` correlation kernel | uniform minimal long-cycle product quotient | yes | not a global sampler claim | rational n=5,7,9 | keep reduction |
| Stanley/UST comparison | same quotient via tree basis exchange | yes | quotient only | exhaustive n=5,7 | reject direct transfer |
| shared-factor two-step coupling | H0 coordinate correlation | conditional on proof | not applicable | exact n=7,9; numeric to 21 | open |

Odd identity length, `m=0,2`, `N=2`, and the identity-bridge cases
`S_3,m=4`, `S_4,m=4,6` are outside this fixed nonidentity endpoint.  No
conclusion about them is drawn.

## 8. Artifacts and reproduction

Primary proof artifacts:

- `plan.md`, `checkpoint.md`, `theorem.md`, `gap_parameterization.md`,
  `report.md`;
- `h0_coordinate_correlation.py`, exact output
  `h0_coordinate_correlation_n9.json`, and compact scaling output
  `h0_coordinate_correlation_scaling_n21.json`;
- `gap_schema_verifier.py`, `gap_schema_checks_n7.json`;
- `h0_spectral_certificate.py`, `h0_spectral_certificate_n9.json`;
- `h0_phase_collision.py`, `h0_phase_collision_n9.json`;
- `moment_scaling_diagnostic.py`, `moment_scaling_n21.json`.

Negative-route artifacts:

- `cyclic_tree_action.py`, `stanley_local_action.py`,
  `quotient_basis_exchange.py`, `one_bubble_family.py`,
  `maximal_interval_incidence.py`, `equivariant_bijections.py`,
  `primary_bijection_quotient.py`, `pollak_pair_product_falsifier.py`, and
  their recorded JSON outputs.

Representative commands from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/gap_schema_verifier.py --n 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/gap_schema_checks_n7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation.py --n 7 --n 9 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation_n9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation.py --compact --n 7 --n 9 --n 11 --n 13 --n 15 --n 17 --n 19 --n 21 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation_scaling_n21.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_spectral_certificate.py --n 5 --n 7 --n 9 --input experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_coordinate_correlation_n9.json --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M73-cyclic-orbit-incidence-gap/h0_spectral_certificate_n9.json
```

All scripts are deterministic; stochastic seeds are `null`.  Exact rational
claims are separated from floating diagnostics in every JSON artifact.

## 9. Verdict

**OPEN AT A NAMED STEP, WITH A PROVED DIAMETER-TWO REDUCTION.**

The original cyclic-orbit incidence gap remains unresolved.  M73 replaces
the false tree-equivariance, one-bubble, parking, and residual-size closure
routes by an exact cyclic-composition kernel and a universal diameter-two
source graph.  The remaining H0 coordinate-correlation obligation is the
local shared-factor two-step influence inequality (SF), or the stronger
uniform two-step chi-square bound.  Moment harmonic behavior is finite
diagnostic evidence only.  No polynomial H0 bridge gap or Terminal claim is
made.
