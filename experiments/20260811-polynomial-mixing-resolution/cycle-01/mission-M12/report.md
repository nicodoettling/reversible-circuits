# M12 Final Report: Sparse and Near-Minimal Red Team

## 1. Exact claim with all quantifiers and conventions

Permutations are maps on `[N]`; `pq` means `p` after `q`, and words evaluate
as `t_1 ... t_m`.  The target is the uniform law `pi` on `Omega(N,m)`.  The
kernel is exactly

```text
K = (1/2) I
    + (1/(2 |R_m|)) sum_{r in R_m}
        (1/(m-r+1)) sum_i H_{i,r},
R_m = {r in {3,4,5}: r <= m},
```

with every `H_{i,r}` uniform on the exact length-`r` same-product fiber.

For a nontrivial support component `C`, let `v_C` be its label count, `k_C`
its factor count, and

```text
g_C = (k_C - 2(v_C-1))/2,
G(w) = sum_C g_C.
```

Write `A_g={w:G(w)=g}` and `A_{<=g}=union_{h<=g} A_h`.  For a cut use the
orientation-free ratio

```text
Phi_pm(A) = Q(A,A^c) / min{pi(A), pi(A^c)}.
```

The following claims are proved.

**Claim M12.1 (zero surplus).** For every `N>=3` and even `m>=4` for which
`A_0` is nonempty and proper, with `M=binom(N,2)`,

```text
Phi_pm(A_0) >= 1 / [72 (m-1)(m-3) M^3].
```

At `m=2(N-1)`, `A_0` is exactly the full-support connected minimal layer.
Thus the principal near-minimal layer, regardless of its stationary mass, is
not a superpolynomial conductance cut.

**Claim M12.2 (cumulative zero/one surplus).** For every `N>=4` and even
`6<=m<=2(N-1)`,

```text
Phi_pm(A_{<=1})
  >= 1 / [27648 N^2 m (m-1)^2 (m-3)^2 M^6].
```

These claims reject two named candidate bottlenecks.  They do not prove an
inverse-polynomial gap for `K`, and they do not establish TERMINAL B.

## 2. Full argument or construction

The full proof, including all injections and exceptional subcases, is in
[`proof_notes.md`](./proof_notes.md), with one corrected nonemptiness witness
in [`proof_notes_correction.md`](./proof_notes_correction.md).

The enumerative input is as follows.  If `C_g(v)` counts connected identity
words on a fixed labeled `v`-set of length `2(v-1)+2g`, then

```text
C_0(v) = (2v-2)! v^(v-3).
```

This is [Vakil, Conventions 1.2 and Corollary 1.5](https://arxiv.org/abs/math/9812105),
specialized to the labeled partition `1^v`.  It is a cited result, not
re-proved here.  Vakil defines the relevant number as transitive
factorizations of one fixed permutation; for `1^v` that permutation is the
identity, and the extra product in his cover normalization is one.  This
gives `C_0(2)=1`, `C_0(3)=24`, and `C_0(4)=2880`, checking the normalization.

Deleting an equal pair at a fixed adjacent position of a minimal connected
word leaves exactly two minimal connected components.  Conversely, for every
labeled unordered bipartition of sizes `a,v-a`, interleave a minimal word on
each part, choose one of the `a(v-a)` crossing edges, and insert that edge
twice.  Deletion recovers the bipartition, both component words, their
interleaving, and the crossing edge, so the only multiplicity is the explicit
factor `1/2` for the two orders of the bipartition.  Hence the fixed-position
square probability is

```text
p_v =
  [(1/2) sum_{a=1}^{v-1} binom(v,a)
       a^(a-2) (v-a)^(v-a-2)]
  / [(2v-2)(2v-3)v^(v-3)]
  >= 1/(12v)                       (v>=3),
```

while `p_2=1`.

Conditional on any all-minimal weighted-component macrofiber, the proved
macrofiber factorization gives independent uniform internal words and a
uniform color interleaving.  Two specified consecutive internal occurrences
of a color of multiplicity `k` remain adjacent globally with exact probability
`k/m`.  Summing over components gives

```text
E[number of globally adjacent equal pairs] >= 1/12,
Pr[at least one] >= 1/[12(m-1)].
```

For any such pair, select a length-four window containing it.  Replace `tt`
by a deterministic `ss` that splits a minimal component and creates exactly
one unit of surplus.  A size-two minimal component is handled by moving its
square into another nontrivial component; such a component exists because
`m>=4`.  Since a length-four same-product fiber has at most `M^3` elements,
the exact kernel gives this specified output probability at least

```text
1/[2 |R_m| (m-3) M^3] >= 1/[6(m-3)M^3].
```

Multiplying proves Claim M12.1 and, more strongly,
`Q(A_0,A_1)/pi(A_0)>=delta_0` with
`delta_0=1/[72(m-1)(m-3)M^3]`.

For genus one, Vakil Corollary 1.5 gives

```text
C_1(v) = (2v)! B_v / 24,
B_v = v^v-v^(v-1)
      - sum_{j=2}^v (j-2)! binom(v,j) v^(v-j),
0 < B_v <= v^v.
```

At a fixed adjacent position, choose an isolated label (`v` choices), a
connected genus-one word on the other labels (`C_1(v-1)` choices), and the
crossing endpoint (`v-1` choices), then insert that crossing edge twice.
Deletion uniquely recovers all three choices, so this is an injection with
exactly `v(v-1)C_1(v-1)` outputs.  The auxiliary lower bound

```text
C_1(v-1) >= binom(v-1,2) C_0(v-1)
```

is also an injection: at one designated position insert a chosen square into
a chosen minimal connected word; deleting that designated pair recovers both
inputs.  Combining this with the displayed upper bound on `C_1(v)` gives a
fixed-position genus-one bridge-square probability at least `1/(64v^4)`.

After color interleaving, every `A_1` macrofiber has probability at least

```text
1/[32 N^2 m(m-1)]
```

of exposing a square whose refresh lands in `A_2`.  The `v=2` genus-one case
uses a minimal companion component (forced by `m>=6`); both its size-two and
larger cases are treated separately in the proof notes.  Including the exact
kernel normalization gives

```text
Q(A_1,A_2)/pi(A_1)
  >= delta_1
  = 1/[192 N^2 m(m-1)(m-3)M^3].
```

Finally, reversibility and the `A_0 -> A_1` flow imply
`pi(A_1)>=pi(A_0)delta_0`, so
`pi(A_1)/pi(A_{<=1})>=delta_0/2`.  Retaining only the `A_1 -> A_2` flow
gives `Phi_pm(A_{<=1})>=delta_0 delta_1/2`, which is Claim M12.2.  This is the
stationary-mass accounting: it remains valid whether the low-surplus side or
its complement has mass below one half.

No reducibility example and no asymptotic cut with superpolynomially small
flow was obtained.

## 3. Probability, runtime, path length, and congestion accounting

- Laziness: the favorable update includes the exact factor `1/2`.
- Block choice: it includes `1/|R_m|`; the proof uses `|R_m|<=3`.
- Window choice: it includes `1/(m-3)` for `r=4`.
- Conditional choice: `F_4(h)<=M^3`, because the first three factors determine
  the fourth; hence a specified valid block has probability at least `M^-3`.
- At `m=4`, `|R_4|=2` and the only `r=4` window is the whole word; the stated
  bound remains conservative.
- Every constructed comparison is a single actual transition, so path length
  is one and there is no routed-flow or canonical-hub congestion term.
- Choosing the witness window and replacement edge is deterministic in
  polynomial time.  Actual exact `r=4` heat-bath sampling has polynomial
  per-step cost by the inherited direct midpoint sampler; no new runtime claim
  is needed for these intrinsic transition lower bounds.
- No computation was run, so there is no stochastic seed, sampling runtime,
  or finite-data extrapolation to report.

## 4. Dependencies

- **Proved (inherited):** exact heat-bath reversibility and uniform
  stationarity; feasible connected-component criterion; macrofiber
  factorization into uniform color interleavings and independent connected
  factors; polynomial exact `r=4` conditional sampler.
- **Proved here:** the square-deletion bijection and its multiplicity; the
  exact `k/m` color-adjacency probability; the one-step transition lower
  bound; the genus-one fixed-position insertions; the reversibility-based
  stationary layer-mass comparison; Claims M12.1 and M12.2.
- **Cited:** Vakil, Conventions 1.2 and Corollary 1.5, for `C_0(v)` and
  `C_1(v)`.  The fixed-permutation and cover normalizations were explicitly
  translated above.
- **Empirical only:** the three smoke-case state counts and pure-Hurwitz
  component counts.  They calibrate, but are not used to prove, either claim.
- **Conditional/unneeded here:** the global Classification H/irreducibility
  theorem.  These conductance calculations do not assume Hurwitz
  transitivity or global irreducibility.

## 5. First unproved step

> **Uniform sparse surplus-threshold proposition.** There exist universal
> constants `c>0,C<infinity` such that for every `N>=3`, every even
> `4<=m<=2(N-1)`, and every integer `g>=2` for which both `A_{<=g}` and its
> complement are nonempty,
> `Phi_pm(A_{<=g}) >= c(Nm)^(-C)`.

The present report proves the analogous statement for thresholds `g=0` and
`g=1`.  Proving the proposition would eliminate every total-surplus threshold
as a superpolynomial sparse bottleneck.  Refuting it with an explicit sequence
and then controlling the full boundary flow, not merely the layer mass, would
create a serious TERMINAL B candidate.

## 6. Strongest self-attack and failure mode

The result rules out only two coarse cuts.  A superpolynomial bottleneck may
sit strictly inside `A_0` or `A_1`, inside a full-support positive-surplus
fiber, or in a statistic unrelated to total surplus.  A polynomial average
escape rate from a macro layer gives no restricted-fiber gap.

The restriction `m<=2(N-1)` is substantive.  It ensures the sparse layer
geometry needed in the `v=2` and companion-component cases and makes `A_0`
nonempty.  It says nothing about denser bridges.  The higher-genus extension
is also genuinely open: this report has no uniform analogue of the Vakil
genus-one bridge-square ratio for `g>=2`, and an exponent depending on `g`
would not be enough when `g` grows with `N,m`.

The Vakil formulas are cited rather than re-proved.  A normalization mismatch
would invalidate the numerical ratios, although the fixed-permutation
definition, the `1^v` specialization, and the values at `v=2,3,4` were checked.

Finally, lower-bounding the conductance of a proposed cut is not a global gap
bound and cannot establish TERMINAL A.  Failure to find another cut is not
evidence against TERMINAL B.

## 7. Calibration results

- Odd `m`: `Omega(N,m)` is empty; no cut is asserted.
- `m=0`: singleton; no cut is asserted.
- `N=2`, even `m`: singleton; excluded from the claims except for internal
  count checks such as `C_0(2)=C_1(2)=1`.
- `m=2,N>=3`: the chain is disconnected because no allowed block fits; this
  excluded case is not used to claim TERMINAL B.
- `S_3,m=4`: `A_0` contains the 24 connected minimal words and `A_1` the 3
  repeated-edge words, totaling 27.  The `r=4` move is the whole-word heat
  bath and is retained in the exact normalization.  The four pure-Hurwitz
  components are irrelevant to the exact heat-bath cut flow.
- `S_4,m=4`: `A_0` contains 96 connected three-label minimal words and 18
  two-square/two-component minimal words; `A_1` contains 6 repeated-edge
  words, totaling 120.  This checks disconnected minimal components and color
  interleavings.
- `S_4,m=6`: `A_0` has 2880 full-support minimal words; `A_1` has
  `960+90=1050` words (a three-label genus-one component plus an isolate, or
  one minimal and one genus-one two-label component); `A_2` has 6 repeated-edge
  words.  The total is 3936, and the proved `A_{<=1} -> A_2` construction is
  visible in this smallest case.
- Connected near-minimal doubled-tree words lie in `A_0`, but the proof counts
  the entire minimal Hurwitz class and never routes through one doubled-tree
  hub.
- Disjoint components retain nontrivial color order; the exact `k/m`
  interleaving factor is included.
- Edge multiplicity parity and degree parity are not used as identity
  criteria.
- The known failure of length-two local simulation is irrelevant: every
  crossing is one actual length-four heat-bath transition.
- No claim is inferred from the known finite spectra or the graph-only
  20260721 experiment.

## 8. Artifacts and reproduction commands

Artifacts, all under the owned directory:

- `plan.md`
- `checkpoint.md`
- `proof_notes.md`
- `proof_notes_correction.md`
- `report.md`

Repository commit inspected: `502a6f0` (`main`).  No executable computation,
randomness, third-party package, or raw-data file was used.  Read the proof
with:

```bash
sed -n '1,999p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M12/proof_notes.md
sed -n '1,120p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M12/proof_notes_correction.md
sed -n '1,999p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M12/report.md
```

## 9. Verdict

OPEN AT A NAMED STEP: Uniform sparse surplus-threshold proposition.
