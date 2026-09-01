# M133 plan: defect coefficient no-valley frontier

Date: 2026-08-13 UTC.

## Objective

Continue the independently accepted M125/M129 exact coefficient reduction for
the M113/M118 auxiliary incidence law.  The primary target is the universal
ordinary log-concavity inequality

```text
H[d,c]^2 >= H[d,c-1] H[d,c+1]
```

for `d>=4` and `3<=c<=d-1`.  A permissible weaker target is a rigorous
single-crossing/no-valley theorem for `c -> H[d,c]` sufficient for the exact
defect birth-death projection of M120/M124.

## Target, convention, and scope

The target is the auxiliary law `rho(kappa)=|C_kappa|/Z_inc` on realizable
connected-unicyclic incidence keys.  Write `R=d-c(p)` and
`M[d,r]=sum_{R(kappa)=r}|C_kappa|=H[d,d-r]`.  Permutations compose as
`(pq)(x)=p(q(x))`, with word factors multiplied left-to-right.  This mission
does not alter or sample the original uniform identity-word law.

Imported proved inputs are exactly the M113/M118 cell formula, M120/M124
directional defect rates, and M125/M129 rooted coefficient recurrence.
Ultra-log-concavity and real-rootedness are treated as refuted at `d=4`.

## Work plan

1. Re-express the subtractive connected extraction as a positive structural
   decomposition whenever possible (core cycle with attached trees,
   exponential/logarithmic species, or renewal representation).
2. Derive exact coefficient or ratio recurrences across the cycle-count
   index `c`; search for an injection, total-positive kernel, or
   single-crossing criterion.
3. Use exact arithmetic only to falsify candidate universal claims and to
   identify minimal boundary cases or asymptotic counterfamilies.  Finite
   verification will not be promoted to a theorem.
4. If full log-concavity cannot be closed, freeze the first strict positive
   reduction or a minimal universal obstruction, with every conditional
   implication stated beside its missing hypothesis.

## Expected failure modes

- connected extraction remains subtractive after the chosen transform;
- the positive unicycle-core representation has weights that do not preserve
  log-concavity under convolution;
- ordinary log-concavity eventually fails, while unimodality survives;
- a ratio bound controls only a proper subclass of cycle types or cuts;
- finite exact signs are mistaken for an asymptotic proof.

## Reproducibility

All new computation will be deterministic (`seed=null`) under the repository
Python environment and will write machine-readable JSON in this directory.
The final package will contain a halfway checkpoint, proof note, 9-field
report, scripts, raw output, freeze manifest, and SHA-256 inventory.
