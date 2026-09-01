# M326 immutable dependency audit

Date: 2026-08-14 UTC

## Frozen M323 package

```text
0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c  SHA256SUMS
```

This equals the assigned top.  The inventory contains exactly fifteen rows:

```text
analytic_obstruction.md
audit_request.md
checkpoint.md
final_checkpoint.md
freeze_manifest.md
guard_plan.md
guard_report.md
halfway_checkpoint.md
plan.md
report.md
run_manifest.md
slpf_k7_h2_guard.py
slpf_k7_h2_results.json
source_lock.md
token_and_candidate.md
```

All fifteen rows pass `sha256sum -c SHA256SUMS`.

## Direct frontier packages

| mission | rows | independently observed top | result |
|---|---:|---|---|
| M305 | 11 | `4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46` | all pass |
| M310 | 8 | `310e5708d48b5ad63d6ad4928be02c98de343d9e0cd91e363fe48eade047f276` | all pass |
| M313 | 14 | `9b67c63e98361bd31e03919295c673d55235a6f7395730b477ca04a5e267f0b1` | all pass |
| M316 | 10 | `1b6caa11e6bb7409e7420d75cd2131f5753707b80736bed1bd9b5fe3f4dbc149` | all pass |
| M319 | 11 | `10f3435003684d4a32570028c314882bbfa28daf0ddc4b8a12d6ba02319ea009` | all pass |
| M321 | 8 | `50d153ff89699d893bd44df6fdc346eec66fd001f843c28ff4d84a19cdfcb960` | all pass |

These contain `62` payload rows.

## Raw-profile dependency chain

| mission | rows | independently observed top | result |
|---|---:|---|---|
| M91 | 13 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | all pass |
| M261 | 9 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` | all pass |
| M264 | 6 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` | all pass |
| M267 | 8 | `001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6` | all pass |
| M270 | 9 | `6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e` | all pass |
| M276 | 9 | `882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db` | all pass |
| M279 | 8 | `3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66` | all pass |
| M282 | 9 | `cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7` | all pass |
| M286 | 8 | `3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a` | all pass |
| M289 | 9 | `327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680` | all pass |
| M290 | 10 | `85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687` | all pass |
| M292 | 9 | `8fefffab69cca864c9260429e9eef34671aab23a497e36fb05cb6b89c378740f` | all pass |
| M293 | 10 | `b7020fb3ee6cfc9b2536b500928320ff4ce0bc8fc0983c65989ff092d9ac3f1f` | all pass |
| M297 | 12 | `a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792` | all pass |
| M302 | 7 | `1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27` | all pass |

These contain `136` payload rows.  Thus the independently checked total is
`62+136=198`.  M297's gated primitive script row is exactly
`9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`.

No stale temporary artifact was used.
