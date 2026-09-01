# M73 halfway checkpoint: cyclic quotient is connected but not naturally local

Date: 2026-08-12.

## Frozen target and conventions

For odd `n=2l+1`, `m=n-1`, and `h=(0 1 ... n-1)`, the law is uniform on
the reduced transposition factorizations `t_1...t_m=h`.  Permutations compose
as `(pq)(x)=p(q(x))`; tuples multiply left-to-right.  The target is the `H_0`
sector of M70, equivalently the uniform stationary-flow quotient by
simultaneous conjugation `U(t)=h^-1 t h`.  This is not the identity bridge.

## Proved structural falsifiers

1. The raw support edge set is not a Dénes bijection.  Already for the
   four-cycle,

   ```text
   ((0,1),(2,3),(1,3))  and  ((2,3),(0,1),(1,3))
   ```

   have the same product `(0 1 2 3)` and the same support tree.  They differ
   by commuting adjacent disjoint factors.  Hence a raw support-tree basis
   exchange has no unique factorization lift without retaining a potentially
   large compatible-order fiber.

2. Under Stanley's genuine bijection to uniform labelled Cayley trees,
   simultaneous conjugation is not cyclic relabeling of tree vertices and is
   not diagonal translation of Pruefer values.  Exact counts are:

   ```text
   n=5: tree-shift matches 5/125; Pruefer-shift matches 4/125;
   n=7: tree-shift matches 6/16807; Pruefer-shift matches 5/16807.
   ```

3. Quotienting by `U` does not restore locality of an adjacent Hurwitz move
   under Stanley's bijection.  At `n=7`, a single Hurwitz edge can still have
   quotient tree basis distance `5=n-2` and quotient Pruefer Hamming distance
   `5`.

4. A single contiguous right/inverse Hurwitz bubble does not simulate every
   Cayley basis exchange modulo `U`.  It covers `950/1860` directed micro
   exchanges at `n=5`, but only `68168/730170` at `n=7`.  The first failure is
   the path-tree exchange `(0,1)->(0,4)` at both sizes.

These are universal-route refutations because one exact counterexample is
enough; their finite frequencies are only diagnostics.

## Exact positive calibration

Let `U_n` be UST down-up on Stanley Cayley trees and project its stationary
flow to the `U`-orbits.  This quotient remains reversible for the uniform
orbit law and has gap at least `1/(n-1)`, because it is the exact projection
of the accepted UST basis chain.  Let `bar L_n` be the quotient adjacent
raw-rank heat bath.

The exact quotient graphs give:

```text
                         n=5       n=7
orbit states               25      2401
directed bar-L edges       120     17150
directed quotient-UST      510    303954
max shortest L distance      4        12
lexicographic path load     333/20 81887/168
```

The load is the fully normalized comparison ratio: quotient stationary
factors cancel, UST cut denominators and local two/three-state fiber
denominators are exact, and path length is included.  These finite values are
consistent with a polynomial comparison but do not prove one.

## Current first unproved step

> **RECOVERABLE STANLEY-EXCHANGE ROUTING.**  For every labelled Cayley-tree
> basis exchange `T -> T-e+f`, route the corresponding factorization to the
> target cyclic orbit through adjacent Hurwitz heat-bath edges in length
> `n^O(1)`, so that a used directed edge together with `n^O(1)` choices of
> exchange/path metadata recovers the source transition.

M70's full-state H4 padding would then transfer the resulting polynomial
gap from `bar L_n` to `B_l`, closing the fixed-long-cycle `H_0` sector.  The
one-bubble version is refuted above; the remaining task is a multi-bubble or
fixed braid-word construction with recoverable metadata, not mere diameter.

## Artifacts

- `plan.md`
- `cyclic_tree_action.py`, outputs through `n=7`
- `quotient_basis_exchange.py`, outputs through `n=7`

Both scripts are deterministic, use `seed=null`, record the repository commit
and exact command, and verify state counts, free cyclic orbits, local fiber
sizes, row normalization, and detailed balance.

## Redirected H0 coordinate-correlation checkpoint

The coordinator redirected the primary lane after the tree comparisons were
refuted.  Let `G_i=t_(2i-1)t_(2i)`, `theta(g)=h^-1gh`, and let `K` be M16's
one-coordinate forward correlation operator.  On `theta`-invariant functions
`K=K*`.  The following statements are now proved in `theorem.md`.

1. If `a(g)` is the number of ordered transposition-pair lifts and `F_r(q)`
   is the exact number of minimal length-`r` transposition factorizations,
   then on cyclic product orbits

   ```text
   bar K([g],[s])=sum_(u in [s])
      a(u)F_(n-5)((gu)^-1h)/F_(n-3)(g^-1h),
   bar pi([g])=|[g]|a(g)F_(n-3)(g^-1h)/n^(n-2).
   ```

   Row normalization and detailed balance hold exactly over the rationals.

2. `K` itself need not be positive: negative eigenvalues occur.  For a real
   invariant eigenvalue `kappa`, the covariance matrix of
   `(v(G_1),...,v(G_l))` is `(1-kappa)I+kappa 11*`.  Positivity therefore
   proves `kappa>=-1/(l-1)`.  The transverse M16 Gram branch is at most
   `1/(l-1)`; only the positive spectral edge remains.

3. With `L_0=bar K-Pi`, the exact two-step likelihood is

   ```text
   R_0^(2)(g,t)=E_(S~pi)[R_0(g,S)R_0(S,t)].
   ```

   The first open lemma has been reduced to the pointwise completion bound

   ```text
   sup_g E_(T~pi)|R_0^(2)(g,T)-1| <= C/l^2.           (CP)
   ```

   Since the left side is `||L_0^2||_(infinity to infinity)`, (CP) implies
   every invariant `|kappa|<=sqrt(C)/l`, and hence the H0 coordinate-Gram
   top is `O(1/l)`.  Exact cyclic collision formulas for `Tr(L_0^2)` and
   `Tr(L_0^4)` are also recorded, but (CP) is the sharper target.

Exact rational characteristic polynomials and root-isolating intervals give

```text
n  l  dim(H0)  kappa_min       kappa_max       coordinate-Gram top
5  2      4    -1               1               1
7  3     15    -.4214363295      .2838445467     .5225630311
9  4     38    -.2599518174      .1700536823     .3775402617
```

The exact maxima in (CP), multiplied by `l^2`, are `3.2877834853` at `n=7`
and `3.2298852677` at `n=9`.  Floating checks at `n=11,...,21` stay between
`2.29` and `2.56`.  The maximizer is exceptional at `n=7`, but for every
tested `n=9,...,21` it is the oriented 3-cycle whose three circular support
gaps are as balanced as possible:

```text
n=9,11,13,15,17,19,21:
(3,3,3),(3,4,4),(4,4,5),(5,5,5),(5,6,6),(6,6,7),(7,7,7).
```

Thus the extremizer is not a fixed small-gap family.  Its two-step signed
target deviation is dominated by double-transposition targets; the largest
negative class has complement cycle sizes `(n-2,1,1)`, while the total
oriented-3-cycle sector has the compensating positive signed mass.  Simple
minimum-gap and reciprocal-gap envelopes fail to capture this: their needed
constants grow through `n=21`.  The current analytic target is to sum Cayley
completion weights by noncrossing overlap pattern before taking absolute
values, especially for this balanced-third source.

New artifacts are `theorem.md`, `h0_coordinate_correlation.py` and its exact
and scaling outputs, `h0_spectral_certificate.py` and output, and
`h0_phase_collision.py` and output.  All finite spectra are labeled finite;
no H0 bridge gap or Terminal claim is made.

## Final pre-freeze checkpoint: diameter-two shared-factor reduction

The H0 coordinate-correlation problem is still open, but its first analytic
step is now local.

1. `gap_parameterization.md` proves exact quotient stationary weights:
   oriented three-cycles are cyclic positive three-compositions, while
   double transpositions are colored positive four-compositions (separated
   or nested).  It proves the exact four-schema row formula
   `{I3,IS,IN,X}` from the three residual cycles of `g^-1h`; consequently
   `bar K^2` is a signed sum of sixteen schema pairs.
2. The cross-cycle first-edge law is exactly a pair of independent critical
   Borel tree sizes conditioned on their sum.  The smaller-fragment coupling
   has exact TV equal to a Borel tail, asymptotic to `2/sqrt(pi d)`, so a
   schema-by-schema one-step coupling is too lossy.
3. The quotient source graph joining two product orbits when lifts share one
   raw transposition has diameter at most two for every odd `n>=5`.  The
   proof rotates the second shared chord into the larger arc of the first;
   the unique no-room case gives an admissibly oriented three-cycle.
4. The new first open lemma is therefore **SHARED-FACTOR TWO-STEP
   INFLUENCE**:

   ```text
   max_(O~O') TV(bar K^2(O,.),bar K^2(O',.)) <= C/n^2.
   ```

   Diameter two would give `delta(bar K^2)<=2C/n^2`, hence every invariant
   `|kappa|=O(1/l)`.  This is equivalently a strong-data-processing bound for
   the two-block Gibbs/data-augmentation kernel of the exact quotient joint
   law.
5. Exact exhaustive values for the adjacent maximum are
   `7185517/30375000` at `n=7` and
   `2094407996609/19603684800000` at `n=9`.  The quotient source graph has
   diameter two at both sizes.  Floating checks through `n=21` keep
   `n^2` times the adjacent maximum between `6.72` and `7.36` for `n>=11`.
6. A stronger uniform two-step chi-square row bound `C/n^4` is also
   sufficient and remains numerically stable.  It is unproved.
7. Fixed Schatten moments are not promoted: the positive minimum-residual
   decomposition of `l^2 Tr(L0^2)` has an approximately harmonic finite
   profile, with a weaker analogous profile for trace four.  This is only
   numerical evidence, not a proof of logarithmic divergence.
8. `gap_schema_verifier.py` checks every complement type, stationary weight,
   orbit size, row entry, normalization, and collapsed-kind identity exactly:
   all 400 entries pass at `n=5` and all 11025 pass at `n=7`.
9. The coarse target-kind mass is proved to be within
   `6/[n(n-4)]` of stationarity after every positive number of steps, but
   conditioning only on the unordered residual sizes is false.  At `n=7`
   the exact two-step kind-mass spread within residual type `(3,2,2)` is
   `259/2160`.

Verdict for freeze: **OPEN AT A NAMED STEP**.  No polynomial H0 Poincare
gap, no full fixed-endpoint bridge gap, and no Terminal A/B claim is made.
