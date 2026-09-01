# M77 plan: fresh referee audit of frozen M75

Date: 2026-08-12.

## Objective and frozen inputs

Independently referee the frozen M75 report without modifying M75 or any
predecessor directory.  The required frozen hashes are

```text
e699e8b54684488ae34a8df87edea5f9a88002939e34d9facc55c549b741ed39  M75 report.md
17bb22b3c041ec1917f206d0a3cf9a8fba2f049fd5a6b61da2eb004699a6b89b  M75 freeze_manifest.md
```

The target distribution is the global uniform law on
`Omega(N,m)`, while the M75 result is scoped to conditional coarea inside a
two-component exterior Hurwitz macro at `N>=5,m=2N-2`.  The literal kernel is

```text
K=(1/2)I+(1/6) sum_(r=3)^5 (1/(m-r+1)) sum_i H_(i,r).
```

Permutations compose as `(pq)(x)=p(q(x))`, words evaluate as
`t_1...t_m`, and right Hurwitz acts by `(a,b)->(b,bab)`.

## Audit obligations

1. Reprove the randomized first-crossing/coarea load bound, including
   countably supported word laws, expected-length normalization, actual-edge
   source recovery, and the endpoint-only variant when the law has positive
   zero-length mass.
2. Recheck the M60 null-push identity, globally interleaved support-component
   preservation, literal padded-H3 realization, path lengths, and source
   recovery/cell cardinality.
3. Independently exhaust all deletion pairs and all signed radius-one and
   radius-two Hurwitz paths for the displayed ambient `N=6,m=10` witness.
4. Independently enumerate the connected `S_3`, length-six simple-positive-
   braid incidence multigraph, including row counts, column degree,
   stabilizer/parallel multiplicities, and a marked-set noninvariance witness;
   audit the Garside-complement statement algebraically.
5. Recompute `D_N`, the arbitrary H3-fiber bound, `p_H`, and the terminal
   normalization.  Check all displayed constants and exceptional cases.
6. Verify that average, worst-row, two-component, multilevel, auxiliary, and
   full-`K` conclusions remain explicitly separated and that no Terminal or
   polynomial-mixing claim is made.

## Independent exact checks

Create a fresh standard-library-only script in this directory.  It will:

- enumerate triple-transposition fibers for `2<=N<=8`;
- test a rational finite coarea model whose word law includes the empty word;
- execute a nontrivial null-push certificate with another component globally
  interleaved and validate every local product and macro signature;
- exhaust the displayed `N=6,m=10` obstruction through signed radius two;
- enumerate all 240 connected identity words in `S_3` at length six and all
  720 simple positive braids.

All checks are deterministic (`seed=null`) and produce one machine-readable
JSON result.  Finite checks are used only to audit the corresponding finite
claims or algebraic implementation, never as asymptotic evidence.

## Verdict rule

Return `ACCEPT` only if every scoped theorem and normalization is correct up
to explicitly classified nonmaterial corrections.  Return `REJECT` for any
false theorem, missing material hypothesis, invalid source-recovery bound,
incomplete finite obstruction, or scope overclaim.  The final report will
give numbered objections (`none` if accepted), material/nonmaterial
corrections, commands, hashes, and repository status.
