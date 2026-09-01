# M131 plan: first open suffix excess five

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact target

Work only on the auxiliary full nonlazy stationary-flow parking-degree
projection in the minimal-long-cycle sector. For every right-heavy context

```text
x=(s,K,K-1,B),  s>=6, K>=1, B=s-5,
q_x=w_6 w_(s-5)/w_(s+1),
```

prove or refute

```text
H(x)=(I-Q)^(-1)A_0(x) <= q_x(1-q_x).
```

Every attachment rank `j=1,...,k` is retained; only `j=0` and inactive
rank-one targets are killed. The project target remains uniform on
fixed-length identity words, but this is only an auxiliary projection lemma.
Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.

## Method

1. Reconstruct the exact `L=5` support, canonical exceptional basins, and
   reset envelope from definitions. Cross-check grouped and literal forms.
2. Prove the needed arbitrary-deficit `L=3` child envelope, specialized at
   least to the deficit-two child forced by the `L=5` root. Retain every
   descendant attachment rank before aggregation and use only accepted
   `L<=4` results.
3. Form the exact rational closed envelope `E_5(z)`. Search literal smallest
   cases for either an actual contraction counterexample or a normalization
   error.
4. If the envelope survives, clear denominators and seek a complete finite-
   rank plus tail-box Bernstein certificate. If this is infeasible or false,
   freeze the first exact obstruction or the narrowest remaining scalar
   sign lemma.

## Expected failure modes and anti-drift

- The 31 exceptional basins may make the ordinary-basin envelope too loose.
- The deficit-two `L=3` child normalization may introduce a missing split or
  attachment factor; literal recurrence is the independent check.
- Bernstein coefficients may be negative even when the actual Cayley curve
  is positive; that refutes only the selected box certificate.
- Do not use the refuted generic basin-frame/Bessel, raw one-step defect, or
  two-layer sign arguments. Do not infer an auxiliary gap, ROOT-MEAN LIFT,
  original-chain mixing, Terminal A, or Terminal B.

## Reproducibility

Use Python 3 standard-library `fractions.Fraction`, deterministic arithmetic,
and `seed=null`. Record exact commands, raw JSON, Python/dependency versions,
repository status, a nine-field report, freeze manifest, and SHA-256 hashes.
