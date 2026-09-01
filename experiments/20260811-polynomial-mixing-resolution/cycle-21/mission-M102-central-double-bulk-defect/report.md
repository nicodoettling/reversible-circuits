# M102 final report: collision renormalization blocks the naive bulk limit

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, target, and controlling verdict

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  For `n=3k`, odd `k>=3`, retain frozen M94's uniform minimal
long-cycle factorization law, nonlazy rank-two quotient kernel, balanced
sources

```text
A_k=(0,k,2k),       B_k=(0,1)(k,2k),
```

and central double event `E_k` whose four cyclic support gaps are at least
`(k+1)/2`.

The mission verdict is:

```text
STRICT ASYMPTOTIC OBSTRUCTION; (BD) REMAINS UNRESOLVED.
```

It proves that the tempting generic double/double continuum integral for
`k^2 Delta_k(E_k)` is nonintegrable.  An explicit rational collision cell has
a complete signed integrand

```text
F(delta)=-C delta^(-3/2)+O(delta^(-1/2)),   C>0.
```

Therefore the discrete small-Borel-component and collision/triangle layers
must be retained as a renormalizing counterterm.  The remaining falsifiable
statement is the matched finite-part transfer `(MBF)` in the proof note.
`(BD)`, `(BA2)`, and direct signed L1 are not decided.

## 2. Exact proved advance

M94's raw event convolution and M91's channel-combined Abel formula are
reproduced in `bulk_defect_obstruction.md`, equations `(1.1)--(1.2)`.  No
absolute value or targetwise square is inserted.

For

```text
s=(1/10,1/9,24/25,24/25+delta),       separated color,
t=(1/7,9/20,5/7,15/16),               separated or nested color,
```

the residual topology gives exact positive factors frozen by
`collision_face_symbolic.json`.  The coefficient of `delta^-3/2` is

```text
[(5400/59)^(3/2)-(2700/29)^(3/2)]
 (89/8100)^(3/2)
 [(284497920/99373)^(3/2)
  +(1317120000/398453)^(3/2)].
```

It is strictly negative because `5400/59<2700/29`; hence writing it as `-C`
gives `C>0`.  The neighboring positive residual factors are smooth, so their
first-order Taylor remainder times `delta^-3/2` is
`O(delta^-1/2)`.  That remainder is locally integrable, while the leading
term is not.  This proves the naive unrenormalized bulk integral diverges on
an open set of the other coordinates.

A second, finite-floating falsification candidate attacks pointwise score
positivity on `E_k`.  At `k=9`, the separated target with gaps
`(5,5,5,12)` has `9z_k=-0.410159...`.  The margin is far above roundoff, but
the retained probe is not an exact-rational certificate, so this is labeled
**empirically refuted** rather than proved false.

## 3. Probability, multiplicity, and cancellation accounting

- The law is the uniform minimal factorization law for a long cycle, not the
  global identity bridge.
- The kernel is M73's exact nonlazy pair-product quotient kernel.  The
  original lazy `{3,4,5}` heat-bath kernel is not substituted.
- M94's `a=3` triangle and `a=2` double lift counts and literal cyclic orbit
  factors remain in the exact finite sum.
- The collision coefficient retains the full signed source contrast `B-A`
  and both separated and nested target colors before its sign is taken.
- The collision face is where a separated double intermediate loses a
  support gap.  The finite lattice layers of component size `r=O(1)` and the
  collision/triangle topology are not lower order; they renormalize the
  formal `epsilon^-1/2` bulk divergence.
- The exact radical certificate is deterministic and standard-library only.
  The score table uses the accepted kernel construction and converts to
  floating arithmetic only after exact integer completion counts.

## 4. Dependencies and status labels

- **Accepted proved inputs (M91/M94/M100):** exact two-channel Abel identity,
  exact orbit-aware Borel convolution, Abel coefficient asymptotics, central
  event mass `Theta(k^-1)`, and the Cauchy implication `(BD)=>(BA2)`
  refutation.
- **Proved here:** explicit nonintegrable rational collision cell and its
  exact signed radical coefficient; identification of the required discrete
  small-component/collision topology.
- **Deterministic finite only:** the `k=7,9` score profile and the bounded
  Sobol falsifier that exposed the nonintegrability; pointwise positivity is
  empirically refuted by a large-margin witness.
- **Unresolved:** `(MBF)`, the finite-part constant and its sign, `(BD)`,
  `(BA2)`, direct signed L1, the general strict edge, H0, every bridge or
  identity heat-bath gap, and both Terminals.

No new literature theorem is used.

## 5. First unproved standalone lemma

> **MATCHED BOREL FINITE-PART TRANSFER `(MBF)` (unresolved).**  Truncate the
> exact M94 event convolution at separated-double intermediate gaps at least
> `epsilon n`; add the exact layers `1<=r<epsilon n` and the collision/triangle
> boundary topology with literal lift/orbit factors; combine the two source
> channels and both target colors before taking limits.  Then
>
> ```text
> k^2 Delta_k(E_k)=C_*+o(1)
> ```
>
> for a finite constant `C_*`, with cancellation of the
> `epsilon^-1/2` terms before `epsilon->0`.

Proving `C_* !=0` would settle `(BD)` and thereby refute `(BA2)` only.  It
would leave direct signed `L1=O(k^-2)` open.

The suggested exact interface is to subtract the boundary value inside the
Borel sum before applying Stirling/Euler--Maclaurin:

```text
sum_r b_r H_k(r/k)
 =sum_r b_r[H_k(r/k)-H_k(0)]+H_k(0)sum_r b_r.
```

The bracket should leave the integrable `x^-1/2` singularity; the last term
is paired with the collision/triangle counterterm.

## 6. Strongest self-attack

The collision obstruction does not prove that a finite part exists, much
less that it is nonzero.  Its sign cannot be transferred to the exact finite
defect: the discrete boundary counterterm can dominate or cancel it.  The
finite positive values of `k^2 Delta_k(E_k)` through `k=11` do not resolve
this.  Moreover, the `k=7,9` score probe shows cancellation already within
the central event.  The only safe conclusion is that a generic bulk-only
Riemann limit is invalid and `(MBF)` is necessary.

The rational cell establishes local nonintegrability of the formal density,
not a divergence of the exact finite convolution.  The exact convolution is
finite at every `k` and contains precisely the boundary layers suppressed by
the failed continuum replacement.

## 7. Falsification and diagnostics

`bulk_score_probe.py` was run only at `k=7,9`, never beyond `k=9`.  It
reproduces M94's event mass and defect:

| `k` | `k pi(E_k)` | `k^2 Delta_k(E_k)` | `k Delta/pi(E)` |
|---:|---:|---:|---:|
| 7 | .07314864 | .04320591 | .59065907 |
| 9 | .07224023 | .04216567 | .58368673 |

These are formula checks only.  At `k=9`, seven of 60 event orbits have
negative score and `kz_k` ranges from `-.4102` to `1.3503`.

The bounded `2^12`-point Sobol probe of the naive integral produced a block
standard deviation larger than its mean and extreme collision values.  It is
retained under the explicit status
`deterministic_qmc_falsifier_naive_integral_nonintegrable`; its printed
"candidate" arithmetic is not a coefficient estimate.  The exact symbolic
certificate, not the QMC output, proves nonintegrability.

Boundary scope: the family begins at `k=3,n=9`; `k=1`, even `k`, other odd
`n`, identity endpoints, `m=0,2`, and `N=2` are outside it.

## 8. Artifacts, commands, runtime, and hygiene

Owned artifacts are `plan.md`, `checkpoint.md`,
`bulk_defect_obstruction.md`, this report, two compact diagnostic scripts,
one exact symbolic script, three JSON payloads, and `SHA256SUMS`.

Representative commands from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/bulk_score_probe.py --k 7 9 --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/bulk_score_probe_k9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/collision_face_symbolic.py --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/collision_face_symbolic.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/continuum_bulk_integral.py --power 12 --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M102-central-double-bulk-defect/naive_bulk_qmc_falsifier.json
```

The quotient probe took about six minutes on this host; the compact symbolic
and bounded Sobol runs took seconds.  All runs are deterministic with fixed
or null seeds.  No package, network, commit, push, predecessor, coordinator,
manuscript, or skill file was changed.  Generated caches are removed before
freeze.  JSON parsing, Python syntax, checksums, `git diff --check`, and owned
status are checked below.

## 9. Verdict and action

**STRICT ASYMPTOTIC OBSTRUCTION; KEEP `(BD)` OPEN AND REPLACE THE NAIVE BULK
INTEGRAL BY `(MBF)`.**

M94's central-event signal remains a credible threat to `(BA2)`, but this
mission neither proves nor refutes it.  The key new durable lesson is that
support-collision strata are leading-order renormalizers for the Borel
convolution.  Any next attack must derive the matched finite part with the
discrete small-component and triangle boundary terms before evaluating a
sign.  Even success would refute only `(BA2)` and would leave the direct-L1
route and the original mixing question unresolved.
