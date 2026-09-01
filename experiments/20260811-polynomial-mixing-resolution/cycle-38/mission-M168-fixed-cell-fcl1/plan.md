# M168 plan: fixed balanced-cell FCL1

Date: 2026-08-13. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact target

Work only with M161/M166's accepted fixed balanced separated cell for
M73's nonlazy cyclic rank-two quotient kernel.  Permutations compose as
`(pq)(x)=p(q(x))`; factors multiply left-to-right.  Let `n=3k`, with odd
`k>=3`, and retain

```text
A_k=(0,k,2k),                 B_k=(0,1)(k,2k),
t_y=(0,1)(1+y,2+y),          1<=y<=3k-3,
z_k(y)=[bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/bar pi(O_y),
Z_k(y)=k z_k(y).
```

The sole theorem target is

```text
(FCL1)  sup_(odd k>=3) sum_(y=1)^(3k-3)|Z_k(y)| < infinity.
```

Prove this uniformly, or refute it by a rigorous asymptotic or exact
infinite counterfamily.  Finite checks are falsification/calibration only.

## Accepted inputs

- Frozen and accepted M155/M159 boundary-condensate reduction.
- Frozen and accepted M161/M166 complete signed fixed-cell formula,
  including literal `IS`, `IN`, and `X` target responses, triangle and
  double intermediate strata, two source channels, reflection, and exact
  normalization.
- M102/M105 warning: collision and lower-support terms must remain inside
  the signed convolution before absolute value.

## Proof route

1. Rewrite M161's lag-slice/circular-correlation formula as explicitly as
   possible for the special boundary edges, retaining all signed categories.
2. Seek a discrete first- or second-difference representation in the lag
   variable and apply Abel summation only after the two source channels and
   triangle/double pieces have been combined.
3. Seek a circular-correlation total-variation inequality whose right-hand
   side is summable uniformly in `k`; track wraparound and exceptional phases
   exactly.
4. If boundedness fails, isolate a sign-stable term or exact formula giving
   an infinite odd-`k` lower-bound family.  Do not infer failure from a finite
   trend.

## Guardrails and expected failure modes

- No broad quotient matrix, broad shell scan, direct-L1/all-edge estimate,
  gap claim, H0 claim, bridge claim, identity-chain claim, or Terminal
  inference.
- No schemawise absolute values before the `IS/IN/X` and triangle/double
  cancellations.
- A formal Abel identity without a uniform endpoint/variation bound is only
  a reduction, not FCL1.
- A fixed-cell theorem, if obtained, is only one cell and does not establish
  M155's direct-L1 obligation.

## Deliverables

- `checkpoint.md`, updated at halfway.
- A compact theorem/proof or obstruction note and only narrowly targeted
  exact code/data if needed.
- A nine-field `report.md` with labeled claim status, dependencies,
  falsification, limitations, commands, hashes, and hygiene.
- `freeze_manifest.md` and `SHA256SUMS`; freeze for a fresh independent audit.

