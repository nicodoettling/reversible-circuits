# M177 final report: fresh referee of M173

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT M173'S STRICT FRESH TERMINAL-SECTOR THEOREM.
PROVED: exact six-term actual-history AMV retained-branch recursion.
REFUTED: closure on (M,C,||Z||^2) or scalar child T_1 alone.
PROVED: fresh terminal constant-child aggregate <=1/4.
PROVED: actual-history live h=1 charge <=(1-q_0)/4 for L>=2,
        with the separate L=1 bound (1-q_0)/2.
UNRESOLVED: reset plus h>=2 AMV budget and universal all-suffix T_1.
```

No material objection was found. Two nonmaterial wording/scope cautions are
recorded in Field 7.

## Field 2 — integrity, target, and convention

M173's complete `SHA256SUMS` ledger passed before substantive reading, and its
manifest inventory matched. I did not edit M173. The project target remains
the uniform fixed-length identity-transposition bridge law, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right. This audit concerns
only `F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| AMV terminal sector | fresh auxiliary right-heavy `T_1` boundary | N/A | N/A | independent beta/Jacobi and Cayley rational audit | accept scoped theorem |

## Field 3 — AMV recursion

Bayes' identity gives the sensitive normalization

```text
(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_child[L_a||Phi_a||^2].
```

Expanding `Phi=M+(u-p_a)C/sigma_a^2+Z` yields all six M173 terms, including
the three vector cross terms. The parent covariance is exactly
`sqrt(eta*pi_a)(delta M+C)`, so the subtraction retains
`2delta<M,C>`. The killed observation `a=d` is absent, without survival
conditioning. An independent asymmetric two-coordinate rational audit passes
the trace, all six terms, covariance subtraction, and total `T_1` identity.

## Field 4 — finite-summary obstruction

The unit-normalized degree-two and degree-three Jacobi modes under
`Beta(1,2)` both have `(M,C,||Z||^2,T_1)=(0,0,1,1)`, while their lifted
charges are exactly `18/35` and `32/63`. This proves unrestricted-operator
nonclosure of the named summaries. It is not an actual-history counterexample.

## Field 5 — analytic terminal operator bound

M173's central-binomial argument proves `R_d<=3d/8` for all `d>=2`: the
ratio induction gives `4^d/binom(2d,d)^(-1)<=2sqrt(d)`, the analytic tail
starts at `d=8`, and the exact rational bases `d=2,...,7` all pass. Equality
occurs only at `d=2`.

The binomial theorem, including `r=n`, gives exactly

```text
sum_(r=1)^n (r+1)eta_(n,r)=((n+1)/(n+2))^n<=2/3.
```

Consequently `sum eta_(n,r)R_(r+1)<=1/4`, with equality at `n=1` and strict
inequality thereafter.

## Field 6 — actual-history `h=1` normalization

For fresh `s=B+L`, `h=1`, `n=L-1`, and `d=r+1`, independent cancellation
gives

```text
m_s=w_(B+1)c(n,r)/[(r+1)!w_(B+L+1)],
q_child/q_parent=w_(B+L+1)/[w_(B+1)w_(n+2)],
eta=m_s q_child/q_parent=c(n,r)/[(r+1)!w_(n+2)].
```

There is no extra split, observation, `q_0`, or parent-`q` factor. For each
retained observation the exact constant-child charge is
`eta Q(e_a)||M_a||^2`, and `Q(e_a)>=0` as an orthogonal-projection residual.
Thus observation-dependent norms may be dominated coordinatewise by their
maximum before summing to `eta R_d`; no common-vector assumption is used.

Every retained child has suffix excess zero and `(K',R')=(d+1,d-a)`.
M109/M114 therefore gives `||M_a||^2<=1-q_0` for `B>=2`; `B=1` is inactive.
This proves the accepted `(1-q_0)/4` actual-history bound.

## Field 7 — numbered objections, dependencies, and limitations

1. **Material objections: none.** All claims in the frozen disposition pass.
2. **Nonmaterial exposition:** positivity is of each `Q(e_a)` projection
   residual, not of each algebraic summand in the closed formula for `R_d`.
   M173's maximum domination is nevertheless correct.
3. **Nonmaterial boundary wording:** for `B=1`, the `h=1` root is already
   excluded by the live-rank condition; calling the would-be child inactive
   has the same zero effect.
4. **Limitation:** accepted dependencies M109/M114, M162/M165, and M167/M170
   are essential. The theorem does not include the reset term, any `h>=2`
   branch, a nonfresh parent, a total AMV inequality, a gap, or Terminal A/B.

The first unresolved lemma remains M173's exact fresh-parent aggregate of the
reset and all `h>=2` branches with the full weighted `Z_0,Z_1,Z_2` data.

## Field 8 — reproducibility

Run from this M177 directory:

```text
python3 -B independent_exact.py --output independent_results.json
```

Python 3.12.3, standard library only, deterministic `seed=null`. The checker
imports no M173 or predecessor code. It performs one asymmetric six-term AMV
audit, both Jacobi witnesses, the six `R_d` bases, one varying-observation max
test, five selected exterior cancellations including `r=n`, four aggregate
rows, and the `L=1` row. It reports `status=pass`, `failures=[]`. This is a
compact algebra audit, not a broad scan; the universal statements rest on the
proof in `proof_audit.md`.

## Field 9 — boundaries, artifacts, and hygiene

The killed atom `a=d`, `L=0` absent first mode, `L=1,d=1`, `B=1`, and
`r=n` boundaries are all explicit. Original-chain cases `m` odd, `m=0,2`,
and `N=2` receive no new conclusion.

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_exact.py`,
`independent_results.json`, `proof_audit.md`, this report, the freeze manifest,
and `SHA256SUMS`. No package, configuration, commit, remote, predecessor,
coordinator, manuscript, or project-skill file was changed.

