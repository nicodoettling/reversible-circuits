# M108 final report: direct adjacent-pair gap reduction

Date: 2026-08-12. Audited commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision and exact proved claim

**PROMOTE THE STRICT DIRECT REDUCTION; DO NOT CLAIM PAIR-GAP OR A
TERMINAL.**

Let `N>=3`, `M=binom(N,2)`, `l>=2`, and let `h in A_N` be a
feasible endpoint for an even raw bridge of length `m=2l`. For the lazy
adjacent raw-pair chain `J_(2l,h)` and the nonlazy complete micro-pair chain
`C_(l,h)` defined in Section 2, the following Dirichlet-form comparison is
proved:

```text
E_J(f,f)
 >= [(l-1)/(4 M^7 l^2 (2l-1))] E_C(f,f)
 >= [1/(12 M^7 l^2)] E_C(f,f).
```

Consequently,

```text
gap(J_(2l,h)) >= gap(C_(l,h))/(12 M^7 l^2).
```

The denominator `12 M^7 l^2` is a conservative uniform simplification; the
first displayed coefficient is the exact coefficient delivered by this
argument. The theorem is new for the auxiliary `J`/PAIR-GAP route, but it
is quantitatively redundant for Terminal A: the accepted direct comparisons
`E_K>=E_B/12` and `E_B>=E_C/(2l^2)` already transfer a universal
complete-pair gap to `K` with the stronger loss `1/(24l^2)`.

## 2. Target, convention, kernels, and laziness

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Put `T=T_N` and declare the target to be uniform on

```text
Omega_(2l)(h)={t in T^(2l): t_1...t_(2l)=h}.
```

Let `H_(k,r)` be exact uniform same-product heat bath on raw positions
`k,...,k+r-1`. The three kernels are

```text
J_(2l,h)
 = (1/2)I + 1/[2(2l-1)] sum_(k=1)^(2l-1) H_(k,2),

B_(l,h)
 = 1/(l-1) sum_(i=1)^(l-1) H_(2i-1,4),

C_(l,h)
 = 1/binom(l,2) sum_(1<=i<j<=l) P_(i,j).
```

Here raw factors are grouped into microcoordinates
`A_i=(t_(2i-1),t_(2i)) in T^2`, and `P_(i,j)` is conditional expectation
given every raw microcoordinate except `i,j`. Thus `J` has an explicit
one-half hold, while `B` and `C` are nonlazy averages of orthogonal
conditional-expectation projections. All three are reversible for the same
uniform fixed-endpoint bridge law. A singleton fiber has gap one.

Sampler diagnostic ledger:

| candidate | claimed target | product/identity ok | crosses Hurwitz macro-components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| lazy `J` | uniform feasible fixed-endpoint bridge | yes | yes, via square refreshes; qualitative only | all four-letter endpoints in `S_3,S_4`; global `S_3,l=3`, `S_4,l=2` | strict comparison proved; universal gap open |

## 3. Local four-letter theorem and connectivity dependency

For every feasible `g in A_N`, define on the uniform four-letter fiber

```text
L_(4,g)=[H_(1,2)+H_(2,2)+H_(3,2)]/3.
```

The following fixed-scale input is proved:

```text
gap(L_(4,g)) >= delta_4 := 2/(3M^7).
```

The connectivity proof uses the accepted type-A specialization of
Douvropoulos--Lewis, published Theorem 18 and Proposition 8(4), respectively
preprint Theorem 4.2 and Proposition 2.7(4), as checked by the M14 l=4
referee. Equal-length transposition factorizations of the same arbitrary
product are Hurwitz-equivalent precisely within a fixed labeled
support-component/factor-count macro. Each Hurwitz move is a positive
adjacent `H_2` transition.

The accepted square-tree construction supplies adjacent bridge and surplus
squares. Each square can be refreshed directly,

```text
(a,a) -> (b,b).
```

For `g!=id`, refreshing every square to one edge in a fixed nontrivial
endpoint cycle reaches a macro depending only on `g` and length four. For
`g=id`, refresh both squares to one fixed edge. At minimum endpoint length
there is no square and the macro is already unique. This proves local
connectivity for every feasible arbitrary endpoint, including unions of
endpoint cycles and fixed points.

If `V=|Omega_4(g)|`, then `V<=M^3` because the first three factors
determine the fourth. A feasible two-letter fiber has size `M`, `3`, or
`2` according as its product is identity, a 3-cycle, or a disjoint double
transposition. Every selected positive edge in a local spanning tree
therefore has transition probability at least `p_*=1/(3M)`. Uniform
tree routing gives

```text
Var(f) <= (V-1)/2 sum_tree (nabla f)^2,
E_L(f,f) >= p_*/V sum_tree (nabla f)^2,
```

and hence `gap(L)>=2p_*/[V(V-1)]>=2/(3M^7)`. The canonical state is used
only to prove connectivity on this fixed four-letter conditional fiber; no
global flow is routed through a canonical hub.

## 4. Complete comparison and scan-factor accounting

Fix the complement of aligned raw block
`I_i={2i-1,2i,2i+1,2i+2}`. If the fixed prefix and suffix products are
`p=t_1...t_(2i-2)` and `s=t_(2i+3)...t_(2l)`, then

```text
p (block) s = h
```

forces the exact arbitrary block endpoint

```text
g=p^(-1) h s^(-1).
```

The conditional law is uniform on this feasible `Omega_4(g)). Write
`e_k=<f,(I-H_(k,2))f>`. Conditional Poincare with the local theorem gives

```text
<f,(I-H_(2i-1,4))f>
 <= 1/(3 delta_4) sum_(k=2i-1)^(2i+1) e_k.
```

Every raw adjacent boundary appears in at most two aligned blocks, so

```text
E_B(f,f) <= 2/[3 delta_4(l-1)] sum_(k=1)^(2l-1) e_k.
```

The exact one-half laziness of `J` gives

```text
E_J(f,f)=1/[2(2l-1)] sum_k e_k
 >= [3 delta_4(l-1)]/[4(2l-1)] E_B(f,f)
 >= E_B(f,f)/(6M^7).
```

The accepted M16 braided-collision comparison, Section 2.6, is
`E_B>=E_C/(2l^2)` in the present random-scan normalizations. Combining the
two inequalities gives the claim in Section 1. For the identity endpoint,
M01/M01-audit's accepted comparison `E_K>=E_J/(3M^2)` additionally yields

```text
gap(K_(N,2l)) >= gap(C_(l,id))/(36M^9l^2).
```

No unbounded path, hidden hub, or exponential congestion enters this
comparison.

## 5. Dependencies and supersession ledger

The proved reduction uses only:

- the accepted Douvropoulos--Lewis arbitrary-product Hurwitz classification
  and type-A translation audited in M14;
- the accepted square-tree macro construction at fixed raw length four;
- the accepted M16 complete-to-adjacent braided Dirichlet comparison;
- M01/M01-audit only for the optional final `K>=J/(3M^2)` consequence.

No new literature dependency is introduced.

The former M27 proposal

```text
mu_l(h) <= A/l
```

for universal PRODUCT-INCREMENT BASE CORRELATION is **REFUTED**, not
unresolved. Accepted M67 gives `mu_l(h)=Omega(l^(-1/2))` on the feasible
minimal odd-long-cycle family. M70/M72 nevertheless prove inverse-polynomial
control of every nonzero cyclic character sector, including the Krylov
closure of that witness. The remaining special-family sector is the
cyclic-invariant `H_0` quotient.

M73/M80 reduce that sector to endpoint-sharing two-step influence; M83/M88
refute the one-step `O(1/n)` shortcut but retain the signed two-step target;
M91/M93 leave balanced `(BA2)` or direct signed `L1`; M94/M100 isolate
`(BD)`; M102/M105 prove the exact singular-face asymptotic and
nonintegrability of the naive bulk integral. They establish the need for a
collision/triangle-type counterterm class, not that this is the exact
complete matching topology.

## 6. First unproved theorem and exact remaining scope

The first universal hypothesis needed by the new reduction is:

> **UNIVERSAL COMPLETE-PAIR GAP (unresolved).** There exist universal
> `c>0` and `C<infinity` such that for every `N>=3`, `l>=2`, and
> feasible `h in A_N`,
>
> ```text
> gap(C_(l,h)) >= c(Nl)^(-C).
> ```

This statement specifies the uniform bridge law, complete conditional-pair
kernel, all feasible arbitrary endpoints, and all lengths `l>=2`. It would
imply the desired inverse-polynomial PAIR-GAP by Section 1. It remains open
for growing base windows and arbitrary endpoints.

The sharp accepted special-family subfrontier is the long-cycle
cyclic-invariant `H_0` gap and its endpoint-sharing signed two-step
interface. It is a necessary fixed-endpoint subcase of the universal theorem,
not a substitute for it. There is no smallest unresolved fixed `l`: each
fixed `l` has a crude polynomial-in-`N` tree bound whose exponent grows
with `l`. The unresolved issue is uniformity in growing `l` and in the
endpoint.

## 7. Boundary audit, self-attack, and fresh exact diagnostics

Boundary cases are explicit:

- `l=2`: `B` and `C` are the whole four-letter heat bath; the proof
  retains all three adjacent H2 scans.
- empty or parity-infeasible fibers are not assigned a gap;
  even raw length forces `h in A_N);
- `N=2` is forced/singleton and excluded from the theorem;
- `m=0` is singleton; at `m=2`, outside the theorem, the whole-pair heat
  bath has gap one; odd identity bridges are empty;
- singleton conditional fibers obey the gap-one convention.

The local `M^{-7}` bound is deliberately crude. It relies on an accepted
classification for connectivity, not on finite matrices. It gives no useful
global canonical paths. The comparison is one-way, proves no lower bound for
`C`, and cannot prove Terminal B. A fixed long-cycle result cannot be
promoted to arbitrary endpoints.

`exact_matrix_audit.py` imports no predecessor code and directly enumerates
transposition words and conditional projections. The deterministic rerun
gave:

| check | states/words | minimum actual gap | theorem bound/result |
|---|---:|---:|---:|
| all feasible `S_3` four-letter endpoints | 81 total, 3 endpoints | `0.3333333333333328` | `delta_4=0.00030483158055174517` |
| all feasible `S_4` four-letter endpoints | 1296 total, 12 endpoints | `0.10414475595051942` | `delta_4=2.381496723060509e-6` |
| `S_3,l=3,h=id` | 243 states | `gap(J)=0.1` | `gap(B)=0.5`, `gap(C)=2/3` |
| `S_4,l=2,h=id` | 120 states | `gap(J)=0.05207237797525943` | `gap(B)=gap(C)=1` |

The script checked PSD forms for the local bound, the sharp `J>=B`
coefficient, `B>=C/(2l^2)`, and the sharp and conservative `J>=C`
coefficients. Minimum numerical margins were between
`-3.54e-16` and `1.67e-16`, consistent with floating eigensolver
roundoff. These bounded checks can refute a formula but do not prove a
universal gap.

## 8. Artifacts, reproducibility, and hygiene

Retained artifacts are `plan.md`, `checkpoint.md`,
`pair_gap_reduction.md`, `exact_matrix_audit.py`,
`exact_matrix_audit.json`, this report, and `SHA256SUMS`. The decisive
deterministic command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M108-pair-gap-direct/exact_matrix_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M108-pair-gap-direct/exact_matrix_audit.json
```

Environment: Python `3.12.3`, NumPy `1.26.4`, no randomness
(`seed=null`). No package installation, network access, commit, push,
manuscript edit, skill edit, predecessor edit, or write outside the owned
mission directory was made. The generated obsolete
`pair_gap_reduction.md.orig` draft was deleted before freeze. Caches are
absent. The final manifest covers every retained artifact except itself.

## 9. Verdict, status ledger, and action

**PROMOTE THEOREM 3 AS A STRICT DIRECT PAIR-TO-COMPLETE REDUCTION. PAIR-GAP,
TERMINAL A, AND TERMINAL B REMAIN OPEN.**

```text
four-letter arbitrary-endpoint H2 connectivity and M^-7 gap    proved
lazy J versus aligned B, with exact scan/laziness factors       proved
lazy J versus complete C, sharp and conservative constants      proved
M27 universal mu_l(h)<=A/l premise                              refuted
universal complete-pair gap over all h,l                        unresolved
long-cycle cyclic-invariant H0 gap                              unresolved
endpoint-sharing signed two-step / BA2 / L1 / BD / MBF          unresolved
universal adjacent-pair gap                                     unresolved
both Terminals                                                   unresolved
```

The next admissible theorem is the universal complete-pair gap above, with
the long-cycle `H_0` problem retained as its sharp accepted special-family
frontier. The present result must not be reported as a complete mixing proof.
