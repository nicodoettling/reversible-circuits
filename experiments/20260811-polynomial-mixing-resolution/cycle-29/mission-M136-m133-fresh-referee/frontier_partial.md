# M136 capped frontier recomputation record

Date: 2026-08-13 UTC.

The following deterministic command was run from this directory:

```text
python3 -B independent_referee.py --skip-small \
  --frontier-case 23:7 --frontier-case 24:8 \
  --frontier-case 25:8 --frontier-case 26:9 \
  --output frontier_results.json
```

The checker uses a dynamic root type (maximum current multiplicity, ties to
the smaller atom size), unlike frozen M125's smallest-present convention and
M129's largest-present convention.  Before printing `match=True`, it requires
equality of the full exact mass triple, the cycle-type counts, the exact
log-concavity margin, and both integers in the reduced ratio.

Completed stdout was:

```text
frontier d=23 r=7 ratio=1.00806970271 match=True
frontier d=24 r=8 ratio=1.00625245219 match=True
frontier d=25 r=8 ratio=1.00342080614 match=True
```

At the coordinator's request, the finite-only scan was capped while the
`d=26,r=9` recurrence was still running.  The process was interrupted with
`KeyboardInterrupt` before its final JSON write, so no claim of independent
`d=26` mass recomputation is made.  The frozen `d=26` payload's exact margin,
reduced ratio, positivity, and cycle-type counts are checked separately in
`independent_results.json`; that is an internal-consistency audit, not a mass
recomputation.

This file is a transparent transcription of the completed live stdout, not a
substitute for a machine-generated raw result.  The independently generated
small-case result is `independent_results.json`.
