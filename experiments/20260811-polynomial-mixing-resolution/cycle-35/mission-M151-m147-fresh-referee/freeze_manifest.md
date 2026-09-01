# M151 freeze manifest

Date: 2026-08-13 UTC.

## Verdict and scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NM-1: frozen M147 report Field 4 contains one extra `/q`; frozen proof is correct.
```

The accepted result is the exact `(kappa,D)` all-suffix recurrence, its
reachable deficit-blind pointwise scalar nonclosure witness, and the
unrestricted fixed-moment non-identifiability theorem for the auxiliary
unweighted reset excursion. It proves no auxiliary gap, `ROOT-MEAN LIFT`,
original-chain gap, polynomial mixing, or project terminal.

## Frozen predecessor hashes

```text
e760b6b7620e0278c8a21969112cb5675e268217d64d2319230f9642baecee11  M147 report.md
6084710041b5cb0797fefc05f477bc230bc70d893bb5e8ff2bb3dad9a9004d62  M147 all_suffix_functional_obstruction.md
bcf02d860baf08f6774f858f44ab76c3307632de90d683434e355189fcf763b6  M147 all_suffix_exact.py
441000e76bc60c12093355bda4272ee9fefc9b621c3e4b30b30d17bcb39cb06b  M147 all_suffix_exact.json
8989d0998e819a24dd6b22f50df75a2199b4860fede1dcdd2aacf67625a63cea  M147 freeze_manifest.md
3fddbaf63f38f9ff014ad5f1ee6f537e4ca994c85d8c4511da6f439f91b3c96c  M147 SHA256SUMS
```

All matched before substantive inspection. Rerunning the frozen M147 command
to a temporary file reproduced JSON SHA-256
`441000e76bc60c12093355bda4272ee9fefc9b621c3e4b30b30d17bcb39cb06b`
with zero failures.

## Environment and command

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
dependencies: Python standard library only
seed: null
command: python3 -B fresh_referee.py --output fresh_referee.json
```

The final clean-room run reports zero failures across 3,618 attachment
entries, 6,370 literal root entries, 195 root-mean cases, eight grouped
recurrences, 8,129 `L=1` states, and 13 parity-moment pairs.

## Owned artifact hashes before manifest

```text
85db2d8a14dce97576a36271f584a497ae76a9451636d0bc0812be68d9094bd4  plan.md
9029d578fcfe95fbac96b5445f9f1f85c682752cac946073995e7dada4e787e7  checkpoint.md
c90ae3e0d6870c429f91b34f711b0be508cec4ed36175c190bca3e4c476d8758  proof_audit.md
27b11e9cae6e3d069649f2dbfe6d528a78128d617eca7b8eff0af79e61f0f6ab  fresh_referee.py
d9b572cb4cf6fee5ab63bbe8f3da07529983a73e83b75d28424a7ad5657761db  fresh_referee.json
f98bd88222ad137d5402ab7dac730f02e04e12fc8372cf832ade85a759441b8c  report.md
```

## Hygiene

Only the assigned M151 directory was edited. No predecessor or coordinator
artifact was modified. No package was installed, no network was used, and no
Python cache is retained.

