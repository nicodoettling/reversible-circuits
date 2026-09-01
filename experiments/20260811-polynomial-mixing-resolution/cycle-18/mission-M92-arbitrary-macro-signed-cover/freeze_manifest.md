# M92 freeze manifest

Frozen: 2026-08-12 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and dependency status

This freeze contains a scoped two-component minimal-exterior analysis only.
The positive theorem is a worst-row marked-hitting-to-oblivious-cover
transfer.  A second proved reduction shows that an inverse-polynomial gap
only for connected genus-one signed-Hurwitz fibers of length `2d` suffices.
That gap and the marked hitting bound remain unresolved.  Classification H /
connected-support Hurwitz transitivity remains conditional pending its
source and convention audit, and neither positive reduction uses it.  No
unrestricted `H4/H5`, full-`K`, full exterior, or Terminal claim is frozen.

## Frozen predecessor boundary

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M75-partial-macro-coarea/report.md
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M77-m75-fresh-referee/report.md
c55f51c6ff05d7af7e79b3679a707fcf252112dfe6c3e7de4ef6213a501f8b12  experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/report.md
78130a18f581c9d6a2fdcb6ed2c854287fba43dd9128d5dc2405b9771598364e  experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/zero_row_theorem.md
63e7bfe3cfebda7b622ec2620eaf285d27b86da2f48ed1f9638613d8df3e1213  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M85-m84-fresh-referee/report.md
5c09b466fc404ee7145f87125456f23e539fffb1e8c0aeff0264ded32a78a6ff  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/report.md
c147163c711ba06b82b8248d0d86fe4ef6ecd7d8b8ae9c2014944e1bc7e25682  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M86-voltage-signed-bypass/signed_cover_theorem.md
b1de5bff15be9e9fe682ebaa0afe51d1cc5e35b9c35da3b33ce363219e5ac421  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M89-m86-fresh-referee/report.md
96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d  experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M68-intermediate-exterior-layer-action/report.md
285fca42f7f58a9f45ba63cb163f28566ccd5a30e8da1fb01679200500d90ffa  experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M74-m68-fresh-referee/report.md
d8ec2b835e5169b91977a33ac725680d206d62e9d7f6b944abbc203037d22bf4  experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M05-shuttle-comparison/report.md
536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67  experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M13-hurwitz-barbell/diameter_audit.md
```

The M13 dependency is recorded only to identify the conditional adaptive
diameter claim; it is not promoted or used in the positive results.

## Primary owned payload hashes

```text
d66dd58f929199f4ca65f6a5242a2f825cc8b6e38ef9bc6af9e8817cab49429c  plan.md
a7d516ad3ab0b7395b54291189238a4a7851a1014ebb8a89fb30b26170beaad4  checkpoint.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  oblivious_cover_reduction.md
48edcc7ea1e5260b1aaca748ad92bbaef38a6c5739b5a9827689fba1f8fc2711  tree_cotree_metadata_audit.py
2d3aa497741f33eb0c1d88597c4d5e3094f9e348c2b64e449bc1e76d8e57b4e6  tree-cotree-metadata-results.json
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  report.md
```

These are duplicated in `SHA256SUMS`, which additionally authenticates this
manifest.  `SHA256SUMS` deliberately does not hash itself.

## Exact check and hygiene

From the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M92-arbitrary-macro-signed-cover/tree_cotree_metadata_audit.py \
  --collision-n 4 --path-d-max 12 --all-tree-d-max 6 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M92-arbitrary-macro-signed-cover/tree-cotree-metadata-results.json
```

Python `3.12.3`; seed `null`; nonstandard dependencies `{}`.  The traversal
and witnesses are deterministic; elapsed wall time in the JSON is naturally
machine-dependent.  Bytecode generation was disabled.  The owned directory
must contain no `__pycache__` directory or `.pyc` file at handoff.
