# M104 plan: partial-fiber handle-cycle expansion

Date: 2026-08-12. Status: complete; frozen after final consistency audit.

## Objective and declared target

Audit M97's exact spectrum-preserving lift of the half-lazy signed adjacent-
Hurwitz walk on

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected}, d>=2,
pi_d=Unif(X_d).
```

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply left-to-
right. The base kernel is

```text
P_d=(1/2)I+[1/(4(2d-1))]sum_i(R_i+R_i^(-1)),
R_i(a,b)=(b,bab), R_i^(-1)(a,b)=(aba,a).
```

The lifted law is `tilde_pi(w,j)=pi_d(w)/ell(w)` on admissible central cuts
`j in J(w)`, where `ell(w)=|J(w)|`. The project target remains the global
fixed-length uniform identity-word law for the lazy exact `{3,4,5}` heat-
bath chain; this mission studies only the auxiliary genus-one Hurwitz gap.

## Named claim under test

At fixed admissible cut and exact seam data `(j,p,Q_L,Q_R)`, determine:

1. whether the raw uniform word fiber is a literal product of independent
   genus-zero prefix/suffix factorization sets;
2. whether `1/ell(w)` is the only coupling under `tilde_pi`, with pointwise
   Radon--Nikodym distortion at most `2d-1` from a product conditional law;
3. which literal signed Hurwitz moves preserve the fixed seam data and cut
   admissibility, and what restricted kernels they induce;
4. whether a seam projection has inverse-polynomial flow without canonical-
   word routing or quantitative Classification H.

The target deliverable is either an inverse-polynomial partial-fiber
decomposition, a precise conditional comparison such as
`gamma_1(d)>=poly(d)^(-1) min(gamma_0-side,seam-gap)`, or the sharpest proved
route obstruction.

## Proof and falsification program

- Derive the conditional counting law algebraically and audit all empty and
  boundary fibers.
- Compute how an internal move changes `(p,Q_L,Q_R)`, including the special
  prefixes immediately adjacent to the seam.
- Test the fixed-seam claim exactly for `d<=4`; use this only to falsify
  universal assertions and to expose move components.
- Analyze the `p=id` fiber with one connected minimal genus-zero side on all
  `d` labels and the other side a square. Explicitly check whether this
  reintroduces the same-size minimal genus-zero Hurwitz gap and blocks an
  inductive label-size decrease.
- Do not route through a canonical word; do not assume Classification H
  quantitatively; do not infer asymptotics from finite data.

## Required artifacts

`checkpoint.md`, a proof or obstruction note, an exact audit script and
machine-readable output if computation is useful, a nine-field `report.md`,
`freeze_manifest.md`, `SHA256SUMS`, cache audit, and final shared status.

## Expected failure modes

- Conditioning on support partitions may destroy the naive product law.
- Interior Hurwitz moves may preserve products but refine/coarsen side
  support partitions at the one intermediate prefix.
- Fixed seam data may freeze every incidence-cycle coordinate, leaving no
  seam projection inside the restriction.
- The full-label genus-zero side may make tensorization circular rather than
  inductive.
- The `1/ell` density comparison can transfer gaps only after a valid common
  reversible kernel/comparison is specified; measure comparison alone is not
  a gap proof.
