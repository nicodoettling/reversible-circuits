# M288 Final Report: Fresh Immutable Referee of M284

Date: 2026-08-14 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict

```text
FINAL VERDICT: ACCEPT M284 AT ITS STATED STRICT WORD-LEVEL SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL QUALIFICATIONS: TWO.
```

The accepted result is the literal braid-fiber rank-lifting identity, the
conditional one-step at-most-two local refinement, and the `V_D`
obstruction to chart/local-type-only coverage. The full polynomial M135
matching-coset refinement remains unresolved.

| field | result |
| --- | --- |
| candidate | rank-lifted schedule-intersection lemma |
| claimed target | deterministic rooted minimal-sector endpoint fibers |
| identity ok | exact endpoint algebra and compact guard pass |
| crosses Hurwitz components | not applicable; no sampler is claimed |
| exact diagnostics | manifests, type audit, seams, boundaries, `V_D` |
| verdict | accept strict lemma and strict obstruction only |

## 2. Provenance

M284's `SHA256SUMS` digest is exactly
`3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3`;
all six payloads pass. Every payload of all sixteen cited
M135/M137, M175/M176, M181/M183, M200/M202, M240/M242, M269/M271,
M273/M275, and M278/M281 inventories also passes at the top digests listed
in `proof_audit.md`. Their coordinator ledger scopes agree with M284.

## 3. Type and endpoint audit

M135's `K_Q` is a finite same-rank action fiber. Its preimage
`Ktilde_Q` is a subset of `B_(2d-2)`. M278's correction
`c_(T,i)` is instead in `B_(2d)` and starts at the old-edited padded
state `N_T`; it does not itself map the unedited upper source to the edited
upper target.

The standard injection `j_d` adds two inert strands. Hence for
`beta in Ktilde_Q`,

```text
U_T=u_T k_d^2
  --j_d(beta)--> u'_T k_d^2=N_T
  --c_(T,i)-->  A_T.
```

For a family sharing one correction `c`, the map
`beta -> j_d(beta);c` is injective. Cancellation of the common terminal
factor and injectivity of `j_d` prove the exact displayed intersection
identity. After quotienting to finite action images, distinct braids can
coalesce, so this is only a sufficient recursive construction. M284 states
that qualification correctly.

## 4. Local alphabet and boundaries

After the accepted M273/M275 composition closes ordinary IDL, every optional
nonchild scan sign may be chosen negative. Thus a fixed ordinary odd edit
uses either identity or one tree-independent open word. Internal evens use
identity, the cross seam uses two inverse moves, and the last seam uses one.
The rows partition every adjacent index.

At `d=5`, the indices are odds `1,3,5`, internal evens `2,4`, cross
`6`, and last `7`. The endpoint `v=d-1` has an empty scan and the
five-move carrier. The maximum displayed increment is exactly
`4(d-v-1)+5<=4d-7`. A chart-compatible lower `q`-class cover therefore
lifts in one step to at most `2q` displayed classes. This is not an
iterated polynomial bound and is not a full matching-color theorem.

## 5. `V_D` obstruction

For every `D>=6`,

```text
V_D=e_1,e_2,e_2 e_1 e_2,e_2,e_3,e_3,...,e_(D-1),e_(D-1)
```

has identity product, connected support, and length `2D-2`. Every star
edge remains. Its first two factors are unequal. Every unedited extension
chart has equality in each consecutive pair, and simultaneous global
conjugation preserves that equality pattern. Therefore the entire global
orbit of `V_D` is chartless.

Each M135 perfect-matching color has exactly one `H`-orbit edge over every
left global orbit, including `[V_D]`. Hence charts and local correction
type alone fail to cover any color. This is not a lower bound on the true
number of action schedule classes: a source-dependent base route may still
produce a polynomial refinement.

## 6. Independent guard and objections

The no-import `convention_guard.py` passes prefix embedding, all-negative
scan/carrier schemas, 52 cross-seam regimes, every last seam and edit
boundary for `5<=d<=12`, and `V_D` for `6<=D<=12`. Its normalized
digest is
`adcfb4cc7134cedeca1ec5241598dc8ab695cd513aec565fe577944608afe0f8`.
These finite checks calibrate conventions only.

1. **Material objections:** none.
2. **N-1, nonmaterial:** “minimal safe signature” is proof-theoretic under
   the accepted inputs, not an information-theoretic minimality theorem.
3. **N-2, nonmaterial:** “literal braid” means before quotienting to the
   finite action image; the set identity is in the braid group, while the
   length bound concerns the displayed representative.

## 7. Exact stopping line

```text
ACCEPT:
  strict rank-lifted braid-fiber identity;
  conditional one-step q -> 2q local split;
  V_D chart/local-type-only coverage obstruction.

UNRESOLVED:
  true polynomial M135 refinement and polynomial representatives;
  chartless base routes; synchronized/every-color routing; voltage.

NO INFERENCE:
  lower bound on true schedule classes; congestion; gap; mixing; Terminal.
```

