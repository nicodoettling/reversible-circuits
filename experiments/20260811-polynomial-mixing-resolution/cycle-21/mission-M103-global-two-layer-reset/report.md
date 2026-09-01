# M103 final report: global two-layer reset defect

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, scope, and convention

```text
VERDICT: REFUTE THE GLOBAL TWO-LAYER SUFFICIENT CONDITION EXACTLY.
FULL WEIGHTED AND UNWEIGHTED RESET RESOLVENTS REMAIN UNRESOLVED.
```

This mission concerns only the full **nonlazy stationary-flow
parking-degree projection** in the minimal long-cycle factorization sector.
It proves no auxiliary gap, ROOT-MEAN LIFT, result for the original lazy
exact same-product `{3,4,5}` heat-bath chain, Terminal A, or Terminal B.

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.

## 2. Exact claim and counterexample

With M90's transformed quantities

```text
g=A+Qg,
U=q(1-q)K/(R+1),
r_U=U-A-QU,
```

the assigned universal statement was

```text
(I+Q)r_U(x)>=0             for every reachable active context x.   (2.1)
```

It is **refuted** at the fresh reachable context

```text
x=(s,K,R,B)=(30,1,0,10).
```

The standalone exact certificate gives

```text
r_U             =-.003687096818561213...,
Qr_U            = .003535610344928366...,
(I+Q)r_U        =-.00015148647363284748...,
(I+Q)r_U / U    =-.006914605163495121... .         (2.2)
```

The complete exact numerator and positive denominator of every quantity in
(2.2) are frozen in `two_layer_exact.json`. Hence this is a rational sign
certificate, not a floating-point inference.

## 3. Algebra, all-rank normalization, and finite descent

Direct expansion gives the exact paired identity

```text
(I+Q)r_U=U-A-QA-Q^2U.                              (3.1)
```

`two_layer_exact.py` imports no predecessor module and reconstructs the
Cayley root law, contextual mean, canonical basin energy, and
negative-hypergeometric attachment law with `fractions.Fraction`. For every
root group it verifies `sum_(j=0)^k nu(j)=1`, then retains every live rank
`j=1,...,k`; `j=0` is killed. No finite recurrence deletes `j<k`.

For every retained deep child,

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,       P=s+K-R,          (3.2)
```

so all local and full resolvent calculations are finite DAG sums. The
witness is fresh `(K,R)=(1,0)`, hence belongs to the accepted reachable
closure without an auxiliary reachability construction.

## 4. Complete-excursion self-attack

The strongest attack is decisive for scope: the new local obstruction does
not survive the complete excursion. The same standalone exact implementation
computes at `(30,1,0,10)`

```text
weighted transformed resolvent / U   =.7372496452184509...,
weighted margin                      =.005756384312696922...>0,
unweighted transformed resolvent / U =.8267268839096050...,
unweighted margin                    =.003796100097007001...>0.  (4.1)
```

The exact fractions are in the raw JSON. These are exact **finite survival
diagnostics only**. They refute neither universal full-resolvent frontier and
do not establish a gap.

## 5. Boundary and asymptotic falsification attempts

The predecessor M98 right-heavy counterfamily is not a two-layer
counterfamily. In the proved `K->infinity` right-heavy limit,

```text
b_infty(s,B)
 =r_infty(s,B)
  +sum_(t>B,t-1>=2)m_(s,t)r_infty(t-1,B).          (5.1)
```

At `(s,B)=(16,4)`, the negative local limit `-4.459e-5` is compensated by
the first layer `0.006473...`. A scaled binary64 scan of (5.1) through
`s=160` found no negative value. Its worst normalized row moved from
`B approximately s/4` at moderate rank to fixed `B=1`, reaching
`.0347319...` at `s=160`. This is empirical falsification only; it is not an
asymptotic sign proof.

In contrast, a targeted exact fresh-context search along
`B approximately s/3` led to the retained negative rank-30 witness. Only
(2.2) is promoted from that search. No first-failure assertion or infinite
fresh counterfamily is claimed.

An initial unoptimized request for `s<=200` was interrupted after its
completed printed prefix through rank 140 and produced no JSON; no result
from that incomplete run is used. The retained optimized raw scan is
`right_heavy_s160.json`.

## 6. Dependencies and status ledger

- **Frozen/accepted inputs:** M50/M56/M65/M69 root-composition, contextual,
  basin-current, and attachment formulas; M71/M76/M79/M82/M87/M90/M96
  transformed recurrence, weighted budget, strict phase, and reachability;
  M98/M99 right-heavy one-layer counterfamily and its audit.
- **Proved here:** identity (3.1), the exact all-rank rational counterexample
  (2.2), and its fresh-context reachability.
- **Refuted here:** the universal global two-layer condition (2.1).
- **Exact finite only:** both complete resolvent survival values (4.1) and
  nearby fresh positive values.
- **Empirical only:** right-heavy `K->infinity` scan through rank 160.
- **Unresolved:** universal weighted and unweighted full reset inequalities,
  marked occupation, ROOT-MEAN LIFT, auxiliary `Pbar` gap, original heat-bath
  gap, and both terminal outcomes.

No new literature theorem is invoked.

## 7. Boundary cases and strongest limitations

- The counterexample uses active rank `s=30` and `1<=B=10<=s`; it does not
  concern the exceptional original-chain regimes `m` odd, `m=0`, `m=2`, or
  `N=2`.
- A failed sufficient inequality is not a slow mode. No stationary-mass cut,
  conductance estimate, congestion lower bound, or spectral-gap upper bound
  is supplied.
- The sign is finite, not yet an infinite rational counterfamily. One exact
  witness is nevertheless sufficient to refute the universal template.
- The scalar `q(1-q)` remains an algebraic budget. No Bernoulli random
  variable or event representation is inferred.

## 8. Artifacts, commands, runtime, and hygiene

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-21/mission-M103-global-two-layer-reset/
```

Principal artifacts are `plan.md`, `checkpoint.md`, `obstruction.md`, this
report, and:

```text
two_layer_exact.py / two_layer_exact.json
right_heavy_asymptotic_probe.py / right_heavy_s160.json
```

Reproduction from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M103-global-two-layer-reset/two_layer_exact.py --with-resolvents --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M103-global-two-layer-reset/two_layer_exact.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M103-global-two-layer-reset/right_heavy_asymptotic_probe.py --s-max 160 --emit-every 40 --output experiments/20260811-polynomial-mixing-resolution/cycle-21/mission-M103-global-two-layer-reset/right_heavy_s160.json
```

The full standalone exact command took about 94 seconds under Python 3.12.3;
the optimized binary64 scan took about 5.5 seconds internally. Both are
deterministic, use `seed=null`, and require no nonstandard dependency.

Source compilation, JSON parsing, manifest verification, whitespace checks,
cache hygiene, and repository status are checked before freeze. No
predecessor, coordinator note, manuscript, project skill, or shared source is
edited.

## 9. Final handoff and next lemma

```text
GLOBAL TWO-LAYER DEFECT: REFUTED EXACTLY.
FULL WEIGHTED/UNWEIGHTED RESET FRONTIERS: UNRESOLVED.
PBAR GAP / ORIGINAL K GAP / TERMINALS: UNRESOLVED.
```

The clean next standalone target is:

> **FULL RESET EXCURSION.** Prove
> ```text
> [(I-Q)^(-1)A](x)<=U(x)
> ```
> for every reachable active context, or prove the stronger universal
> unweighted resolvent bound.

This target permits compensation across every defect depth, which is now
necessary: M98 kills the one-layer sign and M103 kills the global two-layer
pairing.
