# M183 mathematical audit notes

Date: 2026-08-13 UTC.

## 1. Core relation and reverse conjugation

The clean-room implementation reconstructed the chronological four-move word
on

```text
U=(01)^2(02)^2(03)^2,       V=(01)^2(02)^2(13)^2.
```

Unique transporter recovery gives `(23)` and `(01)(23)`.  At the post-base
pair, the displayed factor-position expression

```text
I=(1,3,1,3,5,3,5,3,5,1,3,1)
```

multiplies to `(id,(01)(23))`.  Independently applying the elementary word
`E_j` at every `j=1,...,6` on both coordinates verifies
`E_j X=x_j^(-1)Xx_j` in all twelve cases.

The order reversal is correct.  If the current state is `q^(-1)Xq`, its
factor at position `j` is `q^(-1)x_jq`; applying `E_j` changes the state to
`(x_jq)^(-1)X(x_jq)`.  Therefore applying the `E_j` in reverse expression
order accumulates the original product `p=x_(I_1)...x_(I_12)`.  All twenty-
four coordinate-prefix identities were checked directly.  The correction
has length `196`, the full relation length `200`, and the final transporters
are `(23),id`, with signs `1,0` and common anchor fixed.

The independently reconstructed relation-list digest is

```text
32f90842f682615a72def42e0f940d9125a719ed8b38e9375fe1d81fa5e50629
```

and matches the literal list frozen in M181 `results.json`.

## 2. All-label minimal embedding

For `r=floor((d-1)/3)` and `t=d-1-3r`, each of the `r` six-factor blocks is
three adjacent doubled edges, and each of the `t` fillers is `(0x)^2`.
Thus the product is identity and the length is

```text
6r+2t=2d-2.
```

In a `U` block every nonanchor label is adjacent to `0`; in a `V` block the
third label connects through `a`; filler labels attach directly to `0`.
The support is therefore connected on all `d` labels.  A shifted local word
uses only the five generator indices internal to its six positions.  Its odd
transporter `(b_k c_k)` fixes anchor `0`, every other block label, and every
filler label, proving the endpoint is a relabeling of the entire word.

The clean-room rows at `d=5,7,10` cover one filler pair, no filler with two
blocks, and even tuple width four.  All direct endpoint and outside-block
checks pass.

## 3. Distinct quotient patterns

If two selected patterns differ in block `k`, one word has local last edge
`{0,c_k}` and the other has `{a_k,c_k}`.  Equality at local positions one
and three first maps `{0,a_k}` and `{0,b_k}` to themselves.  Their unique
intersection forces `rho(0)=0`, then `rho(a_k)=a_k` and `rho(b_k)=b_k`.
The last-edge equality is impossible because `{0,rho(c_k)}` cannot equal
`{a_k,c_k}`.  This argument is symmetric and independent of `d`; positionwise
word equality prevents block permutation.  Exhaustive checks at `d=5,7`
agree.

## 4. Voltage basis, including even width

On the ordered patterns `0,e_1,...,e_(s-1)`, the `k`th shifted relation has
sign representative with coordinate zero equal to zero and a single one in
coordinate `k`.  If a linear combination of these representatives belongs
to `Delta`, its zero coordinate forces the diagonal bit to be zero, after
which every coefficient is zero.  Hence their quotient classes have rank
`s-1=dim W_s` for both parities of `s`.

The warning about edge vectors is also exact.  A connected graph's vectors
`e_i+e_j` span the even-weight space `E`.  For odd `s`, `Delta` is not in
`E`, so its image fills `W_s`; for even `s`, `Delta<=E`, so the image has
dimension `s-2`.  Clean-room ranks for `s=2,...,6` are respectively
`0,2,2,4,4` for path-edge classes versus `1,2,3,4,5` for the constructed
single-coordinate classes.

## 5. Inclusion in every perfect-matching color

M135 defines one edge for each `H`-orbit in `Z_d`, with left endpoint its
containing global `G`-orbit.  A perfect matching therefore supplies exactly
one edge `Q_c` over each constructed distinct left quotient point—not the
literal gadget word.  Choosing any `u_c in Q_c` gives
`u_c=alpha_c.W_c` for some `alpha_c in G`, with no reason to require
`alpha_c in H`.

Hurwitz action is coordinatewise `G`-equivariant.  Consequently a source
stabilizer relation with transporter `delta_(c,k)` becomes one with
transporter `alpha_c delta_(c,k) alpha_c^(-1)` on `u_c`; its sign is
unchanged.  Independent tests used different cyclic `alpha_c` in each
coordinate and generally moved the anchor.  Every endpoint and sign passed.
The right endpoints are pairwise distinct solely because the selected edges
belong to a matching.  This is precisely the hypothesis needed by the
accepted M169 interface.

## 6. Endpoint and exact-sequence scope

Full source voltage implies the M175 chord space equals all of `W_s`.  If,
and only if, the matched quotient target lies in the source synchronized
component, its fixed-endpoint tree offset is defined in `W_s` and therefore
belongs to that chord space.  M175 then gives a zero-voltage quotient route.
M181 states this implication conditionally and never infers quotient
connectivity from stabilizer rank.

M169 gives

```text
K_mon(q)=relative_sign^(-1)(V_stab(q)).
```

Thus `V_stab(q)=W_s` does imply `K_mon(q)=S_d^s` at the source, but supplies
neither the target quotient route nor a quantitative word bound.

## Numbered objections

**None.**  No material logical, computational, provenance, or scope objection
survives the independent checks.
