# M170 proof audit of frozen M167

Date: 2026-08-13 UTC.

## 1. Immutable gate, scope, and disposition

The three coordinator-supplied hashes match the frozen M167 artifacts:

```text
d18ed32964935b0a58f236b04464be847fe673d24bb37ad3c11b409ba78f0997  report.md
ba552a74790df708d06e94066dfe3aa784c5c4eae5eb3e602490f2e3999ac627  operator_obstruction_theorem.md
4e7dd6a68de760d07e6ba1202ff3699210170eb8260d797b505bd55e200df4ec  freeze_manifest.md
```

M167 is immutable. The audited object is only `F=H/q`, the normalized full
unweighted reset excursion of the auxiliary nonlazy minimal-long-cycle
parking projection. The project target remains uniform fixed-length identity
transposition words, with `(pq)(x)=p(q(x))` and displayed factors
left-to-right.

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTION 1: operator_obstruction_theorem.md Section 6 is
  truncated mid-statement. Cite that file only for its complete Sections
  2--5; use report.md Field 7 for the unresolved aggregated modal-vector
  target.
NONMATERIAL CORRECTION 2: the product proof of eta_(n,r)<=r/(r+1)! directly
  covers r<=n-1. The true boundary r=n requires the separate calculation
  eta_(n,n)=1/(n+2)^n<=n/(n+1)!.
```

The all-suffix boundary remains unresolved. Nothing here implies an
actual-history counterexample, auxiliary gap, `ROOT-MEAN LIFT`, original
lazy `{3,4,5}` gap, polynomial mixing, Terminal A, or Terminal B.

## 2. Accepted actual-history functional

For integer `b>=1`, let `U~Beta(1,b)`. Its moments, mean, and variance are

```text
E[U^k]=k! b!/(b+k)!,
p_b=1/(b+1),
sigma_b^2=b/[(b+1)^2(b+2)].
```

For scalar or Hilbert-valued `f`, define

```text
Q_b(f)=E||f(U)||^2
       -||E[(U-p_b)f(U)]||^2/sigma_b^2.
```

By M162/M165's accepted actual-history feature map, `T_1` is the sum of
these coordinate functionals. A retained shared observation has coordinate
`sqrt(eta/pi_a)L_(d,a)Phi_child`. All `a<d` are retained and `a=d` is omitted
exactly, without survival conditioning. M167 uses this normalization.

## 3. Clean-room child-first-mode leakage

Fix `b>=1`, take degree `d=1`, retain `a=0`, and kill `a=1`. Then

```text
pi_0=E_b(1-U)=b/(b+1),
mu_child=Beta(1,b+1),
f(U)=U-1/(b+2),
g(U)=(1-U)f(U)/sqrt(pi_0).
```

The child `f` is its monic first mode. Exact beta moments give

```text
Q_(b+1)(f)=0,
||f||^2=(b+1)/[(b+2)^2(b+3)].
```

Bayes gives `E_b[(1-U)f]=pi_0 E_(b+1)f=0`, so `g` has no parent constant
mode. Direct substitution of the moments through degree four gives

```text
Q_b(g)=4(b+1)/[(b+2)^2(b+3)^2(b+4)].
```

Because `g` is quadratic and has zero constant mode, this positive remainder
is exactly parent degree-at-least-two energy. Normalizing by the child
first-mode norm yields

```text
Q_b(g)/||f||^2=4/[(b+3)(b+4)].
```

At the smallest case `b=1`, the child norm is `1/18`, its child `T_1` is
zero, the parent tail is `1/90`, and the normalized leakage is `1/5`.

Logical reach: this proves that scalar child `T_1` does not determine the
exact shared-observation transfer and refutes zero-preserving/homogeneous
scalar closures which discard child first-mode energy. It does not refute an
arbitrary scalar inequality supplied with an additional external mode budget,
an aggregated vector closure, or the actual-history boundary itself.

## 4. Clean-room retained constant-child calculation

Let `U~Beta(1,1)` be uniform. For degree `d>=1`, put

```text
L_a(U)=binom(d,a)U^a(1-U)^(d-a),
pi_a=E L_a=1/(d+1),
e_a=L_a/sqrt(pi_a),              a=0,...,d-1.
```

The killed atom is `a=d` with mass `pi_d=1/(d+1)`. Beta integration gives

```text
E[e_a^2]
 =(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a),
E[(U-1/2)e_a]
 =(2a-d)/[2 sqrt(d+1)(d+2)].
```

Since `Var(U)=1/12`,

```text
Q_1(e_a)
 =(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a)
  -3(2a-d)^2/[(d+1)(d+2)^2].
```

The coefficient identity

```text
sum_(a=0)^d binom(d,a)^2/binom(2d,2a)
 =4^d/binom(2d,d)
```

follows by rewriting a summand as
`binom(2a,a)binom(2d-2a,d-a)/binom(2d,d)` and convolving the coefficients of
`(1-4z)^(-1/2)`. Summing only `a<d` gives exactly

```text
R_d
 =(d+1)/(2d+1)[4^d/binom(2d,d)-1]
  -d/(d+2)+3d^2/[(d+1)(d+2)^2].
```

The retained constant energy and genuine high tail are

```text
sum_(a<d)(E e_a)^2=d/(d+1),
H_d=R_d-d/(d+1).
```

The smallest degrees distinguish the degenerate and first genuine cases:

| `d` | `R_d` | constant energy | `H_d` | killed mass |
|---:|---:|---:|---:|---:|
| 1 | `1/2` | `1/2` | `0` | `1/2` |
| 2 | `3/4` | `2/3` | `1/12` | `1/3` |
| 3 | `649/700` | `3/4` | `31/175` | `1/4` |
| 4 | `113/105` | `4/5` | `29/105` | `1/5` |

The central-binomial expansion

```text
4^d/binom(2d,d)=sqrt(pi*d)(1+1/(8d)+O(d^(-2)))
```

therefore yields the slightly sharpened form

```text
R_d=sqrt(pi*d)/2-3/2+O(d^(-1/2)).
```

Thus `H_d` diverges, while `pi_d=1/(d+1)` vanishes. This refutes any
degree-uniform branch-local inequality `H_d<=C pi_d` and even a uniform
`O(1)` bound on the retained total. It is only an operator-level
constant-child family: it does not assert that all normalized coordinates
occur with unit exterior weight in a single actual history.

## 5. Terminal exterior coefficient and factorial summability

Use M147/M151's accepted definitions

```text
w_k=k^(k-1)/k!,
c(n,r)=r n^(n-r-1)/(n-r)!       (1<=r<=n),
c(0,0)=1.
```

For the terminal `h=1` branch, `n=L-1` and `d=r+1`. The normalized exterior
coefficient is exactly

```text
eta_(n,r)=c(n,r)/[(r+1)!w_(n+2)]
 =r n^(n-r-1)(n+2)!/
   [(n-r)!(r+1)!(n+2)^(n+1)].
```

For `1<=r<=n-1`, factor out `r/(r+1)!`:

```text
eta/(r/(r+1)!)
 =(n/(n+2))^(n-r-1)
   [(n+2)!/(n-r)!]/(n+2)^(r+2)
 <=1.
```

Both factors are at most one. At the boundary `r=n`, the exponent used in
the first factor is negative, so M167's one-line product argument does not
apply. Directly,

```text
eta_(n,n)=1/(n+2)^n<=n/(n+1)!       (n>=1),
```

which restores the same bound. The exceptional `(n,r)=(0,0)` has `eta=1`
but `d=1` and hence `H_1=0`; it is outside the `r>=1` obstruction sum.

For each fixed `r>=1`, the displayed ratio tends to `e^(-2)`, so

```text
eta_(n,r) -> e^(-2)r/(r+1)!.
```

Finally `R_(r+1)=O(sqrt(r+1))`, and the corrected uniform majorant gives

```text
sum_(r=1)^n eta_(n,r)R_(r+1)
 <=C sum_(r>=1) r sqrt(r+1)/(r+1)!<infinity
```

uniformly in `n`. M167 is therefore correct that the local square-root
growth is factorially summable and supplies neither a harmonic divergence
nor an actual-history counterfamily.

## 6. Surviving unresolved scope and truncation

The frozen `operator_obstruction_theorem.md` literally ends after
`decompose each actual child feature as`. It is not a complete standalone
statement of the unresolved lemma. This is artifact incompleteness, not a
failure in its completed Theorems 3.1, 4.1, or Section 5.

The complete surviving target is in frozen `report.md` Field 7. Each actual
child feature must retain

```text
Phi_child=M_child
 +(u-p_child)C_child/sigma_child^2+Z_child,
E Z_child=E[(U-p_child)Z_child]=0,
```

and one must bound only the aggregate exact expression

```text
Q_parent(Phi_reset)
 +sum_(d,t,a<d) eta_(d,t)/pi_a
    Q_parent(L_(d,a)Phi_child)
 <=1-q_parent.
```

This remains unresolved. Constant, first, and high child modes, their vector
cross terms, every retained shared observation, and exact killing of `a=d`
must remain visible. M167's two counterfamilies rule out only the narrower
closures audited above.

Citation rule: cite frozen `operator_obstruction_theorem.md` for its complete
Sections 2--5 only; cite frozen `report.md` Field 7 for the unresolved
aggregated modal-vector target.

## 7. Independent checker, process scope, and hygiene

`independent_exact.py` uses standard-library `Fraction` arithmetic, no
randomness, and no predecessor imports. It checks selected smallest and
boundary rows only: `b=1,2,5`, `d=1,2,3,4`, and six terminal eta cases,
including `r=n`. Every assertion passes. `independent_results.json` records
the exact output. This is an algebra audit, not a finite proof of the
all-suffix statement.

The exact check `ps -p 1677566` returned no process. The frozen M167 directory
contains only its six declared artifacts and no retained raw diagnostic or
cache. This verifies present stopped-PID/no-retained-output scope; no claim is
made about unrecoverable ephemeral terminal output. No `L=7` or broad scan was
run.

Only the owned M170 directory was edited. No predecessor, coordinator,
manuscript, project skill, package, configuration, commit, or remote state was
changed.
