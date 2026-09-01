# M170 final report: fresh referee of frozen M167

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTION 1: The frozen theorem note's Section 6 ends
  mid-statement. It is citable for complete Theorems 3.1/4.1 and Section 5,
  while report.md Field 7 is the source for the unresolved aggregated
  modal-vector target.
NONMATERIAL CORRECTION 2: The eta majorant is true, but the displayed product
  proof needs a separate r=n line: eta_(n,n)=1/(n+2)^n<=n/(n+1)!.
```

M167's three mathematical obstruction claims are accepted with their stated
operator-level scope. The universal all-suffix `T_1` boundary remains
unresolved.

## Field 2 — immutable provenance, target, and convention

The supplied frozen hashes match exactly:

```text
d18ed32964935b0a58f236b04464be847fe673d24bb37ad3c11b409ba78f0997  report.md
ba552a74790df708d06e94066dfe3aa784c5c4eae5eb3e602490f2e3999ac627  operator_obstruction_theorem.md
4e7dd6a68de760d07e6ba1202ff3699210170eb8260d797b505bd55e200df4ec  freeze_manifest.md
```

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, displayed factors left-to-right.
The audit concerns only the auxiliary normalized excursion `F=H/q`; there is
no sampler claim.

## Field 3 — exact child-first-mode leakage

For `U~Beta(1,b)`, degree `d=1`, retained `a=0`, and killed `a=1`, let

```text
f(u)=u-1/(b+2),
g(u)=(1-u)f(u)/sqrt(b/(b+1)).
```

Exact beta moments independently give

```text
Q_(b+1)(f)=0,
||f||^2=(b+1)/[(b+2)^2(b+3)],
Q_b(g)=4(b+1)/[(b+2)^2(b+3)^2(b+4)],
Q_b(g)/||f||^2=4/[(b+3)(b+4)].
```

At the smallest `b=1`, these are `0`, `1/18`, `1/90`, and `1/5`. The
normalization and leakage coefficient are correct.

## Field 4 — exact retained constant-child formula

For the fresh uniform law and normalized Bernstein coordinates `e_a`, exact
integration gives M167's coordinate formula and retained sum

```text
R_d
 =(d+1)/(2d+1)[4^d/binom(2d,d)-1]
  -d/(d+2)+3d^2/[(d+1)(d+2)^2].
```

The retained constant energy is `d/(d+1)`, the genuine high tail is
`R_d-d/(d+1)`, and the killed mass is `1/(d+1)`. The smallest rows are
`R_1=1/2` with zero genuine high tail and `R_2=3/4` with high tail `1/12`.
The central-binomial expansion yields

```text
R_d=sqrt(pi*d)/2-3/2+O(d^(-1/2)),
```

which verifies M167's stated `o(1)` remainder and divergence conclusion.

## Field 5 — exact logical reach

The degree-one example proves that child scalar `T_1` does not determine the
shared-observation transfer and refutes zero-preserving/homogeneous scalar
closures that discard child first-mode energy. It does not refute every
scalar inequality equipped with an external mode budget.

The `R_d` family refutes degree-uniform branch-local bounds
`high tail<=C*pi_d` and even uniform `O(1)` retained-total bounds. These are
operator-level constant-child coordinates, not a simultaneous actual-history
counterexample. Neither family refutes the universal all-suffix boundary or
an aggregated modal-vector proof.

## Field 6 — exterior eta bound and summability

For `1<=r<=n`, the exact terminal coefficient is

```text
eta_(n,r)
 =r n^(n-r-1)(n+2)!/
  [(n-r)!(r+1)!(n+2)^(n+1)].
```

For `r<=n-1`, M167's product comparison proves
`eta<=r/(r+1)!`. For `r=n`, the separate calculation in nonmaterial
correction 2 proves the same bound. The exceptional `(n,r)=(0,0)` has
`eta=1` but degree `d=1` and zero genuine high tail. For fixed `r`,

```text
eta_(n,r)->e^(-2)r/(r+1)!.
```

Since `R_(r+1)=O(sqrt(r+1))`, the exterior aggregate is uniformly dominated
by the convergent factorial series
`sum r sqrt(r+1)/(r+1)!`. M167 correctly rules out a harmonic obstruction.

## Field 7 — surviving aggregated modal-vector scope

The surviving statement is unresolved and is fully stated only in frozen
M167 `report.md` Field 7. It must retain each child decomposition

```text
Phi_child=M_child
 +(u-p_child)C_child/sigma_child^2+Z_child,
```

with the orthogonality constraints on `Z_child`, exact vector cross terms,
all retained shared observations, and exact omission of killed `a=d`. Only
after summing the exterior coefficients may one seek the parent budget. The
truncated theorem-note Section 6 is not a standalone citation for this lemma.

## Field 8 — independent exactness and process audit

`independent_exact.py` uses Python 3.12.3 standard-library `Fraction`, no
randomness, and no predecessor code. It checks only selected exact smallest
and boundary cases; all assertions pass, with output in
`independent_results.json`. Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-39/mission-M170-m167-fresh-referee/independent_exact.py
```

No `L=7` or broad scan was run. `ps -p 1677566` found no live process, and
the frozen M167 inventory contains no retained diagnostic output or cache.
This verifies current stopped-PID/no-retained-output scope, not unrecoverable
ephemeral history.

## Field 9 — artifacts, hashes, hygiene, and prohibited inferences

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_exact.py`,
`independent_results.json`, `proof_audit.md`, this report,
`freeze_manifest.md`, and `SHA256SUMS`. The freeze manifest records payload
hashes; the final ledger verifies them.

Only this M170 directory was edited. M167 remained immutable. No predecessor,
coordinator, manuscript, project skill, package, configuration, commit, or
remote state was changed. No actual-history counterexample, auxiliary gap,
`ROOT-MEAN LIFT`, original-chain gap, polynomial mixing result, Terminal A,
or Terminal B is claimed.
