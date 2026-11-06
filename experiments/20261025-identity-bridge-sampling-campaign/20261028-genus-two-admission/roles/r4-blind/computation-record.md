# Computation record I1-J5

Claim: independently verify the genus 0/1/2 fixed-permutation count formulas against exact transposition-word enumeration, and the DYZ all-genus majorant on a bounded table.

Coordinator reservation: I1-J5, granted before execution. Base commit supplied by coordinator: `d8893491e04aff74ff3185f7054470ffa24a44a4`.

Parameters: degree 2 through length 6; degree 3 through length 8; degree 4 through length 6. Compare genus 0, 1, 2 wherever the specified length is within the enumeration limit. DYZ table degrees 1 through 8 and genera 0 through 5. Deterministic; seed 0 is metadata only. No nonstandard dependencies.

Pre-run estimate: at most approximately 66,000 word prefixes, 128 MiB, 45 seconds, 10 KiB output. Granted wrapper limits: 45 seconds, 1 GiB. Exact command:

```sh
/usr/bin/python3 -B /home/nico/projects/harnesses/codex-research-harness-releases/v0.3.2/src/research_harness/bounded.py --run-file /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/attempts/000002/run.json --timeout 45 --memory-gib 1 -- /usr/bin/python3 -B experiments/20261025-identity-bridge-sampling-campaign/20261028-genus-two-admission/roles/r4-blind/check_blind.py --output experiments/20261025-identity-bridge-sampling-campaign/20261028-genus-two-admission/roles/r4-blind/check-results.json
```

Observed: wrapper exit 0; 65,835 prefixes; 65 fixed-permutation comparisons; 42 majorant comparisons; all passed. Child elapsed 0.030377971939742565 seconds. Full output is `check-results.json`. Reservation was released immediately by coordinator message. No unknown cleanup, retries, bypasses, or concurrent child jobs.

Limit: this script implements scalar coefficient evaluation, not the complete polynomial-size conditional sampler. The latter is proved explicitly in the blind report and has not been delivered as production sampler code.
