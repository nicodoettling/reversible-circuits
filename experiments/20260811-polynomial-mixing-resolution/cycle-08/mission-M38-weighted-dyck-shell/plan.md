# M38 plan — weighted Dyck median shell

## Exact target and convention

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`.  Let `m=2N-2`, and let `F_N` be the connected,
full-support identity transposition words of length `m`.  For
`w=(t_1,...,t_m)` put `x_j=t_1\cdots t_j`,
`h_j=N-#cycles(x_j)`, and `Area(w)=sum_{j=1}^m h_j`.

The primary claim under test is that one can choose a feasible integer `q_N`
with

```text
1/4 <= mu_N(Area <= q_N) <= 1/2
```

and with the exact shell ratio

```text
mu_N(Area=q_N) / mu_N(Area<=q_N) >= (N m)^(-C)
```

for a universal `C`.  Combined with the already proved M34 H3 valley action,
this would give an inverse-polynomial full-`K` conductance lower bound for
this particular median-area cut.  If instead an explicit sequence has a
superpolynomially thin shell, I will audit all H3/H4/H5 boundary mechanisms
and the global smaller-side orientation before treating it as a Terminal-B
candidate.

## Exact enumeration route

1. For each Dyck sign path `P`, derive a support-partition Möbius formula for
   its connected weight `W_N(P)`.  If `rho` is a set partition and `A_rho(P)`
   counts identity words whose factors stay within blocks of `rho`, then
   Möbius inversion should give

   ```text
   W_N(P) = sum_{rho} (-1)^(|rho|-1)(|rho|-1)! A_rho(P).
   ```

   Group the sum by integer partitions of `N` and retain the exact number of
   labeled set partitions of each block-size profile.

2. Compute every `A_rho(P)` by a finite cut/join transfer recurrence on tuples
   of conjugacy-class partitions of the corresponding Young subgroup.  The
   transition multiplicity is the exact number of right-multiplying
   transpositions taking one cycle type to another.  Extend the recurrence to
   an area generating polynomial, avoiding enumeration of individual words.

3. Prove the recurrence and inversion formula independently of computation.
   Implement them with exact integers and validate the known complete
   `N=3,4,5` path and area tables.  Then enumerate the smallest further `N`
   that is computationally reasonable to falsify candidate shell inequalities
   or identify the correct asymptotic statement.  Finite agreement will be
   labeled exact finite evidence only.

4. Use the recurrence to seek an analytic comparison: adjacent area-layer
   injections from M34, explicit near-mountain weights, or a weighted Catalan
   lattice inequality.  Track injection multiplicity; a mere monotonicity of
   individual path weights is not enough because the number of paths per area
   varies.

## Calibration and expected failure modes

- Check exact complete weights for `N=3,4,5`, including mountain and
  near-mountain paths and doubled-tree words.
- Keep the original full lazy kernel
  `K=I/2+(1/(2|R_m|)) sum_r (1/(m-r+1)) sum_i H_{i,r}` in every conductance
  conclusion.  At `m=4`, H4 is a whole-word heat bath.
- The cut `A_q` lies inside `F_N`; if its conditional mass is at most `1/2`,
  then its global mass is also at most `1/2`, so the smaller-side denominator
  is exact.  Otherwise the complement and all exits from `F_N` must be handled.
- Nonunimodality at `N=5` rules out assuming log-concavity or unimodality.
- Pointwise macro escape is false, Catalan-uniform surrogates are
  nonresponsive, and locality alone supplies no shell mass.
- Odd `m` is empty; `m=0` and `N=2` even are singleton; `m=2,N>=3` is excluded.
  The small global calibrations are `|Omega(3,4)|=27`, `|Omega(4,4)|=120`,
  and `|Omega(4,6)|=3936`, with 4, 13, and 17 pure-Hurwitz components.

## Deliverables

Write an exact script and machine-readable output if computation is used,
then a genuine halfway `checkpoint.md` and a final `report.md` in this
directory.  The report will use the required nine-field schema and will not
claim universality from finite enumeration.
