# M110 fresh referee report on frozen M104

Date: 2026-08-12 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, accepted claim, and exact scope

```text
ACCEPT M104's exact fixed-seam product, comparison constants, conditional
restriction--projection inequality, and same-size circularity obstruction.
Material numbered objections: none.
```

For every realizable fixed seam key, M104 correctly proves a literal raw
product of two componentwise genus-zero side laws.  The exact lifted
conditional is its `1/ell` tilt, with a two-sided polynomial density bound.
Internal and seam signed-Hurwitz moves separate exactly.  The generalized
two-side M05 shuttle gives the valid conservative bounds

```text
gap(P_kappa) >= Gamma_0(d)/(420 D^10),
gap(L_kappa) >= Gamma_0(d)/(420 D^13),       D=2d-1, d>=3.
```

The generic restriction--projection calculation also correctly gives

```text
gamma_1(d)=gap(L)
 >= Gamma_0(d) beta(d)/(2940 D^13).
```

This is only a conditional reduction.  The decisive cell `kappa_e` contains
the same-`d`, full-label, minimal genus-zero Hurwitz walk, so the fixed-cell
route is circular and is not an induction.  This audit proves no polynomial
bound for `Gamma_0(d)`, `beta(d)`, or `gamma_1(d)`, no worst-source marked
hitting bound, no full lazy `{3,4,5}` heat-bath gap or mixing theorem, and
neither Terminal A nor Terminal B.

## 2. Frozen provenance and package integrity

All four assigned digests independently match:

| frozen M104 artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `a04c67103dd356d00b3c9ac267ba2eb255c69632d06707cb839ed8dd5ebb269b` |
| `fixed_fiber_decomposition.md` | `f0d2138d269e4695b545379500bc64ea64ebb849d757d06b87e8fd5e899a7def` |
| `results.json` | `184f00e909708a3ddac114eaebee54dd8f6c1b3a65710bbb2ba69c5d13c689e3` |
| `freeze_manifest.md` | `f36a625702a7b93dbebabc3ded4edcfda326ba3c85dae244bb52ed92ab8412f9` |

Running `sha256sum -c SHA256SUMS` in the M104 directory returned `OK` for
all seven entries.  The five dependency digests named by that manifest also
match: M97 report and manifest, M101 report, M05 report, and M05 referee
report.  M92/M95 were read only as frozen context.  No M104, predecessor,
coordinator, manuscript, project-skill, or shared durable artifact was edited.

## 3. Target, convention, kernel, boundary, and dependencies

The audited auxiliary target and kernel are

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected},
pi_d=Unif(X_d),
P_d=I/2+[1/(4D)]sum_(i=1)^D(R_i+R_i^(-1)),   D=2d-1,
R_i(a,b)=(b,bab),        R_i^(-1)(a,b)=(aba,a).
```

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  The accepted M97/M101 lift is

```text
A_d={(w,j):j in J(w)},
tilde_pi(w,j)=pi_d(w)/ell(w),
L((w,j),(w',j'))=P_d(w,w')/ell(w'),
gap(L)=gap(P_d)=gamma_1(d).
```

M97/M101 are imported only for the central-cut interval and exact spectrum.
M05 and its referee are imported for the shuttle method, whose specialization
and constants are independently reconstructed below.  No Classification-H
rate or transitivity assumption enters the positive fixed-cell statements.
If one of the factor spaces or projections is reducible, its declared gap is
zero and the lower bounds remain true but vacuous.

At `d=2`, the base, lift, and unique cell are singletons, with gap convention
one.  The displayed quantitative comparisons begin at `d>=3`.  Odd global
`m`, global `m=0`, `m=2`, and `N=2` are outside this auxiliary genus-one
problem and remain governed by the project's stated exceptional cases.

## 4. Literal product, factor counts, incidence, and side dependence

At a central cut `w=uv` after `j`, fix

```text
kappa=(j,p,Q_L,Q_R),       p=eval(u).
```

The side conditions—length, product, support partition, and componentwise
genus zero—separate once this key is fixed.  Realizability means that the
bipartite incidence multigraph with vertices `Q_L union Q_R` and one edge
per cycle of `p` is connected.  Since both side genera are zero, the M97
Euler identity gives

```text
|Q_L|+|Q_R|=c(p),
```

so that fixed incidence graph is unicyclic.  It depends only on the key.
Every pair of side factorizations therefore has identity total product,
connected total support, and the same central cut.  Conversely every word in
the cell supplies one such pair.  Hence, literally,

```text
C_kappa=U_kappa x V_kappa.
```

For a block `C` of either support partition, additivity of genus zero forces

```text
k_C=|C|+c(p_C)-2.
```

Scanning a component-color interleaving therefore gives the exact factor
count

```text
|U_kappa|=[j!/prod_C k_C!] prod_C |F(C,p_C,k_C)|,
```

and analogously on the right.  Isolates have `k_C=0` and one empty word.
There is no hidden component-length summation.

Now write `J(w)={b,...,h-1}`.  Starting from the fixed cut state
`(p,Q_L)`, the forward genus evolution uses only the suffix `v`; consequently

```text
r_R(v)=h-j.
```

After reversal, the state at the reversed cut is fixed by `(p,Q_R)`, and
continuation uses only `reverse(u)`; therefore

```text
r_L(u)=j-b+1.
```

It follows exactly that

```text
ell(u,v)=r_L(u)+r_R(v)-1,
1/ell(u,v)=integral_0^1
             z^(r_L(u)-1) z^(r_R(v)-1) dz.
```

Thus the lifted conditional is a nonnegative continuous mixture of product
weights.  M104 correctly refrains from treating that identity alone as a
Poincare inequality.

## 5. Internal/seam classification and the `D^3` lift comparison

A signed move wholly inside a side preserves the ordered side product.  On
the affected pair it also preserves the support-component partition: equal,
disjoint, and one-endpoint-intersecting transposition pairs can be checked
directly.  Hence it preserves `kappa`; the side genera stay zero and the cut
stays admissible.

Across the seam, let the old prefix end in `a` and the suffix begin with
`b`.  If its product is `p`, the two new prefix products are

```text
pab       and       pba.
```

Either equals `p` exactly when `a=b`; in that case both signed moves fix
`(a,a)` literally.  Therefore no nontrivial seam move remains in a fixed
cell.

For `C=|C_kappa|` and
`S=sum_(x in C_kappa)1/ell(x)`, the lifted conditional density is

```text
nu(x)=1/[S ell(x)],
d nu/d mu=C/[S ell(x)],           C/D<=S<=C.
```

Thus its density ratio lies in `[D^-1,D]`.  For an off-diagonal internal
edge `(x,y)`, the lifted/raw stationary-flow ratio is

```text
C/[S ell(x)ell(y)] in [D^-2,D].
```

The variance ratio also lies in `[D^-1,D]`, by minimizing squared distance
to a constant under the two measures.  Comparing the Dirichlet and variance
forms therefore gives exactly the accepted conservative bounds

```text
D^-3 gap(P_kappa) <= gap(L_kappa) <= D^2 gap(P_kappa).
```

The lower `D^3` loss is the one used later.  No unrecorded cut-refresh edge
is needed: every transition ending outside the same fixed cut/key is held in
the standard restriction.

## 6. Two-side M05 shuttle and the constants `420 D^10`, `420 D^13`

The generalized ideal product chain retains exactly two side-color slots,
even when a color coordinate is a singleton identity chain, together with
all nontrivial internal component coordinates.  If `s` is its slot count,
the unicyclic identity gives

```text
2<=s<=|Q_L|+|Q_R|+2=c(p)+2<=d+2<=3D.
```

Every side has length at most `D+1`.  Its half-lazy adjacent multiset-color
gap is at least `1/(4D^3)`, and every internal-coordinate gap is at least
`Gamma_0(d)`.  Since `Gamma_0(d)<=1`, equal-slot tensorization yields

```text
gap(P_*)>=Gamma_0(d)/(12D^4).
```

The source-recovery accounting is also correct:

- each requested internal move shuttles consecutive same-component factors
  through disjoint side components and back, in fewer than `4D` moves;
- metadata `(side,component,u,v,orientation,stage)` has fewer than
  `16D^4` values;
- a fixed directed physical edge and fixed metadata recover at most one
  source by inverse prefix;
- an ideal labeled internal flow is at most `mu/8`, because `s>=2`;
- every used physical directed edge has capacity at least `mu/(4D)`.

Consequently the internal comparison congestion is at most

```text
(16D^4)(mu/8)(4D)/(mu/(4D))=32D^6.
```

Direct side-color swaps contribute at most `3D`; adding possible collisions
gives at most `35D^6`.  Therefore

```text
gap(P_kappa)
 >=[Gamma_0(d)/(12D^4)]/[35D^6]
 =Gamma_0(d)/(420D^10).
```

Section 5's lower lift comparison adds `D^3`, proving

```text
gap(L_kappa)>=Gamma_0(d)/(420D^13).
```

The two identity slots, full physical scan `4D`, orientation multiplicity,
path length, and stage metadata are all present; no omitted normalization was
found.

## 7. Projection constant, PSD, and the decisive circular cell

The stationary-flow projection `bar L` is the orthogonal compression of
the PSD lift `L` to cell-constant functions, hence is itself reversible and
PSD.  Let

```text
alpha=min_kappa gap(L_kappa),       beta=gap(bar L).
```

For `g_k=E[f|C_k]`, the pointwise three-term inequality across cells gives

```text
E_barL(g,g)<=3 E_L(f,f)+3 W,
W=sum_k bar_pi(k) Var(f|C_k).
```

The two endpoint terms contribute together at most `3W`; there is no extra
factor two under the convention
`E=(1/2)sum Q(x,y)(f(x)-f(y))^2`.  Since `W<=E_L/alpha`, total variance obeys

```text
Var(f)<= [1/alpha+3/beta+3/(alpha beta)] E_L(f,f)
       <= [7/(alpha beta)] E_L(f,f),
```

using `alpha,beta<=1`.  Thus `gap(L)>=alpha beta/7`, and
`2940=7*420` is correct.  If either gap is zero, the claimed lower bound is
trivially valid.

The decisive route obstruction is the realizable key

```text
kappa_e=(2d-2,id,{[d]},
         {{endpoints(e)} plus all other isolates}).
```

Its cell is exactly

```text
Z_d x {(e,e)},
Z_d={connected identity words on [d] of length 2d-2}.
```

Only the `D-2=2d-3` adjacent positions inside `Z_d` can make an off-diagonal
restricted move.  The right-square position and seam position are held.
Hence

```text
P_kappa_e=[(D-2)/D]P_0,d+[2/D]I,
gap(P_kappa_e)=[(D-2)/D]gap(P_0,d)       (d>=3).
```

At `d=2`, both chains are singleton identities and use gap convention one.
For `d>=3`, this exposes the full-label minimal genus-zero gap at the same
label size `d`; neither labels nor a known complexity parameter decreases.
The bounded lift tilt does not repair that circularity.  This is a rigorous
obstruction to the proposed induction, not evidence that any chain is slow.

## 8. Independent computation, reproduction, self-attack, and hygiene

`independent_audit.py` was written from scratch with the Python standard
library and imports no M104 or predecessor code.  The command was

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M110-m104-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M110-m104-fresh-referee/independent_results.json
```

It is deterministic (`seed=null`), used Python `3.12.3`, and has no
nonstandard dependency.  It exhausted the full `d=2,3` genus-one spaces and
the decisive `d=4` circular cell:

| audit | base words | lifted incidences | cells | failures |
|---|---:|---:|---:|---:|
| full `d=2` | 1 | 1 | 1 | 0 |
| full `d=3` | 240 | 336 | 9 | 0 |
| `d=4` `kappa_e` | 2,880 left times 1 right | 2,880 checked | 1 | 0 |

At `d=3`, all 2,688 internal and 672 seam proposals passed, as did every
Cartesian count, incidence, forced component length, side-dependence, and
integral check.  Exact observed density ratios ranged from `16/37` to
`36/23`; internal-edge flow ratios ranged from `8/37` to `36/23`, within the
proved universal bounds.

At `d=4`, the independent circular-cell histogram was

```text
ell:   1    2    3    4    5
count: 480  744  936  528  192,
```

and the raw scan identity was `5/7 P_0,4 + 2/7 I`.  These finite facts are
falsifiers and proof calibration only; none supplies asymptotic expansion.

The strongest self-attack is precisely the accepted circularity: both open
inputs may contain the same difficult full-label geometry.  The standard
restriction theorem cannot be advertised as progress toward an induction
without an independent `Gamma_0` estimate or a mean-lift argument bypassing
bad cells.  The full heat bath also has `H4/H5` moves absent from this
auxiliary Hurwitz analysis, so no negative full-kernel conclusion follows.

All M110 artifacts are confined to its assigned directory.  Bytecode was
disabled; cache and final shared-worktree status are recorded in the freeze
manifest.

## 9. Final verdict, objections, and first open obligations

**ACCEPT, with zero material numbered objections.**

The exact fixed-cell algebra, `D^3` density/flow comparison, generalized
two-side M05 recovery, constants `420D^10`, `420D^13`, projection factor
`1/7`, and combined constant `2940D^13` are all valid.  Promote the exact
product/comparison theorem and, especially, `kappa_e` as the decisive
same-size circularity obstruction to this standard decomposition route.

The following remain **UNRESOLVED** and must remain visibly open:

```text
Gamma_0(d) >= d^(-O(1)),
beta(d) >= d^(-O(1)),
gamma_1(d) >= d^(-O(1)),
worst-source marked hitting for M92,
the full lazy {3,4,5} heat-bath gap and mixing time,
Terminal A and Terminal B.
```

No terminal or project-level polynomial-mixing conclusion follows from the
accepted M104 package.
