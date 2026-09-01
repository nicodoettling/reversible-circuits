# M123 Halfway Checkpoint

Date: 2026-08-12.

## Scope retained

The only target is the auxiliary right-heavy inequality

```text
H=(I-Q)^(-1)A_0 <= q(1-q)
```

uniformly over suffix excess.  No fixed-`L` theorem, gap, ROOT-MEAN LIFT,
mixing, or terminal claim is being attempted.  Every live attachment rank
`j=1,...,k` remains in every recurrence.

The repository instruction `references/experiments.md` disagrees with the
filesystem: that path is absent, while the required file exists at
`.codex/skills/reversible-circuit-sampler/references/experiments.md`.  The
latter was read and used; the discrepancy is not silently ignored.

## Reconstructed exact recurrence

For `x=(s,K,R,B)`, the accepted transformed recurrence is

```text
H(x)=A_0(x)+sum_y Q(x,y)H(y),
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B),  t>B, j=1,...,k,
```

with `j=0` and rank-one reset-energy targets killed.  Both suffix excess
`L=s-B` and phase `P=s+K-R` descend, so this is a finite DAG.  M90's direct
variance/Bessel budgets, M98's one-step defect sign, and M103's two-layer
defect sign are accepted as refuted and are not being retried.

## Narrowed structural lemma

The promising lift has two separate parts which must not be conflated.

1. **Complete marked suffix histories.**  Before killing rank-one
   reset-energy targets, expand the accepted pointwise inheritance through
   every root group and every attachment rank.  Retain the initial ambient
   factor word, external and inner attachment positions, scan pair,
   favourable rank-two outcome, the two-chain shuffle, and all inverse
   insertion records.  The deletion/insertion bijection makes distinct
   marked histories disjoint, while the closed contextual-mean identity
   should make their total stationary success mass exactly `q`.
2. **Reset frame categories.**  A variance proof would additionally need
   the canonical reset currents to be categories (or an orthogonal frame)
   of that success submeasure.  This is a new assertion, not a consequence
   of Part 1.

## First structural obstruction found

The natural **unique active-reset category** assertion is false already at
the right-heavy state

```text
x=(s,K,R,B)=(4,1,0,1).
```

The supported source composition `C=(1,1,1,1)` has positive terminal marked
success mass (`H_x(C)=1`).  Its canonical first-merge path is

```text
(1,1,1,1) -> (2,1,1) -> (3,1) -> (4).
```

The first endpoint has an inactive rank-one reset target, but the endpoints
`(2,1,1)` and `(3,1)` both have active reset targets.  Hence every retained
word/scan/outcome atom over this source lies in at least two active canonical
basins.  Keeping finer marks cannot remove membership in two basins that is
already forced by the source composition.  Assigning the atom only to its
first active edge changes the later basin current and therefore does not
reproduce `A_0`.

This refutes the natural partition/event proof, not the target inequality.
The exact fallback is a signed two-copy collision frame:

```text
theta_e^2/c_e
 = sum_(C,C' in basin(e))
     [rho(C)(h(C)-q)] [rho(C')(h(C')-q)] / c_e.
```

After multiplying by every complete deep-history weight, summing this
identity gives `H` exactly.  Nested-basin pairs occur repeatedly and have
both positive and negative signed cross terms, so a Bernoulli/Bessel bound
does not follow formally.

## Remaining work

- implement an independent exact rational complete-history and signed-frame
  checker;
- certify the minimal collision and quantify the failed first-edge
  partition identity;
- verify the signed-frame equality against direct resolvents on all small
  DAGs, retaining all `j`;
- search exact small and broader discovery ranges for either a target
  violation or a stronger collision/normalization failure;
- write the standalone lemma/refutation and nine-field final report with
  hashes, commands, claim labels, and limitations.

