# Coordinator Synthesis: Two-Worker Sampler Test Run

## Scope

Two workers ran for a bounded test of the project-local `reversible-circuit-sampler` workflow.

- Worker A: exact small-case enumeration and diagnostics harness.
- Worker B: pure Hurwitz baseline and orbit-obstruction demonstration.
- Target distribution under comparison: uniform fixed-length identity transposition words.

## Outputs

- Worker A report: `experiments/20260617-214335-worker-a-exact-harness/report.md`
- Worker A script: `experiments/20260617-214335-worker-a-exact-harness/exact_identity_harness.py`
- Worker A data: `experiments/20260617-214335-worker-a-exact-harness/results.jsonl`
- Worker B report: `experiments/20260617-214335-worker-b-hurwitz-baseline/report.md`
- Worker B script: `experiments/20260617-214335-worker-b-hurwitz-baseline/hurwitz_baseline.py`
- Worker B data: `experiments/20260617-214335-worker-b-hurwitz-baseline/results.jsonl`

## Main Results

Both workers independently reproduced the known exact smoke cases:

| Case | Identity words | Hurwitz components |
| --- | ---: | ---: |
| `S_3, m=4` | 27 | 4 |
| `S_4, m=4` | 120 | 13 |
| `S_4, m=6` | 3936 | 17 |

Worker A produced a reusable exact enumeration harness with diagnostics for prefix cycle types, per-position transposition frequencies, adjacent repeats, support graph invariants, edge multiplicity histograms, and window cycle types.

Worker B produced a pure Hurwitz baseline. Its traces preserved identity and the weighted support invariant, visited only the starting component, and gave explicit lower bounds showing pure Hurwitz cannot be globally uniform over identity words. Best possible pure-Hurwitz TV lower bounds versus global uniform were:

| Case | Largest component / total | TV lower bound |
| --- | ---: | ---: |
| `S_3, m=4` | `24 / 27` | `0.111111` |
| `S_4, m=4` | `24 / 120` | `0.800000` |
| `S_4, m=6` | `2880 / 3936` | `0.268293` |

## Skill Test Assessment

The skill was sufficient to orient independent workers and constrain their outputs. The assigned write directories avoided conflicts, and both workers produced comparable artifacts.

Gap found: the skill had diagnostic guidance, but it did not explicitly define a repeatable sampler-candidate iteration protocol. This was added to `references/experiments.md` after the run.

## Permission Note

The run did not require broad permissions. The environment still requires explicit approval for escalated actions; blanket full permission cannot be granted from inside the agent session. The practical pattern is to use scoped approvals for specific command prefixes and keep worker write scopes isolated.

## Conclusion

This two-worker setup is viable. The next test batch should move from baseline validation to an orbit-breaking sampler candidate, using Worker A's exact harness as the reference.
