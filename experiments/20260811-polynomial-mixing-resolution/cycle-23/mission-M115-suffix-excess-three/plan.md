# M115 plan: suffix excess three

## Objective and scope

Extend the frozen, independently accepted M109 full-reset-excursion argument
from suffix excess `L=s-B<=2` to the first unresolved boundary `L=3`.  The
object is the auxiliary full nonlazy stationary-flow parking-degree projection
in the minimal-long-cycle sector, not the original lazy `{3,4,5}` heat-bath
chain.  The project target remains uniform on fixed-length identity words.

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are displayed
left-to-right.

## Exact target

For every active right-heavy context

```text
x=(s,K,K-1,s-3),  s>=4, K>=1,
```

test and, if possible, prove the complete all-depth inequality

```text
H(x)=(I-Q)^(-1)A_0(x) <= q_x(1-q_x).
```

Every attachment rank `j=1,...,k` must be retained.  The accepted `L<=2`
theorem may be used only at right-heavy descendants in its stated scope;
non-right-heavy descendants require their own exact bound.

## Method

1. Derive the eight supported root compositions, their exact stationary
   masses and contextual means, the seven exceptional canonical basins, and
   the four live `(k,t)` groups.
2. Derive a closed reset-energy envelope by exact exceptional currents plus
   the accepted canonical-basin estimate on all ordinary basins.
3. Derive and aggregate the new non-right-heavy `L=1` descendant bound; use
   the accepted `L=0,1,2` theorems for the remaining children.
4. Construct a standalone `Fraction` checker for every formula, all retained
   ranks, and bounded discovery.  Finite data will validate or falsify the
   envelope but will not establish a universal sign.
5. Either prove the scalar envelope uniformly, give an exact reachable
   counterexample, or isolate the narrowest remaining scalar inequality.

## Prohibited inferences

- Do not use the refuted one-step or two-layer defect signs.
- Do not infer the all-`L` excursion inequality from `L=3`.
- Do not claim an auxiliary gap, ROOT-MEAN LIFT, original-chain gap,
  polynomial mixing, Terminal A, or Terminal B.

## Deliverables

`checkpoint.md`, `suffix_excess_three.md`, `l3_exact.py`, `l3_exact.json`, a
nine-field `report.md`, and `SHA256SUMS`, all confined to this directory.
