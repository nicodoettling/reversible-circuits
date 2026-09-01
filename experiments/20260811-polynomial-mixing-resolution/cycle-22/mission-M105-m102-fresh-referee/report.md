# M105 fresh referee report on frozen M102

Date: 2026-08-12. Audited commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, accepted claim, and scope

```text
ACCEPT M102's explicit nonintegrable collision-face proposition.
Required numbered scope corrections: one.
Nonmaterial normalization clarifications: one.
```

For `n=3k`, odd `k>=3`, retain the uniform minimal-long-cycle
factorization law, M73's nonlazy rank-two quotient kernel, sources
`A_k=(0,k,2k)` and `B_k=(0,1)(k,2k)`, and M94's central double event.
The accepted result is exactly that the naive generic double/double
continuum density has an open rational cell on which

```text
F(delta)=-C delta^(-3/2)+O(delta^(-1/2)), C>0.
```

Its ordinary improper bulk integral diverges locally to `-infinity` and
cannot by itself prove `(BD)`. This is a failed continuum transfer for a
coordinate kernel of the minimal long-cycle bridge, not a result about the
identity-word target or lazy `{3,4,5}` heat-bath kernel. The audit does not
accept as proved that a triangle stratum is the exact complete matching
counterterm; Section 6 gives the required scope correction.

## 2. Frozen provenance and package integrity

The assigned hashes independently match:

| M102 artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `0e8f82a63c0e936e0f466bf9d33f9e1182f58fd48c2491998f0f7f5ffb7a5c1e` |
| `bulk_defect_obstruction.md` | `57c38e10a519ff9f2bdeaf6d0893e18554911337adee9c4001bf13442d8edf4b` |
| `SHA256SUMS` | `54ac293104a246f087c8ce8571c800301655e01d641769437f43b6398a0257ef` |

`sha256sum -c SHA256SUMS` returned `OK` for all ten M102 entries. The M94
and M100 manifests also passed completely before conclusions were read. No
predecessor, coordinator, manuscript, skill, or other worker file was edited.

## 3. Target, convention, and dependencies

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Inherited proved inputs are M91's channel-combined Abel
identity and M94/M100's orbit-aware Borel event convolution, Abel
asymptotics, central-event mass, and conditional Cauchy implication. No new
literature theorem is used. This referee derived the collision topology from
labeled support permutations rather than assuming M102's residual lists.

## 4. Residual topology, colors, lifts, and orbit factors

`independent_collision_audit.py` imports no predecessor code. It uses exact
affine support positions in `delta` and in an infinitesimal `eps` for B's
adjacent edge. Direct permutation composition gives

```text
A*s_S:       delta, 1/90, 29/90, 1/3-delta, 1/3
B*s_S:       delta, eps, 1/90, 1/3, 59/90-delta-eps
s_S:         delta, 1/90, 89/90-delta
s_S*t_S:     delta, 1/90, 25/112, 43/140, 2311/5040-delta
s_S*t_N:     delta, 1/90, 979/5040-delta, 37/140, 297/560.
```

These reproduce all M102 face lists. The target gaps are
`43/140,37/140,25/112,23/112`, strictly above `1/6`, so an open
neighborhood remains in the event. The nested intermediate has no
`delta`-zero residual and is bounded. The crossing matching has one residual
cycle rather than the required three and is inadmissible, so S and N exhaust
the generic target colors at this cell.

For double intermediate and target states, `a(s)=a(t)=2`; hence the raw lift
factor is four. There is no further quotient-orbit factor in the invariant
raw event formula: raw target positions already count all translations. In
the finite quotient, `|O_A|=k`, `|O_B|=n`, and every odd-`n` double orbit has
size `n`; these sizes do not multiply the source-row event defect.

## 5. Sign, normalization, Taylor remainder, and open-cell audit

The independently derived face bases are

```text
source A 2700/29       source B 5400/59
intermediate 89/8100
joint SS 284497920/99373
joint SN 1317120000/398453.
```

Thus M102's stripped two-target-color coefficient is

```text
R=[(5400/59)^(3/2)-(2700/29)^(3/2)]
   (89/8100)^(3/2)
   [(284497920/99373)^(3/2)
    +(1317120000/398453)^(3/2)] < 0.
```

The sign is exact because `5400/59<2700/29`; `R=-8990.626343656686...` is
only a display. Restoring `a(s)a(t)=4`, the net critical-Borel factor
`(2*pi)^-2`, and `n=3k` gives the normalized local coefficient in direct
support-position coordinates

```text
4*(2*pi)^(-2)*(k/n)^2*R = R/(9*pi^2)
                       = -101.21565586947543... .
```

No source lift or source-orbit factor belongs here. After extracting
`delta^-3/2`, every other residual is bounded away from zero on a small
closed product box. Its coefficient is uniformly `C^1`, so
`G(delta)=G(0)+O(delta)` and the remainder is `O(delta^-1/2)`. The strict
negative sign persists on a smaller positive-volume box with bounded positive
Jacobian. Therefore the unrenormalized integral diverges there to
`-infinity`. M102's Proposition 1 is rigorous.

## 6. Numbered objections and corrections

1. **Required scope correction: complete matching topology is unresolved.**
   M102 proves that the generic-bulk replacement fails and exact small-`r`
   Borel layers cannot be discarded. It does not exhaustively glue all
   collision cells to lower-support cells, handle intersecting faces, or
   prove a literal triangle/double lift-and-orbit multiplicity identity.
   Finiteness at each `k` does not imply cancellation of an
   `epsilon^-1/2` term in scaled `k^2 Delta`; that scaled sequence could fail
   to converge. Safe wording is:

   ```text
   exact small-component layers are necessary;
   triangle/collision and other lower-support strata are candidate
   same-order counterterm classes whose topology and multiplicities remain
   to be exhaustively matched.
   ```

   `(MBF)` may include triangle terms in its proposed expansion, but their
   coefficient, completeness, and cancellation remain part of that
   unresolved lemma.

2. **Nonmaterial normalization clarification.** M102's radical is the
   correct stripped coefficient. The complete local `k^2 Delta`
   position-density coefficient is `R/(9*pi^2)`. This changes neither sign
   nor nonintegrability.

There is no objection to the residual lists, source contrast, target-color
sum, `O(delta^-1/2)` remainder, or open-cell divergence.

## 7. Fresh symbolic and finite `k=7,9` checks

The frozen symbolic program rerun into `/tmp` reproduced its exact bases.
The independent affine program reconstructed them without hard-coded lists.
`independent_finite_probe.py` also imports no predecessor code: it constructs
ordered transposition pairs, exact integer completion counts, admissible
states, quotient rows, and the event; only final matrix arithmetic is
`float64`. It obtains:

| `k` | `k*pi(E)` | `k^2 Delta(E)` | negative event orbits | range of `k z` |
|---:|---:|---:|---:|---:|
| 7 | .07314864161123523 | .04320590873435413 | 3/28 | `[-.276094,1.218981]` |
| 9 | .07224023359526269 | .04216566592865655 | 7/60 | `[-.410159,1.350249]` |

Exact event-mass and orbit-count formulas, quotient normalization, source
orbit sizes, and all-double orbit sizes pass. The `k=9` minimum is the
separated gaps `(5,5,5,12)` witness. These are deterministic finite formula
checks only, not asymptotic evidence.

## 8. Artifacts, commands, and hygiene

M105 owns `plan.md`, `checkpoint.md`, two scripts, two JSON outputs, this
report, and `SHA256SUMS`. Decisive commands were

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M105-m102-fresh-referee/independent_collision_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M105-m102-fresh-referee/independent_collision_audit.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M105-m102-fresh-referee/independent_finite_probe.py --k 7 9 --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M105-m102-fresh-referee/independent_finite_probe_k9.json
```

Both are deterministic with `seed=null`, Python `3.12.3`; the finite script
uses NumPy `1.26.4`. No package, network, random input, commit, push, or
external write was used. JSON parses, scripts execute, caches are absent,
and the final manifest covers every retained artifact except itself.

## 9. Verdict, status ledger, and action

**ACCEPT THE NONINTEGRABLE SINGULAR-FACE THEOREM, WITH THE REQUIRED TOPOLOGY
SCOPE CORRECTION IN SECTION 6.**

```text
exact residual topology and two target colors              proved
coefficient, strict sign, and local normalization           proved
O(delta^-1/2) remainder and open-cell nonintegrability      proved
necessity of exact small-r layers                           proved
triangle as exact complete matching renormalizer            unresolved
existence/cancellation/nonzero value in (MBF)               unresolved
(BD), (BA2), direct signed L1                               unresolved
H0, bridge/identity gaps, both Terminals                    unresolved
```

The safe next lemma must enumerate all small-component and lower-support
strata with literal lift/orbit multiplicities, prove a uniform matched
subtraction, and only then evaluate the finite part. Nothing in M102 decides
`(BD)`, refutes `(BA2)`, proves direct signed `L1`, or advances a spectral-gap
Terminal by itself.
