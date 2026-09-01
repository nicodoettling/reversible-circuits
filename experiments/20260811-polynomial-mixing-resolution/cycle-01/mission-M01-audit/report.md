# M01 / pair-chain independent audit report

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `pq` means `p` after `q`, and words evaluate
as `t_1...t_m`. Let `M=binom(N,2)`.

The audit proves all three frozen claims:

1. For every `N>=3` and even `m>=4`, the exact lazy same-product
   `{3,4,5}` chain `K_{N,m}` is irreducible on `Omega(N,m)`.
2. For the exact lazy adjacent-pair heat bath
   `J=(1/2)I+[1/(2(m-1))]sum_j H_{j,2}`, every real `f` satisfies
   `E_K(f,f)>=E_J(f,f)/(3M^2)`, and hence
   `gap(K)>=gap(J)/(3M^2)`.
3. At every fixed adjacent position under the uniform bridge law,
   `Pr(t_j=t_{j+1})=p_{m-2}/(M p_m)>=1/M`, the square label is uniform,
   and the stationary changed-square refresh rate of `J` is exactly
   `(1/2)[p_{m-2}/(M p_m)](1-1/M)`.

## 2. Full argument

The complete symbolic audit is in `proof_audit.md`.

Ben-Itzhak--Teicher Theorem 3.4 has precisely the needed identity,
equal-length, transposition-factor hypotheses. Its graph uses all labeled
vertices, including isolates. Its Hurwitz generator is the inverse project
generator, so the equivalence relation is the same. Length-three padding
realizes every classified Hurwitz move at both endpoints. Each macro-class has
an explicit adjacent-square representative obtained from doubled labeled tree
edges plus surplus square pairs. A length-four window refreshes each square,
including at a boundary and for `m=4`, connecting all states to one word.

For the pair comparison, a nontrivial same-product pair replacement must
change both coordinates, so an off-diagonal `J(x,y)` has a unique scan index.
This validates the frozen exact point-probability formula. Padding by an
unchanged neighbor gives the corresponding `H_3` transition. The estimates
`F_3<=M^2`, `F_2>=1`, and
`(m-1)/(|R_m|(m-2))>=1/3` yield the pointwise ratio and then the Dirichlet
comparison.

The square statement is an exact insertion/deletion bijection followed by
even-moment monotonicity for the self-adjoint random-transposition operator.

## 3. Probability, runtime, path length, and congestion accounting

- A selected padded Hurwitz rewrite has exact contribution
  `[2|R_m|(m-2)F_3(h)]^{-1}` and worst-case lower bound
  `[6(m-2)M^2]^{-1}`.
- A selected square refresh has exact contribution
  `[2|R_m|(m-3)F_4(h)]^{-1}` and lower bound
  `[6(m-3)M^3]^{-1}`.
- At most `m/2` nontrivial square refreshes follow the classified Hurwitz
  path, but the classification gives no polynomial bound on that path's
  length or on the runtime for constructing it.
- No canonical-path congestion bound is claimed. Routing through the universal
  square word is explicitly disallowed for mixing because it is an atypical
  hub.
- The comparison has exact loss at most `3M^2`; it uses one `H_3` transition
  per off-diagonal `J` transition and has no path-length congestion factor.
- An `H_2` conditional sample is elementary and polynomial-time: the product
  fiber has size `M` for identity, 3 for a 3-cycle, and 2 for a product of two
  disjoint transpositions.
- The deterministic exact audit ran under Python 3.12.3 in about 10.3 seconds
  on the current machine. It has no random seed or nonstandard dependency.

## 4. Dependencies

- **Cited and checked:** Ben-Itzhak and Teicher,
  `Literature/0110110v1.pdf`, Theorem 3.4 and Definitions 1.3, 3.1--3.3.
- **Proved in this audit:** convention translation; endpoint padding;
  component identity and `k>=2(v-1)` necessity; paired representatives;
  boundary square refresh; uniqueness of the off-diagonal `J` scan;
  pointwise and Dirichlet comparison; square insertion/deletion and spectral
  moment argument; qualitative irreducibility of `J`.
- **Empirical/exact finite facts only:** the three calibration enumerations in
  `results.json`. They are falsification checks, not the universal proof.
- **Not used:** finite spectral convergence, the missing fresh-square lemma,
  a quantitative Hurwitz-mixing theorem, or a normal-form congestion claim.

## 5. First unproved step

**Proposition PAIR-GAP.** There exist universal constants `c>0` and finite
`C` such that, for every `N>=3` and even `m>=4`,

```text
gap(J_{N,m}) >= c (Nm)^(-C).
```

This proposition, together with the audited comparison, would prove the gap
part of TERMINAL A. It remains completely open here.

## 6. Strongest self-attack

The audit establishes only a sufficient comparison from the simpler chain
`J` to `K`. A small gap or bottleneck for `J` would not refute fast mixing of
`K`, because the comparison is one-way. Qualitative irreducibility of `J`
does not control its gap. Likewise, the square frequency is stationary
average flow: sparse individual words can have no adjacent square, and no
arbitrary cut conductance follows from the lemma. Finally, the classification
path can be exponentially long or congested without contradicting anything
proved here.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty by sign.
- `m=0`: the empty word is a singleton state space.
- `N=2`, even `m`: the only transposition is forced, so the state space is a
  singleton.
- `m=2,N>=3`: the stated `{3,4,5}` kernel has no allowed block and is excluded;
  its `M` square words are not connected by that kernel. The auxiliary `J`
  would be a different whole-pair heat bath.
- Exact `S_3,m=4`, `S_4,m=4`, `S_4,m=6`: `results.json` has state counts
  27, 120, 3936; one `K` component; 4, 13, 17 Hurwitz components; normalized
  rows; scan multiplicity one; and all comparison/square checks passing.
- `m=4`: `H_{1,4}` is retained. Its update coefficient is exactly `1/4`, and
  its contribution to each whole-word target is `1/(4|Omega|)`.
- Near-minimal connected words: when `k=2(v-1)`, the representative is exactly
  a doubled labeled tree with no surplus tail.
- Disjoint supports/interleavings: the proof keeps relative order within each
  component and invokes the labeled classification to handle the original
  interleaving; it does not discard word order.
- Edge/vertex parity: neither is used to characterize identity words.
- Known `L=2` warning: internal simulation inside a two-letter block remains
  impossible. The comparison pads outside that pair by an unchanged third
  factor, including inward padding at an endpoint.
- Canonical hub: used only for finite reachability, never for gap or
  congestion.

## 8. Artifacts and reproduction

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

- `plan.md`
- `checkpoint.md`
- `proof_audit.md`
- `exact_audit.py`
- `results.json`
- `report.md`

Exact command:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M01-audit/exact_audit.py \
  > experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M01-audit/results.json
```

The computation can falsify the named universal claims in the listed cases;
it cannot prove their extension beyond those cases.

## 9. Verdict

PROVED
