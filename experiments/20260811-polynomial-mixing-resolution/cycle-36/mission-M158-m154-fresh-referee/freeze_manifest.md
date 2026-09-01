# M158 freeze manifest

Date: 2026-08-13 UTC.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen artifacts

```text
plan.md
checkpoint.md
independent_referee.py
independent_results.json
report.md
freeze_manifest.md
```

`SHA256SUMS` hashes precisely these six payload files and is not self-hashed.

## Exact reproduction

Run from this mission directory with Python `3.12.3`, SymPy `1.12`, and no
network access:

```text
python3 -B -c 'from pathlib import Path; compile(Path("independent_referee.py").read_text(), "independent_referee.py", "exec"); print("compile ok")'
python3 -B independent_referee.py
```

The run is deterministic with `seed=null`. It imports no M154 or predecessor
module or output. Frozen predecessor payloads are read only to verify the eight
assigned SHA-256 values.

## Frozen decision and scope

M158 **ACCEPTS** M154 with zero material numbered objections. The accepted
scope is the universal explicit inner-conjugation braid, literal-versus-inner
Nielsen equivalence, and the exact zero-relative-parity-voltage criterion for
accepted `d>=5` M135/M141 aligned matching subfamilies, including the explicit
transporter word-length caveat. Exact finite reproduction accepts the complete
`d=3` two-orbit framing split, the `d=4` `S_4/V_4` block system and accepted
witness, and only quotient transitivity/primitivity at `d=5`.

No broad `d>=5` transitivity theorem, alternating image, zero-voltage routing,
polynomial transporter or braid length, common M135 braid, spectral gap,
mixing theorem, or terminal outcome is proved. The rank-five checker does not
compute the action-group order or enumerate group elements. No cache directory
is part of the freeze, and no file outside this owned M158 directory was
modified.
