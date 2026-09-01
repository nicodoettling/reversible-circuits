# M233 fresh immutable referee report

Date: 2026-08-13 UTC.

## Verdict

```text
FINAL VERDICT ON M230 CORRECTED SALVAGE: ACCEPT.
MATERIAL OBJECTIONS TO M230: NONE.
NONMATERIAL OBJECTIONS TO M230: NONE.

M227 DISPOSITION: REJECT AS A SELF-CONTAINED FROZEN PROOF.
```

M230 correctly identifies the material gap in frozen M227 and supplies a
valid exact repair. The accepted result is only the corrected
full-seven-dimensional one-atom theorem `p_1>p_2>1/4`; the optima themselves
and every uniform or recursive consequence remain open.

## 1. Immutable-source verification

M230's seven `SHA256SUMS` payloads all pass. The independently computed
checksum-ledger digest is

```text
5e9e0b59490a64dec97738127f0d2060187f062598d527e3b6cbbb47378b96d3.
```

The directory inventory is exactly those seven payloads plus `SHA256SUMS`.
M230 and M227 remained immutable throughout this audit.

## 2. Clean-room reconstruction

The standalone checker imports and reads no predecessor code or data. Direct
beta integrals reconstruct

```text
integral b_i b_j
 = C(6,i)C(6,j)(i+j)!(12-i-j)!/13!,
integral (u-1/2)b_i(u)du=(i-3)/56,

G_ij=integral b_i b_j
     -12 integral (u-1/2)b_i integral (u-1/2)b_j.
```

Multiplication by `b_(1,0)` followed by exact degree-two-to-six elevation
reconstructs

```text
e=(1,5/6,2/3,1/2,1/3,1/6,0),  M=ee^T,
<G,M>=1/4.
```

## 3. Material M227 gap independently confirmed

Deleting coordinate 6 because `e_6=0` does not preserve the primal
objective. A particularly direct witness is

```text
C=M+e_6 e_6^T.
```

It PSD-dominates `M`, and the added term has bandwidth zero, but restricting
to coordinates `0,...,5` removes the strictly positive objective contribution

```text
G_66=433/10192.
```

Thus M227's claimed restriction equality is false. Its six-dimensional dual
matrices are likewise not, without completion, feasible for the declared
seven-dimensional duals. M230's `M-1` classification is correct and
material; frozen M227 is rejected as a self-contained proof.

## 4. Exact seven-dimensional dual repair

For bandwidth one, the checker independently verifies

```text
y_1=(869/1494) Xbar_1[:,5].
```

The resulting `7 x 7` matrix equals `G` on every entry with `|i-j|<=1`, is
positive definite, and has final `LDL^T` pivot

```text
25/747>0.
```

For bandwidth two, it independently verifies

```text
y_2=(-43/54) Xbar_2[:,4]+(419/324) Xbar_2[:,5].
```

This satisfies the two clique equations at `(4,6)` and `(5,6)`, equals `G`
on the complete width-two band, is positive definite, and has final pivot

```text
97/3564>0.
```

All six inherited pivots are strictly positive in each case. The exact
matrix digests reproduce as

```text
w=1 73f302213b3de78b2da2b4bba7968d59c2fab0aa93a2f6548be13ac02ec4f6d6
w=2 4d70d7645a7f74443a2c7c575279cfc065e794512bc588323607b5b8ebdb7190
```

Since `e_6=0`, both completions preserve the active six-dimensional dual
objectives exactly.

## 5. Primal certificates, brackets, and strict conclusions

Zero-extending each six-dimensional primal yields a full bandwidth-`w`
matrix. Its slack is the direct sum of a positive-definite six-dimensional
slack and a zero coordinate. The checker reproduces every positive active
slack pivot and obtains

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,
167478197/630630000 <= p_2 <= 894863807/3363360000.
```

Exact subtraction gives

```text
lower(p_1)-upper(p_2)=10951531/155232000>0,
lower(p_1)-1/4       =15605731/180180000>0,
lower(p_2)-1/4       = 9820697/630630000>0.
```

Therefore M230's corrected theorem `p_1>p_2>1/4` is proved for the declared
one atom. No exact optimum is identified.

## 6. Generic bookkeeping

The exact binomial elevation identity

```text
(E_(n,L)z)_r=sum_k z_k C(n,k)C(L-n,r-k)/C(L,r)
```

is verified and sends `zz^T` to the rank-one matrix
`(E_(n,L)z)(E_(n,L)z)^T`. For a surviving weight
`lambda=eta/pi_a>0`, multiplying both atom and certificate by `lambda`
preserves PSD domination and scales the linear objective. Applying the
envelope only to the pre-existing live-atom list creates no killed `a=d`
branch. None of these pointwise facts supplies aggregation or recursion.

## 7. Numbered objections and boundaries

1. **Material objections to M230:** none.
2. **Exact-certificate objections:** none.
3. **Conic-program objections:** none; the full symmetric Frobenius pairing
   and on-band constraints are consistent.
4. **Generic-bookkeeping objections:** none within the stated pointwise
   scope.
5. **Scope objections:** none. M230 explicitly excludes exact optima, a
   degree-uniform factor, aggregation, recursive closure/contraction,
   all-state control, spectral gap, mixing, and Terminal A/B.

## Reproduction

```text
python3 -B cleanroom_exact.py --output results.json
```

Python 3.12.3, standard-library exact `Fraction`, `seed=null`.
