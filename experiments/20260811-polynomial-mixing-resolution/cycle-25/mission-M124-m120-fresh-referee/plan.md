# M124 plan: fresh referee audit of frozen M120

Date: 2026-08-12 UTC.

## Objective

Audit the immutable M120 mission at
`../mission-M120-local-unicycle-incidence-gap` and issue a binary
`ACCEPT`/`REJECT` decision.  The audit target is the auxiliary incidence
chain `A_d` with stationary law `rho(kappa) proportional to |C_kappa|`, not
the original uniform identity-word law.

## Assigned claims

1. Verify all five supplied SHA-256 digests before relying on M120.
2. Independently derive the nonidentity singleton-split probability and its
   universal lower bound.
3. Verify existence and exact probability of a reverse singleton join at
   every identity key for `d>=3`.
4. Verify the full defect range, the statewise down/up probabilities, the
   `h(a+b)/(h(a)h(b))` binomial-pmf inequality, and the `d=2` exception.
5. Audit the exponential-valley counterexample and confirm M120 does not
   promote any spectral-gap conclusion.
6. Reconstruct all keys and exact adjacent flows for `2<=d<=5` in a fresh
   script that imports no M120 or predecessor mission code.

## Target, convention, and kernel

For a realizable connected-unicyclic key
`kappa=(j,p,Q_L,Q_R)`, permutations compose as
`(p q)(x)=p(q(x))`, factors multiply left-to-right, and

```text
rho(kappa)=|C_kappa|/Z_inc,
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2 Z_inc)
```

for compatible adjacent cuts, with all unused row mass held.  The factor
`1/2` is the left/right direction coin.

## Method and falsifiers

- Re-derive every ratio from one-sided genus-zero counts, keeping factorial,
  atom, block, and direction factors separate.
- Search every finite key through `d=5` for a missing constructed neighbor,
  an exact ratio mismatch, a failed bound, a missing defect level, a row-mass
  failure, or an edge not changing defect by one.
- Instantiate the claimed valley chain with exact rational arithmetic and
  check detailed balance, rate floors, and exponentially small middle-cut
  conductance.
- Reject on any material formula, quantifier, boundary, or claim-status
  failure.  Numerical finite agreement alone is not grounds for acceptance.

## Artifacts and command

Planned owned outputs: `checkpoint.md`, `fresh_audit.py`, `results.json`,
`report.md`, `SHA256SUMS`, and `freeze_manifest.md`.

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M124-m120-fresh-referee/fresh_audit.py \
  --d 2 3 4 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M124-m120-fresh-referee/results.json
```

The computation is deterministic (`seed=null`).  No file outside this
mission directory will be edited.
