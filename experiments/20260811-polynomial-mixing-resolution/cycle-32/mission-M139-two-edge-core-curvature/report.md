# M139 final report: exact two-edge-core cavity reduction

Date: 2026-08-13 UTC.

## Field 1 — decision and claim status

Verdict: **PROMOTE FOR FRESH AUDIT** the exact marked-pair recurrence and
cavity/Lagrange/beta-integral reduction; **REFUTE** shifted ULC and a uniform
inverse-linear H2 curvature surplus; **KEEP OPEN** ordinary two-edge-core
log-concavity and the higher-core curvature budget.

**PROVED, relative to accepted M125/M129 and M133/M136:** a connected
unicyclic incidence graph has core length two exactly when one unique
unordered atom pair is co-blocked in both colours.  This yields an exact
marked connected-component recurrence.  Its labelled atom species has a
coupled one-boundary cavity representation; the two-boundary core transforms
collapse by Lagrange inversion, and the cut factorials collapse to one
positive beta integral.  Exact formulas for `H_2[d,2]` and `H_2[d,3]` follow.

**REFUTED:** shifted ultra-log-concavity fails at `d=4,c=3`, with cleared
margin `-2424287232`.  The universal quantitative strengthening with surplus
`1+1/d` fails at `d=16,c=12`, with an exact negative integer certificate.
The direct same-orientation TP2/PF cavity route is obstructed: homogeneous
child degrees change TP orientation, and the raw scalar cavity coefficients
are not log-concave.

**EXACT FINITE:** ordinary H2 log-concavity and the exact full higher-core
budget have no failure through `d=18`.  The candidate H2 surplus `1+1/d^2`
also survives this cap.  These are finite falsification facts only.

**UNRESOLVED:** universal H2 log-concavity, any sufficient quantitative H2
surplus, a universal higher-core correction bound, full `H` log-concavity,
DEFECT NO-VALLEY, every downstream spectral gap, and both terminal outcomes.

## Field 2 — target, convention, and dependency boundary

The target is the auxiliary M113/M118 connected-unicycle incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
H[d,c]=M[d,d-c],
```

not the uniform identity-word law and not the lifted `bar_pi` law.  The
project convention is `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right; no new permutation manipulation occurs here.

The imported proved inputs are the M125/M129 exact cycle-type coefficient
formula and the M133/M136 subtraction-free unique-cycle expansion.  ULC and
real-rootedness of the total row were already refuted upstream and are not
reintroduced.  `H_2[d,c]` means exactly M133's core-length-two summand.

## Field 3 — marked-pair theorem and exact recurrence

For fixed indexed cycle atoms, an ordered pair of partitions is a bipartite
edge-labelled incidence multigraph.  On `|pi_L|+|pi_R|=|E|`, connectedness
makes it unicyclic.  Two atoms are co-blocked in both colours exactly when
their edges have the same two endpoints.  They then form a parallel-edge
cycle; uniqueness of the graph cycle makes this pair unique.  Conversely the
two core edges are co-blocked in both colours.  This proves the marked-pair
characterization.

For marked sizes `a,b` and unmarked multiset `nu`, the one-colour marked
partition polynomial is exactly

```text
P^bullet_(a,b;nu)(y)
 =y sum_(e<=nu)binom(nu,e)
    (a+b+||e||)^(|e|-1)P_(nu-e)(y).                   (3.1)
```

The marks lie in one join component.  Selecting its unmarked atoms gives

```text
C^bullet_nu
 =A^bullet_nu
  -sum_(proper e<nu)binom(nu,e)C^bullet_e A_(nu-e),   (3.2)
```

where `A^bullet=P^bullet(y)P^bullet(z)`.  Summing the unicycle diagonal over
unordered marked pairs isolates the H2 incidence polynomial exactly.  This
proves the multiset engine in `two_edge_core_scan.py`; finite comparison is an
audit, not the proof.

## Field 4 — exact cavity and Lagrange collapse

Define

```text
q_a=a^(2a+1)/(a!)^2,       xi_a=u q_a x^a.
```

This is exact because M125's type multiplier is
`d! product_a q_a^m_a/m_a!`.  With

```text
Phi_s(B)=sum_k 1/k! sum_bvec
            (s+sum b_i)^(k-2) product B_(b_i),
Psi_s(B)=sum_k 1/k! sum_bvec
            (s+sum b_i)^(k-1) product B_(b_i),
```

the unique positive formal cavity solution is

```text
T^L_a=y Phi_a(B^R), B^L_a=xi_a T^L_a,
T^R_a=z Phi_a(B^L), B^R_a=xi_a T^R_a.                (4.1)
```

The exact core species is

```text
U_2=yz/2 sum_(a,b)xi_a xi_b
              Psi_(a+b)(B^R)Psi_(a+b)(B^L).          (4.2)
```

The factor `1/2` is the unordered labelled core pair and treats equal sizes
correctly.  Root deletion proves (4.1)--(4.2) bijectively.

If `tau_B=sum_b B_b exp(b tau_B)`, Lagrange inversion proves

```text
Psi_s(B)=exp(s tau_B)/s.                              (4.3)
```

Thus, for `Q(X)=sum_a q_aX^a`, coefficientwise double integration
`I_2(sum f_nX^n)=sum f_nX^n/n^2`, and
`X=x exp(tau_L+tau_R)`,

```text
U_2=(u^2 yz/2)I_2(Q(X)^2).                            (4.4)
```

The remaining one-boundary transform has the exact positive representation

```text
Phi_s(B)=integral_0^1 t^(s-1)
            Psi_s((t^bB_b)_b)dt.                     (4.5)
```

This is a strict reduction: both core vertices are scalarized; only the
coupled multitype `Phi` cavity remains.

## Field 5 — beta cut transform and exact boundaries

Using

```text
j!(2d-j)!=(2d+1)! integral_0^1 t^j(1-t)^(2d-j)dt
```

and substituting `y=(1-t)/t`, `z=t/(1-t)` gives exactly

```text
H_2[d,c]
=d!(2d+1)![x^d u^c] integral_0^1 t^d(1-t)^d
 U_2(x,u,(1-t)/t,t/(1-t))dt.                         (5.1)
```

This absorbs every factorial cut weight into one positive integral.  Put
`S_n=sum_(a=1)^(n-1)q_aq_(n-a)`.  The first two cycle-count boundaries are

```text
H_2[d,2]=(d!)^3 S_d/(2d^2),                           (5.2)

H_2[d,3]=d!(d-1)!(d+1)!
 sum_(n=2)^(d-1)(S_n/n)q_(d-n)/(d-n)^2.              (5.3)
```

The complete formal proofs, including Lagrange coefficients and all powers,
are in `two_edge_core_reduction.md`.  `analytic_certificates.py` checks the
boundary formulas against all exact rows through `d=18` with zero failures.

## Field 6 — exact TP and curvature obstructions

In homogeneous child degree `k`, the `Phi` kernel in boundary size `s` and
total child size `S` is proportional to `(s+S)^(k-2)`.  For increasing rows
and columns, its `2x2` minors are positive for `k=0,1`, zero for `k=2`, and
negative for every `k>=3`.  The proof differentiates
`(s_2+S)/(s_1+S)`, which is strictly decreasing.  Hence degree summation mixes
TP orientations and the standard TP2 composition route cannot be used.

The scalar specialization begins

```text
Phi_1(t)=1+t/2+t^2/2+2t^3/3+...,
```

with first LC margin `-1/4`.  This refutes a raw PF/LC cavity proof but not
the final coupled coefficient inequality.

At `d=4`, the H2 row `(80136,109440,44928)` gives the exact shifted-ULC
counterexample

```text
109440^2-4*80136*44928=-2424287232.                   (6.1)
```

At `(d,c)=(16,12)`, the exact H2 masses at `c=11,12,13` are recorded in the
proof note and results JSON, and

```text
16 H_2[16,12]^2-17 H_2[16,11]H_2[16,13]
=-12068184285817619472004173248675719963879857493070204183335383575630227635520668657140147159040000000000.
                                                                    (6.2)
```

Thus no universal multiplicative surplus `1+1/d` is possible.

## Field 7 — bounded exact audits and higher-core budget

The marked recurrence matches frozen M133 core-two profiles exactly for all
`2<=d<=8`; there are zero mismatches.  The independent recurrence was then
capped at `d=18` as a falsifier.  There is no ordinary H2 log-concavity
failure.  The weakest tested ratio is

```text
H_2[18,13]^2/(H_2[18,12]H_2[18,14])
 ~=1.0315381584725043.                                (7.1)
```

The candidate inverse-square surplus survives through the cap, but this is
finite only.  With `E[d,c]=H[d,c]/H_2[d,c]`, every exact accepted full row
through `d=18` satisfies M133's budget inequality; the weakest tested ratio
of H2 curvature to higher-core correction is approximately
`1.0326546295475394` at `(18,13)`.  Neither sign is promoted to an asymptotic
claim.

`analytic_certificates.json` has zero reference, boundary, or transform
failures.  Its exact test minors for child degrees `0,1,2,3,4` are

```text
17/5184, 1/72, 0, -1/36, -17/576,
```

which self-attack all orientation cases around the transition.

## Field 8 — reproduction, provenance, and hygiene

Commands from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_scan.py --max-d 18 --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/analytic_certificates.py --h2-results experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/analytic_certificates.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/curvature_budget.py --h2-results experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/curvature_budget_results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, exact deterministic arithmetic, `seed=null`.

The computational lane was capped after the proof-critical `d<=18` payload.
Four obsolete duplicate analytic-search processes identified during the run
were terminated; none produced or contributed retained output.  No package,
commit, push, manuscript, project skill, coordinator file, predecessor file,
or other worker directory was changed.  Generated bytecode cache was removed.

## Field 9 — final verdict and next proof obligation

The ordinary two-edge-core theorem (1.1) is neither proved nor refuted.  The
deliverable is a strict positive reduction and two exact obstructions, not a
claim from finite signs.

The first remaining lemma is:

> Prove fixed-`x` coefficient log-concavity in `u` of the beta-integrated
> coupled `Phi` fixed point (5.1), with a quantitative surplus; separately
> bound the higher-core curvature
> `E[d,c-1]E[d,c+1]/E[d,c]^2` by that surplus.

The raw `Phi` kernels cannot be handled by a same-orientation TP/PF closure,
so a successful proof must exploit the coupled fixed point, the beta
functional, or cancellation across child degrees.  Even success would only
prove full `H` log-concavity after the higher-core comparison.  It would then
imply DEFECT NO-VALLEY and at most M120's conditional defect-projection gap;
fixed-defect expansion, `gap(A_d)`, the handle projection, and the original
lazy exact `{3,4,5}` heat-bath gap would remain open.  Neither Terminal A nor
Terminal B follows.
