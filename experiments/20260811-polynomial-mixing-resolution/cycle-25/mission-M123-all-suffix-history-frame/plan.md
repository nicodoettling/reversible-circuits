# Mission M123 Plan: All-Suffix Complete-History Frame

## Objective and exact target

Study only the auxiliary right-heavy full-excursion inequality

```text
H := (I-Q)^(-1) A0 <= q(1-q)
```

for every admissible suffix excess `L`, with the definitions and right-heavy
regime inherited from the audited M50--M121 artifacts.  The deliverable is one
standalone universal structural lemma about complete marked histories,
categories, frames, or decision trees, proved or refuted.  This mission does
not claim a spectral gap, mixing time, or terminal project resolution.

Claim labels will be `proved`, `conditional`, `empirical`, `conjectured`,
`refuted`, or `unresolved`.  The target distribution of the surrounding
sampler remains the uniform fixed-length bridge law on `Omega(N,m)` under the
repository's stated kernel; this auxiliary mission itself concerns a finite
substochastic excursion DAG and makes no new sampler claim.

## Audit scope

Read and reconcile only the relevant artifacts from missions M50, M56, M65,
M71, M76, M79, M82, M87, M90, M96, M98, M99, M103, M106, M109, M114, M115,
M116, M117, and M121.  In particular preserve these known negative inputs:

- `Phi` is not assumed to be a literal Bernoulli event;
- direct variance/Bessel budgets are refuted, and outside the right-heavy
  regime `Phi` can exceed `1`;
- every attachment index `j` remains in the history space;
- one-step and two-layer reset-defect sign claims are refuted.

## Proposed route and falsification order

1. Reconstruct exact definitions of `Q`, `A0`, `H`, `q`, suffix excess `L`,
   right-heavy, reset outcomes, attachment labels, and the already-refuted
   candidate inequalities.
2. Lift averaging to fully marked word/scan/outcome histories.  Search first
   for a genuine latent event or subprobability with mass `H`; if impossible,
   search for an exact signed-frame/telescoping identity whose total positive
   reset energy is bounded by the initial Bernoulli variance `q(1-q)`.
3. State one precise universal lemma, including normalization and exceptional
   cases, before trying to prove it.
4. Build an independent exact rational DAG evaluator/enumerator.  Test all
   small admissible instances available from precursor generators, retaining
   every attachment `j`; use exhaustive finite search to falsify the lemma
   before relying on symbolic reasoning.
5. If refuted, extract the smallest exact counterexample and the structural
   reason.  If it survives, give a complete induction/decision-tree proof or
   isolate the first unproved implication without overclaiming.

## Computational standard

Use Python standard-library exact arithmetic (`fractions.Fraction`) with fixed
deterministic enumeration order.  Record the exact command, Python version,
repository commit, source hashes, parameters, and machine-readable JSONL/JSON
output.  Exact finite checks are labeled `exact finite`, never asymptotic.

## Expected failure modes

- a putative latent indicator reproduces only an averaged `Phi`, not the full
  resolvent occupation;
- signed frame terms fail to be nonnegative history-by-history;
- attachment averaging hides a bad `j`;
- a proposed induction is equivalent to a previously refuted local defect
  sign;
- the claimed budget holds only at fixed `L`, not uniformly over suffixes;
- normalization silently uses `Phi <= 1` outside right-heavy instances.

## Planned artifacts

- `checkpoint.md` (halfway state and narrowed lemma)
- `history_frame_search.py` (exact rational audit/search)
- `results.jsonl` and `summary.json` (raw exact output)
- `proof_notes.md` (definitions, lemma, proof/refutation)
- `report.md` (required nine fields and verdict)
- `hashes.sha256` (artifact/source hashes)

