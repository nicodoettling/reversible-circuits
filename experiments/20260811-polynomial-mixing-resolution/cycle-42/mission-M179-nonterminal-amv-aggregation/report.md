# M179 final report: fresh nonterminal `h=2` AMV sector

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: FREEZE STRICT FRESH h=2 SECTOR THEOREM FOR FRESH AUDIT.
PROVED: every suffix-one actual-history child feature is affine (Z=0).
PROVED: exact branch charge <=(1/2)S for d=1 and <=(2/3)S for d>=2.
PROVED: actual-history child trace S<=3/4 for d=1 and S<=1 for d>=2.
PROVED: the complete fresh h=2 descendant charge is at most 1/4.
UNRESOLVED: exact reset plus h>=3 AMV budget and total parent inequality.
```

This removes exactly the `h=2` descendant sector from the first open AMV
obligation after M173/M177.  It does not aggregate the parent reset term and
does not prove the remaining budget.

## Field 2 — target, convention, and scope

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.  This mission concerns only `F=H/q`, the normalized full
unweighted reset excursion in the auxiliary nonlazy minimal-long-cycle
parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| affine `h=2` AMV sector | fresh auxiliary right-heavy `T_1` contribution | N/A: no sampler | N/A: auxiliary recurrence | exact beta matrix, history trace, root/Cayley cancellation | sector proved; total open |

No nonfresh, all-suffix, weighted/root-mean, auxiliary-gap, original-chain,
polynomial-mixing, Terminal A, or Terminal B claim follows.

## Field 3 — affine degree collapse and exact branch form

Fix the fresh parent

```text
xi=(B+L,2,1,B),       U_parent~Beta(1,1).
```

For `h=2`, a degree-`d` root and retained observation `a<d` have child

```text
xi_a=(B+1,d+2,a+1,B),
mu_a=Beta(a+1,d-a+1).
```

The child suffix excess is exactly one, so M162/M165's degree theorem gives

```text
Phi_a=M_a+(u-p_a)C_a/v_a,       Z_a=0,
p_a=(a+1)/(d+2),
v_a=(a+1)(d-a+1)/[(d+2)^2(d+3)].
```

With `V_a=C_a/sqrt(v_a)`, the exact child diagonal trace is

```text
S_a=E_child||Phi_a||^2=||M_a||^2+||V_a||^2.
```

M173's branch formula, including the exact covariance subtraction
`12 pi_a||delta_a M_a+C_a||^2`, is a `2x2` quadratic form in `(M_a,V_a)`.
Here `pi_a=1/(d+1)` and the likelihood-weighted moments are computed by the
second posterior `Beta(2a+1,2d-2a+1)`.  This keeps the mean--covariance cross
term exactly.  The killed `a=d` observation is absent without survival
conditioning.

Crucially, the generalized-eigenvalue comparison is parent branch `T_1`
against child **trace `S_a`**.  It is not a comparison with child `T_1`,
child `F`, or a scalar finite summary.

## Field 4 — all-degree `2x2` theorem

At `d=1,a=0`, the exact normalized branch matrix is

```text
diag(1/2,1/5),
```

so its largest eigenvalue is `1/2`.

For `d>=2`, Vandermonde bounds the positive likelihood matrix by replacing

```text
lambda_0=(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a)
```

with `(d+1)/(2d+1)` in Loewner order.  Writing `x=(2a-d)^2`, the proof note
factors both diagonals and the determinant of `(2/3)I-G_*`.  The determinant
numerator is a concave quadratic `P_d(x)` on `0<=x<=d^2`; its exact endpoint
values are

```text
P_d(0)=(d-1)(d+2)^3(5d^4+24d^3+64d^2+72d+18)>0,

P_d(d^2)=(d+1)(2d+1)
 (d^5+152d^4+557d^3+658d^2-216d-144)>0.
```

The diagonal slacks are also positive for every `d>=2`.  Hence

```text
B_(1,0)<=1/2 S_0,
B_(d,a)<=2/3 S_a       for d>=2, a<d.
```

This is an analytic all-degree matrix proof.  No diagonalization shortcut
or separate bounds on `M_a,C_a` are used.

## Field 5 — actual-history child trace

For `B>=2`, abbreviate

```text
y=w_B/w_(B+1),   b=w_B/w_(B+2),
h=B/(B+2),       z=1/(d+3).
```

The suffix-one child's explicit feature has exactly:

1. constant ordinary reset coordinates, with total trace at most
   `b(h-b/2)`;
2. the exceptional reset coordinate `u-b/2`; and
3. the unique descendant coordinate
   `(1-u)Phi_0/sqrt(1-p)`, where `Phi_0` is constant and the accepted
   all-deficit suffix-zero theorem gives `||Phi_0||^2<=1-y`.

Therefore the actual-history trace, not a generic affine supremum, obeys

```text
S_a<=b(h-b/2)+(p-b/2)^2+p(1-p)z
     +(1-p+pz)(1-y).
```

For `d=1,a=0`, Cayley-ratio monotonicity reduces this to
`8y^2-9y+2<=0` on `[1/3,2/3]`, giving `S_0<=3/4`.  For `d>=2`, convexity in
the retained `p` interval, exact endpoint comparison, and
`b<=3/8`, `1-y<=2/3` give `S_a<=1`.

At `B=1`, both targets in the actual suffix-one history have rank one and
are inactive, so `Phi_a=0` and `S_a=0`.  The `B>=2` envelope is not applied
there.

## Field 6 — exact exterior and quarter aggregation

Put `n=L-2` and `r=d-1`.  Direct root/split cancellation gives

```text
eta^(2)_(n,r)=m_group q_child/q_parent
 =c(n,r)/[(r+1)!w_(n+3)].
```

This contains no additional observation or split factor.  At the separate
`n=0,L=2` boundary, `(r,d)=(0,1)` and `eta=1/w_3=2/3`, so

```text
(2/3)(1/2)(3/4)=1/4.
```

For `n>=1`, `r=1,...,n`, and the exact first moment, including `r=n`, is

```text
sum_(r=1)^n(r+1)eta^(2)_(n,r)
 =(n+1)^n(n+2)/(n+3)^(n+1)<=3/8.
```

Each degree `d=r+1` has exactly `d` retained observations `a<d`.  Applying
the coefficientwise `2/3` branch bound and actual-history `S_a<=1` gives

```text
T_1^(h=2)(xi)<= (2/3)(3/8)=1/4.
```

Observation-dependent child features are dominated separately; no common
vector is assumed.  This is the entire `h=2` descendant sector and nothing
else.

## Field 7 — dependencies, limitations, and next lemma

Complete frozen SHA ledgers passed before substantive use for M109/M114,
M115/M116, M147/M151, M157/M160, M162/M165, M167/M170, and accepted
M173/M177.  The proof uses M109/M114's all-deficit suffix-zero boundary,
M147/M151's canonical-basin inequality, M157/M160's actual-history kernel,
M162/M165's feature/degree theorem, and M173/M177's exact AMV recursion.

The strongest self-attack is scope: `S<=1` is proved only from the explicit
actual-history `L'=1` feature.  An unrestricted affine child with the same
beta law need not satisfy it.  The `1/4` is an absolute sector charge, not a
statement that the reset and all descendants fit below `1-q_parent`.

After reserving accepted `h=1` and the present `h=2`, the first unresolved
lemma is:

> Bound the exact fresh-parent reset plus every `h>=3` retained descendant,
> preserving the full Hilbert residual and all likelihood-weighted cross
> terms, against the remaining parent budget.

## Field 8 — reproducibility and exact checks

Run from this M179 directory:

```text
python3 -B h2_modal_exact.py --output h2_modal_exact.json
```

Python 3.12.3, standard library only, deterministic `seed=null`.  The checker
imports no predecessor code and reports `status=pass`, `failures=[]`.  It
contains:

- one asymmetric exact affine cross-term audit;
- the exact `d=1` matrix;
- eleven selected endpoint/interior Loewner rows for `d=2,3,7,20`;
- eight named actual-history norm rows including `B=1`;
- five direct `eta=m_group q_child/q_parent` cancellation rows; and
- four exterior first-moment rows, including `n=0` and equality at `n=1`.

The finite rows audit formulas; the proof note establishes the uniform
matrix, trace, and exterior inequalities.  No `L=7` enumeration or broad
scan was run.

## Field 9 — boundaries, artifacts, and hygiene

The `L=0,1` absent sector, `L=2/n=0/d=1` boundary, `B=1` inactivity, killed
`a=d`, and `r=n` root boundary are explicit.  Original-chain cases `m` odd,
`m=0,2`, and `N=2` receive no new conclusion.

Owned artifacts are `plan.md`, `checkpoint.md`,
`h2_affine_sector_theorem.md`, `h2_modal_exact.py`, `h2_modal_exact.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`.  No predecessor,
coordinator, manuscript, project-skill, package, configuration, commit, or
remote state was changed.  No cache or temporary rerun is retained at
freeze.
