# M312 final report

Date: 2026-08-14 UTC.

## Verdict

```text
OBSTRUCTION-PROGRESS WITH A STRICTER SURVIVING REDUCTION.
ACTUAL d>=6 WRAD REMAINS UNRESOLVED.
FRESH AUDIT REQUIRED.
```

## Proved exact content

1. For every nonzero weight vector, the unrestricted finite-action weighted
   agreement maximum is the outer maximum over positive-weight anchors of
   the normalized stabilizer expression

   ```text
   max_(s in S) sum_Q lambda_Q 1[L_Q;s;R_Q in S].
   ```

   A fixed arbitrary anchor gives only a conditional maximum.
2. At every compatible pivot tuple,

   ```text
   T_I=H_I;s_I,
   T_(I union J)
    ={h;s_I:h in intersection_(Q in J)D_I(Q)}.
   ```

   The one-pivot child signature and the witness/frame covariance laws are
   exact.
3. The predeclared HSCA pointwise-forced-cell lemma would imply WRAD without
   a pair moment.
4. PHTC's polynomial-size conditional-compatibility collapse would imply
   WRAD by the exact higher-arity intersection law.

## First proof obstruction

The natural `Sym/Alt` identity matching has WRAD density one, but every
polynomial-size pivot tuple forces only its pivot points.  Since the matching
degree can be taken as

```text
N_d=d^(d-3)(2d-2)!/d!,
```

the forced weight is superpolynomially too small.  Therefore HSCA is not a
formal consequence of transitivity, uniform point fibers, and framed
transporter-coset geometry.  This is not an actual-M135 realization and does
not refute actual HSCA; it isolates the missing actual-specific fixed-closure
theorem.

## Surviving actual-specific lemma

PHTC retains the positive-weight constraints individually extendable from a
polynomial-size compatible node and asks that an inverse-polynomial-weight
cell have one common residual transporter.  It survives both the abstract
identity matching and M301/M304's actual `d=3` triple, while making no Helly
or pair-moment inference.  Actual `d>=6` PHTC is unresolved.

No `d=6` computation was run after the analytic obstruction.  Finite action
nonemptiness remains separate from polynomial shortest literal braid length.
No MRAD, SSTID, route, voltage, congestion, spectral-gap, mixing, or Terminal
claim follows.

