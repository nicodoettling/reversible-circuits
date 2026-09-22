# Self-contained handoff — connected genus-one sampler

Saved 2026-09-07 21:59 UTC, before the external shutdown margin.
Exact native session ID: `01a07db2-4703-7312-ae54-75fcdc0bdc13`.
One native goal was created without a token budget. Its mathematical
objective is achieved; native status is active pending final delivery review.
Completion will be recorded only after the goal tool succeeds. No automatic
restart, cap reset, or continuation is authorized.

## Target and accepted result

This new run superseded the old local mixing objective. T0 requests a
sampler within TV 2^(-b) of uniform on connected ordered transposition
identity words of length 2N on all canonical labels [N], in expected
poly(N,b) bit time. Products act rightmost first; labels and positions are
distinguished. Accepted S1.v2 is stronger: exact uniform sampling, expected
O(N^10 log^3(N+1)) bit time, polynomial space, for every N>=2. N=2 is a
singleton, N=1 infeasible. The resource variable is N, not log N wires.

Read `proof.md`, `coordinator_report.md`, and the accepted final rows of
`claim_ledger.md`. Deleting the last transposition leaves one connected
predecessor or two anchored components whose genera sum to at most one.
Vakil's positive genus-one count formula permits a polynomial DP aggregating
cycle allocations by size, cycle count, and symmetric moments. Unique
reconstruction and actual conditional integer masses prove uniformity.
No exponential subset inventory, mixing result, or prefix-connectivity
completion oracle is assumed.

From repository root:

    python3 -B experiments/20260907-genus-one-sampler/sample.py --n 8
    python3 -B experiments/20260907-genus-one-sampler/sample.py --n 4 --m 8 --target restricted

Core arbitrary-endpoint g0/1 API: `roles/r1-recursive/sampler.py`.
Python labels are zero-based; CLI labels are one-based. Standard-library
Python3.12.3 suffices. The theorem uses independent fair bits; SystemRandom
is the implementation default. Fixed PRNG seeds are diagnostic only.

## Accepted versions and full reviews

Frozen R1-T1.1 proof SHA256:
`c779902224eaab4ebe2837fbb0d4aaaf9850aa4aede5443cd86259a746f6b9ba`.
Frozen core sampler SHA256:
`d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d`.
Complete nonauthor reviews are `roles/r2-structural/recursive_audit.md` and
`roles/r3-referee/candidate_audit.md`. Both accept the mathematics, bit
bound, repaired explicit-stack code and global integration.

The independent blind report `roles/r3-referee/blind_report.md` froze at
2026-09-07T21:26:04.326022Z with SHA256
`e638cecd1c337a8d740be59f09aa7d9b895778616419dbcf85b3c9befde2250c`.
Its isolated initial input and later candidate snapshots are preserved.

Second accepted construction: `roles/r2-structural/proof.md` and
`cut_sampler.py`, fully reviewed in `roles/r1-recursive/structural_audit.md`.
It samples uniform cut incidences through a weighted unicyclic grammar and
accepts with 1/|J(w)|; expected trials are at most 2N-1. It requires only
its checked genus-zero primitive and the elementary M97 cut, not a
previous genus-one decoder.

The original worker proofs/reports deliberately retain their provisional
pre-review annotations and frozen hashes. Canonical ledger entries record
later acceptance. Same-model review is correlated, not external human
certification. Do not rewrite the original reports to erase review history.

## Global consequence and remaining scope

`global_consequence.md` (G1.v1.2) proves exact sampling of A_01, the global
words with every nontrivial component of genus 0 or 1. Weights are
m! product_B C(|B|,ell_B)/ell_B!, with exact labeled components and uniform
position interleaving. Global TV is exactly 1-Z_01/Z. `global_mass.py` uses
the existing positive DYZ count code, checked against an independent
endpoint/support DP. `global_mass_results.json` stores 369 exact certificate
rows, all independently reproduced by the referee with a different total
recurrence. Covered mass at m=2N is 80/81 for N=3, 4375/4672 for N=4,
about .0268221 for N=16, and 3.9064e-6 for N=32.

A separate proof gives log(Z_01/Z)<=-N log N+4N loglog N+O(N), so the
restricted global TV tends to one. This is not a plot inference or a
hardness result. Richer hybrids can include higher-genus primitives;
size-two higher-genus fibers are trivial but outside the literal g<=1
certificate. Approximate component samplers require conditional error
at most epsilon/(2N) each and add at most epsilon/2 to omitted mass.

No first unproved lemma remains for T0 under the checked published count
theorem. Arbitrary higher-genus connected decoding and an all-length global
sampler remain unresolved outside this theorem. Scalar counts or fixed
surplus alone do not resolve those later obligations.

## Evidence and sources

Complete X2/X3/X4 probability laws passed, including all 131040 X4 words.
Forced-assignment masses, arbitrary endpoint counts, actual forward stack
execution and exact assembly laws passed their recorded finite checks.
Root fresh reruns: coordinator_r1_results.json,
coordinator_recursive_forward_results.json, coordinator_structural_parser_results.json.
Full commands/domains/seeds appear in run_manifest.md and complete role
reports. The degree600 mechanical stack fixture uses stub count oracles;
it is not a large-degree sampler benchmark. Seeded draws test validity only.

`regression_registry.md` retains adjacent-square zero fibers, their tree
extensions, cut-decoration bias, ordinary/connected endpoint mismatch,
unweighted support-graph bias, historical handle-lumping and cached-prefix
failures, and the corrected interpreter recursion issue.

Load-bearing checked primary sources:
Vakil, Genus 0 and 1 Hurwitz Numbers, Section1.2, Corollary1.5, Proposition3.2,
https://math.stanford.edu/~vakil/files/g01hurwitz.pdf;
DYZ, Classical Hurwitz numbers and related combinatorics, Proposition1
Eq13 and Section1.2 Eqs19-20,
https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf.
Imported implementation source hashes are in global_mass_results.json.

Inherited inputs: experiments/20260905-bridge-length-phase-diagram/
phase_diagram.md, coordinator_report.md, claim_ledger.md and
roles/r3-intermediate-hybrid/report.md; and
experiments/20260811-polynomial-mixing-resolution/cycle-19/
mission-M97-genus-one-hurwitz-gap/report.md Sections3-7.
Prior agent acceptance was not external certification. The newer September5
scope conflicts chronologically with HANDOFF's older dense-only summary;
no protected document was changed.

## Operations and a later authorized continuation

Immediately reread these exact files on any continuation:
`experiments/20260907-genus-one-sampler/tmux-run.json` and
`notes/genus-one-sampler-run.log.genus-one-sampler-20260907.cap-status.json`.
Activation2026-09-07T21:07:10.321763Z; wrapup2026-09-08T00:37:10.321763Z;
graceful shutdown01:06:05.321763Z; hard deadline01:07:10.321763Z.
These clocks were never reset. This session authorizes no work past the cap.

Contexts /root, /root/r1_recursive, /root/r2_structural, /root/r3_referee
all use gpt-6-astra/ultra. Workers never delegated. Only this experiment was
edited. No commit, push, installation, machine change or additional Codex
process/service/tmux was launched. Initial commit:
20e86f665f69053031fe7eec0c3388458affb1fc. Initial dirty state is recorded in
run_manifest.md. `changed_files.txt` inventories exact research edits;
pre-existing launcher metadata and external cap/log sidecars are excluded.
Preserve user work and unrelated services.

Next at this snapshot: final nonauthor delivery review, completion
bookkeeping and final git status. No new construction is necessary. A later
research extension requires new user authority.
