# M186 Plan — Small-Component Boundary Response

## Objective

Attack exactly M180/M182's unresolved small-component boundary-response
lemma `(SCBR)`, equivalently the bounded boundary-incidence response `(BIR)`,
for the accepted fixed-cell family.

## Target and convention

Permutations compose as `(pq)(x)=p(q(x))`, displayed factors multiply
left-to-right, `n=3k` with odd `k>=3`, and

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform law on minimal length-`n-1` transposition
factorizations of `h`; the operator is M73's nonlazy cyclic rank-two
coordinate kernel. It is not the global fixed-length identity law or the
lazy `{3,4,5}` heat-bath chain.

## Frozen dependency gate

Before substantive derivation, verify the accepted immutable manifests for
M91, M174/M178, M180/M182, and the relevant fixed-cell dependencies they
name. Do not edit any predecessor.

## Exact claim under attack

For M180's already channel-, kind-, and collision-combined signed component
coefficients,

```text
M_(r,k)(d)=1/((n-3)(n-4))
            sum_s a(s)delta_k(s)N_r(d;s),
```

prove

```text
|sum_(d<=n/2)[M_1(d)u_1(d)+M_2(d)u_2(d)]|=O(1/n),
```

or derive a rigorous asymptotic counterterm or strictly narrower coefficient
lemma. Equivalently, one may prove the single-observable `(BIR)` estimate.

## Method

1. Derive an exact critical-Borel/Abel coefficient formula for the combined
   `M_1(d),M_2(d)` from the literal two source channels.
2. Preserve signed channel/kind/collision cancellation until after
   combination.
3. Seek signed summation by parts against the exact `u_r(d)` sequence, or a
   direct two-step boundary-incidence estimate for `W`.
4. If the full bound remains out of reach, isolate the smallest explicit
   coefficient estimate that is equivalent or sufficient and prove a
   nontrivial part of it.
5. Use exact `k=3,5` only to calibrate identities and try to falsify proposed
   universal algebra; infer no sign or asymptotics from those ranks.

## Prohibitions

No absolute-value split by source channel, no finite-sign inference, no broad
shell/quotient computation, no `k=7`, and no FD/FCL1/direct-L1/H0/gap/mixing
or Terminal inference.

## Deliverables

A halfway `checkpoint.md`, compact proof or obstruction, independent exact
checker and machine-readable output when useful, a nine-field `report.md`,
numbered limitations, frozen hashes/manifest, and a fresh-referee request.
