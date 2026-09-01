# M167 final report: all-suffix first-Jacobi boundary

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: FREEZE STRICT OBSTRUCTION REDUCTION FOR FRESH AUDIT.
UNRESOLVED: T_1(B,L,kappa,1)<=1-q_(B,L) for all B,L,kappa.
PROVED: scalar child-T_1 induction cannot close under the exact
        shared-observation transfer.
PROVED: no degree-uniform branch-local charge of retained high modes to the
        killed atom can hold.
PROVED: the terminal exterior Cayley weights factorially suppress that local
        obstruction, so it does not yield an actual-history counterfamily.
```

The requested universal theorem has neither been proved nor refuted. The
deliverable is a strict reduction to an aggregated modal-vector inequality
which must retain child constant, first, and high-mode data.

## Field 2 — scope, target, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right. This mission concerns only `F=H/q`, the normalized full
unweighted reset excursion of the auxiliary nonlazy minimal-long-cycle
parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| all-suffix first-Jacobi boundary | auxiliary right-heavy excursion budget | N/A: no sampler | N/A: auxiliary recurrence | exact algebraic counterfamilies and exterior summability | universal boundary unresolved; strict reduction kept |

No auxiliary gap, `ROOT-MEAN LIFT`, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing result, Terminal A, or Terminal B follows.

## Field 3 — accepted actual-history functional

For `b=kappa-1>=1`, let `mu_b=Beta(1,b)` and

```text
Q_b(f)=E_mu ||f(U)||^2
       -||E_mu[(U-1/(b+1))f(U)]||^2/Var_mu(U).
```

M162/M165's orthogonal history coordinates give exactly
`T_1=sum_gamma Q_b(phi_gamma)`. A retained shared observation has coordinate
`sqrt(eta/pi_a)L_(d,a)Phi_child`. All `a<d` are retained; `a=d`, equivalently
attachment rank `j=0`, is killed exactly and is never survival-conditioned.

## Field 4 — exact child-first-mode leakage

For degree `d=1`, retain `a=0` and kill `a=1=d`. Put

```text
f(u)=u-1/(b+2),
g(u)=(1-u)f(u)/sqrt(b/(b+1)).
```

The child law is `Beta(1,b+1)`, so `f` is a pure first Jacobi mode and its
child `T_1` is zero. Exact beta moments give

```text
Q_b(g)=4(b+1)/[(b+2)^2(b+3)^2(b+4)]>0,
||f||^2=(b+1)/[(b+2)^2(b+3)].
```

Thus the parent high-mode leakage from a unit child first mode is exactly

```text
4/[(b+3)(b+4)].
```

This infinite family proves that a recursion carrying only scalar child
`T_1` cannot dominate the exact transfer. At least child first-mode energy
and its vector relation to the constant/high parts must be retained.

## Field 5 — exact branch-local killed-atom obstruction

For the fresh law `Beta(1,1)` and degree `d>=1`, let

```text
L_a(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=1/(d+1),
e_a=L_a/sqrt(pi_a),       a=0,...,d-1.
```

The omitted `a=d` atom has mass `1/(d+1)`. Exact beta integration gives

```text
Q_1(e_a)
 =(d+1)/(2d+1) * binom(d,a)^2/binom(2d,2a)
  -3(2a-d)^2/[(d+1)(d+2)^2].
```

Using
`sum_(a=0)^d binom(d,a)^2/binom(2d,2a)=4^d/binom(2d,d)`, the retained total is

```text
R_d=sum_(a<d)Q_1(e_a)
 =(d+1)/(2d+1)[4^d/binom(2d,d)-1]
  -d/(d+2)+3d^2/[(d+1)(d+2)^2]
 =sqrt(pi*d)/2-3/2+o(1).
```

The retained constant energy is `d/(d+1)`, so the genuine degree-at-least-two
tail `R_d-d/(d+1)` also diverges. Therefore neither
`high tail<=C*pi_d` nor any degree-uniform `O(1)` branch-local charge is
possible. This is an operator-level counterfamily, not an actual-history
counterexample to the universal boundary.

## Field 6 — factorial exterior summability

For the terminal `h=1` branch, put `n=L-1` and `d=r+1`. Its exact normalized
exterior coefficient is

```text
eta_(n,r)=c(n,r)/[(r+1)! w_(n+2)]
 =r n^(n-r-1)(n+2)!/
   [(n-r)!(r+1)!(n+2)^(n+1)].
```

It satisfies `eta_(n,r)<=r/(r+1)!`, and for fixed `r`,

```text
eta_(n,r) -> exp(-2)r/(r+1)!.
```

Since `R_(r+1)=O(sqrt(r+1))`,

```text
sum_(r>=1) eta_(n,r)R_(r+1)
 <=sum_(r>=1) r sqrt(r+1)/(r+1)! < infinity
```

uniformly in `n`. Hence the local square-root growth is not a harmonic
actual-history obstruction. Exterior Cayley aggregation remains viable.

## Field 7 — surviving theorem target and limitations

The first surviving standalone lemma is the **AGGREGATED MODAL VECTOR
inequality**. Decompose every child feature as

```text
Phi_child=M_child
 +(u-p_child)C_child/sigma_child^2+Z_child,
E Z_child=E[(U-p_child)Z_child]=0.
```

One must prove the parent budget only after summing the exact quantities

```text
Q_parent(Phi_reset)
 +sum_(d,t,a<d) eta_(d,t)/pi_a
    Q_parent(L_(d,a)Phi_child)
 <=1-q_parent.
```

The vector cross terms among `M_child`, `C_child`, and `Z_child`, every shared
attachment observation, and the killed `a=d` branch must remain exact.
Fields 4–5 prove that neither child scalar `T_1` nor a branch-local killed
charge can establish this inequality. Field 6 proves only summability, not
the inequality.

## Field 8 — dependencies, exactness, and boundary audit

Accepted dependencies are M147/M151's all-suffix attachment recursion,
M157/M160's shared-observation signed kernel, and M162/M165's actual-history
feature map, Parseval identity, and exact first-mode recursion. The complete
M162 and M165 `SHA256SUMS` ledgers were verified before use.

The displayed counterfamilies and summability bounds are exact algebraic
proofs; no finite scan is their basis. No `L=7` enumeration was run. At
`L=0`, the absent first mode is zero-extended as M165 recommends, giving the
trivial base row. Pointwise Jensen, diagonal trace, generic frames, scalar
deficit-blind closures, and survival conditioning are not used.

One exploratory diagnostic inadvertently requested a broader symbolic kernel
calculation (`B=50`, degrees below 50). It was terminated immediately at PID
`1677566`; the PID was confirmed absent and no partial output or artifact was
retained.

## Field 9 — artifacts, hygiene, and audit request

Owned artifacts are `plan.md`, `checkpoint.md`,
`operator_obstruction_theorem.md`, this report, `freeze_manifest.md`, and
`SHA256SUMS`. There is no raw numerical payload because the promoted claims
are closed-form algebraic proofs. No predecessor, coordinator, manuscript,
project-skill, package, configuration, commit, or remote state was changed.
