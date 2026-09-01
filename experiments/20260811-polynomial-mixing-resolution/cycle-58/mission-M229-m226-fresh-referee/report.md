# M229 report: fresh immutable referee of M226

Date: 2026-08-13 UTC.

## 1. Verdict

**ACCEPT**, with one nonmaterial domain qualification.

M226's coefficient identities and reduction to YCM and TCM are correct over
the complete WBE range. YCM, TCM, WBE, and DE remain unresolved.

## 2. Immutable gate

Every M226 frozen artifact passed; its exact checksum-file digest is

    a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a.

M217/M222 also passed before their conditional implication was cited.

## 3. Exact derivation

Independent collection of the one surviving and two fragmentation sources
reproduces `G_k(x)`. The two-seam incidence atoms then give all three B
coefficient cases: below `k`, at `k`, and above `k`. Pairing marked parent
sizes and applying the Borel convolution reproduces the closed A coefficient
including surviving, marked-fragmentation, and untouched contributions.

Finite linearity yields the exact Y prefix. Literal face multiplicities give
the exact signed X-minus-Y two-run prefix without dropping any kind, seam, or
collision.

## 4. Conditional scope

YCM implies Y-WBE. YCM plus TCM and one triangle inequality imply X-WBE.
Together they imply WBE for both observables. Only conditionally on WBE does
the audited M217/M222 normalizer estimate yield DE. None of these open
hypotheses is proved here.

## 5. Exact falsification

Clean-room standard-library checks at `k=3,5` pass. For the `k=5` B witness,
first edge `{3,10}` and parent `(1,2,10,11,12,13,14)`, exactly five
disjoint child-size-one edges produce a two-run face of size at most seven.
This exceeds `4 min(7,1)=4` and independently confirms the refuted shortcut.

## 6. Numbered objections

1. Material objections: none.
2. Nonmaterial qualification: restrict M226 (2.1) to
   `1<=x<=(3k-3)/2`, precisely the arguments used by its seam formulas.
   The overbroad `x>=1` wording can leave kernel domains and omits an
   invisible long surviving coefficient. No stated cutoff coefficient or
   implication changes.

Action: freeze this accepting audit. Keep YCM, TCM, WBE, DE, J2, and all
downstream claims open.

