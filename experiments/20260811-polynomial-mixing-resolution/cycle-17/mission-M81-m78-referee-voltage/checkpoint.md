# M81 checkpoint: M78 accepted; total incidence remains open

Date: 2026-08-12

## Referee decision

**ACCEPT, with zero material objections.**  The acceptance is scoped exactly
as in M78: the canonical positive-elimination formula and the infinite
depth-two obstruction are proved; the total row probability, the canonical
row lemma, the heat-bath spectral gap, and Terminal B remain unresolved.

The frozen M78 report has SHA-256
`c6b0e36ef09608e3fe962e0d85ad572db02b756726a8128548738473855576e1`.
All eight M78 payload hashes are recorded and verified in
`independent-results.json`.  M78 supplied no separate freeze manifest; that is
a provenance defect, not a mathematical objection, because the complete
payload was immutable and independently hashed before audit.

## Decisive independent checks

The self-contained `independent_audit.py` imports no M78 code.  It reproduced:

- the complete `d=3,4` counts `240` and `131040`, with depth histograms
  `{0:240}` and `{0:130992,1:48}`;
- the `d=5` depth counts `[0,14]` and exact total `1569216/10!=227/525`;
- the `K_(4,4)` counts `[0,0,76]`, eight chronological faces, 32 facial
  collision orders, and zero safe facial orders;
- exact identity trajectories and zero signed voltage sums;
- all 36 base four-cycle voltage vectors, with exactly eight zeros and every
  nonzero vector primitive of coordinate magnitude at most one;
- at `L=2,3,4`, respectively `8L^2` lifted four-cycles, `4` collision orders
  per cycle, and zero safe orders.  Extra direct reruns through `L=8` agree.

The all-modulus proof is symbolic.  In chronological notation
`AD,AB,BC,CD`, the only four collision orders are

```text
(AB,BC,AD,CD), (AB,BC,CD,AD),
(BC,AB,AD,CD), (BC,AB,CD,AD).
```

All four induce the same endpoint maps on the five chronological intervals:

```text
CABD, DABC, ADBC, ABDC, ABCD.
```

Thus an unselected edge can meet endpoint `D` only if its original `D,A,B,C,D`
endpoint lies respectively in those five intervals.  Those are precisely the
five forbidden incidence sectors when `AD,AB,BC,CD` bounds a face.  Hence no
residual edge meets `D`; the two preliminary outputs avoid `D`; and the equal
`CD,CD` pair is deleted.  The lifted corner `D` is isolated for every deck
coordinate and every `L>=2`.

## Continuation status

The exact next reduction is to the random elimination process.  At any
preliminary state, the next two outputs can collide iff two current residual
factors have the same transposition value.  For duplicate values `p` at
positions `i<j`, either selection order yields the same deleted word:

```text
outputs
+ residual[:i]
+ p residual[i+1:j] p
+ residual[j+1:].
```

So the missing theorem is an occupation/hazard bound for **safe duplicate
pairs** in reachable residual states, not a bound based only on shortest
support cycles or homology.

The recorded fixed-seed diagnostic found arbitrary long collisions but zero
safe hits in `50000` full orders at `L=2` and `10000` at `L=3`.  It observed
`1684` and `351` collision prefixes, respectively.  Some selected prefixes
already carry nonzero torus homology, and some deletions leave a component of
size two rather than an isolated singleton.  Therefore both “nonzero homology
implies safe” and “every failure isolates one vertex” are refuted.  These are
empirical/finite structural facts, not an asymptotic or zero-row proof.
