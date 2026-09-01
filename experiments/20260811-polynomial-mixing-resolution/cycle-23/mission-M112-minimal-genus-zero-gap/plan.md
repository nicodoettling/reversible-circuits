# M112 plan: minimal genus-zero Hurwitz gap

Date: 2026-08-12

## Objective and target

Fix `d>=2` and

```text
Z_d={w in T_d^(2d-2): eval(w)=id, support(w)=[d] connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  The target is the uniform law on `Z_d`.  The auxiliary
kernel is the exact half-lazy signed adjacent-Hurwitz walk

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_(i=1)^(2d-3) (R_i+R_i^(-1)),
R_i(a,b)=(b,bab), R_i^(-1)(a,b)=(aba,a).
```

The main target is `gap(P_(0,d))>=d^(-O(1))`.  This is a sufficient input
for only part of M104's `Gamma_0(d)` obligation; it is not a full heat-bath
or Terminal claim.

## Named route to test

1. Define the marked-leaf lift `Y_d={(w,v):v is a leaf of the prefix join
   tree T_J(w)}` and the exact deletion map `(w,v)->Del_v(w) in Z_(d-1)`.
2. Determine the exact or polynomially bounded Radon--Nikodym distortion of
   the deletion projection, including its lift multiplicities.
3. Test the named **marked-leaf restriction/projection lemma**: fibers of
   `(v,Del_v(w))` are connected by literal signed adjacent-Hurwitz moves
   that retain the mark, and projected adjacent moves on `Z_(d-1)` admit
   randomized literal simulations with polynomial congestion.  Do not use a
   canonical-hub flow unless its edge load is proved polynomial.
4. If the lemma survives exact `d=2,3,4` falsification, prove the sharpest
   restriction/projection comparison available.  If it fails, retain the
   smallest exact counterexample and state the corrected route.
5. Separately classify every arbitrary-product component factor in M104's
   definition of `Gamma_0(d)`: prove a reduction to an identity sector if
   one is literal and quantitative, or state precisely which coordinates
   remain additional.
6. Audit DPS Proposition 3/Theorem 5 as a nonrecursive alternative: after
   adjoining a chosen white root, identify the exact
   `Cayley_d x S_(2d-2)` product law; define a polynomial-gap ideal product
   chain; and falsify one-step intertwining separately for an adjacent
   permutation-value swap and one Cayley-tree basis exchange.  Promote a
   comparison only with a source-recovery/congestion proof, not from short
   paths.

## Computation and failure modes

Use a deterministic exact enumerator only for the named fiber-connectivity,
lift-multiplicity, and local-simulation claims at `d=2,3,4`.  Record Python
version, command, runtime, dependency versions, and machine-readable output.
Likely failure modes are reducible marked fibers, exponentially distorted
projection weights, loss of the leaf mark under the only physical path, or
recursive comparison losses multiplying at every label deletion.

## Deliverables

- `checkpoint.md` at halfway.
- A proof/reduction note and, if used, exact script plus JSON.
- A nine-field `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.
- Verdict `prove`, `refute`, or `inconclusive`, with all claims labeled and
  no edits outside this directory.
