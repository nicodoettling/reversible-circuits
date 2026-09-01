# M07 plan: Hurwitz rate curvature

Date: 2026-08-11  
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Objective and exact claim

For a fixed labeled `v`-set let `C(v,k)` count connected identity
transposition words of length `k`, and set

```text
a_v(g)=C(v,2(v-1)+2g)/[2(v-1)+2g]!,
rho_v(0)=0,
rho_v(g)=a_v(g-1)/a_v(g)  (g>=1).
```

Composition is `(pq)(x)=p(q(x))`.  Attack the universal claim

```text
rho_v(g+1)-rho_v(g) >= c(v+g+1)^(-A)
```

for some universal `c>0,A<infinity`, all `v>=2,g>=0`.  An exact negative
increment refutes this claim.  If refuted, immediately analyze the exact
same-law uniform-destination zero-range allocation chain; curvature failure
alone is not a global sampler refutation.

## Proof lanes

1. Audit DYZ Proposition 1, equations (13)--(18), including the relation
   between their cover normalization and fixed-labeled word counts.
2. Derive a large-genus quantitative estimate from the exact character
   formula plus support-exclusion, retaining errors small enough to compare
   two adjacent ratios rather than only their sizes.
3. Study the positive fixed-degree polynomial representation
   `C_d(x)=gamma_d(4sinh^2(x/2))/d` and its central-factorial coefficient
   kernel for log-concavity/total positivity.  Use a preservation theorem
   only after checking its literal hypotheses.
4. Run scalable exact and high-precision falsification using both the DYZ
   recurrence and an independent character/component computation.  Every
   finite run is labeled as a falsification attempt, never a proof.
5. If curvature fails, compute exact zero-range conductance/gaps for the
   smallest induced allocation systems and seek an asymptotic cut with both
   mass and flow.

## Calibration and expected failure modes

- `v=2`: `C(v,k)=1`; `rho_2(0)=0`, while
  `rho_2(g)=k(k-1)` exactly for `g>=1`;
- `C_0(2)=1`, `C_0(3)=24`, `C_0(4)=2880`;
- `rho_4(1)=16/13`, `rho_4(2)=195/82`;
- M12 proves `rho_v(g)>=12/v^3`, not monotonicity;
- ultra-log-concavity fails at `v=4,g=1`, while ordinary curvature is
  positive there;
- fixed-degree asymptotics without a uniform adjacent-ratio error do not
  establish curvature;
- a negative increment refutes only this sufficient route;
- `G=0` allocation restrictions are singletons.

## Reproducibility

All scripts will be deterministic, use exact integer/rational arithmetic
where feasible, state the universal claim they can falsify, record Python and
dependency versions, and write machine-readable output in this directory.
