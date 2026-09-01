# M235 freeze manifest

Date: 2026-08-13 UTC.

## Source lock

- Repository commit at initialization:
  502a6f031c6d5a4bc0064ee5b370a4fa3914f993.
- Python: 3.12.3.
- Permutation convention: (pq)(x)=p(q(x)).
- Ambient theorem domain: odd k>=3 and 2<=ell<=(3k-1)/2.
- No network, nonstandard package, randomness, Magma, SAT, or ILP was used.

## Frozen dependency inventory digests

    M192 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
    M195 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a
    M199 1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed
    M207 817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d
    M211 79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225
    M215 59b4bade09ebd0cdaf11265544345ad411d1c482c2353213b3eee8208f938928
    M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
    M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
    M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
    M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688

Every corresponding sha256sum -c SHA256SUMS command passed before proof
work.  No dependency file was edited.

## Reproduction commands

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-60/mission-M235-tcm-two-run-moment/tcm_exact_check.py
    python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-60/mission-M235-tcm-two-run-moment

The first command produces the payload frozen as results.json.

## Frozen files

    plan.md
    checkpoint.md
    tcm_two_run_proof.md
    tcm_exact_check.py
    results.json
    report.md
    manifest.md

SHA256SUMS records these seven files.  After it is written, M235 is immutable
and awaits a fresh independent audit.

## Exclusions

M235 proves only TCM.  It makes no claim of YCM, WBE, DE, conditional J2,
PCR/WPCR, any downstream response, spectral gap, mixing time, or Terminal.

