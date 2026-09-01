# M173 final report: aggregated modal-vector and terminal sector

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: FREEZE STRICT TERMINAL-SECTOR THEOREM FOR FRESH AUDIT.
PROVED: exact six-term actual-history AMV branch recursion.
PROVED: (M,C,||Z||^2) and scalar child T_1 do not close that recursion.
PROVED: fresh constant-child terminal aggregate is at most 1/4.
PROVED: fresh actual-history live h=1 descendants contribute at most
        (1-q_0)/4 for L>=2; L=1 contributes at most (1-q_0)/2.
UNRESOLVED: reset plus h>=2 AMV budget and universal all-suffix boundary.
```

This removes the terminal `h=1` sector from the fresh-parent AMV obligation,
but it does not prove the total parent budget.

## Field 2 — scope, target, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, factors displayed left-to-right.
This mission concerns only `F=H/q`, the normalized full unweighted reset
excursion of the auxiliary nonlazy minimal-long-cycle parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| aggregated modal vector | fresh auxiliary right-heavy `T_1` budget | N/A: no sampler | N/A: auxiliary recurrence | exact branch algebra, operator witnesses, analytic terminal sum | terminal sector proved; total open |

No weighted/root-mean claim, auxiliary gap, original lazy `{3,4,5}` gap,
polynomial mixing result, Terminal A, or Terminal B follows.

## Field 3 — exact AMV recursion

For retained observation `a<d`, M162/M165's exact block is

```text
f_a=sqrt(eta/pi_a)L_a Phi_a,
L_a dmu_parent=pi_a dmu_a.
```

Write under the child law

```text
Phi_a=M_a+(u-p_a)C_a/sigma_a^2+Z_a,
E Z_a=E[(U-p_a)Z_a]=0,
delta_a=p_a-p_parent.
```

The sensitive trace normalization is

```text
E_parent||f_a||^2
 =(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_child[L_a||Phi_a||^2].
```

Define `lambda_j=E_child[L_a(U-p_a)^j]` for `j=0,1,2`,
`Z_0=E_child[L_a Z_a]`, `Z_1=E_child[L_a(U-p_a)Z_a]`, and
`Z_2=E_child[L_a||Z_a||^2]`. The branch contribution to parent `T_1`, divided
by `eta`, is exactly

```text
lambda_0||M||^2+2lambda_1<M,C>/sigma_a^2
+lambda_2||C||^2/sigma_a^4
+2<M,Z_0>+2<C,Z_1>/sigma_a^2+Z_2
-pi_a||delta_a M+C||^2/sigma_parent^2.
```

Summing this over every live `(d,t)` and every `a<d`, plus the exact reset
coordinate functional, is the full parent recursion. The killed `a=d` atom
is absent exactly and is never survival-conditioned. This closes only if
`Z` is retained as a full Hilbert-valued polynomial, or its required weighted
moments are retained; one scalar tail norm is insufficient.

## Field 4 — exact finite-summary obstruction

At parent `Beta(1,1)`, degree one, retain `a=0` and kill `a=1`. The child is
`Beta(1,2)`. Its unit-normalized Jacobi modes of degrees two and three both
have

```text
M=0, C=0, ||Z||^2=T_1(child)=1,
```

but their unit-exterior parent charges are respectively

```text
18/35 and 32/63.
```

Thus `(M,C,||Z||^2)` and `(M,C,T_1)` do not determine the exact transfer.
These are unrestricted operator inputs, not claimed actual-history child
features. They refute only the named finite summaries, not an aggregate
inequality retaining the full `Z` profile.

## Field 5 — analytic terminal operator theorem

For the accepted fresh constant-child charge

```text
R_d=(d+1)/(2d+1)[4^d/binom(2d,d)-1]
    -d/(d+2)+3d^2/[(d+1)(d+2)^2],
```

the theorem note proves for all `d>=2`

```text
R_d<=3d/8.
```

The proof uses `4^d/binom(2d,d)^(-1)<=2sqrt(d)` for `d>=1`, handles all
`d>=8` analytically, and checks the exact rational bases `d=2,...,7`.

For terminal `h=1`, put `n=L-1`, `d=r+1`, and

```text
eta_(n,r)=c(n,r)/[(r+1)!w_(n+2)].
```

The binomial theorem gives exactly, including `r=n`,

```text
sum_(r=1)^n (r+1)eta_(n,r)=((n+1)/(n+2))^n<=2/3.
```

Therefore the uniform analytic bound is

```text
sum_(r=1)^n eta_(n,r)R_(r+1)<=1/4,
```

with equality at `n=1` and strict inequality afterwards. This strengthens
M167/M170's factorial summability but remains a scoped operator theorem.

## Field 6 — actual-history fresh terminal corollary

Fix the fresh right-heavy parent

```text
xi=(B+L,2,1,B),     U_parent~Beta(1,1).
```

For `L>=2`, the live `h=1` roots have

```text
t=B+1, n=L-1, d=r+1, 1<=r<=n.
```

Every retained child is `(B,2+d,1+a,B)`, so it has suffix excess zero. Its
feature is constant by M162/M165's degree bound, and M109/M114's accepted
all-deficit boundary gives

```text
||M_child||^2=F(child)<=1-q_0,
q_0=q_(B,0)=w_B/w_(B+1).
```

After summing prefixes and multiplying the exact child/parent split ratio,
the grouped exterior is precisely `eta_(n,r)`—there is no additional `q_0`,
parent-`q`, or observation factor. Freshness gives `pi_a=1/(d+1)`. Each
coordinate projection charge is nonnegative, so varying child norms are
bounded by their maximum and the retained-observation sum is `R_d`. Hence

```text
T_1^(h=1)(xi)
 <=(1-q_0)sum eta_(n,r)R_(r+1)<=(1-q_0)/4.
```

At `L=1`, the separate `(n,r)=(0,0),d=1` row has eta one and `R_1=1/2`,
giving `(1-q_0)/2`. At `B=1` the child target is inactive and the contribution
is zero. No reset or `h>=2` term is included.

## Field 7 — dependencies, limitations, and next lemma

All frozen SHA ledgers verify for M109/M114, M147/M151, M157/M160,
M162/M165, and M167/M170. The proof uses their accepted all-deficit
suffix-zero theorem, all-suffix root coefficients, shared-observation kernel,
actual-history feature/degree bound, and fresh terminal `R_d`/eta formulas.
M170's `r=n` correction is handled separately in the exact first-moment
identity.

The strongest self-attack is that the proved quarter bound controls only
constant suffix-zero children at a fresh parent. General `h>=2` children have
nonconstant `Z`, and Section 4 proves their transfer cannot be inferred from
one tail norm. The first unresolved lemma is:

> Bound the fresh-parent reset plus all `h>=2` terms in the exact AMV
> recursion, retaining the weighted `Z_0,Z_1,Z_2` data, after reserving the
> proved `h=1` charge. Compare only the total with `1-q_parent`.

This is a strict narrowing, not global AMV closure.

## Field 8 — reproducibility and exact checks

Run from the M173 directory:

```text
python3 -B terminal_modal_exact.py --output terminal_modal_exact.json
```

Python 3.12.3, standard library only, deterministic `seed=null`. The compact
checker imports no predecessor code and reports zero failures over:

- one asymmetric two-coordinate audit of all six AMV terms and the exact
  first-mode subtraction;
- two normalized operator nonclosure witnesses;
- the six rational `R_d` bases for `d=2,...,7`; and
- five selected eta first-moment and terminal-aggregate rows, including the
  equality `n=1` row.

The finite checks audit formulas; the analytic proofs establish the uniform
claims. No `L=7` enumeration or broad scan was run.

## Field 9 — artifacts, boundary audit, and hygiene

Owned artifacts are `plan.md`, `checkpoint.md`,
`aggregated_modal_vector_theorem.md`, `terminal_modal_exact.py`,
`terminal_modal_exact.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.

The killed atom, `L=0` absent first mode, `L=1,d=1` terminal exception, and
`B=1` inactive child are separated explicitly. Original-chain cases `m` odd,
`m=0,2`, and `N=2` do not enter this auxiliary lemma. No predecessor,
coordinator, manuscript, project-skill, package, configuration, commit, or
remote state was changed. The generated Python cache was removed before
freeze.
