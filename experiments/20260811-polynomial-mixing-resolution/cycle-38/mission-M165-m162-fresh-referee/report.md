# M165 final report: fresh referee of frozen M162

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CLARIFICATION: At L=0, define the absent A_1 mode as zero or
state the trivial boundary separately.
```

M162 correctly proves an explicit actual-history feature map, finite vector
Parseval and all truncated Jacobi upper bounds, and the exact first-mode
recursion.  Its four right-heavy trace-repair rows are exact.  The result does
not prove the all-suffix boundary or any gap.

## Field 2 — immutable provenance

All supplied frozen hashes match exactly:

```text
f0916943bbd47b9245bf8171e3598ee1e3aeb50f9e54d036c49c6ff898fd02a7  report.md
989d83d74038a7734e79883b56ea5cd285b28d1e3648216c8fa8a5f7e12a3862  vector_beta_theorem.md
4347755c5dac4751534514d9ae43133a9fd0d299bbd7ada875671a651d769094  vector_beta_exact.py
fc4b0506e14a044fa0727e08f67d70f3c8caccc77b186184b78fe20ce3b325d3  vector_beta_exact.json
2dc7b122eb9ee19af9a0f5998e24833c0d72b6f800eee54d3c6d8e269eea6031  freeze_manifest.md
```

M162's complete `SHA256SUMS` also verifies.

## Field 3 — feature normalization and shared observation

For a retained observation `a<d`, the feature scale

```text
sqrt[(m_s(d,t) q_child/q_parent)/pi_a] L_a Phi_child
```

has exactly the accepted M157/M160 Gram coefficient.  Bayes converts its mean
to `sqrt(eta*pi_a)M_child`, so its normalized scalar contribution is
`eta*pi_a F_child`.  This independently confirms the child/parent `q` ratio,
the single `pi_a` denominator for one shared observation, and exact omission
of killed `a=d`.  The reset scaling `J_E/sqrt(qc_E)` likewise gives exactly
`A_0/q`.

## Field 4 — Jacobi and first-mode audit

The shifted parameters are correctly ordered as
`(alpha,beta)=(kappa-D-1,D-1)` under the standard
`(1-z)^alpha(1+z)^beta` convention.  Finite vector Parseval gives

```text
T_r=F+sum_(n=r+1)^L ||A_n||^2 >= F.
```

For the first mode, Bayes yields

```text
eta*pi_a/Var_parent * ||(p_child-p_parent)M_child+C_child||^2.
```

The formula correctly retains `2 delta<M,C>` and omits the killed branch.
The only notation issue is harmless: for the open statement at `L=0`, extend
the missing `A_1` by zero or separate that trivial case.

## Field 5 — clean-room finite check

The standard-library checker uses exact `Fraction` arithmetic, no randomness,
and no predecessor imports.  It represents the Gram kernel as rational
weighted univariate history features, rather than reusing M162's bivariate
kernel implementation.  It evaluates only the four decisive rows.

| state | trace | degree-one energy | `T_1` | budget |
|---|---:|---:|---:|---:|
| `(8,2,1,2)` | 0.81369335 | 0.32053466 | 0.49315869 | 0.80322013 |
| `(7,2,1,3)` | 0.85528212 | 0.30754586 | 0.54773626 | 0.84979630 |
| `(8,2,1,3)` | 0.93988222 | 0.33818353 | 0.60169870 | 0.86343545 |
| `(9,2,1,3)` | 1.00558139 | 0.36121508 | 0.64436630 | 0.87293908 |

All exact frozen fractions match.  There are zero failures across 42 compact
shared-observation monomial checks, two asymmetric Jacobi convention rows,
four scalar/feature normalizations, four diagonal recursions, four complete
modal Parseval decompositions, and four first-mode recursions.

Run from the M165 directory:

```text
python3 -B independent_referee.py
```

The deterministic result has SHA-256
`ea843d189ceabfc8579727047a7c923ef589989e9f70b5414a70d5b5d95e72a1`.

## Field 6 — accepted scope and open frontier

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right.  M162 concerns
only the auxiliary normalized full unweighted reset excursion.  The universal
all-suffix claim

```text
T_1(B,L,kappa,1)<=1-q_(B,L)
```

remains open, as do all-suffix contraction, the auxiliary gap,
`ROOT-MEAN LIFT`, the original lazy `{3,4,5}` heat-bath gap, polynomial
mixing, Terminal A, and Terminal B.

## Field 7 — hygiene

Only the owned M165 directory was edited.  No predecessor, coordinator,
manuscript, project skill, package, configuration, commit, or remote state
was changed.  The repository-level `references/experiments.md` named by
`AGENTS.md` is absent; the audit used the existing skill-owned
`.codex/skills/reversible-circuit-sampler/references/experiments.md`.
