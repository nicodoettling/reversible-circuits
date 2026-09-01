# M72 fresh referee report on frozen M70

Date: 2026-08-12. Frozen source manifest SHA-256:
`a228779765477233a5f8051428b3c4ace8d8d71c4e0bf5ec118388cf39097b88`.
The manifest, theorem, and report hashes match their frozen values. This audit
writes only the M72 directory.

## 1. Exact claim and conventions audited

Permutations compose as `(pq)(x)=p(q(x))`; tuple products are left-to-right.
For `l>=3`, put `n=2l+1`, `m=2l=n-1`, `M=binom(n,2)`, and
`h=(0 1 ... n-1)`.  M70 studies the uniform minimal length-`m`
transposition bridge to `h`, not the identity bridge.

I audited the following frozen claims:

1. M67's additive witness has `O(l^-3/2)` Rayleigh quotient under the
   complete-pair chain `C_l`, aligned chain `B_l`, and half-lazy local
   fixed-endpoint chain `K^h`.
2. Every nonzero cyclic character sector has

   ```text
   R_B>=4/(M^4n^6),
   R_C>=8/(lM^4n^6),
   R_(K^h)>=1/(3M^4n^6),
   ```

   with a factor-four improvement on the witness sector `H_1`.
3. The whole Krylov closure of the witness lies in `H_1`, hence has an
   inverse-polynomial spectral floor.
4. The zero-frequency sector is the cyclic-orbit stationary-flow quotient;
   the finite parking-incidence ranks are `1,4,10,36,116` through `n=7`.

## 2. Independent proof audit

### 2.1 Centering, covariance, and Rayleigh denominators

The nontrivial cyclic character centers `f_i` and `F=sum_i f_i`.  M67's
two-position law gives the same real covariance `C` between every two
distinct pair coordinates and common variance `V`.  Therefore

```text
||F||^2=lV+2binom(l,2)C=lV[1+(l-1)C/V].
```

For a pair heat bath `P_(i,j)`, the untouched summands are measurable outside
the refreshed coordinates, so

```text
||(I-P_(i,j))F||^2
 <=||f_i+f_j||^2=2(V+C).
```

This yields the frozen `C_l` and `B_l` denominators exactly.  For a raw window
of length at most five, at most three aligned pair coordinates intersect it,
including partially intersected endpoint pairs.  The same projection
contraction gives `3V+6C`.  Each of the three normalized block scans has
coefficient `1/6` in the half-lazy kernel, so their total retained coefficient
is `1/2`; M70's `K^h` numerator and denominator are correct.  Since M67 gives
`C/V>=c/sqrt(l)` eventually and Cauchy--Schwarz gives `C/V<=1`, all three
Rayleigh quotients are `O(l^-3/2)`.

### 2.2 Full twist and heat-bath comparison

Applying

```text
sigma_i(a,b)=(b,bab)
```

successively from left to right moves the first factor through the suffix.
For suffix product `q=t_2...t_m=t_1h`, its final value is
`q^-1t_1q=h^-1t_1h`.  Hence

```text
delta=sigma_1...sigma_(m-1):
(t_1,...,t_m)->(t_2,...,t_m,h^-1t_1h),
delta^m=mathcal U.
```

The full word has exactly `m(m-1)` letters and each index occurs `m` times.
For the Koopman fiber permutation `S_i` and conditional heat-bath projection
`R_i`, `(S_i-I)R_i=0` and `||S_i-I||<=2`.  Thus

```text
||(S_i-I)Phi||^2<=4<Phi,(I-R_i)Phi>.
```

Telescoping the full twist and using the exact occurrence count gives

```text
R_(L_n)(Phi)>=sin^2(2pi k/n)/[m^2(m-1)^2].
```

The Koopman-order reversal, if one writes transformations as formal operator
products rather than sequential instructions, only reverses the displayed
word and cyclic character; it changes neither length, multiplicity, nor sine
modulus.  The frozen text also proves the sequential state identity directly.

### 2.3 Full-state macro-changing H4 padding

This point does not rely on M27's fixed-multiset spectral theorem.  For every
off-diagonal raw-adjacent heat-bath edge `x->y`, the changed adjacent pair is
unique and has the same product.  An aligned four-window containing it exists
at every boundary: use start `i` for an interior odd start, `i-1` for even
`i`, and `m-3` for the final pair.  Keeping the two padding factors fixed
places the literal target `y` in the same H4 fiber even if its parking macro
changes.  Therefore

```text
B_l(x,y)>=1/[(l-1)M^4].
```

Minimality makes the raw pair product a 3-cycle or double transposition, with
fiber size three or two, hence

```text
L_n(x,y)<=1/[2(m-1)].
```

With `m=2l`, these imply the deliberately weaker pointwise domination
`B_l(x,y)>=M^-4L_n(x,y)`.  It holds for every directed edge, so the common
uniform stationary law gives the claimed Dirichlet-form comparison without a
path or congestion argument.

### 2.4 Remaining constants and cyclic quotient

Because `n` is odd, the characters `omega^(2k)` exhaust all cyclic
characters.  For `k!=0`,
`|sin(2pi k/n)|>=sin(pi/n)>=2/n`; on `H_1`,
`sin(2pi/n)>=4/n`.  Combining this with `m,m-1<n` gives exactly the frozen
`B_l` constants.  The retained adjacent pair projections have coefficient
ratio `2/l` from `B_l` to `C_l`.  Each aligned H4 projection has coefficient
`1/[6(2l-3)]` in `K^h` and `1/(l-1)` in `B_l`, so the exact ratio is
`(l-1)/[6(2l-3)]>=1/12`.  All displayed lower constants follow.

Every chain commutes with simultaneous conjugation, so the finite Krylov span
of `F in H_1` stays in `H_1`.  A nonidentity power of an odd long cycle has
only odd cycles of length at least three, hence fixes no two-element support
set.  The cyclic action on factorization words is free.  Dénes' count then
gives `n^(n-3)` equal-size orbits, and averaging transition mass over an orbit
gives exactly M70's stationary-flow quotient formula.

Finally, the incidence matrix used in the bounded diagnostic has rows
`#{q:d(mathcal U^q w)=d}` and columns indexed by feasible parking macros.  Its
rational rank is exactly the dimension of the cyclic projection of the macro
function space.  The code uses exact `QQ` rank whenever the modular rank is
not full, so the ranks `1,4,10,36,116` are exact finite facts.

## 3. Probability, runtime, path, and congestion accounting

- Full-twist path length is exactly `m(m-1)`; each raw index occurs `m` times.
- The only unitary-to-heat-bath loss is the exact squared-norm factor `4`.
- One padded aligned transition has scan probability `1/(l-1)` and output
  probability at least `M^-4`; no canonical hub or multicommodity congestion
  is used.
- The direct comparison coefficients are exactly `2/l` and at least `1/12`.
- Fixed block enumeration has at most `M^5` candidates and is polynomial.
- Independent `n=7` reruns complete in seconds.  Their finite eigenvalues are
  not used as proof.

## 4. Dependencies

- **Proved/accepted:** M67 v4 correlation theorem and its fresh ACCEPT report;
  frozen hashes in M70 match.
- **Proved in frozen M70 and independently checked here:** all projection,
  twist, full-state padding, comparison, free-action, and quotient steps.
- **Cited standard:** Dénes' enumeration, used only for the orbit count.
- **Exact finite:** state/fiber/rank arithmetic in the two reruns.
- **Empirical only:** floating Krylov eigenvalues.
- **Open and not assumed:** any gap on `H_0` or lift to original identity `K`.

## 5. First unproved standalone step

> **CYCLIC-ORBIT INCIDENCE GAP.**  The exact stationary-flow cyclic-orbit
> quotient of `C_l` or `B_l`, including its nonconstant parking incidence
> laws `nu_O`, has inverse-polynomial gap in `n=2l+1`.

## 6. Strongest self-attack

The full twist is completely blind to `H_0`; no amount of improving its
polynomial constants addresses that sector.  The exact rank `116` at `n=7`
also rules out treating cyclic averaging as annihilation of the rooted parking
macro.  Moreover, the fixed long-cycle endpoint is not a closed prefix sector
of the identity chain under boundary-crossing local windows.  Thus neither the
polynomial lower sector bound nor the slow Rayleigh witness lifts to Terminal
A or B without new stationary-mass and boundary-flow control.

## 7. Calibration and independent reruns

- `l>=3` ensures `m>=6` and all block sizes `{3,4,5}` exist.  `m=2` and the
  special `m=4` whole-word H4 case are outside the statement and explicitly
  excluded.
- Odd identity length, `m=0`, `N=2`, and the `S_3/S_4` identity calibrations
  are not changed by this nonidentity minimal bridge theorem.
- Every state is a reduced long-cycle factorization, so its support graph is
  a tree and its factor edges are distinct.
- Independent `n=7` rerun: the full twist agrees with conjugation on all
  `16807` states; all `120050` directed raw-pair edges satisfy the padded H4
  relation; minimum exact `B/(M^-4L)=194481/25`.
- All mathematical JSON fields of the Krylov rerun equal the frozen output;
  only elapsed time differs.  The independently rerun H0 JSON is byte-for-byte
  identical, SHA-256
  `a9ed1ef7fb2ff4eba9051536e34f46952f22978475f002e13426c213f0e517d4`.

## 8. Artifacts and commands

- `plan.md`
- `m70_n7_rerun.json`
- `m70_h0_rerun_n7.json`
- `report.md`

Commands:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/n7_exceptional_krylov.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M72-m70-fresh-referee/m70_n7_rerun.json
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/h0_parking_projection.py --n-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M72-m70-fresh-referee/m70_h0_rerun_n7.json
```

No seed; both enumerations are deterministic. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

**ACCEPT**

Numbered objections: none.  M70 proves the scoped polynomial sandwich on the
entire nonzero-frequency exceptional closure with correct normalizations and
scope.  It is a valuable nonterminal theorem, not Terminal A or Terminal B.
