# M129 final report: fresh referee of M125 defect coefficients

Date: 2026-08-13 UTC.

## 1. Verdict

**ACCEPT** the frozen M125 package within its stated scope, with zero
objections.

- **PROVED, relative to the already accepted M113/M118 exact cell formula:**
  M125's rooted one-colour recurrence, connected two-colour extraction,
  connected-unicyclic diagonal, cycle-type coefficient formula, and exact
  equal-cycle multiset aggregation are correct, including the `c=1` boundary.
- **REFUTED:** ultra-log-concavity of the defect masses fails at `d=4`; the
  corresponding quadratic defect polynomial is not real-rooted.
- **EXACT FINITE:** all rows `2<=d<=22` are unimodal and ordinarily
  log-concave, and every tested row `d>=4` fails ULC.
- **UNRESOLVED:** universal ordinary log-concavity, DEFECT NO-VALLEY, every
  downstream incidence/projection spectral-gap obligation, and the original
  lazy exact `{3,4,5}` heat-bath gap.

Neither Terminal A nor Terminal B follows from this audit.

## 2. Target, convention, and dependency boundary

The audited target is the auxiliary M113/M118 incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,
M[d,r]=sum_{R(kappa)=r}|C_kappa|,
R(kappa)=d-c(p),
```

not the uniform law on identity transposition words and not the lifted law
`bar_pi`.  M125 states the project convention `(pq)(x)=p(q(x))`, with tuple
factors multiplied left-to-right.  The recurrence audit itself begins after
the sole imported enumerative input, the M113 exact cell formula accepted by
M118:

```text
|C_kappa|=j!(2d-j)!
  product_(B in Q_L union Q_R)|B|^(c_B-3)
  product_(p-cycle a)[a^a/(a-1)!]^2.
```

I inspected the M113 derivation and M118's independent convention/formula
audit.  This report neither re-proves the classical genus-zero Hurwitz count
underlying that formula nor adds a new assumption.

The complete M125 `SHA256SUMS` check passes.  The coordinator's generic names
`manifest`, `checker`, and `proof` correspond to the actual files
`freeze_manifest.md`, `audit_recurrence.py`, and `defect_recurrence.md`; all
supplied hashes match exactly.  M124's independent frozen checksum set also
passes.

## 3. Independent algebraic audit

Fix indexed cycle lengths `a_i` and a nonempty atom set `S`.

1. In a one-colour set partition, the block containing a fixed root atom is
   unique.  Removing it leaves an arbitrary partition of its complement and
   preserves both the product weight and block count.  Hence

   ```text
   P_S(y)=y sum_(root in B subseteq S)w(B)P_(S-B)(y).
   ```

2. For an ordered pair `(pi_L,pi_R)`, the blocks of
   `pi_L join pi_R` decompose the object uniquely.  Selecting the join
   component containing a fixed root gives

   ```text
   A_S=sum_(root in U subseteq S)C_U A_(S-U),
   C_S=A_S-sum_(proper root-containing U)C_U A_(S-U).
   ```

   The block weights and both colour block counts factor across these join
   components, so no correction factor is missing.

3. The bipartite incidence multigraph has one vertex for every left or right
   partition block and one labelled edge for every cycle atom.  Its connected
   components are exactly the join components.  Thus join-indiscreteness is
   connectedness.  On the coefficient diagonal `L+R=c`, the connected graph
   has `E=c=V` and therefore cyclomatic number `E-V+1=1`, exactly the required
   connected-unicyclic condition, including parallel-edge cases.

4. For a cycle type with `c` cycles and a diagonal term with `R=c-L`, the
   accepted key identity gives

   ```text
   j=d+R-L=d+c-2L,
   2d-j=d-c+2L.
   ```

   Multiplication by the standard cycle-type count
   `d!/product_s(s^m_s m_s!)`, the squared atom factors, and the two cut
   factorials therefore yields M125's formula (4.1).  Indexing the actual
   cycles introduces no extra `c!`: for each fixed permutation its cycle set
   is partitioned once, while the cycle-type factor counts the permutations.

5. Both partition colours are nonempty, so `L,R>=1`.  The diagonal
   `L+R=c` therefore has no `c=1` term.  This proves the repaired defect range
   `0<=r<=d-2`; at `d=2` the sole row is exactly `[1]`.

6. With a root atom of size type `q`, the number of indexed root-containing
   subsets having submultiset `b` is exactly

   ```text
   binom(nu_q-1,b_q-1) product_(i!=q)binom(nu_i,b_i).
   ```

   Grouping the two rooted recurrences by these submultisets proves M125's
   optimized engine.  The choice of which present type supplies the root is
   immaterial; the clean-room implementation deliberately uses the largest
   present size, whereas M125 uses the smallest present size.

No algebraic mismatch or unstated multiplicity was found.

## 4. Clean-room exact audit

`independent_referee.py` imports no M125 code.  It separately implements:

- literal enumeration of ordered pairs of set partitions;
- an indexed-subset recurrence rooted at the greatest indexed atom;
- a multiset recurrence rooted at the largest present cycle size.

All arithmetic is exact `fractions.Fraction` arithmetic and the computation is
deterministic (`seed=null`).  The final run has zero failures:

- all 23 eligible cycle types through `d=6` were tested by literal partition
  enumeration, totaling 47,728 ordered partition pairs;
- indexed and multiset recurrences agree for all 58 eligible cycle types
  through `d=8`;
- the independently constructed rows agree with M124's exact-key rows at
  `d=2,3,4,5`;
- every complete row through `d=22` agrees exactly with frozen M125 output;
- every row `2<=d<=22` is unimodal and ordinarily log-concave;
- every tested row `4<=d<=22` fails ULC.

At `d=4`, the independently recovered primitive row is

```text
(627,1520,1113).
```

The exact margins are

```text
1520^2-627*1113   = 1612549 > 0,
1520^2-4*627*1113 = -481004 < 0.
```

Thus the ordinary inequality survives while ULC is rigorously refuted.  The
second expression is also the discriminant of
`627+1520*x+1113*x^2`, so that exact defect polynomial is not real-rooted.

The weakest ordinary log-concavity ratio among the tested rows occurs at
`(d,r)=(22,7)` and is

```text
203052727873585698084872170325683069756137900805646142215266400921718635527268446717542400
------------------------------------------------------------------------------------------
200683584169771483317004240708824213678414395853532844345497564768651541950121298843365859
```

which is approximately `1.0118053687032518`, exactly matching M125.

## 5. Numbered objections

1. **None.**  No material or minor mathematical, computational, provenance,
   or scope objection survives the fresh audit.

## 6. Scope guard and action

The exact finite signs do not prove the universal coefficient inequality

```text
H[d,c]^2 >= H[d,c-1]H[d,c+1].
```

M125 correctly labels that statement and DEFECT NO-VALLEY unresolved.  Its
warning is also justified: the connected extraction is subtractive and the
failed ULC/real-rooted strengthening cannot supply the desired positivity.

**Action:** accept M125's recurrence reduction and exact `d=4` ULC
counterexample into the coordinator ledger.  Retain the finite `d<=22`
ordinary log-concavity/unimodality only as an exact finite fact.  Do not infer
a defect-projection gap, `gap(A_d)`, a handle-projection gap, or a gap for the
original heat-bath chain.

## 7. Reproduction and provenance

From the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-27/mission-M129-m125-fresh-referee/independent_referee.py \
  --max-d 22 --direct-max-d 6 --recurrence-compare-max-d 8 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-27/mission-M129-m125-fresh-referee/independent_results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, deterministic `seed=null`.

Fresh artifact hashes before report freeze:

| artifact | SHA-256 |
|---|---|
| `independent_referee.py` | `c9e473ec62b78a0e37fc59211877d8a017327fc625ebdfdf2b8899f7714839b4` |
| `independent_results.json` | `96a880122c2a745fe7032d90442ddfcb2ed762d0723345e47630f76cc7604fee` |

Reference hashes recorded by the fresh checker:

| reference | SHA-256 |
|---|---|
| M125 `exact_results.json` | `01938aab9d001597991d13efb3dd0583d61b629c776cfcd2f4ccfde023588131` |
| M124 `results.json` | `36b898a0f987d7df114a0c9ef4cb433441f114f1fe3d03495b9cc88152163553` |
