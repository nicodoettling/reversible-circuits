# M285 checkpoint

## Initial checkpoint (pre-inspection)

- Mission directory initialized before inspecting substantive M280/M283 or
  M91/M94, M261/M264 artifacts for this mission.
- Target fixed: prove/refute all-rank OCI per channel, not merely reproduce
  finite positivity.
- Intended route: exact owner-cycle/phase disintegration followed by a
  Cayley–Borel pairing, PSD kernel, or total-positivity test.
- At most one formula-driven compact exact falsifier is permitted.
- No predecessor, coordinator, manuscript, skill, or shared durable file
  will be edited.

## Halfway checkpoint: source lock and formula freeze

All six required immutable inventories pass.  Their checksum-file digests
are:

```text
M280 60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9
M283 156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf
M91  0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94  47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261 b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264 b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
```

The exact phase/composition law and rooted-owner autocorrelation
decomposition are now fixed in `coefficient_reduction.md`.  The Borel
MON/FOSD route is already refuted by frozen exact inputs; the remaining
natural untested claim is signed spectral dominance after the statewise PSD
repair.

### Sole predeclared compact falsifier

At exactly `k=3`, reconstruct both normalized channels independently and
compute the full signed circular sequence

```text
D_j(ell)=eta_j(Ftilde_ell),   ell mod 9.
```

Test the circulant signed kernel for positive semidefiniteness.  If a Fourier
mode is negative, freeze an exact rational quadratic-form witness; this
refutes signed PSD dominance only, not OCI.  Also guard the six admissible
OCI lags, direct/owner equality, channel normalization, and reflection.
No other rank or falsifier will be run.  Finite survival would remain
inconclusive.

## Final checkpoint: sole falsifier and stop

The predeclared `k=3`, `n=9` check was run once.  It independently rebuilt
both normalized channels using exact `Fraction` arithmetic, with no import
of predecessor code or data.  All six admissible OCI entries in each channel
are strictly positive, so this finite row neither proves nor refutes OCI.

The signed repaired circulant fails PSD dominance in channel two.  For

```text
v=(10,8,2,-5,-9,-9,-5,2,8),
M_(ab)=eta_2(Ftilde_((b-a) mod 9)),
```

the checker obtains exactly

```text
v^T M v=-310962953715709/12252303000000<0.
```

This refutes only the proposed signed-PSD proof route.  OCI, CP, OS+, MS,
FCL1, and every gap/mixing/Terminal claim remain unresolved.  The frozen
standalone obligation is `(GOCI_j)` in `coefficient_reduction.md`; no second
rank or falsifier is authorized or run.
