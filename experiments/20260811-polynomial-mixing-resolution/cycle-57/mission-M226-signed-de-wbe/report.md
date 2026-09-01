# M226 report: signed WBE coefficient reduction

Date: 2026-08-13 UTC.

## 1. Verdict

STRICT EXACT SCALAR COEFFICIENT REDUCTION.

WBE and DE are not proved or refuted. They reduce to two explicit signed
prefix-moment lemmas, YCM and TCM. No DV, J2, PCR, gap, mixing, or Terminal
claim is made.

## 2. Immutable gate

Every file in M192/M195, M199/M207, M211/M215, and M217/M222 passed its
frozen checksum inventory before use. No predecessor was edited.

## 3. Exact one-run reduction

M226 combines the surviving and fragmentation coefficients before any
absolute value. The full B coefficient of `F_ell(x)` is the exact scalar
`G_k(x)` in `wbe_scalar_reduction.md`. Applying the two-seam incidence law
gives closed `B^Y_{k,y}` coefficients, while convolution of all four A
sources gives

    A^Y_{k,y}=
      [2b_y b_(k-y)/(R b_k)]
      [(k-y)+(k-y-1)(k-y-2)/(k-1)]

for `y<k`. Therefore

    S_Y+K_Y=sum_(y=2)^ell(B^Y_{k,y}-A^Y_{k,y})

exactly. This is a one-dimensional Borel coefficient problem.

## 4. Exact two-run reduction

The difference between X and Y is exactly the signed q-averaged B-minus-A
prefix mass of the unique complementary two-run face. It retains every
kind, seam, and collision multiplicity. Thus one more signed scalar moment,
TCM, suffices together with the one-run moment YCM.

## 5. Standalone open lemmas

- YCM: the explicit one-run coefficient prefix is at most
  `C sqrt(ell)/k`.
- TCM: the exact signed two-run coefficient prefix is at most
  `C sqrt(ell)/k`.

YCM+TCM imply WBE for both observables. Neither is claimed here.

## 6. Regimes and failed shortcut

The accepted macroscopic split tail is target-sized when `ell` is comparable
to `k`. For fixed/small `ell` it is too weak, so YCM/TCM cancellation is
essential. A proposed unsigned two-run placement bound
`4 min(ell,a)` is exactly false: at `k=5`, B split `s=2`, parent `7`, child
size `1`, and `ell=7`, there are five qualifying placements rather than
four. This blocks that absolute route but does not refute TCM or WBE.

## 7. Diagnostics

The standard-library exact checker verifies the Y coefficient identities for
odd `k<=15`, and literal X/Y coefficient identities for `k=3,5,7`. Coefficient
signs change, refuting a simple sign argument. The largest displayed scaled
prefixes are about `0.519` for Y and `0.487` for literal X. These are finite
calibration only.

## 8. Action

Freeze the exact reduction and request a fresh immutable audit of (2.1)--
(2.6), the X-minus-Y two-run identity, the exact `k=5` shortcut witness, and
the sufficiency of YCM+TCM. Keep WBE, DE, and every excluded downstream
statement open.

