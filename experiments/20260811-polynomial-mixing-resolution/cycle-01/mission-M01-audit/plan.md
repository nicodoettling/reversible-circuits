# M01 and adjacent-pair comparison audit plan

## Objective

Independently audit the frozen coordinator proofs of:

1. irreducibility of the exact lazy same-product `{3,4,5}` heat-bath chain
   on `Omega(N,m)` for every `N>=3` and even `m>=4`;
2. the Dirichlet-form domination
   `E_K >= E_J/(3*binom(N,2)^2)` for the lazy adjacent-pair heat bath `J`;
3. the exact stationary adjacent-square frequency and changed-refresh rate.

The target law is the global fixed-length uniform bridge law. Permutations are
maps and `pq` means `p` after `q`; a word evaluates as `t_1...t_m`.

## Named failure modes

- a mismatch between the project Hurwitz generator and Ben-Itzhak--Teicher
  Theorem 3.4;
- missing isolated vertices, component weights, or near-minimal components;
- failure of length-three padding at either endpoint;
- failure of a length-four square refresh at a boundary or at `m=4`;
- multiple adjacent-pair scan indices contributing to one off-diagonal
  `J(x,y)`, invalidating the claimed point probability;
- a dropped laziness, block-length, window-scan, or conditional-fiber factor;
- misuse of an average stationary square rate as a worst-state estimate.

## Exact falsification check

Run:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M01-audit/exact_audit.py \
  > experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M01-audit/results.json
```

The finite calculation can falsify the universal claims by finding a
disconnected listed calibration kernel, a normalization error, a nonunique
off-diagonal `J` scan index, a violation of the pointwise comparison, or a
failure of the square-counting identity. It cannot prove the universal
claims; those require the accompanying symbolic audit.

No randomness or nonstandard dependency is used.
