# M291 final report: chartless base-route signatures

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
FINAL VERDICT: PROMOTE THE EXACT FRAMED-STABILIZER REDUCTION.
               REFUTE POLYNOMIAL COMMON-PREFIX PAIRED-CHART COVERS.
               KEEP THE TRUE M135 COMMON-SCHEDULE REFINEMENT UNRESOLVED.
```

For every requested rank `d>=6`, each actual root-stabilizer orbit edge
selected by an arbitrary fixed M135 perfect-matching color has an individual
literal signed-braid route of length at most

```text
100 d (2d-2)^3.
```

After framing both endpoints through the fixed doubled-star chart `c_d`, its
entire literal braid fiber is exactly

```text
alpha_Q ; BStab_d ; delta_Q^(-1).                     (1.1)
```

This is a necessary-and-sufficient reduction: a family has one common
literal schedule exactly when its sets (1.1) have nonempty intersection,
and the polynomial representative-length condition remains separate.

The first attempted compression fails sharply.  For the physical states in
any fixed M135 matching color, any cover assigning one common prefix per
class and requiring that prefix to send its class into *any* ordered
consecutive doubled Cayley-tree word has at least

```text
q >= (2d-2)!/[d^2(d-1)!] >= d^(d-3)                  (1.2)
```

classes.  Valid M278 extension charts are a subset of those paired-tree
words, so (1.2) refutes the narrower chart-canonicalization cover as well.

Crucially, (1.2) neither proves nor lower-bounds the true polynomial M135
matching-coset refinement.  It is not a schedule-class lower bound.  The
source and target frames may cancel through different elements of
`BStab_d`, which is exactly the interaction retained in (1.1).

## 2. Target, convention, and type firewall

The ambient project target is the global fixed-length uniform law on
identity transposition words.  M291 studies only deterministic routing in
its minimal connected sector

```text
Z_d={w in Transpositions(S_d)^(2d-2):product(w)=id,
                                           support(w) connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  A semicolon between braid words means chronological
composition.  The local generators are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

`B_m` denotes literal braid words modulo braid relations acting on words;
`Acal_d` denotes the finite global action image on `Z_d`; `G=S_d` denotes
global relabeling; and `H=Stab_G(d)` denotes the root stabilizer.  None of
these objects is identified with another.

At one fixed rank, projection from literal braid fibers to finite action
fibers preserves common nonemptiness because a common action has a common
braid lift.  It does not preserve representative length.  Across ranks no
finite action embedding is asserted: M284's accepted lift remains the
literal word embedding `j_d` and its exact common-right-cancellation
identity.

## 3. Constructive frame theorem

Use the fixed word

```text
c_d=(1,2)^2(1,3)^2...(1,d)^2.
```

It is the M278 canonical word for the star rooted at the leaf `d`, whose
root edge is `{1,d}`; hence it is a valid doubled-tree extension source
chart.  M13's accepted quantitative construction routes any two words with
the same labeled weighted support components in at most `50Nm^3` signed
Hurwitz moves.  Every member of `Z_d` has the same one-component data, so
for `m=2d-2` it supplies source and target frames

```text
w_Q --alpha_Q--> c_d,       |alpha_Q|<=50d(2d-2)^3,
tau_i(w_Q) --delta_Q--> c_d,|delta_Q|<=50d(2d-2)^3.
```

Their concatenation `alpha_Q;delta_Q^(-1)` realizes the chosen endpoint
pair.  Braid/relabeling equivariance and M135's `H`-equivariance of `tau_i`
show that it realizes the entire actual `H`-orbit edge.  Inserting every
literal braid fixing `c_d` gives (1.1), and reversing any endpoint route
proves the converse inclusion.

Different constructive branches change `alpha_Q` and `delta_Q` only by
right multiplication by chart-stabilizer elements, so the set (1.1) is
branch-independent.  The exact signature data are therefore the intrinsic
framed fiber, not the arbitrary normal-form transcript.

## 4. Arbitrary-rank obstruction proof

The broad target set `P_d` contains one word for every labeled Cayley tree
and every order of its `d-1` edges, with each edge repeated consecutively.
Thus

```text
|P_d|=d^(d-2)(d-1)!.
```

M112/M119 gives `|Z_d|=d^(d-3)(2d-2)!`.  M135/M137 gives free `G` and `H`
actions and exactly one selected `H`-edge over every left global orbit in a
matching color.  Consequently the physical source color `C` has

```text
|C|=(|Z_d|/d!)(d-1)!=|Z_d|/d=d^(d-4)(2d-2)!.
```

Every fixed braid acts bijectively on `Z_d`, so it sends at most `|P_d|`
states of `C` into `P_d`.  The union bound gives (1.2).  This proof permits
overlapping classes, arbitrary class subsets, unlimited prefix length, and
different paired-tree targets within one class.  It therefore applies in
particular to orbit-edge signature covers: `P_d` is globally relabeling
invariant, so one representative maps into `P_d` exactly when its whole
`H`-orbit does.

The proof is analytic for arbitrary rank.  No small-rank enumeration or
guard is used.

## 5. Frozen dependency audit

All 166 payload rows in the frozen M112/M119, M135/M137, M175/M176,
M181/M183, M200/M202, M240/M242, M269/M271, M273/M275, M278/M281, and
M284/M288 checksum inventories pass.  The exact top digests and row counts
are recorded in `dependency_audit.md`.  In particular,

```text
M284 SHA256SUMS 3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3
M288 SHA256SUMS fd4120e216b9140c4a8938724c3415393d6f5495a105f817cf681871545942ca
```

The semantic gates remain unchanged:

- M175/M176 and M181/M183 require a genuine synchronized quotient route;
- M200/M202 is finite rank five only;
- the accepted local correction table begins after a valid chart/common
  base route is available; and
- M284/M288 proves a literal rank-lift identity and a chart-only coverage
  obstruction, not the true common base schedule.

## 6. First remaining lemma

The exact open interface is:

> **FRAMED-STABILIZER COMMON-INTERSECTION.**  For the actual `H`-orbit
> edges of an arbitrary M135 matching color, cover the intrinsic fibers
> `alpha_Q;BStab_d;delta_Q^(-1)` by `d^O(1)` families whose intersections
> contain literal braid representatives of length `d^O(1)`, or prove that
> no such cover exists.

The common-prefix paired-chart strategy cannot prove this lemma by (1.2).
Any successful compressed signature must retain enough two-sided frame data
to detect stabilizer cancellation.

## 7. Numbered qualifications and prohibited inferences

1. The individual `O(d^4)` routes use different frames for different
   orbit edges; they are not a common schedule.
2. The lower bound (1.2) applies only to common chart-canonicalizing
   prefixes (and, by inversion, the analogous target suffixes).  It does not
   count true schedule classes.
3. Finite action fibers and literal braid fibers have the same same-rank
   common-nonemptiness predicate, but only literal words carry the required
   length and accepted cross-rank embedding.
4. No local correction, voltage, recovery multiplicity, congestion,
   spectral-gap, mixing-time, every-color common-schedule, or Terminal
   conclusion is proved or refuted.
5. The main theorem is stated for `d>=6`, hence `m=2d-2` is even and at
   least ten.  Odd `m`, `m=0,2`, and `N=2` are outside this minimal-sector
   interface.  The counting inequality itself is valid from `d=3`.

Material numbered objections to the two claims at their stated scope:
**none found; fresh immutable audit requested**.

## 8. Artifacts and hygiene

Owned artifacts before freezing are `plan.md`, `checkpoint.md`,
`dependency_audit.md`, `framed_stabilizer_obstruction.md`, this report, and
the forthcoming freeze/audit files.  No predecessor, coordinator,
manuscript, project-skill, source-of-truth, or other worker file was edited.
No experiment was needed because the obstruction is a closed-form
arbitrary-rank proof.
