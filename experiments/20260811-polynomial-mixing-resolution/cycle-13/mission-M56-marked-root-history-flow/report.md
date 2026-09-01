# M56 final report: marked root histories and contextual spine reduction

Date: 2026-08-11.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, and convention

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  For every `r>=1`, this report concerns the full
**nonlazy** stationary-flow parking-degree projection `Pbar_r` of the
uniform scan of adjacent rank-two heat baths on minimal factorizations of
`(0 1 ... r)`.  Its stationary law is

```text
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!],
alpha_r=2/[3r(r-1)]          (r>=2).
```

It does not concern the original identity bridge chain `K`.

The assigned ROOT-MEAN LIFT and polynomial-gap claim remain open.  The
following scoped statements are proved universally unless explicitly
labelled finite.

1. Canonical marked coalescence has the exact reverse-history density
   recurrence (2.2) and factorial partition (6.4) in
   `marked_history_recurrence.md`, with
   ```text
   E H_j=(j+1)! binom(r-1,j)/r^j<=j+1.
   ```
   Exact stationary endpoint normalization is false already at `r=3`.

2. For every coarse root composition `b`, fixed refinement `a` which
   splits branch `i`, and local branch macro `u_i in J_(c_i-1)`,
   ```text
   p_(b,a)(d)=alpha_r phi_(r,b,a,i)(u_i).
   ```
   Thus an individual split bias is universally contextual-branch-local.

3. If `s=c_i-1`, the exact dual-norm coefficient is
   ```text
   ||ell_(b,a)||_(-1,b)^2/q_(b,a)
    =||p^ctx_s-Ep^ctx_s||_(-1,Pbar_s)^2/Ep^ctx_s,
   p^ctx_s=alpha_s phi.
   ```
   The factor `alpha_r/gamma_i=alpha_s` cancels exactly.

4. Every contextual suffix statistic has a universal one-active-branch
   recursion.  Conditional on inner root composition
   `C=(c_1,...,c_k)` and fixed suffix size `B`, it is zero if
   `c_k<B`, constant on the entire `C` fibre if `c_k=B`, and if
   `c_k>B` it is another contextual suffix statistic depending only on
   the last-branch macro.

5. In a marked network with separate capacity copies for quotient-edge
   residual commodities, the exact demand-flow recurrence is
   ```text
   T_s(f)<=a(f)+[delta(f)+a(f)] max_(t<s)T_t,
   delta(f)=E[f 1_(c_k>B)]/Ef,
   a(f)=||E[f|root composition]-Ef||_(-1,R_s)^2/Ef.
   ```
   This is an accounting identity, not yet a flow bound in the actual
   unmarked chain.

These results are nonterminal even for `Pbar_r`, and a fortiori are not
Terminal A or B for `K`.

## 2. Full argument and constructions

### 2.1 Marked histories

In root-degree layer `L_k`, merging the first boundary has total rate
`alpha_r k`; choosing its actual destination proportionally defines a
stochastic kernel.  Reversibility yields the exact layer recurrence

```text
h_(k-1)(y)=p_(k-1)
 +[p_(k-1)/(p_k alpha_r k)]
   sum_(x:first-merge(x)=y)P(y,x)h_k(x).
```

For a reverse nested history, put `a_j=P(y_(j-1),y_j)/alpha_r`.
The stationary degree ratio and the forward `alpha_r j` normalization
cancel, giving a factor `a_j/j).  Therefore the unary endpoint density is

```text
g_r(y)=p_1 sum_(j=0)^(r-1) H_j(y)/(j+1)!,
p_1=(r/(r+1))^(r-1)>=e^(-1).
```

Mass supplied by original layer `j+1` proves the displayed exact first
moment in Field 1.  At `r=3`, however, root composition `(1,2)` merges
only to macro `(0,1,2)`, while the unary conditional stationary law puts
masses `1/3,2/3` on `(0,1,1),(0,1,2)`.  Thus a valid cut mark does not
normalize away after it is forgotten.

### 2.2 Universal contextual locality

For each root branch, restrict the noncrossing factor tree to its preorder
interval, close factor-number gaps, and standardize.  Goulden--Yong
sufficiency makes this a root-unary local factorization.  Conversely,
shuffle the local words preserving local order and requiring their
distinguished root attachments in reverse child order.  These operations
are inverse.

The local orbit has

```text
|O^+_u|=c!/product_v d_v!.
```

Its unique lower-zero factor occupies every local word position equally
often.  For a marked split pair inside branch `i`, the number of global
shuffles which leave the pair consecutive depends only on fixed part sizes
and marked local positions.  Summing all other branch words contributes
`product_(j!=i)|O^+_(u_j)|`, while

```text
|O_d|={r!/[k! product_j c_j!]} product_j |O^+_(u_j)|.
```

All other branch factors cancel after division by the exact
`3(r-1)|O_d|` scan/fibre/orbit normalization.  This proves contextual
locality without asserting the false scalar equality to an ordinary unary
split.

Conditioning the contextual observable on its inner root composition
gives a second constrained shuffle: the external attachment is a
distinguished singleton and the remaining factors split into inner
root-branch words.  The right spine enters only the last branch.  If that
branch is too small the suffix is impossible.  At equality the marked cut
factor is its distinguished attachment; uniform attachment positions and
orbit-factor cancellation make the rate constant over the fibre.  Above
equality, summing every other branch leaves a new position-weighted
statistic only on the last branch.  This proves the one-active-branch
recursion.

### 2.3 Exact norm and flow scaling

Conditioned on `b`, the law is the product of `pi_(c_j-1)`, and the
rejected-exit form assigns branch `i` coefficient

```text
gamma_i=s(s-1)/[r(r-1)].
```

Conditional expectation onto coordinate `i` reduces energy and local
tests attain equality.  Since `alpha_r/gamma_i=alpha_s`, the dual norm
identity in Field 1 follows.

At a deeper active size `t<s`, both the contextual demand and its internal
capacity are multiplied by

```text
gamma_(s,t)=t(t-1)/[s(s-1)]=alpha_s/alpha_t.
```

Thus energy scales linearly by `gamma`, and products telescope to
`t(t-1)/[s(s-1)]`.  Summing conditional residual demands costs exactly
`delta(f)Ef max T_t`.

For a quotient electrical flow `theta`, disintegrating one edge in
stationary-flow proportions costs `theta_e^2/Q_R(e)`.  The refined
endpoint is stationary because its merge rate is pointwise constant.  The
coarse residual is

```text
theta_e pi(.|b)[p_e/q_e-1].
```

Contextual locality turns it into a lower-rank demand, whose scaled energy
is exactly `T_t theta_e^2/Q_R(e)`.  Adding marked commodities gives the
recurrence in Field 1 with every probability and capacity retained.

## 3. Probability, runtime, path, and congestion accounting

- Actual pair scan: `r-1` sites; nontrivial pair fibre: three states;
  `alpha_r=2/[3r(r-1)]).
- Canonical coalescence uses at most `r-1` merges.  Its endpoint density
  is at least `e^-1); no universal upper-density theorem is claimed.
- The accepted root quotient has gap
  `2/[9e r(r-1)]` and canonical path length at most `2(r-1)`.
- A branch of internal size `s` receives exact action fraction
  `s(s-1)/[r(r-1)]`.
- Recursive products of action fractions telescope exactly; they are not
  multiplied Radon bounds.
- Fine disintegration of quotient edge `e` has base energy
  `theta_e^2/Q_R(e)`; its labelled residual has energy exactly that
  quantity times its lower-rank contextual coefficient.
- Exact finite quotient solves through ambient `r=7` give
  `max[delta+a]<0.864` and
  `max a/(1-delta)<0.383`.  They do not prove an asymptotic inequality.
- Exact scripts enumerate all Catalan parking macros and up to
  `8^6=262144` raw factorizations at `r=7`; their exponential runtime
  makes them falsifiers only.  All operations in the proved shuffle
  bijections and recurrences are polynomial in a represented word/tree,
  but no full-chain sampler or congestion theorem results.

## 4. Dependencies, labelled

- **Proved/accepted:** M50 full child-boundary support/rate, root stationary
  law, exact fixed-composition product restrictions; M41 Section 11
  root-quotient gap; M54 right-spine support and H-minus reduction.
- **Cited with conventions already checked in the frozen inputs:**
  Stanley--Biane parking-multiset enumeration and Goulden--Yong
  noncrossing-factor-tree order/sufficiency.
- **Proved here:** marked-history recurrence and first moments; smallest
  normalization counterexample; contextual branch locality; exact
  `alpha/gamma` dual-norm cancellation; recursive last-branch locality
  and top-fibre constancy; marked separated-capacity recurrence.
- **Refuted here:** exact stationary endpoint normalization; rigid
  distinguished-leaf routing; scalar contextual-to-unary rate reduction.
- **Empirical exact finite:** endpoint chi-square, unmarked replant
  distances, contextual and recursive collision checks through `r=7`,
  and floating quotient electrical coefficients.
- **Fresh-refereed dependency:** frozen M58 is ACCEPTED in
  `m58_fresh_referee.md`; the coordinator promoted it separately.
- **Conditional:** a polynomial full-`Pbar_r` gap follows only after both
  contextual quotient absorption and actual-edge source recovery are
  proved and then inserted into M54/M50.

## 5. First unproved standalone proposition

> **CONTEXTUAL QUOTIENT ABSORPTION.**  For every rank `s>=2` and every
> contextual suffix-cut observable `f=alpha_s phi` obtained by the
> constrained-shuffle disintegrations above, with suffix size `B`,
> ```text
> ||E[f|root composition]-Ef||_(-1,R_s)^2
>  <=E[f 1_(last root branch size=B)].
> ```

Because `f=0` below `B`, this is exactly `a(f)<=1-delta(f)`.  Even
after this proposition, **MARKED ADDITIVE SOURCE RECOVERY** from
`additive_flow_recurrence.md` must show that edge-labelled recursive
commodities project to actual capacities with additive polynomial load.

## 6. Self-attack

The most dangerous point in the proved locality theorem is the
constrained-shuffle factorization: it requires the full accepted
Goulden--Yong sufficiency, not merely necessity of local clockwise order.
The proof explicitly preserves every local order and imposes the only new
root inequalities; omitting either condition would invalidate the inverse.

The marked recurrence currently duplicates capacities by quotient-edge
history.  In the real chain, `(sum_j F_j(e))^2` cannot be replaced by
`sum_j F_j(e)^2` without cancellation, disjointness, or a source-recovery
bound.  A crude factor equal to the number of contexts at each depth would
be multiplicative and can be exponential.  The exact values
`delta+a<1` through `r=7` neither prove quotient absorption nor address
this collision.  First moments of marked histories likewise do not control
two-history edge intersections.

## 7. Calibrations

- `r=1` is a singleton; all dual norms use the zero convention.
- `r=2` has the exact two-state root quotient and no nontrivial recursive
  branch.
- `r=3` is the first endpoint-normalization failure and is retained.
- Stars, paths, rare/balanced degrees, and every macro through `r=7` occur
  in the exact audits.
- The ordinary scalar local formula already fails at `r=4`; contextual
  locality survives.
- The literal unary harmonic propensity bound fails at `r=7`
  (`157/60=H_7+1/42`); it is not used.
- The restricted M48 leaf-rotation separator and rigid marked-leaf
  obstruction are not lifted to full `Pbar_r`.
- No claim here treats odd identity-word length, `m=0,2`, `N=2`, or
  near-minimal identity factorizations, because this scoped long-cycle
  projection is not `K`.

## 8. Artifacts and exact reproduction

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/marked_history_audit.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/marked_history_n8.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/nested_history_probe.py --n-max 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/nested_history_n8.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/split_context_locality.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/split_context_locality_r7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/recursive_contextual_locality.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/recursive_contextual_locality_r7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/contextual_macro_energy.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M56-marked-root-history-flow/contextual_macro_energy_r7.json
```

Python 3.12.3, NumPy 1.26.4 and SciPy from the recorded environment; no
random seed is used.  The proof details are in
`marked_history_recurrence.md`, `contextual_hminus_reduction.md`, and
`additive_flow_recurrence.md`.  The bounded scripts state exactly which
universal claim a failure could refute.

## 9. Verdict

OPEN AT A NAMED STEP: CONTEXTUAL QUOTIENT ABSORPTION.
