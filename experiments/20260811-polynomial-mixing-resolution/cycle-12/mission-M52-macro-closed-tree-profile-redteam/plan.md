# M52 plan: macro-closed join-tree profile cuts

## Exact target

Use `(pq)(x)=p(q(x))` and the exact lazy `r={3,4,5}` heat-bath chain at
`N>=4,m=2N-2`.  Let `F_N` be the minimal connected full-support macro.  For
`s(T)` equal to either edge/centroid balance `b(T)` or leaf count `ell(T)`, let

```text
H_q={w in F_N:s(T_J(w))>=q},
L_q=F_N\\H_q.
```

Analyze both macro-closed placements

```text
A_q^+=F_N^c union H_q,   A_q^-=F_N^c union L_q.      (P.1)
```

Either prove uniform inverse-polynomial two-sided conductance for every
nontrivial threshold and both cuts, or construct a literal Terminal-B family
with exact stationary mass and all `H3/H4/H5` flow.

## New boundary requirement

The M49/M51 certificate refreshes an adjacent leaf square to remove its label.
For one cut in (P.1) this move remains on the macro-closed side.  Do not solve
the task by merely assigning the reverse macro exit to the other side.  Seek
genuine within-`F_N` profile crossings that work independently of which side
contains `F_N^c`.

## Proof lanes

1. **Exact internal leaf reattachment.**  For a root-marked state with block
   `(v,u)^2,a`, the same `H3` fiber contains `(v,u')^2,a`.  This keeps full
   support and changes only the attachment of leaf `v`, with exact probability
   `1/[6(m-2)D_N]`.  Count source and target attachments without overlap.
2. **Leaf-count shells.**  From a base tree with exactly `q-1` leaves,
   attachment to a nonleaf gives `q` leaves and attachment to a leaf gives
   `q-1`.  Reduce internal conductance to an exact weighted shell-to-tail
   inequality, then seek a universal polynomial proof using strand deletion,
   fixed-tree recurrence, or a growth/deletion double count.
3. **Centroid-balance shells.**  From a base tree with balance `q-1`,
   attachment at a canonical centroid preserves balance while attachment to
   the smaller side of a witness edge can raise it to `q`.  Audit all parity
   and endpoint cases and derive the analogous shell ratio.
4. **Stationary orientation.**  Record
   `pi(F_N)=(2N-2)!N^(N-3)/|Omega(N,2N-2)|` and exact masses of both cuts.
   Prove bounds for both placements in (P.1), not just conditional conductance
   inside `F_N`.
5. **Red team.**  If the shell ratio can be superpolynomially small, calculate
   every internal and macro `H3/H4/H5` crossing before claiming Terminal B.
   Locality or an auxiliary tree bottleneck alone is nonresponsive.

## Exact falsification

Use existing exact weighted tree layers through `N=8` only to falsify named
shell inequalities or detect the first failing threshold.  Any new artifact
will record commit, convention, exact claim, deterministic command, and
finite-scope warning.

## Deliverables

Write a genuine halfway `checkpoint.md`, then a nine-field `report.md` with
exact claims/reductions, probability and runtime accounting, labeled
dependencies, first standalone gap, self-attack, full calibration suite,
artifacts/commands, and exact verdict.
