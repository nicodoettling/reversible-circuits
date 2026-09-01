# M250 final report: metric pruning and root-seam reduction

Date: 2026-08-14 UTC. Base commit:
'502a6f031c6d5a4bc0064ee5b370a4fa3914f993'.

## Verdict

~~~text
PROMOTE THE PROVED METRIC CANONICAL PRUNING THEOREM AND OPEN
COMMON-NONCHILD ENDPOINT CLAUSE.

PROMOTE THE STRICT REDUCTION OF REPAIRED RSMI+/IDL TO THE EXACT
ROOT-SEAM PATH TRANSDUCER.

DO NOT PROMOTE RSPT, RSMI+, IDL, OR UNCONDITIONAL ALL-RANK Z2.
~~~

## Immutable source gate

All M240, M242, M244, and M247 frozen payloads verify. Their top inventory
digests and the locked DPS PDF digest are recorded in Section 1 of
'metric_pruning_root_seam_reduction.md'. Only accepted M244 Theorem 3.1 is
used. M247's rejection of frozen RSMI is preserved; that RSMI is not a
premise or a renamed conclusion.

## Strongest proved theorem

For any canonical unedited off-path excursion, the DPS side-token rewrite has
the literal residual

~~~text
E_a -> S W^(R_a) S S.
~~~

When a canonical child has 'q=R_c=L_c+1', its two slot rows are exactly

~~~text
W^q     S S S B_a^q     -> S,
W^(q-1) S S S B_a^(q-1) -> S.
~~~

Both record the parent black 'x_a'. All intervening rows have one side. The
proof is a postorder induction using M244's complete colored rewrite nodes
and DPS Lemma 2. It upgrades the accepted colored survivor to an actual
metric interface.

As a consequence, in every open/strictly-decreasing row and every
'v<r<d' with 'p(r)!=v', both slot labels have the absolute common second
endpoint 'x_(p(r))' at ranks 'd' and 'd+1'. Thus the slot is literally
'h_r^2' and is disjoint from '{v-1,d-1,d}'. This discharges the factor-level
content of M247 objection M-3.

## First exact unresolved lemma

RSPT is stated in equations (4.1)--(4.5) of the proof note. Its exposed set is

~~~text
E_v={2v-2} union
    union_{r>v,p(r)=v}{2r-3,2r-2}.
~~~

The transducer has exact open/sealed path transitions, inherited-low-label
endpoint output, and separate sealed/open four-label root tables. It applies
the larger-child root-open rule only in the open state. Arbitrary off-path
metric interiors and the common-nonchild endpoint are no longer premises.

Conditional on RSPT, the proof note exhausts all '2d' factor coordinates:
closed equality, IDL-a, IDL-b, proved IDL-c, IDL-d, and every unnamed
coordinate. This is a strict conditional reduction, not a proof of RSPT or
IDL.

## Tiny falsifier

The recurrence and four adversarial rank-seven rows were written in
'checkpoint.md' before the script was created or run. The rows cover an open
multilevel path with both a larger direct child and a common nonchild, the
open empty-scan boundary, a closed late path with a direct child, and a closed
internal ascent with a direct child.

Both deterministic runs give:

~~~text
rows 4
failures 0
row digest d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59
Python 3.12.3
dependencies {}
seed null
~~~

This is exact finite calibration only and proves no all-rank clause.

## Scope

No fixed-edit boundary shape, every-color route, voltage correction, route
length, comparison congestion, spectral gap, polynomial mixing, or Terminal
conclusion follows. M242 objection N-1 is untouched; no generic double
inverse identity is used.

## Audit request

Freeze M250 and commission a fresh immutable referee. The referee should
especially inspect the actual three-side accounting in the two child rows,
the high-suffix argument in Corollary 3.2, and whether RSPT is genuinely
strict and sufficient without silently reusing rejected RSMI.

