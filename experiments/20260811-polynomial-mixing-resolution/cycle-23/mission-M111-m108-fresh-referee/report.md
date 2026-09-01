# M111 fresh independent referee report on frozen M108

Date: 2026-08-12. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision and audited claim

**ACCEPT.** Numbered material objections: **none**.

For `N>=3`, `M=binom(N,2)`, `l>=2`, and every feasible even endpoint
`h in A_N`, frozen M108 proves on the uniform raw bridge law that

```text
E_J(f,f)
 >= [(l-1)/(4 M^7 l^2 (2l-1))] E_C(f,f)
 >= [1/(12 M^7 l^2)] E_C(f,f),
```

and therefore

```text
gap(J_(2l,h)) >= gap(C_(l,h))/(12 M^7 l^2).
```

This is a valid strict reduction to the unresolved universal complete-pair
gap.  It is not a proof of that gap, PAIR-GAP, Terminal A, or Terminal B.

## 2. Source identity and hash gate

Before the proof audit I ran `sha256sum -c SHA256SUMS` inside the frozen M108
directory.  Every listed artifact passed.  The decisive hashes are

```text
report.md                    0f0d2a8abd9d8d11dc76e90d0ec2fa94d952268a1852f79cac78a648da5d31b8
pair_gap_reduction.md        df35c6b39f3b6d3f92ff29cbf493fefd7303d8e2a517178b29eb7cd72e652484
exact_matrix_audit.py        c22ad4cf7df82ee3e74f420126393cd7a159f096dbf36372b394aba69a5ff6d4
exact_matrix_audit.json      5e31b7b0a1f6e31f9e6736580b1d0dd7131be8892de261fd8fd52f07d75e3b0b
SHA256SUMS                   ef95fc8532990a1f536eb27c8335a649c26be4bf062e573b691f174ec97ddbfa
```

The obsolete `.orig` draft named in earlier coordination is absent.  The
audit used the frozen files and did not modify them.

## 3. Target, convention, kernels, and laziness

The convention is `(pq)(x)=p(q(x))`, with displayed tuple factors multiplied
left-to-right.  The target is uniform on

```text
Omega_(2l)(h)={t in T_N^(2l):t_1...t_(2l)=h}.
```

M108's kernels reconstruct exactly as

```text
J = (1/2)I + 1/[2(2l-1)] sum_(k=1)^(2l-1) H_(k,2),
B = 1/(l-1) sum_(i=1)^(l-1) H_(2i-1,4),
C = 1/binom(l,2) sum_(i<j) P_(i,j).
```

Here `P_(i,j)` conditions on every complete raw microcoordinate
`A_k=(t_(2k-1),t_(2k))` except `i,j`; it is exactly M16's natural
complete-pair projection, including the intervening ordered product for a
nonadjacent pair.  `B` is exactly its adjacent scan.  `J` has the displayed
one-half hold; `B` and `C` are nonlazy averages of orthogonal conditional
expectations.  All use the same uniform bridge law and are reversible.

## 4. Independent audit of the local four-letter theorem

Let `d(g)=N-r(g)` be the minimum transposition length.  Feasibility of an
even four-letter factorization gives `d(g) in {0,2,4}`.  The accepted
Douvropoulos--Lewis type-A specialization connects precisely each labeled
support-component/factor-count macro by Hurwitz moves, and every such move is
a positive adjacent `H_2` transition.

The accepted square-tree representative closes the macro quotient at this
fixed length:

- if `d(g)=4`, the factorization is minimal, has no square, and its macro is
  forced by the endpoint cycles;
- if `d(g)=2`, there is exactly one bridge or surplus square, which may be
  refreshed to a fixed edge of a nontrivial endpoint cycle;
- if `d(g)=0`, then `g=id` and the representative consists of two adjacent
  squares, both refreshable to one fixed edge.

Thus the three-scan chain
`L_(4,g)=(H_(1,2)+H_(2,2)+H_(3,2))/3` is irreducible for every feasible
arbitrary endpoint.  No scalable flow is routed through the canonical word.

If `V=|Omega_4(g)|`, the first three factors determine the fourth, so
`V<=M^3`.  A feasible two-letter transposition fiber has cardinality `M`,
`3`, or `2`; consequently every chosen positive spanning-tree edge has
transition probability at least `p_*=1/(3M)`.  For uniform measure,

```text
Var(f) <= (V-1)/2 sum_tree (nabla f)^2,
E_L(f,f) >= p_*/V sum_tree (nabla f)^2.
```

Therefore

```text
gap(L_(4,g)) >= 2p_*/[V(V-1)] >= 2/(3M^7)=delta_4.
```

The singleton convention is handled separately.  All powers and scan
coefficients in this argument are correct.

## 5. Independent audit of the global comparison constants

After fixing the complement of aligned raw block `2i-1,...,2i+2`, write the
outside prefix and suffix products as `p` and `s`.  The bridge equation forces
the block endpoint

```text
g=p^(-1) h s^(-1),
```

and the conditional block law is uniform on its feasible `Omega_4(g)`.
Because `L_(4,g)` averages three projections, conditional Poincare gives

```text
<f,(I-H_(2i-1,4))f>
 <= 1/(3 delta_4) sum_(k=2i-1)^(2i+1)
       <f,(I-H_(k,2))f>.
```

Each raw adjacent boundary occurs in at most two aligned blocks.  Averaging
over the `l-1` blocks and retaining the explicit one-half laziness of `J`
gives exactly

```text
E_J >= [3 delta_4(l-1)]/[4(2l-1)] E_B.
```

M16 Section 2.6 uses the same `B` and `C`.  Translating its collision and
Hamiltonian normalizations back to random-scan Markov forms gives the
Dirichlet-form inequality

```text
E_B >= E_C/(2l^2).
```

Multiplication and `delta_4=2/(3M^7)` yield the sharp M108 coefficient

```text
(l-1)/[4M^7l^2(2l-1)].
```

Since `(l-1)/(2l-1)>=1/3`, the conservative coefficient
`1/(12M^7l^2)` follows.  The kernels share the same stationary law, so the
Dirichlet comparison transfers to spectral gaps without another factor.

## 6. Dependency, supersession, and redundancy audit

The arbitrary-product connectivity input is exactly the accepted M14
Douvropoulos--Lewis translation; M16 supplies the complete-to-adjacent
Dirichlet comparison.  M01/M01-audit is needed only for M108's optional
identity-endpoint consequence `E_K>=E_J/(3M^2)`.  No new external theorem is
introduced.

M108 correctly marks the old universal product-increment premise
`mu_l(h)<=A/l` as **refuted**, not unresolved.  The accepted M67 theorem and
fresh v4 referee prove a feasible minimal odd-long-cycle family with
`mu_l(h)=Omega(l^(-1/2))`.  That witness is not a complete-pair gap upper
bound and is not Terminal B.  The cyclic-invariant long-cycle `H_0` problem
remains only a necessary special-family subfrontier of the broader arbitrary-
endpoint complete-pair gap.

The new `J -> C` route is quantitatively redundant for Terminal A.  M16's
accepted direct coefficient gives

```text
E_K >= E_B/12 >= E_C/(24l^2),
```

which is stronger than combining M108 with M01 to obtain
`E_K>=E_C/(36M^9l^2)`.  M108 states this limitation accurately.

## 7. Fresh no-import finite falsification check

`independent_matrix_check.py` was written in this referee directory and
imports no predecessor module.  It directly enumerates raw bridges, constructs
conditional-expectation matrices from complement partitions, and checks
stochasticity, symmetry, idempotence, gaps, and the claimed PSD comparisons.

The deterministic output is:

| check | states/words | independent result |
|---|---:|---:|
| all feasible `S_3` four-letter endpoints | 81 words, 3 fibers | minimum local gap `0.3333333333333328` |
| all feasible `S_4` four-letter endpoints | 1296 words, 12 fibers | minimum local gap `0.10414475595051942` |
| `S_3,l=3,h=id` | 243 states | gaps `J=0.1`, `B=0.5`, `C=2/3` |
| `S_4,l=2,h=id` | 120 states | gaps `J=0.05207237797525943`, `B=C=1` |

All local and global PSD margins are at most `3.54e-16` below zero in
absolute value, consistent with float64 eigensolver roundoff.  Enumeration
and partition construction are exact; the eigensolver is numerical.  These
checks agree with M108 but are only bounded falsification evidence.

The reproduction command is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M111-m108-fresh-referee/independent_matrix_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M111-m108-fresh-referee/independent_matrix_results.json
```

Environment: Python `3.12.3`, NumPy `1.26.4`, deterministic, `seed=null`.

## 8. Boundary cases, objections, and claim status

Numbered material objections: **none**.

The theorem correctly excludes empty and parity-infeasible fibers.  Even raw
length forces `h in A_N`; feasibility is still stated separately.  At `l=2`,
`B=C` is the whole four-letter heat bath and all three `H_2` scans remain in
`J`.  `N=2` is a forced singleton and is outside the theorem.  For the
identity target, odd raw length is empty, `m=0` is a singleton, and `m=2` is
outside the project `{3,4,5}` kernel regime.  Singleton conditional fibers use
the stated gap-one convention.

```text
four-letter arbitrary-endpoint local gap                  proved
J-to-B conditional comparison and coefficients            proved
B-to-C dependency in the present normalization            proved/inherited
J-to-C sharp and conservative comparisons                 proved
universal complete-pair gap                               unresolved
long-cycle cyclic-invariant H0 gap                        unresolved
PAIR-GAP and both Terminals                               unresolved
```

## 9. Verdict, artifacts, and hygiene

**ACCEPT M108 without a material correction.**  The coordinator may promote
the direct `J -> C` reduction with the exact unresolved scope above.  It must
not be described as a complete-pair gap theorem or a Terminal.

Retained M111 artifacts are `plan.md`, `checkpoint.md`,
`independent_matrix_check.py`, `independent_matrix_results.json`, this report,
and `SHA256SUMS`.  No network access, package installation, random sampling,
commit, push, predecessor edit, coordinator-file edit, manuscript edit, or
skill edit was performed.  No cache file is retained.
