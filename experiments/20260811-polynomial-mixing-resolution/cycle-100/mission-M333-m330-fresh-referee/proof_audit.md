# M333 independent proof audit

Date: 2026-08-14 UTC

## 1. Exact A fiber

Fix only

```text
k=7, n=21, row H_2, (s,t)=(1,1),
Sigma={0,1,6,14,20},
fixed B prefix e=(6,14), f=(3,5).
```

For an A raw atom with profile `P`, M330 assigns the residual mass

```text
a(P) Pr[xi_A | s=1,P]
=a(P) (raw conditional marked mass)/(A marked mass of P).
```

It retains the raw slots before summing over those whose marked-owner support
and support heads both miss `Sigma`. Thus its `N_A` is exactly the
non-Touch A endpoint mass missing from M323, not a profile-only surrogate.
The exact counts are

```text
split-one A prefixes                    1092
raw marked A slots                      3276
positive-residual A slots               3056
positive-residual non-Touch A slots      590
```

and

```text
N_A=2037915313150409615825963
    /288085426550809623412604928 > 0.
```

## 2. First A atom

The first non-Touch positive-residual atom in frozen order is channel 2,
split 1, `e=(3,4)`, `f=(4,5)`, slot 1, owner size 1, empty
marked-owner support, heads `{2,3,4}`, and the all-zero 17-coordinate
profile. Both support sets miss `Sigma`.

Its exact disintegration is

```text
completion ratio                 59379122092290000/81435568248417631248
raw unconditional prefix mass    625/857157
q_1                              1296/2401
raw conditional marked mass      625/462672
A marked mass of profile 0        176355146/69429717
a(0)                             1703889405470479/77788224253329408
Pr[xi_A|1,0]                     1500625/2821682336
residual atom mass               1064930878419049375/91417600301718608805888
```

Indeed, `(625/857157)/(1296/2401)=625/462672`; disintegrating by
the profile marked mass and multiplying by `a(0)` gives the displayed
strictly positive residual mass.

## 3. Fixed B atom and rank obstruction

M323's B atom has slot 1, marked-owner support `{3}`, and heads
`{2,4,5,13}`. Both miss `Sigma`, so it is non-Touch. Its edge
`(6,14)` touching the seam is immaterial because frozen `Touch_Sigma`
tests only marked-owner support and support heads.

The B source accepts the prefix with ranks `18->17->16`. For the
opposite A source, `(6,14)` joins the exterior cycles and `(3,5)`
then cuts, so the ranks are

```text
18 -> 19 -> 18.
```

The required two decreases fail; the switched opposite-A raw prefix is
absent. Frozen `S_pf` is therefore undefined on any token carrying this B
atom.

The remaining exact factors are

```text
b(Q)=21484375/54238159872
Pr[eta_B|1,Q]=1/2
c_H=46/17
pi_(1,1)=61917364224/137858491849
rho_(1,1)=49168032837363259/1633552709319917568.
```

## 4. Product-token conclusion

The first A atom paired with the fixed B atom has exact mass

```text
(c_H pi_(1,1)/rho_(1,1))
 [a(P)Pr(xi_A|1,P)] [b(Q)Pr(eta_B|1,Q)]
=65802548799959422226562500000
 /706358481579483924710894769596909369 > 0.
```

The full fixed-B/nonTouch-A mass is

```text
119877371361788800930939000000000
/2119075444738451774132684308790728107 > 0.
```

Because
`Exc_pf(omega)=Touch_Sigma(xi_A) or Touch_Sigma(eta_B)`, both
disjuncts are false on the displayed token. It lies outside `Exc_pf`, but
the B rank obstruction makes `S_pf` undefined. Hence M323 plus M330
establishes an actual off-`Exc_pf` failure of the frozen `S_pf` in this
one finite cell and exactly discharges M326's sole material objection.

This proves no compatible coboundary, reverse landing, enlarged-exception
estimate, Borel bound, MPCF statement, sampler statement, or downstream
inference. It says nothing about another cell, row, rank, or surgery.
