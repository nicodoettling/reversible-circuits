# M49 plan: label-symmetric branch-balance cuts

## Exact target and convention

Permutations are maps on `[N]`, multiplication is `(pq)(x)=p(q(x))`, and a
word evaluates as `t_1\cdots t_m`.  Work at `N>=4`, `m=2N-2`, with the exact
lazy kernel

```text
K = (1/2)I + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m={r in {3,4,5}:r<=m},
```

where `H_{i,r}` is uniform on the length-`r` same-product transposition
fiber.  Let `F_N` be the minimal connected full-support identity macro and
`T_J(w)` its prefix-join tree.  For a tree `T`, set

```text
b_N(T)=max_{e in E(T)} min(|C_e|,N-|C_e|),
B_{N,q}={w in F_N:b_N(T_J(w))>=q}.
```

The global stationary law is uniform on `Omega(N,m)`.  The principal goal is
either a uniform inverse-polynomial two-sided conductance lower bound for all
nontrivial `q`, or a literal Terminal-B family with correct global mass
orientation and complete `r=3,4,5` boundary accounting.

## Proof lanes

1. Prove the deterministic equivalence between `b_N(T)` and the usual
   centroid branch radius.  This identifies precisely what the symmetric cut
   measures and prevents a hidden label choice.
2. Count an overlap-free, root-marked reservoir of genuine `H_3` exits.  A
   removable adjacent leaf square has exact specified-refresh probability
   `1/[6(m-2)D_N]`, where `D_N=(3N^2+N-12)/2`; all `H_4,H_5` flow is retained
   as additional nonnegative flow.
3. Derive an exact adjacent-size threshold-count inequality.  Leaf insertion
   is monotone for `b_N`, so words in `B_{N-1,q}` yield a counted subset of
   `B_{N,q}`.  Audit the exceptional maximum threshold `q=N/2` for even `N`,
   where `B_{N-1,q}` is empty and a `q-1` correction is required.
4. Seek a projective vertex-deletion or strand-deletion identity for uniform
   minimal transitive identity factorizations.  The needed theorem is a
   polynomial upper bound on the ratio of weighted threshold counts, not
   merely Cayley-tree counting.  If it fails, quantify the strongest surviving
   ratio and determine whether the remaining states admit `H_4/H_5` bypasses.
5. Independently inspect cyclic Hurwitz rotations and paired `H_4` changes for
   a symmetric boundary reservoir.  This is a fallback if adjacent-size
   deletion is too nonlocal.

## Exact finite falsification

Use the fixed-join-tree dynamic program only to test named finite
consequences of proposed deletion/ratio inequalities (smallest available
`N=4,...,8`), never as an asymptotic proof.  Record exact integer threshold
counts, commands, Python version, and repository commit.  In particular test:

- stochastic or ratio monotonicity across `N`;
- whether a polynomial-multiplicity leaf deletion can preserve every
  nontrivial balance threshold;
- endpoint behavior at `q=floor(N/2)`.

## Expected failure modes

- The prefix-join-tree law is highly nonuniform and may lack sampling
  consistency under deletion.
- A tree can have no adjacent repeated leaf square, so pointwise escape is
  false.
- A counted exit from one fixed-root cut need not exit the label-symmetric
  intersection.
- A slow auxiliary parking/leaf-rotation chain does not upper-bound the full
  `K` flow.
- Even a small internal boundary of `B_{N,q}` is nonterminal unless exits from
  `F_N` and global smaller-side orientation are controlled.

## Deliverables

Write a genuine halfway `checkpoint.md`, then a nine-field `report.md` with
all dependency labels, exact normalizations, calibrations, artifacts, the
first standalone gap, and verdict exactly `PROVED`, `REFUTED`, or
`OPEN AT A NAMED STEP`.
