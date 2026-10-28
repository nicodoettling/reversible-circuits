# Prelaunch Compatibility Review

Reviewed 2026-10-28, Europe/Berlin. Campaign:
identity-bridge-sampling-20261025. Result: compatible with the installed v0.3.1
after the operational prompt/runbook updates recorded here. State remains
READY, zero attempts, no native session and no running supervisor.

## Release and Configuration

The installed command resolves to
/home/nico/projects/harnesses/codex-research-harness-releases/v0.3.1/bin/codex-campaign.
Read its README, VALIDATION, OPERATOR_ATTENTION, OUTPUT_LIMITS,
CAMPAIGN_MANAGER and TERMINAL_PLATFORM_EVENTS documentation and the updated
operator skill. The October 25 receipt remains a historical v0.2.2 preparation
record; it is not rewritten to claim newer validation.

The v0.3.1 loader and checkpoint verifier accept the existing manifest and
generation-1 scaffold checkpoint. No init, path migration, rearm or configuration
rewrite was needed. Manifest SHA256 before/after review:
53a4bd1692d6f9a4421ed76a0af5dab5b302bbe4e6e441a871938e82edb2836d.

The verified bootstrap remains commit
748f510f009886a09552da631be850b3e0ec1dd0, generation 1, checkpoint-manifest digest
91dd552c9fb7e9fd767eb420e7f9ef6a81881176a5855069ed3e74e96cadbaed.
It remains an immutable recovery point; prepared worktree changes are still
uncommitted for the first coordinator's inspected checkpoint.

Preserved settings: four total agents, gpt-6-astra, ultra, auto-review,
service_tier=default; same-mission transient recovery and verified-quota-refill
resume; six-hour attempts/ten-minute handoff; 128 GiB attempt maximum and
16 GiB bounded-job address space; 3%/1%/fresh >=5% quota thresholds.
The pinned standalone Codex 0.163.0 executable remains available. The installed
v3 runner digests still match both operational helper pins in the manifest.
No deployment capacity or per-worker runtime is inferred from this configuration.

## Required Updates Applied

- The actual campaign MISSION.md and both source/mirror copies now require the
  current six-field NEEDS_ATTENTION.json protocol for operator/platform/refusal/
  auth/permission/infrastructure blocks. The request identifies this campaign,
  a fresh incident UUID, a short nonsecret reason and its saved relative handoff.
  A prose-only exit zero is insufficient.
- Reviewed theorem completion uses COMPLETION.json. An unresolved exhausted
  frontier needing operator input uses attention instead. Programme 1.1 clarifies
  this operational distinction while retaining P0.v1-P5.v1 scientific scopes.
- The coordinator can use its existing auto-review mechanism for an already
  authorized selected Git commit after a sandbox read-only index error. Denied
  or unavailable approval produces permission attention; it does not authorize
  changing permissions or repeated identical execution.
- Detailed results go to unique artifact files; bounded console capture remains
  1 MiB. Exit 123 is a recoverable incomplete experiment only with the exact
  helper output-limit/descendants-cleaned diagnostic. Preserve partial data,
  change the output plan and obtain a new reservation. Child exit 123 alone
  proves neither overflow nor cleanup. Unknown cleanup/125 needs attention.
- The runbook now names v0.3.1 and documents incident-bound operator rearm.
  Reviewed resolution notes and exact-request digests are operator actions;
  the research coordinator never acknowledges its own request.
- Direct content blocks remain operator holds with management disabled. An
  optionally enabled manager could perform diagnostic HOLD only; this review
  grants no replay/rephrasing, model/tool/permission change or platform clearance.

Scientific mission, mathematical claims/guards, existing evidence fingerprints,
agent ceiling and resource/quota authorization are unchanged. The frozen initial
programme appendix remains for provenance; the current operational compatibility
section and maintained programme govern these delivery rules.

## Optional Manager Disposition

The installed Manager.policy API confirms no manager policy is enabled.
The existing coordinator still performs programme-based research selection.
The new between-attempt manager is optional and requires an explicit separate
enable-manager decision; isolated non-refusal platform restart authority is a
second separate choice. Neither was enabled by this compatibility review.
No policy sidecar, retry-budget delegation or new inference schedule was created.

## Verification

- Installed v0.3.1 offline suite: 339 tests PASS in 36.271 seconds, using inert
  subprocesses, temporary Git fixtures and fake backends. Injected-failure
  diagnostics are expected fixture output. No live platform flag was induced.
- Installed Backend.preflight on this unchanged manifest: PASS in host context.
  It checks the pinned runner/CLI, tmux, sandbox/groups, user-systemd/cgroups
  and disabled-MCP configuration without launching a research attempt.
- Existing scaffold checkpoint: verifies under v0.3.1.
- Project map tests, structural/freshness/render checks and source/mirror identity
  are checked in both checkouts after the documentary updates.
- The first actual attempt still has to verify fresh model/effort/tier and
  observed worker metadata, execute a tiny bounded job through its own real
  Codex tool sandbox, and confirm the first coordinator commit's adoption.
  Host preflight and offline tests do not claim those future live paths.

The primary discovery baseline still has 4,023 entries and 920 branches; the
campaign baseline has 4,027 entries and 920 branches. The only research-file
discovery change in this review is the campaign's operational MISSION.md, whose
exact edits were inspected. All mapped proof-source digests remain unchanged.
Programme/runbook/receipt documents are inside the declared self-excluded map
tree. Baseline acknowledgement records this reviewed administrative delta,
rather than changing mathematical acceptance.

## Changed Files and Boundaries

This review updates the primary PROJECT_MAP.md and generated COVERAGE.md date/
navigation, catalogue.json/inventory.json, PROGRAMME.md, PROGRAMME_DECISIONS.md,
and campaign-identity-bridge-sampling-20261025/MISSION.md and README.md, and adds
this COMPATIBILITY.md. The campaign worktree has the corresponding documents,
its generated FRONTIER.md instead of the primary root entry, and the actual
research-campaigns/<id>/MISSION.md used by the harness.

Earlier uncommitted preparation edits are preserved: TARGETS.md,
UPDATE_PROTOCOL.md, manage.py, test_manage.py and integration-2026-10-25.md
under notes/project-map, plus the rest of the prepared files listed above.
See the [October 25 receipt](../integration-2026-10-25.md) for that complete
initial file list. The existing manifest, checkpoints, instructions, source
proofs and installed release code were not edited.

No start, run, rearm, enable-manager, checkpoint adoption, acknowledgement,
account/quota operation, model inference, primary commit or push was performed.
The existing [operator runbook](README.md) remains the launch entry point.
