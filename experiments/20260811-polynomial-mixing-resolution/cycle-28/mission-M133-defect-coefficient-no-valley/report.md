# M133 final report: positive unique-cycle defect reduction

Date: 2026-08-13 UTC.

## Field 1 — decision and claim status

Verdict: **PROMOTE FOR FRESH AUDIT** the subtraction-free unique-cycle
coefficient theorem; **REFUTE** the natural pairwise core-polarization
shortcut; **KEEP OPEN** universal ordinary log-concavity and DEFECT NO-VALLEY.

**PROVED, relative to the accepted M125/M129 coefficient input:** the
subtractive connected extraction on the required unicycle diagonal has an
exact positive decomposition by unique even core length and recursively
planted opposite-colour trees.  Every orientation, root-edge, length-two-core,
and atom-indexing factor is explicit.

**REFUTED:** proving all pairwise polarized inequalities between fixed-core
profiles cannot establish the total inequality; the first failure is exact at
`d=4,c=3`, core lengths two and four, with margin `-17309376`.

**EXACT FINITE:** the positive recurrence matches literal partition-pair
enumeration for all 37 integer cycle types through total size seven and
reconstructs every accepted total row through `d=8`.  Targeted ordinary
log-concavity checks remain positive through the declared cap `d=26`, but the
weakest tested ratio is only about `1.00237056`.

**UNRESOLVED:** `H[d,c]^2>=H[d,c-1]H[d,c+1]`, DEFECT NO-VALLEY, every
defect/fixed-fiber/incidence/handle spectral gap, and the original lazy exact
`{3,4,5}` same-product heat-bath gap.  Neither Terminal A nor Terminal B
follows.

## Field 2 — target, convention, and dependency boundary

The target is the auxiliary M113/M118 law

```text
rho(kappa)=|C_kappa|/Z_inc
```

on realizable connected-unicyclic incidence keys, not the original uniform
identity-word law and not the lifted `bar_pi` law.  With
`R(kappa)=d-c(p)`, write

```text
M[d,r]=sum_{R(kappa)=r}|C_kappa|,
H[d,c]=M[d,d-c].
```

Permutations compose as `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right.  The imported proved inputs are the M113/M118 exact cell
formula, the M120/M124 directional defect rates, and the M125/M129 exact
cycle-type coefficient reduction.  Only the last is used in the new theorem.
ULC and real-rootedness are treated as refuted at `d=4`.

## Field 3 — subtraction-free planted-tree recurrence

Fix indexed cycle atoms `E` with positive sizes `a_e` and define

```text
w(I)=(sum_{e in I}a_e)^(|I|-3).
```

For colour `epsilon` in `{L,R}`, disjoint boundary and internal edge sets
`B,S`, and `|B|` one or two, define

```text
T_epsilon(B;S)
 = x_epsilon
   sum_{pi partition of S}
   sum_{r_D in D, D in pi}
     w(B union {r_D:D in pi})
     product_{D in pi}
       T_bar(epsilon)({r_D};D minus {r_D}),             (3.1)
```

where `x_L=y`, `x_R=z` and the empty partition contributes one.  Removing the
root vertex of a planted bipartite tree uniquely gives the branch partition
`pi`; each `r_D` is the unique branch edge incident to the root.  Thus (3.1)
counts every planted tree once and uses additions and products of positive
rational weights only.

For an even core set `K`, fix its least atom `e_0` first.  The other edge at
the left endpoint is `e_1`; continue alternately through right and left
endpoints.  The resulting sequence `(e_0,...,e_(2k-1))` has core vertices

```text
left  {e_(2i),e_(2i+1)},
right {e_(2i+1),e_(2i+2 mod 2k)}.
```

Assign every off-core edge to one of these vertices and insert (3.1) with its
two core edges as boundary.  Summing gives a positive polynomial
`U_(E,2k)(y,z)`; summing even core lengths gives `U_E`.

## Field 4 — exact bijection and symmetry-factor audit

**PROVED.**  `U_E` equals exactly

```text
sum_{(pi_L,pi_R):
     pi_L join pi_R indiscrete,
     |pi_L|+|pi_R|=|E|}
  y^|pi_L| z^|pi_R|
  product_{B in pi_L union pi_R}w(B).                  (4.1)
```

An ordered pair of partitions gives a bipartite incidence multigraph.  The
join condition is connectivity, and `V=E` makes the connected graph
unicyclic.  Its unique cycle is even.  Starting at the least core edge and
choosing its left neighbour fixes one traversal; hence there is no `2k`
rotation factor and no orientation factor.  Reversal changes which neighbour
of `e_0` is left and generally gives another ordered coloured pair.  A
two-parallel-edge core occurs exactly once.

After deleting the core edges, every remaining component contains exactly one
core vertex: none would violate connectivity and two would create another
cycle.  Recursive root deletion is then unique and is precisely (3.1).
Conversely the construction makes one even cycle with trees attached, so is
connected unicyclic.  Each vertex receives its full incident-block weight;
each shared edge is correctly present at both endpoint weights.  These maps
are inverse and weight-preserving.  This proof, not the finite audit, proves
(4.1).

## Field 5 — positive `H` decomposition and exact remaining inequality

For integer partition `lambda=(a_1,...,a_c)` of `d`, let

```text
n(lambda)=d!/product_s(s^m_s m_s!),
h(a)=a^a/(a-1)!.
```

Define

```text
H_(2k)[d,c]
 = sum_{lambda partition d, length c}
     n(lambda) product_i h(a_i)^2
     sum_{L=1}^{c-1}
       (d+c-2L)!(d-c+2L)!
       [y^L z^(c-L)]U_(lambda,2k).                     (5.1)
```

Then the accepted M125 formula and (4.1) give the exact positive expansion

```text
H[d,c]=sum_{k>=1,2k<=c}H_(2k)[d,c].                   (5.2)
```

Writing `A_k(c)=H_(2k)[d,c]`, ordinary log-concavity is now the explicit
positive inequality

```text
sum_{k,l}A_k(c)A_l(c)
 >= sum_{k,l}A_k(c-1)A_l(c+1).                        (5.3)
```

This strictly removes the subtractive recurrence identified by M125 as the
first obstacle.  It does not prove (5.3): positivity alone does not make a
sum of profiles log-concave.

A useful exact dominant-core form is obtained from

```text
A[d,c]=H_2[d,c],       E[d,c]=H[d,c]/A[d,c]>=1.
```

The full inequality is equivalent to

```text
A[d,c]^2/(A[d,c-1]A[d,c+1])
 >= E[d,c-1]E[d,c+1]/E[d,c]^2.                        (5.4)
```

It isolates the required budget: quantitative curvature of the doubled-edge
core must absorb the higher-core correction.

## Field 6 — minimal shortcut obstruction and capped finite stress

Pairwise polarization would assert

```text
2A_k(c)A_l(c)
 >= A_k(c-1)A_l(c+1)+A_l(c-1)A_k(c+1)                (6.1)
```

for every core pair; summing would prove (5.3).  It fails at the first possible
case.  The exact `d=4` profiles are

```text
core 2: c=2,3,4 -> 80136,109440,44928,
core 4: c=2,3,4 -> 0,0,216.
```

At `c=3`, the `(2,4)` cleared polarized margin is
`-80136*216=-17309376`.  The full `d=4` row remains log-concave.  Thus the
negative finding is retained: a proof needs aggregate curvature budgeting,
not termwise core polarization.

The targeted exact falsifier, which evaluates only three requested cycle
counts from the accepted recurrence, gives:

| `d` | center defect `r` | exact ratio as decimal |
|---:|---:|---:|
| 23 | 7 | 1.0080697027067378 |
| 24 | 8 | 1.0062524521873242 |
| 25 | 8 | 1.0034208061391020 |
| 26 | 9 | 1.0023705599074406 |

Every underlying exact integer margin is positive and is recorded in the
frontier JSON.  The scan is deliberately capped at `d=26`.  The shrinking
ratios are a warning, not asymptotic evidence.  No claim is made at `d>=27`.

## Field 7 — exact audits, reproduction, and provenance

`positive_unicycle_audit.py` is independent of M125's connected extraction.
It compares (3.1)--(4.1) with literal ordered pairs of set partitions for all
37 integer types with total size `2<=d<=7`; failures are zero.
`core_profile_scan.py` inserts the positive expansion into (5.1), matches all
M125 total rows through `d=8` with zero mismatch, and records the minimal
polarization failure.  It finds no fixed-core log-concavity failure through
`d=8`; that last statement is finite only.  `frontier_scan.py` imports the
frozen accepted M125 core; its `d=8,r=2` smoke ratio
`1.4600344727920804` matches the frozen full row.

Commands from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/positive_unicycle_audit.py --max-d 7 --max-atoms 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/positive_unicycle_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/core_profile_scan.py --max-d 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/core_profile_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/frontier_scan.py --case 8:2 --output experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/frontier_smoke.json
```

The exact capped frontier commands were

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/frontier_scan.py --case 23:7 --output /tmp/m133-frontier-23.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/frontier_scan.py --case 24:8 --case 25:8 --output /tmp/m133-frontier-24-25.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-28/mission-M133-defect-coefficient-no-valley/frontier_scan.py --case 26:9 --output /tmp/m133-frontier-26.json
```

The byte-identical generated payloads were preserved as `frontier_d23.json`,
`frontier_d24_d25.json`, and `frontier_d26.json`; each payload therefore
retains its original `/tmp` output name.  Runs are exact, deterministic,
standard-library-only, and have `seed=null`.

Environment: commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
`3.12.3`.  Frozen M125 hashes used here are report
`dc8f8cb0ab9c6c06f9b49cd56a30b29cc258698dcdfccceb887b265ff67c5879`,
proof `068a42ed4c9141cbabd81ffe35d352c833b634a295a9a6a6f44dabbeb09ffde1`,
core `74cd0159ac62404db172ff3830a1ef58f9f7a105eb2f595b438af66c24c3dde9`,
and manifest
`a6bb1090f1a6f88c38ddd253ec35069e062f9a00563096ae1d0617370b7befdd`.
M129 report and manifest hashes are respectively
`eb7cdcd179a704deed4a8b7cb03a7a69c912bc0b57677a7fb2d886d17056b2d4`
and `9128aa1883796f6bf757bbb46a60ef8450ce9b859f94a4eeed40dac771320b45`.
All M113/M118/M120/M124/M125/M129 frozen checksum inventories pass.

## Field 8 — self-attack, boundaries, and hygiene

- The atom order is used only to choose a canonical core traversal; (4.1)
  proves final relabelling invariance, including equal-size atoms.
- Both cycle orientations were audited: fixing the left neighbour of the
  least core edge removes the factor two rather than silently quotienting it.
- The two-parallel-edge core is included once and supplies the entire `c=2`
  boundary.
- Every off-core component attaches to exactly one core vertex; otherwise the
  graph is disconnected or has more than one cycle.
- Branch set partitions are unordered and every selected child root is an
  actual indexed edge, so no branch factorial is omitted.
- `d=2` is the one-state/two-edge-core boundary.  `c=1` remains impossible
  because both partition colours are nonempty.
- Fixed-core finite log-concavity is not promoted.  Pairwise polarization is
  explicitly refuted rather than hidden by the positive total.
- Targeted `d<=26` signs are finite falsification only and do not prove either
  ordinary log-concavity or unimodality.
- No predecessor, coordinator, manuscript, project-skill, or other worker file
  was edited.  No package was installed and no stochastic conclusion appears.

## Field 9 — first open lemma and downstream action

The first strict positive subproblem is:

> **TWO-EDGE-CORE LOG-CONCAVITY.**  For every `d>=4` and
> `3<=c<=d-1`, the doubled-edge-core contribution defined by (5.1) satisfies
> `H_2[d,c]^2>=H_2[d,c-1]H_2[d,c+1]`.

It is strictly narrower than the full coefficient inequality and is expressed
entirely by the positive planted-tree recurrence.  To finish the original
coefficient target, a quantitative version must be paired with the higher-core
curvature bound (5.4).  The finite core profiles through `d=8` survive this
subproblem but do not prove it.

If full ordinary log-concavity ultimately fails, DEFECT NO-VALLEY remains a
strictly weaker target and must be attacked directly; the positive expansion
still supplies a non-subtractive exact formula for that attack.  Even a future
no-valley theorem yields only M120's one-dimensional projection gap
conditionally.  Fixed-defect two-step expansion, comparison back to `A_d`,
the M113 handle projection, and the original heat-bath gap remain mandatory.
