# M188 fresh referee report on frozen M187

Date: 2026-08-13 UTC. Audited repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: REJECT M187 AS A CITABLE FROZEN PACKAGE.
SALVAGE THE APPEND-ONLY CORRECTED EXACT FINITE RESULT.
NUMBERED MATERIAL OBJECTIONS: FOUR.
```

M187's controlling `final_scope.md` and `audit_correction.md` correctly retract
its geometric all-`d` locality theorem. However, the ordinarily cited
`proof.md` and nine-field `report.md` still label that superseded theorem as
proved. Because an ordinary citation can mislead, separate controlling files
do not make the whole frozen package acceptable as a theorem artifact.

The exact finite `d=5`, width-two result is independently reproduced and
accepted: 14 positive route certificates among 54 targeted eligible quotient
targets in the radius-five ball. No miss is used negatively.

```text
candidate                  | M181 d=5 width-two source pair
claimed target             | matched DPS target quotient tuples
identity ok                | all 72 checked source/target words pass
crosses Hurwitz components | exact only for 14 stored positive routes
exact diagnostics          | ten rooted inversions; 70 targets; radius-five ball
verdict                    | reject package; salvage corrected finite result
```

## Field 2 — immutable provenance and hashes

M187's complete thirteen-entry SHA inventory passed before any payload was
used. Its top-level digest is

```text
02b9ab4d382c6b52945492d6b808a3dad22eb51eb6d0d3e8eecc364a06bc28b2  SHA256SUMS
```

Observed payload hashes are:

| M187 artifact | SHA-256 |
|---|---|
| `audit_correction.md` | `c68a18c023513ae66a762b546f091c2ba4d01c0bf2be3b4012b509b4400f53fe` |
| `checkpoint.md` | `e73ac0031f9ce3190cdca21ef70414ead2e4c5af4c9dd00649cc00dd875d8a87` |
| `checkpoint_final.md` | `2c5f0e5dd6b82d6f5337ab4d6835ec58844ac1667737284ee949b3e2a5bccd0c` |
| `compact_results.json` | `d3345a688eca97c875d08fbff8c276cdb07601f9f1eaf59cfaf2475cd9a60a4d` |
| `final_scope.md` | `c5db3e2b3243a694e2391f302b7f0017cc407e0fa80ded41398ee3f59cba148d` |
| `freeze_manifest.md` | `f0cfb40d4a18ed5c150799adacd72a393b52816e7d9571745886f0d497527e74` |
| `freeze_manifest_final.md` | `02b94648f2ed9ccd3f814152557f82c93ed74a1693638fbe6a22474badef0b16` |
| `halfway_checkpoint.md` | `fb139cff00cd5625bf38cc59a7359ec71bcf147daff39c4354488eac2638154b` |
| `plan.md` | `350cb0780faef0e89d8338d68cec612917049dca4a4b97cfd923e811153cd51b` |
| `proof.md` | `2076f2bcae1210bfe8058e40982e670c1a0463ff12167bdac6b2a67dfe132fef` |
| `report.md` | `4bceeb1101dfd060dadd983de3d0fbb6a64abb10d89117fc06076d6bc2480725` |
| `targeted_dps_probe.py` | `110924eacbf531bfd7b88dcade37304674a244a6f373a4c65f02db9ed385a17a` |
| `targeted_results.json` | `188bcd785b4b597f3a094aaae450986275bc0ac47af5306a1bb9ddee989e2c90` |

M187 remained immutable throughout this referee mission.

## Field 3 — controlling scope and stale artifacts

The controlling files were read before all earlier prose. They unambiguously
retain only:

```text
PROVED BUT FORMAL: exact zero-aligned/one-step-aligned endpoint criterion.
EXACT FINITE: 14 positive d=5 width-two routes among 54 targeted targets.
UNRESOLVED: every-color routing and every nonformal all-d selection rule.
```

This control is logically clear but bibliographically unsafe. `proof.md`
Section 3, `report.md` Fields 1/4/6/9, the original freeze manifest, and both
substantive checkpoints continue to assert or endorse the retracted geometric
theorem. The package therefore fails as a citable unit. The corrected files
and this referee report can be cited append-only for the salvaged result.

## Field 4 — clean-room DPS target reconstruction

The independent checker reimplements permutation arithmetic, both signed
Hurwitz moves, global quotient canonicalization, Prüfer-tree generation, the
rooted plus-mirror hairy-tree boundary/closure, targeted DPS inversion, and
adjacent-value edits. It imports no M187 code or result.

It starts only from

```text
V=(01)^2(02)^2(13)^2(04)^2,
U=(01)^2(02)^2(03)^2(04)^2.
```

Both sources evaluate to identity and have connected all-label support. All
ten rooted descriptors close back to their relabeled source. The seven edits
produce seventy coordinate/root targets; every target again passes identity
and connected-support checks.

The `7*5*5=175` root-pair occurrences are all eligible (the two right
endpoints differ) and collapse to exactly 54 distinct ordered quotient target
tuples. Comparing only after this independent result existed found all seventy
canonical target rows identical to frozen M187.

## Field 5 — independent fourteen-route replay

The checker explores only the signed-Hurwitz quotient ball of radius five
around the named ordered source pair. Level sizes are

| depth | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|---:|
| states | 1 | 6 | 40 | 190 | 795 | 2,976 |

Thus 4,008 quotient tuples are visited. Exactly 14 of the 54 targeted tuples
occur, at path lengths

```text
0,1,1,1,1,1,1,2,2,3,3,3,3,5.
```

Unlike M187's JSON, M188 archives all fourteen explicit signed paths and their
root/edit occurrences. Applying every path afresh reaches its stored target.
The normalized route-record digest is

```text
e87ecd4742ab7392b3ef189f3f05a17757b75fac3fdba675074216468947fdc2
```

For roots `(0,0)`, the positive routes are empty at edits `1,3,7` and the
one-letter paths `R_2,R_4,R_6`; edit 5 is absent from this radius-five witness
set. All claim-bearing summaries and seventy target rows match M187.

## Field 6 — exact endpoint criterion and matching interface

The corrected formal criterion is valid. If every selected coordinate
satisfies

```text
[tau_i(u_c)]=[u_c],
```

then the empty synchronized word reaches the target tuple. If all satisfy

```text
[tau_i(u_c)]=R_i[u_c],
```

then the synchronized one-letter word `R_i` does. These are direct
consequences of the hypotheses and constitute no nonformal selection theorem.

M135 perfectness does not supply either hypothesis. A color selects an
arbitrary `H=Stab(d)`-orbit edge above each left global orbit. Braid action is
`G=S_d`-equivariant, while `tau_i` is accepted only as `H`-equivariant. An
arbitrary coordinatewise relabeler moving `d` therefore transfers M181's
source loops but not its DPS target. Distinct matched right endpoints likewise
do not imply a common quotient braid. The every-color route remains
unresolved.

## Field 7 — numbered objections

1. `proof.md` materially labels the superseded geometric all-`d` DPS-locality
   lemma as proved.
2. `report.md` materially repeats that theorem and requests its audit, so an
   ordinary report citation overclaims despite the separate correction.
3. The original freeze manifest and checkpoints retain stale scope and
   incomplete inventory prose, although the controlling manifest and actual
   checksums preserve integrity.
4. `report.md` says the positive path sequences are stored, but M187 archives
   only their count and lengths. The code recomputes them and M188 now stores
   them, so this is a reproducibility defect rather than a numerical refutation.

These objections require rejection of the frozen package as a citable theorem
artifact. They do not disturb the corrected finite statement.

## Field 8 — reproduction and hygiene

M188 uses Python `3.12.3`, standard library only, dependencies `{}`, and
`seed=null`. From the M188 directory:

```text
python3 -B independent_replay.py
python3 -B compare_frozen.py
```

The first command is clean-room and reads no M187 artifact. The second runs
only after the independent JSON exists and compares it with frozen M187 data;
it imports no M187 code. No `Z_5`, `Q_5`, action group, or quotient component
is broadly enumerated.

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`audit_notes.md`, `independent_replay.py`, `independent_results.json`,
`compare_frozen.py`, `comparison_results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`. No file outside M188 was edited.

## Field 9 — final decision

```text
REJECT M187 AS A CITABLE FROZEN PACKAGE.
ACCEPT THE APPEND-ONLY CORRECTED 14/54 EXACT FINITE RESULT.
ACCEPT ONLY THE FORMAL EXACT-ENDPOINT CRITERION.
KEEP EVERY-COLOR QUOTIENT ROUTING UNRESOLVED.
```

No conclusion follows from the forty bounded-search misses. No nonformal
all-`d` DPS locality, asymptotic route length, spectral gap, mixing, or
Terminal claim is accepted.
