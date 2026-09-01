# M136 freeze manifest

Freeze date: 2026-08-13 UTC.

## Identity and verdict

- Mission: `M136-m133-fresh-referee`
- Upstream frozen mission: `M133-defect-coefficient-no-valley`
- Verdict: **ACCEPT**, zero objections
- Target: M113/M118 auxiliary incidence-key coefficient law `rho`, not the
  original identity-word law
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Dependencies: Python standard library only
- Random seed: `null` (all work exact and deterministic)

## Frozen upstream identity

| M133 artifact | SHA-256 |
|---|---|
| `report.md` | `afd0fcc3dddc51f20c8eb2d3b2d7eeb2d25aa3c9eaea204d91b958adf537619e` |
| `positive_unicycle_reduction.md` | `c80606c1d821c82df8c2d2ab9e4d4be01baa4032046d896cba2604f60c299fb9` |
| `positive_unicycle_audit.py` | `5eefdff04b13de058ddafcc9767aae84f5b2b96b7bc9c75896cfeb3cc2a34e82` |
| `positive_unicycle_results.json` | `1a83ddc483f0b8bad2d6c917e4a726e20406066cac9139dfacdf7b9a9635ff00` |
| `core_profile_scan.py` | `b4cbba5dabace6469695abb852c2f07d54a310fd2cbf884d1cabb95db8509b75` |
| `core_profile_results.json` | `ff55915705acc7ea3377e93ca2a1f7fb206f9f0578b4cea4cad384ac48689e0e` |
| `freeze_manifest.md` | `b3d8707a60fb93c7f3439ed1d995ab8694df01cbed5f96f8c1e1880724240b92` |
| `SHA256SUMS` | `62cfd64d796a22de62ecf25f0b266fc9d64a8a51a731d148733d8599a90e7bfb` |

The complete upstream `sha256sum -c SHA256SUMS` check passed from the M133
directory before audit.

## Decisive fresh checks

- Universal unique-even-core and planted-tree bijection audited in proof.
- Fixed-first coloured-core encodings injective for core lengths `2,4,6,8`.
- 58 cycle types through `d=8` matched an independently rooted connected
  recurrence.
- 37 cycle types through `d=7`, totaling 864,261 ordered partition pairs,
  matched literal graph-pruned core profiles.
- Frozen weighted core profiles through `d=8` reconstructed exactly.
- `d=4,c=3` pairwise polarization margin independently recovered as
  `-17309376`.
- Independent frontier recurrence matches completed for `(d,r)=(23,7),
  (24,8),(25,8)` before the finite-only scan was capped.
- Stored arithmetic and independent cycle-type counts pass for all four
  frontier cases through `(26,9)`; the `d=26` masses were not independently
  recomputed.

## Commands

Final reproducible result:

```text
python3 -B independent_referee.py \
  --small-max-d 8 --direct-max-d 7 \
  --output independent_results.json
```

Capped frontier run:

```text
python3 -B independent_referee.py --skip-small \
  --frontier-case 23:7 --frontier-case 24:8 \
  --frontier-case 25:8 --frontier-case 26:9 \
  --output frontier_results.json
```

The latter was interrupted during `(26,9)` before the output JSON write.  Its
three completed `match=True` lines and the precise limitation are preserved
in `frontier_partial.md`.  No `frontier_results.json` is claimed or frozen.

## Frozen M136 artifact hashes before manifest

| artifact | SHA-256 |
|---|---|
| `plan.md` | `87b4be1346f7f3eb91b5a1bd94b29a1621c949e0c58256c4fee81b325ba8b490` |
| `checkpoint.md` | `68cc2b64f69ccdc3f1fcce4131621a7173425ead3425abfeae5a95d13e101337` |
| `independent_referee.py` | `b76fbfd9683953913f87b729f8dd165d37f4a20a85e549b2e961c0d8c73ab178` |
| `independent_results.json` | `26374d992d7c8a38e09307f9af039e119dc55c788e14f51d93d80c1c330f75ad` |
| `frontier_partial.md` | `0755e89ae0cecb382b687c56d72d0c23134e3c170744c2de94affc08c9c10afc` |
| `report.md` | `23e14408ff585eb57db79a876c77edafc382f61b9562c5d3748948ed79eee710` |

`SHA256SUMS` is the final inventory.  No file outside this M136 directory was
edited.  No package, commit, push, manuscript change, skill change, or
continuation work occurred.
