# Prepared Identity-Bridge Campaign

Prepared 2026-10-25, compatibility reviewed 2026-10-28 (Europe/Berlin), not launched.

The [mission](MISSION.md) fixes the research objective and permissions.
The maintained [programme](../PROGRAMME.md) chooses investigations and records
outcome-dependent next actions. [Decisions](../PROGRAMME_DECISIONS.md) and the
[preparation receipt](../integration-2026-10-25.md) record authorization and checks.
The [compatibility review](COMPATIBILITY.md) records the v0.3.1 update.

## Selected Settings

- Harness: installed codex-campaign v0.3.1; tmux-runner v3 backend.
- Model/effort: gpt-6-astra / ultra, default service tier for all threads.
- Team ceiling: four total, one coordinator and three workers.
- Permissions: auto-review, retaining workspace-write sandboxing.
- Recovery: automatic transient retry and verified-quota-refill resume within
  this mission, after a separate operator launch.
- Attempts: six hours each with ten-minute handoff reserve; no overall deadline.
- Memory: 128 GiB per attempt; bounded jobs at most 16 GiB address space.
- Checkpoints: coordinator-owned local commits about every 30 minutes.
- Quota: checkpoint 3%, stop 1%, fresh >=5% to resume; no credit/reset operations.
- Between-attempt manager: disabled. The coordinator retains programme routing;
  enabling a separate manager or platform-restart delegation needs explicit choice.

Runtime directory:

~~~text
/home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/
~~~

It contains campaign.json and the dedicated worktree on branch
campaign/identity-bridge-sampling-20261025. It is excluded from Git and map
discovery. Scientific artifacts belong inside that worktree's research-campaigns,
the named experiments directory and notes/project-map, never runtime metadata.

The main checkout has preparation edits left for your review. The harness
creates an initial scaffold commit on the campaign branch; prepared map and
programme changes are seeded there as uncommitted files. The first live
coordinator must inspect and checkpoint them, verifying actual sandbox Git
access and supervisor adoption before research experiments.

## Operator Commands

Nothing below was launched during preparation. Once you decide to start:

~~~sh
/home/nico/.local/bin/codex-campaign start --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/campaign.json
~~~

This starts the durable supervisor, which uses tmux for execution attempts;
you do not need an additional tmux shell wrapper. Immediately inspect:

~~~sh
/home/nico/.local/bin/codex-campaign status --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/campaign.json
~~~

A fresh runtime verification and actual coordinator/worker activity establish
health; the existence of a service or tmux session is insufficient.

For a durable stop:

~~~sh
/home/nico/.local/bin/codex-campaign stop --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/campaign.json
~~~

The STOP marker is sticky. A later deliberate operator decision is required for
rearm --confirm and another start. Completion also requires operator review;
the coordinator cannot accept its own theorem through the harness.

If the coordinator publishes NEEDS_ATTENTION.json, first review that exact request
and its saved handoff. Rearm then requires its exact SHA256 and a reviewed
artifact-relative resolution note, using --acknowledge-attention and
--resolution-note. Never delete the request or reuse an old acknowledgement for
a new incident. A refusal/content block remains an operator hold; service
restarts do not clear it. See the current installed attention protocol and the
compatibility review for the exact schema and scope.

Do not re-run init on this existing ID, edit active manifests, remove STOP
manually, change pinned releases in place, or start a second supervisor.
Before integrating the campaign branch into main, review its results and set
catalogue.frontier_path back to PROJECT_MAP.md before rendering the main entry.
