# M12 intermediate-density final report

## 1. Exact claims with all quantifiers and conventions

Permutations are maps on `[N]`; `pq` means `p` after `q`; words evaluate as
`t_1...t_m`.  Put `M=binom(N,2)`.  The exact chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m} 1/(m-r+1) sum_i H_{i,r},
R_m={r in {3,4,5}: r<=m},
```

where every `H_{i,r}` is uniform on the exact same-product length-`r` fiber.
The target is the uniform law on `Omega(N,m)`.

Three claims are proved.

**Claim M12-I (uniform all-genus ratio).**  For every `d>=2,g>=1`, if
`C_g(d)` is the number of connected exact-support identity transposition
words on a fixed labeled `d`-set of length `k=2(d-1)+2g`, then

```text
[C_g(d)/k!] / [C_{g-1}(d)/(k-2)!] <= d^3/12.             (1.1)
```

Consequently, for every labeled exact support partition `P` of `[N]`,
including isolates, if its total surplus at length `m` is at least one, then

```text
E_P(m)/E_P(m-2) <= m(m-1)N^3/12.                        (1.2)
```

**Claim M12-II (threshold theorem conditional on one named proposition).**
Let `N>=3`, let `m>2(N-1)` be even (so `m>=2N`), and suppose the exact layer
counts

```text
W_c(N,m)=#{w in Omega(N,m): c(w)=c}
```

are unimodal in `c`, where isolates count as components.  Then for every
`1<=c_0<=N-2`, both sides of the threshold are nonempty and

```text
Phi_pm^K({c<=c_0})
 :=Q_K({c<=c_0},{c>=c_0+1})
   /min{pi(c<=c_0),pi(c>=c_0+1)}
 >=1/[N^5 m(m-1)(m-2)].                                 (1.3)
```

Since total surplus is `G=m/2-N+c`, this is the requested exponent-uniform
anti-bottleneck statement for every total-surplus threshold throughout the
intermediate window, conditional only on component-layer unimodality.

**Claim M12-III (rigorous low-parameter unimodality).**  The sequence `W_c`
is log-concave for every `N` when `m in {0,2,4,6,8}`, and for every even `m`
when `N<=4`.

No reducibility example and no infinite family of superpolynomially small
conductance or spectral gap was proved.  Thus none of these claims is
TERMINAL B.

## 2. Full argument or construction

The complete proof of (1.1)--(1.3), including every insertion and
multiplicity, is in [`checkpoint.md`](./checkpoint.md).  The exact component
identities, low-parameter proof, finite status, and failed total-positivity
route are in
[`component_unimodality_audit.md`](./component_unimodality_audit.md).

The key new argument is short.  For nonnegative sequences with consecutive
ratio bounds `R_1,R_2`, their convolution has consecutive ratio at most
`R_1+R_2`.  Dubrovin--Yang--Zagier Proposition 1, equation (13), writes each
degree-`d` normalized Hurwitz sequence as a positive sum, over ordered splits
`d_1+d_2=d`, of threefold convolutions.  After writing `ell=j+1`, the third
factor has ratio at most `d_1^2/12`.  Induction in `d` closes because

```text
d_1^3+d_2^3+d_1^2 <= (d_1+d_2)^3.
```

This proves (1.1).  The exact macro-fiber factorization makes `E_P(m)/m!` a
convolution over the component genus sequences, proving (1.2).

For the full boundary flow, fix `c_*=c_0+1` and a length-`m-2` exact support
partition `P` with `c_*` components.  Let `e(P)` be its number of internal
transpositions and `x(P)=M-e(P)` its number of cross-component
transpositions.  Then `e(P)>=1` and `x(P)>=N-1`.  Insert a designated
internal square `(t,t)` into positions one and two.  Padding by the actual
next factor `a`, the `H_3` update replaces `(t,t,a)` by `(s,s,a)` for a
cross-component `s`.  The designated deletion preserves `P`, and the target
merges exactly two components.  Summing every shorter word, internal `t`,
and crossing `s` gives

```text
Q_K({c=c_*},{c=c_0})
 >= [1/Z_m] [1/(2|R_m|(m-2)D_N)]
    sum_{P:|P|=c_*} E_P(m-2)e(P)x(P),                    (2.1)

D_N=(3N^2+N-12)/2 <=4M.
```

Combining (1.2) with (2.1) gives the unconditional layer-averaged downward
rate

```text
Q_K({c=c_*},{c=c_0})/pi(c=c_*)
 >=1/[N^4 m(m-1)(m-2)].                                 (2.2)
```

If `W_c` is unimodal, the boundary layer has at least `1/N` of whichever
threshold side is smaller.  This handles both stationary-mass orientations
and proves (1.3).

The exact component polynomial satisfies

```text
sum_c W_c u^c=sum_{P in Pi_N}(u)_{|P|}Z_P(m),
sum_{N,m} P_{N,m}(u)y^N/N!t^m/m!=exp(uH(y,t)).           (2.3)
```

These identities have not yet yielded universal unimodality.  The natural
exponential-Riordan triangle is not even coefficientwise TP2: its first
relevant minor has `t^4` coefficient `-1/4`.  This rejects that sufficient
criterion, not the unimodality claim.

## 3. Probability, runtime, path-length, and congestion accounting

For `m>=2N>=6`, `|R_m|=3`.  A specified padded square refresh uses:

```text
nonlazy/block-size factor     1/(2|R_m|),
specified H3 window           1/(m-2),
specified conditional output  1/D_N,
D_N=(3N^2+N-12)/2<=4M.
```

There is no extra `1/M`: (2.1) explicitly sums all internal `t` and crossing
`s`.  Fixed-position insertion is injective because deletion recovers the
shorter word and `t`; the target's first pair recovers `s`.  The square
remains in the claimed source macro layer because the shorter word already
has exact support `P`.  The crossing square merges exactly two blocks.

The worst-case layer-averaged crossing probability is (2.2), and the
conditional two-sided threshold conductance is (1.3).  No comparison paths
or congestion argument is used.  This mission proves no global gap and
therefore claims no mixing runtime.  The exact `H_3` fiber has polynomial
size formula and the inherited exact block implementation has polynomial
per-step cost.

The deterministic falsification harnesses use integer partitions and all
irreducible `S_N` character shapes; their runtime is exponential in `N` and
is not offered as a sampler.  They are finite normalization checks only.

## 4. Dependencies

- **Proved here:** the convolution-ratio lemma; (1.1) from the cited positive
  recurrence; the exact-partition bound (1.2); the boundary flow (2.1), rate
  (2.2), orientation lemma, and conditional conductance (1.3); exact
  component identities (2.3); low-parameter log-concavity; the negative
  natural TP2 minor.
- **Cited and hypothesis-checked:** Dubrovin--Yang--Zagier, *Classical
  Hurwitz numbers and related combinatorics*, Proposition 1, equation (13),
  <https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
  Their cover count differs from the fixed-labeled-sheet factorization count
  by a degree-dependent, genus-independent factor `d!`.  Substitution into
  the recurrence only changes each ordered-split summand by a positive
  factor independent of `g`, so the ratio proof is unchanged.  Genus-zero
  values `C_0(2)=1,C_0(3)=24,C_0(4)=2880` independently check the
  normalization.
- **Inherited proved inputs:** exact heat-bath reversibility; the
  labeled weighted-component macro-fiber factorization; connected
  feasibility; exact `D_N` three-step fiber count and padded-square update.
- **Conditional:** universal component-layer unimodality.
- **Empirical/exact finite only:** no log-concavity failure through the
  durable rectangle `N<=15,m<=120`; no real-root failure there; the
  independent extended audit through `N<=22,m<=220`.
- **Route obstruction, not a theorem about `W`:** the sufficient total-
  positivity framework of Bao-Xuan Zhu,
  <https://arxiv.org/abs/2006.14485>, cannot be applied to the natural
  triangle because its required TP2 property fails.

## 5. First unproved step

> **COMPONENT-LAYER UNIMODALITY.**  For every `N>=3` and even `m>=0`, the
> sequence `W_c(N,m)` is unimodal on its exact feasible interval
> `max(1,N-m/2)<=c<=N-1` for `m>0` (and is the singleton at `c=N` for
> `m=0`).

This proposition alone, together with the proved all-genus ratio, yields
(1.3) for every `m>2(N-1)`.  The DYZ ratio does **not** prove monotonicity of
successive rates, genus log-concavity, or unimodality.

## 6. Strongest self-attack / failure mode

The main theorem is conditional at exactly the boundary-mass step.  A
polynomial adjacent-layer ratio cannot replace unimodality: iterating it
over `Theta(N)` layers may lose an exponential factor.  The negative TP2
minor only blocks one proof route and does not refute fixed-`m`
unimodality.  Finite real-rootedness through moderate `N,m` gives no joint
asymptotic control.  Even an unconditional theorem for every component-
count threshold would rule out only this family of cuts; it would not prove
conductance for arbitrary cuts inside labeled weighted-component fibers and
would not establish TERMINAL A.

No threshold counterexample emerged.  In particular, a rare pendant
bridge-square subclass cannot be promoted to a bottleneck because the proved
all-square rate (2.2) is polynomial and the smaller-side mass still requires
the full layer distribution.

## 7. Calibration results

- Odd `m`: `Omega(N,m)` is empty; no conductance claim is made.
- `m=0`: the component polynomial is the singleton layer `c=N`.
- `N=2`, even `m`: singleton word space; excluded from (1.3), while (1.1)
  checks exactly (`C_g(2)=1`).
- `m=2,N>=3`: only repeated-edge words and a disconnected local chain; this
  excluded regime is not used.
- `S_3,m=4`: exact layers `(W_1,W_2,W_3)=(24,3,0)`, total `27`.
- `S_4,m=4`: `(0,114,6,0)`, total `120`.
- `S_4,m=6`: `(2880,1050,6,0)`, total `3936`.
- At `m=4`, the `r=4` move is the whole-word heat bath.  The conductance
  theorem starts at `m>=6` and never drops this normalization; the separate
  `m=4` log-concavity statement is enumerative only.
- Near-minimal doubled-tree words lie outside `m>2(N-1)` but are included in
  the proved `m<=8` formulas and the prior sparse theorems.  No dense formula
  is extrapolated down to them.
- Disconnected components retain every color interleaving through the exact
  factor `m! product C(v_i,k_i)/k_i!` used in (1.2).
- No edge-multiplicity or vertex-degree parity characterization is used;
  all counts come from exact products/connected Hurwitz counts.
- No length-two local simulation, canonical hub, graph-only experiment, or
  finite-spectrum inference is used.
- Stationary mass uses the exact smaller-side minimum in (1.3), handled by
  the orientation lemma rather than assuming which side has mass at most
  one half.

## 8. Artifacts and reproduction commands

Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python was `3.12.3`; the Sturm harness used SymPy `1.12`; all other scripts
have no nonstandard dependency.  Every computation is deterministic, so
the recorded random seed is `null`.

From this mission directory:

```bash
python3 real_root_test.py --n-max 10 --m-max 60 --output log_concavity_results.json
python3 real_root_test.py --n-max 15 --m-max 120 --output log_concavity_results_n15.json
python3 real_zero_test.py --n-max 10 --m-max 60 --output real_zero_results.json
python3 real_zero_test.py --n-max 15 --m-max 120 --output real_zero_results_n15.json
python3 threshold_flow_test.py --n-max 10 --m-max 60 --output threshold_flow_results.json
python3 hurwitz_ratio_test.py --n-max 20 --m-max 160 --output hurwitz_ratio_results.json
```

The universal claim each finite computation could falsify is written in its
script docstring and JSON output.  Compact artifacts are:

- [`plan.md`](./plan.md)
- [`checkpoint.md`](./checkpoint.md)
- [`component_unimodality_audit.md`](./component_unimodality_audit.md)
- [`real_root_test.py`](./real_root_test.py)
- [`real_zero_test.py`](./real_zero_test.py)
- [`threshold_flow_test.py`](./threshold_flow_test.py)
- [`hurwitz_ratio_test.py`](./hurwitz_ratio_test.py)
- `log_concavity_results.json`, `log_concavity_results_n15.json`
- `real_zero_results.json`, `real_zero_results_n15.json`
- `threshold_flow_results.json`, `hurwitz_ratio_results.json`

Files changed by this mission are exactly the files listed above, including
this report.  The generated bytecode cache was removed.

## 9. Verdict

OPEN AT A NAMED STEP: COMPONENT-LAYER UNIMODALITY for all `N>=3` and even `m`.
