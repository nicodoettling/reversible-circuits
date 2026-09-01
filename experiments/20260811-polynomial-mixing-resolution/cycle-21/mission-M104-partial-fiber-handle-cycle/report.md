# M104 final report: exact fixed handle-cycle fibers and circularity

Date: 2026-08-12. Repository commit at execution:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, target, convention, and exact scope

```text
PROMOTE: exact fixed-seam product law, polynomial lift comparison, and a
         conditional restriction--projection inequality.
OBSTRUCTION: one fixed cell is the same-d full-label minimal genus-zero
             Hurwitz walk, so the construction is not inductive.
UNRESOLVED: both the side gap Gamma_0(d) and seam projection gap beta(d).
```

Fix `d>=2`, `D=2d-1`, and

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected},
pi_d=Unif(X_d).
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The auxiliary half-lazy signed adjacent-Hurwitz kernel is

```text
P_d=I/2+[1/(4D)]sum_(i=1)^D(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

M97's accepted lift is

```text
A_d={(w,j):j in J(w)},             ell(w)=|J(w)|,
tilde_pi(w,j)=pi_d(w)/ell(w),
L((w,j),(w',j'))=P_d(w,w')/ell(w').
```

M97/M101 prove `gap(L)=gap(P_d)=gamma_1(d)`.  This mission proves no
inverse-polynomial value for that gap, no M92 marked-hitting bound, no full
lazy `{3,4,5}` heat-bath gap or mixing theorem, and no Terminal claim.  It
uses no quantitative Classification H and no canonical-word routing.

At `d=2`, both base and lifted spaces are singletons and all gaps use the
declared singleton value one.  The quantitative content begins at `d>=3`.

## 2. Exact fixed-cell law and proved decomposition

At a central cut `w=uv` after `j`, put

```text
p=eval(u), Q_L=support partition of u,
Q_R=support partition of v,
kappa=(j,p,Q_L,Q_R).
```

For every realizable key, define side sets `U_kappa,V_kappa` by fixing their
respective length, product, support partition, and componentwise genus zero.
The fixed cell is literally

```text
C_kappa=U_kappa x V_kappa.                            (2.1)
```

The proof is exact.  The two membership conditions separate.  The incidence
multigraph determined only by `(p,Q_L,Q_R)` is connected unicyclic because
the key is realizable, so every pair has connected total support.  Conversely
every cell word supplies one pair.

If `C` is a block of `Q_L`, genus zero fixes its factor count to

```text
k_C=|C|+c(p_C)-2.
```

Consequently

```text
U_kappa=I_(k_C:C in Q_L) x product_C F(C,p_C,k_C),
|U_kappa|=[j!/product_C k_C!] product_C|F(C,p_C,k_C)|,
```

with the analogous right-side formula.  Thus conditioning on
`p,Q_L,Q_R` introduces no hidden component-length sum.

The raw law `mu_kappa=Unif(C_kappa)` is an independent side product.  The
lifted conditional `nu_kappa` is

```text
nu_kappa(x)=1/[S_kappa ell(x)],
S_kappa=sum_(x in C_kappa)1/ell(x),
D^(-1)<=d nu_kappa/d mu_kappa<=D.                     (2.2)
```

There is also an exact noncanonical product-mixture representation.  At
fixed key,

```text
r_L(u)=j-b(uv)+1,       r_R(v)=h(uv)-j,
ell(u,v)=r_L(u)+r_R(v)-1,
1/ell(u,v)=integral_0^1 z^(r_L(u)-1)z^(r_R(v)-1) dz.  (2.3)
```

The side dependence follows because the state at the cut is fixed: forward
continuation to `h` uses only `v`, while reversed continuation to `b` uses
only `reverse(u)`.  Equation (2.3) makes the lift an exact mixture of product
tilts, but a mixture alone is not a Poincare theorem.

Every signed move wholly inside one side preserves its ordered product and
generated support partition, hence preserves the fixed key and cut
admissibility.  A seam move on boundary factors `a,b` changes the prefix
product from `p` to `pab` or `pba`; it preserves `p` exactly when `a=b`, and
then both orientations are literal self-loops.  Thus all nontrivial seam
motion leaves the fixed cell.

Let `P_kappa` be the uniform-law rejected-exit restriction of `P_d` with the
cut held fixed, and `L_kappa` the standard restriction of the exact lift.
For distinct `x,y` in the cell, their stationary edge-flow ratio is

```text
Q_Lk(x,y)/Q_Pk(x,y)
 =|C_kappa|/[S_kappa ell(x)ell(y)] in [D^(-2),D].      (2.4)
```

Together with `D^-1 Var_mu<=Var_nu<=D Var_mu`, this proves

```text
D^(-3)gap(P_kappa)<=gap(L_kappa)<=D^2 gap(P_kappa).   (2.5)
```

## 3. Exact probability, scan, path, congestion, and gap accounting

Define `Gamma_0(d)` as the minimum gap of the half-lazy signed-Hurwitz chain
over every connected component-factorization space `F(C,q,k)` appearing in
any realizable side cell on `[d]`, with

```text
k=|C|+c(q)-2,
H_(C,q,k)=I/2+[1/(4(k-1))]sum_r(R_r+R_r^(-1))
```

when `k>=2`; singleton coordinates have gap one.  If any such whole factor
space is reducible, its gap and hence `Gamma_0(d)` are zero.  This definition
does not assume Classification H.  A uniform inverse-polynomial lower bound
for `Gamma_0(d)` is **UNRESOLVED**.

The accepted M05 shuttle comparison extends literally to the two side
products.  Retain two side-color mixture slots even when singleton, and all
nonempty internal coordinates.  The unicyclic identity
`|Q_L|+|Q_R|=c(p)<=d` gives a slot count `2<=s<=d+2<=3D`.  Therefore the
ideal independent-coordinate chain has

```text
gap(P_*)>=Gamma_0(d)/(12D^4).                         (3.1)
```

The accounting is:

- base holding probability: `1/2`;
- every physical oriented proposal: `1/(4D)`;
- shuttle length: `<4D`;
- recovery metadata `(side,component,u,v,orientation,stage)`: `<16D^4`;
- each ideal labeled internal flow: at most `mu/8`, using `s>=2`;
- every used physical-edge capacity: at least `mu/(4D)`;
- internal comparison congestion: at most `32D^6`;
- direct side-color congestion: at most `3D`;
- total comparison congestion: at most `35D^6`.

No path visits a canonical word.  Fixed metadata and a used edge recover the
source by inverse prefix, as in accepted M05.  Hence

```text
gap(P_kappa)>=Gamma_0(d)/(420D^10),
gap(L_kappa)>=Gamma_0(d)/(420D^13),       d>=3.        (3.2)
```

Now partition `A_d` by the cells and let `bar L` be the exact stationary-flow
projection.  It is reversible and positive semidefinite, being the
compression of `L` to cell-constant functions.  Define

```text
beta(d)=gap(bar L).                                    (3.3)
```

An inverse-polynomial lower bound for `beta(d)` is **UNRESOLVED**.  If
`alpha=min_kappa gap(L_kappa)`, conditional variance plus
`(g_k-g_l)^2<=3[(f_x-f_y)^2+(f_x-g_k)^2+(f_y-g_l)^2]` gives exactly

```text
gap(L)>=alpha beta/7.                                  (3.4)
```

Combining (3.2)--(3.4) with M97's spectrum identity proves only the
conditional implication

```text
gamma_1(d)>=Gamma_0(d)beta(d)/[2940D^13],  d>=3.      (3.5)
```

Constructing a shuttle takes `O(d)` signed operations.  The finite audit is
deterministic and uses no random seed or nonstandard dependency.

## 4. Dependencies and claim-status ledger

| claim or input | status here | dependency/evidence |
|---|---|---|
| M97 central-cut interval and exact lift | imported, independently accepted by M101 | frozen M97/M101 reports |
| raw fixed-cell product and component counts | proved | Section 2 / proof note |
| `1/ell` RN bound and product-mixture identity | proved | equations (2.2)--(2.3) |
| internal preservation and seam separation | proved | literal Hurwitz algebra |
| fixed-cell flow/gap comparison | proved | equations (2.4)--(2.5) |
| M05 shuttle/recovery method | imported accepted method, re-specialized here | frozen M05 report/referee |
| constants `420D^10`, `420D^13` | proved candidate pending fresh audit | full accounting in proof note |
| generic `alpha beta/7` decomposition | proved | direct variance calculation |
| `Gamma_0(d)>=d^{-O(1)}` | unresolved | contains same-size minimal genus-zero input |
| `beta(d)>=d^{-O(1)}` | unresolved | no seam-flow estimate obtained |
| Classification H | conditional project dependency | not used in positive statements |
| finite `d<=4` results | exact finite facts only | `fixed_seam_audit.py`, `results.json` |
| `gamma_1`, M92 cover, full heat-bath gap | unresolved | no unconditional implication |

The `420/2940` quantitative specialization should receive a fresh referee
before coordinator promotion.  The algebraic product law and exact circular
cell do not depend on those constants.

## 5. First unresolved standalone obligations

The coordinate route now has two explicit quantitative obligations:

> **GENUS-ZERO SIDE GAP.**  Prove `Gamma_0(d)>=d^{-O(1)}` for every `d>=3`,
> including connected minimal identity words on all `d` labels.

> **HANDLE-CELL PROJECTION GAP.**  Prove `beta(d)>=d^{-O(1)}` for the exact
> stationary-flow projection of (1.2) onto
> `kappa=(j,p,Q_L,Q_R)`.

Together they imply an inverse-polynomial `gamma_1(d)` through (3.5), which
would feed M92's accepted two-component partial-macro cover.  Neither is
proved here.  The second alone does not bypass the first under the standard
restriction decomposition.

## 6. Strongest self-attack: exact same-size circularity

Fix an edge `e` and the realizable cell

```text
kappa_e=(j=2d-2,p=id,Q_L={[d]},
         Q_R={{endpoints(e)} plus all other isolates}).
```

It is exactly

```text
C_kappa_e=Z_d x {(e,e)},
Z_d={connected identity words on [d] of length 2d-2}.  (6.1)
```

Let

```text
P_0,d=I/2+[1/(4(2d-3))]
                sum_(i=1)^(2d-3)(R_i+R_i^(-1)).
```

The raw restriction has the exact kernel identity

```text
P_kappa_e=[(D-2)/D]P_0,d+[2/D]I,                      (6.2)
```

and, for `d>=3`,

```text
gap(P_kappa_e)=[(D-2)/D]gap(P_0,d).                   (6.3)
```

At `d=2`, both kernels are the singleton identity and both gaps are one by
convention.  Equations (6.1)--(6.3) are the decisive route obstruction:
fixed-cell tensorization exposes the minimal genus-zero Hurwitz gap at the
same label size `d`.  It decreases neither labels, length scale, nor a known
complexity parameter.  The `1/ell` tilt changes its gap only by polynomial
comparison factors.  Therefore this is a circular sufficient reduction, not
an induction and not a proof of `gamma_1(d)`.

This does not show that the genus-zero, genus-one, or full heat-bath chain is
slow.  A projection/mean-lift argument might bypass slow restrictions, and
the full heat bath has `H4/H5` moves absent here.  The obstruction is scoped
only to the proposed standard fixed-cell decomposition route.

## 7. Boundary cases and exact finite falsification audit

The deterministic audit exhausts only `d=2,3,4`.

| `d` | candidate words | base states | lifted states | seam cells | largest cell |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 729 | 240 | 336 | 9 | 64 |
| 4 | 1,679,616 | 131,040 | 234,720 | 101 | 9,216 |

It found zero raw-product count failures, zero side handle-distance failures,
zero incidence or component-length failures, and zero failures among
`2,819,332` wholly internal oriented proposals.  Nontrivial seam proposals
never stayed in one key: at `d=3`, the 672 seam proposals split as 228
self-loops, 180 changed-key admissible moves, and 264 losses of this cut; at
`d=4`, the corresponding counts are 76,656, 173,232, and 219,552.

The maximum within-cell `ell` ratio is exactly `1,3,5=D`.  The circular cell
has `1,24,2880` left words and one right word.  At `d=4`, its `ell` histogram
is

```text
ell:   1    2    3    4    5
count: 480  744  936  528  192.
```

Thus the lifted conditional is visibly not the raw uniform product even in
the circular cell.  These are exact finite calibrations and falsifiers only;
they are not asymptotic expansion evidence.

Odd global `m`, global `m=0`, `m=2`, and `N=2` do not alter this scoped
auxiliary theorem.  They remain governed by the project boundary conventions.

## 8. Artifacts, reproduction, runtime, and hygiene

Owned artifacts are

```text
plan.md
checkpoint.md
fixed_fiber_decomposition.md
fixed_seam_audit.py
results.json
report.md
freeze_manifest.md
SHA256SUMS
```

Reproduction command from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M104-partial-fiber-handle-cycle/fixed_seam_audit.py \
  --d 2 3 4 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M104-partial-fiber-handle-cycle/results.json
```

Python `3.12.3`; seed `null`; dependencies `{}`; elapsed time recorded in the
raw result is `42.33237266540527` seconds.  The run is deterministic.
Bytecode was disabled.  Cache and final shared-worktree status are recorded
in the freeze manifest.  Only the owned M104 directory was edited.

## 9. Verdict and exact implication for M97/M92

**PROMOTE AFTER FRESH CONSTANT AUDIT:** the exact fixed-seam raw fiber is a
product of two componentwise genus-zero side laws; the lifted conditional is
a bounded `1/ell` tilt with an exact product-mixture formula; internal and
seam moves separate exactly; fixed-cell and projection decomposition losses
are polynomial and explicit.

**PROMOTE AS ROUTE OBSTRUCTION:** the cell `kappa_e` is exactly the same-`d`
minimal genus-zero Hurwitz walk up to the displayed scan slowdown.  Standard
fixed-cell tensorization is therefore circular and supplies no induction.

**UNRESOLVED:** `Gamma_0(d)`, `beta(d)`, `gamma_1(d)`, worst-source marked
hitting, M92's unconditional two-component cover, global heat-bath gap and
mixing, and both Terminal criteria.  No project-level mixing claim follows.
