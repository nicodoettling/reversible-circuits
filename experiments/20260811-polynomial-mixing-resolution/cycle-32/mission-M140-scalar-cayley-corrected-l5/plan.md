# M140 plan: scalar Cayley bound and corrected auxiliary L=5 theorem

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact target

Work only on the auxiliary full nonlazy stationary-flow parking-degree
projection in the minimal-long-cycle sector.  First prove the standalone
scalar statement

```text
C_s <= 3/4 for every integer s>=100,

C_s=sum_(k=2)^s sum_(A=1)^(s-k+1)
 [w_A c(s-A,k-1)/(k! w_(s+1))] k lambda(A,k)^2.
```

Then combine it with the independently audited, corrected M138 envelope

```text
R_corr=q[C_s-sum_E a_E lambda_E]
       +sum_E theta_E^2/(q c_E)
```

to prove the complete auxiliary right-heavy suffix-excess-five inequality

```text
H(s,K,K-1,s-5)<=q(1-q),
q=w_6 w_(s-5)/w_(s+1), s>=6, K>=1.
```

Never use the rejected frozen display with `a_E lambda_E^2`.  Every
attachment rank remains present.  The project target remains uniform on
fixed-length identity transposition words, but this mission proves only an
auxiliary recurrence theorem; it does not prove a gap, ROOT-MEAN LIFT,
polynomial mixing, Terminal A, or Terminal B.  Permutations compose as
`(pq)(x)=p(q(x))`, factors left-to-right.

## Proof route

1. Rewrite `C_s` with endpoint weights
   `m_s(A,k)=k w_A c(s-A,k-1)/(k!w_(s+1))`.
2. Derive from `T=ze^T` the exact first-moment identity
   `sum_A m_s(A,k)lambda(A,k)=P[Bin(s-1,1/(s+1))>=k-1]`.
3. Bound `lambda(A,k)<=L_k`, where
   `L_k=(k-1)! sum_(p>=1)p/(p+k-1)!`, and dominate the binomial by
   `Pois(1)` through Bernoulli-to-Poisson coupling.
4. Evaluate the resulting universal majorant
   `U=sum_k L_k P[Pois(1)>=k-1]` as an elementary integral/series and
   prove the rational bound `U<409/500`.
5. Recover a finite correction by the exact identity
   `lambda^2=L_k lambda-lambda(L_k-lambda)` on
   `F={(2,A):1<=A<=4;(3,A):1<=A<=4;(4,1)}`.  Prove the required uniform
   lower bound for `m_s(A,k)` with elementary logarithmic estimates and check
   the correction normalization exactly.
6. Rebuild or cite with exact immutable provenance the 1222 finite and 4212
   tail Bernstein certificates for the corrected one-power L=5 envelope.

## Falsification and reproducibility

Use a standalone Python 3.12 standard-library checker with exact
`fractions.Fraction` arithmetic, deterministic `seed=null`, and no imports
from M131 or M138.  Check the first-moment identity in finite cases, the
binomial/Poisson stochastic order, the integral/series identities, every
rational margin, the fixed-mass log bound on its full parameter range, and
the corrected subtraction normalization.  Record a halfway checkpoint,
proof note, machine-readable JSON, nine-field report, freeze manifest, and
SHA-256 inventory.  M131 and M138 remain immutable.

Expected failure modes: a factorial/index shift in the tree-EGF identity; a
wrong Poisson parameter direction; loss of the `99/100` factor in the finite
correction; a log remainder that is not uniform at `n=96,q=5,k=4`; or reuse
of the rejected two-power exceptional subtraction.
