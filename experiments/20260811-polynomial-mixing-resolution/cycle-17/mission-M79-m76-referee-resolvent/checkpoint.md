# M79 halfway checkpoint

Date: 2026-08-12.

## Referee status

Provisional verdict: **ACCEPT, with no objections to the frozen claims.** The
report and manifest hashes match the assigned frozen hashes. The report keeps
all results inside the auxiliary nonlazy long-cycle parking projection and
labels inverse-split-mass inequality (8.1), polynomial marked occupation,
ROOT-MEAN LIFT, the `Pbar` gap, and every conclusion for the original chain
as unresolved.

Independent exact-rational enumeration through `s=7`, `K<=6` found:

- 162 exact contextual-mean identities;
- 3,750 strict `P=s+K-R` child descents;
- 2,754 canonical reset children, all with `K-R=1`;
- 112 exact seed-kernel formula matches, with exact error zero;
- exact agreement of raw and pure-deep-eliminated inverse-`q` rows with the
  frozen normalization.

The reachability construction is exact: after a reset, the only `R=0` mark is
`(1,0)`; from it a deep step with `k=K'-1,j=R'` reaches every
`K'>R'>=1`. The fixed-power counterfamily algebra also checks: its unary-deep
coefficient is `s^2/(s^2+1)`, its degree-two reset coefficient is `p_s^2`,
and `p_s>=w_(s-1)/(2w_(s+1))->e^-2/2`.

## Decisive new result after refereeing

The proposed inequality (8.1) is **refuted** by an exact reachable seed:

```text
x=(s,K,R,B)=(20,1,0,20).
```

At `B=s`, the contextual observable is one only on the unary root
composition and zero elsewhere. There are no deep children, so `D=0` and
the eliminated and raw reset rows coincide. Exact rational
Cayley-coefficient summation gives

```text
q_x sum_y [(I-D)^(-1)J_can](x,y)/q_y
 = 1.0395701502029937... > 1.
```

The exact numerator minus denominator is positive:

```text
1319315040996006533582695321065228519637911534141383378013775131343321661229366983304182798480404765424423014964179826086315118038022394345522881606506187979374519923727371694831731018692108333627571142876588105484156772290207777121.
```

Rank 19 gives `.9843552830895422`; rank 21 gives
`1.0949193740971426`. The exact artifact is
`terminal_exact_s18_s21.json`. A separately implemented grouped kernel
matches the exact brute-force values through rank 7 and M76's rank-14
eliminated value `.761048371831...`, then independently locates the same
rank-20 violation.

This new counterexample does not create an objection to M76: M76 explicitly
called (8.1) unresolved and warned that its finite margin could reverse. It
does eliminate the advertised constant-one supersolution route. A relaxed
factor or a different potential remains a separate open problem and is not a
proved occupation bound.

## Remaining work

Finish the analytic audit of `(8.1)=>(4.4)`, record the exact `q^{-1}` bound
and nilpotent reset-epoch count, check scaled/unscaled seed normalization in
the final proof narrative, compile the scripts, and freeze a full referee
report with hashes.
