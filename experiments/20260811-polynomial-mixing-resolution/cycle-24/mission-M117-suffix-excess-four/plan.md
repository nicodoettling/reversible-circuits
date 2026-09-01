# M117 plan: suffix-excess-four reset frontier

Date: 2026-08-12. Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and scope

Determine whether the accepted auxiliary right-heavy full reset-excursion
contraction extends from suffix excess `L<=3` to `L=4`:

```text
H(s,K,K-1,s-4) <= q(1-q),  s>=5, K>=1.
```

This concerns only the full nonlazy stationary-flow parking-degree projection
in the minimal-long-cycle sector. It is not a gap or mixing claim for the
original lazy `{3,4,5}` heat-bath chain.

## Method

1. Independently enumerate every supported ordered root composition,
   exceptional canonical basin, and retained `(k,t,j)` child.
2. Implement the literal exact `Fraction` recurrence without importing M115.
3. Derive the arbitrary-deficit `L=2` child envelope required by the
   non-right-heavy child at `t=s-1`.
4. Assemble a closed `L=4` reset-plus-descendant envelope.
5. Countersearch exact boundary, high-`K`, and fresh contexts before trying a
   universal sign proof.
6. If the envelope survives, require exact Bernstein or equivalent algebraic
   positivity certificates covering all `s`; finite scans alone do not prove
   the theorem.

## Expected failure modes

- an omitted ordered composition or nested exceptional basin;
- loss of an attachment rank `j` during grouped accounting;
- a wrong child normalization or misuse of the right-heavy `L<=3` theorem for
  a non-right-heavy child;
- an analytic envelope too loose to remain below `q(1-q)` even though the
  exact resolvent does;
- positivity on actual finite ranks but failure on an independent-ratio box;
- a genuine exact full-resolvent counterexample.

## Reproducibility

Use Python 3.12 standard-library exact rational arithmetic, `seed=null`, and
record exact commands, raw JSON, hashes, and every boundary exception.
