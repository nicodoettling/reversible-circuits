# M138 halfway checkpoint

Date: 2026-08-13 UTC.

## Exact reconstruction completed

The fresh no-predecessor-import checker reconstructs the root law, contextual
means, canonical basins, attachment ranks, literal finite DAG, arbitrary-
deficit envelopes, Cayley coefficient, and both Bernstein transforms.

It confirms:

- 32 supported `L=5` rows, 31 nominal exceptional basins, eight inactive
  endpoints, 16 positive groups, and 11 live groups;
- literal active-basin counts 23 at `s=6` and 47 at `s=7`, with all 23 active
  exceptional currents/capacities matching;
- exactly 17 retained children at `s=6`, with every nominal `t=2` child
  inactive and every `j=1,...,k` otherwise present;
- 504 arbitrary-deficit `L=1,2,3` finite rows with zero bound failures, and
  exact equality of the generic `L=1,2` formulas to the accepted predecessor
  envelopes;
- the displayed `lambda(A,k)`, `lambda(A,2)=A/(A+1)`, the coefficient bound,
  endpoint marginal, and exact `C_s` values, including the frozen rational at
  `s=100`.

## Material frozen-artifact discrepancy

M131 proof equation (5.1) subtracts supported exceptional basin mass times
`lambda(E)^2`.  Frozen `l5_exact.py` line 372 instead subtracts the mass times
`lambda(E)`.

These are not interchangeable for the certificate.  The written
`lambda^2` envelope is a valid but looser upper bound and fails the target,
for example at `(s,K)=(6,64)`, where its normalized value is
`239164429690896046891371756674 / 218369158864796713280022140625 > 1`.
Its exact `s=6` Bernstein coefficient at index two is

```text
-19717205656843140443/125254786225637376000 < 0.
```

The implemented `lambda` subtraction is nevertheless valid: if `a_E` is the
supported exceptional mass, `b_E` the full basin mass, `c_E` the capacity,
and `lambda_E=b_E/c_E`, then `a_E<=b_E` and the ordinary contribution is
`q b_E lambda_E`; hence subtracting `q a_E lambda_E` is safe.  With this
corrected display, the independent checker reproduces all 1222 finite and
4212 conditional-tail coefficients exactly, with zero nonpositive entries.

The final report will distinguish rejection of the frozen displayed proof
from the independently repaired conditional reduction.  Lemma C remains
unattempted and unresolved.
