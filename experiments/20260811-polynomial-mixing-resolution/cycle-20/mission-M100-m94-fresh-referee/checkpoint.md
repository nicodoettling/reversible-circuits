# M100 halfway checkpoint: no material defect found

Date: 2026-08-12.  Controlling status: referee audit in progress.

## Frozen provenance

Running `sha256sum -c SHA256SUMS` inside M94's frozen directory returned
`OK` for all thirteen entries.  The independently observed digests are

```text
report.md             eeceb389e145b094ab29c1be76f8f5e27078c93604e4ba4d051f436c4644338b
bulk_obstruction.md   2e86f0e3cb6c4449c16e83d16535f679deb1ed105c952c8d25aaee26556569be
bulk_event_float_k11  4d1ce5eae2314b03e2e668d81a63487c424e497144db5cc72e61edb78aacd373
SHA256SUMS            47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
```

## Analytic audit to date

- The Borel rewrite is exact: the common `e^-n` cancels in every residual
  tree product and `(n-5)!/(n-3)!=1/[(n-3)(n-4)]`.
- Expanding quotient rows before replacing the intermediate-orbit sum by a
  raw-state sum gives M94's score formula.  The target average by `|O_t|`
  is necessary and correctly retains the short size-`k` orbit of `A_k`.
- For `R_D(s)=b_(D-s)/[(1-1/D)b_D]`, uniform Stirling/Taylor expansion gives
  `R_D(s)=1+(1+3s/2)/D+O((1+s^2)/D^2)` for `s=o(D)`.  Taking
  `D=2k-1,k` gives M94's boundary expansion and its summed error is smaller
  by `u/k` when `u=o(k)`.  The bulk Riemann argument also has the claimed
  integrable `O(x^-1/2)` cancellation at zero.
- Every odd-`n` double orbit has size `n` and four colored encodings, two of
  each color.  Dividing the two-color composition sum by four produces the
  coefficient in M94's exact event-mass formula.  Stirling gives
  `(2 pi n)^-1 I`; since `n=3k`, the reported `I/(6 pi)` limit is correct.
- Stationary Cauchy--Schwarz gives only the conditional implication from
  `(BD)` to an `Omega(k^-3)` BA2 lower bound.  M94 does not promote `(BD)`.
- The shell bound retains both possible double multiplicities: `(d-1)` when
  the fixed residual component is split into two support gaps, and `(j-1)`
  when a remaining residual component is split.  The exact Borel convolution
  identities reduce both to `O(b_d)` uniformly because `d<=n/3`.

## Fresh finite check

`independent_bulk_audit.py` imports no M94 or predecessor code.  It builds
literal ordered transposition pairs and exact completion counts, then checks
raw Borel rows, quotient rows, detailed balance, stabilizers, the score/event
convolutions, the event mass, and Cauchy over `Fraction`.

At `k=3,5` it reproduces M94's scaled rows:

```text
k    k*pi(E)       k^2*Delta(E)    k^4*event-L2    k^4*Cauchy    k^4*BA2
3    .0748530881   .0643913022     .1740956922     .1661750997   5.230225557
5    .0743407909   .0470842462     .1872283239     .1491056401   3.577332647
```

The compact `k=5,7,9,11` payload passes all internal scaling, normalization,
Cauchy, event-orbit-count, and independent exact event-mass checks.  Its large
all-target source JSON files were intentionally not retained, so the audit of
the `k=11` signed defect and full BA2 value is compact-payload consistency,
not a second full-kernel rerun.  Those values remain floating finite only.

## Remaining work

Complete the claim-status audit, freeze the M100 artifacts, remove generated
caches, and issue the final numbered-objection decision.  At this checkpoint
there is no material objection; `(BD)`, `(BA2)`, direct signed L1, H0, every
bridge gap, the identity heat-bath gap, and both Terminals remain unresolved.
