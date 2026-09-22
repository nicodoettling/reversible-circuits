# Run manifest

Native coordinator session: 01a0c7a4-3ed2-7372-914a-19f0ed2228c6. One active native goal, no token budget. Commit20e86f665f69053031fe7eec0c3388458affb1fc. Python3.12.3. Standard-library implementation planned. Initial dirty state in initial_git_status.txt; September7 artifacts and notes are pre-existing/external, excluded from attribution. tmux-run.json, tmux-status.json and external cap/log remain launcher-owned.

Requested coordinator and five fresh workers use gpt-6-astra/ultra. Tool reports six total slots. Actual five-worker startup verification pending. Launcher configuration alone is not evidence. Requested overrides are explicit; backend model metadata availability will be recorded honestly.

Clock and frozen task: plan.md and intake_user_prompt.md. Imported source SHA256 values: imported_hashes.json. Commands and exact tested domains recorded next to results; deterministic exact checks use no seed, stochastic validity diagnostics record multiple seeds.

Conflicts: AGENTS/GOAL_SPEC local mixing objective superseded by explicit current user T0. HANDOFF dense-only summary predates September5/7 component results. Prior internal acceptance is evidence requiring load-bearing verification, not external human certification. Protected old documents remain read-only.

Startup verified2026-09-22 05:47 UTC: list_agents reports /root plus running /root/r1_combinatorial, /root/r2_analytic, /root/r3_sampler, /root/r4_diagnostics, /root/r5_referee. Five successful explicit fresh-context spawns; no capacity mismatch. API task identifiers are available; separate UUIDs/backend observed model metadata are not exposed by this tool. Each spawn explicitly requested gpt-6-astra / ultra with fork_turns=none.

## Completed work and reproducible verification

Five role directories preserve complete initial inputs, frozen proofs/code, raw tests, exact review snapshots, reports and role-specific inventories. Final coordinator artifacts are proof.md, coordinator_report.md, resume.md, claim_ledger.md, regression_registry.md, sample.py, changed_files.txt and artifact_manifest.json. The latter excludes launcher-owned tmux-run.json/tmux-status.json and all external/pre-existing notes and September7 files.

Root decisive commands (standard library, Python3.12.3, no seed unless specified):

```
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/check_inequalities.py --m-max 32 --output experiments/20260922-sparse-global-sampler/coordinator_inequality_results.json
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/coordinator_forward_audit.py
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --seed 1729 --draws 1
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 82 --m 14 --certificate-only
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 82 --m 14 --policy H1 --certificate-only
python3 -B experiments/20260922-sparse-global-sampler/finalize_manifest.py
```

The forward audit exhausts actual production discrete-choice paths; it is deterministic, with no PRNG sampling approximation. Source v1 and v3 results/scripts are both preserved. Final v4 changes only CLI metadata; its non-main AST is unchanged, so focused CLI/diff review is the appropriate new check. Individual bounded calls were at most120seconds; no detached job was used. At most two heavy checks ran concurrently; other independent tiny exact checks were subsecond-to-few-second tasks. No unbounded N²m² grid was attempted.

Source preservation checks independently rehash all four named old imports: unchanged. git diff --stat is empty, and neither old import directory contains newly written bytecode. All attributable research outputs lie inside the owned experiment. Native goal-tool token/time usage is recorded at actual completion, not an invented allocation; no token cap was requested.

## Audit lineage

The R1 analytic proof was independently accepted by R2 and by the post-blind R5 audit. R2's separate derivation was accepted by R1. R3 v3 implementation/complexity was accepted by R4 and R5. Root actual forward-law checks execute the same production branches. R1 reviews the canonical integration and final v4 metadata repair, explicitly disclosing authorship of its analytic subsection. Same-model agreement is correlated. R5's fork_turns=none excluded candidate proofs and historical verdicts; inherited repository framing remained and is disclosed in the blind report. Actual backend model identity/effort is not separately exposed beyond the explicitly requested gpt-6-astra/ultra tool settings.

Native goal completed2026-09-22 06:18:04 UTC. Tool-reported tokens1,080,909; native goal time2,044seconds; no token budget. Exact fields: completion_record.json. All five worker threads had completed before the native goal was marked complete.
