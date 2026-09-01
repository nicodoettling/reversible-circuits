# Bounded two-subagent sandbox smoke test

You are the coordinator of a finite infrastructure smoke test. This is NOT a
persistent goal run. Do not invoke `/goal`, create a goal, resume another
session, or continue beyond the completion criteria below.

Work only in:

`/home/nico/projects/research_projects/reversible_circuits/experiments/20260824-bwrap-subagent-smoke`

The repository root is:

`/home/nico/projects/research_projects/reversible_circuits`

## Objective

Spawn exactly two subagents in one parallel wave. Have them independently
verify the exact number of length-four transposition words evaluating to the
identity in `S_3` and `S_4`, while exercising sandboxed command execution and
workspace writes. Then audit their artifacts, write a machine-readable
verdict, and terminate.

Known expected counts, used only as pass criteria, are:

- `S_3, m=4`: `27`
- `S_4, m=4`: `120`

## Hard boundaries

- Spawn exactly two subagents, no more and no replacements.
- Dispatch both before waiting for either one.
- Do not request elevated, unsandboxed, full-access, or network execution.
- Do not install anything or alter machine configuration.
- Do not use Magma, web search, MCP servers, or external services.
- Do not commit, push, or edit files outside this smoke-test directory.
- Do not edit `HANDOFF.md`, `GOAL_SPEC.md`, `AGENTS.md`, the manuscript, the
  project skill, or existing experiments.
- Do not turn finite counts into a research or mixing-time claim.
- Finish promptly after synthesis. Do not invent follow-on work.

## Coordinator workflow

1. Create `workers/worker-a` and `workers/worker-b` if needed. Append a UTC
   `START` line to `progress.log`.
2. Spawn exactly two subagents in one parallel wave, assigning one worker per
   directory. Include all instructions below in each assignment.
3. Append `SUBAGENTS_DISPATCHED` and the two returned agent identifiers to
   `progress.log`.
4. Wait for both workers. Append one completion line for each.
5. Inspect every required worker artifact. Independently parse both JSON result
   files and verify the counts, return codes, and absence of both forbidden
   files.
6. Write `result.json` and `summary.md`, append `SYNTHESIS_DONE`, and return a
   short final message beginning with either `SMOKE_RUN_PASS` or
   `SMOKE_RUN_FAIL`.

## Worker A assignment

Own only `workers/worker-a`.

1. Run sandboxed shell commands to record `id -nG`, `command -v bwrap`,
   `bwrap --version`, and `python3 --version` in `environment.txt`.
2. Demonstrate an allowed workspace write by creating `workspace-write-ok.txt`.
3. Without requesting escalation, attempt:

   `touch /home/nico/.codex-bwrap-smoke-forbidden-a`

   Capture its exit code and stderr in your own directory. Treat a nonzero
   code plus absence of that file as the expected denial.
4. Write a self-contained `direct_enumeration.py` using tuple permutations and
   `itertools.product`. Enumerate all transposition words of length four and
   count those with identity product for `S_3` and `S_4`. State the composition
   convention in the script or report.
5. Run it and write `results.json` containing the two counts, the denial return
   code, `outside_file_exists`, and `method: "direct_enumeration"`.
6. Write `report.md` and return only after all artifacts exist.

## Worker B assignment

Own only `workers/worker-b`.

1. Run sandboxed shell commands to record `id -nG`, `command -v bwrap`,
   `bwrap --version`, and `python3 --version` in `environment.txt`.
2. Demonstrate an allowed workspace write by creating `workspace-write-ok.txt`.
3. Without requesting escalation, attempt:

   `touch /home/nico/.codex-bwrap-smoke-forbidden-b`

   Capture its exit code and stderr in your own directory. Treat a nonzero
   code plus absence of that file as the expected denial.
4. Write a self-contained `permutation_dp.py`. Starting from the identity,
   propagate exact integer counts over permutation states for four steps using
   every transposition, then report the identity count for `S_3` and `S_4`.
   State the composition convention in the script or report. Do not enumerate
   complete words with `itertools.product`.
5. Run it and write `results.json` containing the two counts, the denial return
   code, `outside_file_exists`, and `method: "permutation_state_dp"`.
6. Write `report.md` and return only after all artifacts exist.

## Required coordinator verdict

Write `result.json` with at least:

```json
{
  "status": "PASS or FAIL",
  "subagents_requested": 2,
  "subagents_completed": 0,
  "worker_a": {
    "method": "direct_enumeration",
    "counts": {"S3_m4": 0, "S4_m4": 0},
    "workspace_write": false,
    "outside_write_denied": false
  },
  "worker_b": {
    "method": "permutation_state_dp",
    "counts": {"S3_m4": 0, "S4_m4": 0},
    "workspace_write": false,
    "outside_write_denied": false
  },
  "bwrap_error_seen": false,
  "approval_prompt_seen": false,
  "notes": []
}
```

Set `PASS` only if all pass conditions hold. Otherwise set `FAIL` and name the
first concrete failure. A worker failure is evidence for this smoke test; do
not hide it by doing that worker's assignment yourself or spawning a replacement.
