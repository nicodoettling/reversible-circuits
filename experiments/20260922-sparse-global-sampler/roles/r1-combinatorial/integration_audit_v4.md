# Final current-version integration audit — R1-INT.v4

Completed 2026-09-22T06:16:07.761457+00:00. **Verdict: ACCEPT the final integration at the exact hashes below. INT-L1 is CLOSED. No further required correction was found.**

This is a final consistency and implementation-dependency audit. R1 authored the analytic argument, so its analytic part is not an independent proof review. R1 did not author the root synthesis/wrapper or R3 code. The review is not blind; all agreement remains correlated internal model review rather than external human certification.

## Current reviewed artifacts

- Canonical SG-T1.v1 proof.md: `f788eaecebefd53373c56a7c0c41d104c34897c4a6aba6c775f5f1ce80ec8da2`.
- Root sample.py: `2d74da262e4c53005a05d4f171b85c5469ade520e38b91b1b0df14f4cbe8386e`.
- R3 sampler-v4.py: `cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002`.
- Mathematical R3 proof-v3.md remains `f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868`.
- R4's reviewed restricted-sampler theorem/accounting remains the unchanged v3 mathematical and choice logic. This audit freshly covers the v4 metadata change.

Complete current byte snapshots and hashes are in `integration_audit_v4_inputs/manifest.json`; the earlier complete input snapshots and original objection remain in `integration_audit_inputs/` and `integration_audit_v1.md`.

## Mathematical and resource conclusions

The full findings INT-M1 through INT-C4 in `integration_audit_v1.md` remain accepted. Direct byte comparison confirms that the canonical proof changed only its sampler executable reference from v3 to v4. Thus there is no drift in T0/T1, H0/H1 subsets, the fixed top-level cutoff, source normalization, conditioned marked probability, pair insertion multiplicity, factorial majorant, finite tail, or the explicit eta(N)=exp(-log(N)^2/(10 loglog(N))) above N=2^160.

The new effective per-a threshold in the canonical synthesis is valid: with L=logN>=max(160log2,100a^2), lnL<=sqrt(L) gives L/(10lnL)>=a, hence eta<=N^(-a). Expected O((N+m+2)^20) bit time and O((N+m+2)^10) bit storage safely dominate the actual marked-state memo, length index, deterministic dictionary-scan accounting, exact count arithmetic, primitive costs, subset choices, cutoff powers, and fair-bit rejection. These bounds refer to N and m, not wire count log2N.

H1 has no mathematical dependence on genus-zero/one endpoint formulas or connected decoding, although its implementation reuses elementary choice/unranking utilities from the historical module. The code and R4's primitive-stub checks support that distinction. H0 retains its separately named and reviewed primitive dependency. Empty/odd lengths, N1/N2, m2, near-minimal components, high-genus small support, and nonempty allowed sets are correctly handled. No claim is made for a uniform negligible error above the stated range.

## INT-L1 repair and fresh recheck

The v3 problem was a real notation inconsistency: both policies printed `Unif(A(N,m))`, while canonical A and B denoted different subsets. The repaired output now declares the selected nontrivial component predicate (`v <= cutoff or g in {0,1}` for H0, `v <= cutoff` for H1), defines v, ell and g, admits isolates explicitly, and says the cutoff stays fixed. Separate metadata records the actual cutoff, original top-level cutoff and diagnostic override. A generic `allowed_count` aliases the legacy count field without assigning H1 to canonical A.

Fresh structural checks compare every top-level AST node except the module docstring and main function, and these are identical to v3. Within main, the full argument parsing, sampler preparation, random-source selection and draw prefix are identical; only predicate assignment and printed metadata follow. The root wrapper differs solely by the frozen source filename and expected hash. Thus no mathematical or sampling-choice code changed.

Command:

    timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r1-combinatorial/integration_verify_v4.py

All assertions passed. Raw results are in `integration_v4_results.json`. Actual current root-wrapper output was checked at:

| policy | N,m | cutoff mode | allowed count | purpose |
|---|---|---|---:|---|
| H0 |4,6|original|3936|canonical H0 target|
| H1 |4,6|original|1056|different canonical H1 target|
| H0 |3,6|diagnostic cutoff0|240|large-support genus<=1 retained under override|
| H1 |4,0|diagnostic cutoff0|1|empty word/isolates under override|

Each printed predicate, actual/original cutoff field, candidate label and generic count agrees with the selected policy. The root wrapper successfully executes the exact hash-frozen v4 source. Existing exhaustive actual-forward law and serialization tests remain relevant because their production logic is unchanged; no unnecessary exhaustive rerun was performed.

INT-L1 is therefore closed on these exact bytes. All v3 evidence and objections are retained. Changing these bytes or a mathematical dependency reopens the affected audit conclusions. Final project certification remains the coordinator's responsibility, including its complete claim ledger and R5 current-version review.

All review writes remain within R1's role directory. No goal, delegation, package installation, machine change, external process/session, commit or push occurred.
