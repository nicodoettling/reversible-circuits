# M282 report: channel-two signed scalar-Abel vector bound

Date: 2026-08-14 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
VERDICT: CSBV PROVED FOR EVERY ODD k>=3, SUBJECT TO FRESH AUDIT.

CEBV, CIBV, DOR, SET, PBV, FD, FCL1, GAP, MIXING, AND TERMINALS:
NOT ATTEMPTED AND UNRESOLVED.
```

The setting is the balanced first fixed cell of the auxiliary uniform
minimal-long-cycle factorization law and M73's nonlazy cyclic rank-two
quotient kernel, with `n=3k`, `(pq)(x)=p(q(x))`, and displayed factors
left-to-right. This is not the global identity-word law or the lazy exact
same-product `{3,4,5}` heat-bath chain.

The theorem proved here is exactly

```text
|| E_(k-1)Phi_(k-1)^D
   +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D) ||_1
 <=C/k,

E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)],
```

with an absolute, non-optimized constant. All lag, literal phase,
ordered-factor, disjoint-kind, and support-collision information is retained
until an exact coefficient aggregation; the norm is taken only after the
signed cancellation.

## 2. Immutable source gate

Every file in every cited checksum inventory passed. The independently
recorded checksum-file digests are

```text
M272 af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
M276 882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M279 3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
M192 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
M195 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M248 c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8
M249 9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7
```

M272 as a whole remains rejected for its unrelated J1 BV gap; M276/M279's
append-only repair and M272's unaffected exact channel-two endpoint/Abel
reduction are the accepted interface. No predecessor was edited.

## 3. Exact common-profile collapse

Put `D=2k-1`, `R=D-2`,

```text
a_L(s)=1-gamma_L(s),      a_F(s)=1-gamma_F(s),
A_s=p_s a_L(s)-q_s a_F(s),
W_s=A_s/a_L(s).
```

Finite summation by parts, retaining the nonzero endpoint, gives exactly

```text
CSBV vector=sum_(s=1)^(k-1) A_s Phi_s^D.           (3.1)
```

For `b_r=e^-r r^(r-1)/r!` and
`K_R(r,x)=b_xb_(r-x)/(Rb_r)`, the raw disjoint second-edge and cross-pair
coefficient in a size-`r` component is

```text
U_r(x)=1/R[4(r-1)/r+(r-x-3)b_xb_(r-x)/b_r],
                                      1<=x<r.       (3.2)
```

The formula includes `x=r-1`, both component choices, all ordered pairs,
and every collision multiplicity. Since the factors are disjoint, the kind
is literally `D`.

Let `c_d` be the signed ordered-support-pair intensity on the abstract
`D`-cycle. Direct disintegration gives

```text
c_d=A_min(d,D-d)
 +sum_(r=1)^(D-1)W_min(r,D-r)[U_r(d)+U_r(D-d)].    (3.3)
```

Thus `c_d=c_(D-d)`. Counting the two literal seams over every phase gives
the exact ambient profile `J`:

```text
c_0=c_k=0,
J_l=[(D-2l)c_l+(l-1)c_(l-1)]/D,       1<=l<=k,
J_l=[(l-k)c_(l-k)+(2k-l)c_(2k-l)]/D,
                                      k+1<=l<=2k-1,
J_(n-l)=J_l.
```

The CSBV vector is exactly `(J_(ell+1)-J_ell)_(ell=2,...,n-3)`. Direct
adjacent subtraction reduces the target to endpoint-inclusive half-BV of
`c`, plus `D^-1 sum|c_s|`; the latter is bounded by `24/D` because every
disjoint support profile has total mass `12` and `sum|A_s|<=2`.

## 4. Decisive signed cancellation

Define, on `d=0,...,k` with zero endpoints,

```text
Z_r(d)=U_r(d)+U_r(D-d),
B_r(d)=(r/R)b_d+4/R.
```

The proved stabilization lemma is

```text
TV(Z_r-B_r)<=C/R                  for every 1<=r<=D-1. (4.1)
```

Its proof treats `r=1,2`, the active range, the `d=r-1/r` cutoff, the
inactive tail, the reflected support, and both zero-padding endpoints. The
central bracket is

```text
e_r(d)=b_d[(r-d-3)b_(r-d)/b_r-r].
```

For `d<=r/2`, Borel ratio products give `|Delta e_r(d)|<=Cb_d`. For
`a=r-d<=r/2`, rewriting the bracket in `a` gives total variation `O(1)`.
After the exterior factor `1/R`, every omitted/cutoff/reflected piece is
`O(1/R)`.

Pairing sizes `s,D-s` therefore gives

```text
V_s=Z_s+Z_(D-s)=B+O_BV(1/R),
B(d)=(D/R)b_d+8/R,                 TV(B)=O(1).      (4.2)
```

The exact normalizer identity is

```text
sum_s W_s=-sum_s q_s[a_F(s)/a_L(s)-1].             (4.3)
```

The accepted explicit ratio bound makes `(4.3)` `O(k^-2)`, while
`sum|W_s|<=3`. Hence, before taking a norm,

```text
sum_s W_sV_s=(sum_sW_s)B+sum_sW_s(V_s-B),
```

and `(4.2)--(4.3)` give half-BV `O(1/k)`. This is the signed cancellation
that the raw rowwise shortcut misses: raw `V_s` contains the common profile
`B` with `Theta(1)` variation.

## 5. First-edge coefficient and endpoints

On `1<=s<k/2`, exact Borel products write `A_s=b_sH_k(s)` with

```text
|H_k(s)|<=Cs/k,             |Delta H_k(s)|<=C/k.
```

Thus the low-range variation sums as `k^-1 sum b_s=O(1/k)`. Above the
midpoint `q_s=0`, both Borel indices are comparable to `k`, giving

```text
A_s=O(k^-3/2),              Delta A_s=O(k^-5/2).
```

The `j/j+1` junction is `O(k^-3/2)`, while the zero-padding endpoints cost
`A_1=O(1/k)` and `A_(k-1)=O(k^-3/2)`. This includes `k=3`. Therefore

```text
TV(0,A_1,...,A_(k-1),0)=O(1/k).
```

Combining this with Section 4 proves ACBV and then CSBV. The nonzero Abel
endpoint remains inside `A`; `c_0=c_k=0` is only half-profile padding.

## 6. One compact exact falsifier

After fixing all formulas, `coefficient_probe.py` evaluated the coefficient
and embedding identities with exact rational arithmetic at
`k=3,5,7,9,15,31`. It imports no predecessor code or data.

| `k` | `k TV(A)` | `k TV(M)` | `k TV(c)` | `k||CSBV||_1` |
|---:|---:|---:|---:|---:|
| 3 | 2.5600 | 5.2800 | 4.8000 | 0.9600 |
| 5 | 2.2070 | 1.9476 | 1.8273 | 0.8543 |
| 7 | 2.1280 | 1.2343 | 1.4907 | 0.9642 |
| 9 | 2.0617 | 0.8961 | 1.4525 | 1.0678 |
| 15 | 1.9052 | 0.4818 | 1.5617 | 1.2580 |
| 31 | 1.6634 | 0.2075 | 1.5052 | 1.2641 |

The embedded norms at `k=3,5,7` reproduce M272's independently enumerated
values exactly. These rows are finite falsification/reproducibility only;
Sections 3--5 are the all-rank proof.

Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M282-channel-two-csbv/coefficient_probe.py --k 3 5 7 9 15 31 --output experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M282-channel-two-csbv/coefficient_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`.

## 7. Exact stop and action

CSBV is proved subject to a fresh immutable audit. This closes only the
scalar-Abel portion of M272's disjoint channel-two coefficient. CEBV remains
independent and open, so CIBV does not follow. DOR and every later endpoint,
prefix, gap, mixing, and Terminal claim remain unresolved.

Final action: **freeze M282 and request a fresh referee focused on the
support-pair disintegration, literal seam map, one-component stabilization
lemma, exact `sum W` cancellation, low/bulk first-edge BV, and all endpoint
terms.**

