# M125 halfway checkpoint

Date: 2026-08-12 UTC.

## Exact status

The target remains the unnormalized auxiliary defect mass

```text
M[d,r] = sum_{R(kappa)=r} |C_kappa|,
R(kappa)=d-c(p),
```

for M113/M118's `rho` law on connected-unicyclic incidence keys.  No claim
about the original word law is being made.

I derived an exact permutation-cycle / incidence-species recurrence that
avoids enumerating permutations, transposition words, or pairs of set
partitions.  Fix an indexed list of cycle lengths `a=(a_1,...,a_c)`.  For a
nonempty atom set `S`, put

```text
w(S) = (sum_{i in S} a_i)^(|S|-3),
P_S(y) = sum_{pi partition of S} y^|pi| product_{B in pi} w(B).
```

Choosing the block containing the least atom gives the exact subset
recurrence

```text
P_empty(y)=1,
P_S(y)=y sum_{B subset S, root in B} w(B) P_{S-B}(y).
```

Let `A_S(y,z)=P_S(y)P_S(z)`.  A pair of colored partitions decomposes
uniquely as a labeled set of connected components of its join.  If `C_S`
is the connected-pair polynomial, selecting the component containing the
least atom gives

```text
A_S(y,z)=sum_{U subset S, root in U} C_U(y,z) A_{S-U}(y,z),
C_S=A_S-sum_{proper U subset S, root in U} C_U A_{S-U}.       (H)
```

On the diagonal `L+R=c`, connectedness means that the bipartite incidence
multigraph has `c` edges and `c` vertices, hence is exactly connected and
unicyclic.  Therefore, for an integer cycle type `lambda=(a_1,...,a_c)` of
`d`, with `m_s` parts of size `s`, the exact contribution is

```text
d!/[product_s s^m_s m_s!]
* product_i [a_i^a_i/(a_i-1)!]^2
* sum_{L=1}^{c-1}
    (d+c-2L)! (d-c+2L)! [y^L z^(c-L)] C_[c](y,z).     (M)
```

Summing (M) over cycle types with `c=d-r` gives `M[d,r]`.  This is already a
proved standalone coefficient recurrence, subject only to writing the full
derivation cleanly in the final proof note.

## Exact cross-checks

The deterministic rational-arithmetic implementation `defect_species.py`
reproduces the frozen `d<=5` masses and both coordinator stress rows exactly
up to their common gcd:

```text
d=2: [1]
d=3: [3, 4]
d=4: [627, 1520, 1113]
d=5: [1482, 4775, 6525, 3388]
d=6: [9139662, 33979680, 63794575, 62828640, 25565795]
d=7: [38271780, 151229400, 340051475, 470006334, 366720025, 123380706]
```

All six rows are unimodal and log-concave.  This remains finite evidence.

## First rigorous obstruction

The natural ultra-log-concavity strengthening is already false at `d=4`.
Writing `a=(627,1520,1113)` and dividing by the binomial row `(1,2,1)` gives
`(627,760,1113)`, for which

```text
760^2 = 577600 < 697851 = 627*1113.
```

Equivalently, after clearing the common raw-mass scale, the ULC margin is
negative.  Thus neither real-rootedness (already known false at `d=4`) nor
the standard ULC route can prove the desired ordinary log-concavity.

## Remaining work and obstruction

The recurrence (H)--(M) has positive block weights but its connected
extraction is subtractive.  I do not yet have a preservation theorem showing
that summing its cycle-type rows yields a log-concave defect sequence.  I will
now (i) repair and freeze the executable after a boundary-case bug for the
excluded one-cycle type, (ii) push the exact recurrence beyond `d=7` to hunt
for an ordinary log-concavity counterexample, and (iii) test whether a weaker
ratio or coefficient recurrence admits a universal proof.  If universal
no-valley remains open, the final deliverable will promote (H)--(M), refute
ULC exactly, and state the first remaining coefficient inequality without
extrapolating from finite `d`.

Even a future proof of DEFECT NO-VALLEY yields only M120's defect-projection
gap.  It does not prove the fixed-defect two-step gap, `gap(A_d)`, or the
terminal heat-bath mixing result.

## Resumed checkpoint — 2026-08-13 UTC

The current filesystem was reconciled against L-0230/L-0231 and the complete
frozen M113/M118/M120/M124 payloads; all four checksum sets pass.  The
preserved core's impossible `c=1` boundary bug is repaired directly, and the
wrapper monkeypatch is removed.

The subset recurrence is now accompanied by a proved exact multiset
aggregation.  An independent checker compares it with direct pairs of set
partitions for every cycle type through `d=5`, the original subset recurrence,
the frozen M124 raw rows, and the primitive `d=6,7` stress rows.  All checks
pass.  Exact coefficient rows extend through `d=22`: all are unimodal and
ordinarily log-concave, while ULC fails from `d=4`; these remain finite facts.

Final disposition: promote the exact coefficient reduction, preserve the
exact `d=4` ULC refutation, and keep universal ordinary log-concavity and
DEFECT NO-VALLEY unresolved.  The first explicit remaining inequality is
`H[d,c]^2>=H[d,c-1]H[d,c+1]` for `3<=c<=d-1`, with `H` defined entirely by
the frozen recurrence in `defect_recurrence.md`.
