# M184 final report: fresh referee of frozen M179

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT M179'S STRICT FRESH h=2 SECTOR THEOREM.
PROVED: suffix-one actual-history children are exactly affine, Z=0.
PROVED: branch charge <=(1/2)S at d=1 and <=(2/3)S at d>=2.
PROVED: actual-history child trace S<=3/4 at d=1 and S<=1 at d>=2.
PROVED: complete fresh actual-history h=2 descendant charge <=1/4.
MATERIAL OBJECTIONS: NONE.
UNRESOLVED: exact reset plus h>=3 and the total parent AMV budget.
```

The accepted claim removes only the fresh `h=2` descendant sector.  It does
not prove that the parent reset and remaining descendants fit in the total
budget.

## Field 2 — integrity, target, and convention

Before substantive reading, all seven entries in frozen M179's
`SHA256SUMS` passed and its inventory matched `freeze_manifest.md`.  The
ledger digest is
`edaf37e884fbd4fb970a38ce626ef850b5eac2490fa8083ed78eb92a73c2c03d`.
M179 was not edited.  All frozen ledgers for its cited accepted dependencies
also pass.

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors left-to-right.  This audit
concerns only `F=H/q` in the auxiliary nonlazy minimal-long-cycle parking
projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| fresh `h=2` AMV sector | auxiliary right-heavy `T_1` descendant charge | N/A | N/A | clean-room beta matrix, history-current, Cayley audit | accept scoped theorem |

No nonfresh, all-suffix, weighted/root-mean, gap, original-chain,
polynomial-mixing, Terminal A, or Terminal B conclusion follows.

## Field 3 — affine collapse and Bayes normalization

At a fresh parent, an `h=2` root of degree `d` and retained observation
`a<d` has child

```text
xi_a=(B+1,d+2,a+1,B),
mu_a=Beta(a+1,d-a+1).
```

Its suffix excess is one.  M162/M165's feature-degree theorem therefore
gives exactly

```text
Phi_a=M_a+(u-p_a)C_a/v_a,       Z_a=0,
S_a=E_child||Phi_a||^2
   =||M_a||^2+||C_a/sqrt(v_a)||^2.
```

Here `S_a` is the full child trace; it is not child `T_1` or `F`.

For the retained coordinate
`f_a=sqrt(eta/pi_a)L_a Phi_a`, independent Bayes calculation gives

```text
(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_child[L_a||Phi_a||^2],

E_parent[(U-1/2)f_a]
 =sqrt(eta*pi_a)(delta_a M_a+C_a).
```

Thus the covariance subtraction is exactly
`12 eta pi_a||delta_a M_a+C_a||^2` and keeps the signed cross term.  The
killed `a=d` observation is absent before the history norm is formed; there
is no survival conditioning.

## Field 4 — exact `2x2` Loewner theorem

Multiplying the child law by `L_a` gives the second posterior
`Beta(2a+1,2d-2a+1)`.  Its affine moments yield M179's symmetric matrix in
`(M_a,C_a/sqrt(v_a))`.  At `d=1,a=0`, it is exactly

```text
diag(1/2,1/5),
```

so the sharp comparison needed there is `B_(1,0)<=S_0/2`.

For `d>=2`, Vandermonde gives

```text
lambda_0<=lambda_*=(d+1)/(2d+1).
```

Increasing `lambda_0` to `lambda_*` is valid in Loewner order because the
scaled part is a second-posterior expectation of an affine outer product.
For `x=(2a-d)^2`, independent algebra reproduces both positive diagonal
factors and

```text
det((2/3)I-G_*)=P_d(x)/positive_denominator,
P_d(x)=A_0+A_1x-A_2x^2,       A_2>0.
```

The determinant numerator is concave on `0<=x<=d^2`; its endpoints are

```text
P_d(0)=(d-1)(d+2)^3(5d^4+24d^3+64d^2+72d+18)>0,

P_d(d^2)=(d+1)(2d+1)
 (d^5+152d^4+557d^3+658d^2-216d-144)>0.
```

This proves `G<=2I/3` for every `d>=2,a<d`.  The proof preserves the matrix
cross term and never bounds `M_a,C_a` separately.

## Field 5 — actual-history trace envelope

For `B>=2`, put

```text
y=w_B/w_(B+1),   b=w_B/w_(B+2),
h=B/(B+2),       z=1/(d+3).
```

A direct reconstruction of the suffix-one history gives:

- the exceptional reset coordinate `u-b/2`;
- constant ordinary reset coordinates with total trace at most
  `b(h-b/2)` by the accepted basin ratio; and
- the sole descendant coordinate `(1-u)Phi_0/sqrt(1-p)`, where `Phi_0` is
  constant and `||Phi_0||^2<=1-y` by the accepted all-deficit suffix-zero
  boundary.

Consequently

```text
S_a<=b(h-b/2)+(p-b/2)^2+p(1-p)z
     +(1-p+pz)(1-y).
```

For `d=1`, the Cayley-ratio bounds reduce this to
`8y^2-9y+2<=0` on `[1/3,2/3]`, proving `S_0<=3/4`.  For `d>=2`, convexity
in retained `p`, the positive endpoint difference `(1-z)y-b`, and the
bounds `b<=3/8`, `1-y<=2/3` give `S_a<=1`.  At `B=1`, no active reset
endpoint exists and the unary target has rank one, so the actual feature is
zero.  This argument applies only to the explicit actual history, not an
unrestricted affine input.

## Field 6 — exterior and final aggregation

With `n=L-2` and `r=d-1`, direct cancellation gives

```text
eta^(2)_(n,r)=m_group q_child/q_parent
 =c(n,r)/[(r+1)!w_(n+3)].
```

No observation, survival, or extra split factor remains.  At the separate
`n=0,L=2,d=1` boundary, `eta=2/3`, hence

```text
(2/3)(1/2)(3/4)=1/4.
```

For `n>=1`, including `r=n`, the binomial theorem gives

```text
sum_(r=1)^n(r+1)eta^(2)_(n,r)
 =(n+1)^n(n+2)/(n+3)^(n+1)<=3/8.
```

Each degree `d=r+1` has exactly `d` retained observations.  Applying the
`2/3` matrix bound and `S_a<=1` coefficientwise gives the complete sector

```text
T_1^(h=2)(xi)<= (2/3)(3/8)=1/4.
```

Observation-dependent child vectors are handled separately; no common-vector
or scalar-child-summary assumption is used.

## Field 7 — numbered objections, dependencies, and limitations

1. **Material objections: none.** Every theorem-critical identity,
   inequality, normalization, and boundary survives independent derivation.
2. **Nonmaterial proof-detail clarification:** before using `b<=3/8` in the
   trace proof, combine the relevant terms as
   `p^2+b(h-p)-b^2/4<=p^2+b(1-p)`.  This makes M179's substitution visibly
   sign-safe; its frozen inequality is correct.
3. **Nonmaterial proof-detail clarification:** the final determinant endpoint
   is uniformly positive because `658d^2-216d-144` is positive at `d=2` and
   increasing.  No hidden finite base audit is needed.
4. **Essential dependencies:** the result uses M109/M114's suffix-zero
   all-deficit boundary, M147/M151's basin ratio, M157/M160's history kernel,
   M162/M165's feature-degree theorem, and M173/M177's AMV recursion.
5. **Limitation:** the absolute `1/4` sector charge does not imply a total
   parent budget.  Reset plus `h>=3` remains the first open lemma.

## Field 8 — clean-room reproducibility

Run from this M184 directory:

```text
python3 -B independent_exact.py --output independent_results.json
```

Python 3.12.3, standard library only, deterministic `seed=null`.  The script
imports no M179/predecessor code or data and reports `status=pass`,
`failures=[]`.  It checks:

- one new asymmetric exact Bayes/cross-term row;
- the exact degree-one matrix;
- eight selected Loewner/factorization rows at `d=2,5,11`;
- eight actual-history trace rows reconstructed from composition basins,
  including `B=1`;
- five direct `eta=m_group q_child/q_parent` rows, including `n=0,r=n`; and
- four exterior moments through `L=6`.

These named rows audit the formulas.  The all-degree theorem rests on the
analytic proof in `proof_audit.md`.  No `L=7`, `h>=3`, or broad scan was run.

## Field 9 — boundaries, artifacts, and hygiene

The absent `L=0,1` sector, `L=2/n=0/d=1`, `B=1` inactivity, killed `a=d`,
and `r=n` boundaries are explicit.  Original-chain cases `m` odd, `m=0,2`,
and `N=2` receive no new conclusion.

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`independent_exact.py`, `independent_results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`.  No predecessor, coordinator,
manuscript, project-skill, package, configuration, commit, or remote state
was changed.  Generated cache and temporary rerun files are removed before
freeze.
