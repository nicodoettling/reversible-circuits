# M155 final report: boundary-condensate threshold for balanced direct L1

Date: 2026-08-13. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and scope

```text
VERDICT: STRICT BOUNDARY-CONDENSATE REDUCTION.
DIRECT O(k^-2) L1: UNRESOLVED.
```

For `n=3k`, odd `k>=3`, this mission studies only M73's nonlazy cyclic
rank-two quotient kernel under the uniform law on minimal length-`n-1`
transposition factorizations of the long cycle, at

```text
A_k=(0,k,2k),             B_k=(0,1)(k,2k).
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The result is not about the identity-word target or the lazy `{3,4,5}`
heat-bath kernel.  It proves neither the assigned sharp L1 bound nor a
counterexample, H0 theorem, bridge gap, identity-chain gap, or Terminal.

## 2. Strongest proved reduction

Let

```text
z_k(O)=[bar K^2(O_B,O)-bar K^2(O_A,O)]/bar pi(O),
2 TV=E_barpi|z_k|.
```

This is M94's exact complete signed score: both M91 channels and every
triangle/double intermediate topology are combined before taking absolute
values.  For a separated double-target encoding with gaps
`(a,y,b,c-y)`, where `c=3k-a-b`, define

```text
A_k(a,b)=1/(c-1) sum_(y=1)^(c-1) k^2|z_k(a,y,b,c-y;S)|,
W_n(a,b)=(c-1)Gamma_n b_a b_b b_c/2,
Gamma_n=n(n-3)!e^n/n^(n-2).
```

Every double orbit has exactly four colored encodings, two separated and
two nested.  Giving each encoding one quarter of its orbit mass proves the
exact identities

```text
sum_(a,b)W_n(a,b)=(n-3)/(2n),
k^2 E[|z_k|1_D]=2 sum_(a,b)W_n(a,b)A_k(a,b),

2k^2 TV=k^2 E[|z_k|1_T]+2 sum_(a,b)W_n(a,b)A_k(a,b). (2.1)
```

There is no missing stabilizer: odd-`n` double orbits all have size `n`, and
the factor two in `(2.1)` is exactly the two separated encodings out of four.
Duplicated orbit appearances among colored encodings are intentional and
are resolved by the quarter mass.

For each fixed `a,b>=1`, as odd `k->infinity`,

```text
W_(3k)(a,b)->(1/2)b_a b_b,
```

and the normalized weights converge in total variation to two independent
critical-Borel variables.  Their minimum is exactly at the logarithmic
summability threshold:

```text
sum_(1<=a,b<=D)b_a b_b min(a,b)=(2/pi)log D+O(1).    (2.2)
```

Consequently, if one common `lambda>0` satisfies, for every fixed `a,b`,

```text
liminf_(k odd->infinity)A_k(a,b)>=lambda min(a,b),   (BLM)
```

then `liminf k^2 TV=infinity`; the assigned constant `O(k^-2)` estimate is
false.  The proof fixes `D`, applies the finite-sum liminf inequality to
`1<=a,b<=D`, and only then sends `D->infinity`.  If the same lower bound is
uniform for `a,b<=k^theta`, `0<theta<1`, then

```text
TV=Omega(log k/k^2).                                 (UBL consequence)
```

Neither `(BLM)` nor its uniform version is proved.

## 3. Exact positive and logarithmic targets

Equation `(2.1)` makes the exact positive obligation

```text
sup_(k odd) k^2 E[|z_k|1_T]<infinity,
sup_(k odd) sum_(a,b)W_(3k)(a,b)A_k(a,b)<infinity.   (BCL-sharp)
```

A product-Borel-summable fixed-cell envelope can help, but it additionally
needs uniform integrability for the actual finite-`n` weights: when
`c=n-a-b` is small, `W_n/(b_ab_b)` is not uniformly bounded.  This tail
qualification is material.

The weaker standalone target is

```text
k^2 E[|z_k|1_T]+2 sum_(a,b)W_(3k)(a,b)A_k(a,b)
 <=C log(2+k).                                       (BCL-log)
```

It is exactly `TV=O(log k/k^2)` for this balanced family.  A uniform
all-strict-edge analogue, together with M80's diameter-at-most-four theorem,
would give `delta(bar K^2)=O(log n/n^2)` and hence, by self-adjointness,
`|kappa|=O(sqrt(log n)/n)`.  Thus even a logarithmic obstruction to the
assigned sharp constant would leave polynomial decay in M73's H0
coordinate-Gram route.  The balanced theorem alone gives no such all-edge
conclusion.

The new first unresolved statement is **BOUNDARY-CELL SCORE DICHOTOMY
`(BCL)`**: prove `(BCL-sharp)` or `(BCL-log)`, or prove `(BLM)`/its uniform
mesoscopic version from the exact M94 posterior convolution.

## 4. Why the M102/M105 obstruction is retained

M102/M105 prove that a generic double/double continuum density has a
nonintegrable collision face and do not prove that triangle strata are its
complete counterterm.  Here every collision, exact small-Borel layer, and
lower-support topology remains inside the finite score `z_k` before
`|.|` and before averaging over `y`.  The reduction therefore neither uses
the invalid bulk-only limit nor assumes collision/triangle completeness.

## 5. Exact validation and finite calibration

`boundary_condensate_check.py` uses only the standard library.  Over exact
`Fraction` arithmetic it checks the point-cell formula and

```text
sum_(a,b)W_(3k)(a,b)=(3k-3)/(6k)
```

for `k=3,5,7,9`, obtaining respectively `1/3,2/5,3/7,4/9`.  Floating
partial sums through `D=100000` calibrate `(2.2)` only; the proof uses
Stirling and the layer-cake identity.  The checker also records hashes and
compact summaries of the already retained M94 `k=7,9` shell files.  Those
shell profiles have approximately constant `d*k^2` absolute shell mass over
an interior range, but they aggregate colors and cells and do not test
`(BLM)`.

Reproduction from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M155-balanced-direct-l1/boundary_condensate_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M155-balanced-direct-l1/boundary_condensate_results.json
```

Python `3.12.3`; deterministic; `seed=null`; no nonstandard dependency.
Two attempted redundant broad shell builds were capped and interrupted at
ten and three minutes.  Their source writes only after all requested ranks,
so neither produced an output and neither contributes evidence.

## 6. Dependencies, self-attack, and status ledger

- **Accepted inputs:** M73/M80 exact quotient kernel and strict-edge
  geometry; M83/M88 balanced edge; M91 posterior/Borel--Abel identity;
  M94/M100 colored compositions, exact score, and shell mass;
  M102/M105 singular-face warning and topology scope correction.
- **Proved here:** `(2.1)`, product-Borel boundary condensation, `(2.2)`,
  `(BLM)` implication, uniform `(UBL)` logarithmic implication, and the
  exact formulations `(BCL-sharp)`/`(BCL-log)`.
- **Exact finite:** colored-cell identities at `k=3,5,7,9`.
- **Finite floating only:** inherited shell calibration at `k=7,9`.
- **Unresolved:** the score alternatives, direct L1, `(BD)`, `(BA2)`, the
  general strict-edge theorem, H0, every bridge/identity-chain gap, and both
  Terminals.

The strongest self-attack is decisive: the product-Borel law says nothing by
itself about `A_k(a,b)`.  Even `(1,1)` could have a bounded or vanishing
limit because the exact collision and lower-support contributions may cancel
inside `z_k`.  Minimum-residual shell data do not isolate `(a,b)` or color.
Thus this is a strict, falsifiable reduction—not a proof or refutation of the
assigned direct-L1 estimate.

## 7. Hygiene and verdict

M155 changed only its owned directory.  It installed no package, used no
network, and made no commit or push.  No predecessor, coordinator, manuscript,
goal, skill, or shared project file was edited.  No generated Python cache is
retained.

**Final verdict: STRICT BOUNDARY-CONDENSATE REDUCTION; DIRECT L1
UNRESOLVED.  Prioritize fixed-cell score asymptotics, beginning with
`(a,b)=(1,1)`, before another broad shell computation.**

