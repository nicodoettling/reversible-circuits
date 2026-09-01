# Frozen addendum: all-length crude gap and minimal-cycle red team

## 1. Exact claim and conventions

Use `(pq)(x)=p(q(x))`, let `M=binom(N,2)`, and let `Q_N` be two uniform
transposition steps.  For `N>=3`, pair length `l>=2`, and feasible endpoints
`u,v in A_N`, put `h=u^{-1}v` and

```text
Omega_h^(2l)={t in T_N^(2l):t_1...t_(2l)=h}.
```

On its uniform law define

```text
B_l=(1/(l-1)) sum_{j=1}^{l-1} H_{2j-1,4},
mathcal H_l=sum_{j=1}^{l-1}(I-H_{2j-1,4})=(l-1)(I-B_l).
```

**Theorem.** Every nonempty such bridge is irreducible and, writing
`V=|Omega_h^(2l)|`,

```text
gap(B_l;u,v)
 >= 2/[(l-1)M^4 V(V-1)]
 >= 2/[(l-1)M^(4l+4)],                                (1)

Lambda_N(l;u,v) >= 2/M^(4l+4).                        (2)
```

The first denominator is for `V>=2`; a singleton has gap one.  The exponent
is exactly `4l+4`: `M^4` comes from one four-factor conditional fiber, while
the ordered-pair spanning-tree load contributes `V^2<=M^(4l)`.

## 2. Full proof

The qualitative input is Douvropoulos--Lewis, published Theorem 18 (Theorem
4.2 in the section-numbered preprint) and published Proposition 8(4)
(Proposition 2.7(4) in that preprint).  The checked type-A specialization says
same-product transposition factorizations are Hurwitz-equivalent exactly when
their factorization graphs have the same labeled components and component
weights, with

```text
k_C=v_C+q_C-2+2g_C.
```

For every `l>=2`, every adjacent pair among the `2l` factor positions lies in
an aligned window `[2j-1,2j+2]`: use the window beginning immediately before
an even-position pair, the window beginning at an odd-position pair, and the
last window for `(2l-1,2l)`.  Retaining the other two factors makes every
adjacent Hurwitz generator an exact same-product `H_4` outcome.

Inside each graph component, arrange minimal factorizations of its endpoint
cycles, adjacent bridge squares along a tree of those cycles, and adjacent
surplus squares.  The checked orbit theorem reaches this target.  Every
adjacent square is contained in an aligned window and can be replaced by a
square on one fixed nontrivial endpoint cycle.  This separates all endpoint
cycles and stores every excess pair on that anchor.  For the identity
endpoint, arrange the whole word as adjacent squares and refresh every pair
to one designated transposition.  Thus all macros reach a common macro and
`B_l` is irreducible.  This also covers minimum-length words, where the macro
is already unique and no square is required.

For the quantitative statement, `V<=M^(2l)`.  If

```text
F_4(g)=#{(r_1,...,r_4) in T_N^4:r_1...r_4=g},
```

then a specified positive outcome has probability

```text
p_* >= 1/[(l-1)F_4(g)] >= 1/[(l-1)M^4].               (3)
```

Choose any spanning tree of the positive transition graph.  Its paths have
length at most `V-1`, and any edge has ordered-pair load at most `V^2`.  For
uniform `pi`,

```text
Var_pi(f) <= ((V-1)/2) sum_tree (nabla f)^2,
E_B(f,f) >= (p_*/V) sum_tree (nabla f)^2.
```

Hence `gap(B_l)>=2p_*/[V(V-1)]`, proving (1).  Multiplication by `l-1`
gives (2).  At `l=2`, the sole `H_4` is the whole-word heat bath and the true
gap is one; (1)--(2) remain valid but deliberately weak for `N>=3`.

## 3. Probability, runtime, path, and congestion accounting

- Window choice is exactly `1/(l-1)` and the conditional outcome probability
  is exactly `1/F_4(g)`; no laziness is inserted.
- Path length is at most `M^(2l)-1`; ordered-pair edge load is at most
  `M^(4l)`; stationary edge conductance is at least `p_*/V`.
- An exact step enumerates at most `M^4` blocks.  Constructing the crude tree
  by full enumeration costs at most `M^(2l)` states and is not polynomial in
  `N,l` when `l` grows.
- Since each heat bath is an orthogonal conditional expectation, `B_l` is
  positive semidefinite.  The same accounting yields

  ```text
  tau_B(epsilon)
   <= ((l-1)/2)M^(4l+4)(2l log M+log(1/epsilon)).
  ```

## 4. Dependencies and status

- **CITED AND CHECKED:** Douvropoulos--Lewis published Theorem 18 and
  Proposition 8(4), with the preprint numbering stated above.
- **PROVED:** the aligned-window translation, macro square canonicalization,
  and complete state-count/spanning-tree bound.
- **EXACT FINITE:** the counterexample audit below; it is not a dependency of
  (1)--(2).
- **CONDITIONAL/OPEN:** an exponent independent of `l` in the M10 base
  regime.

## 5. First unproved proposition

> **UNIFORM BASE-SCALE FIXED-ENDPOINT GAP.**  There exist universal positive
> `c,C,C_0` such that for all `N>=3`, `2<=l<=C_0N log(N+1)`, and feasible
> endpoints,
>
> ```text
> Lambda_N(l;u,v) >= c(Nl)^(-C).
> ```

The all-length bound (2) is superpolynomial when `l=Theta(N log N)` and does
not discharge this proposition.

## 6. Counterexample search and strongest self-attack

A natural nonnormal-Schreier candidate is the minimum factorization of a
full odd cycle: take odd `N`, `h=(1...N)`, and `2l=N-1`.  Every factorization
graph is a labeled tree and the component/weight macro is unique, so no
support-component threshold can be a bottleneck; any obstruction must live
inside the transitive Hurwitz action.

The tempting next shortcut is to treat the raw factorization graph as a
uniform Cayley tree and cut on the number `X` of tree edges crossing a fixed
balanced label bipartition.  The exact first local case `N=7,l=3` refutes
that stationary-law premise.  The true crossing histogram is

```text
X:                    1     2     3     4     5    6
factorization count: 2880  4080  4700  3345  1500  302
uniform-tree count:   576  2832  5452  5139  2376  432.
```

Both rows total `7^5=16807`, but they differ sharply.  For the actual smaller
side `A={X<=2}`,

```text
pi(A)=6960/16807,
Q(A,A^c)=228568/2100875,
Phi(A)=28571/108750 = 0.2627218390... .                (4)
```

The calculation includes the exact `1/2` scan over the two aligned windows
and every conditional-fiber denominator; 6592 of the 6960 states in `A`
have a positive crossing outcome.  An independent reverse-direction sum over
the complement gives exactly the same rational stationary flow.  Thus this
bounded cut is neither invariant nor a thin interface.  It does not prove an
asymptotic lower bound: the raw tree distribution and full boundary flow still
require a uniform formula in odd `N`.  No explicit superpolynomial bottleneck
was obtained, and a slow auxiliary `B_l` would not by itself imply Terminal B
for `K`.

## 7. Calibration

- `l=2` is the whole-word heat bath; `N=2` is singleton but excluded from the
  numerical bound because `M=1`; `m=0` is singleton and original `m=2` is
  outside aligned dynamics.
- Odd identity-word length is empty.  Every feasible endpoint and both word
  boundaries are covered by the qualitative proof.
- The 27/120/3936 checks and every-endpoint `l=3,4` finite checks remain in
  the frozen M14 artifacts.
- Minimum words, labeled support, ordered interleavings, and exact
  microfactor multiplicities are retained.  No parity statistic is used as
  a characterization.
- The generic surjective-support zipper for `N>=5` and canonical growing-
  length hubs are not used.

## 8. Artifacts and reproduction

Owned files in `cycle-04/mission-M14-l4-resolution/`:

- `general_length_addendum.md`;
- `minimal_cycle_cut.py`;
- `minimal_cycle_cut_N7.json`;
- the corrected `report.md` and `checkpoint.md`.

Run from the repository root:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-l4-resolution/minimal_cycle_cut.py --N 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-l4-resolution/minimal_cycle_cut_N7.json
```

The JSON records the exact claim, target, kernel, command, Python `3.12.3`,
null seed, exact rational masses and flows, and commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED
