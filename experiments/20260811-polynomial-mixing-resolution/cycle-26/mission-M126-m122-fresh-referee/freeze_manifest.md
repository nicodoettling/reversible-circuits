# M126 freeze manifest

Frozen: 2026-08-13 UTC.

## Mission and verdict

Mission: fresh referee audit of immutable M122
`mission-M122-rooted-product-local-comparison`.

Final verdict: **ACCEPT AS A SCOPED THEOREM/OBSTRUCTION, with zero material
numbered objections.**

M122's infinite DPS star cascade, `d-2` route lower bound, universal
square-prefix full twist, conditional `2L-1` short route, recovery bounds,
and one-root-refresh capacity factor are accepted.  All-edge congestion,
ROOTED PRODUCT LOCAL COMPARISON, every physical spectral gap, and both
terminal outcomes remain unresolved.

## Environment and reproduction

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Python: `3.12.3`.  Dependencies: `{}`.  Seed: `null` (deterministic).

Run from this mission directory:

```text
python3 -B independent_star_referee.py \
  --min-d 3 --max-d 24 --output independent_results.json
python3 -c 'from pathlib import Path; p=Path("independent_star_referee.py"); compile(p.read_text(),str(p),"exec"); print("compile ok")'
python3 -c 'import json,pathlib; q=json.loads(pathlib.Path("independent_results.json").read_text()); assert q["all_finite_checks_pass"]; assert q["parameters"]=={"max_d":24,"min_d":3}; assert all(not r["failures"] for r in q["rows"]); assert not q["exhaustive_small_braid_audit"]["failures"]; assert q["disjoint_last_factor_counterexample"]["short_fails"] and q["disjoint_last_factor_counterexample"]["full_succeeds"]; print("json/assertions ok")'
sha256sum -c SHA256SUMS
```

The checker imports no predecessor experiment code or output.  Its finite
rows are convention checks and counterexample searches; the universal proofs
are audited in `report.md` against M122's frozen proof note.

## Frozen M122 inputs verified

```text
c4c4d305d1800aa8edbde6ca10484928bdfd36f0bf447c33f0a759f780b4401a  report.md
70d5b4ca80bbc1f81adefbb671c17395b0a08dd89bd7bf9318daa0e3b193ed32  star_cascade_obstruction.md
19160f865a8a24b69f511b1108ba32808f2ca097dc83b86b24e3c3b3bdce6605  star_cascade_audit.py
2affa2c0621f5e024977da4950309afe62f18ce83bf7ab2eeaeb42cabe0a22a6  star_cascade_results.json
513c296d933768ecefa5cfe801191be24c4606e97a0d07326901637cc5c9d932  freeze_manifest.md
554370997c6e75604b3f88b5d98abc0b4806ce673784b7994c5531722689afa0  SHA256SUMS
```

Every observed digest matched before the corresponding source was accepted.

## M126 payload hashes

The sibling `SHA256SUMS` freezes these five payload files:

```text
df4393827eb9f298daa6a0d978c5881e403aefdb827633dd2f28f30c4aeb64ce  plan.md
066ad033ce58027416b294c762aa8902c075ec5b7511a9275670d0b4c493b0b1  checkpoint.md
1fb3392cc5a1aca3f002449098e42044741c7ae1e0c1cd62a0e39122128a505c  independent_star_referee.py
c4729f7b2a22bbac13911ba73add34c80ddbf59ff5f1f260fcca24a1998959e1  independent_results.json
70aed254e8f4ac945bf3551d846b89e3010ab2bf41581be2521c21cbd32f1ce2  report.md
```

`freeze_manifest.md` and `SHA256SUMS` are intentionally not self-listed.

## Hygiene

No file outside the owned M126 directory was edited.  Frozen M122 remained
immutable.  No package was installed, no commit or push was made, and no
`__pycache__` directory is present.  Temporary M122 reproduction output was
written only under `/tmp` and is not part of the repository.
