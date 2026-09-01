# Mission M273 plan: decorated root-seam transition

## Objective

Prove or strictly reduce the decorated-lens root-seam transition (`DL-RST`) at
the root step `a=1`, using the literal states frozen by M269/M271 and the exact
CP-6 root contexts frozen upstream.

## Claim target and status

Target claim: **unresolved** pending source locking and derivation.  For
`alpha=m-1`, `beta=m`, `gamma=m+1`, `delta=m+2`, derive the complete old/new
root endpoint tables for both the sealed and open cases, including persistent
child ports, cyclic post-wrap order, and the new child `d` with `R_d=beta`.

No claim about IDL, RSPT, routing length, congestion, spectral gap, mixing, or
a terminal resolution is in scope unless the exact local lemma closes and is
then accepted by a fresh independent audit.

## Required immutable inputs

- M240/M242, M244/M247, M250/M254, M257/M260, M262/M265, M269/M271.
- The locked DPS source identified by those missions.
- `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, and
  `references/sampling-problem.md`.

All cited artifact hashes will be recorded before the derivation.  A hash
mismatch stops the theorem route and is reported rather than reconciled.

## Method

1. Reconstruct the exact CP-6/root row contexts and conventions from frozen
   artifacts.
2. Expand the literal decorated input word in the three possible states:
   reversed base (`p(v)=1`), open `F_v(r)`, and sealed `C_a`.
3. Perform an analytic local word rewrite, tracking every named coordinate
   and direct-child port through the cyclic seam and the inserted child `d`.
4. Derive the endpoint table and list all boundary cases.
5. Only after formulas are fixed, use a tiny predeclared symbolic/finite
   falsifier if needed.  A counterexample must be upgraded to an arbitrary-rank
   obstruction and a minimally richer state description.
6. Freeze a theorem or strict reduction, compute artifact hashes, and request
   fresh immutable audit.

## Expected failure modes

- CP-6 was proved only for an undecorated row and does not preserve persistent
  ports at the root seam.
- Cyclic wrap changes the chronology of a surviving port.
- The open lens needs more state than `(v,r)` at `a=1`.
- A boundary case (`d=1`, no old child, first/last slot, or sealed root) is
  silently excluded by an upstream convention.

