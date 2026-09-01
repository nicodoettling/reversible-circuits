# M95 freeze manifest

Frozen: 2026-08-12 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict and scope

```text
ACCEPT frozen M92 with zero material numbered objections.
```

The acceptance is a reduction/obstruction result only.  The genus-one
connected-Hurwitz gap `gamma_1(d)`, uniform two-component marked hitting,
distributed-root surgery, an unconditional arbitrary-macro cover, full
`H4/H5` behavior, the full lazy `{3,4,5}` heat-bath gap/mixing bound, and
Terminal A/B all remain unresolved.

## Frozen audited inputs

```text
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  M92 report.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  M92 oblivious_cover_reduction.md
e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc  M92 freeze_manifest.md
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  M77 report.md
d8ec2b835e5169b91977a33ac725680d206d62e9d7f6b944abbc203037d22bf4  M05 report.md
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  M68 report.md
285fca42f7f58a9f45ba63cb163f28566ccd5a30e8da1fb01679200500d90ffa  M74 report.md
```

## Owned payload hashes before this manifest

```text
5861f2b239ba7545adf764ee7744feaa2b12893661ff486d409886b424ca1ec7  plan.md
377bdebaad3b8641c8a4b13c2f89dcab7cd68d1a427fc71f33c8405d536a1e6f  checkpoint.md
6aa6552e9bf3f220404ecc73e709b83bba4f3decb405750670aeb6239dfcd9f3  independent_audit.py
b36f7300a7209ca1c37ccb02eb2a1fbd6ba8fe00605d069ff5503e7dd9ad5f09  independent-results.json
feeb86aa8fcd18cf0af9342928adb7c4780beaff25fc453f3416d66794bfe237  report.md
```

The final `SHA256SUMS` duplicates these entries and authenticates this
manifest.  It deliberately does not hash itself.

## Reproduction and hygiene

From the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M95-m92-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M95-m92-fresh-referee/independent-results.json
```

Python `3.12.3`; seed `null`; nonstandard dependencies `{}`.  The checker is
deterministic apart from the recorded elapsed time.  Bytecode generation was
disabled.  The owned directory contains no `__pycache__` or `.pyc` file at
freeze.  No predecessor or shared durable file was edited.
