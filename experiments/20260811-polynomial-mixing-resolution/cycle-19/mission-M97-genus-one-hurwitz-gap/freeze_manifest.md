# M97 freeze manifest

Frozen: 2026-08-12 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and status

This freeze promotes only the exact tree--unicycle--tree handle-cut
decomposition and its spectrum-preserving cut lift. The inverse-polynomial
genus-one gap and worst-source hitting of the connected-deletable adjacent-
square set remain unresolved. Classification H is not used. No full-`K`,
mixing, or Terminal claim is made.

## Frozen dependency boundary

```text
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  M92 report.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  M92 oblivious_cover_reduction.md
e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc  M92 freeze_manifest.md
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  M68 report.md
285fca42f7f58a9f45ba63cb163f28566ccd5a30e8da1fb01679200500d90ffa  M74 report.md
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  M77 report.md
```

M92/M95 are imported only for the all-`d` unmarked tree family. The positive
decomposition is elementary and independent of those sources.

## Primary owned payload hashes

```text
0eef0d34af6855d1697632af957237b37a6d4af3bada00a1fcafeb876025df79  plan.md
79184ffb8203812bfdbce8ef276acd94aa6eb06054adcf07e7d421608f85c9a9  checkpoint.md
323507b7fc4af7a723812c73e5a284aac533dbf6451a013f4d678f2a8eeef393  handle_time_audit.py
5de0c3915658c28e7cacde2aa01c3022d38a272858358b65f4de29e08af80417  results.json
73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99  report.md
```

These hashes are duplicated in `SHA256SUMS`; that file additionally hashes
this manifest. `SHA256SUMS` deliberately does not hash itself.

## Exact audit and hygiene

The deterministic finite audit used Python `3.12.3`, seed `null`, and no
nonstandard dependency:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
 experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/handle_time_audit.py \
 --d 2 3 4 \
 --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/results.json
```

It enumerated `1,240,131040` states for `d=2,3,4`. Its positive observations
are finite calibrations only; its strong-lump failure is a falsifier.

The final cache search found no `__pycache__` directory or `.pyc` file in the
owned directory. Final `git status --short` showed

```text
?? experiments/20260811-polynomial-mixing-resolution/
?? notes/
```

The repository is a shared multi-agent worktree, so Git collapses all new
experiment content under the common untracked parent. M97 edited only its
owned directory and did not alter `notes/` or another mission directory.
