# M274 report: minority-sign closure attempt

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, and scope

```text
VERDICT: KEEP THE EXACT MS/CP HIERARCHY AND TWO SIGN-PROOF FIREWALLS.
MON AND RESPONSE-FOSD ARE REFUTED.
CP, OS+, MS, AND FCL1 REMAIN UNRESOLVED.
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`, and
`n=3k`.  This mission concerns only the first separated fixed cell of the
auxiliary uniform minimal factorization law of the long cycle under M73's
nonlazy cyclic rank-two quotient kernel.  It is not the global identity-word
law or the lazy exact same-product `{3,4,5}` heat-bath chain.

For `1<=y<=n-3`, let

```text
z_k(y)=[bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/pi_y,
P_k=sum_y(z_k(y))_+,       N_k=sum_y(-z_k(y))_+.
```

## 2. Exact minority-sign interface

M168/M171's elementary identity is

```text
sum_y|kz_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).
```

M266/M268 now proves the first term is uniformly bounded.  Therefore,
under the accepted proved PCS estimate,

```text
FCL1  iff  k min(P_k,N_k)=O(1).                     (MS)
```

This is the exact minority-sign target.  Directional negative mass
`kN_k=O(1)` is sufficient but stronger; universal one-sign is stronger
again.  The proof note reconstructs the full per-lag raw and M91
two-channel formulas, lag endpoints, reflection, `T/D` kinds, `IS/IN/X`
topologies, Abel endpoints, singleton, and cutoff terms.

M261/M264's exact per-lag affine separation is retained:

```text
z_k(ell-1)=Lambda_n e^(-2)/[(n-3)(n-4)]
 [2eta(T)+eta(I_ell)+eta(Q_ell)],

eta(T)=12(k-1)/[3k(3k-4)(2k-1)]>0.
```

The positive baseline `2eta(T)` is separate from the collision/decorated
remainder, which has no proved lower bound.  The phase-summed baseline
`2n eta(T)` is likewise separate from `eta(B_k)`.

## 3. Repaired fully recombined channel lemma

Let

```text
g_(k,y)(s)=bar K(O_s,O_y)/pi_y
          =2W_(k,y)(s)/(A_s pi_y).
```

For the normalized M91 channel laws define

```text
CP_j(k,y)=(H_(j,B)-H_(j,A))(g_(k,y)),       j=1,2.
```

Then exactly

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y).
```

The proof note gives direct non-Abel coefficient formulas for both `CP_j`:
channel one compares the full first-edge laws on merged `L` and separate
`C_-,C_+`, tensoring the common `M` edge; channel two compares the full
ordered first-two-factor laws `N_L` and `N_(C_-C_+)`.  Thus

```text
(CP)  CP_j(k,y)>=0 for j=1,2 and every allowed (k,y)
```

would prove OS+, hence MS and FCL1.  CP is strictly weaker than the refuted
termwise Abel monotonicity and stronger than the needed cross-channel
negative-mass estimate.  No proof of CP was found.

## 4. Exact refutations and arbitrary-rank firewall

The tempting termwise Borel statement

```text
R(Phi_(j,u+1))>=R(Phi_(j,u)),
R(Phi_(j,u))>=R(Psi_(j,u))                           (MON)
```

is false.  The exact capped checker finds 4 violations at `k=3` and 46 at
`k=5`, the latter split into 32 adjacent and 14 embedding failures.  The
first `k=3` failure is

```text
R_(3,2)(Phi_(1,1))-R_(3,2)(Psi_(1,1))
 =-876877452441/14123762450000.
```

A response-monotone coupling is impossible as well.  At `k=3`, `j=1`,
`y=1`, threshold `343359/268912`, the exact B-minus-A response upper-tail
mass is `-32/375`.  Thus first-order stochastic dominance fails, although
the mean `CP_1` is positive in this row.

Raw coefficient signs fail at every rank.  The merged-only exterior chord
`(1,2k)` gives a positive raw atom, while the separate-only chord `(0,1)`
gives a negative raw atom, in both channel-one and channel-two direct
coefficient sums.  The channel-two second edge `(1,2)` remains internal
after either cut.  Hence no atomwise-positive factorization can prove CP;
full completion-weight cancellation is essential.

## 5. Exact finite falsification and its limits

The predeclared exact M161 evaluation at `k=9` retains all 24 lags and the
full `T/D` by `IS/IN/X` decomposition.  Every rational score is strictly
positive.  The minimum is at `y=k-2=7`:

```text
z_9(7) approximately 0.005999872316550588,
triangle contribution approximately +0.010948178900420163,
double contribution approximately   -0.004948306583869577.
```

Thus k=9 does not refute OS+, but the sign requires cross-kind cancellation.

At `k=3,5`, all 18 capped lags have both exact channel values `CP_j`
positive (36 channel values total).  The smallest
weighted values `alpha_j CP_j` are recorded exactly in the proof note and
raw JSON.  These finite facts do not prove CP, OS+, or MS.  No higher-rank
scan was run.

## 6. Dependencies and status labels

- **Accepted proved inputs:** M91/M94/M100; M161/M166; M168/M171;
  M174/M178; M261/M264; M266/M268; and M267/M270 where the literal owner
  representation is discussed.  Every named checksum inventory passes.
- **Proved exact here:** PCS makes MS equivalent to FCL1; the direct
  fully recombined CP formulas and implication hierarchy; arbitrary-rank
  sign-indefiniteness of their raw ordered atoms.
- **Refuted exact here:** termwise `(MON)` and scalar response `(FOSD)`.
- **Exact finite only:** OS+ through the retained `k=9` row and channel
  positivity at `k=3,5`.
- **Unresolved:** CP, OS+, MS, FCL1, every other fixed cell, direct L1/H0,
  all bridge/sampler gaps, polynomial mixing, and both Terminals.

## 7. Commands and reproducibility

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_exact.py --k 9 --output experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/exact_sign_k9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/check_monotonicity.py --output experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/monotonicity_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`.  The
second checker imports the frozen M91 exact auditor only to reuse its
accepted quotient and normalized conditional-law constructors.  It verifies
the four recombined blocks sum exactly to the direct two-step score.

## 8. Final action

**FREEZE THE EXACT MS EQUIVALENCE, DIRECT CP HIERARCHY, MON/FOSD
REFUTATIONS, AND ARBITRARY-RANK RAW-SIGN FIREWALL FOR FRESH AUDIT.  KEEP CP,
OS+, MS, AND FCL1 OPEN.**

No gap, mixing, or Terminal inference is licensed.
