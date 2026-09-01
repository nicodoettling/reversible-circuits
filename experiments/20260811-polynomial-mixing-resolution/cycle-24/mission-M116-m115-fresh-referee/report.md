# M116 final fresh referee report on frozen M115

Date: 2026-08-12.  M115 records repository base commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The accepted result is the auxiliary full nonlazy stationary-flow
parking-degree reset-excursion contraction

```text
H(s,K,K-1,s-3)<=q(1-q),  s>=4, K>=1,
```

in the minimal-long-cycle sector.  Hence the accepted positive-history
comparison gives `G<=H<=U` at these right-heavy seeds.  The project target is
still uniform on fixed-length identity words in `Omega(N,m)`; permutations
compose as `(pq)(x)=p(q(x))`, with factors displayed left-to-right.

This result proves only the suffix-excess-three boundary.  It does not prove
the all-`L` excursion claim, an auxiliary gap, ROOT-MEAN LIFT, the original
lazy `{3,4,5}` heat-bath gap, polynomial mixing, Terminal A, or Terminal B.

## 2. Frozen provenance and manifest gate

M115's manifest verified without error before the audit.  Principal hashes
are

```text
30a72149e1213eee3a8eb287db1f6f7f5d649f2cf9aa46b3c0f99b92d46441d5  report.md
b12ee541ceee4e195d9741fe3956fa668c22d8c8fe0859ea99232b00ba3c1835  suffix_excess_three.md
ff3d2d286c898e1c5d8da074f5d4b797c33ff31b43bd9377440c361a11a6edac  l3_exact.py
444d424b20d0b4f7122c3a6ed6084142b5ce701eececa654ad1fd914eb56406d  l3_exact.json
79a4259923fbe6dd0018bca3eea5ca0cae5c96150c68dbe333351cad881ec39e  independent_l3_audit.py
c78456397be02642800a45295a261e4c0f36d49c8c95a9e763a268d4e46412fb  independent_l3_audit.json
199499d29ffbe7937bf18d0786380c4623b856603e11c3a99c2032ff114bfb2f  SHA256SUMS
```

All remaining entries also matched their manifest.  No predecessor artifact
was edited.

## 3. Recurrence, support, and basin audit

The accepted M109/M114 finite-DAG recurrence retains every attachment rank
`j=1,...,k` and kills only `j=0` or inactive rank-one children.  The fresh
literal reconstruction independently enumerates every ordered composition
and every rank.

For `B=s-3`, exactly eight compositions have nonzero contextual mean:

```text
(3,B), (1,2,B), (2,1,B), (1,1,1,B),
(2,s-2), (1,1,s-2), (1,s-1), (s).
```

Their eight masses and means reproduce M115 exactly and sum to root mean `q`.
Intersecting their canonical paths gives exactly seven exceptional basins,
with supported occurrence mass

```text
q[37/64+5/(16y)+3/(16vy)].
```

Fresh current/capacity calculation reproduces all seven square terms in
M115 (3.2).  The ordinary-height subtraction is valid because total path mass
is `hbar`, while subtracting only supported mass inside exceptional basins is
smaller than subtracting their full basin mass and therefore enlarges the
ordinary upper bound.  Adding inactive reset edges is likewise harmless.

## 4. General `L=1` child and parent normalization

For arbitrary reachable deficit `D=K_0-R_0`, the two supported `L=1`
compositions have means `2p` and `y_0(1-p)`, where
`p=D/(K_0+1)`.  The unary attachment masses are exactly `p` killed and
`1-p` retained.  Its terminal child preserves `D`, so the accepted universal
all-deficit `L=0` theorem proves

```text
H/b_0 <= b_0(h_0-b_0/2)+(2p-b_0)^2/4+(1-p)(1-y_0).
```

M116's literal recurrence checks 168 arbitrary-deficit contexts, including
`S=2`, with zero failures.

For the parent group `(2,s-1)`, the two retained ranks have deficits two and
one and parameters `p_1=2/(K+3)`, `p_2=1/(K+3)`.  The parent factor
`3q/(16b)` cancels the child factor `b` exactly, giving

```text
(3/16)[nu_1F(p_1)+nu_2F(p_2)].
```

The two terminal groups and unary right-heavy `L=2` group give the other two
terms in M115 (5.2), with no omitted `j`.

## 5. Boundary cases

At `s=4`, the nominal `(2,s-2)` and `(3,s-2)` children have rank one and are
inactive; their upper-bound charges vanish because `y=1`.  At `K=1`,
`z=1/2` and the attachment law remains regular and fresh-uniform.

The literal corner `(s,K,R,B)=(4,1,0,1)` retains exactly

```text
(k,t,j)=(1,4,1),(2,3,1),(2,3,2),
```

and gives

```text
H/[q(1-q)] = 44975303/224870400 = .2000054386...,
envelope/[q(1-q)] = 1326997/2928000 = .4532093579....
```

Thus neither boundary requires an unstated limiting argument.

## 6. Finite and tensor Bernstein certificates

M116 independently derives polynomial coefficients using forward
differences, Newton interpolation, and power-to-Bernstein conversion.  Exact
degree checks show degree at most six in `z` and multidegree at most
`(2,2,2,2,6)` in `(r,u,v,y,z)` after the displayed positive clearing.

- All 119 finite coefficients for `s=4,...,20` are positive and exactly equal
  to M115's frozen numerator/denominator pairs.
- All 567 tensor coefficients on `[1/3,2/5]^4 x [0,1/2]` are positive and
  exactly equal to M115's frozen pairs.
- The fresh tensor minimum is `682328/28125` at `(2,2,2,0,0)`.
- The exact bound `(18/19)^17<2/5`, monotonicity of the Cayley ratios, and
  their lower bound `>1/3` put every `s>=21` tuple inside that box.
- Replacing `hbar,h1` by one enlarges the envelope, so positivity on the box
  proves the actual tail sign.

This is a complete algebraic certificate, not finite-rank extrapolation.

## 7. Independent computation and reproducibility

`independent_m115_referee.py` imports no predecessor code.  Its literal
finite-DAG path and its Newton/Bernstein path are independent of M115's helper
implementations.  A fresh-only run that read no predecessor artifact had zero
failures.  The durable command is

```text
python3 -B independent_m115_referee.py \
  --output independent_m115_referee.json \
  --reference-json ../../cycle-23/mission-M115-suffix-excess-three/l3_exact.json
```

It records 168 `L=1` contexts, 15 complete `L=3` DAGs, all 119 finite and 567
tensor coefficients, 837 degree-check slices, and zero failures.  Post-hoc
comparison finds exact equality on all 119 finite coefficients, all 567
tensor coefficients, and all 15 shared complete-resolvent ratios.  Arithmetic
is exact `Fraction`, Python is 3.12.3, dependencies are standard-library only,
and `seed=null`.

Directly rerunning M115's literal script from `/tmp` reproduced its frozen
JSON hash exactly.  Directly rerunning its primary script reproduced the
entire mathematical payload exactly after excluding only the nondeterministic
elapsed-time field.

## 8. Dependencies and unresolved frontier

- **Accepted inputs:** M109/M114's exact all-`j` recurrence,
  `beta_E<=degree(E)`, positive-history `G<=H`, universal all-deficit `L=0`
  contraction, and right-heavy `L<=2` contraction.
- **Accepted from M115 after this audit:** eight-support and seven-basin
  formulas, arbitrary-deficit `L=1` envelope, all four descendant charges,
  exact universal scalar certificate, and right-heavy `L=3` contraction.
- **Unresolved:** right-heavy full-excursion contraction beginning at `L=4`,
  every auxiliary gap and ROOT-MEAN obligation, the original heat-bath gap,
  polynomial mixing, and both project terminals.

The proof remains structurally local to `L=3`; growing exceptional-basin
combinatorics prevent any automatic all-`L` inference.

## 9. Final verdict and hygiene

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`independent_m115_referee.py`, `independent_m115_referee.json`, this report,
and `SHA256SUMS`.  The final freeze verifies source compilation, exact rerun,
JSON parsing, whitespace, manifest integrity, and owned cache hygiene.  No
M115 file, coordinator note, manuscript, project skill, or shared source was
edited.
