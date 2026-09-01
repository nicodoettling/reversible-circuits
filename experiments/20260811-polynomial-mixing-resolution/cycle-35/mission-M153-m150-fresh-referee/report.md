# M153 fresh referee report on M150

Date: 2026-08-13 UTC.

## Verdict

```text
FINAL VERDICT: ACCEPT.
NUMBERED OBJECTIONS: none.
```

M150 correctly proves that its particular reduced Pin class-lifting
descriptor is constant on every aligned product-one transposition
factorization: the reduced kernel is all of `F_2^s` for `d>=4`, while the
chosen Pin extension splits at `d=3`.  Its signed-Hurwitz invariance argument
is exact.

This acceptance has the same strict scope as M150.  It does not classify all
central extensions or Nielsen invariants, find a simultaneous braid or
action-coset intersection, bound braid length, prove a spectral gap or mixing
theorem, or reach a terminal outcome.

## 1. Immutable-input gate

Before reading the proof or checker contents, I independently obtained the
following SHA-256 values; each equals the coordinator-supplied value:

| frozen M150 artifact | observed SHA-256 |
|---|---|
| `report.md` | `4c80fa05b6ef015f458a2f96fdf8a5c39e3f3e218fb16ac859e6c1f368ce3ad5` |
| `lifting_invariant_theorem.md` | `f7a592f945213a565cb8bbbf07218396649e9cfdef3fd4d6a77e106a5fd8edfe` |
| `lifting_invariant_audit.py` | `349278984fcba6885caf6b4da2e2fdfedee69c14485ed87795f5b4c4a968c2e2` |
| `results.json` | `5735acbd9e22567557e797c854b3c5f6aedc4a0bc00fdc74708bd1fa88a1195a` |
| `freeze_manifest.md` | `15825463c635a948f78df2b3d24b51e9deb6657c24660fdf951ef5a9b062eb97` |
| `SHA256SUMS` | `70b2936be9deef248c12a77e1e08cf2b259f770976b7cf66eaaee5a08e46f0b3` |

`sha256sum -c SHA256SUMS` also passed all seven payload entries in the frozen
directory.  I made no edit there.

## 2. Parameters and convention audited

Fix `d>=3`, `s>=1`,

```text
P_(d,s)={(g_1,...,g_s) in S_d^s : sgn(g_1)=...=sgn(g_s)},
```

and let `C_(d,s)` consist of tuples whose every coordinate is a
transposition.  Products use `(pq)(x)=p(q(x))`.  The audited move is

```text
(a,b) -> (b,b^(-1)ab),
```

which preserves the ordered product `ab`.  Every product-one sequence in
`C_(d,s)` has even length by sign.  The matching application uses the
minimal-sector length `2d-2`, but the constancy proof itself is universal for
product-one sequences in this class.

## 3. Numbered proof audit

### 3.1 Explicit Pin extension and kernel — accepted

In Euclidean `Cl_d`, the unit root

```text
a_(ij)=(e_i-e_j)/sqrt(2)
```

squares to one, and its twisted adjoint is the coordinate transposition
`(ij)`.  Thus the root-generated group, with scalar `z=-1`, surjects onto
`S_d`.

For completeness, the compressed kernel sentence in M150 can be expanded as
follows.  A product `u` of `k` unit vectors has definite Clifford parity and,
if its twisted adjoint is identity, obeys

```text
u e_i=(-1)^k e_i u        for every i.
```

Expand `u` in the standard blade basis.  A nonempty blade has an included
index, and commuting that corresponding `e_i` through the blade has the
opposite sign to the displayed requirement.  Hence only the empty blade can
occur; parity then forces `k` even.  Therefore `u` is scalar.  Its Clifford
norm is one, so `u=+/-1`.  Since both scalars occur, the kernel is exactly
`{1,z}`.  Coordinate product and restriction above `P_(d,s)` consequently
give the central kernel `Z=<z_1,...,z_s> ~= F_2^s`.

The clean-room enumeration independently found root-generated preimage
orders `12=2|S_3|` and `240=2|S_5|`, exactly two lifts above each permutation,
and identity fibers `{+1,-1}`.

### 3.2 One `P_(d,s)`-conjugacy class — accepted

For transpositions `t,u`, take any transporter `g` with `gtg^-1=u`.  If `g`
is odd, `gt` is even, still transports `t` to `u`, and differs only by a
source-centralizer element.  Hence every coordinate transporter may be made
even independently.  Their tuple belongs to `A_d^s <= P_(d,s)`, proving that
`C_(d,s)` is one `P_(d,s)`-class.  The fresh checker exhaustively found even
transporters for all `9` ordered source-target pairs at `d=3` and all `100`
at `d=5`.

### 3.3 Centralizer-commutator quotient — accepted

Let `E -> P_(d,s)` be the central extension, fix `x in C_(d,s)` and a lift
`x~`, and set

```text
K_C=<[x~,h~] : h in C_P(x)> <= Z.
```

The commutator is in `Z`; a central change of either lift does not change it.
Define the lift over `g x g^-1` by conjugating `x~` with a lift of `g`, modulo
`K_C`.  If two conjugators give the same base element, their ratio is a base
centralizer element, and precisely the resulting commutator ambiguity lies in
`K_C`.  Conversely, equality upstairs implies equality after projection.
Thus the conjugacy orbit maps bijectively to `C_(d,s)` and supplies the
claimed conjugacy-equivariant section `ell`.

Changing the base lift to `z_0 x~` multiplies every section value by the same
`z_0`.  Its product over an even-length sequence is unchanged because `Z` has
exponent two.  This verifies the claimed canonicity for all product-one
transposition sequences, in particular length `2d-2`.

### 3.4 Signed-Hurwitz invariance — accepted

Conjugacy equivariance gives

```text
ell(b^(-1)ab)=ell(b)^(-1) ell(a) ell(b).
```

Therefore

```text
ell(b) ell(b^(-1)ab)=ell(a) ell(b),
```

exactly, with no commutativity assumption.  The inverse move follows from the
same identity.  The fresh checker verified this equality on all nine ordered
pairs of rank-three transpositions using the independently constructed
section.

### 3.5 Localized `d>=4` annihilation — accepted

For coordinate `q`, choose a transposition `v_q` disjoint from `t_q` and put
`h^(q)_q=t_qv_q`, with identity in every other coordinate.  Each coordinate
of `h^(q)` is even, so `h^(q) in A_d^s <= P_(d,s)`.  The nontrivial coordinate
commutes with `t_q`, hence `h^(q)` centralizes the whole tuple `x`.

For the root lifts `a` of `t_q` and `b` of `v_q`, disjointness gives
`a^2=b^2=1` and `ab=-ba`.  Taking `ab` above `t_qv_q`,

```text
[a,ab]=a(ab)a^(-1)(ab)^(-1)=baba=-1.
```

Every other coordinate contributes `+1`, so this commutator is exactly `z_q`,
not merely a diagonal kernel element.  Varying `q` gives every basis vector
of `Z`; since `K_C<=Z`, this proves `K_C=Z` for all `d>=4,s>=1`.

The clean-room checker exhaustively tested every transposition tuple through
width three: at `d=4`, `6+72+648=726` localized witnesses; at `d=5`,
`10+200+3000=3210`.  Each witness was all-even, centralized its tuple, and
had Clifford commutator exactly `-1` in only the selected coordinate.

### 3.6 Rank-three splitting — accepted

For the two `A_2` simple roots `a,b`,

```text
a^2=b^2=1,       ab+ba=-1,
aba=-a-b=bab.
```

Thus `a,b` satisfy the Coxeter presentation of `S_3`.  The resulting map
`sigma:S_3 -> S~_3` projects identically to `S_3`, so it is a homomorphic
section.  Coordinatewise it splits the extension above `P_(3,s)`.

Using this section, a product-one aligned sequence lifts to
`sigma^s(product)=1`.  Any other conjugacy-equivariant class section is a
uniform central translate; for even length `m`, its extra factor is
`z_0^m=1`.  Hence translate independence is not an empirical matching fact.

The fresh implementation built the six-element section by closure, checked
all `36` multiplication-table entries, and obtained
`sigma((0 2))=-a_(02)`.  It then checked all `27` rank-three product-one words
of length four (`24` connected) and all `243` of length six (`240`
connected); every section product was `+1`.  Central translates in widths one
through four canceled at both even lengths.

## 4. Falsification and boundary audit

- `d=3`: no disjoint transposition exists, so M150 correctly uses a separate
  split-cover proof rather than the localized witness.
- `d=4`: the localized proof already works; every transposition has a
  disjoint transposition.  The fresh bounded audit included this first valid
  rank.
- `d=5`: exact finite Pin-fiber and tuple-width-three diagnostics agree with
  the universal algebra.
- `s=1`: `h^(1)=tv` is even and remains in `P_(d,1)=S_d`; the proof still
  kills the sole kernel generator.
- Odd factor length cannot be product one because every aligned factor has
  odd sign in each coordinate.  The translate-independence statement is thus
  applied only where its parity hypothesis is automatic.
- `d=2` lies outside M150's stated theorem and is not silently covered.

No counterexample or convention mismatch was found.

## 5. Nonblocking editorial notes

1. If promoted verbatim, expand the one-line Pin-kernel justification with
   the blade-parity argument in Section 3.1 above.
2. Prefer “the reduced Pin descriptor” over an unqualified “Schur invariant”:
   the result deliberately concerns this explicit extension and quotient, not
   every extension-theoretic or Nielsen invariant.

These are clarity recommendations, not objections to correctness.

## 6. Evidence, reproduction, and scope boundary

The independent checker uses exact arithmetic in `Q(sqrt(2))`, imports no
M150 code, uses Python `3.12.3`, has no nonstandard dependency, and is
deterministic (`seed=null`).  From this directory run:

```text
python3 -m compileall -q cleanroom_pin_audit.py
python3 -B cleanroom_pin_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert all(x["kernel"]==["+1","-1"] for x in q["finite_pin_preimages"]); assert all(not row["failures"] for x in q["localized_kernel"] for row in x["rows"]); assert all(row["nonidentity_section_products"]==0 for row in q["d3_even_product_one"]["rows"]); print("M153 assertions ok")'
sha256sum -c SHA256SUMS
```

Status labels:

```text
proved:      explicit cover/kernel, reduced class lift, Hurwitz invariance,
             d>=4 annihilation, d3 split and constant value
exact finite diagnostics: d3/d4/d5 rows recorded in results.json
unresolved:  other extension/Nielsen invariants, common braid,
             action-coset intersection, polynomial braid length, chain gap
```

Accordingly, M150 may be entered in the coordinator ledger as a fresh-audited
negative sharpening: this natural reduced Pin obstruction is absent.  It is
not a terminal result and supplies no sufficiency claim.
