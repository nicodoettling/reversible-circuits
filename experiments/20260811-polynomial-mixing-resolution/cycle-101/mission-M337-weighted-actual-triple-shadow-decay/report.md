# M337 final report

Date: 2026-08-14 UTC

## Verdict

```text
STRICT ANALYTIC PROGRESS.
PROVE THE EXACT PIVOT-AVERAGING/TRIPLE-SHADOW IDENTITIES.
PROVE W-RATSD+HLDT => THE QUANTITATIVE TERMINAL WHOLE-NODE CONCLUSION,
CONDITIONALLY ON ITS UNRESOLVED ACTUAL-FAMILY CLAUSES.
ACTUAL d>=6 AHTSS/AHLDT AND HPRN REMAIN UNRESOLVED.
```

## Exact advances

For arbitrary nonnegative weights at an actual residual node,

```text
sum_P lambda_P(W-c(P))=rho W^2,
sum_P lambda_P c(P)=W^2(1-rho).
```

These identities prove that whenever `rho>0`, some active pivot retains at
least `(1-sqrt(rho))W`. This is weight-dependent and assumes neither
polynomial support nor unweighted expansion.

For the whole actual child triple shadow,

```text
Xi_A=sum_(P in A)lambda_P T(P)
    =sum_{Q<R}lambda_Q lambda_R lambda(Sh(Q,R)),
sum_(P in A)lambda_P c(P)^2 rho'_P=2Xi_A.
```

This is the strongest exact active-pivot average available from the accepted
one-/two-/three-signature algebra. `Xi_A` includes regenerated pairs and is
not controlled by parent pair density alone.

## Conditional theorem

The frozen W-RATSD+HLDT statement includes:

- an inverse-polynomial heavy anchored initial whole node;
- relative whole-shadow descent and logarithmic weight payment above a
  density threshold;
- a heavy terminal alternative at every final step;
- heavy whole-child terminality below the threshold.

Conditionally on those clauses, multiplicative density descent takes at most
`ceil(B_low d^B_rel log d)` nonterminal steps. Logarithmic losses telescope,
and the separately quantified final loss gives final weight

```text
||lambda||_1/d^(C_init+C_log+C_fin).
```

The final whole child is edgeless. This conditional implication is proved;
the hypotheses are not.

## First unresolved actual lemmas

1. **AHTSS:** above the threshold, choose one active pivot satisfying both
   whole-child relative density descent and logarithmic weight payment, or a
   heavy terminal alternative.
2. **AHLDT:** below the threshold, a heavy active pivot supplied by the exact
   averaging lemma has `T(P)=0`.

The `d=3` star/triple shows why neither follows from generic pair averaging:
the heavy leaves regenerate a child edge while only the vanishing-weight
center is terminal. This remains boundary evidence and is not promoted to
actual `d>=6`.

## Firewall

No computation or `d=6` census was run. No child was replaced by an induced
graph; no unweighted MIDEC, polynomial-support assumption, conflict
independence, transitivity, or pair-moment shortcut was used. HPRN, PHTC,
WRAD, routing, gap, mixing, Terminal, and all downstream results remain
unresolved and unpromoted.

