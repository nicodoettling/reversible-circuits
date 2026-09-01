# M149 fresh-referee report on frozen M145

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The immutable M145 payload proves, relative to the accepted finite-DAG and
scalar inputs stated below, the auxiliary right-heavy suffix-excess-six
inequality

```text
H(s,K,K-1,s-6)<q(1-q),
q=w_7 w_(s-6)/w_(s+1),  s>=7, K>=1.
```

The accepted positive-history comparison gives `G<=H`, and the seed is
right-heavy, so `G<=H<U=q(1-q)`.

## Field 2 — target, convention, and scope

The project target remains uniform on fixed-length identity transposition
words in `Omega(N,m)`. Permutations compose as `(pq)(x)=p(q(x))`, with tuple
factors displayed left-to-right.

The accepted claim concerns only the full **nonlazy stationary-flow
parking-degree projection** in the minimal-long-cycle sector. It proves no
all-`L` contraction, weighted auxiliary gap, ROOT-MEAN LIFT, original
`{3,4,5}` heat-bath gap, polynomial mixing theorem, Terminal A, or Terminal B.

## Field 3 — immutable provenance and dependency reconciliation

All six supplied M145 hashes matched before inspection and again inside the
final clean-room run:

```text
plan        eef285e14c41ba475dac8c16bfeb9500188935807f766f98ddbacb4d45385231
checkpoint  4b7519915ee8ca97c4483c818a99b020fa0a589196ac05d5a49ab602eaa70182
proof       6e0af764322dcde3108f6b35102f9a7f334c427077ae5ae5de95ce0bbe84e65d
checker     9ec575eea344e9ea57e9561b29fdfa3dc3c7c982fe5f0052fbf61b853423e314
JSON        a3583b387a6553fcdbf156fdb3f37bf71f077c729a400983f79ebfa81513c6fc
report      46bc88095f2223874341d820daa60ffe90f59815ab29aecc5156b0f645b815f4
```

Exactly those six files were treated as immutable. The predecessor cache was
observed and left untouched.

M140's scalar proof and M144's fresh ACCEPT report were read as the only new
scalar dependency. Their observed proof/report hashes are respectively
`d8e49d7e06eb82f45621febb3107e75d0ab35eea440402db083797675e994bb6`
and
`7670f7f4717a81d427df68c24b4bd90a5e38e57ea7d8ae21caa437e79c86b6d2`.
M144 accepts the universal theorem `C_S<3/4` for every `S>=100`. The accepted
M109/M114 all-rank recurrence, finite descent, terminal theorem, and
positive-history comparison were inspected, as were M117/M121's
arbitrary-deficit lower-excess inputs. The rejected M131 two-power display is
negative provenance only and is not used.

## Field 4 — exact support, basins, and every attachment rank

A contextual `L=6` row is `(P,B+h)`, where
`0<=h<=6` and `P` is an ordered composition of `6-h`. Therefore the row count
is

```text
32+16+8+4+2+1+1=64.
```

At fixed `h<6`, every composition of `6-h` is a canonical endpoint. Its
basin consists of every refinement of its first part. Thus an exceptional
basin that intersects contextual support is wholly contained in that support,
and the endpoint count is

```text
32+16+8+4+2+1=63.
```

The degree ranges give 22 positive groups. The six positive-height levels
contain 16 deep groups and

```text
(2+3+4+5+6)+(2+3+4+5)+(2+3+4)+(2+3)+2+1
=20+14+9+5+2+1=51
```

nominal positive attachment ranks. The clean-room code independently checks
the defining attachment law sums to one and retains every `j=1,...,k` before
boundary killing. Each child has

```text
excess h-1, offset a+k, deficit D+k-j.
```

At `s=7`, `B=1`; precisely the 20 height-one ranks have rank-one targets and
are inactive. Their displayed terminal charge vanishes because the one-ratio
split is one, leaving exactly 31 retained ranks. No coincident child was
grouped before every rank appeared.

## Field 5 — full-basin subtraction and recursive all-deficit envelope

For each endpoint `E`, the independent reconstruction verifies exactly

```text
b_E=c_E lambda_E
```

by summing all ordered refinements of its first part. Since every exceptional
basin is fully supported here, replacing its ordinary current removes

```text
q^2 c_E lambda_E^2=q^2 b_E lambda_E
```

before restoring the exact current square. This is one power of `lambda_E` on
the **full basin mass** `b_E`. It is not the rejected supported-mass expression
`a_E lambda_E^2`.

After division by the contextual split `q`, write normalized capacity
`\bar c_E=c_E/q` and normalized current `Theta_E=theta_E/q`. The expanded
reset used by the clean-room checker is exactly

```text
R=q C_S-q^2 sum_exceptional \bar c_E lambda_E^2
  +sum_exceptional Theta_E^2/\bar c_E.
```

Adding inactive canonical edges is harmless because every added energy is
nonnegative. Ordinary basins are supplied by `C_S`; exceptional full
baselines are subtracted and replaced exactly.

Induction on suffix excess then gives the arbitrary-deficit recurrence: a
parent normalized group mass times an attachment probability multiplies
`q_child F_child`, with only actual rank-one targets killed. This induction
uses the accepted terminal bound at `L=0` and does not assume contraction for
an arbitrary-deficit child. It applies the same refined reset to right-heavy
and non-right-heavy descendants.

The clean-room full-state recurrence separately enumerates literal
compositions/basins and aggregates them by the Cayley-forest formula. Their
resets and full resolvents agree exactly at all six selected roots

```text
s in {7,8}, K in {1,2,5}.
```

All six satisfy `exact H <= q F < q(1-q)`.

## Field 6 — multiaffinity, degree, and tail cutoff

For a basin at height `h`, split the seven Cayley ratios into bottom and top
products `P_h` and `P_top`. Its normalized capacity is `eta/P_h`, while its
normalized current has the form

```text
Theta=alpha-gamma P_top.
```

The `P_h P_top^2` term in `Theta^2/(\bar c_E)` equals the full ordinary
baseline just subtracted. What remains is a linear combination of `P_h` and
`P_h P_top`, hence squarefree in every ratio. In a descendant term, the
`1/P_h` in normalized parent group mass cancels `P_h` in the child split.
Induction therefore proves that the refined envelope is multiaffine in all
seven consecutive ratios.

Every attachment denominator occupies a consecutive offset segment
`(1+az),...,(1+(a+k-1)z)`. Along a descending history these segments are
consecutive and their total occupied length is at most six. Reset squares
require at most two copies. Consequently every denominator divides

```text
Delta_6(z)^2,  Delta_6(z)=product_(r=1)^6(1+rz),
```

and direct degree tracking gives at most 14 after this chosen clearing.
A generic clean-room finite-difference audit gives exact multidegree
`(1,1,1,1,1,1,1,14)`, with nonzero top degree, and independent off-grid
identities rule out an interpolation mismatch.

For `s>=105`, `B=s-6>=99`; every nonterminal reset has total rank at least
`B+1>=100`, so the accepted M140/M144 theorem permits replacing every
`C_S` by `3/4`. This enlarges the recurrence because all occurrences of
`C_S` have nonnegative propagated coefficients. Monotonicity of
`b_n=(n/(n+1))^(n-1)`, the accepted lower bound `b_n>1/e>4/11`, and the exact
check

```text
b_99<187/500
```

place all seven ratios in the certified tail box. The cutoff has no off-by-one
error.

## Field 7 — independent exact certificates and boundary attacks

The M149 checker imports no M145 or predecessor source or output. It rebuilds
the recurrence from definitions and uses integer-node Newton interpolation
into the monomial basis, followed by the direct power-to-Bernstein identity.
This is structurally different from M145's Bernstein evaluation-matrix
inversion.

- For `s=7,...,104`, all 1,470 degree-14 coefficients are positive. The
  minimum occurs at `(s,index)=(104,0)` and is approximately
  `0.08438881398289777`. The ordered exact-fraction digest is
  `12bcb36c2409ede2ae36d8157a10671246c498043e0f6c6a8dc9f081018edde0`,
  exactly M145's digest. All 98 independent off-grid checks pass.
- In the tail, multiaffinity makes the seven ratio-axis Bernstein
  coefficients equal the 128 box-vertex specializations. Newton/power
  conversion in `z` gives all 1,920 coefficients. Every coefficient is
  positive; the minimum is

  ```text
  11435975715855226131133337
  /149750370000000000000000000
  ```

  at `(1,1,1,1,1,1,0,0)`. The exact tensor off-grid identity passes, and the
  ordered digest
  `b2aafe3c93fc583b7ae7dc32fadaf3a46de97dac0fe8ba46f8ace2a6815dec1d`
  exactly matches M145.
- All 270 arbitrary-deficit contexts through `L=4` satisfy
  `exact H <= q F`. The largest exact/bound ratio is exactly `761/763` at
  `(S,K,R,B)=(3,4,2,1)`, matching M145.
- The strict `s=7` boundary is covered by its complete degree-14 positive
  Bernstein row on `z in [0,1/2]`, including `K=1`, and by the exact
  31-child literal/grouped audits. It is not inferred from a limiting rank.

The compact result file reports zero failures.

## Field 8 — reproducibility and owned artifacts

Run from this directory:

```text
python3 -B cleanroom_referee.py --output cleanroom_referee.json
```

The final run used Python 3.12.3, standard-library `Fraction` arithmetic,
deterministic `seed=null`, and no nonstandard package. Its compact JSON SHA-256
is

```text
7cacc0f0bb5a44d107bab1851034837115c7ee6f3916068223d3962ee27c8787
```

and reports `status=ACCEPT`, `failure_count=0`. `freeze_manifest.md` records
the immutable predecessor gate, accepted dependency boundary, exact command,
and owned pre-freeze hashes. `SHA256SUMS` is the final owned inventory.

## Field 9 — disposition, limitations, and hygiene

Accept M145's refined auxiliary `L=6` contraction within its explicit
dependency boundary. The reusable advance is the full-basin refined
multiaffine recurrence; the sign certificate itself stops at `L=6`. No claim
for `L>=7`, an all-`L` contraction, a weighted auxiliary spectral gap,
ROOT-MEAN LIFT, the original chain, polynomial mixing, or either project
terminal is promoted.

No package was installed, no machine configuration changed, and no commit or
push was attempted. Only the assigned M149 directory was edited. The
predecessor cache was not deleted or modified. The local cache created while
syntax-checking the owned checker was removed before freeze.

