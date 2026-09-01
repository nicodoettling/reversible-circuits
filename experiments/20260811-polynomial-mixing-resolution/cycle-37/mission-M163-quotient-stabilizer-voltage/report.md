# M163 final report: quotient stabilizer voltage

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP A PROVED STABILIZER-COSET REDUCTION AND EXACT LOW-RANK
STABILIZER RESULTS; UNIVERSAL FULL VOLTAGE REMAINS UNRESOLVED.

PROVED universally (d>=3): relative parity is a groupoid cocycle; its image
on a quotient-tuple point stabilizer is a subgroup V_stab; and all voltages
of quotient braids routing one fixed tuple to another form exactly one coset
of V_stab. A zero-voltage route exists exactly when that coset contains zero.

EXACT at d=3: every ordered quotient tuple of widths 1..4, including every
ordered distinct M135-type matching subfamily, has V_stab=0.

EXACT for the accepted d=4 witness: both endpoint tuple stabilizers have
V_stab=0, while the endpoints are already separated in the quotient by the
S_4/V_4 block invariant.

UNRESOLVED for d>=5: whether accepted M135 tuple stabilizers have full
voltage, whether the required endpoint coset contains zero, and whether
either quotient routing or inner correction has polynomial word length.
```

This mission proves no common M135 braid, broad action transitivity,
polynomial diameter, spectral gap, or Terminal conclusion.

## Field 2 — reconciled accepted inputs and immutable provenance

M154 was left byte-for-byte immutable. The mission reconciled the accepted
M135/M137 incidence and matching construction, M141/M143 common-parity
generation, M146/M148 factor-class collapse, M150/M153 reduced Pin
descriptor, and M154/M158 inner-Nielsen/voltage reduction. M158's independent
checker was hash-gated before its elementary exact combinatorial functions
were imported:

```text
0189310b6108bef9fe3b687e6131d7a70e577d523766680154e0f9b91e8c10e9
```

No predecessor file was edited. No unverified literature classification is
used.

## Field 3 — target, action, and voltage group

Let `Z_d` be the connected product-one transposition words of length
`m=2d-2`. The literal signed braid action commutes with free simultaneous
`S_d` relabeling, and `Q_d=Z_d/S_d`. For an ordered width-`s` tuple set

```text
X=Z_d^s,  Y=Q_d^s,  N=S_d^s,
W_s=F_2^s/Delta,  Delta=<(1,...,1)>.
```

One braid acts diagonally on the coordinates; `N` relabels them
independently. A section `sigma:Y->X` gives the unique deck transporter

```text
b sigma(q)=c(b,q)sigma(bq),
```

and relative parity voltage

```text
nu(b,q)=parity(c(b,q)) mod Delta in W_s.
```

Products in the proof use a left action: in `b_2 b_1`, `b_1` acts first.
The finite checker uses the accepted chronological convention
`R_j(a,b)=(b,b^-1*a*b)`.

## Field 4 — proved groupoid cocycle and stabilizer subgroup

Commutation of braid and deck actions gives

```text
c(b_2b_1,q)=c(b_1,q)c(b_2,b_1q),
nu(b_2b_1,q)=nu(b_1,q)+nu(b_2,b_1q).
```

For `B_q={h:hq=q}`, the restriction `h |-> nu(h,q)` is therefore a
homomorphism. Its image is the intrinsic subgroup

```text
V_stab(q)=nu(B_q,q)<=W_s.
```

Equivalently, for a physical lift `x` of `q`, it is the set of relative
parities of the unique transporters `rho_x(h)` satisfying
`hx=rho_x(h)x`. This characterizes `V_stab` directly via the point/tuple
stabilizer, without closing the entire quotient action group.

## Field 5 — exact endpoint-coset and zero-adjustability theorem

Assume `R(q,r)={b:bq=r}` is nonempty and fix `b_0 in R(q,r)`. Every route
has the unique form `b=b_0h`, `h in B_q`; hence

```text
{nu(b,q):b in R(q,r)} = nu(b_0,q)+V_stab(q).
```

Thus zero is adjustable precisely when `nu(b_0,q) in V_stab(q)`, or
equivalently when this affine coset contains zero. Conjugation by `b_0`
identifies source and target stabilizers and preserves their voltage images.

Under a section change `sigma'(q)=a(q)sigma(q)`,

```text
nu'(b,q)=alpha(q)+nu(b,q)+alpha(bq).
```

Therefore `V_stab(q)` is section-independent, but a route coset is
translated by arbitrary independent endpoint lift changes. Bare
zero-membership is asserted only for fixed physical endpoints; the complete
physical routing criterion transforms by the same coboundary and is
invariant. Matched simultaneous relabeling of both members of an M135 pair
also cancels.

## Field 6 — inner loops are exactly zero relative voltage

M154's explicit product-one braid loops realize conjugation by aligned
factor tuples. Accepted M141 says those tuples generate `P_(d,s)` for the
stated `d>=5` M135 subfamilies. Since every element of

```text
P_(d,s)={(g_1,...,g_s):sign(g_1)=...=sign(g_s)}
```

has diagonal parity, every such inner loop has zero class in `W_s`. It lies
in the kernel of stabilizer voltage and must not be counted as a nonzero
voltage adjustment.

The interface is consequently exact: first find a quotient route whose
affine voltage coset contains zero; only then use an inner `P_(d,s)` loop to
remove the literal transporter. Qualitative generation does not bound the
length of that correction.

## Field 7 — exhaustive rank-three stabilizer theorem

The checker reconstructed all four quotient points and the signed generator
cocycle directly from canonical physical representatives. It exhausted all
ordered tuples through the maximum distinct width:

| width `s` | all tuples | ordered distinct tuples | `V_stab` on every tuple |
|---:|---:|---:|:---|
| 1 | 4 | 4 | `0` |
| 2 | 16 | 12 | `0` |
| 3 | 64 | 24 | `0` |
| 4 | 256 | 24 | `0` |

The last column holds for all tuples, not only distinct tuples. Hence the
rank-three quotient stabilizer supplies no relative-parity adjustment at any
width. This strengthens the interpretation of M154's two framed pair
orbits: their nonzero relative framing cannot be repaired by a quotient
loop.

This is an exact finite theorem, not an asymptotic proof.

## Field 8 — accepted rank-four witness and capped rank five

For the accepted rank-four witness, the exact quotient indices are

```text
source=(28,35),  target=(56,62).
```

The source augmented orbit and quotient orbit both have size `240`; its
stabilizer voltage is trivial. The target augmented orbit and quotient orbit
both have size `9720`; its stabilizer voltage is also trivial. There is no
source-to-target quotient route. Independently evaluating the accepted
`S_4/V_4` projection gives equal block labels at the source and unequal
labels at the target. Thus this witness fails before an endpoint voltage
coset exists; it neither supports nor refutes a `d>=5` full-voltage theorem.

A preliminary `d=5` Schreier--Sims stabilizer attempt did not finish within
its bounded phase (about 100 seconds) and was interrupted without a result.
No d5 group closure was retained or claimed. Per the cap, M163 did not rerun
the already accepted M154/M158 degree-8400 quotient facts and made no d5
voltage inference.

## Field 9 — first unresolved lemma, reproduction, and hygiene

The first qualitative unresolved lemma is:

> For every `d>=5` accepted ordered M135 matching subfamily `q in Q_d^s`,
> determine whether `V_stab(q)=F_2^s/Delta`; if not, determine whether the
> particular source-to-target voltage coset nevertheless contains zero.

Even full voltage would not prove a polynomial quotient word or a short
inner transporter. Those remain separate quantitative obligations.

Deterministic reproduction from this directory, Python `3.12.3`, `seed=null`:

```text
python3 -B stabilizer_voltage_audit.py
```

The checker writes `results.json`, verifies the frozen M158 checker hash,
and contains no stochastic branch. Changed files are confined to this owned
M163 directory. No cache directory is retained.
