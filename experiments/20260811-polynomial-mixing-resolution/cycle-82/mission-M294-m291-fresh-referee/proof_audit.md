# M294 fresh immutable proof audit of frozen M291

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
FINAL VERDICT: ACCEPT M291 AT ITS STATED COMMON-PREFIX SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL QUALIFICATIONS: TWO.
```

M291 proves an exact same-rank framed-stabilizer description of every
individual endpoint fiber and refutes polynomial-cardinality covers that
first apply one common prefix per class and land in the broad set of ordered
consecutive doubled Cayley-tree words. It does not lower-bound unrestricted
common-schedule classes: the source and target frames may cancel through the
chart stabilizer. The true M135 matching-coset refinement remains open.

No every-color common-schedule theorem, voltage statement, congestion bound,
spectral gap, mixing bound, or Terminal A/B conclusion is present.

## 2. Immutable package and dependency gate

The SHA-256 of M291's `SHA256SUMS` is exactly

```text
cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0.
```

The directory has exactly seven payload files besides `SHA256SUMS`, and
these are exactly its seven manifest rows:

| payload | SHA-256 |
|---|---|
| `plan.md` | `45b8168a0fdad70610e96914a07c13ef38d3e51780244e50cf814e45581b2fd6` |
| `checkpoint.md` | `52278b64692da1d15ac76e3462490b4ae8ea25f4a5eb0b8ecb4d8429a7303fb2` |
| `dependency_audit.md` | `d174428ee72f95e6bd7cff085553e7d99262479daf2e46504c8b7e02f70f9447` |
| `framed_stabilizer_obstruction.md` | `ba190f5c636ec52a085235f7a5f9d173b113b8fb7593d17a3d8f55b141027454` |
| `report.md` | `a14b1b56061575a91ee7ba97d70f4896baef542a27ec1ca4e6b850f62b962ceb` |
| `audit_request.md` | `f500a8ef6e004a076c2b1acaa014d8920a11e5b101a5a00938cbd5596a5b51a7` |
| `freeze_manifest.md` | `f488e06837c2e6f8ee3f23568dc3c8aa6d69324d6aad81e7062a23c6d135e41b` |

Every row passes `sha256sum -c`.

The 20 cited frozen predecessor manifests independently reproduce M291's
top digests and row counts:

| mission | rows | top digest |
|---|---:|---|
| M112 | 13 | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` |
| M119 | 8 | `1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8` |
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` |
| M175 | 8 | `f2718a493b7e30a615da1f6e4dbafad9d6501bcbd07822fd791b21eafbb26d88` |
| M176 | 8 | `92fe0752f2014fd320f8bf3ff10e09266872865f705a66ed32787c876592fe4a` |
| M181 | 8 | `d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0` |
| M183 | 7 | `ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46` |
| M200 | 10 | `6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045` |
| M202 | 10 | `33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70` |
| M240 | 9 | `2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3` |
| M242 | 7 | `49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663` |
| M269 | 9 | `c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb` |
| M271 | 7 | `ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73` |
| M273 | 9 | `4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550` |
| M275 | 8 | `8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa` |
| M278 | 8 | `352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad` |
| M281 | 10 | `8a775c75b63b897405a6fc29a455ba322eff7c6e70b13fca735b719ab0e89c8d` |
| M284 | 6 | `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3` |
| M288 | 8 | `fd4120e216b9140c4a8938724c3415393d6f5495a105f817cf681871545942ca` |

All 166 predecessor payload rows pass. M13 predates the manifest format;
its observed hashes also reproduce exactly:

```text
diameter_audit.md  536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67
report.md          4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324
```

The coordinator scopes at L-0013, L-0037, L-0227, L-0238, L-0259,
L-0262, L-0270, L-0289, L-0304, L-0305, L-0308, and L-0312 agree with
M291's imports. In particular: rooted DPS has an exact `d`-to-one root
quotient; every M135 color selects one physical `H`-edge above each left
global orbit; voltage remains conditional on quotient routing; rank-five
coverage is finite only; and M284 supplies chart-local lifting rather than a
full-color base route.

## 3. M13 applicability and exact length

M13 Claim D states that two length-`m` identity-transposition words in
`S_N` with the same labeled weighted support components have signed-Hurwitz
distance at most `50Nm^3`. Its audit counts an explicit constructive route;
it is not a flow or expansion statement.

Here `N=d` and `m=2d-2`. For every selected M135 edge `Q`, both `w_Q` and
`v_Q=tau_i(w_Q)` belong to `Z_d`. Each has the one labeled support
component `[d]`, of total weight `2d-2`. The fixed chart `c_d` has the same
component: its support is a spanning star and its `d-1` edges each occur
twice. Thus M13 applies separately to `(w_Q,c_d)` and `(v_Q,c_d)`, giving

```text
|alpha_Q|, |delta_Q| <= L_d=50d(2d-2)^3.
```

The chronological route `alpha_Q;delta_Q^(-1)` therefore has displayed
length at most `2L_d=100d(2d-2)^3`. This conclusion is per endpoint edge;
the frames depend on `Q` and supply no common flow or congestion bound.

As an additional convention check, the local primary source
`Literature/0110110v1.pdf`, SHA-256
`808c7959381560b53a6c860d1ee3ef33a1cd9b2d956e91fb8dddf9c9575999`,
states Theorem 3.4 in exactly the labeled-component/weight form used here.
Its move is the inverse orientation of M291's named right generator, so the
undirected signed-Hurwitz distance is unchanged. Lemmas 3.7--3.10 are the
constructive normalization steps counted by M13.

## 4. Fixed doubled-star chart

M278's one-based tree is rooted at leaf `d` with root edge `{1,d}`. In its
zero-based output convention the canonical word is

```text
E_2^2 E_3^2 ... E_(d-1)^2 G^2,
E_u=(u-1,p(u)-1),  G=(0,d-1).
```

Take the star centered at one, so `p(u)=1` for `2<=u<=d-1`. Translating
output labels from zero-based to `[d]` gives exactly

```text
c_d=(1,2)^2(1,3)^2...(1,d-1)^2(1,d)^2.
```

The root slot is last, as required by the locked canonical-slot order. At
the stated rank `d>=6`, this is a valid upper extension source chart from old
rank `d-1>=5`.

## 5. Exact framed fiber and route independence

Use chronological composition, so `A_(x;y)=A_y o A_x`. Define

```text
BStab_d={s in B_m:A_s(c_d)=c_d},
Ktilde_Q={beta in B_m:A_beta(w_Q)=v_Q}.
```

If `alpha_Q(w_Q)=c_d` and `delta_Q(v_Q)=c_d`, then every

```text
alpha_Q;s;delta_Q^(-1),  s in BStab_d,
```

maps `w_Q` to `v_Q`. Conversely, for `beta in Ktilde_Q`,

```text
s=alpha_Q^(-1);beta;delta_Q
```

maps `c_d` to itself, and cancellation gives

```text
beta=alpha_Q;s;delta_Q^(-1).
```

Hence, with the orientation exactly as frozen,

```text
Ktilde_Q=alpha_Q;BStab_d;delta_Q^(-1).
```

If `alpha'_Q` is another source frame, then
`alpha'_Q=alpha_Q;s_1` for `s_1 in BStab_d`. Likewise
`delta'_Q=delta_Q;s_2`. Since a subgroup is unchanged by left or right
translation by its members,

```text
alpha'_Q;BStab_d;(delta'_Q)^(-1)
 =alpha_Q;BStab_d;delta_Q^(-1).
```

Thus the fiber is intrinsic and independent of the chosen normalization
routes. A family has one common literal braid element exactly when these
intrinsic fibers intersect; a polynomial-length representative remains an
additional, separate condition.

Braid actions commute with global relabeling, and M135 proves `tau_i` is
`H`-equivariant. Therefore the one route for `w_Q` also maps every
`rho.w_Q` to `rho.v_Q=tau_i(rho.w_Q)`. It realizes the actual selected
physical `H`-orbit edge, not merely the chosen representative.

## 6. Same-rank word/action firewall

Let `p_d:B_m->Acal_d` be the surjection onto the finite global action image
on `Z_d`, and let

```text
K_Q={a in Acal_d:a(w_Q)=v_Q}.
```

Then `Ktilde_Q=p_d^(-1)(K_Q)`, so surjectivity immediately gives

```text
p_d(Ktilde_Q)=K_Q.
```

For any family of endpoint fibers,

```text
intersection_Q Ktilde_Q=p_d^(-1)(intersection_Q K_Q).
```

If the action intersection is nonempty, lift one common action to any braid
element; that single lift acts correctly on every source. Therefore

```text
p_d(intersection_Q Ktilde_Q)=intersection_Q K_Q.
```

This fixed-rank equality uses that each literal endpoint fiber is a full
preimage. It supplies neither a shortest representative nor an action-image
embedding between ranks. It does not conflict with M284's warning that
images of its restricted, identically factored upper liftable sets can have
larger intersections.

## 7. Independent cardinality reconstruction

The rooted DPS bijection has

```text
d^(d-2) (2d-2)!
```

rooted objects: Cayley's `d^(d-2)` labeled trees times all factor-label
orders. Forgetting the white root is exactly `d`-to-one, hence

```text
|Z_d|=d^(d-3)(2d-2)!.
```

Global relabeling by `G=S_d` and relabeling by `H=Stab_G(d)` are free on
`Z_d`, so their orbit sizes are `d!` and `(d-1)!`. A perfect-matching color
contains exactly one source `H`-orbit above each of the `|Z_d|/d!` left
global orbits. These physical `H`-orbits are distinct and disjoint. Thus
the source physical set of an arbitrary fixed color has

```text
|C|=(|Z_d|/d!)(d-1)!=|Z_d|/d
   =d^(d-4)(2d-2)!.
```

For the broad paired-tree set `P_d`, a word uniquely reveals its ordered
list of `d-1` distinct tree edges by reading one edge from each consecutive
equal pair. Therefore the tree/order map is injective as well as
surjective onto the definition, and

```text
|P_d|=d^(d-2)(d-1)!.
```

Every such word has identity product and connected tree support, so
`P_d subset Z_d`.

## 8. Prefix-cover lower bound, orbit formulation, and inversion

Every braid element acts bijectively on `Z_d`. For a fixed prefix `a`,

```text
{w in C:A_a(w) in P_d} subset A_a^(-1)(P_d),
```

and the right side has exactly `|P_d|` elements in `Z_d`. Hence each cover
class using prefix `a` has size at most `|P_d|`. This remains true for
overlapping arbitrary subsets, unlimited prefix length, and different target
paired trees within one class. A union bound gives

```text
q >= |C|/|P_d|
  = (2d-2)!/[d^2(d-1)!]
  = ((d+1)(d+2)...(2d-2))/d.
```

There are `d-2` numerator factors and each is at least `d`, so

```text
q >= d^(d-3).
```

(`q` is integral, so a ceiling gives a slightly sharper but unnecessary
version.)

The set `P_d` is invariant under global relabeling, and braid actions commute
with relabeling. Thus if one representative of an `H`-orbit lands in
`P_d`, its whole physical orbit does. The physical-state proof therefore
translates exactly to the actual selected orbit-edge cover, with no
preferred-root substitution.

The target physical set is `tau_i(C)`. Since `tau_i` is an `H`-equivariant
bijection and a matching is also right-perfect, it has the same orbit count
and cardinality. Applying the same bijective-preimage argument to
target-to-chart routes, then inverting those braid words, gives the analogous
common-suffix obstruction.

## 9. Decisive nonimplication and exact remaining lemma

The counting argument constrains a one-sided prefix selected before using
the target frame. A true common schedule `beta` instead requires, for each
edge `Q`,

```text
alpha_Q^(-1);beta;delta_Q in BStab_d.
```

The two `Q`-dependent frames can cancel through different stabilizer
elements. Therefore the prefix-cover bound is not a lower bound on:

- the number of nonempty genuine common-schedule classes;
- the shortest braid representative in a common action fiber; or
- any congestion, voltage, gap, or mixing quantity.

The exact surviving obligation is M291's framed-stabilizer
common-intersection problem: cover the actual selected endpoint fibers by
`d^O(1)` families whose intersections contain representatives of length
`d^O(1)`, or prove that no such cover exists.

## 10. Numbered objections and qualifications

### Material objections

None.

### Nonmaterial qualifications

1. **N-1, repository-status reconciliation.** `HANDOFF.md` and the embedded
   AGENTS guide still describe the Ben-Itzhak--Teicher classification as
   awaiting source/convention verification, while the active run ledger at
   L-0013 records that verification and L-0037 accepts M13's quantitative
   audit. This referee additionally checked the local primary source and
   found the theorem hypotheses and move orientation consistent. The stale
   durable wording should be reconciled by the coordinator, but it does not
   change M291's frozen-input proof.
2. **N-2, “literal” means before the finite action quotient.** The fiber is
   a subset of the braid group, hence its elements are already modulo braid
   relations; it is not a set of raw strings. The quantitative claim is the
   existence of the displayed signed-generator representatives of the stated
   lengths. M291's explicit representative-length firewall already enforces
   this reading.

## 11. Accepted boundary

```text
PROVED AND ACCEPTED:
  M13 individual endpoint frames through the fixed doubled-star chart;
  exact framed-stabilizer endpoint fiber and route independence;
  fixed-rank equality of literal/action common-nonemptiness;
  exact physical-color and paired-tree cardinalities;
  superpolynomial common-prefix paired-chart cover lower bound;
  inverse target-suffix version.

UNRESOLVED:
  framed-stabilizer common-intersection with polynomial representatives;
  true M135 polynomial matching-coset refinement;
  chartless two-sided base-route signatures and synchronized routing.

NOT CLAIMED:
  lower bound on genuine schedule classes; every-color common schedule;
  voltage, congestion, spectral gap, mixing, Terminal A, or Terminal B.
```

