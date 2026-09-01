# M289 report: channel-two embedding BV

Date: 2026-08-14 UTC.

## Verdict

**PROMOTE TO FRESH IMMUTABLE AUDIT.**  The exact channel-two embedding
vector bound is proved for every odd `k>=3`:

```text
||sum_(1<=s<k/2) qhat_s(Phi_s^D-Psi_s^D)||_1=O(1/k).
```

The proof retains the literal collision support, ordered factors, cyclic
phases, both B seams, the A wrap seam, reflection, support cutoffs, and the
unnormalized weight `qhat_s=q_s a_F(s)`.  It does not invoke the refuted
M211 pointwise `IKBE-b` claim or triangle-bound adjacent conditional
profiles.

## Proof outcome

The raw conditional normalizers cancel before any lag norm:

```text
H=sum_s q_s[(a_F/a_L)mathcal B_s-mathcal A_s]
 =sum_s q_s(mathcal B_s-mathcal A_s)
  +sum_s q_s(a_F/a_L-1)mathcal B_s.
```

The normalizer remainder has full circular variation `O(k^-2)`.  The main
signed term has three pieces:

1. first edges, controlled by an exact two-seam/one-seam comparison applied
   to `s q_s a_L(s)`;
2. all within-component pairs, controlled by the support-pair stabilization
   `TV[Z_(M,r)-((r/R)b+4/R)]<=C/R`, an untouched-component stabilization,
   and phase-embedding BV;
3. the A cross-block pairs, whose exact triangular profile has variation
   `O(k^-1)`.

Thus the complete ambient profile has circular variation `O(k^-1)`, and
restricting its adjacent differences to `l=2,...,3k-3` gives CEBV.

## Exact falsification result

The sole checker imports no predecessor or project code.  Direct
minimal-completion enumeration and the fixed closed formulas agree exactly:

| `k` | B ordered disjoint atoms | A ordered disjoint atoms | exact CEBV `l1` |
|---:|---:|---:|---:|
| 3 | 20 | 18 | `148/135` |
| 5 | 504 | 240 | `1411115143/1382976000` |

The fixed-formula scan at `k=3,5,7,9,15,31` is reported only as a finite
boundary/convention falsification.  It is not evidence for the asymptotic
bound; the analytic lemmas prove that bound.

## Boundary audit

- `k=3`: exact enumeration covers the unique split `s=1`, component sizes
  `1,2,3,4`, midpoint/reflection coincidences, and all zero endpoints.
- `k=5`: exact enumeration covers `s=1,2`, both seams, the A wrap, and the
  first nontrivial reflected support.
- Lemma 2 treats `r=1,2`, the `r-1/r` active/inactive cutoff, the reflected
  row, half-cycle midpoint, and endpoint zero padding uniformly.
- The A cross coefficient is `4u/k^2` per directed block-pair orientation,
  giving total mass `8u`; the complete raw B/A masses are respectively
  `12a_L(s)` and `12a_F(s)`.
- `qhat` is used literally as a subprobability and is never renormalized.

## Dependencies and first open item

The theorem depends on the accepted M276/M279 CEBV interface and the exact
completion/Borel identities inherited through the verified predecessor
chain.  M282/M286 supplies an independently accepted instance of the
support-pair stabilization method, but the M289 extension and embedding
comparison are proved in `cebv_coefficient_reduction.md`.

No CEBV mathematical lemma remains open in this deliverable.  The first open
obligation is the standalone fresh immutable reconstruction stated in
Section 10 of the proof.  The theorem must not enter a coordinator ledger as
accepted before that audit.

## Scope

This report closes only CEBV, subject to audit.  It makes no CIBV assembly,
DOR, SET, PBV, FD, FCL1, spectral-gap, polynomial-mixing, or Terminal A/B
inference; all remain open.
