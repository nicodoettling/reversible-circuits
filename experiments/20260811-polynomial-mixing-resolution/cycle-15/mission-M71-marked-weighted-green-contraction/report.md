# M71 final report: marked deep contraction, canonical reset frontier

Date: 2026-08-12.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, conventions, and scope

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  For every `r>=2`, this mission concerns only the full
**nonlazy stationary-flow parking-degree projection** `Pbar_r` in the
minimal factorization sector of `(0 1 ... r)`, with

```text
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!],
alpha_r=2/[3r(r-1)].
```

It does not concern the original fixed-length identity chain `K`.

Starting from frozen M56 and frozen/refereed M65, the exact marked
child-resolved recurrence is proved, and every rank-only polynomial
Lyapunov weighting of M56's electrical disintegration is refuted by an
explicit infinite family.  Replacing the electrical root quotient by
M50's first-boundary canonical flow gives three new universal results:

1. every quotient residual resets to a right-heavy context `K-R=1`;
2. its normalized canonical base energy is at most
   `e(1+log s) min(s,K-R)` and hence at most `e(1+log s)` immediately
   after a reset;
3. the exact stationary deep kernel contracts suffix excess plus one by
   a factor `3/4`.

A fixed actual edge is compatible with only polynomially many current
embedding/mark/source labels, so unmarking can lose only one polynomial
Cauchy factor **provided** the aggregated marked occupation is first
bounded.  That last occupation estimate is unresolved.  Therefore this
mission proves neither a universal polynomial energy comparison for actual
`Pbar_r` nor an infinite obstruction surviving unmarking.

## 2. Full argument and construction

### 2.1 Exact marked Green DAG and rank-only obstruction

For local rank `s`, put

```text
G_s=R_s/alpha_s,
rho_s(C)=w_(s+1)^(-1)[1/k!]product_i w_(c_i),
w_a=a^(a-1)/a!,
q_(s,K,R,B)=w_(s+1-B)w_B/w_(s+1).
```

M65's conditional mean is denoted `H_(s,K,R,B)`.  An electrical quotient
edge whose refined endpoint contains adjacent parts `(A,B)` at boundary
position `p` creates the child mark

```text
(A+B-1,k-1,k-p-2,B),
```

with coefficient `(theta_e^2/Q_G(e))/q`.  A deep group with `k` parts and
last part `t>B` creates children

```text
(t-1,K+k,R+j,B),          1<=j<=k,
```

with M65's exact negative-hypergeometric coefficients.  This is the
rank-acyclic recurrence in `checkpoint.md`; taking a lower-rank maximum
recovers M56's false scalar recurrence exactly.

For every fixed exponent `p>=0`, take

```text
x_(s,K)=(s,K,K-1,s-1),        K=s^2.
```

The unary composition and terminal composition give an exact weighted
coefficient with lower limit

```text
1+e^(-1)(1-e^(-1))^2/2>1.
```

Thus every rank-only power eventually amplifies.  This is a theorem about
a proof template, not a gap upper bound: the suffix mark makes the child
terminal, so the bad scalar history is inconsistent after `B` is restored.

### 2.2 Canonical first-boundary quotient flow

Send each root-composition charge to the one-part hub by repeatedly merging
the first two parts.  A used edge is

```text
(A,c_2,...,c_k)->(A+c_2,c_3,...,c_k).
```

Its boundary position is `p=0`, so the residual child is exactly

```text
(A+c_2-1,k-1,k-2,c_2),
```

and hence `K-R=1`.  If `B_e` is M50's recoverable source basin, the
canonical current is

```text
theta(e)=sum_(C in B_e)rho_s(C)(H(C)-q).
```

M50 gives `rho_s(B_e)<=e rho_s(refined)` and exact normalized capacity
`Q_G(e)=rho_s(refined)k`.  Cauchy on each basin and the harmonic sum over
the unique first-merge path give

```text
sum_e theta(e)^2/Q_G(e)
 <=e(1+log s) Var_rho(H).                           (2.1)
```

The M65 closed formula also gives

```text
0<=H(C)<=min(s,K-R).
```

For the terminal line this follows from
`T_(K,R)(k)<=min(k,K-R)`; for the deep line it follows from
`w_aw_b/w_(a+b)<=1` and `D<=1`.  Since
`Var(H)<=q max H`, (2.1) proves

```text
a_can(s,K,R,B)<=e(1+log s)min(s,K-R).               (2.2)
```

Every reset child therefore has base cost at most `e(1+log s)`.

### 2.3 Exact deep descendant law and contraction

Put `S=s+1-B`, `L=s-B`, and let `n=s-t` be the prefix size before the
last root part.  Define

```text
A_n=sum_(p>=0)1/(p+1)!
       sum_(a_1+...+a_p=n)product_i w_(a_i).
```

After stationary mass, split ratio, and mean are cancelled, every
contextual deep kernel is dominated by the exact probability law

```text
P_S(n)=A_n w_(S-n-1)/w_S,          0<=n<=S-2.       (2.3)
```

For `T(z)=z exp(T(z))`, its generating function is

```text
A(z)=(exp(T(z))-1)/T(z)=1/z-1/T(z).
```

The identity `A(z)T(z)=T(z)/z-1` proves normalization.  Differentiation
and Lagrange inversion give the exact first moment

```text
E_(P_S)n=(S-1)^(S-1)/S^(S-2)-1>=(S-2)/4.           (2.4)
```

The lower bound follows from
`(1-1/S)^(S-1)>=e^(-1)` for `S>=8`; direct exact substitution handles
`2<=S<=7`.  A deep child has suffix excess `L_y=L-1-n`.  Consequently,
for the exact marked deep coefficients,

```text
sum_y Wdeep(x,y)(L_y+1)<=(3/4)(L+1).                (2.5)
```

Thus a pure-deep excursion has total `(L+1)` occupation at most
`4(L+1)`.  This is the requested weighted/non-max mechanism and retains
the actual stationary descendant factors that the false scalar recurrence
discarded.

The positional fraction is also exactly harmonic under the full shuffle:

```text
E[(R+J+1)/(K+k+1)]=(R+1)/(K+1).
```

Deleting the zero-contribution `J=0` class makes it superharmonic for the
substochastic deep kernel.

### 2.4 Actual-edge multiplicity

M65's pointwise inheritance shows that within this contextual class, no
earlier `j`-sequence survives once histories reach the same standardized
active macro and current `(K,R,B)`.  At a deep step,

```text
s'=t-1, K'=K+k,       s-s'=s-t+1>=k,
```

so `K+s` never increases.  Ambient feasibility gives `K+s<=r`; quotient
resets have `K=k-1<=s-1`.  Hence fewer than `r^4` numerical
`(s,K,R,B)` marks occur.

A fixed actual macro edge can lie in a recursive subproblem rooted only at
an ancestor of its moved tree edge, giving at most `r+1` active embeddings.
Including orientation, initial refinement, and nearest quotient-reset edge
as recovery metadata gives a conservative `O(r^9)` labels per actual edge.
If each aggregated label flow has already been constructed, one application
of Cauchy gives

```text
sum_e (sum_lambda F_lambda(e))^2/Q(e)
 <=O(r^9) sum_lambda sum_e F_lambda(e)^2/Q(e).       (2.6)
```

This removes exponential current-label multiplicity as an independent
obstruction.  It does not prove the marked occupation needed on the right
side of (2.6).

## 3. Probability, runtime, path, and congestion accounting

- Actual scan normalization is `alpha_r=2/[3r(r-1)]`; all displayed
  quotient energies use `G_s=R_s/alpha_s` and return to `R_s` by the exact
  factor `alpha_s^(-1)`.
- A canonical root path has at most `s-1` edges.  Its charge-flow bound uses
  the harmonic weighted occurrence `sum_(k=2)^ell 1/k<=1+log s`, not the
  worst path length.
- M50's exact source-basin ratio is at most `e`; normalized capacity of a
  refined `k`-part endpoint is `rho k`.
- Pure deep suffix-excess occupation is at most `4(s-B+1)` by (2.5).
- A fixed actual edge has conservative current-label multiplicity
  `O(r^9)`; (2.6) applies this loss once.
- Exact state counts are `2^(s-1)`.  The electrical scans reached `s=11`;
  the canonical scan reached `s=14` and took `52.70` seconds.  Python was
  `3.12.3`, NumPy `1.26.4`, SciPy `1.11.4`; seed is `null`.
- The largest recorded canonical deep-mass identity error is
  `1.20e-11`.  Finite linear-solve residuals are diagnostics only.

## 4. Dependencies by status

- **Proved/frozen M50/M41:** root-composition stationary law and exact
  merge/split capacities; first-boundary basin recovery and ratio at most
  `e`; exact product restrictions and balanced induction.
- **Proved/frozen M56:** contextual branch locality; exact
  `alpha/gamma` norm cancellation; one-active-last-branch recursion; exact
  quotient disintegration and residual normalization.
- **Proved/frozen and freshly accepted M65/M69:** closed contextual mean;
  negative-hypergeometric marked inheritance; scalar absorption and relaxed
  scalar absorption refutations.
- **Proved here:** child-mark DAG; infinite rank-only Lyapunov obstruction;
  canonical right-heavy reset; canonical base-energy bound; exact deep
  descendant first moment and `3/4` contraction; polynomial current-label
  multiplicity and one-shot Cauchy lemma.
- **Empirical exact finite:** electrical and canonical marked resolvents,
  dynamic finite potentials, and all small-r coefficient scans.
- **Open:** canonical right-heavy reset occupation and its aggregated
  actual-edge implementation; ROOT-MEAN LIFT and the full `Pbar` gap.

## 5. First unproved standalone step

> **CANONICAL RIGHT-HEAVY RESET OCCUPATION.**  Let `D` be the exact marked
> deep kernel and `J_can` the first-boundary canonical quotient residual
> kernel.  Every row of `J_can` lands in `K-R=1`, and `D` satisfies (2.5).
> Prove that the rank-acyclic Green expansion generated by `D+J_can` has
> total normalized base energy at most `A r^C`, uniformly over every
> ambient-feasible contextual mark.  Construct it after aggregating all
> histories with the same `(active embedding,K,R,B,nearest reset)` label.

With this statement, the one-shot multiplicity bound (2.6), M56's exact
norm cancellation, and M54's H-minus reduction would give a polynomial
ROOT-MEAN LIFT for auxiliary `Pbar`.

## 6. Strongest self-attack

The root-basin current is additive and recoverable on the composition tree,
but its fine disintegration has a biased coarse endpoint.  At `s=3`, root
composition `(1,2)` merges entirely to macro `(0,1,2)`, whereas the target
stationary unary fibre assigns masses `1/3,2/3` to
`(0,1,1),(0,1,2)`.  Even aggregate canonical coalescence has densities
`15/16,33/32`, not one.  Thus a recurrence which drops quotient-reset
children is false, and the canonical base bound plus deep contraction does
not yet imply `O(s log s)` total energy.

Likewise, polynomially many current labels do not control the sum of
historical amplitudes inside one label.  Those amplitudes must be aggregated
before routing, and the resulting squared occupation is exactly the open
operator in Field 5.  The finite roughly linear resolvent is not a proof.

Finally, `(k,last part)` is not a strong lumping of `G_s`: at `s=5`,
compositions `(1,3,1)` and `(2,2,1)` have the same `(3,1)` statistic but
aggregate split rates `4/3` and `2` to `(4,1)`.  No reduced two-coordinate
spectral theorem is being assumed.

## 7. Calibrations and falsification attempts

- `s<=1` is a singleton and carries zero recursive energy.
- `s=2` has the exact two-state quotient; it is included in every recurrence
  and in the infinite rank-only obstruction.
- `B=s` has no deep continuation; `B=s-1` is the critical rank-only
  obstruction but terminates after one descent.
- `K=1,R=0`, `R=0`, and `R=K-1` are all scanned; additional
  `K=64,128,256,1024,4096` slices test large synthetic contexts.
- The exact electrical marked resolvent maxima for `s=2,...,11` are
  `.444,.580,.671,.744,.790,.828,.857,.879,.898,.914`.
- The canonical marked maxima through `s=14` are
  `.444,1.145,1.764,2.533,3.157,3.676,4.155,4.654,5.083,5.458,
  5.803,6.153,6.463`.  These are compatible with polynomial growth only.
- A finite dynamic potential for electrical flow with factor `1-1/s`
  stays below `2.534` through `s=11`; this is discovery evidence, not a
  universal certificate.
- Odd identity length, `m=0,2`, `N=2`, and identity-bridge small cases are
  outside this auxiliary long-cycle projection; no inference about them is
  made.

## 8. Artifacts and reproduction

Proof artifacts:

- `plan.md`, `checkpoint.md`, `canonical_weighted_reduction.md`,
  `unmarking_multiplicity_audit.md`, `report.md`;
- `weighted_green_probe.py`, `marked_resolvent_probe.py`,
  `lyapunov_certificate_probe.py`, `canonical_marked_probe.py`;
- corresponding machine-readable JSON outputs in this directory.

Representative commands from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/weighted_green_probe.py --s-max 10 --K-max 32 --exponents 1 2 3 4 6 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/weighted_green_s10_k32.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/marked_resolvent_probe.py --s-max 10 --K-max 32 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/marked_resolvent_s10_k32.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/lyapunov_certificate_probe.py --s-max 11 --K-max 16 --certificate 1.0,1.0 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/lyapunov_c1_s11_k16.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/canonical_marked_probe.py --s-max 14 --K-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M71-marked-weighted-green-contraction/canonical_marked_s14_k8.json
```

All calculations are deterministic.  `python3 -B -m compileall -q` passed
for the four scripts; generated bytecode was removed.

## 9. Verdict

**INCONCLUSIVE, WITH PROVED REDUCTION.**

The false scalar-max and rank-only templates are rigorously eliminated.
The surviving route now has a proved logarithmic canonical reset cost, a
proved fixed-factor deep contraction, and a proved one-shot polynomial
unmarking multiplicity bound.  The exact remaining gap is repeated
right-heavy reset occupation after histories are aggregated.  No universal
polynomial energy comparison and no unmarked infinite obstruction is proved;
the global goal remains open.
