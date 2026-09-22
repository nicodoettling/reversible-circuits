# R2 final nonauthor synthesis and delivery audit — version 1

**Verdict: ACCEPT canonical S1.v2, G1.v1.2, their unchanged implementation, and the corrected synthesis content. No mathematical T0 obligation remains under the checked published count theorem and stated fair-bit input model.** The coordinator must finish the already planned inventory/status regeneration after these new review files are frozen. This administrative action does not reopen any mathematical claim.

The complete assignment is `synthesis_review_input.md`. The twelve reviewed delivery inputs are preserved byte-for-byte in `synthesis-review-input/`; `synthesis_input_manifest.json` gives their hashes and intake inventory checks. This report follows my completed, frozen independent C1 construction and my completed, frozen nonauthor R1/global audit. I read the complete R3 candidate and global audits and complete R1 structural audit only in this synthesis phase, after my R1 review had finished. Same-model agreement is correlated and is not external human certification or independent statistical evidence.

## Exact-version and drift checks

The entire mathematical body of canonical `proof.md`, from “Frozen objects and theorem” through R1-C6, is byte-identical to the frozen R1-T1.1 proof I accepted. `synthesis_proof_md.diff` records every change. The additions specify accepted status, canonical labels, ideal independent fair bits, zero-based Python versus one-based CLI labels, the explicit implementation stack, current review dependencies, and the separate global target. The changed final paragraphs replace a pending-review annotation with the actual accepted reviews. None changes a formula, allocation rule, reconstruction multiplicity, target or bit exponent.

The complete executable `sample.py` differs from R3's reviewed snapshot only by replacing “provisional” with “audited” in its opening module docstring. Its AST after removing that docstring is identical. The original core sampler hash remains `d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d`. The core R1 proof/code/audit/results/report, my complete C1 payload, and my prior recursive-review payload all retain the frozen hashes. Seventeen such payload files were checked; the separate R3 blind report hash also remains unchanged.

The full global diff against R3's preserved G1.v1 is `synthesis_global_consequence_md.diff`. Its only mathematical wording changes are the two clarifications R3 requested: treat N=0 separately in the operand bound, and distinguish a singleton word fiber on two vertices from a singleton vertex component. G1.v1.2 otherwise updates accepted status and explicitly discharges the primitive gate. R3's complete later candidate audit accepts the actual primitive and `unrank_subset`, including the same integrated sampler. My prior audit already accepted that integration. Thus the earlier conditional G1-SAMPLE statement now has its premise supplied; calling it accepted does not assume an unproved decoder.

## Claim and dependency reconciliation

| Claim | Delivery finding |
|---|---|
| S1 / T0 | Accepted exact Unif(X_N), every N>=2 and b>=1, zero TV error, expected O(N^10 log^3(N+1)) bit time and polynomial space in degree N. N=2 is the one-word case; N=1 is empty. |
| Arbitrary endpoint extension | Accepted connected genus zero/one at length N+c(sigma)-2+2g, with canonical permutation arrays, rightmost-first products, and the singleton genus-zero empty base. |
| Count normalization | Checked Vakil Section 1.2 and Corollary 1.5 remain explicit. The fixed endpoint count is c=G product(alpha_i); no cycle-equality, conjugacy, label, cyclic-shift or position quotient is newly introduced. The positive formula can be derived algebraically, so no new graph-encoding theorem is needed. |
| Allocation and word law | Nonnegative E/S/Q moments, all actually forced cycle choices, zero branches, anchored components and unique final-edge reconstruction are unchanged. R2's full forward law tests and R3's different moment/tape tests concern the same current code. |
| Complexity and executable stack | The O(N^7) operation and O(N log(N+1)) operand bounds, common denominator 24(N!)^5, bounded integer rejection and explicit continuation implementation were both audited. Canonical text does not claim polynomial cost in log N or exactness of a finite PRNG. |
| Independent C1 route | R1's complete structural audit accepts the positive unicycle grammar, actual parser, labeling multiplicities, nonempty cut J(w), reciprocal 1/|J(w)| forgetting correction and expected polynomial rejection cost. It does not rely on the accepted genus-one R1 decoder. |
| G1-COUNT / assembly | Checked DYZ Proposition 1 equation (13), Section 1.2 equations (19)–(20), label/position normalization and least-label component selection remain explicit. The exact word-level weight is m! product C(v,ell)/ell!. |
| G1-SAMPLE | Accepted exact Unif(A_01), where every nontrivial component has genus <=1. Its global TV is exactly 1-Z_01/Z when the restricted fiber is nonempty. The error from approximate primitives is separately conditional on per-history error bounds. |
| G1-SAT / G1-OMIT | At m=2N, 2N=2s-2k+2G with G<=k and s<=N forces no isolates and genus one in every component. The distinct factorial/composition and subgroup-return proof gives covered mass tending to zero. No hardness or all-global-sampler inference is made. |

The latest accepted ledger rows explicitly supersede earlier provisional rows. The unchanged original role reports and raw count metadata can still say “provisional” or “conditional on accepted connected primitives”; these are preserved historical/dependency annotations, not current unresolved obligations. In particular `global_mass_results.json` retains the latter condition while S1.v2 now supplies it. The canonical proof, final ledger, coordinator review and handoff consistently identify that closure.

The complete R3 audit confirms the only needed randomness premise is fresh fair bits. Its deep stack test replaces counting oracles with fixture oracles, as the canonical report and resume now explicitly state. It establishes stack mechanics only. R1's structural audit likewise records a reversed child-list order in the production parser relative to its algebraic convention; it supplies the weight-preserving bijection and exact parser tests. No proposed correction or remaining lemma is hidden by agreement among workers.

## Test-domain and reproducibility checks

`synthesis_checks.py` performs deterministic comparisons of the saved artifacts, not new sampler experiments. The three complete coordinator rerun result objects equal their frozen role originals after removing only command, git-status and timing metadata. This compares every saved mathematical field, not only a digest or top-level pass flag. All 369 global certificate rows also equal the copy on which R3's global review was based.

The reported domains and totals agree with raw output: R1's 112698 forced queries and 1745 endpoint comparisons; R2's 97232 raw moment entries and 5068 full forward words; R3's 7754 full moment tables, 11631 forced masses, 3192 count formulas and 1488 actual-function replays. The degree-600/1200-step fixture is accurately labeled as using stub count oracles. Global checks distinguish 91 coordinator count cells from 48 R3 endpoint/support cells, 369 rational rows and 2016 subgroup inequalities. The integrated seeded checks are 15 connected draws, 51 restricted draws and seven rejected inputs; they claim validity only. The complete X4 law is over 131040 connected words, whereas the saturated restricted global numerator is 131250 because it includes the 210 two-component words.

Two minor delivery errors were found, reported to the coordinator and corrected before acceptance:

1. `run_manifest.md` originally said each worker used `assignment.md`. R1/R2 do; R3 instead preserves `operational-assignment.txt`, `blind-brief.md`, `global-audit-assignment.txt` and `candidate-audit-assignment.txt`. The current manifest names the actual files, whose existence I checked.
2. `coordinator_report.md` and `regression_registry.md` described “all 58 numerical codes through N5.” Raw parser counts are 1,4,15,58 at N=2,3,4,5, respectively. Both files now say 58 at N5, 78 across N2..5. The 1420 labeled macros at N5 and 4431 partial coefficient checks were already correct.

The saved twelve-input snapshot contains these three corrected files. Its artifact manifest was generated before those corrections; its only three hash/size mismatches are exactly those files. All other recorded entries match. `changed_files.txt` exactly equals the manifest's research paths plus the manifest itself, and there were no unlisted preexisting research artifacts. New files produced by this review were explicitly excluded from that intake comparison. The coordinator's promised final regeneration must include them, the corrected hashes and final status documents; no assertion here treats the old inventory as already final.

Forty-three inventoried Python/JSON artifacts pass syntax parsing without importing or running sampler code. No `__pycache__` directory or tracked git diff exists. Commit remains `20e86f665f69053031fe7eec0c3388458affb1fc`. Python is 3.12.3; dependencies are the standard library. The exact command was:

```text
timeout 30s python3 -B experiments/20260907-genus-one-sampler/roles/r2-structural/synthesis_checks.py
```

It passed in well under one second. Raw results, provenance, command, no-seed declaration and current git status are in `synthesis_checks.json`. This phase used no additional stochastic trial, enumeration, construction, shared edit, process/session configuration, delegation or goal operation.

## Negative findings and remaining scope

The canonical registry retains the adjacent-square zero-fiber witness (ab)^3 and its tree extensions, mark-forgetting bias, unconstrained-versus-connected endpoint counts, uniform support-graph bias, fixed-genus subset-inventory failure, historical handle-lumping failure, CP-1's invalid marginal probability product, and the repaired Python recursion issue. Both accepted routes provide a true conditional word law rather than reviving any refuted argument. Counts alone, prior agent approval and finite histograms remain insufficient and are not used as a missing sampler step.

**First unproved T0 step: none identified.** The published fixed-endpoint count theorem remains a named checked dependency; no conjectural mathematical input remains. General higher-genus decoding, a prescribed exposed-prefix connectivity oracle, all-length global generation, local-chain polynomial mixing and polynomial cost in wire count log N are outside the achieved theorem. The statement that the genus<=1-only global law has TV tending to one is a limitation of that named support restriction, not a general sampling impossibility.

This acceptance covers the twelve preserved input versions and the immutable core dependencies identified above. Final administrative inventory/status changes may record this acceptance and the actual goal outcome. Any later change to the mathematical body, counting formulas, allocation rules, decoder or randomness primitive requires the corresponding downstream audit again.

## Frozen delivery input hashes

| file | SHA-256 |
|---|---|
| proof.md | 0da7b35f84f236070ead636b4c20044c8cbdc0849701f4fe0678e3bab6c1b6dc |
| global_consequence.md | d4c6a37f8f2d89b8d965d1a70579e1e97960c606bf92e61eec6aae4686519152 |
| coordinator_report.md | 2e21eee0edea751fcf670b6ce767ca33618269d570a6852ff11b5f7db3bad428 |
| coordinator_review.md | 2763886ffe4354e8dad9016467699efb578408f5b99cd48be6c4381ca7232f31 |
| claim_ledger.md | a41964f7d64c6aee87d8609dea55499371561f162c092648633049a9a14151ed |
| regression_registry.md | c5e5bc6d2f323e9a77b130ccd4f04defacf1a90794bc11cf3fbac791242fb2ad |
| run_manifest.md | ca8c9ae4c0fd1f52f5ede319e5127bc8fc0b8a0353736110e338938d9abeaaae |
| checkpoint.md | ec5c5954daa62299b5417718ce6834c007182c69b256a5168150ed52c0ed806d |
| resume.md | 08977f5ecad0f74f7f6042a0363c0704f4e90f69bcd3cccb1eb5362f312c5105 |
| sample.py | cb4524c973c40a4a79ec38769102ce1afd9d4d711ba5a92760fee90fb70990a8 |
| changed_files.txt | 83097433ac95c41166e2b6b228695b027b5b5faa7b223d1e768126974b667bf7 |
| artifact_manifest.json | e3c9c497b2393730d453b5fdcf1857e0108b5ec623fdf44a468183c2a67949b9 |
