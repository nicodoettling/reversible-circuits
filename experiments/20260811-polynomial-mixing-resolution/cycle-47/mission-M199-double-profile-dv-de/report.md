# M199 report: literal double-profile reduction

Date: 2026-08-13 UTC. Commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and scope

```text
STRICT EXACT PROFILE REDUCTION.
IKBE, DV, DE, CONDITIONAL J2 PREFIX, AND DOWNSTREAM: OPEN.
```

Target: uniform minimal factorizations under the fixed-cell nonlazy cyclic
rank-two kernel, `n=3k`, odd `k>=3`, with `(pq)(x)=p(q(x))`.

## 2. Immutable gate

All M174/M178/M180/M182/M186/M189/M192/M195 manifest entries passed; none
was edited. The accepted input is M192/M195's literal disjoint laws.

## 3. Exact normalization

```text
R_*=2k-3,  K_*(r,d)=b_d b_(r-d)/(R_* b_r).
```
`R_*` is total exterior rank after the first factor, not initial rank
`2k-2` or post-second rank `2k-4`. It is the per-placement second-edge
denominator. Fresh audit of this point is requested.

## 4. Literal B formula

Every B disjoint pair is uniquely indexed by first start `i`, marked piece
`r in {s,2k-1-s}`, second split `d`, and offset
`1<=a<=r-d-1`. Its conditional mass is
`K_*(r,d)/[(2k-1)(1-gamma_L(s))]`. Exact seam indicators give both one-run
faces and their complementary two-run face, retaining all kinds/collisions.

## 5. Literal A formula

There are `2k` first A chords of split `s`. Summing
`K_*(r_e(f),d_e(f)) chi_l^Z(e,f)` over nonincident second edges and dividing
by `2k(1-gamma_F(s))` gives the full profile. The untouched cycle has exact
mass `(k-1)/(2k-3)`.

## 6. Open IKBE

The `s -> s+1` map has four exact edits: added boundary placements, deleted
placements, kernel/seam Radon--Nikodym edit, and gamma normalization. The
remaining lemma is
```text
sum_s sqrt(s)|Phi_(s+1)^D(Z)-Phi_s^D(Z)| <= C sqrt(l),
|Phi_s^D(Z)-Psi_s^D(Z)| <= C sqrt(l)/k.
```
The first clause is DV; the second implies DE after `q_hat` averaging.
Neither is proved.

## 7. Exact diagnostics

The standard-library checker, capped at `k=3,5,7,9`, passes 540 assertions.
Maximum finite DV ratios at `k=9` are 1.2428 (X) and 1.3331 (Y); maximum
pointwise embedding ratio is 1.0051. These imply no universal result.

## 8. Open obligations

1. Prove/refute the combined boundary edit.
2. Prove/refute the seam/marked/untouched embedding estimate.
3. Fresh-audit denominator, face orientation, untouched mass, collisions, and
   IKBE implication.

## 9. Artifacts and action

Artifacts: plan/checkpoint, `double_profile_reduction.md`, checker/results,
summary, report, and freeze files. Python 3.12.3, standard library, seed null.
Freeze only this reduction; keep IKBE/DV/DE and downstream open.
