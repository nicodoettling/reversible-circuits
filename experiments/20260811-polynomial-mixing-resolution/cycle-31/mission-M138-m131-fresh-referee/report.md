# M138 fresh referee report on frozen M131

Date: 2026-08-13 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
FINAL VERDICT: REJECT AS FROZEN.
MATERIAL NUMBERED OBJECTIONS: ONE.
NONMATERIAL CORRECTIONS: NONE.
```

**M-1.** Frozen proof equation (5.1) subtracts supported exceptional mass
times `lambda(E)^2`, but frozen `l5_exact.py` subtracts it times
`lambda(E)`.  The positive finite and tail certificates belong only to the
implemented one-power formula.  The written two-power envelope exceeds its
target at exact finite points and has negative Bernstein coefficients.

The one-power subtraction is rigorously valid and the corrected conditional
theorem is independently salvaged below, but this referee does not promote a
corrected theorem from an immutable rejected payload.  Lemma C is not
attempted and remains unresolved.

## Field 2 — target, convention, and scope

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.
The audited statement is only

```text
H(s,K,K-1,s-5)<=q(1-q),
q=w_6 w_(s-5)/w_(s+1), s>=6,K>=1,
```

for the auxiliary full nonlazy stationary-flow parking-degree reset
recurrence.  It is not an auxiliary gap, ROOT-MEAN LIFT, original-chain gap,
mixing theorem, Terminal A, or Terminal B.

## Field 3 — provenance and dependency audit

All supplied M131 hashes match, including report
`129326b3...70eb3`, proof `b4b22d9f...c1628`, checker
`f8a77e8...f724`, results `ad8779c8...217`, manifest
`db81797b...69c`, and inventory `20b239f7...96f7`.  Every checksum inventory
for M109/M114, M115/M116, M117/M121, and M123/M128 passes.

The positive dependency chain is correctly scoped: M109/M114 supply the
finite-DAG recurrence and lower sectors; M115/M116 and M117/M121 supply the
arbitrary-deficit `L=1,2` envelopes and right-heavy contraction through
`L=4`.  M123/M128 only delimit discarded generic frame routes, which M131
does not reuse.

## Field 4 — root, basin, live-rank, and boundary audit

Independent ordered-composition reconstruction confirms exactly:

```text
32 supported roots;
31 nominal exceptional basins, 23 active and 8 inactive;
16 positive root groups;
11 live deep groups.
```

Every `j=1,...,k` is present before aggregation.  Literal full-basin counts
are 23 at `s=6` and 47 at `s=7`; all 23 active supported exceptional currents
and capacities match at `K=1,5`.  At `s=6`, the retained child count is 17,
exactly as listed by M131, while every nominal `t=2` child is rank one and
inactive.  No root-structure or boundary objection remains.

## Field 5 — arbitrary-deficit and Cayley-coefficient audit

The fresh checker derives the full `(a,D,k,j,z)` attachment law and recursively
constructs the arbitrary-deficit envelope through `L=3`.  It reproduces the
accepted closed `L=1` and `L=2` formulas exactly.  Across 504 contexts

```text
ell=1,2,3; ell+1<=S<=8; 2<=K<=8; 1<=R<K,
```

there are zero formula mismatches and zero exact-resolvent bound failures.

It independently derives

```text
lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!](A)_p/A^p,
lambda(A,2)=A/(A+1),
lambda(A,k)<=2A/[k(A+1)],
```

the endpoint-degree marginal, and the exact `C_s` sum.  Literal basin ratios
and the endpoint marginal have zero failures.  `C_100` agrees exactly with
M131 and is approximately `.7145417887532552`; it is finite falsification
data only.

## Field 6 — decisive refined-subtraction objection

For each nominal exceptional endpoint define

```text
c_E=degree(E)rho(E),
b_E=rho(B_E)=c_E lambda_E,
a_E=rho(B_E intersect supported roots)<=b_E.
```

The ordinary contribution after division by `q` is `q b_E lambda_E`.
Therefore subtracting `q a_E lambda_E` is safe, and the implemented corrected
reset envelope is

```text
R_corr=q[C_s-sum_E a_E lambda_E]
       +sum_E theta_E^2/(q c_E).
```

The proof instead displays `a_E lambda_E^2`.  That remains an upper bound but
is looser and does not receive the asserted sign certificate.  At
`(s,K)=(6,64)`, its normalized value is exactly

```text
239164429690896046891371756674
/218369158864796713280022140625 > 1.
```

At `s=6`, its Bernstein coefficient at index two is

```text
-19717205656843140443/125254786225637376000 < 0,
```

and four coefficients are nonpositive.  This is a proof/certificate failure,
not an `H` counterexample.

## Field 7 — corrected certificates and conditional implication

Using the proved one-power subtraction, the independent checker evaluates at
nodes inside each certified interval and inverts the Bernstein evaluation
matrix exactly.  This is independent of M131's integer-node Lagrange route.

- All 1222 finite coefficients for `s=6,...,99` are positive.  The minimum is
  `5307578203959502651/4736091661711441920000` at `s=7`, index zero.
- Under `C_s<=3/4`, with path heights replaced by one, the corrected tail
  polynomial has multidegree `(1,1,2,2,2,2,12)`.  All 4212 coefficients on
  `[4/11,187/500]^6 x [0,1/2]` are positive.  The minimum is
  `4360847276079323/50118750000000000000` at `(1,1,2,2,2,0,0)`.
- Exact off-grid identities pass.  All 1222 and all 4212 coefficient fractions
  match M131's frozen checker output after using the correction.  The 504
  child rows, 20 selected `L=5` rows, and six selected `C_s` values also match.

The ratio box contains every `s>=100` tuple: the Cayley ratios decrease,
`b_n>1/e>4/11`, and the exact comparison
`500*95^94<187*96^94` gives `b_95<187/500`.  Replacing `C_s` by `3/4` and
each height by one enlarges the corrected envelope by positivity and
induction.  Thus the corrected conditional implication is salvaged, but not
promoted here.  Lemma C itself stays open.

## Field 8 — retained negative and rational checks

The inherited coarse `beta<=degree` envelope is indeed refuted only as a
certificate.  At `(7,4096)` its normalized value is
`1.0194850323300793...`, while actual `H/[q(1-q)]` is
`.40251029996439475...`; both exact fractions match M131.

The `e` correction is sound.  The exact upper estimate

```text
1957/720+1/4410=31967/11760<87/32
```

implies `2(3-e)>9/16`, refuting the tempting opposite sign.  The strict lower
bound `e>163/60` gives `2(3-e)<17/30`.  Neither proves Lemma C.

## Field 9 — reproducibility, disposition, and hygiene

The independent implementation imports no predecessor source and uses Python
3.12.3, standard-library `fractions.Fraction`, no nonstandard dependencies,
and `seed=null`.  Reproduce from this directory with

```text
python3 -B independent_m131_referee.py \
  --output independent_m131_referee.json \
  --reference-json ../../cycle-28/mission-M131-suffix-excess-five/l5_exact.json
```

The fresh mathematical payload is constructed before the optional post-hoc
reference is opened.  It reports zero corrected-formula failures and one
frozen-artifact objection.

```text
FINAL VERDICT: REJECT AS FROZEN.
M-1: proof uses lambda^2; certified source uses the valid sharper lambda.
CORRECTED AUXILIARY THEOREM: independently salvaged, not promoted.
LEMMA C: unresolved and not attempted.
```

No M131, predecessor, coordinator, manuscript, project-skill, or other worker
file was edited.  No package was installed and no stochastic conclusion is
used.
