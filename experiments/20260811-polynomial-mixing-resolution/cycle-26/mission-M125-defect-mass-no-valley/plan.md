# M125 plan: exact defect-mass no-valley

Date: 2026-08-12 UTC.

## Objective and exact target

Study the auxiliary stationary law

```text
rho(kappa)=|C_kappa|/Z_inc
```

of the exact connected-unicycle incidence chain `A_d` from M113/M118, not
the original uniform identity-word law.  For a realizable key
`kappa=(j,p,Q_L,Q_R)` on `[d]`, put `R(kappa)=d-c(p)` and

```text
M_{d,r}=sum_{R(kappa)=r}|C_kappa|,
mu_{d,r}=M_{d,r}/sum_s M_{d,s},       0 <= r <= d-2.
```

The primary statement to prove or refute is:

> **DEFECT NO-VALLEY.**  For every integer `d>=3`, the finite sequence
> `(mu_{d,0},...,mu_{d,d-2})` is unimodal.

The preferred stronger target is log-concavity
`M_{d,r}^2 >= M_{d,r-1}M_{d,r+1}`.  Normalization is immaterial.

## Exact inputs and conventions

Use M113's realizability criterion and exact cell formula

```text
|C_kappa|=j!(2d-j)!
  product_{B in Q_L union Q_R}|B|^(c_B-3)
  product_{a cycle of p}[|a|^|a|/(|a|-1)!]^2,
j=d+|Q_R|-|Q_L|,
```

where `Q_L,Q_R` coarsen the cycle partition of `p` and their bipartite
cycle-incidence multigraph is connected and unicyclic.  Permutations compose
as `(pq)(x)=p(q(x))`, with word factors multiplied left-to-right.  The cell
formula and target are already convention-audited in M118.

## Work program

1. Read the complete relevant M113/M118/M120/M124 reports, proof notes, and
   exact audit code/data; reconstruct the defect coefficient sum from the
   exact cell formula.
2. Derive an exact labeled-species / exponential generating function by
   separating permutation-cycle atoms, the two colored set partitions, and
   connected-unicyclic bipartite incidence structures.  Record a coefficient
   formula or finite recurrence that reproduces the audited masses.
3. Implement a deterministic exact-arithmetic coefficient engine independent
   of full key enumeration.  Cross-check `d<=5` against frozen mission data and
   the coordinator-provided primitive integer rows for `d=6,7` (up to a common
   gcd/normalization).
4. Test candidate coefficient recurrences, total-positivity/ULC inequalities,
   and minimal/boundary cases.  Explicitly avoid a real-rootedness argument,
   since the defect polynomial is already non-real-rooted at `d=4`.
5. Either give a universal proof, give an exact counterexample `(d,r)`, or
   isolate and prove/refute one standalone coefficient recurrence or ULC
   lemma that strictly narrows DEFECT NO-VALLEY.

## Boundary cases and falsification

- `d=2` has the one-state sequence and is recorded only as an exception; the
  assigned universal statement starts at `d=3`.
- Check both ends `r=0,d-2`, all internal log-concavity inequalities, exact
  integrality/denominators, left/right color symmetry, and agreement of total
  coefficient normalization.
- Finite verification will be labeled exact finite evidence, never a proof of
  the universal statement.
- A proof must keep every unproved analytic/combinatorial dependency next to
  the conclusion using it.

## Expected failure modes

- The connected-unicyclic condition may resist a positive species
  factorization after the factorial cut tilt `j!(2d-j)!`.
- A natural recurrence may have mixed signs or fail to preserve
  log-concavity/ULC.
- The sequence may remain log-concave in computed cases without a closed
  preservation theorem; in that event the deliverable will be a rigorously
  proved/refuted named coefficient lemma, not an extrapolation from finite
  data.
- Even a proved no-valley lemma yields only M120's conditional defect
  projection gap; it does not prove `gap(A_d)`, the fixed-defect restriction,
  or the terminal heat-bath mixing claim.

## Reproducibility deliverables

Create `checkpoint.md`, proof/derivation notes, deterministic exact code,
machine-readable raw output, a nine-field `report.md`, and `SHA256SUMS`.
Record the repository commit, exact commands, Python version, dependencies,
and `seed=null`.  Edit no file outside this mission directory.
