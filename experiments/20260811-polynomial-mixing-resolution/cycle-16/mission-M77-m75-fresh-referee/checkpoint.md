# M77 checkpoint: all decisive independent checks agree with M75

Date: 2026-08-12.  Provisional verdict: **ACCEPT**, subject to the final
artifact/hash audit.

## Frozen-input integrity

The frozen inputs match the mission prompt exactly:

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
17bb22b3c041ec1917f206d0a3cf9a8fba2f049fd5a6b61da2eb004699a6b89b  M75 freeze_manifest.md
```

Every artifact hash listed inside the M75 manifest was also recomputed and
matches.  No frozen file was modified.

## Proof audit

1. **Randomized first-crossing theorem: correct.**  Successful source/word
   pairs have total mass at least `eta|S|`.  For a fixed word and time, the
   actual directed edge source and inverse prefix determine at most one
   original source.  Summing over times gives path load at most
   `E ell=Dbar`; summing possible first-hit times gives terminal load at
   most `E(ell+1)=Dbar+1`.  Nonnegative Tonelli sums make the same proof
   valid for countable support.
2. **Endpoint variant, including empty words: correct.**  For a fixed
   terminal edge and fixed word there is only one possible source at the
   endpoint, so total terminal load is at most `sum_beta mu(beta)=1`,
   including positive mass on `ell=0`.  Path load remains at most `Dbar`;
   hence `max(Dbar,1)` is the right denominator.
3. **M60 null pushing: correct.**  From `xUy=U`,
   `x=UyU^{-1}`; right-bubbling through `U` changes the moving factor to
   `U^{-1}xU=y` and yields `PUyyS`.  Globally interleaved factors in
   other components are disjoint and conjugate the moving factor trivially.
   Every bubble, refresh, and square slide is a padded same-product H3
   outcome.  The displayed lengths and the `binom(m,2)M` reconstruction
   bound are correct.
4. **Normalizations: correct.**  Independent enumeration through `N=8`
   gives
   `D_N=M+6(N-2)+2 binom(N-2,2)=(3N^2+N-12)/2`.
   Any length-three fiber has at most `M^2` members because its first two
   transpositions force the third.  Thus
   `p_H=1/[6(m-2)M^2]`, while a specified square refresh has probability
   `1/[6(m-2)D_N]>=p_H` for the stated `N>=5` regime.
5. **Positive braid double count and Garside discussion: correct.**  Each
   fixed simple positive braid is a bijection, so every target column has
   exactly `m!` incoming edges even with parallel/stabilizer
   multiplicity.  This is only an average identity and gives no row
   minimum.  For a simple braid `beta`, the left complement satisfies
   `beta^L beta=Delta`; applying it moves the marked set to
   `beta^L G`.  Since the marked set is not braid invariant, this cannot
   flatten the rows.
6. **Scope: correct.**  M75 keeps whole-macro averages, arbitrary partial
   subsets, worst-row domination, two-component exit, multilevel merger
   occupation, and full-`K` mixing separate.  It makes no Terminal-A,
   Terminal-B, conductance-upper-bound, spectral-gap, or polynomial-mixing
   claim.

## Independent exact results

The fresh `independent_audit.py` imports no M75 code.  Its JSON records:

- a rational two-state coarea model with empty-word mass `1/2`,
  `Dbar=1/2`, and endpoint denominator exactly `1`; every subset passes,
  with equality for the full set in the endpoint bound;
- a nontrivial `N=5,m=8` null push with `x!=y` and a second nontrivial
  support component interleaved inside `U`; all six H3 steps preserve
  product and labeled weighted support data, and 241 distinct reconstructed
  words occur among the 280 allowed source descriptions;
- for the displayed ambient `N=6,m=10` witness, exactly the two deletion
  pairs `(0,5),(2,7)` preserve identity and both residuals are
  disconnected; all 18 signed radius-one paths fail, there are 15 distinct
  radius-one endpoints, and 104 of all 324 signed radius-two paths succeed;
- for all 240 connected `S_3` identity words of length six and all 720
  simple positive braids, marked row counts range from 608 to 720 with nine
  values, every column degree is 720, distinct row endpoints range from 15
  to 119, and maximum parallel multiplicities take exactly
  `{12,16,24,48}`.  A concrete braid sends a marked word to an unmarked
  word.

The finite results reproduce the decisive M75 values but are not promoted to
an asymptotic row bound.

## Remaining work

Finalize the report, reproduction command, owned-file hashes, and repository
status.  No material or nonmaterial correction has been identified.
