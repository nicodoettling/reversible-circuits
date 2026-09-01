# M133 subtraction-free unique-cycle reduction

Date: 2026-08-13 UTC.

## 1. Scope and imported input

The target is M113/M118's auxiliary incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
M[d,r]=sum_{R(kappa)=r}|C_kappa|,
H[d,c]=M[d,d-c].
```

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  The only imported enumerative input is the accepted M125/M129
coefficient formula.  For fixed indexed permutation-cycle atoms `E`, with
positive integer sizes `a_e`, it uses

```text
w(I)=(sum_{e in I}a_e)^(|I|-3)
```

as the weight of a block `I`.  If `C_E(y,z)` is the weighted polynomial of
ordered pairs of atom partitions whose join is indiscrete, then M125 needs
only its connected-unicycle diagonal

```text
[y^L z^R] C_E(y,z),       L+R=|E|.
```

M125 obtained `C_E` by subtractive connected-component extraction.  The
theorem below replaces that extraction, on exactly the required diagonal, by
an addition-and-product recurrence with positive rational terms.

## 2. Planted-tree polynomial

Let the colours be `L,R`, write `x_L=y`, `x_R=z`, and let `bar(epsilon)` be
the opposite colour.  For disjoint finite edge sets `B,S`, where `|B|` is one
or two, define the planted polynomial `T_epsilon(B;S)` recursively by

```text
T_epsilon(B;S)
 = x_epsilon
   sum_{pi in Part(S)}
   sum_{r_D in D for every D in pi}
     w(B union {r_D:D in pi})
     product_{D in pi}
       T_bar(epsilon)({r_D}; D minus {r_D}).             (2.1)
```

The empty set has one empty partition, one empty root choice, and empty
product one.  Hence, for example,

```text
T_epsilon({e};empty)=x_epsilon a_e^(-2),
T_epsilon({e,f};empty)=x_epsilon(a_e+a_f)^(-1).
```

Interpretation: the root is one coloured incidence vertex.  The edges in `B`
enter it from outside the planted object.  Removing the root divides the
internal edges `S` into the nonempty branch edge sets `D`.  In each branch,
`r_D` is the unique edge incident to the root; beyond it lies a planted tree
of the opposite colour.  The exact incident block at the root is therefore
`B union {r_D}` and receives precisely its M125 weight.  Formula (2.1) is
well-founded because every recursive internal set is strictly smaller than
`S`.  Every term is positive.

## 3. Canonically oriented even core

Fix a total order on the indexed atom set `E`.  For an even core subset
`K subseteq E`, `|K|=2k>=2`, put `e_0=min K`.  Let

```text
(e_0,e_1,...,e_(2k-1))                               (3.1)
```

range over all permutations of `K minus {e_0}` after the fixed first entry.
It encodes the coloured core vertices

```text
left:  {e_(2i),e_(2i+1)},              0<=i<k,
right: {e_(2i+1),e_(2i+2 mod 2k)},     0<=i<k.         (3.2)
```

Assign every off-core edge in `E minus K` to one of these `2k` core vertices.
If the assigned internal sets are `S_0,...,S_(2k-1)`, define

```text
U_(E,2k)(y,z)
 = sum over K, sequences (3.1), and assignments
     product_{i=0}^{k-1}
       T_L({e_(2i),e_(2i+1)};S_i)
     product_{i=0}^{k-1}
       T_R({e_(2i+1),e_(2i+2 mod 2k)};S_(k+i)).        (3.3)
```

Finally put

```text
U_E(y,z)=sum_{k>=1, 2k<=|E|}U_(E,2k)(y,z).             (3.4)
```

There is deliberately no division by `2k`, by two orientations, or by a
vertex automorphism group.  The atoms are indexed.  In an actual coloured
unicycle, start at its least core edge `e_0`; its other edge at the *left*
endpoint is uniquely `e_1`; then alternate through the right and left
endpoints.  This recovers exactly one sequence (3.1).  Reversing the sequence
interchanges which neighbour of `e_0` is left and therefore describes a
different ordered pair of partitions.  When `2k=2`, the same second edge is
the other core edge at both endpoints and the construction still occurs once.

## 4. Positive unique-cycle theorem

**Theorem (proved).**  For every indexed positive-size atom set `E`,

```text
U_E(y,z)
 = sum_{(pi_L,pi_R):
        pi_L join pi_R indiscrete,
        |pi_L|+|pi_R|=|E|}
     y^|pi_L| z^|pi_R|
     product_{B in pi_L union pi_R} w(B).              (4.1)
```

Thus `U_E` is exactly the connected-unicycle diagonal of M125's `C_E`, and
each core-length summand in (3.4) has positive rational coefficients.

**Proof.**  An ordered pair of partitions gives a bipartite multigraph: its
partition blocks are the coloured vertices and every indexed atom is one edge
between its two blocks.  Join-indiscreteness is graph connectivity.  On the
displayed diagonal the graph has `E=V`, so a connected graph has cyclomatic
number one and a unique cycle.  Bipartiteness makes its core length even; two
parallel edges are the allowed length-two case.

Choose the least core edge and traverse from its left endpoint as in Section
3.  This canonically recovers `K` and (3.1)--(3.2).  Delete the core edges.
Every remaining component contains exactly one core vertex: zero would
contradict connectedness, and two would create a second cycle.  This uniquely
assigns every off-core edge to one core vertex.  In each resulting rooted
tree, removing the root vertex uniquely gives a set partition of its edge set
into branches and identifies in each branch the sole edge incident to the
root.  Repeating is exactly recurrence (2.1).

Conversely, (3.3) makes one coloured even cycle and attaches only trees to its
vertices.  It is therefore connected and unicyclic.  The partition and root
choices in (2.1) recover each attached rooted tree once.  Every incidence
vertex is created once, and its factor is `w(I)` for its full incident edge
set `I`; both endpoints correctly include a shared edge.  The colour markers
give `y^|pi_L|z^|pi_R|`.  The two constructions are inverse and preserve all
weights, proving (4.1).  QED.

## 5. Positive defect coefficients

For an integer partition `lambda=(a_1,...,a_c)` of `d`, temporarily index its
parts and let

```text
n(lambda)=d!/product_s(s^m_s m_s!),
h(a)=a^a/(a-1)!.
```

Define the positive core contribution

```text
H_(2k)[d,c]
 = sum_{lambda partition d, length c}
     n(lambda) product_i h(a_i)^2
     sum_{L=1}^{c-1}
       (d+c-2L)!(d-c+2L)!
       [y^L z^(c-L)]U_(lambda,2k).                     (5.1)
```

Here `U_(lambda,2k)` means (3.3) with indexed atom sizes `a_1,...,a_c`.
The orientation used `min E`, but (4.1) shows that the resulting polynomial is
invariant under reindexing.  M125/M129 and (4.1) now give the exact positive
decomposition

```text
H[d,c]=sum_{k>=1,2k<=c}H_(2k)[d,c].                   (5.2)
```

This removes the named subtractive-extraction obstacle.  It does not itself
prove log-concavity: sums of log-concave sequences need not be log-concave.

## 6. Exact expanded inequality and a minimal failed shortcut

Put `A_k(c)=H_(2k)[d,c]` for fixed `d`.  The desired ordinary inequality is
equivalent to the positive-core inequality

```text
sum_{k,l} A_k(c)A_l(c)
  >= sum_{k,l}A_k(c-1)A_l(c+1).                       (6.1)
```

A tempting sufficient statement is the pairwise polarization

```text
2A_k(c)A_l(c)
 >= A_k(c-1)A_l(c+1)+A_l(c-1)A_k(c+1)                (6.2)
```

for every `k,l`; summing (6.2) would prove (6.1).  This shortcut is
**refuted exactly at the first possible rank**.  At `d=4,c=3`, the core
profiles are

```text
A_1(2),A_1(3),A_1(4) = 80136,109440,44928,
A_2(2),A_2(3),A_2(4) = 0,0,216.
```

For `(k,l)=(1,2)`, the cleared margin in (6.2) is

```text
-80136*216 = -17309376.                               (6.3)
```

The full `d=4` inequality remains positive, so (6.3) refutes only termwise
polarization.  It shows that a valid proof must budget the strong curvature
of the two-edge-core profile against the arrival of longer cores.

An exact dominant-core restatement makes that budget explicit.  Let

```text
A[d,c]=H_2[d,c],
E[d,c]=H[d,c]/A[d,c] >= 1.                            (6.4)
```

Then (6.1) is exactly

```text
A[d,c]^2/(A[d,c-1]A[d,c+1])
 >= E[d,c-1]E[d,c+1]/E[d,c]^2.                        (6.5)
```

The first strict next proof route is therefore:

1. prove a universal quantitative lower bound on the left side of (6.5) from
   the planted-tree recurrence with a doubled two-edge core; and
2. prove a matching upper curvature bound on the positive higher-core
   correction `E`.

Neither bound is proved here.  They are narrower and positivity-preserving;
unlike (6.2), they survive all current exact checks.

## 7. Exact audits and boundaries

`positive_unicycle_audit.py` implements (2.1)--(3.4) and compares it with a
separate literal enumeration of ordered pairs of set partitions.  For every
integer cycle type of total size `2<=d<=7` with at least two atoms, all 37
cases agree coefficient-by-coefficient, with zero failures.  This includes
the two-parallel-edge boundary and all even core lengths through six.

`core_profile_scan.py` inserts the positive polynomials into (5.1).  Through
`d=8`, it reconstructs the accepted total rows, finds no fixed-core
log-concavity failure, and records (6.3) as the minimal polarized failure.
These finite signs are only falsification checks.  The theorem is justified
by the bijection in Section 4, not by finite enumeration.

The cases `d=2` and `c=2` have only the two-edge core and one left plus one
right block.  The impossible `c=1` type remains excluded exactly as in
M125/M129.  Ultra-log-concavity and real-rootedness remain refuted at `d=4`.

## 8. Downstream scope

Universal ordinary log-concavity and the weaker DEFECT NO-VALLEY statement
remain unresolved.  Even either one would give only M120's conditional
one-dimensional defect-projection gap.  Fixed-defect two-step expansion, a
comparison back to `A_d`, the M113 handle projection, and the original lazy
exact `{3,4,5}` same-product heat-bath gap all remain open.  No terminal claim
is made.
