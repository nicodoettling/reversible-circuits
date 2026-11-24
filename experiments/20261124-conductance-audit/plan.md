# Conductance draft audit

Date: 2026-11-24 (Europe/Berlin). Starting commit:
`7c2a54f833158bdb4fe4b4fec6f8de8c743f60a2`.

The user requested verification of `Transposition_walk_conductance.pdf` and
integration of valid results into the main manuscript. `source.pdf` preserves
the supplied draft. The linked private ChatGPT conversation could not be
retrieved; it supplies no additional evidence or instructions.

Target: global uniform fixed-length identity transposition words. Products
act rightmost first. The draft's kernel is half-lazy adjacent pair heat bath,
with a uniform index in 1,...,m-1 and exact uniform same-product replacement.
The project kernel is the half-lazy uniform mixture of feasible block sizes
3,4,5, then uniform nonwrapping window and exact conditional replacement.

Tested claims: the connected-map count, component switching, balanced-cut
argument and bounded-slot extension; long-length profile conductance; the
all-endpoint connectivity and exponential-in-N cut bound. The named project
obligation is the adversarial route in GOAL_SPEC: does a universal polynomial
bound fail for the exact project chain?

Method: full mathematical audit with expanded proofs; deterministic exhaustive
checks of small endpoint fibers, component/genus identities and boundary
flows, plus exact component-assembly checks of the switching inequality.
No stochastic inference: seed 0 is recorded but unused. Python standard
library only. No production sampler is changed.

Boundary cases include odd m, m=0, m=2, N=2, minimal connected words,
S3,m=4, S4,m=4 and S4,m=6. Finite checks can refute steps, but cannot prove
the asymptotic theorem or exhibit its unspecified sufficiently-large onset.
Failure modes: wrong map encoding exponent, nonuniform switching counts,
uncontrolled cap jumps, confusing pair updates with project updates, missing
parity, or confusing profile expansion with full-chain mixing.

Reproduce from repository root:

```sh
python3 -B experiments/20261124-conductance-audit/check.py > experiments/20261124-conductance-audit/results.jsonl
cd papers/transposition_identity_samplers
TEXMFVAR=/tmp/conductance-tex-cache latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/conductance-paper-build main.tex
```

The TeX build uses a temporary font cache and output directory. The report
records final checks.
