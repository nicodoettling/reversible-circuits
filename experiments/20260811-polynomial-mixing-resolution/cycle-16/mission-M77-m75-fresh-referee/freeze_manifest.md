# M77 freeze manifest

Date: 2026-08-12.

Repository commit recorded by the fresh exact audit:

```text
502a6f031c6d5a4bc0064ee5b370a4fa3914f993
```

Frozen M75 inputs independently verified before the audit:

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  ../mission-M75-partial-macro-coarea/report.md
17bb22b3c041ec1917f206d0a3cf9a8fba2f049fd5a6b61da2eb004699a6b89b  ../mission-M75-partial-macro-coarea/freeze_manifest.md
```

Final SHA-256 values of every M77 artifact other than this manifest:

```text
1186fd961c8c53ad7cbcec1abf30b037e67225c424234048afb5aca8cb69dca0  plan.md
a3c43407dd523ce23240967beba710ce3fbfee690fd99228cc1121f234dd6a9a  checkpoint.md
c30e9bebf14693c618976eba042c5ec6e62fc8c7c5dbe7b67f34585a0808bf1e  independent_audit.py
4bc5af9f368d2c6133823ff1d4344f380e43e7576d686631b7137e2a73feac73  independent-results.json
ad09b58a061e8b65382a3fff316e846ef291b06de761fbad79711cf9b645fd44  report.md
```

Reproduction command from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M77-m75-fresh-referee/independent_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M77-m75-fresh-referee/independent-results.json \
  --m75-report experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M75-partial-macro-coarea/report.md \
  --m75-manifest experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M75-partial-macro-coarea/freeze_manifest.md
```

Environment: Python 3.12.3; seed `null`; nonstandard dependencies `{}`.
All assertions passed.  No predecessor/frozen directory was edited.
