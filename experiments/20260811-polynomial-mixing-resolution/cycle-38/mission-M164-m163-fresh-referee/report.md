# M164 fresh referee report on frozen M163

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision, objections, and exact scope

```text
FINAL DECISION: ACCEPT M163 AT ITS EXACT NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M163 correctly proves the groupoid parity cocycle, the intrinsic stabilizer-
voltage subgroup, and the exactly oriented endpoint route-voltage coset. Its
zero criterion retains the necessary fixed-section/fixed-physical-endpoint
caveat. Accepted M154 inner `P_(d,s)` correction loops correctly contribute
only zero relative voltage. The stated `d=3` and accepted-witness `d=4`
facts were independently reproduced.

```text
candidate                  | stabilizer-voltage affine-coset reduction
claimed target             | diagonal literal signed-Hurwitz orbit lifting
identity ok                | Hurwitz and relabeling preserve product one
crosses Hurwitz components | not applicable; this classifies action orbits
exact diagnostics          | complete d3 widths 1..4; accepted d4 witness/block
verdict                    | accept strict qualitative reduction only
```

No `d>=5` full-voltage theorem, source-to-target quotient route, polynomial
braid length, short inner correction, physical-sector gap, original
`{3,4,5}` heat-bath gap, Terminal A, or Terminal B conclusion follows.

## Field 2 — immutable provenance

All assigned SHA-256 values matched before the proof audit. M163's own
`SHA256SUMS` also verified all seven payload files. No frozen M163 code was
imported, executed, or modified.

| frozen M163 artifact | observed SHA-256 |
|---|---|
| `report.md` | `ff5f33859a3ff57d6e60bac3a1efaf535c2420839400bea4061916de812e3a7a` |
| `proof.md` | `c151e4b4d986472f46b2a5b32598b665d30496fc7e8df31764b6b2695269b79e` |
| `stabilizer_voltage_audit.py` | `ebae09e2065627687468e89388b5768d1bc3320fb927a4936755c406be746614` |
| `results.json` | `01026b59612f1ec27394a5c068aded3ad35456b548af8d8a445b98b5f6fbab2e` |
| `freeze_manifest.md` | `128dc9a5ad79764c0556b4928586f8f896bfca9ac6a8e23253ee18b44ac8b95e` |
| `SHA256SUMS` | `7a235dd5246182375166fc63ab067728c8129191e86640a411156709f55de62a` |

## Field 3 — target, freeness, and conventions

For `d>=3`, let `Z_d` be the connected product-one length-`2d-2`
transposition words and `Q_d=Z_d/S_d`. Connected edge transpositions
generate `S_d`; a simultaneous relabeler fixing a word therefore centralizes
`S_d`, and is the identity because `Z(S_d)=1`. Thus the `S_d` action is
free.

For width `s`,

```text
X=Z_d^s,  Y=Q_d^s,  N=S_d^s,
W_s=F_2^s/Delta,  Delta=<(1,...,1)>.
```

The braid group acts diagonally on `X`, the deck group `N` acts
coordinatewise, and the actions commute. Products use M163's left-action
convention: in `b_2 b_1`, `b_1` acts first.

## Field 4 — cocycle and stabilizer image

For a section `sigma:Y->X`, freeness gives the unique transporter

```text
b sigma(q)=c(b,q) sigma(bq).
```

Commutation gives the nonabelian reverse-order formula

```text
c(b_2b_1,q)=c(b_1,q)c(b_2,b_1q).
```

Coordinatewise parity abelianizes this order, so

```text
nu(b_2b_1,q)=nu(b_1,q)+nu(b_2,b_1q) in W_s.
```

On `B_q={h:hq=q}`, this is a homomorphism to the abelian group `W_s`.
Its image `V_stab(q)` is therefore a subgroup. Equivalently it is the set
of relative parities of the unique physical transporters for literal quotient
loops. This establishes the intrinsic stabilizer characterization without
closing a full quotient permutation group.

## Field 5 — endpoint coset orientation and zero criterion

If `b_0q=r`, every other route is uniquely

```text
b=b_0h,  h in B_q,
```

not `hb_0`, under the stated left-action convention. Hence

```text
nu(b_0h,q)=nu(h,q)+nu(b_0,q)
```

and the route-voltage set is exactly

```text
nu(b_0,q)+V_stab(q).
```

In a general abelian voltage group, zero membership would require
`-nu(b_0,q) in V_stab(q)`; here `W_s` has exponent two, so this is exactly
M163's criterion `nu(b_0,q) in V_stab(q)`. Conjugation by `b_0` identifies
the source and target stabilizers, and the inverse cocycle identity shows
their voltage images agree in the fixed `W_s`.

## Field 6 — section/base-lift caveat and physical endpoints

If `sigma'(q)=a(q)sigma(q)`, direct substitution gives

```text
c'(b,q)=a(q)c(b,q)a(bq)^(-1),
nu'(b,q)=alpha(q)+nu(b,q)+alpha(bq).
```

For a loop, the endpoint terms cancel, proving that `V_stab(q)` is
section-independent. For a route `q->r`, the affine coset is translated by
`alpha(q)+alpha(r)`; bare zero membership is therefore not invariant under
arbitrary independent endpoint-lift changes.

For fixed physical lifts `x=n_x sigma(q)` and `y=n_y sigma(r)`,
`bx=y` is equivalent to `c(b,q)=n_x^(-1)n_y`. The corresponding parity
condition changes by precisely the same coboundary, so the physical criterion
is intrinsic. Applying the same coordinatewise relabeler to both endpoints
conjugates the literal transporter and preserves its parity, as M163 states.

## Field 7 — why accepted inner loops have zero voltage

Accepted M154 realizes aligned simultaneous conjugation by every element of
the aligned factor-generated group. Accepted M141/M143 identifies that group,
for the stated `d>=5` M135 subfamilies, as

```text
P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

Every element has diagonal parity and hence zero image in
`F_2^s/Delta`. These quotient loops lie in `ker(nu)`; they cannot supply a
nonzero voltage adjustment. After a quotient route has zero relative voltage,
they can remove its remaining `P_(d,s)` transporter qualitatively. M141
generation supplies no polynomial bound on the aligned word length.

## Field 8 — independent exact `d=3` and `d=4` reconstruction

The clean-room checker imports or executes no predecessor code. It implements
permutation composition, relabeling, signed Hurwitz moves, quotient
canonicalization, unique transporter parity, augmented tuple orbits, and the
`S_4/V_4` perfect-matching projection independently.

At `d=3` it reconstructed

```text
|Z_3|=24,  |Q_3|=4,  positive quotient image order=12,
all positive quotient generators even.
```

All inverse-edge and all two-signed-generator cocycle checks had zero
failures. Exhaustion of `4+16+64+256=340` ordered quotient tuples at widths
one through four found `V_stab={0}` for every tuple.

At `d=4` it reconstructed

```text
|Z_4|=2880,  |Q_4|=120,
40 S_4/V_4 fibers of size 3,  zero signed-action block failures.
```

The accepted witness had the same indices `(28,35)` and `(56,62)` under
the clean-room lexicographic canonicalization. Its source and target
quotient/augmented orbit sizes were respectively `240/240` and
`9720/9720`, so both stabilizer voltages are trivial. The source-to-target
route-voltage set was empty. The source pair has equal block labels, the
target pair unequal labels, and the independently closed paired subgroup
orders were `96` and `288`. Thus this witness fails before any endpoint
voltage coset exists.

These are exact finite facts only. They imply nothing at `d>=5`.

## Field 9 — unresolved lemma, reproduction, and hygiene

M163's first unresolved qualitative question remains:

> For accepted ordered M135 matching subfamilies at every `d>=5`, determine
> whether `V_stab(q)=F_2^s/Delta`; if not, determine whether the particular
> fixed-endpoint source-to-target voltage coset nevertheless contains zero.

Even a positive answer would leave quotient-route length and aligned inner-
transporter length unresolved.

Deterministic reproduction from this directory, Python `3.12.3`,
`seed=null`:

```text
python3 -B independent_referee.py
```

The checker reads frozen M163 bytes only for hash verification. It uses no
network and no stochastic branch. Owned artifacts are `plan.md`,
`checkpoint.md`, `independent_referee.py`, `independent_results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No M163, predecessor,
coordinator, manuscript, skill, or other mission file was edited.

```text
ACCEPT. ZERO MATERIAL NUMBERED OBJECTIONS.
PROMOTE ONLY THE QUALITATIVE STABILIZER-COSET REDUCTION AND EXACT d3/d4 FACTS.
KEEP d>=5 FULL VOLTAGE, ROUTING, WORD LENGTH, AND EVERY GAP CLAIM UNRESOLVED.
```
