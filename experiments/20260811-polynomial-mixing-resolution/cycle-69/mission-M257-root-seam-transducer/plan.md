# Mission M257 plan: root-seam transducer

## Objective

Resolve exactly the root-seam path transducer (RSPT) left in M250,
equations (4.1)--(4.5), for every ordinary odd edit and every `d >= 5`.
The allowed terminal outputs of this mission are: a proof, a symbolic
counterfamily, or the first standalone path-row lemma still missing.

## Scope and target

- **Claim under test:** the deterministic DPS root-seam identities used by
  the repaired initial-defect lemma.  This is a combinatorial statement about
  one canonical unedited and one edited tree run, not a Markov-chain result.
- **Sampler target in the surrounding project:** global fixed-length uniform
  law on identity words in `S_N`; no sampler or mixing claim is proved here.
- **Immutable inputs:** M240/M242; only M244 Theorem 3.1 as corrected by M247;
  M250/M254; and the locked DPS source PDF with SHA-256
  `98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
- **Required boundary cases:** cyclic seam `a=1`, lower-index post-wrap
  children, new child `d`, edited coordinate, every root label, and exhaustion
  of unnamed coordinates.
- **Forbidden inferences:** fixed edits, every-color synchronization,
  voltage-corrected length, spectral gap, mixing, or either Terminal.

## Method

1. Verify all immutable manifests and the locked PDF digest.
2. Reconstruct precisely M250 equations (4.1)--(4.5), token meanings, and
   open/closed root states from the frozen artifacts and cited source pages.
3. Derive the one-dimensional stopped-path/root-token recurrence before any
   calibration.  Prove the exposed-set open/closed transitions and inherited
   low-endpoint assertions row by row.
4. Give explicit sealed/open root tables covering every root label and the
   cyclic seam.  Track unnamed-coordinate supply rather than assuming a fresh
   label exists.
5. Only after the analytic recurrence is fixed, reuse at most M250's four
   frozen rows as calibration.  No new finite census is allowed.
6. Freeze the strongest valid result, label all dependencies and gaps, record
   a falsification attempt on the minimal/boundary cases, hash all artifacts,
   and request a fresh audit.

## Expected failure modes

- M250's stated recurrence may omit a lower-index child reached after cyclic
  wrap.
- An inherited low endpoint may change rank when the edited high label is
  inserted or when unnamed labels are exhausted.
- The open/closed state may not contain enough information to determine the
  root output; an additional stopped-path datum may be necessary.
- A root table may silently assume the edited coordinate is distinct from a
  root endpoint or that a fresh unnamed coordinate remains.

## Verdict vocabulary

`proved`, `refuted`, or `unresolved reduction`.  Finite calibration alone is
never promoted to a universal statement.
