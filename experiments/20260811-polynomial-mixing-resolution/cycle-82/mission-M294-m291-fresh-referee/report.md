# M294 report: fresh referee of M291

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M291 AT ITS STATED COMMON-PREFIX SCOPE.
ZERO MATERIAL OBJECTIONS; TWO NONMATERIAL QUALIFICATIONS.
```

The frozen package, its exact seven-payload inventory, and all cited
predecessor inventories pass. The main calculations independently check:

```text
each chart frame <= 50d(2d-2)^3,
each separate endpoint route <= 100d(2d-2)^3,

Ktilde_Q=alpha_Q;BStab_d;delta_Q^(-1),

|Z_d|=d^(d-3)(2d-2)!,
|C|=|Z_d|/d=d^(d-4)(2d-2)!,
|P_d|=d^(d-2)(d-1)!,

q >= |C|/|P_d|
  = (2d-2)!/[d^2(d-1)!]
  >= d^(d-3).
```

The doubled-star word is exactly the M278 canonical-slot chart for the star
rooted at leaf `d`, after the documented zero-based to one-based label
translation. The chronological order in the framed fiber is correct,
changing either frame leaves the fiber unchanged, and braid/global-label
equivariance realizes the whole actual selected `H`-orbit edge.

At fixed rank, literal endpoint fibers are full preimages of finite action
fibers, so projection preserves their common-nonemptiness predicate. It does
not preserve a shortest representative and gives no cross-rank action map.

The lower bound is exactly one-sided. It refutes polynomial covers by common
prefixes landing in any ordered consecutive doubled-tree word, and by
inversion the analogous target suffixes. It does not lower-bound true
two-sided schedule classes because source and target frames may cancel
through different chart-stabilizer elements. The framed-stabilizer
common-intersection remains the first open lemma.

## Numbered qualifications

1. The active run ledger records the Ben-Itzhak--Teicher source/convention
   audit as completed, while `HANDOFF.md` and AGENTS still carry the older
   pending-audit wording. Direct inspection of the repository's local PDF
   confirms the hypotheses and inverse-generator translation used here;
   coordinator reconciliation of the durable wording is still advisable.
2. “Literal braid” means a braid-group element before quotienting to its
   finite action, not a raw spelling. Length concerns an explicit signed-
   generator representative. M291 already keeps this distinction.

No every-color common-schedule, voltage, congestion, gap, mixing, or
Terminal statement is accepted.

