# M320 independent proof audit of frozen M317

Date: 2026-08-14 UTC

## Verdict at proof level

M317's mathematical claims are correct at their frozen scope.  Actual
`d>=6` HPRN, APOH, SPBE, PHTC, and WRAD remain unresolved, and M317 does not
infer any downstream theorem from them.

## 1. Residual partial maps and tuple orbits

Fix a compatible pivot tuple `I`, a witness `s_I`, and

```text
H_I={h in Sbar : x_P^h=x_P for all P in I},
z_Q=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I : x_Q^h=z_Q}.
```

After tagging pivot and residual coordinates, the equations
`a_(I,V)^h=b_(I,V)` say exactly (i) that `h` fixes every pivot and hence lies
in `H_I`, and (ii) that `h` lies in every `D_I(Q)`.  Therefore

```text
intersection_(Q in V) D_I(Q)
 = {h in Sbar : a_(I,V)^h=b_(I,V)}.
```

Nonemptiness is consequently equivalent both to one diagonal full-tuple
orbit and to extension of the displayed partial prescription by an element
of `H_I`.  If a solution `h_0` exists, every solution is a left coset of the
pointwise stabilizer of the distinct residual source points under M317's
right-action convention.  M317 does not confuse the coset description with
existence.

For any two tagged coordinates, equality of sources iff equality of targets
is exactly well-definedness plus injectivity.  Including the pivots supplies
all four collision rules: a residual source on a pivot must remain there, an
outside source cannot enter the pivot set, repeated residual sources have
repeated targets, and distinct sources have distinct targets.  These are
only partial-bijection conditions, not membership in `H_I`, as M317 states.

The remaining ladder is exact:

```text
D_I(Q) nonempty
 <=> source and target share an H_I point orbit;
D_I(Q) intersect D_I(R) nonempty
 <=> the ordered source and target pairs share an H_I orbital;
intersection_(Q in V) D_I(Q) nonempty
 <=> the complete tuples share an H_I orbit.
```

The diagonal pair orbital includes equality.  Pair-orbital preservation need
not imply the final tuple-orbit condition for a general permutation group;
M317 correctly leaves that higher-arity step open for the actual action.

## 2. Covariance

With chronological right action, replacing `s_I` by `g;s_I`, `g in H_I`,
uses `(g;s_I)^(-1)=s_I^(-1);g^(-1)`.  Hence every target becomes
`z_Q^(g^(-1))` and every signature becomes `D_I(Q);g^(-1)`.  Intersections
are uniformly right-translated.  Accepted frame changes uniformly conjugate
the stabilizer and signatures.  Point-, pair-, and full-tuple orbit tests are
therefore invariant exactly as claimed.

## 3. Exact quantifiers in `SPBE => PHTC => WRAD`

M317's SPBE quantifies universal `B,C`, every nonzero weighted actual
`d>=6` matching, a positive-weight outer anchor, a compatible pivot tuple
with `|I|<=d^B`, and the whole set `V=G_I(supp(lambda))`.  Its three clauses
give weight at least `||lambda||_1/d^C`, all pair intersections, and extension
of every pairwise-consistent actual partial map at that node.

For the current `V`, pair intersections give orbital preservation (including
equality); the extension clause and the tuple identity give the full common
intersection.  This is PHTC with the same exponents.  Choosing its common
`h` makes `h;s_I` satisfy every normalized constraint indexed by `V`.
The accepted anchored score is a maximum over positive-weight anchors, so the
chosen anchor is admissible and the score is at least `lambda(V)`.  This is
WRAD.  M317 retains the anchor maximum and does not replace the whole `G_I(U)`
by a proper subcell when claiming PHTC.

## 4. Symmetric and alternating calibration actions

For `Sym(X)_(B)`, an admissible partial injection on `X\B` leaves equally
many unused sources and targets; any bijection between them completes it
while fixing `B`.  For `Alt(X)_(B)`, an arbitrary completion can have its
parity toggled by precomposing a transposition of two unused source points,
which changes no prescribed image.  With zero or one unused point the
completion is unique, so its parity is the exact obstruction.

For `|X\B|>=4`, restricting an odd full permutation to any two source points
leaves at least two unused points and admits an even completion, while the
full odd prescription does not.  This is an exact pairwise-to-full parity
obstruction.  M317 explicitly does not identify either calibration action
with the actual chart-stabilizer action.

## 5. Exact `d=3` boundary evidence

The authenticated M301/M304 evidence agrees with M317:

- the actual `d=3` matching `[0,1,2,9]` is conflict-independent, while the
  exact census has zero pairwise-compatible complete perfect matchings;
- the subfamily `[0,2,9]` has pair intersections
  `K_0 intersect K_2={45}`, `K_0 intersect K_9={49}`, and
  `K_2 intersect K_9={89}`, but empty triple intersection.

Thus the first example refutes only the formal implication from the coarser
M135 conflict invariant to exact pair compatibility.  The second is an
actual boundary-rank pairwise/full-tuple separation.  Neither lies in the
`d>=6` domain of SPBE or PHTC, so neither proves nor refutes either actual
all-rank gate.  M317 states this strict limitation correctly.

## 6. HPRN and APOH

HPRN supplies SPBE clauses 1 and 2: with the positive anchor and compatible
`|I|<=d^B`, the whole `G_I(U)` has inverse-polynomial weight and all residual
pairs intersect.  APOH supplies clause 3: every actual residual partial map
preserving all `H_I` orbitals extends in `H_I`.  The HPRN map preserves those
orbitals by the pair-intersection identity, including its equality kernel.
Therefore `HPRN+APOH => SPBE` is complete.

As standalone prose, “inverse-polynomial weight” in the displayed HPRN gate
does not restate `lambda(G_I(U))>=||lambda||_1/d^C` or the universal/all-input
quantifiers.  In context these are inherited unambiguously from the
immediately preceding SPBE definition and fixed weighted instance.  This is
a nonmaterial wording clarification, not a logical gap.  APOH's “actual
residual partial map” correctly restricts its homogeneity demand to the
actual-form maps at selected HPRN nodes.

## Scope result

No `d=6` computation or theorem search was performed.  The audit makes no
new-rank, all-rank, literal-length, MRAD, SSTID, route, voltage, congestion,
spectral-gap, mixing, or Terminal inference.
