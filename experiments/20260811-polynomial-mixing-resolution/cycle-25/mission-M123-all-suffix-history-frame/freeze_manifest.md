# M123 freeze manifest

Freeze date: 2026-08-13 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen claim

The natural canonical-basin analysis frame is not bounded by the identity.
The first exact failure is local rank `s=5`; the four-coordinate Rayleigh
quotient is `421891/418853>1`.  Measure-preserving full-space constant
pullback preserves this Gram obstruction.  This refutes only the generic
category/Bessel proof route.  The all-suffix contraction, a differently
success-weighted history operator, every gap, ROOT-MEAN LIFT, and both project
terminals remain open.

## Durable commands

Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/history_frame_search.py \
  --s-max 10 --multitype-s-max 8 \
  --results experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/results.jsonl \
  --summary experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/summary.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/micro_history_collision.py

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/hidden_frame_spectrum.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M123-all-suffix-history-frame/hidden_frame_spectrum.json
```

Python was `3.12.3`; all mathematical computations use standard-library
`fractions.Fraction`, have no nonstandard dependency, and use `seed=null`.

## Reconciliation of the interrupted artifact

The preserved `hidden_frame_spectrum.py` attempted factorial-time full
characteristic-polynomial expansion.  Its interrupted `s=5` run produced no
output file.  It was replaced by exact Gaussian principal determinants and a
rational Rayleigh witness.  The replacement finishes in about three seconds
and asserts every displayed fraction.  No claim relies on the aborted run or
on a floating eigenvalue.

## Verification record

- The durable all-attachment recurrence rerun completed with zero
  complete-history, signed-frame, right-heavy-target, or multitype failures.
- A fresh rerun under `/tmp/m123-verify.NfYp2M` produced byte-identical
  `results.jsonl`; its mathematical `summary.json["result"]` payload equaled
  the durable payload exactly.  Metadata command paths and elapsed time were
  deliberately excluded from that comparison.
- The fresh frame-certificate JSON was byte-identical to the durable JSON.
- The literal collision rerun reproduced two favourable marks and durable
  JSON SHA-256 `79a2bda224d680b2a617ac3511d8a60f3a8d5e75447f2f162e7e97340b1f15b8`.
- All three Python files passed `python3 -m compileall -q`; the generated
  owned `__pycache__` was removed afterward.
- All three JSON files parsed successfully.
- Final whitespace and checksum verification are recorded by the successful
  `git diff --check`/owned whitespace audit and `sha256sum -c SHA256SUMS`
  performed after this manifest was created.

## Pre-manifest artifact hashes

```text
0f9e02b477ea5acbff92e18174176ddf9458fbecd1a3bbdcaa5530687613257c  plan.md
e51ca38d2e6b3a09cbec34129833c71b48a903df54e88c584d496db2bfcc07f0  checkpoint.md
bbbff2b52a8e639ab5d09b60c4782e693f614150d36e6c07a18346f1e2a79836  history_frame_search.py
cf4f4ff792e71a83ecf0976ebe400c90c05b1c6f1f525af1fe179414a0b7b58a  results.jsonl
f4fa2b7952e700b4abd679b1aab5b1261ff0fb48e0377b6045f6ad04cb62c39a  summary.json
c85974e8b739eca52f5e2519d540554fa6bc760426be943dea0562eea810156e  micro_history_collision.py
79a2bda224d680b2a617ac3511d8a60f3a8d5e75447f2f162e7e97340b1f15b8  micro_collision.json
f8aa025594bbe695c04ad6888b03e93c8e2d10877e20a7760b6c366d80413fdd  hidden_frame_spectrum.py
5a0247db16a0af0f0d68dbf357415f4da216fdfb5dbde7a9caf42261bf8f153b  hidden_frame_spectrum.json
b214d4efaf27bb706b85d162a07fa2179679feb8d80da79443b8660a7e36e754  proof_notes.md
05a65a8f6111029a93a1c06e1dc014579ae013ff3d0ccaa356050189437afb9c  report.md
```

`SHA256SUMS` is the authoritative final checksum list and additionally
includes this manifest.  The checksum file does not hash itself.
