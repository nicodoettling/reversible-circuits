# M288 Fresh Proof Audit of Frozen M284

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
FINAL VERDICT: ACCEPT M284 AT ITS STATED STRICT WORD-LEVEL SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL QUALIFICATIONS: TWO.
```

M284 proves a rank-lifted endpoint-fiber/intersection lemma for explicit
braid elements on valid rooted extension charts, an at-most-two local
correction alphabet for one rank step, and an arbitrary-rank obstruction to
covering an M135 matching color by those charts and local types alone.

It does not prove or lower-bound the number of genuine finite-action schedule
classes needed for M135. It proves no every-color route theorem, quotient
route, voltage correction, congestion, spectral gap, mixing theorem, or
Terminal A/B.

## 2. Immutable inventory and ledger gate

M284's top inventory digest independently recomputes exactly as assigned:

```text
M284  3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3
```

All six listed M284 payloads pass `sha256sum -c SHA256SUMS`. Every payload
in all sixteen cited inventories also passes. Their independently recomputed
top digests are:

| mission | top SHA-256 |
| --- | --- |
| M135 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` |
| M137 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` |
| M175 | `f2718a493b7e30a615da1f6e4dbafad9d6501bcbd07822fd791b21eafbb26d88` |
| M176 | `92fe0752f2014fd320f8bf3ff10e09266872865f705a66ed32787c876592fe4a` |
| M181 | `d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0` |
| M183 | `ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46` |
| M200 | `6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045` |
| M202 | `33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70` |
| M240 | `2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3` |
| M242 | `49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663` |
| M269 | `c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb` |
| M271 | `ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73` |
| M273 | `4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550` |
| M275 | `8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa` |
| M278 | `352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad` |
| M281 | `8a775c75b63b897405a6fc29a455ba322eff7c6e70b13fca735b719ab0e89c8d` |

The corresponding coordinator ledgers were checked at L-0238, L-0259,
L-0262, L-0270, L-0289, L-0304, L-0305, and L-0308. The scopes agree:
M135/M137 leave matching-coset realization open; M175/M176 and M181/M183
make voltage consequences conditional on actual synchronized quotient
routing; M200/M202 are finite rank five, width two, and qualitative; M240/M242
were conditional on IDL until M269/M271 and M273/M275 closed the ordinary
endpoint composition; and M278/M281 prove only the local
old-padded/new-rank correction table.

No predecessor or coordinator file was edited.

## 3. Type firewall

Put `m=2d-2`. At lower rank, the M135 endpoint fiber is

```text
K_Q={a in A_d : a(w_Q)=tau_i^(d)(w_Q)}.
```

It is a subset of the finite lower-rank action image. Its braid preimage is

```text
Ktilde_Q={beta in B_m : beta(w_Q)=tau_i^(d)(w_Q)}.
```

In contrast, M278/M281's local object is a braid element
`c_(T,i) in B_(m+2)` with the endpoint

```text
c_(T,i)(N_T)=A_T,
N_T=u'_T k_d k_d.
```

Its source is already the old edited word padded at the new rank. It is not
an element of the lower-rank action image, and the accepted endpoint is not
`c_(T,i)(U_T)=A_T`. The upper M135 fiber is a subset of the different
finite action image `A_(d+1)`. M284 keeps all four types separate.

## 4. Added-strand embedding and endpoint order

The standard inclusion

```text
j_d:B_m -> B_(m+2),       R_r^(+/-1) -> R_r^(+/-1)
```

adds two vertical strands on the right. Deleting those two added strands on
the image is a left inverse, so the inclusion is injective. Its Hurwitz
action touches only the first `m` factors.

For `beta in Ktilde_(Q_T)`,

```text
U_T=u_T k_d k_d,
j_d(beta)(U_T)=beta(u_T) k_d k_d
              =u'_T k_d k_d=N_T.
```

Only after that prefix action is the accepted correction applied:

```text
(j_d(beta);c_(T,i))(U_T)=c_(T,i)(N_T)=A_T.
```

Thus M284's source ordering is correct: lower edit, inert padding, then local
new-rank correction. No source/target reversal occurs.

## 5. Exact common-correction intersection

For a fixed terminal correction `c`, define

```text
f_c(beta)=j_d(beta);c.
```

Translation by a group element is bijective and `j_d` is injective, hence
`f_c` is injective. For any finite family of lower braid fibers,

```text
intersection_Q f_c(Ktilde_Q)
 =f_c(intersection_Q Ktilde_Q).
```

The reverse inclusion is immediate. For the forward inclusion, an element
in every translated set has presentations `j_d(beta_Q);c`; cancellation of
the common chronological terminal factor makes all `j_d(beta_Q)` equal,
and injectivity of `j_d` makes all `beta_Q` equal. This proves M284's
displayed identity exactly.

The qualification is essential. If `phi_(d+1)` is the finite action map,
then only

```text
phi_(d+1)(intersection_Q L_Q)
  subset intersection_Q phi_(d+1)(L_Q)
```

is automatic. Distinct upper braids may induce the same finite action, so
the inclusion can be strict. M284 correctly treats the literal braid-fiber
identity as a sufficient recursive construction, not as a classification
or a lower bound on action-image intersections.

## 6. Complete local alphabet and every boundary

The accepted M273/M275 composition closes M240's ordinary IDL hypothesis.
For an ordinary odd edit

```text
i=2v-3,       2<=v<=d-1,       L=d-v-1,
```

M240/M242's scan requires a negative sign at a direct larger child and
allows either sign at every nonchild. Choosing every optional sign negative
therefore gives the one tree-independent open word

```text
c_open=Q^-_(d,v);B_d;(Q^-_(d,v))^(-1),
|c_open|=4L+5=4(d-v-1)+5<=4d-7.
```

A sealed ordinary row uses identity. The other accepted rows are:

| family | indices | literal corrections |
| --- | --- | --- |
| ordinary odd | `1,3,...,2d-5` | `id` or one fixed `c_open(d,v)` |
| internal even | `2,4,...,2d-6` | `id` |
| cross seam | `2d-4` | `(R_(2d-5)^(-1))^2` |
| last seam | `2d-3` | `R_(2d-2)^(-1)` |

These rows are disjoint and their union is every
`1<=i<=2d-3`. At `d=5` they give odds `1,3,5`, internal evens `2,4`,
cross `6`, and last `7`. At `v=d-1`, the scan is empty and the
five-move carrier remains. Cross and last lengths are two and one, so the
maximum is always `4d-7`.

Consequently, a declared chart-compatible `q`-class lower cover splits by
at most two literal corrections and yields at most `2q` displayed upper
classes in one rank step. This is conditional on having valid charts and
explicit lower schedules; it is not an iteration theorem or an M135
full-color cover.

## 7. The `V_D` chart-coverage obstruction

For `D>=6`, let `e_r=(0,r)` and

```text
U_D=e_1,e_1,e_2,e_2,...,e_(D-1),e_(D-1),
V_D=R_2(U_D)
   =e_1,e_2,e_2 e_1 e_2,e_2,e_3,e_3,... .
```

Every displayed factor is a transposition. Associativity and involutivity
give

```text
e_1 e_2 (e_2 e_1 e_2) e_2
 =e_1 e_1=id,
```

and every later factor is in an adjacent square. The support retains all
`D-1` star edges, so it is connected on all `D` labels. The word has
length `2D-2`, hence lies in the minimal connected identity sector
`Z_D`.

The canonical-slot lemma gives every unedited M278 extension-chart source
the coordinate equality pattern

```text
f_1,f_1,f_2,f_2,...,f_(D-1),f_(D-1).
```

Simultaneous conjugation is injective and preserves equality at every fixed
coordinate pair. In `V_D`, positions one and two are the distinct
transpositions `e_1,e_2`. Therefore no member of the whole global orbit
`[V_D]_G` is an unedited extension-chart source.

For every fixed adjacent edit, an M135 color is a perfect matching of the
orbit-incidence multigraph. Its left vertices are all global orbits, so
left-perfectness includes exactly one `H`-orbit edge incident to
`[V_D]_G`. Every representative of that edge is chartless by the same
pair-equality invariant. Thus charts plus local correction type alone do
not cover any complete M135 color.

This is only a coverage obstruction to that named naive descriptor. A
source-dependent base route may move a chartless word into a chart and may
still admit a polynomial common-action cover. M284 correctly proves neither
a lower bound on genuine schedule classes nor failure of the true M135
refinement.

## 8. Compact independent guard

`convention_guard.py` imports no M284 or predecessor code/data and performs
no orbit or route search. It checks:

- `V_D` identity, support, length, and first-pair defect for
  `6<=D<=12`;
- the prefix-fixing added-strand action at `d=5,6,7,8`;
- all-negative direct-child, disjoint-nonchild, and carrier schemas for
  `5<=d<=12`;
- 52 cross-seam meeting/disjoint rows, every last-seam row, and every edit
  boundary for `5<=d<=12`.

All checks pass. The normalized result digest is

```text
adcfb4cc7134cedeca1ec5241598dc8ab695cd513aec565fe577944608afe0f8.
```

This is convention calibration only. Sections 3--7 supply the proof.

## 9. Numbered objections and qualifications

### Material objections

None.

### Nonmaterial qualifications

1. **N-1, “minimal” is proof-theoretic.** M284's “minimally safe recursive
   signature” means the smallest interface currently licensed by the frozen
   inputs: chart certificate, explicit lower braid or full braid fiber, and
   literal correction. It is not a theorem that no smaller compressed
   signature can exist. M284's explicit unresolved-refinement and no-lower-
   bound language already enforces this reading.
2. **N-2, braid element versus displayed spelling.** The intersection
   identity lives in the braid groups `B_m` and `B_(m+2)`; “literal” means
   before quotienting to their finite action images and with one fixed
   correction element. Different strings related by braid relations can
   represent the same braid element. The length assertion concerns the
   displayed concatenated representative. This clarification changes no
   endpoint, set identity, or bound.

## 10. Accepted boundary

```text
PROVED AND ACCEPTED:
  rank-d action fibers are distinct from rank-(d+1) local corrections;
  added-strand endpoint lifting and the exact common-c braid-fiber identity;
  fixed-(d,i) local correction alphabet of size at most two;
  conditional one-step q -> 2q displayed-class recurrence;
  V_D obstruction to chart/local-type-only full-color coverage.

UNRESOLVED:
  polynomial M135 action-coset refinement;
  polynomial base-route signature cover for chartless selected edges;
  synchronized/every-color routing and voltage-corrected length.

NOT CLAIMED:
  a lower bound on true schedule classes; congestion; a spectral gap;
  polynomial mixing; Terminal A or Terminal B.
```
