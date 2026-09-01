# M300 report: all-middle channel-one pairing

Date: 2026-08-14 UTC.

## Verdict

```text
KEEP AND FREEZE THE EXACT MIDDLE CUT-LENGTH AND EXTERIOR HAHN--ABEL
REDUCTIONS.

MCLP_1 SURVIVES THE SOLE EXACT k=7 FALSIFIER BUT IS UNRESOLVED.
GOCI_1, GOCI_2, OCI/CP, OS+, MS, FCL1, GAP, MIXING, AND TERMINALS
REMAIN UNRESOLVED.
```

This mission concerns only the first separated fixed cell of the auxiliary
uniform minimal long-cycle factorization law under the nonlazy cyclic
rank-two quotient kernel, for odd `k>=3`, `n=3k`, and
`(pq)(x)=p(q(x))`. It is not a direct theorem about the global uniform
identity-word law or the lazy exact `{3,4,5}` heat-bath chain.

## 1. Immutable dependency gate

All payloads in the required frozen M274/M277, M280/M283, M285/M287, and
M295/M298 inventories pass. Their eight top checksum digests are recorded in
`dependency_audit.md`. The inherited status is unchanged: the exact
owner-correlation formulas are accepted, fixed-middle positivity and signed
PSD dominance are refuted only in their named senses, and GOCI/OCI remains
open.

The scalar shorthand

```text
beta_1(ef)=gamma_k(e)nu_M(f)
```

is retained only for the designated exterior/middle channel-one
decomposition. The controlling collision-safe identity is

```text
eta_1(F_ell)
 =sum_(f in T(M))nu_M(f)sum_e gamma_k(e)F_ell(ef).            (1)
```

Unrestricted rank-two doubles still have two ordered lifts; channel one has
already conditioned/summed its commuting color orders.

## 2. Exact middle cut-length phase reduction

For middle vertices `m_a=k+a`, oddness of `k` uniquely partitions every
unordered chord as

```text
f_(a,u)={m_a,m_(a+u)},       a in Z/kZ, 1<=u<k/2.
```

The per-chord class weight is

```text
w_(k,u)=tau(u)tau(k-u)/[(k-1)tau(k)]>0.
```

With

```text
P_(k,ell)(u)
 =sum_(a in Z/kZ)sum_e gamma_k(e)F_ell(e f_(a,u)),
```

equation `(1)` becomes exactly

```text
eta_1(F_ell)=sum_(1<=u<k/2)w_(k,u)P_(k,ell)(u).               (2)
```

The frozen candidate

```text
(MCLP_1) P_(k,ell)(u)>=0
```

therefore implies `(GOCI_1)`. It is strictly weaker than the refuted
fixed-middle candidate because all `k` middle phases are combined before a
sign is requested. It is not atomwise positivity, conditioned MON/FOSD, or
signed PSD.

## 3. Complete exterior Hahn decomposition

Let `D=2k-1`, `A={1,...,k-1}`, and
`P={2k,...,3k-1}`. The exact signs of the complete exterior coefficient are:

```text
A-to-P cross chord:        gamma=nu_D>0,
seam chord {0,c}:          gamma=-nu_k(c)/2<0,
chord internal to A or P:  gamma=nu_D(c)-nu_k(c)/2<0.
```

The last sign follows at every rank from the strict decrease of
`tau(d-1)/tau(d)`. This is a complete Hahn support theorem: exactly
`k(k-1)` exterior chords are positive and exactly `k(k-1)` are negative,
with equal total masses but unequal atom weights.

For a fixed middle class, average the response over all its phases. Group
positive cross chords and negative internal/seam chords by the canonical
`L` cut `c`. If their corresponding normalized response means are
`Xbar_c,Ybar_c`, define

```text
x_c=2c v_D(c),
y_c=(k-c)v_k(c)-(D-2c)v_D(c)>0,
r_c=x_c-y_c=Dv_D(c)-(k-c)v_k(c),
R_c=sum_(d<=c)r_d.
```

Then `R_(k-1)=0` and exact summation by parts gives

```text
P_(k,ell)(u)
 =sum_(c=1)^(k-1)y_c(Xbar_c-Ybar_c)
  +sum_(c=1)^(k-2)R_c(Xbar_c-Xbar_(c+1)).            (EHA_1)
```

`proof.md` defines every mean and proves all coefficients. This reduces the
signed sum over `2k(k-1)` exterior atoms to a combined inequality over
`2(k-1)` fully middle-averaged cut means.

The reduction does not itself prove a sign. Already at `k=7`, the exact
`R_c` are negative through `c=3` and positive at `c=4,5` before returning
to zero. Hence no one-direction successive-cut Abel certificate closes the
formula. The first unresolved lemma is the nonnegativity of the literal
combined right side of `(EHA_1)`.

## 4. Sole exact falsifier: `k=7`

The predeclared standard-library checker used exactly `k=7`, `n=21`, all
three middle cut classes, all seven phases per class, and all eighteen
admissible lags. It imports no predecessor code or data.

Every one of the 54 class/lag totals is strictly positive. The minimum is at
`u=2`, reflected lags `ell=6,15`:

```text
18391884160007872512505581390057340062886183764340384475832641580678550316483694546164031922299480179423171
/181211325370827177616731812976270118138716435331141156018616780003928170444373248989640785920000000000000000
approximately 0.1014941208689418.
```

This class positivity is genuinely cross-middle: 44 of 378 fixed-middle
cells are negative. Their exact minimum is at `u=2`, phase `6`,
`f=(8,13)`, and `ell=8,13`, approximately `-0.05202816554946053`.

Every complete `eta_1(F_ell)` is positive at this rank; the minimum is
approximately `0.02016735366799382` at `ell=8,13`. These are finite facts,
not an all-rank theorem.

The checker verifies chord-law/gamma normalization, the unique class
partition and positive weights, literal equals repaired response, exact
state/class/full reflection, and equality of direct and class-reconstructed
full averages. A second run reproduced both JSON outputs byte-for-byte:

```text
mclp_k7.json            314252c8e3a89bc024e6963da33c606b65edbd869ff6228c8058d930d0989660
exterior_abel_k7.json   c15b11102eee06c7467a3b6154e0c1c9262e33f01c72928fd9601adf628e83a8
```

## 5. Exact status and action

| Claim | Status | Evidence | Action |
|---|---|---|---|
| designated channel-one disintegration `(1)` | proved | direct normalized-law expansion | retain with lift qualifier |
| unique middle cut-class decomposition `(2)` | proved | odd-`k` chord partition | retain |
| complete exterior Hahn support | proved | ratio monotonicity and exhaustive support split | retain |
| exterior Hahn--Abel identity `(EHA_1)` | proved | exact mass counts and summation by parts | retain |
| universal `(MCLP_1)` | unresolved | no all-rank sign proof/counterexample | fresh audit the reduction only |
| all 54 `k=7` MCLP cells positive | exact finite only | `mclp_k7.json` | do not extrapolate |
| 44/378 `k=7` fixed-middle cells negative | exact finite only | same artifact | retain cancellation warning |
| `(GOCI_1)` / `(GOCI_2)` | unresolved | MCLP not proved; channel two lacks factorization `(1)` | remain open |
| CP/OS+/MS/FCL1, gap, mixing, Terminal | unresolved | no downstream theorem | no inference |

Final action: **freeze the exact middle cut-class and exterior Hahn--Abel
reductions for fresh immutable audit; keep `(MCLP_1)` and `(GOCI_1)` open.**

No statement is made about channel two because its two-factor completion law
does not share channel one's independent exterior/middle disintegration.
Main-chain exceptional cases `m` odd, `m=0`, `m=2`, and `N=2` are outside
this already-reduced auxiliary-cell scope.
