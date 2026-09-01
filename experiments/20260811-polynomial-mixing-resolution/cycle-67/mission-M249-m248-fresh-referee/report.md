# M249 report: fresh immutable referee of M248

Date: 2026-08-14 UTC.

## Verdict

**ACCEPT**, with zero material and zero nonmaterial objections.

For every odd `k>=3` and integer `2<=ell<=(3k-1)/2`, frozen M248 proves

```text
|S_(Y_ell)+K_(Y_ell)|<=7000sqrt(ell)/k,
|S_(X_ell)+K_(X_ell)|<=7160sqrt(ell)/k,
|DE_(Y_ell)|<=7004sqrt(ell)/k,
|DE_(X_ell)|<=7164sqrt(ell)/k.
```

Thus WBE and signed averaged DE are proved for both literal observables.

## Decisive checks

- M248's full inventory passes with checksum-file digest
  `c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8`.
  Every file in all eight cited dependency inventories also passes, and
  every recomputed checksum-file digest agrees with M248's manifest.
- The exact partition identity gives `S_Y+K_Y` as the accepted YCM prefix.
  Subtracting the complete literal X and Y raw laws gives the accepted TCM
  prefix, retaining all kinds, both seams, ordered-tuple multiplicity, and
  equal-size collisions.
- Accepted YCM `7000` and TCM `160` give X-WBE `7160` by one triangle
  inequality on the common full domain.
- Fresh algebra gives
  `a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L]`,
  `a_L>=1/2`, and hence `|N_Z|<=16/k^2`.
- Since `k^2 ell>=18`, the remainder is at most
  `4sqrt(ell)/k`, giving DE constants `7004` and `7164`.

The no-import independent checker passes through odd `k<=2001`, all
admissible splits and cutoffs, and every generated corrected-domain G call.
This is exact finite falsification only; the proof is the symbolic derivation
in `proof_audit.md`.

## Numbered objections

1. Material objections: none.
2. Nonmaterial objections: none.

## Scope

DV remains open. This acceptance does not infer conditional J2,
PCR/WPCR/SCBR, any comparison theorem, spectral gap, mixing bound, or either
Terminal.

