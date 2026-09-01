# M80 final report: ACCEPT M73 and localize its influence lemma

Date: 2026-08-12. Base repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Referee verdict

**ACCEPT, with zero numbered objections.** This accepts the frozen M73 exact
cyclic-product kernel, covariance bound, cyclic-composition and four-schema
parameterization, conditioned-Borel calculation, diameter-two source graph,
finite rational certificates, and their stated implications. It does **not**
accept M73's unresolved shared-factor influence inequality, an `H_0` gap, a
fixed-long-cycle bridge gap, or Terminal A/B.

The requested hashes independently match:

```text
M73 report    bfb427ff4cc8649c2f5dda61f64fd0ba5364143f3cc93c2bcbe61810392a6692
M73 manifest  da76521810b9ec668ef0e09fab80237d5cea715f9a40878548663d35f8ddf60f
```

Running `sha256sum -c` from the repository root passed all 35 manifest
entries. The frozen directory contained no Python cache.

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The target here is the uniform minimal length-`n-1` transposition bridge to
the odd long cycle `h=(0 1 ... n-1)`, compressed to pair products and then to
simultaneous-`h`-conjugacy orbits. It is not the identity bridge.

## 2. Independent audit

### 2.1 Kernel, stationary law, and covariance

Fixing one pair product `g` leaves the minimal completion `g^-1 h`; fixing
two ordered pair products `g,s` leaves `(gs)^-1 h`. Dénes' cycle counts plus
independent interleaving therefore give exactly

```text
pi(g)=a(g)F_(n-3)(g^-1h)/n^(n-2),
J(g,s)=a(g)a(s)F_(n-5)((gs)^-1h)/n^(n-2),
K(g,s)=a(s)F_(n-5)((gs)^-1h)/F_(n-3)(g^-1h).
```

The quotient uses literal orbit masses. The bridge rotation gives the twisted
raw symmetry, and cyclic-orbit summation makes the quotient joint law
symmetric. Thus every quotient row normalizes and `bar K` is self-adjoint in
`L^2(bar pi)`.

On this invariant block an eigenvalue `kappa` is real. The `l=(n-1)/2`
coordinate evaluations have covariance

```text
(1-kappa)I_l+kappa 11*.
```

Positivity gives `kappa>=-1/(l-1)`. M16's accepted scalar Gram formula then
leaves only the largest positive invariant eigenvalue. No positivity of `K`
itself is assumed.

### 2.2 Composition weights, schemas, and Borel law

The oriented three-cycles are cyclic positive 3-compositions, with the
balanced orbit stabilizer included. Every double-transposition orbit is free
for odd `n`. Lagrange inversion gives the displayed `T^3` and
`T^4/(1-T)` normalizations and total stationary masses `3/n` and `(n-3)/n`.

Conditioning the first two completion factors on their residual-component
colors yields exactly `I3,IS,IN,X` with coefficients

```text
r_i(r_i-1)/[(n-3)(n-4)]
and 2r_i r_j/[(n-3)(n-4)].
```

The local Cayley completion counts give the stated `nu_d` and `mu_d`. After
orienting the chosen edge uniformly, the `d/2` oriented-anchor multiplicity
turns `nu_d` exactly into two critical Borel variables conditioned on their
sum. The smaller-fragment coupling consequently loses
`Theta(d^-1/2)`, so it cannot prove the desired result schema by schema.

### 2.3 M73 source graph and implication

The diameter-two proof correctly handles both chord-placement cases. A
rotated shorter chord fits strictly inside the larger arc of the first chord,
unless both lengths are extremal; in the extremal case sharing an endpoint in
the required cyclic order produces an admissibly oriented three-cycle.

If M73's adjacent-row inequality were proved, a path of length at most two
would give `delta(bar K^2)<=2C/n^2`. Dobrushin contraction bounds every
nonconstant eigenvalue of `bar K^2`; self-adjointness of `bar K` then gives
`|kappa|<=sqrt(2C)/n`. The square-root and path factors are correct.

## 3. Fresh exact computation

`independent_exact_audit.py` was written from scratch in this directory and
imports no M73 code. It exactly reconstructs the marginal, quotient kernel,
stationary masses, detailed balance, `bar K^2`, shared-factor graph,
constructive chord placement, and conditioned-Borel entries:

```text
n  support  quotient  graph edges  diameter  max adjacent TV(bar K^2)
5       20         4            6         1  1
7      105        15           95         2  7185517/30375000
9      336        38          553         2  2094407996609/19603684800000
```

It found zero constructive chord-placement failures among `100,441,1296`
ordered chord pairs. A separate rerun of M73's schema verifier reproduced all
`400` entries at `n=5` and all `11025` at `n=7`; its output is byte-identical
to M73's frozen JSON. A separate kernel rerun reproduced both exact adjacent
fractions above.

These are exact finite facts, not an asymptotic proof.

## 4. New proved endpoint-sharing localization

Let `Lambda_n` have the same cyclic product orbits as M73's `Gamma_n`. Join
two vertices only when they have lifts

```text
(a,b),(a,c),  with b and c sharing an endpoint,
```

or the analogous shared-second-coordinate lifts. This is a strict
localization of M73's arbitrary shared-factor adjacency.

**Proposition (proved).** For every odd `n>=5`,

```text
diam(Lambda_n)<=4.
```

**Proof.** Let `T_n` be the subset of oriented-three-cycle orbits.

First, every vertex is at distance at most one from `T_n`. This is immediate
for a three-cycle. Otherwise choose a lift `g=ab` of a noncrossing double
transposition. The endpoints of `a` cut the polygon into two arcs, and the
disjoint chord `b` lies wholly in one open arc. Join the initial endpoint of
that directed side of `a` to either endpoint `z` of `b`, calling the connector
`c`. Then `ac` is the admissibly oriented three-cycle on the two endpoints of
`a` and `z`. The lifts `(a,b),(a,c)` share `a`, while `b,c` share `z`, so the
two product orbits are adjacent in `Lambda_n`.

Second, the induced graph on `T_n` has diameter at most two. Write two orbit
parameters as cyclic positive triples `[x_1,x_2,x_3]` and
`[y_1,y_2,y_3]`. Choose minima `x` and `y`. Since `x,y<=n/3`,
`z=n-x-y>0`, so `[x,y,z]` is a positive triple. Two oriented-three-cycle
orbits whose cyclic triples share a part are adjacent: rotate them so the
common part is the same directed side `AB`, and use lifts
`(AB)(BC)` and `(AB)(BC')`; their differing chords share `B`. Hence the
intermediate triple `[x,y,z]` is adjacent to both given triples.

Therefore arbitrary vertices have distance at most `1+2+1=4`. QED.

This yields the stricter sufficient lemma:

> **ENDPOINT-SHARING TWO-STEP INFLUENCE (open).** For odd `n>=7`, if two
> product orbits have lifts `(a,b),(a,c)` with `b,c` sharing one endpoint (or
> the second-coordinate analogue), then
>
> ```text
> TV(bar K^2(O,.),bar K^2(O',.))<=C/n^2.
> ```

The proposition and triangle inequality would give
`delta(bar K^2)<=4C/n^2`, hence `|kappa|<=2sqrt(C)/n`. Thus this strictly more
local cut/join lemma is sufficient for M73's correlation goal. Algebraically,
for `g=ab,g'=ac`,

```text
g^-1 g'=bc,
```

which is a three-cycle when `b!=c` share one endpoint. This exposes a single
local cut/join perturbation rather than an arbitrary replacement chord.

## 5. Finite diagnostics of the localized graph

`localized_source_metric.py` constructs `Lambda_n` and its `bar K^2` edge
influences. Graph combinatorics are exact; TV entries below are floating:

```text
n   quotient  Lambda edges  diameter  n^2 max-edge TV
7         15            75         2       11.5915
9         38           323         3        7.9951
11        75           889         3        6.8062
13       132          1994         3        5.8992
15       213          3894         3        5.7924
17       320          6856         3        5.7665
19       459         11265         3        5.6044
21       634         17517         3        5.7137
```

Thus the proved constant four can plausibly be sharpened to three, but the
universal diameter-three statement is not promoted. The stable scaled TV is
also finite evidence only.

A still finer graph allowing only unit cyclic endpoint slides is connected in
the tested sizes but has diameter `n-3`. Its finite worst edge influence does
not display the extra uniform `n^-1` gain that naive telescoping would require.
This route is retained as a negative diagnostic, not a refutation of an
asymptotic inequality.

## 6. First unproved analytic step and attempted coupling

For an endpoint-sharing edge, the two sources agree on a raw chord and their
other chords differ by a three-cycle cut/join. The four-schema formula gives
an explicit coupling interface: delete the common chord, couple identical
residual component factorizations and color interleavings, and analyze only
the cut/join component boundary under the second posterior resampling.

The obstruction remains taking absolute values only after the complete
sixteen-schema sum. Conditioned-Borel laws of sizes `d` and `d+1` differ at
order `d^-3/2`, not `d^-2`, so a direct adjacent-size fragment coupling still
loses too much. No signed cancellation estimate controlling the complete
posterior predictive was proved here. Consequently the endpoint-sharing
influence lemma remains **unresolved**.

## 7. Dependencies and caveats

- **Accepted here:** the frozen M73 proved claims and exact finite
  certificates, with zero objections.
- **Proved here:** universal `diam(Lambda_n)<=4` and its exact Dobrushin/
  eigenvalue implication.
- **Exact finite:** independent rational checks through `n=9`; localized
  graph diameters through `n=21`.
- **Floating finite only:** localized TV scaling through `n=21`.
- **Open:** endpoint-sharing influence, the sharper diameter-three claim, the
  `H_0` gap, and every bridge/global mixing conclusion.

The exact `n=5` obstruction remains outside the proposed influence lemma.
Odd identity length, `m=0,2`, `N=2`, and identity-bridge calibrations are
outside this nonidentity minimal-long-cycle target.

## 8. Reproduction and artifacts

Primary artifacts:

- `plan.md`, `checkpoint.md`, `report.md`;
- `independent_exact_audit.py`, `independent_exact_audit_n9.json`;
- `schema_rerun_n7.json`, `kernel_rerun_n9.json`;
- `localized_source_metric.py` and its JSON outputs through `n=21`.

Representative commands from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/independent_exact_audit.py --n 5 7 9 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/independent_exact_audit_n9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/localized_source_metric.py --n 7 9 11 13 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/localized_source_metric_n13.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/localized_source_metric.py --n 15 17 19 21 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M80-m73-referee-adjacent/localized_source_metric_n21.json
```

All computations are deterministic with `seed=null`, Python `3.12.3`, and
NumPy `1.26.4` where used.

## 9. Final verdict

**ACCEPT FROZEN M73; PROMOTE THE PROVED DIAMETER-FOUR LOCALIZATION, NOT THE
OPEN INFLUENCE BOUND.**

M73's reduction survives fresh audit. The continuation strictly localizes its
remaining analytic obligation to one three-cycle cut/join perturbation while
preserving constant source-graph diameter. This is proof progress, but it is
not an `H_0` gap or a Terminal result.
