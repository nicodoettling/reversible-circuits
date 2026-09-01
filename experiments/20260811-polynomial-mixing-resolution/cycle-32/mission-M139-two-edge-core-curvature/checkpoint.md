# M139 halfway checkpoint

Date: 2026-08-13 UTC.

## Decisive progress

The two-parallel-edge core has an exact marked-pair characterization: in a
connected-unicyclic bipartite incidence multigraph, the core has length two
if and only if there is a unique unordered pair of edge-atoms that lie in a
common left block and a common right block.  Marking that pair gives an exact
rooted connected-component recurrence aggregating all unmarked equal-size
atoms by binomial multiplicity.  The new implementation matches every frozen
M133 two-edge profile through `d=8` exactly.

The marked species also has a compact formal generating-function reduction.
Put

```text
q_a = h(a)^2/a = a^(2a+1)/(a!)^2,
xi_a = u q_a x^a.
```

For a boundary-size `s` and child vector `B`, define

```text
Phi_s(B)=sum_k 1/k! sum_(b_1,...,b_k)
             (s+sum b_i)^(k-2) product_i B_(b_i),
Psi_s(B)=sum_k 1/k! sum_(b_1,...,b_k)
             (s+sum b_i)^(k-1) product_i B_(b_i).
```

The unique formal cavity solution is

```text
T^L_a=y Phi_a(B^R),   B^L_a=xi_a T^L_a,
T^R_a=z Phi_a(B^L),   B^R_a=xi_a T^R_a.
```

Then the exact two-edge-core EGF is

```text
U_2 = yz/2 sum_(a,b) xi_a xi_b
                  Psi_(a+b)(B^R) Psi_(a+b)(B^L).
```

If `tau_B=sum_b B_b exp(b tau_B)`, Lagrange inversion gives the exact
collapse

```text
Psi_s(B)=exp(s tau_B)/s.
```

Thus, with `Q(X)=sum_a q_a X^a`, `I_2(sum f_n X^n)=sum f_n X^n/n^2`, and
`X=x exp(tau_L+tau_R)`,

```text
U_2=(u^2 yz/2) I_2(Q(X)^2).
```

Only the positive one-boundary cavity transform `Phi` remains multitype.
The factorial cut sum is also a positive beta integral: substituting
`y=(1-t)/t`, `z=t/(1-t)` in `U_2` absorbs
`(d+c-2L)!(d-c+2L)!`.  This reduces the theorem to coefficient
log-concavity of one explicit positive integral of the coupled cavity
solution.

## Exact obstructions and finite calibration

- Shifted ULC of `H_2[d,c]` is refuted at `d=4,c=3`, with exact cleared
  margin `-2424287232`.
- The quantitative strengthening
  `H_2[d,c]^2 >= (1+1/d)H_2[d,c-1]H_2[d,c+1]` is refuted first in the capped
  scan at `d=16,c=12`.
- Ordinary H2 log-concavity has no failure through `d=18`; this is exact
  finite falsification only.  The weakest tested ratio is about
  `1.03153815847` at `d=18,c=13`.
- The weaker candidate surplus `1+1/d^2` survives through `d=18`; this is
  not a theorem.
- Against the accepted total rows through `d=18`, the H2 curvature pays the
  exact higher-core correction in every tested case; the weakest budget ratio
  is about `1.03265462955`.  Again this is finite only.

The natural TP proof does not close.  In homogeneous child degree `k`, the
`Phi` kernel in boundary size `s` and total child size `S` is proportional to
`(s+S)^(k-2)`: it is TP2 for `k=0,1`, rank one for `k=2`, and reverse-TP2 for
every `k>=3`.  Degree summation therefore mixes determinant orientations.
Indeed `Phi_1(t)=1+t/2+t^2/2+2t^3/3+...` is not even log-concave at degree
one.  No standard TP/PF composition theorem applies directly.

## Status and next step

**PROVED, pending fresh audit:** exact marked-pair recurrence and the formal
cavity/Lagrange/beta-integral reduction.

**REFUTED:** shifted ULC and uniform inverse-linear curvature surplus.

**UNRESOLVED:** ordinary H2 log-concavity and a quantitative surplus that
universally dominates higher cores.  The first remaining lemma is coefficient
log-concavity of the explicit beta-integrated coupled `Phi` fixed point, or a
new comparison exploiting cancellation between its mixed TP degrees.

No defect-projection, incidence-chain, handle-projection, original heat-bath,
or terminal claim follows.
