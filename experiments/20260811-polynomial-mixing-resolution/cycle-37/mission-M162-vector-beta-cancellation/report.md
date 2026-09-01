# M162 final report: vector beta/Jacobi cancellation

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: PROMOTE THE UNIVERSAL FEATURE/JACOBI REDUCTION FOR FRESH AUDIT.
PROVED: exact actual-history feature map, finite vector Parseval, every
        truncated Jacobi upper bound, and an exact first-mode recursion.
EXACT FINITE: T_1 repairs every right-heavy trace failure for
              B<=3,L<=6,kappa<=8.
UNRESOLVED: the all-suffix T_1 boundary and every gap/terminal.
```

## Field 2 — scope, target, and convention

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.
This mission concerns only `F=H/q`, the normalized full unweighted reset
excursion of the auxiliary nonlazy minimal-long-cycle parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| actual-history vector/Jacobi cancellation | right-heavy auxiliary all-suffix excursion budget | N/A: no sampler | N/A: auxiliary recurrence | exact transfer, Gram, Parseval, first-mode recursion | strict reduction; all-suffix boundary open |

No auxiliary gap, `ROOT-MEAN LIFT`, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing result, Terminal A, or Terminal B follows.

## Field 3 — explicit history feature and shared observation

For `mu=Beta(D,kappa-D)`, a live root group `(d,t)`, and retained
observation `a<d`, put

```text
L_a(u)=binom(d,a)u^a(1-u)^(d-a),  pi_a=E_mu L_a,
eta=m_s(d,t)q_child/q_parent.
```

The recursively defined Hilbert-valued polynomial is

```text
Phi_x(u)
 = direct-sum_E J_E(u)/sqrt(qc_E)
   direct-sum_(d,t,a<d) sqrt(eta/pi_a)L_a(u)Phi_child(u).
```

The direct sum uses distinct coordinates for every actual history branch.
Induction proves

```text
K_x(u,v)=<Phi_x(u),Phi_x(v)>,
H(x)/q_x=||E_mu Phi_x||^2.
```

The observation `a=d`, equivalently attachment rank `j=0`, is killed and is
absent exactly.  Bayes uses a single `pi_a` denominator because the two beta
copies share the observation.

## Field 4 — universal Jacobi/Parseval upper bounds

Let `P_n` be the monic shifted-Jacobi polynomials for the current beta law,
`h_n=E P_n^2`, and `A_n=E[P_n Phi]/sqrt(h_n)`.  Since `Phi` has degree at
most suffix excess `L`, vector Parseval gives

```text
E||Phi||^2=sum_(n=0)^L ||A_n||^2,
H/q=||A_0||^2,
T_r:=E||Phi||^2-sum_(n=1)^r||A_n||^2
    =H/q+sum_(n=r+1)^L||A_n||^2 >=H/q.
```

For `r=L` this is tautological equality and is not promoted as progress.
For fixed `r`, it is a rigorous off-diagonal upper bound for the actual
history feature, not diagonal trace, pointwise polarization, positive part,
absolute value, or the generic frame refuted by M123/M128.

The parameter convention is audited: under the standard Jacobi weight
`(1-z)^alpha(1+z)^beta`, the shifted parameters are
`(alpha,beta)=(kappa-D-1,D-1)`.  The checker independently Gram--Schmidts
from exact beta moments at every state.

## Field 5 — exact first-mode recursion

With `p=D/kappa`, `sigma^2=Var_mu(U)`,
`M=E Phi`, and `C=E[(U-p)Phi]`, the first mode is

```text
||A_1||^2=||C||^2/sigma^2,
T_1=E||Phi||^2-||C||^2/sigma^2.
```

For a retained branch, if `delta=p_child-p_parent`, Bayes gives

```text
E_parent[(U-p_parent)L_a Phi_child]
 =pi_a(delta M_child+C_child).
```

Orthogonality of actual history blocks yields the universal exact recursion

```text
||A_1(parent)||^2
=E1_reset
 +sum_retained eta*pi_a/sigma_parent^2
    ||delta M_child+C_child||^2.
```

The signed cross term `2 delta<M_child,C_child>` is retained.  The killed
branch is absent exactly.  Combined with the exact likelihood-weighted
diagonal recursion, this is a universal recursion for `T_1`, but not yet a
closed scalar bound.

## Field 6 — exact finite repair

The capped exact run covers 588 states with
`B<=3,L<=6,kappa<=8,1<=D<kappa`.  It has zero failures across 12,096
shared-X monomial-pair checks, 168 retained/killed mass checks, 2,324 modal
energy checks, 588 feature/Parseval checks, and 588 first-mode recursion
checks.

On all 147 right-heavy rows `D=1`, `T_1<=1-q`.  Diagonal trace passes 143;
the first mode is necessary and sufficient for the remaining four:

```text
(s,kappa,D,B)=(8,2,1,2),(7,2,1,3),(8,2,1,3),(9,2,1,3).
```

At `(9,2,1,3)`, trace is about `1.00558139`, first-mode energy about
`.36121508`, and `T_1` about `.64436630`, with the exact negative budget
margin displayed in `vector_beta_theorem.md`, (5.1).  No
higher Jacobi mode is needed anywhere in the cap.  These are exact finite
facts, not an all-suffix theorem.

## Field 7 — dependencies, limitations, and self-attack

Accepted inputs are M147/M151's all-suffix recurrence and attachment
coordinates, M152/M156's latent-beta contextual functions, and M157/M160's
shared-observation signed kernel.  The new feature map reconstructs those
definitions and does not assume M123/M128's refuted ambient frame.

The strongest self-attack is that finite-degree Parseval alone is formal
bookkeeping.  The substantive open issue is a uniform tail estimate.  The
first-mode recursion still contains a likelihood-weighted child diagonal
and a child constant-centered cross term, so it does not close on `T_1`.
No inequality charging all remaining modes to the killed atom has been
proved.  The 94 arbitrary-deficit local-budget failures in the full capped
grid are expected under M147/M151 and are not counterexamples to the
right-heavy boundary.

## Field 8 — reproducibility

Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M162-vector-beta-cancellation/vector_beta_exact.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M162-vector-beta-cancellation/vector_beta_exact.json \
  --max-B 3 --max-excess 6 --max-kappa 8
```

Python 3.12.3, standard library only, exact `Fraction` arithmetic,
deterministic `seed=null`.  Output is compact and retains theorem-critical
counts, parameter-convention examples, the four repair rows, and the
tightest nontrivial row.  No `L=7` enumeration was run.

## Field 9 — next lemma and hygiene

The first standalone theorem is:

> Prove `T_1(B,L,kappa,1)<=1-q_(B,L)` for all `B>=1`, `L>=0`, and
> `kappa>=2`, using the exact killed-observation and mixed first-mode
> recursions.  Equivalently, uniformly charge the high-Jacobi tail after the
> degree-one mode.

Only this owned M162 directory was edited.  No predecessor, coordinator,
manuscript, project-skill, package, configuration, commit, or remote state
was changed.
